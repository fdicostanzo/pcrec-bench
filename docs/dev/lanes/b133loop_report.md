# [B133] lane report: TIMED-LOOP ISOLATION in every driver

Lane b133loop, 2026-10-09, branch lane/b133loop (worktree worktrees/b133loop), sonnet.
Pin 255bcdd8 (abi 68) throughout; nothing in store/, no pinned window run, no pcrec build touched.

## What was built
- **Isolation, all seven engines.** Everything between a subject's two clock reads
  now lives in a translation unit of its own, `noinline` + `aligned(64)`, holding only the
  timed function and what it calls: `testees/{pcrec,pcre2,onig,tre,vectorscan}/timed.c` +
  `timed.h`, `testees/re2/timed.cc` + `timed.h`, and the `rust-timed` crate
  (`testees/rust/timed/`). The driver builds a small input struct of already-resolved entry
  points and reads back an output struct (volatile fields, so the sigsetjmp/longjmp timeout
  path is unchanged). Loop bodies, bounds, call shapes and clock source (CLOCK_MONOTONIC /
  `Instant`) are the master text verbatim apart from locals becoming struct fields. Moved
  with the loop because they run inside the clock window: tre's `emit_caps`, vectorscan's
  `hs_scan` callbacks + SOM match list, pcre2's `do_match`, pcrec's buffer-variant dispatch
  and `utf8_next_start` (a three-line copy now lives in each timed unit).
- **pcrec shim:** the four wrappers the loop calls (`pb_search`, `pb_match_caps`,
  `pb_search_in`, `pb_match_caps_in`) are `aligned(64)` (`PB_TIMED`), because [B132]
  located a getter above them shifting them mod 64.
- **Builds:** `pcrecbench/driverrun.build_driver` links a sibling `timed.c` automatically
  and includes it + `timed.h` in the staleness check (every C adapter unchanged); re2's
  adapter compiles `timed.cc` and checks it; rust's adapter checks `timed/`; `Cargo.lock`
  gained only the `rust-timed` package (regex version unchanged; `--locked` build OK).
- **Not timed code, left where it was:** info/stamp getters, load/compile phase clock reads
  (compile timing), output formatting stay in `driver.*` `main()`; no cold section was
  needed because the timed code no longer shares a function or object with them.
- **What Rust could and could not pin:** `#[inline(never)]` in its own crate (own codegen
  units/object: main.rs edits cannot change its code generation); alignment via a
  `global_asm!` that re-declares the function's own section (`.text.rust_timed_run`)
  `.balign 64`, giving 0 mod 64 in the link (proof below). NOT pinned: per-function
  alignment as a language feature (nightly only), and the link-order neighbours; the
  proof is the check, not the trick. The release profile was NOT touched (codegen-units/LTO
  would change the `regex` dependency's own codegen, a confound).

## Charter-vs-committed checklist
1. Isolation in every driver: DONE, committed (see above). Semantics: compiled `-Wall
   -Wextra` clean of new warnings; the smoke (`quick`, pcrec-auto and pcre2-jit, capability
   and sentinel) ran and validated; the full answers control is item 2(b), OWED.
2. Proof:
   (a) object level: DONE, `docs/dev/measurements/2026-10-09-b133-isolation-proof.{py,txt}`.
       With 40 dummy `printf`/`emit!` lines inserted before the list-path return in each of
       six drivers (pcrec, pcre2, onig, tre, vectorscan, re2) plus rust, the timed
       function's normalised disassembly (addresses, call/jump targets and rip
       displacements masked) is IDENTICAL, its address is 0 mod 64 in both builds
       (e.g. pcrec 0x4c40 -> 0x5040, rust 0xd5c40 -> 0xd7880) while `main()` grows by
       240-1350 instructions (the control that the comparison can see change). pcrec shim:
       on winpath-near-miss and keyword-prefix-order, caps and nocaps artifacts, the four
       wrappers are identical and 0 mod 64 with 41 getters added; the PRE-[B133] shim (git
       ec62878) with the same getters moves a wrapper mod 64 (positive control; note 40
       identical 16-byte getters add 640 B = 0 mod 64 and move nothing, hence the varied
       sizes and the 41st). Reproduce: `python3 docs/dev/measurements/2026-10-09-b133-isolation-proof.py WORKDIR`.
   (b) unchanged-answers control, `make check-harness`: **OWED** (see below).
3. Instrument-change measurement (BEFORE = master ec62878 driver+shim, AFTER = this lane,
   pin 255bcdd8, A/B/A/B, 25 cells: pcrec-auto 10, pcrec-nocaps 10, pcre2-jit 5, scratch
   tier, core 11): script + analysis committed (`scripts/instrument_ab.sh`,
   `scripts/instrument_cells.txt`, `docs/dev/measurements/2026-10-09-b133-instrument-ab-analysis.py`);
   the numbers are **OWED**. PREDICTION stated before the run: movers (winpath, trim-nested-
   star, numeric-id, phone-list, us-zip, base10num, ipv4, uuid, semdiv) AFTER/BEFORE
   0.85-1.00 (the isolated, aligned loop recovers some or all of [B132]'s +10-17%; winpath
   up to ~0.80 where the shim wrapper alignment also matters), controls 0.97-1.03,
   pcre2-jit 0.97-1.03 (its driver is isolated too, so a small non-zero step is possible).
4. Sentinel set: DONE, committed. `bench/sentinel` (sentinel@0.1): 14 patterns + the
   floor, capability@0.2's 75 short subjects, regime search_short, byte copies checked by
   `gen_patterns.py --check` / `gen_subjects.py --check`, 1,125 oracle expectations,
   `.rxt` export generated. `scripts/run_suite.sh` PREPENDS it to every suite (SENTINEL=0
   skips; a `sentinel:end` pass is available) for pcrec-auto, pcrec-nocaps, pcre2-jit.
   Reading rule: `bench/sentinel/NOTES.md` (sentinel shift + flat pcre2-jit = the instrument
   moved; check `program_sha256` first — program-identity is a property of a pin pair).
   Deviations: the sentinel has 14 patterns, not [B132]'s 16: `wild-codegrammar-json-
   stringcontent-escape` and `bracket-array-define` contain a newline and cannot be exported
   as a `.rxt` `pattern` line, which the per-set export gate requires; the dry-run rehearsal
   (`run_suite.sh --dry-run`, synthetic, scratch) wrote validator-accepted records for
   pcrec-auto and pcrec-nocaps (1,155 rows each); the third cell (pcre2-jit) was killed by
   my own 230 s wrapper timeout and re-smoked with `quick` instead.
5. Re-pin control: DONE, documented ("Re-pin control" in testees/pcrec/CLAUDE.md) and
   executable (`scripts/instrument_ab.sh`, same script as item 3). No standalone
   re-pin procedure doc exists in the repo (re-pin knowledge lives in the per-pin sections
   of testees/pcrec/CLAUDE.md and in lane reports), so none was edited.
6. Docs: DONE — decisions.md BD16, docs/methodology.md (one paragraph), CLAUDE.md of
   testees/{pcrec,pcre2,onig,tre,vectorscan,re2,rust}, bench/, scripts/, pcrecbench/,
   plan.md row. No schema change; before/after is `run.harness_commit` (R19). NOT done:
   root CLAUDE.md / APPROACH.md mention (manager's call at merge).

## OWED (one detached chain, marker below)
`scripts/b133_owed_run.sh` waits for a quiet box (3 consecutive passes, <= 3 h; the box was
NOT quiet when the lane ended — b130trend's `tools/trend.py` held a core at ~100% and
`pcrecbench quiet` returned rc 3), then runs the A/B/A/B (~55 min est.), then
`make check-harness`. Launched detached by the lane at the end of its work (BD3: it is the
only heavy job this lane runs; the manager should not start another until the marker).
- log: `worktrees/b133loop/build/b133/chain.log`; A/B log `build/b133/ab/run.log`
  (marker `DONE rc=`); check-harness log `build/b133/check-harness.log`
- completion line: `CHAIN_DONE ab_rc=<n> check_rc=<n> <date>` (or `CHAIN_DONE
  quiet-wait-timeout (nothing measured)` if the box never went quiet)
- then: `python3 docs/dev/measurements/2026-10-09-b133-instrument-ab-analysis.py build/b133/ab`
  and fold the table + the check-harness verdict into this report. Expected check-harness:
  only the four known pruned-build reds; anything else is a finding.
