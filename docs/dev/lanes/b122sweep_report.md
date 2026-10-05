# lane b122sweep report — [B122] step (c') — the round-1 WIDE MOVER SWEEP

Branch `lane/b122sweep`, worktree
`.claude/worktrees/agent-a3cbadc260de4bd8d` (this agent's own dedicated
worktree, created already merged onto `lane/b122read`'s own merge
2124f81; a lane branch was checked out from that point rather than a
nested `worktrees/b122sweep`, per this environment's own restriction on
creating a second worktree from inside an already-isolated agent
worktree). Read-only over committed inputs only — no compile, no run,
no timing, no store load, no window. `~/pcrec` was not touched.

## 1. Findings first

1. **The reporter already carries exactly the rule the brief asks for,
   per cell** — the `d119`/`null_band` TSV sections ([B79],
   `docs/design/null_band_v1.md`): `program_sha256`-field identity
   (identical/changed) and a bar = max(within-window IQR%, the
   identical population's own per-stratum |Δ%| half-width). Re-deriving
   this by hand from `rank` rows would have been a second, weaker
   implementation of arithmetic the project keeps in exactly one place
   — so the sweep script reads `d119`/`null_band`, never `rank`, and
   states why in its own docstring.
2. **THE NULL, measured**: across the eight reports' 1,255
   program-identical d119 cells, R8's own 2×stddev rule (column 18,
   `delta_verdict`) STILL fires faster/slower on up to **51%** of them
   at small magnitude (capability auto 198 cells: 111 unchanged / 63
   faster / 24 slower, worst fired |Δ%| 51.29%; utf8 auto similarly,
   50.25%) — cross-window noise by construction, since the program did
   not change. This is why the D119 bar, not the raw R8 column, is the
   real/noise cut this sweep applies; confirmed structurally too (1,255
   of 1,255 identical rows read the reporter's own `null-control`
   token, never scored against a bar).
3. **234 real movers** (identity=changed AND D119 bar in
   {regress, improve}) across all eight sets: altwide 59, bounded 92,
   capability 12, email-specimen 3, litrun 7, loglines 5, syntax 38,
   utf8 18. 0 of 702 changed-identity rows are unjoined against the
   census (every (set, pattern, route, form) key matched).
4. **Per cause** (joined to `2026-10-04-b122-census.txt`'s own
   attribution): `-fno-run-overlap` 96 rows (68 improve/28 regress, six
   of eight sets — the WIDEST real mover by row count and set spread);
   the flagless `[CLS-TREE] S2` range-respelling step 65 rows (30/35,
   three sets, almost entirely bounded's `cls-upto-*`/`dig-*`/`nest*`
   ladder — a program change with no deny flag of its own); K82's own
   `-fno-req-run-fold` 32 rows (16/16, four sets, the single largest
   individual ratios: ×9.08 improve, ×2.29/×55.66 regress); K81's own
   `-fno-view-edge` 28 rows (14/14, four sets, net-neutral, ALL on
   whole-subject match-compliance cells — a different shape than K81's
   own ~+1-9 ns-scale prediction); all-three 9 (0/9, capability's
   userpass + utf8's alt-shared-char); 2 unattributed-flagless (bounded
   nest2-64/nest3-16); K78's own flagless fill-move, 2 (email-specimen
   `factored`, net flat, confirming §6 item 8 of the prior ledger).
5. **b122read's five §6 spot claims all CONFIRMED exactly** when
   re-derived from this wider join: `ci-ascii-control` ×2.77/×8.38,
   `alt-shared-char` ×2.06/×1.21, altwide `clsa-64`/`clsd-64`
   ×1.16-×1.37 on all three regimes, the five K82 fold-family patterns'
   two-sided regime split, and litrun's own "no mover beyond ±1.17×"
   (its own worst real mover, `wild-secrets-github-pat`, reads exactly
   ×1.16 ≤ the stated bound — a positive confirmation, not merely an
   absence of a counter-example).
6. **Two real populations beyond anything in I-127's text or the prior
   ledger's spot check**: `-fno-run-overlap` moves 15 syntax@0.1
   forced-VM cells (`lka-pos`/`lka-verb`/`cls-h`/`mod-n`/`mod-x`/
   `esc-hex`/`lit-cat`/`asr-nwb`/`cls-s-lc`, ×1.11-×1.45) and 5
   utf8@0.1 cells (`lit-1ch-3b`/`asr-a-z`/`lit-anchored-run`,
   ×1.12-×1.15); the flagless `[CLS-TREE] S2` range-spelling step moves
   63 bounded@0.3 cells (0.1-47%) spanning the whole `cls-upto-*`/
   `dig-*`/`nest*` ladder, of which K81's own text names only one
   member (`cls-upto-1024`).
7. **Cross-check**: the sweep's per-stratum D119-bar reading agrees
   with the brief's own cruder literal wording (pooled max|Δ%| per
   (set, route) rather than per-stratum) on 548 of 702 changed rows
   (78.1%); 141 rows read real by the bar alone (a narrower per-stratum
   band than the pooled reading), 13 by the pooled rule alone (that
   cell's own stratum happens to have a wider band than the set/route
   pool) — both directions are a legitimate consequence of per-stratum
   vs. pooled thresholds, not a defect in either rule, and both counts
   are stated so nobody has to take "the bar" on faith.

## 2. Charter-vs-committed checklist

| brief item | status |
|---|---|
| Build a ranked mover table per set/config: every row faster/slower beyond spread, with the ratio, joined to the census cause (route forced-VM for pcrec-vm, auto for pcrec-auto/-nocaps; whole vs plain form as the reporter defines it) | **COMMITTED** — `docs/dev/measurements/probe_b122_sweep.py` §3 of its own output (`docs/dev/measurements/2026-10-05-b122-sweep.txt`): per set, every d119 cell sorted by \|Δ%\|, with testee slug, regime, form, R8 verdict/ratio, D119 bar verdict and the census-joined cause; `cfg` is derived from the testee id's route token exactly as specified (vm → `vm`; auto-caps/auto-nocaps → `auto`), `form` from `whole-subject`→`whole` else `plain` |
| THE NULL: the same verdict distribution over identity-identical patterns; report count + ratio spread per set; use it as the threshold separating real movers; state the rule BEFORE applying it | **COMMITTED** — the script's module docstring states the rule before any table; §2 of the archive gives, per (set, route), the identical population's n/R8-unchanged/faster/slower counts and the worst fired \|Δ%\|; the chosen threshold is the reporter's own D119 bar (which already contains exactly the brief's suggested per-(regime,scale)-stratum range as its band term, plus the within-window IQR) — the brief's own cruder pooled-range version is ALSO computed and cross-checked against the bar in §3b (548/702 agree, both disagreement directions named and explained) |
| Per cause: real movers faster/slower, the largest of each, which sets — what round 2 is chosen from | **COMMITTED** — §4 of the archive; the same table is in the ledger §7.3 and the outbox draft, with row counts, improve/regress split, sets touched and the largest improve/regress cell named per cause |
| Reconcile with b122read's spot claims (ci-ascii-control, alt-shared-char, altwide class-tail, litrun flat, K82's fold-family split): confirmed/refuted by the null | **COMMITTED** — §6 of the archive, one block per claim with the matched d119 rows' identity/R8/bar/Δ% shown; all five CONFIRMED (the litrun claim verified as a positive bound-check, not an absence) |
| Write it as a committed probe script (re-runnable, deterministic) + its archived output (D35 source header) | **COMMITTED** — `docs/dev/measurements/probe_b122_sweep.py` (module docstring states the two inputs, the rule and why `d119`/`null_band` rather than `rank`); `docs/dev/measurements/2026-10-05-b122-sweep.txt` (the script's own stdout, sha256 of both input sets printed in its own header — no compile/run/timing, so no load samples apply, same stated exemption as `probe_rxt_format.py`'s own archive); two independent runs diffed byte-identical before archiving |
| Add a §5 replacement/§7 to the ledger; update the outbox draft with the per-cause table (short: top movers per cause and the null) | **COMMITTED** — `docs/dev/ledgers/2026-10-05-b122-round1-wide-c4c70f2c.md`: an addendum appended to §5 pointing at the new §7, plus the new §7 (7.1-7.5: the null by set×route, the ranked real-mover narrative per set, the per-cause table, the §6 reconciliation, what §7 did not do); `docs/dev/lanes/b122read_outbox_draft.md` updated with a short "UPDATE" block carrying the per-cause table and the two beyond-ask populations, still marked as a DRAFT the manager commits to `outbox_to_pcrec.md` |
| State what was NOT read | **COMMITTED** — §7.5 of the ledger (the census-cause-naming rule is mechanical over the census's own columns + its header's four named flagless cases, not independently re-derived against pcrec's diff, same BD2 caveat §2/§5 already carry; the D119 bar's own arithmetic is imported from the reporter's committed output, never hand-re-verified; no clang/deny-twin measurement, unchanged from §5) |
| `make check-interpret` only if a sidecar is touched | **N/A, correctly skipped** — no `.interpretation.md` sidecar was touched by this lane (only the ledger, the outbox draft, this report, the two measurements files and their CLAUDE.md entries) |
| Deliver `docs/dev/lanes/b122sweep_report.md` with the checklist, then end | **COMMITTED** — this file |

## 3. How the numbers were produced

- `docs/dev/measurements/probe_b122_sweep.py` parses all eight
  `reports/2026-10-05-*-round1-c4c70f2c.tsv` files directly (stdlib
  only, no `pcrecbench` import — the TSV is the committed artifact, and
  reading it independently is also a light structural check that the
  reporter's own file is self-describing): every `d119` row's
  `gave_up_summary` key-value string (`identity=`, `delta_pct=`,
  `iqr_pct=`, `band_pct=`, `bar_pct=`, `bar_source=`, `stratum=`,
  `before_ns=`, `after_ns=`) and its `value`/`delta_verdict` columns;
  every `null_band` `band_pct` row's own strata.
- The census join reads `docs/dev/measurements/2026-10-04-b122-census.txt`'s
  own embedded TSV (from its `set\tpattern_id\t...` header line to EOF)
  into a dict keyed `(set, pattern_id, config, form)`; the route→config
  and `whole-subject`→`whole` mappings are exactly as the brief states
  them.
- The four flagless-cause names (A1, K78, the two `[CLS-TREE] S2`
  shapes) are assigned by a small lookup table cross-checked against
  the census's own `engine`/`dfa_scan_edge` columns (the fallback rule:
  `engine=="dfa" and dfa_scan_edge=="range"` on a `not-restored-by-
  round1-denials` row reads `[CLS-TREE] S2 (range spelling)`), not
  independently re-derived from pcrec's source diff.
- Every number quoted in the ledger §7 and the outbox draft's table was
  cross-checked against the archived script output with `grep`/`awk`
  during this lane's own work (several first-draft prose counts were
  WRONG against the script's own numbers and were corrected in place —
  e.g. the syntax `run-overlap` population is 15 rows, not 9; the
  altwide `run-overlap` count is 58 of 59, not 57; the utf8 K82 count is
  13 rows, not 9 — all fixed before this report was written).

## 4. Validation

- Determinism: `probe_b122_sweep.py` run twice, outputs diffed
  byte-identical, before either run was archived.
- The archived file's own numbers were re-extracted independently with
  `awk`/`grep` against the eight committed report TSVs and the census
  file (not merely trusted from the script's own print statements) for
  every count quoted in the ledger §7 and the outbox draft — see §3
  above for the corrections this caught.
- No `make check` target was run: this lane touched no code under
  `pcrecbench/`, `schema/`, `catalogue/` or `tools/`, only a new
  measurements script/archive, a ledger addendum, an outbox draft and
  two CLAUDE.md maintenance entries, none of which any `make check`
  target gates.
- No store write, no record read, no engine run, no window.

## 5. OWED

Nothing is OWED. The script and its archive are committed and
re-runnable; the ledger §7 and outbox draft update are complete; this
report is the last deliverable.
