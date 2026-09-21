# b67viewer — the results viewer's v1.1 fix wave, lane report

Branch `lane/b67viewer`, built against `docs/design/results_viewer_v1.md`
§9 (Frank's eight 2026-09-21 review notes, arriving in three waves over
the day) on top of the merged v1.0 (`lane/b66viewer`, `viewer/viewer.html`
+ `tools/viewer_export.py`). Not merged; the manager merges.

## Charter vs. committed, item by item

**9.1 (BUG, priority 1): deselecting an engine/variant must remove its
column immediately; deselecting a family removes the band; no duplicate
columns under any selection sequence.** DONE, and the ROOT CAUSE is one
layer further down than the brief's own suspect ("per-pin variants
rendering as extra columns independent of the tree's selection keys").
The real cause lives in `tools/viewer_export.py`: `_engine_variant()`
built its display label from only `engine_mode` + `config_extra`,
dropping the `captures` axis entirely. `pcrec-auto` (captures=on) and
`pcrec-nocaps` (captures=off) both have `engine_mode="auto"` and no
`config_extra`, so BOTH produced the label `"auto"` — two distinct
`testee_id`s sharing one tree leaf. The v1.0 tree recovered a
`testee_id` at click time by reverse-scanning `testeeIndex` for
`(family, variant, pin)` and returning the FIRST match — so a
family-level deselect, which discovers its member ids by walking that
same lossy tree, could only ever find ONE of the two ids sharing a
label; the other survived every "deselect this family" click untouched,
and both ids' header columns carried the identical visible label (read
by a person as "duplicate columns" — they were not byte-identical
columns, but indistinguishable ones).

Fixed at the source, not patched at the symptom: `engine_variant_for()`
(new in `tools/viewer_export.py`) reads `testee_id`'s OWN config_slug
segment — `schema/validate.py`'s `derive_testee_id` builds
`testee_id = "<engine>_<version>_<engine_mode>-<caps>-<simd>[_<config_extra>]"`,
so everything after the second underscore is already a per-testee-id
UNIQUE identity, by construction (two testees with the same segment
would be the same testee_id). `viewer.html`'s domain tree was rebuilt to
match: `variants[v].pins[pin]` now stores the REAL `testee_id` straight
from the row that produced it, never reconstructed later — the old
`testeeIdOf()` reverse-scan function (and its "unreachable in practice"
fallback, which was in fact reachable whenever two testee_ids collided)
is gone. Family/variant checkbox handlers read ids directly off this
map.

A REAL SIDE-EFFECT of the fix, found while testing it (not a bug): the
domain tree can legitimately grow a THIRD (pin-picker) tier for a
variant even on the DEFAULT (non-`--all-pins`) export, when different
SET VERSIONS were each last measured at a different pcrec pin — e.g.
`email-specimen@0.1`'s newest `pcrec-auto` record and `@0.2`'s are two
different pins, so `auto-caps-simdna` under `pcrec` renders two pin
rows. v1.0's own report had assumed this path was "unexercised by the
committed data" (its Deviation #1); it is exercised, on the real store,
today (`libpcre2`/`pcrec` families both hit it in the committed export).

**9.2: column headers show the ordered DATE (newest measured_utc,
YYYY-MM-DD) instead of the pin; the pin moves to the tooltip; any pin
list orders by date.** DONE. `testeeIndex[id].newestDate` is computed
once in `buildDomain()` (domain-wide, over every row that testee_id
carries across every loaded set — not filter-dependent, so the label and
any pin-picker's order stay stable as filters change). Header label:
`<date> · <n>/<N>` (the coverage chip rides along, §9.3); `title`
becomes `"<testee_id> · pin <pin>"`. The pin sub-tier (when a variant
carries more than one pin) sorts by that same date, newest first. Minor
addition beyond the literal ask: a single-pin variant's own `<label>`
now also carries its sole `testee_id` as a `title` (useful for hover,
and for a test to address a single-pin leaf without guessing an id).

**9.3: per-engine coverage chip (n/N of the CURRENT filtered rows with
measured data).** DONE, at three places: the family row (OR across its
testees — "does this engine have anything here at all"), each
single-pin variant leaf, each pin sub-row, and the column header.
`rerenderAll()` now computes `filteredRows()`/`buildMatrixRows()` ONCE
and threads the same `groups` into both `renderFilters(groups)` and
`renderTable(rows, groups)`, so the filter panel's chips and the table
can never compute two different counts for "current" (this also removes
a duplicate `buildMatrixRows` call `renderTable` used to make on its
own).

**9.4: metric CHECKBOXES (any subset), stacked values in fixed order
(ns, MB/s, ×best), terse labels; single-metric selection keeps the
compact form.** DONE. `state.metrics` is now an array (`METRIC_ORDER`'s
order); `cellDisplay` renders each selected metric as one
`.metric-line` when more than one is selected, and falls back to the
EXACT v1.0 markup (no wrapper, no label) when exactly one is — the same
code path, not a special case, so "keeps today's compact form" is
literal.

**9.5: sorting targets a chosen displayed metric; ×best sorting works.**
DONE — and a REAL BUG was found and fixed while wiring it. v1.0's
`metricValue()` ranked the `best` metric by each cell's raw `median_ns`,
with a comment claiming this is equivalent to the ratio ("'best' metric
still ranks by ns; ratio is a display transform"). It is not: the ratio
denominator (`bestNs`) is the ROW's own best among the visible testees,
and different rows have different bests, so "smallest raw ns across
rows" and "smallest ratio-to-that-row's-own-best across rows" can
disagree the moment two rows pick different winners — which they do on
real data (verified below). `metricValue(cellRow, metric, bestNs)` now
takes the row's own `bestNs` and computes the true ratio when
`metric === "best"`. A `effectiveSortMetric()` helper (the user's own
`sortMetric` choice when it is still among the displayed metrics, else
the first displayed one — the design note's stated default) feeds this
into `sortGroups`'s `rankFor`; a small "sort by:" control
(`.sort-metric-row`) appears only once more than one metric is
displayed (the design note's own suggested shape — "a small per-header
affordance (or a global 'sort by' tied to the metric checkboxes)").

**9.6 (added mid-day): default selection = latest engines only.** DONE.
`computeDefaultTesteeIds()`: a testee is an "ablation/deny-flag/
toolchain arm" iff its `engine_variant` carries a `_<config_extra>`
suffix past the `<mode>-<caps>-<simd>` triplet — engine-neutral, never a
hard-coded pcrec config list, and derivable straight from testee_id's
own construction rule (the same one 9.1's fix reads). Such arms are
NEVER default-selected. A canonical variant (no suffix) contributes
only its OWN newest pin (by the same `newestDate` 9.2 computes); an
older pin of the same canonical variant is excluded by default but
stays reachable through the pin sub-picker. Applied on the true first
load (no hash, no `localStorage` restore — either is used in full,
untouched — this is the literal "on first load, no saved state"
condition) AND on "reset view" (which would otherwise silently
readopt v1.0's "everything" the moment a user clicked it, undoing the
whole point of the amendment). A "latest only" button was added
alongside "all"/"none" in the dropdown so a user can return to the
default roster without a full state reset (metrics/sort/filters
untouched) — a small addition beyond the literal ask.

A REAL, NAMED (not a bug) finding from testing this: the pcrec family
checkbox now starts render as `indeterminate` on a fresh load (some but
not all of its testees are default-selected) rather than v1.0's always
either-fully-checked-or-fully-unchecked. Clicking an INDETERMINATE
checkbox is standard browser/UX convention — it moves to fully CHECKED
(select the rest), never to unchecked — confirmed here as intentional,
correct behavior. The verification suite's own 9.1a flow had to be
adjusted for this (see below); the discovery process is worth recording
because it is exactly the kind of interaction 9.6 introduces for every
family with any ablation arm.

**9.7 (added mid-day): the engine picker becomes a DROPDOWN.** DONE, and
a REAL BUG was found and fixed while wiring it — the second of this
wave, and the sharper one. `#engine-picker-toggle` (`"Engines: n/N
selected"`) opens `#engine-picker-panel` (the unchanged family/variant/
pin tree) as a collapsible panel, closed by default; it closes again on:
re-clicking the toggle, a click anywhere OUTSIDE the panel, or Escape.

The bug: the FIRST implementation closed the dropdown SYNCHRONOUSLY
inside the document-level "click outside" listener
(`if (engineDropdownOpen) { engineDropdownOpen = false; rerenderAll(); }`).
Any OTHER interactive control on the page that lives outside the panel —
every metric/Sets/Regime/Form/Status checkbox — ALSO bubbles its click
to `document`, so clicking one of those WHILE the dropdown happened to
be open triggered this same synchronous `rerenderAll()`, which rebuilds
`#controls-row`/`#filters` and DETACHES the checkbox the user just
clicked. A direct DevTools probe (below) proved the real, counter-
intuitive event order in Chromium is:

    click (target) -> click bubbles to document -> input -> change

not the "change fires before the click finishes bubbling" order a
synchronous-DOM mental model suggests — and a checkbox already removed
from the document by the time `change` would fire NEVER fires `change`
at all in Chromium. So a click on, say, the "MB/s" metric checkbox,
made while the dropdown happened to be open, would toggle the checkbox's
own `.checked` to `true`, then get silently detached by the outside-
click handler's rerender BEFORE its own `change` handler ever ran to
update `state.metrics` — the click's effect was completely and silently
lost. This surfaced as the 9.4/9.5 verification checks intermittently
failing in ways that made no sense reading the code in isolation, and
was root-caused with a minimal three-line reproduction outside the app
entirely (`click`/`input`/`change`/`doc-click` listeners on a bare
`<input type=checkbox>`, confirming the order directly) before touching
`viewer.html` again.

Fixed by DEFERRING the outside-click close to a macrotask
(`setTimeout(fn, 0)`): the clicked control's own handler (and its own
`rerenderAll()`) now always finishes completely first; by the time the
deferred closer runs, nothing is mid-dispatch, so closing the dropdown
on top of that already-settled state is safe. The fix is documented
in-line in `viewer.html` at the listener itself, not only here.

**9.8 (added mid-day): pattern text in the pattern column.** DONE, same
export-then-render shape as 9.1's own fix. `tools/viewer_export.py`
gains `_pattern_text_entry()` / `PATTERN_TEXT_MAX_BYTES` (2,000 B,
"~2 KB" per the design note): each set's payload now carries a
`patterns` map, `{pattern_id: {text, omitted, truncated, full_bytes}}`
— ONE entry per pattern_id, factored OUT of the per-row data (a
pattern's text is invariant across every row that shares it; carrying
it per row would have multiplied a ~2 KB string across every testee/
regime/form row bench/altwide's corpus has for that pattern, a real and
pointless size cost). `omitted` is the RECORD's own free_text-cap
fallback (KB-7, record_schema.md, 1 MiB at schema v1.5) — genuinely
unreachable on the real corpus today (nothing is within a megabyte of
that cap), so the absent-text arm is verified against a hand-built
synthetic fixture, exactly the same posture `tools/selfcheck.py`'s own
omission-fallback control takes for the identical reason.
`viewer.html`: a pattern's text renders inline after its name when
short (`<=32` chars, muted code face, `.pattern-inline`) and is ALWAYS
available as a popover on the pattern cell (hover OR click — reusing
the existing `#tooltip` element with its own content renderer,
`patternPopoverHtml`); click PINS it open (ignores further hover) until
the same cell is clicked again, Escape, or an outside click (the SAME
deferred-close mechanism 9.7 fixed, shared rather than reimplemented).
A truncated entry's popover ends with `"… truncated, full N bytes"`
using the record's TRUE original length; an omitted one says so
plainly, in words, never silently blank.

## Root-cause reproductions, as asked ("write the failing reproduction
FIRST in the DevTools harness, then fix, then show it passing")

**9.1.** The reproduction was written and run FIRST against the merged
v1.0 code (before any fix in this lane): a headless-Chromium session
loaded the real production `viewer/data/*.js`, clicked the `pcrec`
family checkbox's `<input>` to deselect it, and read
`#table-scroll thead tr.col-labels th[data-testee]`'s `data-testee`
values. It showed the exact symptom Frank reported — after deselecting
"all pcrec", a `pcrec_*_nocaps-*`-shaped column remained selected and
visible (the second half of the `auto`/`nocaps` collision), and its
header rendered the SAME variant label as a still-selected `auto`
column from a DIFFERENT family context, reading as a duplicate. After
the fix (`tools/viewer_export.py`'s `engine_variant_for` +
`viewer.html`'s testee_id-direct tree), the SAME reproduction — now
committed as the first checks in the verification suite below (9.1a/
9.1b) — passes: every pcrec column disappears on deselect, re-selecting
restores exactly the original set, and an explicit duplication-
provoking sequence (`none` → select-pcrec-only → uncheck one variant
leaf → recheck) keeps the column count equal to the selection count and
never produces a duplicate `data-testee` value at any step.

**9.7.** The reproduction was a MINIMAL bare-DOM script (no viewer.html
involved at all): a checkbox with `click`/`input`/`change` listeners
plus a `document`-level `click` listener that removes the checkbox's
parent and rebuilds it, called via `.click()` — this alone reproduced
"the `change` handler never fires" with zero app code in the loop,
proving the bug was a genuine DOM/event-ordering fact rather than
anything specific to this codebase, before the fix (deferred close) was
written or applied to `viewer.html`.

## Real headless-Chromium DevTools verification

**The harness.** b66viewer's own verification script was explicitly
"not committed, throwaway" (its report says so), so there was nothing
to literally reuse from the repository; this lane reused the SAME
TECHNIQUE — headless Chromium driven over the real DevTools protocol,
never a simulated/mocked DOM — built fresh since no npm packages
(puppeteer, chrome-remote-interface) are installed on this box and none
could be installed. The driver is ~130 lines over Node 24's built-in
`WebSocket`/`fetch` (no dependency): launches
`/snap/bin/chromium --headless=new --no-sandbox ...`, opens a real page
via `/json/new`, and drives it with `Page.navigate` / `Runtime.evaluate`
(with `awaitPromise` support, needed once the main check script became
an `async` IIFE to await the 9.7 deferred-close fix's own settling
delay) / `Console.enable` / `Runtime.exceptionThrown`. Every check
drives the REAL DOM (`.click()` on real checkboxes/buttons, reading
real rendered `textContent`/`innerHTML`) and cross-checks every
rendered NUMBER against an INDEPENDENT second computation written
fresh in the test script from the raw `window.BENCH` data (never by
calling into `viewer.html`'s own internal functions, which are not
exposed on `window` at all — `App` is a closed IIFE) — the same "a
control shares no source with what it controls" rule this project's
own harness checks follow elsewhere. Kept in the session scratchpad,
not committed (mirrors b66's posture; a throwaway verification tool,
not part of `make check`, which does not gate `viewer/` at all).

**Environmental findings, not app bugs, both named for the record.**
(1) Snap-packaged Chromium's `file://` access is confined to non-hidden
paths under `$HOME` — `/tmp` (this session's own scratchpad) is
UNREADABLE to it (`ERR_FILE_NOT_FOUND`, confirmed empirically), so
every fixture the harness NAVIGATES TO lived under a plain `$HOME`
path; Chromium's own `--user-data-dir` profile has no such restriction.
(2) Chromium does NOT scope `localStorage` per `file://` PATH — two
different `viewer.html` copies opened in the SAME browser profile share
one `localStorage` origin, so a second page's `loadPersisted()` can
silently inherit a filter-state hash the first page persisted. Fixed in
the harness by giving the multi-pin and absent-text fixtures their OWN
browser instance each (own profile, own port); named in `viewer/
CLAUDE.md` too, since it is a real fact about the persisted-state
design this lane did not change (v1.0's `try/catch`-guarded, hash-wins
posture already tolerates it gracefully).

**What ran, and against what data.** The FULL committed
`viewer/data/*.js` (regenerated TWICE in this lane — once under the 9.1
export fix, again under 9.8's `patterns` field addition: 10 sets, 86
records, 1,322 matrix rows, 40 engine columns "all", 13 under 9.6's new
default) — never a synthetic fixture for the numbers that matter. Three
supporting fixtures, each real data or a deliberately minimal synthetic
one, never invented numbers: (a) an `--all-pins`-exported slice of
`bench/bounded` (real pcrec pins, 716-3,339 rows per set version) for
the pin sub-tier's date-ordering; (b) a hand-built one-row synthetic
`BENCH.load()` fixture (a single `omitted: true` pattern-text entry,
the only way to reach that arm on the real, well-under-the-cap corpus);
(c) a copy of the production data with one set's data file deleted, for
the missing-file degrade check (b66's own precedent, re-verified).

**Results, run against the real production data
(`viewer/viewer.html` + the regenerated `viewer/data/`), 2026-09-21:**

    72/72 checks passed, 0 failed
    console.error calls: 0
    uncaught exceptions: 0

Broken down:

- **9.6 default roster (2 checks)**: the fresh-load column set
  (13 testees) matched EXACTLY against an independent, from-scratch
  recount over `window.BENCH`'s raw rows (same ablation-suffix +
  newest-pin-per-canonical-variant rule, re-derived rather than
  imported from the app) — `13` vs `13`; and confirmed smaller than the
  "everything" roster (40), proving the 45-column default is genuinely
  retired, not merely relabeled.
- **9.7 dropdown round-trip (9 checks)**: toggle exists, starts closed,
  labels itself `"Engines: n/N selected"`, opens on click, the tree
  becomes reachable once open, closes on a second toggle click WITHOUT
  changing the current selection, reopening shows the SAME selection
  (a real round-trip, not just "it opens again"), and a click OUTSIDE
  the panel closes it too — this last one read AFTER an explicit
  `await sleep(30)` for the (correct, load-bearing) deferred close to
  actually fire, not a synchronous read.
- **9.1 reproduction and regression (15 checks, incl. 2 for the
  indeterminate-checkbox finding; a 16th, "a testee id was chosen for
  per-column checks", is shared setup for 9.2/9.3 below and counted
  there)**: the family checkbox starts
  `indeterminate` under 9.6's default and clicking it selects ALL of the
  family (confirmed, both asserted explicitly); FROM a definite
  fully-checked state, deselect-all-pcrec removes exactly those 9
  CANONICAL columns (post-collapse; a fixture-real 31 includes ablation
  siblings) with zero left starting `pcrec_`; total column count drops
  by exactly the removed count; no duplicate `data-testee` values at any
  step; re-select restores the ORIGINAL set exactly; the duplication-
  provoking sequence (`none` → pcrec-only (31) → uncheck
  `auto-caps-simdna` → recheck → reset view) keeps column count ==
  selection count throughout, with the DATA-DRIVEN discovery that this
  particular leaf, on the real store, carries FIVE pins today
  (`1989c62`/`25b1984f`/`692c2e8`/`96e44c2`/`a7e0bdf`, all sharing the
  `auto-caps-simdna` config_slug at different pcrec pins across
  different sub-benches' own last-measured dates) — the test asserts
  the REMOVED set equals the leaf's own known ids exactly, not a
  hard-coded count, which is what caught both this and the
  indeterminate-checkbox finding in the first place.
- **9.3 coverage (5 checks, incl. the shared setup line that also
  chooses the testee 9.2 reads)**: header chip `22/1322` and family chip
  `819/1322`, each matched EXACTLY against an independent recount over
  `window.BENCH`'s raw rows (never the app's own reducer).
- **9.2 date label (4 checks)**: header label starts with a real
  `YYYY-MM-DD` (`2026-09-02`), matches an independent newest-
  `measured_utc` recount, the pin is in the `title` tooltip, and the
  visible label is provably NOT the raw pin string.
- **9.4 stacked cell (4 checks)**: a real measured cell renders compact
  under one metric, then — the SAME cell, tracked by its stable
  `data-cid` — stacks exactly two `.metric-line`s labeled `["ns",
  "MB/s"]` in that order once MB/s is also checked (this is also the
  check that, before the 9.7 deferred-close fix, intermittently failed
  for the reason described above).
- **9.8 pattern text (10 checks)**: a real altwide truncated witness
  (`ci-256`, 2,105 real bytes) renders NO inline text (over the ~32-char
  bound), opens a popover on click showing its own truncated prefix and
  the tail `"… truncated, full 2,105 bytes"` (the THOUSANDS-SEPARATED
  form, matched against the SAME `toLocaleString("en-US")` rendering
  path the popover itself uses — a control that shares the formatting
  rule, not a coincidence of matching digits), and closes again on a
  second click; a real short witness (`altwide@0.1`'s `floor` pattern,
  text `"#"`) renders inline with an exact text match; the synthetic
  absent-text fixture renders no inline text, opens a popover that says
  `"omitted"` and names the `free_text` cap explicitly, and — checked
  as its own assertion, not assumed — does NOT also claim a truncation.
- **9.5 sort-by-ratio fix (7 checks)**: sorting a real 22-row column by
  `×best` (single-metric, compact form) produced
  `[1,1,1,1,1,1,1,1,1,1,1,1.001,1.001,1.001,1.001,1.002,1.002,1.002,1.003,1.006,1.252,1.946]`
  — genuinely monotonic, with at least 2 distinct values compared (a
  real ordering test, not a coincidence of one winner everywhere); a
  second run with BOTH `ns` and `×best` displayed defaults sort-by to
  `ns` (the first displayed metric, `active` class asserted) and, after
  clicking the "sort by ×best" control, produces the SAME monotonic
  ratio sequence read out of the STACKED cell's second `.metric-line`
  — proving the fix works both compact and stacked, and that "sort by"
  targets a non-default displayed metric correctly; non-measured rows
  still sink beneath every numeric row.
- **Missing-data-file degrade (2 checks)**: removing `altwide@0.1.js`
  from a copy produces the named summary line
  (`"1 set data file missing: altwide@0.1"`) with the remaining 1,228
  rows still rendering — never a blank page.
- **Nonsense pattern search (1 check)**: a substring matching nothing
  produces the named empty state, not a blank table.
- **Multi-pin date ordering (6 checks, incl. 2 harness-setup lines,
  `--all-pins` bounded fixture, its own browser instance)**: a real
  variant with 9 rendered pin rows,
  every label leading with a date, the sequence
  `["2026-09-21","2026-09-06","2026-09-05","2026-09-05","2026-09-02","2026-09-01","2026-08-31","2026-08-30","2026-08-30"]`
  genuinely newest-first (asserted against its own sorted-descending
  copy, never by sha), and selecting exactly ONE pin leaf shows exactly
  its own column with NONE of its 8 sibling pins' columns present.
- **9.8 absent-text arm (5 checks, its own browser instance)**: listed
  under 9.8 above; separated here only to show it ran as its own real
  navigation, not folded into the main page's DOM.
- **Baseline render checks (2)**: real rows, real header columns.

**Render-time re-measurement, now TWO scales** (the design note's
421 ms budget, b66's own measurement at the OLD 45-column default; 9.6
retires that default, so both the new default's own cost and the
still-reachable "all" scale are reported):

    DEFAULT scale (1,322 rows x 13 cols, 9.6's latest-canonical roster):
      single metric (ns):     median 84.8 ms  (5 samples: 307.6, 82.2, 89.2, 79.3, 84.8)
      three metrics stacked:  median 78.8 ms  (5 samples: 82.6, 77.7, 76.3, 78.8, 79.7)

    ALL scale (1,322 rows x 40 cols, every ablation arm -- the old v1.0 default):
      single metric (ns):     median 235.5 ms  (5 samples: 222.8, 230.2, 239.7, 235.5, 267.0)

Read plainly, not oversold: the DEFAULT scale's "stacked" median
(78.8 ms) sitting slightly BELOW its own "single" median (84.8 ms) is
NOISE, not a real "stacking is faster" effect — the single-metric run's
first sample (307.6 ms) is a cold-start/warm-up outlier dragging that
median up slightly; both numbers are comfortably in the same ~75-90 ms
band once that's accounted for. What IS a real, attributable number:
the ALL scale (every ablation arm, still one click away via the
dropdown's own "all" button) costs 235.5 ms — well under the 421 ms
budget b66 measured at a similar 45-column scale, and the DEFAULT scale
a typical session actually renders at is 3x smaller again. No
regression at either scale from this wave's own changes (stacking,
popovers, the dropdown): the render loop's asymptotic shape is
untouched: only what a cell's `innerHTML` string contains, and how many
columns are visible by default, changed.

## What was NOT independently re-verified from b66's original 19-check
suite (honest gap, not silently assumed)

Firefox/Safari/WebKit: not tested, only Chromium's headless mode (same
gap b66 named). Real mouse hover for the tooltip/popover: not
simulated (same gap; click was used throughout instead, which this
wave's own "hover/click" design explicitly makes an equally-valid
trigger). Visual/layout (phone-width, dark-mode contrast, the sticky
header, the new dropdown panel's own layout): not rendered and looked
at by a human or a screenshot tool in THIS lane either — the CSS added
for the dropdown, stacked cells, coverage chips and the pattern popover
was written to the existing token/layout conventions and reviewed by
eye in the source only. The `form` filter checkbox: code-reviewed
(unchanged code path from `regime`'s, which WAS exercised at runtime in
b66's own suite), not independently re-clicked in this lane's own
session — no reason to expect the untouched code path regressed, named
rather than silently assumed.

## Files touched

- `tools/viewer_export.py` (`engine_variant_for`, the §9.1 root-cause
  fix, `_engine_variant` kept as a documented, now-unreachable-in-
  practice fallback; `_pattern_text_entry`/`PATTERN_TEXT_MAX_BYTES` and
  the `patterns` map on every set's payload for §9.8)
- `viewer/viewer.html` (all eight amendments: the domain tree rewrite
  and testee_id-direct tree for 9.1; date/coverage rendering for 9.2/
  9.3; checkbox metrics + stacking for 9.4; sort-by-metric for 9.5;
  `computeDefaultTesteeIds()` + the first-load/reset-view wiring for
  9.6; the dropdown panel + its deferred-close fix for 9.7; the pattern
  inline/popover rendering, sharing the deferred-close mechanism, for
  9.8)
- `viewer/data/*.js` (regenerated twice — the 9.1 export fix, then the
  9.8 `patterns` field; real content changed both times, not just
  `generated_utc`)
- `viewer/CLAUDE.md` ("v1.1 amendments" section covering all eight
  items, incl. both real bugs found and the localStorage cross-file
  finding)
- `docs/design/results_viewer_v1.md` (STATUS line + every §9 item's own
  status note, all to IMPLEMENTED; both root-cause notes folded into
  the original asks)
- `docs/design/CLAUDE.md` (the `results_viewer_v1.md` entry extended to
  summarize the v1.1 wave)
- `docs/dev/lanes/b67viewer_report.md` (this file)

Branch `lane/b67viewer`, not merged. Worktree at `worktrees/b67viewer/`.
