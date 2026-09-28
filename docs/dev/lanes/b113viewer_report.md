# b113viewer — "current engines only" checkbox, default ON ([B113])

Lane `b113viewer` (this session was already an isolated worktree at
launch — see "worktree deviation" below), branch `b113viewer`, off
master `e90d63a`.

Frank, 2026-09-28, verbatim: *"i want to have the 'current engine'
visibility a checkbox defaulting on. i sometimes want to compare to past
engines."*

## Worktree deviation from the brief, stated up front

The brief said `worktrees/b113viewer` on branch `b113viewer` (the
standing lane ritual, `docs/dev/lanes/BOILERPLATE.md` step 1). This
session's own harness had already placed it in a pre-existing isolated
worktree (`.claude/worktrees/agent-abd032cf05a33d2ec`) at launch, off
master `e90d63a`, before any instruction was read — the same isolation
mechanism the BOILERPLATE ritual achieves by hand, just assigned
automatically rather than created manually. Renamed that worktree's
branch from the harness's own `worktree-agent-abd032cf05a33d2ec` to
`b113viewer` to match the brief as closely as possible; the worktree
directory path itself could not be renamed from inside a session
sandboxed to it. Flagging this now rather than after the fact, per this
project's own convention (see `b107viewer_report.md`'s naming-deviation
note).

## Charter-vs-committed checklist (items 1-4 of the brief)

1. **DATA: re-export with `--all-pins`** — COMMITTED (`099b67c`).
   `viewer/data/` grew from 5.1 MB to **12 MB** — comfortably under the
   brief's ~25 MB stop threshold, so nothing was withheld. 12 sets
   exported (the 11 previously committed + `litrun@0.1`, a new 11-record
   set that landed in the store since the last export and was picked up
   incidentally by this regen, unrelated to `--all-pins` itself — noted,
   not investigated further, since this lane's scope is the checkbox).
   Run detached per the boilerplate's KB-16 discipline
   (`setsid`-equivalent via the Bash tool's tracked `run_in_background`,
   which — unlike a bare `setsid … & disown` — DOES notify on
   completion): `gnutimeout 2400 python3 tools/viewer_export.py
   --all-pins > /var/tmp/b113viewer/export.log 2>&1; echo "DONE
   rc=$?" >> /var/tmp/b113viewer/export.log`. Took **~29 minutes**
   wall (started 15:22:05Z, `DONE rc=0` observed ~15:51Z) — longer than
   b107viewer's ~12 min non-`--all-pins` full export, as expected
   (every pin's own record is now loaded and jsonschema-validated, one
   at a time, never the whole store at once — KB-16's own "never
   accumulate" rule holds; peak memory was not separately measured this
   lane, since the exporter's own docstring already states the
   one-record-at-a-time discipline that keeps it well below the
   report.py whole-store-load failure mode). A foreground bounded
   `until`-loop poll paired the wait (boilerplate's post-b54/b57
   fallback rule); its first attempt used a three-command chain whose
   background exit code reflected only its LAST command (`tail`, always
   0) rather than the poll's own timeout — a **false "done" read**,
   caught by checking the log's actual byte count before trusting it,
   fixed by re-polling with the `until`-loop as its own single
   background command so its exit code is load-bearing. Noted for
   whoever writes the next one.

2. **VIEWER: the checkbox** — COMMITTED (`e426b17`). `viewer/viewer.html`:
   - `state.currentEnginesOnly` in `defaultState()`, default `true`.
   - Hash key `ceo`; `hashToState()` reads `q.ceo === undefined ? true
     : q.ceo === "1"` — an OLDER persisted hash/`localStorage` state
     (no `ceo` key at all) defaults **ON**, never silently OFF, per the
     brief's own instruction (same posture as the pre-existing `nm`
     key, not `ee`'s absent-means-OFF one).
   - "Current" = the newest `testee_id` of its own **(family, variant)**
     identity, by `testeeIndex[id].newestDate` — the SAME rule
     `computeDefaultTesteeIds` uses, EXCEPT that arms are not dropped:
     an ablation/deny-flag/toolchain arm's own newest pin is current
     too (the brief's own instruction — "this applies to
     ablation/deny-flag arms too"). Both rules now share one grouping
     helper, `newestPerFamilyVariant(admit)` (an optional per-testee
     admit callback), rather than stating "newest per (family,variant)"
     twice — `computeDefaultTesteeIds` passes an `admit` that excludes
     arms, the new `currentTesteeIds` passes none.
   - When ON: `pickerEnumerableTesteeIds` narrows to current pins only,
     ON TOP OF (not instead of) "show engines with no data"'s own
     narrowing — hiding a non-current testee from both the family tree
     and the third-tier pin sub-picker; `displayedTesteeIds` (the
     matrix's own column list) now ALWAYS routes through
     `pickerEnumerableTesteeIds` (previously it special-cased
     `showEmptyEngines` ON as a direct-to-`visibleTestees()` shortcut;
     folding that shortcut into the shared function is a no-op when
     neither toggle would remove anything, and is what lets the new
     narrowing reach the matrix and the picker through one code path
     instead of two). A testee's own SELECTION (`state.testees`) is
     untouched either way — verified: the "Engines: n/N selected"
     count (which reads the raw selection) is IDENTICAL with the
     toggle ON vs OFF.
   - When OFF: every pin is listed/selectable again, including the
     third-tier pin sub-picker for a variant with more than one
     surviving pin.
   - "latest only" and "reset view" keep their existing meaning
     verbatim (both set the SELECTION via `computeDefaultTesteeIds`,
     untouched by this change) — verified: after "latest only", an
     ablation arm's own pin checkbox is still UNSELECTED (arms stay
     excluded from the selection default, distinct from "current").
   - The virtual "pcrec (auto)" column is unaffected by construction:
     `resolveVirtualAutoTestee` already always reads the newest pin of
     its resolved variant regardless of any display filter, and is
     appended to `displayedTesteeIds`'s result rather than routed
     through it.
   - Placement: immediately below "show engines with no data" in the
     Status filter group, as asked ("beside").
   - The "no engine has data" empty-state message now names both
     toggles (`… (see "show engines with no data" / "current engines
     only")`), since either can now be the cause.

3. **VERIFY** — COMMITTED, headless, real-browser confirmation OWED
   (see below). Two layers:
   - A synthetic `jsdom` fixture (`gen_fixture.py` + `test.js`, both in
     the session scratchpad, NOT committed — throwaway per this
     project's own convention for lane-local verification scripts):
     two (family,variant) identities each carrying an OLD/NEW pin
     pair — one canonical (`pcrec auto-caps-simdna`), one an ABLATION
     ARM (`pcrec auto-caps-simdna_noedge`) — plus one single-pin control
     family (`pcre2 jit-caps-simdna`), driven through `JSDOM.fromFile`
     with `runScripts:"dangerously"`. **All 10 checks passed**: default
     ON and correctly placed; picker (ON) lists exactly the 3 current
     ids (2 old pins hidden, the arm's own newest pin present); picker
     (OFF) lists all 5; with all 5 explicitly selected, the matrix
     shows the same ON/OFF split; the "n/N selected" count is unchanged
     by the toggle; an old hash with no `ceo` key defaults ON, explicit
     `ceo=0`/`ceo=1` honored either way; "latest only" still excludes
     the ablation arm from the selection.
   - A second script (`real_spotcheck.js`) ran the SAME real
     `viewer.html` against the REAL re-exported `viewer/data/` (item 1,
     above) — the "per-set current-vs-past count" the brief asked for,
     read off the page's own `window.BENCH._sets` and the picker's own
     DOM, not reimplemented:

     ```
     current engines only = ON:  44 testee ids enumerable in the picker
     current engines only = OFF: 126 testee ids enumerable in the picker
     => 82 non-current (older-pin) testee ids hidden by default
     ```

     | set | distinct testee_ids | current | past |
     |---|---|---|---|
     | altwide@0.1 | 6 | 2 | 4 |
     | altwide@0.2 | 25 | 9 | 16 |
     | bounded@0.1 | 10 | 2 | 8 |
     | bounded@0.2 | 10 | 2 | 8 |
     | bounded@0.3 | 32 | 11 | 21 |
     | capability@0.1 | 43 | 14 | 29 |
     | email-specimen@0.1 | 9 | 2 | 7 |
     | email-specimen@0.2 | 30 | 6 | 24 |
     | litrun@0.1 | 11 | 11 | 0 |
     | loglines@0.1 | 41 | 11 | 30 |
     | syntax@0.1 | 15 | 5 | 10 |
     | utf8@0.1 | 15 | 11 | 4 |

     The 82 hidden ids are every pre-current pcrec pin named in the
     top-level `CLAUDE.md`'s own status history (`8da6120` through the
     sha immediately before the live pin) — spot-checked by eye against
     that history and consistent with it. `litrun@0.1` shows 0 past
     because it is a brand-new set with only the live pin's own
     records.
   - **NOT verified**: a real (non-jsdom) browser session — this
     sandbox has no working headless Chromium under its snap
     confinement (unchanged from every prior viewer wave, `chromium
     --headless --dump-dom` still returns a sub-frame-error page, not
     confirmed, but not tried again since v1.1/v1.3 already established
     this box's limitation is stable and not code-dependent) — this is
     Frank's own to give five minutes, per the standing note in every
     prior viewer lane's report.
   - **One jsdom-only artifact found, NOT a page bug** (same posture as
     the pre-existing `var()` artifact §11 already documents):
     `persist()`'s `history.replaceState()` call is not
     `try/catch`-guarded (unlike the `localStorage.setItem` two lines
     below it in the same function) and jsdom throws a `SecurityError`
     from it on every state change against a `file://` document. It
     fires AFTER `persist()`'s own render calls (`renderFilters` /
     `renderControls` / `renderTable`) have already completed, so it
     never corrupted a check in either script above; confirmed harmless
     by isolating a bare `history.replaceState` call against a minimal
     jsdom document outside `viewer.html` before concluding it was
     jsdom's own restriction and not a real one (real browsers permit
     same-document `replaceState` on `file://` freely). Not fixed — out
     of this lane's charter, and `persist()`'s existing behavior is
     unchanged in any environment that does not throw here.

4. **DOCS** — COMMITTED (`e426b17`).
   - `viewer/CLAUDE.md`: new "v1.4 amendments" section (mirroring the
     v1.1/v1.3 sections' own voice), plus the "Regenerating" block
     rewritten to state the new Makefile default and the direct-call
     escape hatch for the old newest-pin-only export.
   - `docs/design/results_viewer_v1.md`: new §12, "v1.4 amendments",
     with the same content in the design note's own fuller voice
     (including the shared-helper refactor rationale and the full
     verification paragraph).
   - `Makefile`: `viewer-data` target now passes `--all-pins`
     unconditionally (`$(PYTHON) tools/viewer_export.py --all-pins
     $(ARGS)`), with an updated comment; `ARGS` still layers on top
     (e.g. `--sets loglines` for a dev slice, still all-pins). The old
     newest-pin-only behavior is reachable by calling
     `python3 tools/viewer_export.py` directly (no Makefile), which is
     stated in both docs.

## What was NOT run

- `make check` (explicitly excluded by the brief — "this lane is
  light, do NOT run the full `make check`"). This lane touches
  `viewer/viewer.html`, `viewer/data/*.js`, `viewer/CLAUDE.md`,
  `docs/design/results_viewer_v1.md`, and `Makefile`'s `viewer-data`
  target only — none of `bench/`, `schema/`,
  `pcrecbench/harness.py`/`adapters.py`/`report.py`, or `testees/`,
  which is what `make check`'s sections gate; the viewer carries no
  `make check` target by design (`docs/design/results_viewer_v1.md` §6
  scope fence).
- `node --check` WAS run on the extracted inline `<script>` (syntax
  pass, clean) before the jsdom verification, the same static check
  every prior viewer wave used as a first gate.
- A real-browser confirmation (OWED to Frank, as in every prior viewer
  wave — stated above).

## Files touched

- `viewer/viewer.html` — the checkbox, the shared
  `newestPerFamilyVariant` helper, `pickerEnumerableTesteeIds`/
  `displayedTesteeIds` composition, hash read/write, empty-state
  message.
- `viewer/data/*.js`, `viewer/data/manifest.js` — re-exported
  (`--all-pins`); `viewer/data/litrun@0.1.js` newly added.
- `viewer/CLAUDE.md`, `docs/design/results_viewer_v1.md` — v1.4
  write-up.
- `Makefile` — `viewer-data` target default.
- `docs/dev/lanes/b113viewer_report.md` — this file.

## Commits

- `e426b17` — code + docs (checkbox, Makefile default, both write-ups).
- `099b67c` — the `--all-pins` data re-export.

Branch `b113viewer` is ready for the manager to merge. No further
long-running work is owed from this lane; the export (the one item that
could have exceeded the ~4-minute DO-THEN-FINISH threshold) already
completed and is committed, so nothing is left OWED to a follow-up
agent.
