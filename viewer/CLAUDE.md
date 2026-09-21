# viewer/ — the results viewer ([B66], docs/design/results_viewer_v1.md)

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
