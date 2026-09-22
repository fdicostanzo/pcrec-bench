# Lane `b72smalls` — delivery report

Branch `lane/b72smalls`, worktree `worktrees/b72smalls`, off `master` at
`04f7b04` (the twenty-ninth session's [B71] collection). Five "parked
smalls" from the wake queue, per the brief: implement each if mechanical,
stop and report the open question if it needs a ruling.

## Charter-vs-committed checklist

1. **KB-21's describe()-vs-schema smoke arm.** BUILT.
   `tools/selfcheck.py:check_describe_schema_shape` (commit `29df1e8`).
2. **KB-25's check-report growth fix.** BUILT AND MEASURED.
   `pcrecbench/tests/test_report.py`'s `_load_real_store` (commit
   `e105db5`).
3. **The rust diagnostic-truncation nit.** BUILT (KB-26).
   `testees/rust/src/main.rs` + `testees/rust/adapter.py` +
   `tools/selfcheck.py:check_rust_multiline_diagnostic` (commit
   `0cdc266`).
4. **The vectorscan NMATCHES gap.** BLOCKED-ON-RULING — not built, per
   the brief's own instruction ("if it is an instrument-design question
   ... report it as such and stop"). Question below.
5. **b47subgrain's two OWED load checks (§6 Q6).** BUILT AND TESTED
   (commit `ac583bb`), but building them surfaced a SECOND,
   newly-discovered BLOCKED-ON-RULING conflict, distinct from the one
   the report's line ~183 already named (that one was about item 8's
   `--subject-grain` auto-passing, not this item). Question below.

`make check-harness` is the OWED, detached, LAST act — see "Owed to
merge" at the bottom.

---

## 1. KB-21's describe()-vs-schema smoke arm — BUILT

`docs/dev/known_issues.md` KB-21 (line ~974): the re2 `runtime_options`
bare-string bug was fixed same night; the parked follow-up asked for a
check arm that validates a discovered adapter's `describe()` block
against the schema's own `setup.testee` shape, in the smoke tier, so the
next such mismatch fails `make check` rather than a measured cell at
`store.write`.

`tools/selfcheck.py:check_describe_schema_shape` (wired into `main()`
right after `check_kb1_runtime_options`):

- **Positive sweep**: for one representative testee of EVERY discovered
  adapter (onig, pcre2, pcrec, re2, rust, tre, vectorscan — ~9 s total on
  this box), `describe()`'s own block is mirrored through the exact two
  steps `record.build_setup` performs before writing it (`tier` popped,
  `testee_id` DERIVED via `record.derive_testee_id` since `describe()`
  never carries it) and validated against `schema/record.schema.json`'s
  `$defs/setup/properties/testee` sub-schema.
- **Negative, both directions, on the REAL re2 adapter's REAL
  `describe()` block** (not a hand-typed stand-in): `runtime_options`
  reverted to the exact KB-21 bug shape (`["longest_match=true"]`) is
  refused BY NAME (`runtime_options.0: 'longest_match=true' is not of
  type 'object'`); the unmodified (fixed) block validates clean as the
  control.

`docs/dev/known_issues.md` KB-21 updated in place with the fix. Verified
standalone (3/3 PASS); not yet re-verified inside the full
`make check-harness` run at time of writing this report (see "Owed to
merge").

## 2. KB-25's check-report growth fix — BUILT, MEASURED

`docs/dev/known_issues.md` KB-25's own remedy sketch named two
candidates: "scope the live-store arm to an index-prefiltered slice" or
"move the live-store validation to a separate non-default target". Built
the first — the SAME mechanism KB-16 already proved correct for a real
CLI query (`report.discover_index` + `report.index_row_could_match`,
reused, not reimplemented).

`pcrecbench/tests/test_report.py`'s `_load_real_store()` used to
`discover_records` (every path in `store/`, any sub-bench) then
`load_all` (jsonschema-validate every one), even though every REAL_STORE
`build_report` call site in this file already filters to
`subbench="email-specimen"` — grep-confirmed, seven call sites, all of
them. Now it prefilters to that subbench BEFORE opening a file, and
caches per subbench rather than once.

**Measured before/after on this box, same store (217 records, 48
email-specimen), via `make check-report` (which also runs
`test_quick`/`test_matrix_page`/the CLI smoke):**

| | wall | user | max RSS | pass/fail |
|---|---|---|---|---|
| BEFORE (unmodified, `/var/tmp/b72smalls_checkreport_BEFORE.log`) | 26:03.46 | 1548.70s | 7,667,420 KB | 84+7+8 passed, 0 failed |
| AFTER (this fix, `/var/tmp/b72smalls_checkreport_AFTER.log`) | 5:25.80 | 322.58s | 1,411,056 KB | 84+7+8 passed, 0 failed |

**×4.8 faster wall, ×5.4 less peak RSS, identical pass/fail counts on
both runs** — only what the suite loads moved, never what it asserts
(the brief's own constraint). `docs/dev/known_issues.md` KB-25 and
`pcrecbench/tests/CLAUDE.md` both updated with the table. The two raw
`/usr/bin/time -v` logs are ephemeral (`/var/tmp/`, not committed) —
the numbers above are transcribed verbatim into both committed docs, so
nothing is lost if they are cleaned up.

## 3. The rust diagnostic-truncation nit — BUILT (KB-26)

`docs/dev/lanes/b69census_report.md` §4 (lines ~129-138) found
`rust-default`'s `did-not-compile` diagnostic stubbed to
`"regex build failed [Syntax]: regex parse error:"`, the actual parser
detail dropped, and named it "worth a `testees/rust/CLAUDE.md`-side fix"
without diagnosing WHERE the truncation happened.

**Root-caused**: not in the reporter (KB-18 already fixed a DIFFERENT
truncation, downstream, in already-stored records) but in the DRIVER
PROTOCOL's transport. `regex::Error`'s own `Display` is genuinely
multi-line (reproduced live on `(abc`: four physical lines — a header, the
offending snippet, a caret, a one-line summary), and
`pcrecbench.driverrun.run_driver` reads a driver's stdout ONE PHYSICAL
LINE at a time (`proc.stdout.splitlines()`); every physical line after
the diagnostic's first carried no recognizable `kind<TAB>...` prefix, so
`pcrecbench.adapters.parse_driver_line` silently dropped it before the
text ever reached a record.

Fixed at two points:

- `testees/rust/src/main.rs`'s new `escape_for_transport` folds a
  multi-line message into ONE physical line before writing it (backslash
  escaped first, then the two line-break bytes) — applied at all four
  dynamic `error<TAB>...` emission sites.
- `testees/rust/adapter.py`'s new `_unescape_driver_text` undoes it, once,
  immediately after `run_driver` returns — scoped to THIS adapter's own
  driver text only, so no other engine's diagnostic is reinterpreted.

`tools/selfcheck.py:check_rust_multiline_diagnostic` (wired into
`main()` after `check_high_byte_pattern_argv`): the `(abc` witness now
carries the offending snippet, the caret line AND the summary (not just
the truncated header); an ordinary single-line diagnostic is unaffected
(the control); `_unescape_driver_text` is proven reversible directly,
including the edge case where a real backslash sits immediately beside a
real newline in the original message. Verified standalone: 3/3 PASS.
`testees/rust/CLAUDE.md` and `docs/dev/known_issues.md` (new entry
KB-26) both updated.

## 4. The vectorscan NMATCHES gap — BLOCKED-ON-RULING, not built

`docs/dev/dev_journal.md` line ~4688 names it as a remaining item;
`testees/vectorscan/CLAUDE.md`'s own "`NMATCHES` (throughput regime):
also unavailable, also honest" section (lines ~149-163) already states
the finding in full: Hyperscan's `nosom` (no start-of-match) block-mode
scanner is an ALL-MATCHES streaming scanner, not a single-match engine —
it reports every match END-offset (unordered, for assertion-bearing
patterns), which is neither "first match" nor the driver protocol's
existing `--find-all` NON-OVERLAPPING count (KB-17's advance rule, which
needs each match's START offset to de-duplicate, and this config
structurally does not have one). `driver.c` already accepts `--find-all`
for protocol compliance but always prints `NMATCHES = -`, honestly.

**This is an instrument-design question, not a mechanical gap**, per
`docs/dev/research/2026-09-12-b42-engine-landscape.md` §2.2's own
diagnosis (quoted in `testees/vectorscan/CLAUDE.md`): "the driver
protocol itself needs a THIRD invocation mode or a declared variant that
restates the expectation in all-ends terms." Two of the three ways to
close it either defeat the `nosom` config's own purpose (enabling
`HS_FLAG_SOM_LEFTMOST` would give a real non-overlapping count but stop
measuring the SOM-free fast path this config exists to measure) or invent
a NEW reduction over end-offsets alone that is not the same quantity
every other engine's `NMATCHES` reports (a raw end-offset count
double-counts overlapping starts a non-overlapping rule would collapse) —
a new definition needs a ruling, not a lane's guess. Not touched.

**The question for whoever picks this up**: should the driver protocol
grow a third invocation mode / a declared "all-ends" expectation variant
(`record_schema.md §5`'s `all-ends` convention, already named for exactly
this engine) so Hyperscan's NMATCHES can be measured on its own terms
instead of being forced into the existing non-overlapping-count shape? Or
should `nosom`'s `NMATCHES` stay permanently `-` and a SEPARATE
`vectorscan-block-som` config (documented, not yet wired — see
`testees/vectorscan/CLAUDE.md`) carry `HS_FLAG_SOM_LEFTMOST` and answer
the existing NMATCHES shape instead? Either is a real, buildable answer;
neither is this lane's to pick.

## 5. b47subgrain's two OWED load checks (§6 Q6) — BUILT, TESTED, and a
   NEW conflict found and filed

`docs/dev/lanes/b47subgrain_report.md` line ~62: "Both load checks the
note specifies (§6 Q6). NOT BUILT — OWED." `docs/design/
interpret_subject_grain_v1.md` §6 Q6 (line ~838) is RULED YES, both,
under Frank's "fail loudly generally" posture:

- **(i)** a `compile:` quantity's selector may not name `subject_or_na`
  or `regime_or_na` (Cause B: the report's `compile` section carries
  neither dimension — `render_tsv` writes the empty string there, never
  `n/a`).
- **(ii)** every `testee=` glob must match ≥1 MEASURED index testee for
  its own `(subbench, version)`, vacuous when unmeasured (Cause C:
  `testee=pcrec_*-auto-*` matches nothing real — a real testee_id has an
  UNDERSCORE before `auto`, not a hyphen).

Both built in `pcrecbench/interpret.py`, exactly as specified,
store-free (check (ii) reads `index.rows` only, never a record), wired
into `interpret()` right after `load_predictions`. Two new fixture files
(`catalogue/fixtures/predictions-compile-scope.tsv`,
`-testee-glob.tsv`) exercise both checks' clean/sabotage/vacuous arms
directly in `check_interpret.py` section 1, mirroring the
`predictions-utc-before/after.tsv` precedent. `make check-interpret`:
**190 passed, 0 FAILED** (was 155).

**The report's own line ~183 mentions a design question — checked, and
it is NOT this item's own question**: that line is about item 8 (whether
the `/pcrec-bench-interpret` skill should auto-pass `--subject-grain`),
explicitly flagged as "a design question for whoever picks up item 8's
owed decision, not answered here" — a different, still-open item this
lane was not asked to touch.

**But implementing Q6 (i) exactly as ratified surfaced a GENUINE, NEW
conflict, found only by actually running the check against the real
corpus, not anticipated by either report:**

`docs/dev/predictions/capability-0.1-first.tsv`'s real, already-committed
clauses P2.a and P2.b carry EXACTLY the Cause-B defect shape Q6 (i)
exists to catch (`regime_or_na=n/a` against a `compile:` quantity) —
this is the SAME file, SAME defect, the design note itself diagnosed
when it recommended Q6 in the first place. Loading it now raises. That
by itself would be fine (the check is working as ratified) — except
`docs/dev/predictions/CLAUDE.md`'s own entry for this exact file states
this project's rule in plain language: *"Predictions are stated-PRE-RUN
artifacts ... and this format defines no revision mechanism for an
already-scored file"* — the file is explicitly NOT to be edited, ever,
even though its own recommended fix has been sitting written-up and
verified since 2026-09-17 (`docs/dev/lanes/b42predhyg_report.md`).

Worse: FOUR committed `reports/*.interpretation.md` sidecars are stamped
`predictions: docs/dev/predictions/capability-0.1-first.tsv`
(`2026-09-17-...-first-a770139e`, `2026-09-18-...-after-cf0962e3`,
`2026-09-18-...-ext-first-cf0962e3`, `2026-09-19-...-ext-second-
cf0962e3`), so `interpret()` now permanently refuses to regenerate ANY of
them — breaking `catalogue/CLAUDE.md`'s own stated invariant, "every
bump regenerates every committed sidecar in the same commit."

**Three of this project's own standing rules are now in genuine
tension, and picking among them is a ruling, not a lane's call:**

1. Q6 (i)'s "fail loudly generally" posture (ratified).
2. Predictions files are immutable once scored (`docs/dev/predictions/
   CLAUDE.md`'s stated rule).
3. Every committed sidecar must stay regenerable / byte-identical-checked
   (`catalogue/CLAUDE.md`'s stated rule).

**Filed, not silently absorbed.** `catalogue/check_interpret.py` carries
a narrow, explicit, well-documented STOPGAP so `make check-interpret`
stays green (190/190) WITHOUT hiding the gap: section 1 excepts EXACTLY
`capability-0.1-first.tsv`'s P2.a/P2.b (and asserts, both directions,
that they fail with Q6 (i)'s own reason and nothing else — no other file
gets a pass); section 3 names the four blocked sidecars explicitly
(`_SIDECARS_BLOCKED_ON_CAPABILITY_FIRST_RULING`) and reports them in a
SEPARATE count, never folded into "fresh". Both blocks carry inline
comments citing this exact conflict and its three colliding rules.
**This does NOT fix the underlying tension for real usage** — the actual
`/pcrec-bench-interpret` skill and `scripts/regen_sidecars.py` would hit
the identical `PredictionError` today if asked to refresh any of these
four sidecars for real.

**The question for whoever rules on it**: how should Q6 (i)'s load
check, the predictions-immutability rule, and the sidecar-regeneration
invariant reconcile for this one historical file (and its four
sidecars)? Candidates, not a recommendation: (a) treat this as the one
narrow, permanent, NAMED exception this lane's stopgap already encodes,
formalized instead of provisional; (b) decide that fixing an
ALREADY-DIAGNOSED, ALREADY-WRITTEN-UP authoring defect (not a
re-prediction, not a changed verdict — the numbers this file predicted
never move) is NOT the kind of revision the immutability rule was meant
to forbid, and apply `b42predhyg`'s already-verified fix to the file
after all; (c) some other resolution this lane did not consider.

---

## Verification run

- `check_describe_schema_shape` standalone: 3/3 PASS.
- `check_rust_multiline_diagnostic` standalone: 3/3 PASS (and confirmed,
  by hand, that the pre-fix truncated diagnostic WOULD have failed it —
  the check has teeth).
- `make check-schema`: 5 examples accepted, 73 sabotages rejected for
  their own rule, 0 wrong.
- `make check-interpret`: 190 passed, 0 FAILED (was 155; +35 from this
  lane's Q6 fixtures/checks).
- `make check-report`: rc=0, 84+7+8 passed both before and after KB-25's
  fix (measured, see item 2 above).
- `make check-harness`: **OWED TO MERGE**, launched DETACHED per
  DO-THEN-FINISH — see below.

## Owed to merge

`make check-harness` (~20 min; touches `tools/selfcheck.py`,
`testees/rust/`) is running DETACHED:

    log:    /var/tmp/b72smalls_check.log
    marker: the exact line "B72 CHECK DONE rc=<n>" appended to that log

Check with `tail -5 /var/tmp/b72smalls_check.log` or
`grep "B72 CHECK DONE" /var/tmp/b72smalls_check.log`. Not a harness-
tracked task (launched via `setsid ... & disown`) — no completion
notification will arrive; a fresh agent or the manager must poll the
marker. If it fails, the two most likely causes given this lane's own
changes: `check_describe_schema_shape` or `check_rust_multiline_
diagnostic` (both new, both verified standalone above but never run
inside the FULL suite alongside 300+ other checks that build/prepare
adapters in sequence).

## Delivery

Branch `lane/b72smalls`, four commits (`29df1e8`, `0cdc266`, `ac583bb`,
`e105db5`), all incremental, all with their own CLAUDE.md/known_issues.md
updates in the same commit. Working tree clean. Not merged (the
manager's job); not pushed.
