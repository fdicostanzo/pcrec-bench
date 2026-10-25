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
