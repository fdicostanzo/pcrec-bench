# b67viewer — the results viewer's v1.1 fix wave, lane report

Branch `lane/b67viewer`, built against `docs/design/results_viewer_v1.md`
§9 (Frank's five 2026-09-21 review notes) on top of the merged v1.0
(`lane/b66viewer`, `viewer/viewer.html` + `tools/viewer_export.py`). Not
merged; the manager merges.

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

## Root-cause reproduction, as asked ("write the failing reproduction
FIRST in the DevTools harness, then fix, then show it passing")

The reproduction was written and run FIRST against the merged v1.0 code
(before any fix in this lane): a headless-Chromium session loaded the
real production `viewer/data/*.js`, clicked the `pcrec` family
checkbox's `<input>` to deselect it, and read
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

## Real headless-Chromium DevTools verification

**The harness.** b66viewer's own verification script was explicitly
"not committed, throwaway" (its report says so), so there was nothing
to literally reuse from the repository; this lane reused the SAME
TECHNIQUE — headless Chromium driven over the real DevTools protocol,
never a simulated/mocked DOM — built fresh since no npm packages
(puppeteer, chrome-remote-interface) are installed on this box and none
could be installed. The driver is ~120 lines over Node 24's built-in
`WebSocket`/`fetch` (no dependency): launches
`/snap/bin/chromium --headless=new --no-sandbox ...`, opens a real page
via `/json/new`, and drives it with `Page.navigate` / `Runtime.evaluate`
/ `Console.enable` / `Runtime.exceptionThrown`. Every check drives the
REAL DOM (`.click()` on real checkboxes/buttons, reading real rendered
`textContent`/`innerHTML`) and cross-checks every rendered NUMBER
against an INDEPENDENT second computation written fresh in the test
script from the raw `window.BENCH` data (never by calling into
`viewer.html`'s own internal functions, which are not exposed on
`window` at all — `App` is a closed IIFE) — the same "a control shares
no source with what it controls" rule this project's own harness
checks follow elsewhere. Kept in the session scratchpad, not committed
(mirrors b66's posture; a throwaway verification tool, not part of
`make check`, which does not gate `viewer/` at all).

**A snap-confinement finding, not an app bug.** Snap-packaged Chromium's
`file://` access is confined to non-hidden paths under `$HOME` —
`/tmp` (this session's own scratchpad) is UNREADABLE to it
(`ERR_FILE_NOT_FOUND`, confirmed empirically: the worktree under
`$HOME/pcrec-bench` loads fine, a hidden `$HOME/.dir` does not, a plain
`$HOME/dir` does) — so every file the harness NAVIGATES TO (dev-slice
copies, a missing-data-file fixture, an `--all-pins` fixture) had to
live under a plain `$HOME` path; Chromium's own `--user-data-dir`
profile has no such restriction (that is the launching process's own
file access, not a renderer's navigation). A second finding, also
environmental rather than an app bug: Chromium does NOT scope
`localStorage` per `file://` PATH — two different `viewer.html` copies
opened in the SAME browser profile share one `localStorage` origin, so
a second page's `loadPersisted()` silently inherited a filter-state
hash the first page had persisted, filtering the second page's own
unrelated data to zero rows before any check ran. Fixed in the harness
by giving the multi-pin fixture its OWN browser instance (own profile,
own port) rather than reusing the main suite's; named here (and in
`viewer/CLAUDE.md`'s own note) because it is a real fact about the
persisted-state design, not something this lane changed — v1.0's
`try/catch`-guarded, hash-wins-when-present posture already tolerates it
gracefully, and it is not one of Frank's five asks.

**What ran, and against what data.** The FULL committed
`viewer/data/*.js` (regenerated in this lane under the 9.1 fix: 10 sets,
86 records, 1,322 matrix rows, 40 engine columns on this run of the
export — the exact count moves slightly release to release as the
store grows and pins collapse differently) — never a synthetic fixture
for the numbers that matter. A second, `--all-pins`-exported slice of
`bench/bounded` (multiple real pcrec pins, 716-3,339 rows per set
version) was built ONLY to exercise the pin sub-tier's date-ordering,
since the default export can (see 9.1's side-finding) but does not
reliably carry more than one pin per variant on every set.

**Results, run against the real production data
(`viewer/viewer.html` + the regenerated `viewer/data/`), 2026-09-21:**

    43/43 checks passed, 0 failed
    console.error calls: 0
    uncaught exceptions: 0

Broken down:

- **9.1 reproduction and regression (12 checks)**: fixture has pcrec
  columns to begin with (31); deselect-all-pcrec removes exactly those
  9 CANONICAL columns (post-collapse; the 31 includes ablation
  siblings) with zero left starting `pcrec_`; total column count drops
  by exactly the removed count; no duplicate `data-testee` values at
  any step; re-select restores the ORIGINAL set exactly; the
  duplication-provoking sequence (`none` → pcrec-only (31) → uncheck
  `auto-caps-simdna` → recheck → reset view) keeps column count ==
  selection count throughout, with the DATA-DRIVEN discovery that this
  particular leaf, on the real store, actually carries FIVE pins today
  (`1989c62`/`25b1984f`/`692c2e8`/`96e44c2`/`a7e0bdf`, all sharing the
  `auto-caps-simdna` config_slug at different pcrec pins across
  different sub-benches' own last-measured dates) — the test asserts
  the REMOVED set equals the leaf's own known ids exactly, not a
  hard-coded count, which is what caught this in the first place (a
  first attempt hard-coded "drops by 1" and correctly failed on real
  data).
- **9.3 coverage (4 checks)**: header chip `22/1322` and family chip
  `819/1322`, each matched EXACTLY against an independent recount over
  `window.BENCH`'s raw rows (never the app's own reducer).
- **9.2 date label (4 checks)**: header label starts with a real
  `YYYY-MM-DD` (`2026-09-02`), matches an independent newest-
  `measured_utc` recount, the pin is in the `title` tooltip, and the
  visible label is provably NOT the raw pin string.
- **9.4 stacked cell (3 checks)**: a real measured cell renders compact
  under one metric, then — the SAME cell, tracked by its stable
  `data-cid` — stacks exactly two `.metric-line`s labeled `["ns",
  "MB/s"]` in that order once MB/s is also checked.
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
- **Multi-pin date ordering (4 checks, `--all-pins` bounded fixture)**:
  a real variant with 9 rendered pin rows, every label leading with a
  date, the sequence
  `["2026-09-21","2026-09-06","2026-09-05","2026-09-05","2026-09-02","2026-09-01","2026-08-31","2026-08-30","2026-08-30"]`
  genuinely newest-first (asserted against its own sorted-descending
  copy, never by sha), and selecting exactly ONE pin leaf shows exactly
  its own column with NONE of its 8 sibling pins' columns present.
- **Baseline render checks (2)**: real rows, real header columns.

**Render-time re-measurement** (the 421 ms budget b66 measured at
1,326×45; asked for explicitly): at the CURRENT production scale
(1,322 rows × 40 columns — close to but not identical to b66's own
count, since the store and its pin-collapse have moved since), clicking
"all" (the same synchronous `performance.now()`-wrapped technique b66
used):

    single metric (ns):     median 275.3 ms  (5 samples: 480.6, 274.1, 273.3, 275.3, 300.0)
    three metrics stacked:  median 303.8 ms  (5 samples: 303.8, 305.6, 302.7, 302.3, 320.8)

Stacking three metrics costs ~29 ms extra median (10.4%) at this scale
— no regression against b66's 421 ms figure; both numbers sit
comfortably under it (this run's own single-metric baseline, 275 ms, is
itself below b66's number, most likely reflecting the store's own
column-count/roster drift since 2026-09-18 rather than a JS
performance change — nothing in this lane's diff touches the render
loop's asymptotic shape, only what a cell's `innerHTML` string
contains).

## What was NOT independently re-verified from b66's original 19-check
suite (honest gap, not silently assumed)

Firefox/Safari/WebKit: not tested, only Chromium's headless mode (same
gap b66 named). Real mouse hover for the tooltip: not simulated (same
gap). Visual/layout (phone-width, dark-mode contrast, the sticky
header): not rendered and looked at by a human or a screenshot tool in
THIS lane either — the CSS added for stacked cells and coverage chips
was written to the existing token/layout conventions and reviewed by
eye in the source only. The `form` filter checkbox: code-reviewed
(unchanged code path from `regime`'s, which WAS exercised at runtime in
b66's own suite), not independently re-clicked in this lane's own
session — no reason to expect the untouched code path regressed, named
rather than silently assumed.

## Files touched

- `tools/viewer_export.py` (`engine_variant_for`, the §9.1 root-cause
  fix; `_engine_variant` kept as a documented, now-unreachable-in-
  practice fallback)
- `viewer/viewer.html` (all five amendments; the domain tree rewrite,
  date/coverage rendering, checkbox metrics + stacking, sort-by-metric)
- `viewer/data/*.js` (regenerated under the fix; real content changed —
  `engine_variant` values, not just the `generated_utc` timestamp)
- `viewer/CLAUDE.md` (new "v1.1 amendments" section, incl. the
  localStorage cross-file finding)
- `docs/design/results_viewer_v1.md` (STATUS line + §9's own status
  line, both to IMPLEMENTED; the 9.1 root-cause note folded into the
  original ask)
- `docs/dev/lanes/b67viewer_report.md` (this file)

Branch `lane/b67viewer`, not merged. Worktree at `worktrees/b67viewer/`.
