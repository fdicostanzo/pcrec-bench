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
| `data/<subbench>@<version>.js` | generated, one per exported set: `BENCH.load({set, subbench, version, rows: [...]})`. Committed so a fresh clone works without running the exporter first; regenerate at will (`make viewer-data`). |

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
