# Lane `b47subgrain` — delivery report

Branch `lane/b47subgrain` off `master` at `52f8c0e` (carries the cf0962e3
re-pin, catalogue 1.4). Implements
`docs/design/interpret_subject_grain_v1.md` §6's eleven rulings, ratified
in full by Frank (2026-09-17, live, one question at a time). Three
commits:

- `311a140` — `pcrecbench/interpret.py` (grain routing, ruling α/β, the
  stamp-gap fix) + `pcrecbench/report.py` (the subject-grain slice).
- `5772726` — catalogue 2.0, seven new fixtures, `gen.py`/
  `check_interpret.py` extensions, the first committed `.subject-grain.tsv`.
- `4802ce3` — `interpreter_v1.md` v1.4 (the folded design of record), the
  four regenerated sidecars, CLAUDE.md updates.

Not merged. `make check-interpret` 147/147 (was 133+). `make check-schema`
5/73/0 (unaffected). `catalogue/acceptance_10.py` 25/25 (unaffected).
`make check-harness` and full `make check` were **not** run per the
brief — owed to the merge.

## Charter-vs-committed checklist

1. **Catalogue 2.0 with `grain=subject`.** DONE.
   `catalogue/rules.toml` `catalogue_version = "2.0"` (MAJOR, §6 Q3).
   `SELECTOR_KEYS` gains `grain` (`pcrecbench/interpret.py`);
   `GRAIN_VALUES = {"set", "subject"}` validated at selector-parse time.
   R-PRED-1..4's `predicate`/`threshold_src` text documents the route and
   ruling (α)/(β); no rule's `template`/`no_fire`/`legend`/`links` moved
   (confirmed: `make check-interpret` section 6 found no such diff in
   any of the three commits, so the human-review gate is not blocking
   this lane's own WIP history — the manager's merge commit is still
   where a real prose change, if any is added later, would need the
   approval line).

2. **The reporter's subject-grain slice (the 5.62 MiB shape).** DONE.
   `render_tsv_subject_grain_slice` in `pcrecbench/report.py`: a pure
   row filter over `render_tsv`'s own `--grain subject` output — keeps
   `record` rows and `rank` rows' `median_ns` metric, keeps
   `excluded`/`not_ranked`/`scratch`/`did_not_compile` whole, drops
   `compile`/`compile_stamp`. CLI surface `--subject-grain-slice`
   (requires `--grain subject --format tsv`, refused by name otherwise).
   MEASURED on its first real use: 17,836 full subject-grain lines → a
   2,981-line slice (16.7%), consistent with the design note's ×4.8
   corpus-scale estimate. `REPORTER_VERSION` unchanged (additive only).
   One real slice is committed:
   `reports/2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.subject-grain.tsv`
   — chosen because it carries a real R-BUCKET-DOMINATED firing
   (`orig`/`large-subject-throughput`/`libpcre2_10.46_interp-caps-simdna`,
   `t-a-valid-addrs` at a 99.877% share, MEASURED). No back-fill (§6 Q9):
   the other 42 committed report groups carry no `.subject-grain.tsv`.

3. **The interpret route: `--subject-grain` wired for real.** DONE.
   The flag already existed as a stub (only `r_bucket_dominated`
   consumed it). Now also consumed by `evaluate_predictions`: a clause
   whose selector names `grain=subject` is scored against a second
   `RuleView` bound to `ctx.subject_grain` (R-PRED-1's own declared
   `inputs`, the same pattern `r_bucket_dominated` already used); with no
   `--subject-grain` file supplied the clause is `not-evaluable` BY NAME
   ("the clause selects grain=subject but no --subject-grain input was
   supplied"), never silently read as `grain=set`.

4. **Both load checks the note specifies (§6 Q6).** **NOT BUILT — OWED.**
   The note's two store-free `load_predictions` checks — (i) a
   `compile:` quantity's selector may not name `subject_or_na`/
   `regime_or_na` (closes Cause B, P2's authoring defect); (ii) every
   `testee=` glob must match ≥1 index testee for its own measured
   `(subbench, version)`, vacuous when unmeasured (closes Cause C, P4's
   glob defect) — are RULED YES (§6 Q6) but this lane did not implement
   them. They are independent of grain/catalogue-2.0 mechanics (pure
   `load_predictions`-time checks against already-declared inputs) and
   are a clean, separately-reviewable follow-up. **Owner: the next
   interpreter-touching lane. Trigger: any time — no dependency on a
   run or a re-pin.**

5. **(α)+(β) for P5 (the ruled shape, not the `section=` mandate).**
   DONE. `pcrecbench/interpret.py`'s `_sections_for`/`_select`/
   `_elsewhere`: the default section read for `n_wrong`/`n_gave_up`/
   `pass_rate`/`status` widens to `rank` UNION `excluded` (base rows
   only, `metric=pass_rate`, so a P-2 `giveup_smallest` detail row is
   never double-counted); an EVALUATED clause is also annotated with
   what its selector reaches outside that default read. MEASURED,
   real-world confirmation: regenerating the capability-0.1-first
   sidecar with the UNCHANGED, already-committed
   `docs/dev/predictions/capability-0.1-first.tsv` flips P5 from a false
   `confirmed` (worst 0.000, masking `date-nested-plus`) to the correct
   `refuted` (worst 10.000 on `evil-alt-nested`) — the exact verdict the
   ledger reached by hand, reached mechanically, with NO edit to the
   predictions file. Two more real firings: the syntax sidecar's P11/P13
   each gain a "; also present in: excluded (N)" / "did_not_compile (N)"
   clause (ruling β). Two dedicated fixture pairs added for CI coverage
   beyond that real-world proof:
   `R-PRED-2__alpha-widened-default`/`R-PRED-1__alpha-narrow-selector-control`
   (a real excluded cell, three `pcrec` VM testees at `n_gave_up=5`, on
   email-specimen's `orig`/`large-subject-throughput`).

6. **The `build_stamp`/`check_interpret.py` §3 freshness stamp-gap fix,
   unconditional.** DONE. `build_stamp` now takes `subject_grain_path`
   and records `subject_grain`/`subject_grain_sha256` on EVERY stamp
   (`(none)` when absent) regardless of any other ruling;
   `check_interpret.py` section 3 reads the stamped path back and passes
   it to its own re-render. Verified: this is why every one of the four
   regenerated sidecars' stamp block gained the two new lines even
   though none of them uses `--subject-grain`.

7. **Fold the rulings into `interpreter_v1.md` as the design of
   record.** DONE. v1.4: a new top-of-file changelog paragraph, a new
   §6.7 (the eleven rulings restated in the note's own voice, each
   pointing at what changed), §2.5's subject-grain follow-up line struck
   as IMPLEMENTED, §4.7's R-BUCKET-DOMINATED row and its `example`
   corrected, §11 Q2 corrected, §6.3's selector-key list and
   section-less-default text amended.
   `docs/design/interpret_subject_grain_v1.md` is untouched — it stays
   the derivation record per its own §6 Q11 and this note's ruling.

8. **The four-surface regen at catalogue 2.0.** DONE, with one
   deliberate scope decision stated plainly:
   - **Sidecars**: all four committed `reports/*.interpretation.md`
     regenerated with their EXISTING recorded inputs (report, index,
     predictions where applicable) — **none was given `--subject-grain`**,
     even though email-specimen's report now has a real slice sitting
     beside it. Wiring that sidecar to actually READ the slice (which
     would make R-BUCKET-DOMINATED fire in a committed sidecar for the
     first time) is a substantive decision about that specific report
     the note's own §7 leaves open ("a lane transcribing/repairing a
     predictions file... belongs to whoever owns the next sample") and
     is NOT this lane's to make unilaterally. **Owner: whoever next
     touches the email-specimen report or wants R-BUCKET-DOMINATED's
     first sidecar firing. Trigger: on request — the mechanism is
     proven via the fixtures either way.** Every provenance header
     (`report`, `index`, `predictions` and their sha256s) is preserved
     byte-for-byte; only the two new `subject_grain*` lines and the
     `catalogue:` version line move, plus the capability sidecar's real
     P5 content flip and the syntax sidecar's two β annotations.
   - **Fixtures**: regenerated via `catalogue/fixtures/gen.py` (211
     files in 65 fixtures, up from 58; `--check` clean).
   - **Goldens**: regenerated via `catalogue/refresh_golden.py` (all
     four ACCEPTANCE entries re-run; only the syntax+predictions golden
     moved, two lines, both ruling β).

9. **`make check-interpret` green (147, ≥133), `make check-schema`
   green.** DONE, both confirmed after the final commit (re-run
   independently, see the numbers at the top of this report).
   `make check-harness`/full `make check` **deliberately not launched**
   per the brief — owed to the merge.

10. **KB-16: never load the whole record store.** Confirmed unchanged.
    `check_interpret.py` never gained a store-loading call; every
    `run_interpret` call site in this lane's diff reads a committed TSV
    or a fixture/golden file. The ONE store-loading command this lane
    ran was a single, narrow, ~12 s / 104 MB `pcrecbench report
    --subbench email-specimen --version 0.1 --grain subject` (a 14-record
    candidate query, not a store-wide one) to produce the real
    subject-grain slice committed in item 2 above — run once, in the
    foreground (well under the box's memory-heuristic threshold; nothing
    detached, no marker needed), never as part of `check-interpret`
    itself.

## What a reviewer should look at first

- `pcrecbench/interpret.py`'s `_sections_for`/`_select`/`_elsewhere`/
  `evaluate_predictions` (the mechanism) and `build_stamp` (the fix).
- `pcrecbench/report.py`'s `render_tsv_subject_grain_slice`.
- The capability sidecar's diff (`git show 4802ce3 -- reports/2026-09-17-*.interpretation.md`)
  is the single clearest real-world proof this lane's (α) ruling does
  what the design note predicted, with zero hand-editing of the scored
  predictions file.
- `catalogue/fixtures/fixtures.toml`'s seven new `[[fixture]]` blocks
  and `catalogue/fixtures/gen.py`'s `subject_grain`/`mutate_subject_grain`/
  `predictions_source` additions, if the fixture-declaration extension
  itself needs review before it becomes a second precedent.

## Not touched, and why

- `docs/dev/plan.md` / `docs/dev/dev_journal.md` — left for the manager
  at merge, per this project's usual lane pattern (a lane report is the
  input; the manager's merge commit is where plan rows close).
- `.claude/skills/pcrec-bench-interpret/SKILL.md` — no change needed;
  its existing invocation shape (report + optional `--predictions`,
  matched by `subbench`/`version`) already produced the correct
  regenerated sidecars in this lane without any `--subject-grain`
  guidance being added to it. Whether the skill should ever pass
  `--subject-grain` automatically (e.g. when a sibling `.subject-grain.tsv`
  exists) is a design question for whoever picks up item 8's owed
  decision, not answered here.
- `pcrecbench/tests/test_report.py` — not run (would touch the full
  675 MB store per its own `REAL_STORE` cache, a heavier check than this
  brief authorized; owed to the merge alongside `make check-harness`).
