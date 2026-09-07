# [B33] item (1)+(2) — the clang compile-only gate, made repeatable

Lane `b33cc`, 2026-09-07. Sonnet.

## Deliverable (1): the compile-only gate script

`docs/dev/measurements/probe_cc_gate_census.py`, wired as `make
cc-gate-census`.

### Reading "3 modes x 2 forms" — corrected from the brief

The brief's own reading ("the '3 modes' are this project's regime tokens
`match`/`search_short`/`throughput`, see `REGIME_MODE`") does not survive
contact with the code, and the brief itself asked for this to be checked
before writing new enumeration logic. Two problems with the regime-token
reading:

1. `pcrecbench.subbench.REGIME_MODE` maps THREE regime tokens onto only
   TWO match semantics (`match`, `search`) and says nothing about pcrec's
   engine selection. Crossing regime x form would either (a) duplicate
   the exact same plain-form compile for `search_short` and `throughput`
   (both resolve to the same PLAIN artifact per
   `testees/pcrec/CLAUDE.md`'s "search_short and throughput use the PLAIN
   artifact"), or (b) need ad hoc per-set filtering by declared regimes
   for no reason tied to what pcrec actually compiles.
2. It cannot explain the ORIGINAL a7e0bdf census's own finding: "50 of
   264 cells refuse under clang with ONE cause -- a frameless VM
   artifact['s]... indirect goto". A frameless VM artifact only appears
   where the VM is FORCED or auto-selects broadly across the corpus --
   nothing about which REGIMES a set declares would produce that
   population.

This project has ALREADY used "3 modes x 2 forms" for a full-corpus
census once before, and there "mode" unambiguously means pcrec's three
ENGINE CONFIGS: `testees/pcrec/CLAUDE.md`'s [B26] entry states "the
whole `RX_ENGINE_SEL` census -- 77 patterns x 2 forms (plain,
`(?:...)\z`) x 3 ENGINE MODES (auto, nocaps, vm) = 462 cells per pin".
`tools/selfcheck.py`'s `check_cc_axis`/`CC_KIND_CASES` (the [B24] lane's
OWN check) also pairs `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm` against
their `-clang` siblings -- the same three names. This is the reading the
script implements: MODE = `auto` / `nocaps` / `vm` (the FLAGS of
`pcrec-auto`/`pcrec-nocaps`/`pcrec-vm`, read from
`testees/pcrec/configs.toml`, never retyped), FORM = `plain` /
`whole-subject`.

### What it does

Per (subbench, pattern, mode, form) cell: emit-c ONCE via the pin's
pcrec binary (pcrec's own C output does not depend on which C compiler
will consume it -- only on the FLAGS the mode picks and the pattern TEXT
the form picks, so running it twice per compiler would be pure waste);
if pcrec itself refuses (a real `did-not-compile` -- a size cap, the NFA
cap), ONE row records that refusal for both `gcc_result` and
`clang_result` (neither compiler ran, so there is nothing to diverge on
there); otherwise gcc and clang each compile the SAME
one-translation-unit shim+artifact command
`testees/pcrec/adapter.py`'s phase 2 uses. No phase 3 (no dlopen, no
driver, no match run), no timing regime beyond the wall clock printed
per row for a reader's sense of where time went, no quiet-box gate.

The gate's PASS condition is `gcc_refusals == clang_refusals` (compiler-
level refusals only, as a set of cell keys) -- exit 0 on parity, 1 on a
divergence, which is printed under `# DIVERGENCE:` naming every
gcc-only and clang-only cell. A divergence would be a finding for the
outbox, never silently patched here.

Patterns are enumerated by `subbench_dirs()` (mirroring
`tools/selfcheck.py`'s own rule verbatim: every `bench/<name>/` with a
`subbench.toml`, sorted, by discovery) x every `Subbench.patterns` in
sidecar order -- the harness's own loader, never a second parser.

### Cell count, gcc/clang refusal sets

Enumerated at pin **d34c9131**: **185 patterns** across five sub-benches
(altwide 33, bounded 43, email 3, loglines 11, syntax 95) x 3 modes x 2
forms = **1,110 cells**.

Validated per-sub-bench BEFORE committing to the combined run (so a bug
in one set's patterns could not burn the whole sweep's wall-clock):

| sub-bench | cells | pcrec refusals | gcc refusals | clang refusals | wall |
|---|---|---|---|---|---|
| email | 18 | 0 | 0 | 0 | 8.3s |
| bounded | 258 | 4 (`cls-upto-65535`, NFA cap) | 0 | 0 | 153.0s |
| loglines | 66 | 0 | 0 | 0 | 29.8s |
| altwide | 198 | 86 (size caps, both routes) | 0 | 0 | 409.2s |
| syntax | 570 | 87 | 0 | 0 | 178.5s |
| **sum** | **1,110** | **177** | **0** | **0** | **~779s serial** |

The five subset counts sum to exactly 1,110 -- the full 185 x 3 x 2
enumeration, confirmed complete by arithmetic, not assumed.

**gcc and clang refusal sets are BYTE-IDENTICAL: both empty (0
compiler-level refusals in the whole corpus).** Every one of the 177
`did-not-compile` cells is a PCREC refusal (a size cap, the NFA-state
cap, or a feature-gate message such as syntax's `xcl-minus` --
`"module 'extended-classes' is enabled but (?[...) is not implemented
yet"` -- firing before either compiler runs), recorded identically on
both sides by construction, so none of them contributes to either
compiler's refusal set.

**Combined single-invocation run** (the archived file,
`docs/dev/measurements/2026-09-07-cc-gate-census-d34c9131.txt`, 1,119
lines: 5-line source header + 1-line count/column header + 1,110 data
rows + a 2-line summary footer): **1,110 cells, 177 refused (pcrec
emit-c), gcc refused 0, clang refused 0, wall 778.4s. PARITY: gcc and
clang refusal sets are byte-identical (0 cells each).** This matches the
five-subset sum (1,110 cells, 177 pcrec refusals, 0/0 compiler refusals)
exactly -- the combined run is the same enumeration in one process, not
a different sample, and confirms it byte-for-byte rather than merely
by count.

This CONFIRMS at d34c9131 what [B26]'s 1989c62 re-pin already found (the
clang refusal set going empty once pcrec's abi-14 [CC-CLANG] fix
landed): the [CC-CLANG] fix holds across five more re-pins and a much
larger corpus (1,110 cells here vs. 462 in the [B26] census, now
including altwide and syntax, neither of which existed at a7e0bdf).

### Wall-clock and the check-harness-vs-standalone decision

The combined sweep took **778.4s (~13.0 minutes)** for 1,110 cells,
running alone on a quiet-ish box (load ~1.0-1.7 during the earlier
per-set rehearsals; the combined run itself finished cleanly while
`make check-harness` ran concurrently in this same session -- see
Validation below). `make check-harness`'s own stated budget is
~20 minutes for the whole harness contract; this sweep alone is nearly
that on its own for a COMPILE-ONLY census that touches no schema, no
store and no driver -- so it is a
**STANDALONE target, `make cc-gate-census`**, run at re-pin time
alongside the `list_axes.tsv`/`list_definitions.tsv`/`list_limits.tsv`
re-archive convention (`testees/pcrec/CLAUDE.md`'s "re-archive at every
re-pin" rows), never bolted onto `check-harness`'s own runtime. This
matches the brief's own steer: `check-harness` is the SMOKE suite
(`--trials 1 --iters 1`, minutes, not a measurement); a full compile-only
sweep over every pattern x mode x form at TWO compilers is not that.

### Where it lives, how it's invoked

- `docs/dev/measurements/probe_cc_gate_census.py` -- the script, in the
  same directory and following the same conventions as every other
  archived probe here (`probe_altwide_size_census.py` is its direct
  template: `--pin` resolves via `pin.sh --path`, never builds; a
  `--dry-run` that prints every argv untouched; a stable dated archive
  filename under a source header).
- `make cc-gate-census` (root `Makefile`) -- resolves the pin from
  `testees/pcrec/configs.toml` (never retyped), writes to a dated file
  under `docs/dev/measurements/` by default, `ARGS="..."` passes extra
  flags through (e.g. `make cc-gate-census ARGS="--subbench email"` for
  a quick rehearsal).
- `docs/dev/measurements/2026-09-07-cc-gate-census-d34c9131.txt` -- the
  archived output, source-headed, one row per cell (subbench, pattern,
  mode, form, gcc_result, clang_result, diagnostic).

## Deliverable (2): the timed clang arms stay on-demand

Verified, no code change needed. `scripts/run_suite.sh`'s default
`SUITE="bounded loglines email"` never names a `:clang` label; the
`:clang`/`:clangrerun` suffix is documented in the script's own header
comment as "a LABEL, nothing else" -- it only runs when a session
explicitly writes it into `$SUITE` (e.g. the historical
`bounded:clangrerun` one-off ask, `TESTEES_bounded_clangrerun` set by
hand). `scripts/CLAUDE.md`'s own cell-length table already documents
clang cell costs (`auto-clang` 49.4 min on bounded@0.3) precisely
because they are NOT part of the default nightly order and need their
own budget line when someone opts in. No new timed-clang tooling was
built (out of scope, per the brief -- item (3), I-37's periodic-clang
ask, is explicitly left for the next lane).

## Validation

- `make check-schema`: **4 example(s) accepted, 72 sabotage(s) rejected
  for the intended rule, 0 sabotage(s) WRONG** (`4/72/0`, unchanged --
  this lane touches no schema file).
- `make check-harness`: **337 check(s) passed, 0 FAILED** (run
  concurrently with the combined cc-gate sweep above, both completed
  clean -- this lane adds no check function, only a standalone probe
  script under `docs/dev/measurements/`, so the count is whatever this
  worktree's base commit already carried; not something this lane
  moved).
- `probe_cc_gate_census.py` run for real against d34c9131, both as five
  independent per-sub-bench subsets (table above, run first as a
  cheaper correctness rehearsal) and as the single combined invocation
  that produced the committed archive file (1,110 cells, 778.4s,
  PARITY). Exit code of the combined run: **0** (refusal-set parity).
- No leftover `build/cc-gate-census-*` tempdirs after either the subset
  runs or the combined run: the script's own cleanup path
  (`shutil.rmtree` on its tempdir, gated on `cleanup` -- only skipped
  when `--workdir` is passed explicitly) ran in every invocation;
  confirmed by listing `build/` after the combined run finished.

## Do-not-touch confirmed

No pcrec source read from anywhere but `~/pcrec` (read-only, via the
pin's build under `build/pcrec-d34c9131/`, never written to); no
`store/` record produced (every compile here stops before phase 3 --
no dlopen, no driver, no match run, so nothing here is a `pinned` or
`scratch` record); no timed-clang re-run tooling built (item 3 left for
the next lane).

Numbers inline above; log paths:
`/tmp/claude-1001/-home-duxevents-pcrec-bench/a7d9b911-1584-43fd-9823-65fc4e8c5e10/scratchpad/{email,bounded,loglines,altwide,syntax,full}_cc.log`
(session-scratchpad, not committed -- the committed archive is the
combined run's own output file).
