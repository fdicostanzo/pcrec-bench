# lane b117prep report — the compilee optimization-level sweep, PREP

**Branch**: `lane/b117prep`, worktree `worktrees/b117prep`, from master
`9bf8211` (the manager's own "[B117] prep started" commit). Box shared
with pcrecdev1's two back-to-back `make test` runs (U2, then S3+K67);
this lane did LIGHT work only throughout (`uptime`/`pgrep -a make`
checked before every heavier step) and never ran `make check`,
`make check-harness` in full, or the census in full.

## 1. Findings first

1. **The mechanism [B117] predicted DOES reach real codegen, on a real
   witness.** `check_olevel_axis`'s arm 3: `a(b|c)+d` forced under
   `--engine=vm`, `.so` `.text` section 21,877 B at `-O0` vs 12,343 B at
   `-O3` (-43.6%) — the override is not merely textual, it changes what
   gcc actually emits.
2. **Two ad hoc sanity runs of the census script (2-3 patterns each,
   through the REAL adapter, never the checked-in production population)
   give the FIRST real signal on the DFA-vs-VM direction the charter
   asks about**, and it points the way the plan row's own reasoning
   expected:
   - `ipv4-near-miss` under `pcrec-auto` (a DFA-route pattern): `.so`
     bytes and `.text` bytes IDENTICAL at `-O2` and `-O3` (32,688 /
     17,213 B both) — the table-walk route reading FLAT under a higher
     `-O` level, as P2 of the predictions file states.
   - The SAME pattern forced under `--engine=vm`: `-O0`'s `.so`/`.text`
     (35,952 / 21,474 B) is measurably LARGER than `-O2`'s (27,528 /
     15,463 B), while `-O3`'s (27,488 / 15,551 B) sits within a few
     hundred bytes of `-O2` — the VM/goto-dispatch route reading
     SENSITIVE to the floor arm and roughly flat at the ceiling, as P4/P5
     of the predictions file state.
   - Answer identity held on every sanity cell (0 mismatches) — no sign
     of an optimization-level codegen bug on these two witnesses.
   - These are TWO-PATTERN sanity runs to prove the script correct, never
     a corpus reading — the full 640-cell census is OWED (§3).
3. **`build_flags` did not name the EFFECTIVE optimization level before
   this lane**, exactly the gap the brief asked to check for: the
   pre-existing `cflags` clause said "the artifact+shim compile also
   carries -O3 ... appended after -O2 -fPIC -shared", which states the
   ARGV but leaves "so what level does it actually run at" to a reader's
   own memory of gcc/clang's last-flag-wins precedence. Fixed with a
   small, self-contained addition (`effective_olevel()` +
   a named "EFFECTIVE OPTIMIZATION LEVEL" clause) rather than a bigger
   rework — see §2.1.

## 2. What was built

### 2.1 Eight configs + the honesty clause (deliverables 1-2)

`testees/pcrec/configs.toml`: `pcrec-auto-o0`/`-o1`/`-o3`/`-os` and
`pcrec-vm-o0`/`-o1`/`-o3`/`-os`, each `pcrec-auto`/`pcrec-vm` plus ONE
`cflags = ["-O<n>"]` entry — `pcrec-auto-align64`'s own shape exactly.
No `-o2` config exists: `pcrec-auto`/`pcrec-vm` themselves ARE this
axis's `-O2` arm (a `pcrec-auto-o2` testee would derive the identical
artifact and collide with its own sibling in the store). Thirty-nine
pinned pcrec configs now (was thirty-one).

Derived ids verified directly (`python3 -m pcrecbench testees` /
`Adapter.describe`):

    pcrec-auto-o3  -> pcrec_a32bc86e_auto-caps-simdna_cf-o3
    pcrec-vm-os    -> pcrec_a32bc86e_vm-caps-simdna_cf-os

Every PRE-EXISTING testee_id is unchanged: `python3 -m pcrecbench
testees` lists 39 (31 + 8, matching `git show HEAD:testees/pcrec/
configs.toml | grep -c '^\[testees\.'` = 31 on the parent commit), and a
scripted sweep over every non-`-o0/-o1/-o3/-os` testee found the new
"EFFECTIVE OPTIMIZATION LEVEL" clause on NONE of them.

`testees/pcrec/adapter.py`: `effective_olevel(cflags)` (picks the LAST
`-O<n>` flag in a `cflags` list, mirroring gcc/clang's own precedence —
tested on a two-`-O`-flags case a `configs.toml` row never produces but
a `pcrec-local` caller's `$PCREC_LOCAL_FLAGS` could); wired into the
existing `cflags_note` construction so `build_flags` reads, e.g.:

    ...; COMPILEE FLAGS ([B35], pcrec I-39 (v)): the artifact+shim
    compile also carries -O3 -- OUR OWN phase-2 flags, appended after
    -O2 -fPIC -shared, never passed to pcrec; ...; EFFECTIVE
    OPTIMIZATION LEVEL ([B117], Frank 2026-09-29's compilee
    optimization-level sweep): gcc and clang both take the LAST -O flag
    on the command line, so the fixed -O2 above is OVERRIDDEN -- this
    artifact is actually compiled at -O3

Inert on every config with no `-O` flag in `cflags` (`pcrec-auto-align64`
etc. — checked directly, no clause added).

### 2.2 The proof arm: `check_olevel_axis` (deliverable 3)

`tools/selfcheck.py`, wired into `make check-harness`'s `main()` right
after `check_cflags_axis()`. Six checks, run standalone (never as part
of a full `make check` while the box was busy):

1. the eight configs' `cflags`, derived id and the NAMED effective-level
   clause;
2. `effective_olevel()` itself over six cases incl. the two-`-O`-flags
   last-wins shape and a non-`-O` cflags list (`None`);
3. **THE REAL PROOF**: compiles `a(b|c)+d` under `pcrec-vm-o0` and
   `pcrec-vm-o3` with a `subprocess` spy (the SAME technique
   `pcrec-auto-align64`'s own arm 3+4 uses) — the flag reaches the REAL
   gcc argv AFTER the fixed `-O2`, is ABSENT from pcrec's own argv, and
   the two `.so` objects' ELF `.text` sizes DIFFER (21,877 vs 12,343 B) —
   the control that the override is not merely textual;
4. the CLI lists all eight configs, and `pcrec-auto-o3` still answers
   the pure-DFA smoke pattern (`foo[0-9]+bar`) by the libpcre2 oracle,
   both forms — an optimization flag that broke codegen would otherwise
   pass as a speed change, the same control `pcrec-auto-align64`'s own
   arm 4 runs.

Standalone run (email subjects generated first — a pre-existing
environment gap in the fresh worktree, unrelated to this lane, fixed by
running `bench/email/gen_subjects.py`/`gen_throughput_subjects.py`):

    check_cflags_axis: PASS 10 FAIL 0
    check_olevel_axis: PASS 6 FAIL 0
    check-schema:      6 example(s) accepted, 74 sabotage(s) rejected, 0 wrong

### 2.3 The bench/capability roster (deliverable, [B111]'s gate)

Every new testee id needs an `EXT_BENCH_ROSTER` row or an
`EXCLUDED_TESTEES` entry in the same commit ([B111]). Added eight
roster rows (`bench/capability/gen_patterns.py`), each declaring
EXACTLY its base's (`pcrec-auto`/`pcrec-vm`) own token set — `cflags`
rides on THIS PROJECT's own phase-2 `$CC` compile only, never reaching
pcrec's parser, the identical reasoning `pcrec-auto-align64`'s own
roster row already states. Regenerated `patterns.rxt`
(`python3 bench/capability/gen_patterns.py`); `--check` clean. Diff is
exactly the roster line (+8 ids) and eight new `capabilities
pcrec-*-o<n>` blocks, byte for byte the base testee's own block.

    check_capability_roster_coverage: PASS 4 FAIL 0 (44 roster, 12 excluded)
    check_capability_policy:                PASS 7 FAIL 0
    check_capability_policy_noop_elsewhere: PASS 6 FAIL 0

### 2.4 Predictions (deliverable 5)

`docs/dev/predictions/capability-0.1-b117-olevel-a32bc86e.tsv`, 7
falsifiable clauses, loaded and validated through
`pcrecbench.interpret.load_predictions` before committing:

- P1-P3: the DFA/table-loop route (`pcrec-auto`) predicted FLAT (within
  ±15%, a band deliberately WIDER than any same-pin cross-testee
  null-control this project has computed, since none exists for this
  specific pair) at `-O0`, `-O3` and `-Os` — the hot loop is a
  table-indexed byte walk with little for the compiler's own scheduling/
  inlining passes to move.
- P4-P6: the VM/goto-dispatch route (`pcrec-vm`) predicted MEASURABLY
  SLOWER at `-O0` (>15%) and `-Os` (>5%), and NO WORSE at `-O3` (≤5%,
  one-sided — a win is not itself a surprise) — the dispatch loop is
  exactly the straight-line, schedulable/inlinable shape `-O0`/`-Os`
  cost the most on and `-O3` should help most.
- P7: a compile-side `.so`-size clause on the DFA route's `-O0` arm,
  citing this lane's own two-witness sanity finding (§1.2) as the
  single-witness precedent it generalises.

All seven predate any store measurement of these testees (none exists
yet), so `stated_utc` trivially precedes the population.

### 2.5 The census script (deliverable 4) — BUILT, NOT RUN IN FULL

`docs/dev/measurements/probe_b117_olevel_census.py`: every compiling
`bench/capability` pattern (read via `pcrecbench.subbench.find`, never
retyped) × {auto, vm} × five levels (o0/o1/o2/o3/os), plain form only,
through the REAL adapter (`Adapter.prepare`/`compile`/`measure` — never
a hand-rolled gcc/driver invocation, so its numbers are the SAME
measurement a future window's own compile-cost column would show).
Records per cell: phase-2 (`gcc`) wall time, `.so` whole-file size,
ELF `.text` size (`size`, binutils), `emit_bytes`/`emit_code_bytes` (for
contrast — pcrec's OWN size definition, provably unmoved by `cflags`),
and answer identity against the level's own `-O2` build over every
`search_short` subject (`matched`/`start`/`end`, subject by subject).

`--dry-run` verified: 640 cells (64 patterns × 2 engines × 5 levels).
Two SANITY runs (§1.2) — `--limit 1`/`--limit 2`, `--jobs 1`/`2` —
confirmed the script end to end (compiles, measures, diffs, writes a
well-formed TSV) at negligible cost (2-12 cells, 0.6-3.8 s wall).

**THE FULL RUN IS OWED, NOT LAUNCHED BY THIS LANE** — per
`docs/dev/lanes/BOILERPLATE.md`'s 2026-09-25 rule ("a run longer than
~4 minutes is your LAST act... do NOT launch it yourself: the manager
launches it"). Estimated from the sanity runs' per-cell rate
(~0.6-1.3 s/cell serial-equivalent): 640 cells at `--jobs 4` ≈ 3-4
minutes best case, with real variance from the corpus's own slower
patterns (recursion, ReDoS-designed, atomic-group members) this lane's
2-pattern sample cannot bound — treated conservatively as over the
4-minute line.

    python3 docs/dev/measurements/probe_b117_olevel_census.py \
        docs/dev/measurements/2026-09-29-b117-olevel-census.txt

(no `$B117_SCRATCH` override needed — defaults to `/var/tmp/
b117scratch`, cleaned up by the script's own `TemporaryDirectory` use
per cell). Archive the printed `DONE rows written; compiled=N
refused=N answer_mismatches=N` line and the file itself as
`docs/dev/measurements/2026-09-29-b117-olevel-census.txt` (the plan
row's own named target). `answer_mismatches` should read 0; a nonzero
count needs investigation before any timing reading proceeds — it would
mean an `-O` level broke codegen correctness on a real corpus pattern
(the census's stated purpose is to CHECK that, corpus-wide, before
anyone trusts a number this axis produces).

### 2.6 Documentation

`testees/pcrec/CLAUDE.md` (opening count 31 → 39, new table row + a
mention in `adapter.py`'s file-role row), `testees/CLAUDE.md` (the
`pcrec/` row), `bench/capability/CLAUDE.md` (a `[B117]` roster-addition
paragraph in the established `[B101]`-style shape), `docs/dev/plan.md`
(the `[B117]` row's `STATE` and a prep-complete narrative).

## 3. Charter-vs-committed checklist (session_discipline.md §7(c))

| brief item | status |
|---|---|
| (1) configs `pcrec-auto-o1`/`-o3`/`-os` + `-o0`, and the same on `pcrec-vm` | COMMITTED — `testees/pcrec/configs.toml`, verified via `pcrecbench testees`/`describe()`, every pre-existing testee_id unchanged |
| (2) a check arm proving the effective level, + honesty of `build_flags` | COMMITTED — `effective_olevel()` + the named clause (adapter.py); `check_olevel_axis` (tools/selfcheck.py), 6/6, incl. a REAL `.text`-size differential on a live compile |
| (3) a compile-only census script, run if the box is free, archived | SCRIPT COMMITTED (`docs/dev/measurements/probe_b117_olevel_census.py`), `--dry-run` + two sanity runs verified. **THE FULL RUN IS OWED** to the manager (BOILERPLATE's long-run rule) — exact invocation above, target archive path `docs/dev/measurements/2026-09-29-b117-olevel-census.txt` |
| (4) predictions BEFORE any timing | COMMITTED — `docs/dev/predictions/capability-0.1-b117-olevel-a32bc86e.tsv`, 7 clauses, loaded and validated |
| a lane report with the exact `run`/window invocation | THIS FILE, §4 |
| [B111] roster gate (not in the original brief, but a same-commit MUST) | COMMITTED — `bench/capability/gen_patterns.py` + regenerated `patterns.rxt`; `check_capability_roster_coverage` 4/4 |

Also OWED (not this lane's scope, but named so the manager does not have
to re-derive it): the TIMED WINDOW itself — see §4.

## 4. The manager's window (once the box is quiet and the census above is clean)

Capability × the 8 new testees + `pcrec-auto`/`pcrec-vm` as the
same-window `-O2` control (the plan row's own instruction: "measured IN
THE SAME WINDOW, same-window control, not a cross-window compare"):

    SUBBENCH=capability \
    TESTEES="pcrec-auto pcrec-auto-o0 pcrec-auto-o1 pcrec-auto-o3 pcrec-auto-os pcrec-vm pcrec-vm-o0 pcrec-vm-o1 pcrec-vm-o3 pcrec-vm-os" \
    setsid scripts/run_window.sh > /dev/null 2>&1 &

Ten testees × 64 patterns × 2 forms × 2 regimes (`search_short`,
`throughput` — capability declares no `match`) is a real window; size
it against `scripts/CLAUDE.md`'s own per-cell cap table before launching
unattended. Rehearse first with `--dry-run`:

    SUBBENCH=capability TESTEES="pcrec-auto-o0" scripts/run_window.sh --dry-run

Read: set-grain ratios of each `-o<n>` testee vs `pcrec-auto`/`pcrec-vm`
(same-pin, same-window — no cross-pin noise-floor question), scored
against `docs/dev/predictions/capability-0.1-b117-olevel-a32bc86e.tsv`
via `pcrecbench interpret`. Regenerate the report's `.interpretation.md`
sidecar per [B41]'s standing rule.

## 5. Process notes

- Box was busy with pcrecdev1's `make test` for most of this lane
  (`uptime` load1 1.3-3.4, `pgrep -a make` showing pcrecdev1's own PIDs
  early on); every step taken was LIGHT (single-pattern/few-pattern
  compiles, targeted `selfcheck.py` arms, `make check-schema`) and
  verified against the box-state rule before running. `pgrep -a make`
  showed no pcrec `make` by the end of the session (load1 dropped to
  ~0.9-1.4), but the full census was still treated as OWED per the
  ~4-minute DO-THEN-FINISH rule rather than launched speculatively.
- `bench/email`'s subjects were not yet generated in this fresh
  worktree (`python3 bench/email/gen_subjects.py` /
  `gen_throughput_subjects.py`) — needed for `check_cflags_axis`'s own
  pre-existing arm 5 (a scratch `quick` cell on `bench/email`), unrelated
  to this lane's own changes; generated once, gitignored as always.
- No `store/` or `reports/` write; no timing of any kind. This lane
  measures nothing pinned itself, matching `pcrec-auto-align64loops`'s
  own b110probe precedent.
