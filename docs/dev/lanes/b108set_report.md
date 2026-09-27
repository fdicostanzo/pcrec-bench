# b108set: bench/litrun@0.1 + predictions (lane report)

Lane `b108set` (sonnet), 2026-09-27. Branch `lane/b108set`, one commit
(`9082329`), worktree `worktrees/b108set`. Task: plan.md [B108] steps
(2)+(3) / inbox I-113 — build `bench/litrun/` (S7.1's 2×2 factoring ×
lit-run set, S7.2's L-sweep) and its predictions.

## Findings first

1. **The set builds, is internally consistent, and passes every generic
   harness gate it was scoped against.** `gen_patterns.py --check`,
   `gen_subjects.py`, `gen_throughput_subjects.py`,
   `gen_pattern_facts.py --check` and `gen_expectations.py --check` all
   reproduce byte for byte (14 patterns, 27 short + 27 throughput
   subjects, 1,134 expectations). `tools/selfcheck.py`'s
   `check_manifests()`/`check_expectations()` were run scoped to `litrun`
   only (via `subbench_dirs()` monkeypatched to `[('litrun', ...)]` —
   the same functions the real `make check-harness` calls, not a
   reimplementation) and both PASS, including their negative controls (a
   sabotaged manifest/expectations file is rejected). The floor-pattern
   quick-cell check (the harness contract's per-set driver smoke) was
   reproduced by hand with `pcrecbench quick` on `pcre2-jit` (5/5,
   `measured`), and I also ran `pcrec-auto` on `wild-secrets-github-pat`
   and `pcrec-vm` on `lit-l31` (both 5/5, both compile and answer
   correctly) as an extra pcrec-specific sanity pass beyond what the
   generic gate itself checks. `tools/export_rxt.py litrun --verify`
   round-trips clean against the pinned pcrec's `--list-source`.
2. **The tiling construction for the L-sweep's throughput subjects is
   PROVEN, not assumed, in three independent ways**: (a) a generation-time
   brute-force check (`gen_throughput_subjects.py`'s
   `check_no_accidental_match`, run over two full periods of every
   `fbf`/`lbf` unit — zero exceptions raised across all 18 subjects); (b)
   a direct `re.findall` count against all 27 committed throughput
   subjects, confirming `mat-l<L>` matches exactly `len // L` times and
   `fbf`/`lbf` match zero times, at every one of the 9 lengths; (c) the
   real libpcre2 oracle's own `gen_expectations.py` run, which is what the
   set's committed `expectations.tsv` actually encodes. All three agree.
3. **One deliberate scope decision worth flagging explicitly**: the 2×2
   set's `-fno-altcls-factor` axis (half of S7.1's own `{default,
   -fno-altcls-factor} × {default, -fno-lit-run}` crossing) has **no
   scorable clause in the predictions file**, because [B108]'s own ack
   line names only `pcrec-auto-nolitrun`/`pcrec-vm-nolitrun` as new deny
   testees — no `-fno-altcls-factor` testee is chartered anywhere I could
   find (`testees/pcrec/configs.toml` has no `altcls-factor` axis today).
   Writing a `ratio_to` clause against a testee id that doesn't exist
   would be exactly the "fated to always read not-evaluable" defect this
   project's predictions convention forbids, so I scored ONLY the lit-run
   axis (which IS certain: both testees are named in the ack) and left
   the factoring half as a stated, unscored expectation in both
   `NOTES.md` and the predictions file's own P4.b note. If `b108repin` (or
   a later lane) adds a factoring deny testee, a SEPARATE, freshly-dated
   predictions file is the right way to score it — not an edit to this
   one (predictions are stated-pre-run artifacts; see
   `docs/dev/predictions/CLAUDE.md`'s "Revising an already-scored file").
4. **The predictions file caught its own version of a known bug class
   before commit, not after**: `interpret.py`'s `_op_holds` reads a
   `lt`/`gt`/etc. threshold from `hi`, never `lo` (`lo` is only used by
   `between`) — the exact defect `syntax-0.1-rust-first.tsv`'s own
   documented history describes catching AFTER a window started. I built
   this file with a small script
   (`/tmp/.../scratchpad/build_litrun_preds.py`, not committed — scratch
   only) specifically so every row's `op`/`lo`/`hi` triple is generated
   from one code path rather than typed by hand 24 times, and verified
   the shape (`between` rows have both `lo` and `hi`; every other op has
   `hi` only) programmatically before commit.
5. **An emergent, genuine cross-term the oracle caught and I did not have
   to hand-anticipate**: `lit-l3`'s literal (`"abc"`) is byte-identical to
   `ctrl-abc-dollar`'s own prefix, so a few subjects legitimately match
   BOTH patterns, and `mat-l3` (tiled `"abc"`, ending exactly at the
   subject's own end) is the only L-sweep throughput subject
   `ctrl-abc-dollar`'s `$` finds anything on (`tput_mn` = 1/27 in
   `pattern_facts.tsv`). Documented in `NOTES.md` under "Subjects" so a
   future reader doesn't mistake it for a defect.
6. **`littext.py` carries no randomness primitive**, unlike every other
   generator sub-bench (`altwidetext.py`/`logtext.py`/`censustext.py`
   each define an `Rng`). This is a deliberate departure, explained in
   both `NOTES.md` and `littext.py`'s own header: every pattern and every
   subject here is an explicit, named construction with one stated
   purpose, transcribed directly from pcrec's own lane report rather than
   drawn from a vocabulary — there is nothing a seeded draw would do that
   a constant would not do more legibly.
7. **This set is NOT blinded**, unlike every other `bench/*/` set (pcrec's
   D27 discipline). Stated explicitly, twice (`NOTES.md` and `CLAUDE.md`),
   because it's the one deliberate exception on record: the whole point
   is to measure the EXACT cells pcrec's own engineers named, not a blind
   reading of `docs/spec/` alone.

## Charter-vs-committed checklist (brief's own five bullets)

- **§7.1's 2×2 patterns** — DONE. `alt-foo-tails` (a) =
  `foo.x|foobar|foo.` verbatim; `wild-secrets-aws-access-key-id` (a') and
  `wild-secrets-github-pat` (b') copied byte-for-byte from
  `bench/capability/patterns/` (`cmp` confirmed at generation time,
  `provenance.tsv` carries the full chain back to rebar-wild's
  noseyparker.txt, Unlicense); `ctrl-abc-dollar` (b) = `abc$`, same text
  as pcre2's own testdata pattern `bench/capability`'s
  `wild-semdiv-dollar-trailing-newline-pcre2` already carries. Subjects
  exercise matches AND near-misses of each: AWS's own published example
  key (`AKIAIOSFODNN7EXAMPLE`), pcre2 testdata's own two `abc$` match/
  no-match cases, hand-typed near-misses for every cell (short by one
  byte, wrong prefix, embedded-in-a-longer-string for the search regime).
- **§7.2's L-sweep** — DONE. L = 2, 3, 4, 7, 8, 10, 16, 31, 40, exact
  literals; four subject shapes per length as asked (matching / first-byte
  flipped / last-byte flipped / length L-1), realized at THROUGHPUT SCALE
  for the first three (dense in candidate starts, per-attempt cost
  instrument, ~64 KiB each) and as a short boundary subject for the
  fourth (never tiled — a per-subject-END event, not a per-position one;
  reasoned out in `NOTES.md`). Regime choice (`throughput`, i.e.
  `large-subject-throughput`) and why (S2a's own micro-subjects are too
  fast for this harness to time; pcrec's own memcmp study uses a tight C
  loop this project does not have) stated in `NOTES.md`, "Regime choice".
- **Take the two wild-secrets pattern texts verbatim... with
  provenance** — DONE. `provenance.tsv`, byte-checked at generation time
  against the live `bench/capability/patterns/` files.
- **Engine-neutral set (R-BENCH-4): no pcrec-specific shapes in the set
  files** — DONE. `subbench.toml`'s own closing note states this
  explicitly; no flag, no engine name, no pcrec-specific structure
  appears anywhere under `bench/litrun/` itself. The 2×2/L-sweep testee
  crossings live in the WINDOW's plan and the predictions file, never the
  set.
- **NOTES.md: transcribe I-113 predictions 1-5 as numbered P-rows BEFORE
  any run, stating which live in bounded/loglines/capability vs
  litrun** — DONE (`NOTES.md`, "Predictions"). P1/P2/P3 are transcribed
  in full prose with an explicit "scored against: <set>'s own report"
  line each; P4/P5 (litrun's own) additionally get the machine-readable
  TSV. **Also carried, per the brief's parenthetical**: which live
  arm-pair each L-sweep cell is scored on (default vs `-fno-req-run
  -fno-req-byte`, both build variables of the window's testee configs);
  L=31 named as a WATCH cell throughout.
- **docs/dev/predictions/ entry per its own convention** — DONE.
  `litrun-0.1-first.tsv`, 24 clause rows over 6 parents (P4.a-d,
  P5.a/b/c/d), plus a full entry in `docs/dev/predictions/CLAUDE.md`'s
  file list matching the directory's own documentation convention.
  Load-checked (`interpret.load_predictions`: 24/24 rows, zero closed-set
  errors) and mechanically checked for the `lo`/`hi` op-threshold bug
  class; NOT scorable yet (no `litrun` record exists — `check_testee_
  globs` is correctly vacuous by its own stated rule).
- **NO store/ or reports/ writes, no timing** — HONORED. Every
  `pcrecbench quick` call above ran with `--store build/scratch-litrun-
  check` (removed after each check) and `--synthetic`; nothing touched
  `store/` or `reports/`.

## OWED

- **The FULL `make check-harness`** (every `bench/*/` set together,
  including `altwide`/`syntax`'s own ~500-750 s expectation re-derivation)
  was NOT run by this lane, per `docs/dev/lanes/BOILERPLATE.md`'s
  DO-THEN-FINISH rule (a run this long is the manager's to launch). What
  WAS run, and is a faithful subset (the exact functions `make
  check-harness` calls, scoped to `litrun` only via `subbench_dirs()`) is
  reported above and is COMPLETE, not partial. Command for the full run,
  when convenient: `gnutimeout 900 make check-harness` from the repo
  root (or the merged worktree); the litrun-specific lines will read
  identically to what is quoted in "Findings first" item 1 above.
- **The `-fno-altcls-factor` half of S7.1's 2×2** is a stated but unscored
  expectation (finding 3 above) — owed to whichever lane next charters
  that deny testee, if the manager wants it measured this cycle.
- No other OWED items. Nothing else in the brief was skipped.

## Files

- `bench/litrun/` — the whole new sub-bench (see its own `CLAUDE.md` for
  the file-by-file breakdown).
- `docs/dev/predictions/litrun-0.1-first.tsv`, `docs/dev/predictions/
  CLAUDE.md` (new entry).
- `bench/CLAUDE.md` (new `litrun/` row).
