# Lane `b75kb27` — delivery report

Branch `lane/b75kb27`, worktree `worktrees/b75kb27`, off `master` at
`5b5b69f`. Task: investigate and fix KB-27 (`docs/dev/known_issues.md`)
— the capability report labels `evil-alt-nested` × {`rd-evil-alt-near-
miss`, `sd-empty-alt-hit`} "wrong" though `bench/capability/
expectations.tsv` carries no row for either pair.

## Charter-vs-committed checklist

1. **Investigate the mechanism.** DONE. Established by direct read of
   the actual store records plus a reproducing probe — see §1 below.
2. **Fix at the honest layer.** DONE — `pcrecbench/reduce.py` (the
   reduction), not the harness or the schema. See §2.
3. **Tests.** DONE. `make check-report` (86+7+8 = 101 tests, all new/
   moved ones green), `make check-interpret` (190/190, unaffected),
   `make check-schema` (5/73/0, unaffected). `make check-harness` NOT
   run (a re-pin lane held the box's heavy-suite slot the whole time —
   see §3 and "Owed").
4. **Close out KB-27**, CLAUDE.mds, the lane report, the archived
   probe. DONE.

---

## 1. Mechanism — established by direct read, not inference

Grepped both (pattern, subject) pairs' rows directly out of
`store/records/capability@0.1/*/*.jsonl` for every one of the 21 testee
directories. **The store never fabricates a wrong verdict**: every
affected record's own `match_outcome` is exactly what
`pcrecbench/harness.py`'s `outcome_for()` wrote —
`did-not-match-as-expected`, with diagnostic literally "no expectation
exists for this (pattern, subject, regime) -- the sub-bench must state
one before the cell can be judged". That is `outcome_for()`'s
`expectation is None` branch (the ONLY place in the harness that ever
writes this text), which fires whenever no expectation row exists at
all — the SAME `match_outcome` VALUE a genuinely-disagreeing testee
gets. `pcrecbench/reduce.py`'s `WRONG_ANSWER_OUTCOMES` (which `n_wrong`
sums) includes `did-not-match-as-expected` — correctly, for the case it
was written for — so it ALSO counted the missing-expectation case as a
wrong answer. The mislabelling is at REDUCTION: reading the outcome
VALUE without reading its DIAGNOSTIC, the only place the two cases are
told apart.

`bench/capability/gen_expectations.py` uses the shared derivation
(`pcrecbench/expectations.py`): `derive()` enumerates the FULL (pattern
× subject × declared regime) cross product and skips a row ONLY on an
oracle `Pcre2Error` (a give-up), listed on stderr and never persisted.
For this set, a missing `expectations.tsv` row for a declared
(pattern, regime) is therefore STRUCTURALLY always an oracle give-up,
never an authoring gap.

Wrote `docs/dev/measurements/probe_kb27_no_expectation.py` (archived
output `docs/dev/measurements/2026-09-22-kb27-no-expectation-probe.txt`)
to confirm this over EVERY testee rather than a hand-picked few. Result,
both cells identically: the 21-testee roster splits into three groups —
**9 genuine give-ups** (`gave-up` in both OLD and NEW reduction,
unaffected: `outcome_for`'s give-up branch runs before the `expectation
is None` one), **3 `timed-out`** reads (`pcrec_a770139e`'s three
configs — the per-subject alarm fires on this adversarial pattern at
that pin; unaffected, correctly excluded either way, and an incidental
fact this probe surfaces honestly rather than glossing over), and
**9 testees carrying the "no expectation exists" row** — `libpcre2-dfa`,
`pcrec_{25b1984f,a770139e,cf0962e3}_auto-nocaps`, `re2-default`,
`re2-longest`, `rust-default`, `tre-default`, `vectorscan` — every one
of which the OLD formula scored `n_wrong=5`/`wrong` and the FIXED one
scores `n_no_expectation=5`/`no-expectation`, on the IDENTICAL rows: 18
(testee, cell) pairs fixed, no record's raw fields changed.

## 2. Fix — `pcrecbench/reduce.py`, not the harness or the schema

Three candidate layers were named in the brief; here is why the fix
landed where it did:

- **Not the harness.** `outcome_for()`'s choice to answer
  `did-not-match-as-expected` when no expectation exists AT ALL is a
  deliberate forcing function (the diagnostic's own text: "the
  sub-bench must state one before the cell can be judged") — a set
  missing an expectation for a reason OTHER than a documented oracle
  give-up should still be loud. Changing that behaviour would also only
  ever apply to FUTURE records (the store is append-only); the two
  tainted cells are ALREADY committed with this value, so a harness-side
  fix alone could never make them render honestly.
- **Not the schema.** `match_outcome` is a closed enum
  (`schema/record.schema.json`); growing it for this fix is reachable
  without one, so it was not touched. `REPORTER_VERSION` bumps (v18 →
  v19), which IS the schema-adjacent surface a rendering fix owns.
- **The reduction** (`pcrecbench/reduce.py`), because it is the ONE
  place that can render EVERY affected record — past and future —
  honestly, without a schema bump and without re-measuring anything.

`reduce.py` gains `NO_EXPECTATION_DIAGNOSTIC_PREFIX` (the literal text
of `outcome_for()`'s one fixed diagnostic, duplicated rather than
imported — importing `harness.py` would pull the adapters/driverrun/
store machinery for actually RUNNING a cell into `reduce.py`'s import
graph, which today is as light as `report.py`'s own "never runs an
engine" posture) and `_is_no_expectation_row(row)`.
`reduce_match_cell`/`reduce_set_cell` compute `n_no_expectation` and
subtract it back out of `n_wrong`; `outcome_counts` (the raw tally,
rendered verbatim in the excluded-cells table's `outcomes` column) is
untouched. `_failure_label` and `--format matrix`'s `_matrix_cell`
(`pcrecbench/report.py`) both gain a SIXTH closed status token.

**The token is `no-expectation`, deliberately NOT `unjudged`** — the
KB's own original suggestion. `pcrecbench.reduce`'s `trial_agreement`
block (schema v1.4) already renders "N unjudged" on every record's
`agreement:` line, a COMPLETELY UNRELATED count (rows the speed-
disagreement rule could not judge). That count and a new status token
named the same word would sit in the SAME committed report, often the
same table — this lane's own review caught the collision before
merging (verified by grepping every existing "unjudged" occurrence in
the codebase before picking a final name), not something flagged
after the fact. `scripts/matrix_page.py`'s `STATUS_CHIPS` gains the
matching `chip-no-expectation` entry (an unhandled sixth token would
otherwise render as an "unparseable cell" in the HTML page).

Files touched: `pcrecbench/reduce.py`, `pcrecbench/report.py`,
`scripts/matrix_page.py`, `pcrecbench/tests/test_report.py`,
`pcrecbench/tests/test_matrix_page.py`, `pcrecbench/CLAUDE.md`,
`pcrecbench/tests/CLAUDE.md`, `scripts/CLAUDE.md`,
`docs/dev/known_issues.md`, `docs/dev/measurements/CLAUDE.md` +
the new probe/archive pair.

## 3. Tests — targeted checks only, no full `make check`

A re-pin lane (per the brief) held the box's heavy-suite slot the
whole time this lane ran; `make check-harness` (~20 min, builds every
pcrec config) was never run, per the mandate's "one heavy suite on the
box at a time" rule. Every check this lane's OWN surface needs is
outside that heavy suite:

- **`make check-schema`**: 5 example(s) accepted, 73 sabotage(s)
  rejected for the intended rule, 0 wrong — unaffected (this fix
  touches no schema file).
- **`make check-interpret`**: 190 passed, 0 FAILED — unaffected (this
  fix touches no TSV column the interpreter's catalogue reads; the
  `n_wrong`/`n_gave_up` columns it does read are unchanged in shape).
- **`make check-report`** (run piece by piece rather than through
  `make` directly, since a background run was needed for the ~5.5 min
  `test_report.py` module — see below):
  - `python3 -m pcrecbench.tests.test_report`: **86 passed, 0 failed**
    (was 84; +2 new: `test_no_expectation_cell_is_not_wrong`,
    `test_no_expectation_diagnostic_matches_harness`).
  - `python3 -m pcrecbench.tests.test_quick`: **7 passed, 0 failed**
    (unchanged).
  - `python3 -m pcrecbench.tests.test_matrix_page`: **8 passed, 0
    failed** (unchanged in count; `test_status_chip_cell_html` now
    exercises the sixth chip via its existing generic loop over
    `STATUS_CHIPS`).
  - `schema/validate.py --check-filename` over every fixture group
    `check-report` names (`fixtures/store`, `fixtures/store_walk_only`,
    the two `mixed_version` "ok" halves, `fixtures/v14_pair`): all
    accepted, matching `check-report`'s own documented counts.
  - CLI smoke: `report --format md/tsv`, `--grain subject --format md`,
    `--format matrix` piped through `scripts/matrix_page.py`, and the
    `--grain subject --format matrix` refusal — all as `make
    check-report`'s target specifies, all green. `build/check-report-
    smoke.matrix.tsv`'s header confirms `reporter: v19 (2026-09-22)` and
    that its provenance comment reads `no-expectation`, not `unjudged`.

`test_report.py` alone took ~5.5 minutes wall (matching KB-25's own
measured `make check-report` total of 5:25.80 at a smaller store — the
store has not grown in `email-specimen` count since KB-25's own
measurement, 48 both times, so this is the SAME cost that fix already
accepted, not a regression this lane introduced). Run via
`gnutimeout 590` into a log file rather than the Bash tool's own 120 s
foreground default, per the box's measurement discipline.

**Before/after counts**: 84 → 86 reporter tests (test_report.py); 7 → 7
(test_quick.py, unaffected); 8 → 8 (test_matrix_page.py, count
unaffected — the sixth token rides the existing generic chip test).
check-schema 78 → 78 (unaffected). check-interpret 190 → 190
(unaffected). `make check-harness`: OWED (not run — see above; nothing
in this lane's diff touches `tools/selfcheck.py`, any adapter, or any
`bench/*` generator, so it is not expected to move, but it was never
actually run against this change).

## 4. Committed reports — NOT regenerated, an explicit OWED item

Following this project's own precedent for every prior reporter-
version-bumping fix (KB-18, [B52], and the rest of `reports/CLAUDE.md`'s
own history): the regeneration of `reports/` is left to a separate,
later lane or the window/manager next holding the store, never done
inside the fix-authoring lane itself. This lane follows the same rule.

The ONE group this fix changes the rendering of —
`2026-09-22-capability-0.1-budu-ryzen1600-wrapfix-25b1984f.*` — is cheap
to regenerate on demand (7 records, its own committed header names the
exact query; NOT a whole-store load, so KB-16's ~750 s / 3.6 GB concern
does not apply here). It was deliberately NOT regenerated by this lane,
to stay consistent with how every other reporter-version-bump landed.
The exact command and the two-cell story are in `docs/dev/
known_issues.md`'s KB-27 entry (the "Regeneration" and "Both cells,
EVERY testee..." sections) — copied here verbatim for a reader who
stops at this file:

> Until [regeneration] runs, a reader of the COMMITTED
> `2026-09-22-capability-0.1-*-wrapfix-25b1984f` files still sees the
> PRE-FIX rendering: `evil-alt-nested` × {`rd-evil-alt-near-miss`,
> `sd-empty-alt-hit`} on `pcrec_25b1984f_auto-nocaps-simdna` still reads
> `n_wrong=5`/`wrong` there today, exactly as this KB describes — the
> fix is real and tested, but it has not yet been applied to any file
> under `reports/`. Tonight's [B74] window, which reads this exact
> group as part of its comparison population, should regenerate it (or
> run the whole-store wave if one is already due) before treating its
> `evil-alt-nested` "no winner at all" reading as current.

**`pcrecbench interpret`/`regen_sidecars.py` note**: while probing
whether a targeted regen was practical, `python3 scripts/
regen_sidecars.py` was run (read-only against `reports/`'s already-
committed `.tsv` files; confirmed via `git status` that it wrote
NOTHING — every file either regenerated byte-identical or failed
loudly). It surfaced FOUR pre-existing, unrelated failures
(`2026-09-17-...-first-a770139e`, `2026-09-18-...-after-cf0962e3`,
`2026-09-18-...-ext-first-cf0962e3`, `2026-09-19-...-ext-second-
cf0962e3` — all `pcrecbench interpret --render` exiting 2 on a
`docs/dev/predictions/capability-0.1-first.tsv` selector defect,
already diagnosed and filed as a genuine tension in `docs/dev/lanes/
b72smalls_report.md` item 5). Confirmed NOT caused by this lane (they
predate it and this lane's diff never touches `interpret.py` or that
predictions file) and NOT this lane's to fix — named here only so
whoever runs the real regeneration is not surprised by them.

## Delivery

Branch `lane/b75kb27`, incremental commits (see `git log lane/b75kb27`),
all with their own CLAUDE.md/known_issues.md updates in the same
commits where practical. Working tree includes the fix, tests, the
archived probe, this report, and KB-27 CLOSED. Not merged (the
manager's job); not pushed.
