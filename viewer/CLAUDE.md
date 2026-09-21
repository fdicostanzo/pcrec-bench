# viewer/ — the results viewer ([B66]/[B67], docs/design/results_viewer_v1.md)

A single-page, client-side READING AID over the canonical store's
SET-GRAIN results: pick engines, sets, regimes, forms and a metric; get a
sortable matrix that re-renders instantly, entirely in the browser, with
no server and no build step. Like the matrix HTML pages under `reports/`,
it is **never a canonical surface and never a ranking input** — the
canonical numbers live in `reports/` and `store/`. Every number this page
shows is reduced by `tools/viewer_export.py` through the SAME
`pcrecbench.reduce` functions (`reduce_set_cell`, `cells_from_record`) the
reporter (`pcrecbench/report.py`) calls, so a viewer cell equals the
committed report cell byte-for-value (design note 2's own rule) — this
page never reimplements a median.

## Files

| file | role |
|---|---|
| `viewer.html` | the whole app: inline CSS + JS, no CDN, no build step, no ES modules — works from `file://` (R12). Registers `window.BENCH` before loading `data/manifest.js` and each `data/<set>.js` via dynamically-created `<script src>` tags (the one loading mechanism `file://` permits: `fetch()`/XHR are null-origin-CORS-blocked, and classic scripts are not). A missing/stale data file degrades to a named per-set notice (`Sets` panel, `(data file missing)`), never a blank page. |
| `data/manifest.js` | generated: `BENCH.manifest({generated_utc, store_rows, all_pins, files, sets, status_sink_order})` — which `data/*.js` files exist and how each set's rows are grouped/counted, plus the non-measured sink order `viewer.html`'s sort rule reads (so the exporter and the page can never disagree about it). |
| `data/<subbench>@<version>.js` | generated, one per exported set: `BENCH.load({set, subbench, version, rows: [...], patterns: {...}})`. `patterns` is [B67] 9.8's addition -- one pattern-text entry per `pattern_id`, keyed separately from `rows` (a pattern's text does not repeat per row). Committed so a fresh clone works without running the exporter first; regenerate at will (`make viewer-data`). |

The exporter itself, `tools/viewer_export.py`, is documented in
`tools/CLAUDE.md` — its own module docstring is the full design
(inclusion/dedup rule, per-row status derivation, the memory discipline).

## v1.1 amendments ([B67], docs/design/results_viewer_v1.md 9)

Frank's five 2026-09-21 review notes, all IMPLEMENTED:

1. **9.1 (bug fix): every engine column key comes straight off its row's
   own `testee_id`, never reconstructed.** The tree used to recover a
   testee_id at click time from a (family, variant, pin) triple via a
   linear scan; the ROOT CAUSE was one layer further down —
   `tools/viewer_export.py`'s old `engine_variant` label was built from
   only `engine_mode` + `config_extra`, silently DROPPING the `captures`
   axis, so `pcrec-auto` (captures=on) and `pcrec-nocaps` (captures=off)
   both rendered the SAME variant label `"auto"`. Two distinct testee_ids
   sharing one visible tree leaf is what let a family-deselect miss one
   of them (it survived, looking like a "duplicate" of itself under a
   different family's columns) and what could, for a differently-shaped
   config set, produce genuinely duplicate-LOOKING header labels.
   Fixed at the source: `engine_variant_for()` now reads testee_id's own
   config_slug segment (`schema/validate.py`'s `derive_testee_id`:
   `<engine>_<version>_<engine_mode>-<caps>-<simd>[_<config_extra>]` —
   everything after the second underscore), which is unique per
   testee_id BY CONSTRUCTION. `viewer.html`'s domain tree now stores the
   real testee_id at every pin leaf (`variants[v].pins[pin] = testee_id`)
   the moment it reads a row, and never reconstructs one — the dead
   `testeeIdOf()` reverse-scan function is gone.
2. **9.2: column headers lead with the DATE.** Each testee's own newest
   `measured_utc` (YYYY-MM-DD, domain-wide — not filter-dependent, so a
   pin picker's ordering stays stable under any filter) is the primary
   label; the pin moves to the `title` tooltip (`<testee_id> · pin
   <pin>`). A single-pin variant leaf's own `<label>` also carries its
   sole testee_id as a `title` now (a small addition beyond the ask,
   useful for tooling/hover alike). Any place pins are listed (the
   third-tier picker under a variant with more than one pin) orders them
   newest-first by that same date, never by sha.
3. **9.3: a coverage chip (`n/N`)** rides beside the family row, each
   variant leaf (when single-pin), each pin sub-row, and the column
   header — all computed against the render's own CURRENT filtered
   `groups` (never the domain-wide total), threaded through from
   `rerenderAll()` so filters and table agree by construction rather
   than by two separate computations.
4. **9.4: metric CHECKBOXES**, any non-empty subset of `ns` / `MB/s` /
   `×best`, `METRIC_ORDER`'s fixed display order. A single selected
   metric renders exactly as v1.0 did (no wrapper, no label) — "single-
   metric selection keeps the compact form" is the literal same code
   path, not a special case.
5. **9.5: sorting targets a chosen DISPLAYED metric.** `effectiveSortMetric()`
   is the user's own choice when it is still displayed, else the first
   displayed metric. Fixed a real bug found while wiring this in:
   ranking by `×best` used to sort by each cell's raw `median_ns` (a
   leftover comment called this equivalent to the ratio — it is NOT: two
   different matrix rows have two different `bestNs` denominators, so
   "smallest raw ns" and "smallest ratio-to-THIS-row's-own-best" can
   disagree the moment two rows pick different winners).
   `metricValue(cellRow, metric, bestNs)` now takes the row's own
   `bestNs` and genuinely ranks by the ratio when `metric === "best"`.
6. **9.6: fresh-load default selects only the LATEST canonical variant
   per (family, config identity).** `computeDefaultTesteeIds()`
   (`viewer.html`): a testee is an "ablation/deny-flag/toolchain arm"
   iff its `engine_variant` carries a `config_extra` suffix (an `_` past
   the `<mode>-<caps>-<simd>` triplet -- engine-neutral, no hard-coded
   pcrec list); such arms are NEVER default-selected. A canonical
   variant (no such suffix) contributes only its own NEWEST pin (by
   domain-wide `newestDate`); an older pin of the same canonical variant
   is excluded by default but stays reachable via the pin sub-picker.
   Applies on the true first load (no hash, no `localStorage` restore --
   either of those is used in full, untouched) AND on "reset view" (which
   would otherwise silently readopt v1.0's "everything" default the
   moment a user clicked it). MEASURED at production scale: 13 columns
   by default against 40 under "all" (still one click away, via the
   dropdown's own "all" button, or the "latest only" button restores the
   default explicitly without a full state reset).
7. **9.7: the engine picker is now a DROPDOWN.** A compact
   `#engine-picker-toggle` button (`"Engines: n/N selected"`) opens
   `#engine-picker-panel` (the same family/variant/pin tree, unchanged)
   as a collapsible panel; closed by default. Closes on: clicking the
   toggle again, a click anywhere OUTSIDE the panel, or Escape. The
   outside-click close is **deferred via `setTimeout(0)`, and this is
   load-bearing**: a checkbox click that bubbles past the panel (any of
   Sets/Regime/Form/Status/metric -- everything outside the panel) fires
   its own "change" handler AFTER "click" finishes bubbling to
   `document` (confirmed empirically, order is click → this document
   listener → input → change -- not what the synchronous-DOM intuition
   suggests), so closing the dropdown SYNCHRONOUSLY there used to
   rebuild `#controls-row`/`#filters` and detach the just-clicked
   checkbox before its own "change" ever fired -- and a checkbox already
   removed from the document never fires "change" in Chromium, so that
   click's effect was silently lost outright (found via the MB/s-in-a-
   multi-metric-selection checks consistently failing to register).
8. **9.8: pattern text.** `tools/viewer_export.py` gained
   `engine_variant_for`'s sibling for this ask, `_pattern_text_entry` /
   `PATTERN_TEXT_MAX_BYTES` (2,000 B): each set's exported payload now
   carries a `patterns` map (`{pattern_id: {text, omitted, truncated,
   full_bytes}}`), ONE entry per pattern (factored out of the per-row
   data -- a pattern's text is invariant across every row that shares
   it, and duplicating a ~2 KB string per row across bench/altwide's
   corpus would have been a real size cost for nothing). `omitted` is
   the RECORD's own free_text-cap fallback (KB-7); this bench's own
   further truncation is separate and always carries the TRUE
   `full_bytes` even when truncated. `viewer.html`: a pattern's text
   shows inline after its name when short (`<=32` chars, muted code
   face, `.pattern-inline`) and is ALWAYS available as a popover
   (hover OR click; click PINS it open, ignoring further hover, until
   the same cell is clicked again, Escape, or an outside click) reusing
   the existing `#tooltip` element with its own content renderer
   (`patternPopoverHtml`). A truncated entry's popover ends with
   `"… truncated, full N bytes"`; an omitted one says so plainly, never
   silently blank.

**v1.2 follow-up (2026-09-21, the manager, on Frank's residual-duplicates
note):** the `""` regime — the RESIDUE class after [B70]'s fold, i.e.
whole-subject-form refusals no engine measured anywhere, so no ranked
row existed to absorb them (32 rows corpus-wide; only the two
wrap-artifact ones disappear at the next re-measure) — now defaults
**OFF** on a fresh load (`defaultRegimes()` in `viewer.html`), and its
checkbox is labeled `(unranked-form refusals)`. Reachable, never
default noise. A persisted hash/localStorage state is honored as
saved.

**A named, out-of-scope finding from building this wave's DevTools
verification (not fixed, not one of the five asks):** Chromium does not
scope `localStorage` per `file://` PATH — two different `viewer.html`
files opened in the SAME browser profile share one `localStorage`
origin, so the SECOND page's `loadPersisted()` can silently inherit a
filter state (via the persisted hash) that the FIRST page saved,
filtering its own, unrelated data to nothing. The design note's own
`try/catch`-guarded-convenience posture for `localStorage` already
covers this (the HASH always wins when present, and a broken restore
degrades rather than crashes) — worth knowing if two people's clones of
this repo are ever opened side by side in one browser session, not
worth changing the persistence design over.

## Regenerating

    make viewer-data                              # every set, newest pin
                                                    # per canonical identity
    make viewer-data ARGS="--sets loglines"        # one set (dev slice)
    make viewer-data ARGS="--all-pins"             # every pin its own column

Then open `viewer/viewer.html` directly in a browser (`file://` works; no
server needed).

## What it is NOT (scope fence, design note 6)

No server, no build step, no external CDN (offline/plane-safe), no
subject-grain drill-down (the subject-grain TSVs under `reports/` stay
the deep tool), no cross-machine comparison UI (the `pin`/`record_id`
provenance is carried per row so a future UI can add it; today's store
has one machine), no editing, nothing written back. The viewer never
computes a number the reduction in `tools/viewer_export.py` did not
already define — a ratio (`× best-in-row`) and a derived rate
(`subject_bytes_total / median_ns × 1000` for MB/s) are the only
CLIENT-SIDE arithmetic on this page, both stated in the design note (R4)
and both computed from numbers the exporter already reduced, never from
raw trials.
