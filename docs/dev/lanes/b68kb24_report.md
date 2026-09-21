# Lane b68kb24 — fixing KB-24 (`interpret.evaluate_predictions` crash on `quantity=delta_verdict` under `identity`)

Charter (team-lead brief, 2026-09-21): fix `docs/dev/known_issues.md`
KB-24 properly — `pcrecbench/interpret.py`'s `_reduce()` tags the
`identity` reducer's output `kind="num"` unconditionally, so
`evaluate_predictions` → `_measured_text` runs numeric formatting
(`abs()`, `:.3f`) on `delta_verdict`'s STRING tokens and the whole call
aborts before any clause's verdict is produced. `_op_holds` (the real
predicate) is fine.

## 0. The bug, confirmed before touching anything

Reproduced the crash by hand against the pre-fix code (direct
`I.evaluate_predictions` call over the real committed
`capability-0.1-pin-25b1984f-confirm.tsv` + the real committed report +
`store/index.tsv`):

```
CRASHED AS EXPECTED (pre-fix): TypeError("bad operand type for abs(): 'str'")
```

Matches KB-24's own finding exactly.

**Found while scoping**: KB-24's write-up says this predictions file is
"the FIRST predictions file in the repository to name `quantity=
delta_verdict` at all" and cites a `grep -l` that matched only it. That
is no longer true — `git log` shows five MORE files landed the same
combination since (`[B63]`/`[B64]`, 2026-09-20/21):
`altwide-0.2-pin-25b1984f-confirm.tsv`, `bounded-0.3-pin-25b1984f-
confirm.tsv`, `email-specimen-0.2-pin-25b1984f-confirm.tsv`,
`loglines-0.1-pin-25b1984f-confirm.tsv`, `syntax-0.1-pin-25b1984f-
confirm.tsv`. None of the committed `reports/*.interpretation.md`
sidecars for those six files carries a `predictions_file` stamp (all
were rendered without `--predictions`), so none has ever been
successfully scored — they were presumably blocked by this same crash.
This is a scope note, not scope creep: I did not score any of the five
new files (that is other lanes'/the manager's call), but the fix
unblocks all six, not just the one named in the charter, and constraint
4's real-world verification below is representative of the whole
population, not a special case.

## 1. The fix

`pcrecbench/interpret.py`:

- `_reduce()`'s `identity`/`""` branch now tags `kind` from the REDUCED
  VALUES themselves: `"num"` iff every value is `int`/`float`, else
  `"token"`. This is the same rule `_op_holds`'s `eq-token`/`neq-token`
  path already applies correctly (`str(value) == hi`) — the bug was that
  `_reduce` reasserted `kind="num"` from the REDUCER NAME instead of
  reading what `_value_of` actually produced.
- `_measured_text()` gained a genuine `kind == "token"` branch: no
  `abs()`/`:.3f`, a `{distinct value(s)}` rendering (scoped to the `bad`
  rows on a refutation, to the whole population on a confirmation) —
  the same shape `kind == "set"` already used, and the same shape the
  scratch workaround in `docs/dev/lanes/b60pinconfirm_report.md`
  improvised, now as the tool's own code.

**Candidate (a) vs (b), per interpreter_v1.md §7.2 and the constraint
to argue the choice**: KB-24 offered two candidates — (a) make `kind`
honest at the source (what I did), or (b) refuse `identity` paired with
a non-numeric quantity (`delta_verdict`/`status`) at `load_predictions`
time, forcing `set_of`/`count` instead. §6.5's own reducer contract
("turns a population into one number or one set") does not actually
claim `identity` returns "one number" — it is the one reducer that does
NOT collapse the population, by design (§6.3: "a reducer... turns a
population into one number or one set" is describing the COLLAPSING
reducers; `identity` is explicitly the non-collapsing case, and
`delta_verdict`/`status`/`section` are explicitly closed-set STRING
quantities in `_QUANT_COLUMN`, not an accident of one row shape). More
decisively: by the time this lane started, SIX real, committed
predictions files depend on exactly `identity` + `delta_verdict`
(§0 above) — candidate (b) would have turned all six into a load error
the day after five of them were authored, which is not "fixing" KB-24,
it is deleting the capability those authors just used. Candidate (a)
keeps every existing file expressible and makes the one place that lied
about `kind` tell the truth instead.

`_op_holds` (the actual confirm/refute predicate) is UNTOUCHED.

## 2. Versioning (interpreter_v1.md §3.3 as amended by [B56])

**CODE-ONLY. No `catalogue_version` bump (`rules.toml` unchanged). No
`INTERPRET_VERSION` bump.**

The §3.3 test is whether facts/verdicts move on unchanged inputs.
Two independent checks, both clean:

1. **No verdict can move**: `_op_holds` is untouched, so `confirmed`/
   `refuted`/`not-evaluable`/`partial` are computed exactly as before
   for every clause that did not previously crash. The only thing that
   changes is that a clause that PREVIOUSLY CRASHED (aborting the
   whole `evaluate_predictions` call, producing no verdict for ANY
   clause of ANY prediction in the run) now produces one.
2. **No committed sidecar moves**: ran `scripts/regen_sidecars.py`
   against all 30 committed `reports/*.interpretation.md` files —
   `30 sidecar(s), 0 failure(s)`, every one `fresh, unchanged`. None of
   them stamps a `predictions_file` for the six files in §0 (all were
   rendered without `--predictions`), so there was nothing for either
   the crash or the fix to move in a committed artifact.

Both together are exactly interpreter_v1.md §3.3's MINOR/no-bump case
("a fix that... edits zero characters of any rule's declared field...
and moves nothing a prior version emitted"), stronger even than MINOR:
nothing moved at all, comparable in every direction.

## 3. Regression coverage (`make check-interpret`)

New fixture-only predictions file `catalogue/fixtures/predictions-
kb24.tsv` (never a real prediction — same precedent as
`predictions-subject-grain.tsv`/`predictions-inexpressible.tsv`), one
clause `KB24A`: `quantity=delta_verdict; reducer=identity; op=eq-token;
selector=pattern=factored;regime_or_na=short-subject-search;
testee=pcrec_692c2e8_vm-caps-simdna`, against report "a" (the real,
committed email-specimen-0.1 repin-692c2e8 report), whose real cell at
that selector reads `delta_verdict = "faster ×1.19"`.

Two new `[[fixture]]` entries in `catalogue/fixtures/fixtures.toml`,
same base/control shape every other R-PRED pair uses:

- `R-PRED-1__kb24-identity-token-confirmed` — `hi="faster ×1.19"`
  (matches), `expect=["R-PRED-1"]`.
- `R-PRED-2__kb24-identity-token-refuted` — base of the above,
  `mutate_predictions` changes `hi` to `"unchanged (within spread)"`
  (does not match), `expect=["R-PRED-2"]`, `expect_not=["R-PRED-1"]`.

Both directions exercise `_measured_text`'s new `kind == "token"`
branch (the confirm path takes the `all-confirmed` half, the refute
path takes the `bad` half — both previously crashed identically, since
the crash was in `_measured_text` itself, called unconditionally on
BOTH outcomes). `gen.py --check` reproduces both from their
declarations byte for byte.

`make check-interpret`: **178 → 182 passed** (67 → 69 fixtures; +4 in
section 4, sections 1/2/3/5/6 unchanged) — confirmed the baseline count
by `git stash`-ing this change and re-running before restoring it.
`python3 catalogue/acceptance_10.py`: **25/25**, unchanged.
`make check-schema`: green, unchanged (73 sabotage rejections, 0 wrong).

## 4. Real-world verification (constraint 4)

Scored `docs/dev/predictions/capability-0.1-pin-25b1984f-confirm.tsv`
through the FIXED code via a direct `interpret.evaluate_predictions`
call (the same F27 bypass `docs/dev/lanes/b60pinconfirm_report.md` used
— this population is a second sample of an already-measured one, so
`check_stated_utc`'s re-anchor refuses the normal CLI `--predictions`
path for it; unrelated to KB-24):

| pred | verdict | n ranked | distinct non-"unchanged" tokens |
|---|---|---|---|
| P1 | refuted | 738 | faster ×1.01, faster ×1.02, slower ×1.00, slower ×1.01, slower ×1.04, slower ×1.07 |
| P2 | refuted | 750 | faster ×1.01, faster ×1.07, slower ×1.01, slower ×1.02, slower ×1.03 |
| P3 | refuted | 732 | faster ×1.00, faster ×1.01, slower ×1.00, slower ×1.01, slower ×1.04 |
| P4 | refuted | 732 | faster ×1.01, faster ×1.02, faster ×1.04, faster ×1.05, slower ×1.01, slower ×1.08 |

BYTE-IDENTICAL to the table in `docs/dev/lanes/b60pinconfirm_report.md`
§3 (the scratch-monkeypatched original) — verdict, ranked-value count
and the full distinct-token set match for all four predictions.
Verdict identity confirmed, per the charter's acceptance test.

## 5. Charter-vs-committed checklist

- [x] Fix `_reduce`/`_measured_text` string-safe for both branches —
      DONE (§1), candidate (a) chosen with reasoning stated, per
      interpreter_v1.md §7.2's reducer contract.
- [x] Versioning argued (§3.3 as amended by [B56]) — DONE (§2):
      code-only, no catalogue bump, no `INTERPRET_VERSION` bump; all 30
      committed sidecars regenerated and diffed byte-identical
      (empty diff).
- [x] `make check-interpret` grows a regression arm, both confirm and
      refute directions, demonstrated crashing pre-fix and clean
      post-fix — DONE (§3): reproduced the crash by hand once (§0)
      before the fix, both new fixtures pass post-fix, wired into the
      existing fixture/section-4 machinery.
- [x] Real-world verification against
      `capability-0.1-pin-25b1984f-confirm.tsv`, verdict identity vs
      `b60pinconfirm_report.md` — DONE (§4): byte-identical on all four
      predictions.
- [x] `make check-interpret` green in full (182/182) — DONE.
- [x] `make check-schema` as a smoke — DONE, green, unchanged.
- [x] KB-24 entry STATUS appended (fixed, by what, verified how;
      history preserved, not rewritten) — DONE,
      `docs/dev/known_issues.md`.
- [x] `pcrecbench/CLAUDE.md` updated if roles change — NOT UPDATED,
      deliberately: this is an internal bugfix inside `interpret.py`'s
      existing `_reduce`/`_measured_text` helpers, not a new file, a
      new module responsibility, or a change to what the module's
      CLAUDE.md entry already describes it as doing (a deterministic
      fact-finder over a report TSV + index; predictions scoring is
      already named there). No sentence in that file becomes false or
      stale.
- [x] Committed incrementally.
- [ ] Not merged — per the boilerplate, the manager merges.

## Commit list (branch `lane/b68kb24`, oldest to newest)

See `git log lane/b68kb24` — the fix (`pcrecbench/interpret.py`), the
fixture wiring (`catalogue/fixtures/fixtures.toml`,
`catalogue/fixtures/predictions-kb24.tsv`, the two generated fixture
directories), the KB-24 STATUS append, and this report.
