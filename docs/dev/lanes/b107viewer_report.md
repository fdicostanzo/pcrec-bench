# b107viewer — Frank's viewer feedback (2026-09-27), v1.3

Lane `b107viewer` (Sonnet), writer, worktree `worktrees/b107viewer`,
branch `lane/b107viewer` off master `5f1b2e3`.

## Naming deviation from the brief, stated up front

The brief said to write this up as design-note "§10 'v1.2'". §10 of
`docs/design/results_viewer_v1.md` already exists and is titled
"v1.2 amendments ([B70], Frank's rulings 2026-09-21 evening)" — a
different, already-implemented, already-committed round of work (the
refusal-fold/classify items). Overloading that title with this wave's
seven items would either silently rewrite committed history or attach
unrelated content to an existing version label, both against this
project's own versioning conventions. I wrote this wave as **§11,
"v1.3 amendments"** instead — the next number in the doc's own
sequence (§9=v1.1, §10=v1.2, §11=v1.3) — and `viewer/CLAUDE.md` follows
suit. Flagging this now rather than after the fact.

## Charter-vs-committed checklist (items 1-7 of the brief)

1. **Sticky pattern-name column, incl. header corner cell** — COMMITTED.
   `viewer/viewer.html`: new `.corner-head` CSS rule (`left:0;
   z-index:20`), applied to both the band row's blank corner
   (`th.rowhead-band`) and the col-labels row's "set / pattern" header;
   the body's `th.rowhead` was already sticky-left and is unchanged.
   Verified via jsdom: `corner-head count: 2` in every render.
2. **Row-relative, log-interpolated, adjustable colour scale** —
   COMMITTED. `colorForRatio(ratio, anchors, n, m)`: full green at
   `ratio<=1`, log-space to white at `N` (default 2), log-space to red
   at `M` (default 10), flat red above; anchors are ONE-LEVEL ALIASES
   of `--best-bg`/`--bg-panel`/`--status-wrong-bg` (never new hex
   literals); N/M are two number inputs in a new legend
   (`#colorscale-legend`), persisted in `localStorage`
   (`pcrecbench-viewer-colorscale`, try/catch-guarded, kept OUT of the
   hash-serialized `state`). Non-measured cells are untouched (their
   existing chip styling stands). Verified numerically against
   hand-computed lerps (e.g. ratio 200/150=1.333 → rgb(239,248,240),
   confirmed by direct arithmetic on the anchor RGB triples).
3. **Engine panel scroll/focus preservation** — COMMITTED.
   `captureEnginePanelState()`/`restoreEnginePanelState()`, called from
   `renderFilters` (capture BEFORE `#filters.innerHTML=""` runs) and
   `renderEnginePicker` (restore after the new panel is built). Every
   control in the panel carries a stable `data-focus-key` (never a DOM
   index). Verified via jsdom: `scrollTop` set to 42, a family checkbox
   toggled (forcing a full panel rebuild — `panel replaced (new
   object): true`), and both `scrollTop` (42) and `document.activeElement`
   (the SAME `data-focus-key`, on a brand-new DOM node) survive.
4. **Category selectors (encoding / captures / family) + one hover-help
   line** — COMMITTED. `capsToken()`/`encodingOf()` (engine-neutral,
   read off testee_id's own config_slug segment and its `_utf8` suffix);
   `renderCategoryRow()` is the shared tri-state row builder used by
   BOTH new selectors and (unchanged) the family tree. The `caps` row's
   `title` carries Frank's sentence verbatim. Verified: category rows
   render as `byte`/`UTF-8`/`caps`/`nocaps`/`both` with correct
   membership and coverage chips; the hover title is present exactly on
   the `caps` row.
5. **Hide empty engines (default off)** — COMMITTED.
   `nonEmptyTesteeIds`/`pickerEnumerableTesteeIds`/`displayedTesteeIds`:
   a pure DISPLAY filter over the CURRENT filtered `groups`, never a
   change to `state.testees` or the picker's own "n/N selected" count.
   Verified: filtering to a pattern one pcre2 config never measured
   drops that config from both the matrix columns and every picker
   listing by default (`jit-caps present: false`), with its `0/1`
   coverage chip visible again the moment the new "show engines with no
   data" checkbox (Status section) is checked.
6. **Category click semantics** — COMMITTED, and turned out to need NO
   new logic: it is the native `<input type=checkbox>` click behavior on
   an indeterminate/unchecked vs. fully-checked control, which the
   EXISTING family tree already relied on; stated once in
   `renderCategoryRow`'s own comment rather than re-derived per caller.
   Verified: a fully-selected "both" captures row goes to 0/4 selected
   after its (simulated) click.
7. **Virtual "pcrec (auto)" column** — COMMITTED, on by default.
   `familyCapsNocapsIndex(fam)` is GENERIC (any family with a
   caps/nocaps pair per encoding); `VIRTUAL_AUTO_FAMILY = "pcrec"` is the
   one constant naming which family this page asks it about today.
   `resolveVirtualAutoTestee(g)` picks caps vs. nocaps by the pattern's
   own `captures` count ([B107] exporter addition, below), falls back
   to caps when that count is `null`/unknown, and picks the newest pin
   via the SAME `pinsByDate()` the pin sub-picker already uses.
   `injectVirtualAutoCells(groups)` ALIASES the resolved real cell
   object under a NUL-prefixed synthetic key
   (`VIRTUAL_AUTO_TESTEE_ID = "\u0000virtual-pcrec-auto"`, provably
   distinct from every real schema-slug testee_id) — never a copy, so
   it participates in `computeBest`/the colour scale/sorting exactly
   like an ordinary tied column, per the design note's own "no special
   dedup" ruling; a synthetic `excluded`-status placeholder (never a
   blank cell) explains a missing pair or an unmeasured row. The
   tooltip states which real testee_id was read and why. Verified: a
   2-capture pattern resolves to the caps config's own number, a
   0-capture pattern to nocaps's, an unknown-captures pattern falls
   back to caps with the fallback sentence in its tooltip, and the
   virtual cell's own colour matches its resolved real cell's ratio
   exactly (including landing on full green when it ties the row's
   best).

   **Exporter change** (the one item 7 needed):
   `tools/viewer_export.py`'s `_pattern_capture_count(canonical_text)` —
   `PCRE2_INFO_CAPTURECOUNT` over the pattern's FULL `canonical_text`
   (never the ~2 KB popover cut), re-encoded to UTF-8 bytes itself
   (bypassing `oracle_pcre2.compile`'s `str`→`latin-1` auto-encode,
   which would corrupt a non-Latin-1 character like `café`/`Москва`);
   `None` when the text is omitted or the pattern does not compile
   stand-alone. `pcrecbench/oracle_pcre2.py` gained the constant
   (`PCRE2_INFO_CAPTURECOUNT = 4`, matching the real `pcre2.h` on this
   box) and `capture_count(compiled)`, plus a three-case self-check
   (`(a)(b)`→2, `(?:a)`→0, `(?<x>a)`→1). Verified: the self-check passes
   (`python3 pcrecbench/oracle_pcre2.py`); a direct call test on `café
   résumé` (0) and `Москва (в)` (1) confirms non-Latin-1 safety; a
   `make viewer-data --sets loglines` regen diffed against the
   committed file shows `captures` as the ONLY new field on every
   pattern entry, every row byte-identical otherwise, and the manifest
   moved by nothing but its own timestamp (`--keep-existing-manifest`
   used, confirmed 11/11 sets preserved). This regen was NOT committed
   (a partial single-set export would leave `captures` populated on
   only one set while every other set's patterns lack it) — see OWED
   below.

## Validation

- `node --check` on the extracted inline script: clean, both before and
  after every edit in this wave.
- `python3 -m py_compile` + `ast.parse` on both changed `.py` files:
  clean.
- `python3 pcrecbench/oracle_pcre2.py`: the module's own self-check,
  including the three new `capture_count` assertions: all OK.
- Headless Chromium in this sandbox refused to render a `file://` page
  at all under its snap confinement (`--headless --dump-dom` returned a
  browser-internal sub-frame-error page, not the viewer's own DOM;
  `chromium`/`chromium-browser` both resolve to the same confined snap;
  not pursued further — a sandbox limitation, not a lane finding). Used
  **jsdom** instead (`npm install jsdom`, `/tmp/jsdomtest`):
  `JSDOM.fromFile(..., {runScripts:"dangerously", resources:"usable"})`
  against a synthetic multi-row fixture (captures 0/1/2/unknown across
  four patterns, a pcrec caps/nocaps pair, a pcre2 jit/dfa pair) driving
  the REAL `viewer.html` end to end: DOM inspection + `dispatchEvent`
  for clicks/changes/hover, covering all seven items (scripts kept
  under `/tmp/vtest/`, not committed — scratch, per the mandate).
  One jsdom-only artifact was found and is NOT a page bug, confirmed by
  isolating it against a bare stylesheet before concluding: jsdom's
  `getComputedStyle` does not resolve a NESTED `var()` reference (a
  real browser does, per the CSS Custom Properties spec — this is
  exactly why `--scale-good: var(--best-bg)` was chosen as an alias
  over a duplicated hex literal); `resolveCssVarOnce` in `viewer.html`
  now resolves that one level itself defensively, which cost nothing to
  add and let the jsdom harness verify the real colour arithmetic
  end-to-end rather than only its shape.
- `tools/viewer_export.py --sets loglines --keep-existing-manifest`:
  see item 7 above. Reverted from the working tree after diffing (not
  committed).

## Not run / OWED

- **The full `make viewer-data` regen** (every set, so `captures` lands
  on every pattern's exported entry, not just loglines's) is OWED to
  whoever holds the box next — per the boilerplate, a store-loading run
  this size (~12 min) is the manager's/a detached job's to launch, and
  `b104read` was reported as concurrently rendering reports (also a
  store load) at lane start. Command:
  `python3 tools/viewer_export.py` (no `--sets`, no `--all-pins` —
  matches the committed `viewer/data/`'s own newest-pin convention),
  from the repo root, log path and `.done` marker at the manager's
  discretion. Numbers owed: the full per-set `captures` population
  (every set's own capture-count census) and a fresh page-load spot
  check against the regenerated data.
- Real-browser (non-jsdom) confirmation of the seven items is likewise
  OWED — the sandbox's chromium refusal is stated above; a session with
  a working headless Chromium (or a person's own browser) should give
  this five minutes before calling it fully closed.
- `make check` was NOT run (this lane touches no `bench/`, `schema/`,
  `pcrecbench/harness.py`/`adapters.py`/`report.py`, or `testees/` file
  — only `pcrecbench/oracle_pcre2.py` (additive, self-checked in
  isolation), `tools/viewer_export.py` (no test suite references it),
  and the viewer itself, which carries no `make check` gate by design —
  "the viewer is a reading aid, never a gate", `tools/CLAUDE.md`'s own
  words for `make viewer-data`). If a reviewer wants the belt-and-
  suspenders full suite anyway, it is safe to run and expected green.

## Files touched

- `docs/design/results_viewer_v1.md` — §11 written FIRST, before any
  code (per the brief's own instruction).
- `pcrecbench/oracle_pcre2.py` — `PCRE2_INFO_CAPTURECOUNT`,
  `capture_count()`, self-check.
- `tools/viewer_export.py` — `_pattern_capture_count()`, wired into
  `export_rows_for_record`'s `patterns_meta` construction, module
  docstring updated.
- `viewer/viewer.html` — all seven items.
- `viewer/CLAUDE.md`, `tools/CLAUDE.md`, `pcrecbench/CLAUDE.md` — role
  updates for the above.
