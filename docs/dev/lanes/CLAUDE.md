# docs/dev/lanes/ — the standing lane boilerplate (+ future lane reports)

- **`BOILERPLATE.md`** (2026-09-06, Frank's ruling, mirrored from pcrec):
  the standing rules every lane reads FIRST — scope/BD2/BD3, worktree
  ritual, box facts, process, lifecycle (no lane keepalives — 5-min
  subagent cache TTL; finish-handback-END; TaskStop before windows),
  delivery bar. Briefs carry only task/tier/deliverable and point here;
  update this file when a rule changes rather than growing briefs.
- `<lane>_log.md` / `<lane>_report.md` — a lane's own voice, if it keeps
  one; historical after merge (pcrec's convention, adopted with the
  boilerplate).
- **`b138_chain.sh`** (2026-10-18, lane b138chain, NOT RUN): the [B138]
  RE-BASELINE window chain -- the CORE roster (pcrec auto/nocaps/vm, pcre2
  jit/interp, one config per other engine) at the one canonical pin
  6b2dbd3e, two tiers (1: email, loglines, altwide, bounded, litrun; 2:
  capability, syntax, utf8; each with its own opening and closing sentinel
  pass). Needs `MACHINE_ID` (registers the box in store/machines.tsv,
  idempotent), `PIN` defaults to core 7, `DRYRUN=1` rehearses one cell per
  set into a scratch store. Header carries the per-tier estimate and how the
  sentinel pass yields the measured speed factor. `b138chain_report.md`: its
  rosters, cell counts, estimates, rehearsal result, open questions.
- **`b140drv_report.md`** (2026-10-25, lane b140drv): [B140] build-order step 3 - the pcre2 `--mode subst` driver, the `timed_subst()` instrument (own TU, BD16), the harness plumbing every later substitution driver shares (`pcrecbench/substrun.py`), the `make check-harness` slice (`tools/check_subst.py` section 9), one scratch dry run; charter-vs-committed checklist, BD16 accounting, findings (the trial-agreement rule's blindness at iters = 1, the `subst`-object placeholder gap), check counts.
- **`b140tools_report.md`** (2026-10-25, lane b140tools): [B140] build-order step 4 - the TOOLS tier: `pcrecbench/toolrun.py` (untimed correctness pass, timed `tool | wc -c`, sink check by name), `testees/tools/` (sed/perl/python/sd/rg, pinned by binary sha256 / version), `check_subst.py` section 11; checklist, the per-(tool, case) agreement table, findings, check counts.
- **`b140drv2_report.md`** (2026-10-25, lane b140drv2): [B140] build-order step 3 continued - the RUST (`replace_all`, unicode(false)) and RE2 (`GlobalReplace` on an untimed fresh copy) `--mode subst` drivers on b140drv's shared harness, BD16 instruments as NEW units (`testees/rust/timed-subst/`, `testees/re2/timed_subst.cc`), the additivity proof, `check_subst.py` section 10 (+19 checks), two scratch dry runs; checklist, BD16 accounting, findings, check counts.
- **`b143rep_report.md`** (2026-10-25, lane b143rep): the reporter - Part A (the eight check-report reds were the two-machine refusal; tests now name the host), Part B (reporter v27: `compound=` clause, emit-bytes definition note), Part C (`report --grain subst`, `bench/subst` sidecar rename, the generic gates' skip table); a verbatim sample subst report, make check counts, the `check-harness` run OWED to the manager.
- **`b140pcrec_report.md`** (2026-10-25, lane b140pcrec): [B140] build-order step 3, the LAST library driver - pcrec `--mode subst` at 9ae59f5d4 (abi 84): the substitution artifact kind (rx + subst artifact + private support unit in one `.so`), `timed_subst.c` as a BD16 NEW unit, the four-arm roster (`pcrec-auto`, `pcrec-vm`, both `-sizefirst`), cases 6 and 7 verified by sha256 (basis flipped to `verified-small`), `check_subst.py` section 12, four scratch dry runs; checklist, per-(arm, case) agreement table, BD16 accounting, findings, check counts.
- **`b142fix_report.md`** + **`b142fix_rehearsal.sh`** (2026-10-25, lane b142fix): the compound's `compound` stamp tokens declared (METADATA_DECL), the compound iff in the adapter, the harness check with controls, and the NOT-RUN all-sets scratch-store validation rehearsal.
- **`b142win2_chain.sh`**, **`b142win3_chain.sh`**, **`b142night_runbook.md`** (2026-10-25, lane b147chains, NOT RUN): the night behind [B142] part 1 as two box-queue reservations (`scripts/boxq_window`): part 2 = bench/subst at 9ae59f5d4 (library tier 10 testees, tools tier 5, the BD16 sentinel reads over pcre2-jit/rust-default/re2-default/pcrec-auto, the acc-main JIT-stack check, subject pre-generation/verification), ~3.1 h; tier 2 = litrun/syntax/utf8/email/bounded (+ loglines) x {auto, auto@6b2dbd3e} with a sentinel pair, ~6.4 h. Both carry a STOP_AT_NIGHT deadline (09:30) with per-set longest-cell margins. The runbook has the two launch commands, the order and how to check state.
- **`b148l1_report.md`** (2026-10-27, lane b148l1): [B148] L1 — record schema v1.11 (`call-stream`, `match_row.stream`, `testee.assist`, `v1.11-group`, X47-X53 with 13 generated negatives), REQUIRES `vars` + `unusual-<member>`, the `twin_of` tag, the §6.4 record-fit check, the set-grain skip table for the viewer/trend/frontpage and the reporter's refusal/drop; charter-vs-committed checklist, X-rule table, check counts, five findings.
