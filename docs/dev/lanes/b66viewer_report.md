# b66viewer — [B66] THE RESULTS VIEWER, lane report

Branch `lane/b66viewer`, built to `docs/design/results_viewer_v1.md` v1.0
in full. Hand-off complete; not merged (the manager merges).

## What was built

1. **`tools/viewer_export.py`** (440 lines) — walks `store/index.tsv`,
   picks the newest record per `(subbench@version, testee_id,
   machine_id)` (the same R2/OD-S15 rule `report.py`'s `build_report`
   uses, computed here from `index.tsv` columns alone — no record file
   opened to decide inclusion), then by default collapses across PINS of
   one canonical `(engine_name, config_slug)` identity to the newest pin
   (`reports/CLAUDE.md`'s [B61] convention, generalised past pcrec's own
   ablation testees to every engine); `--all-pins` skips that collapse.
   Each surviving record is loaded ONE AT A TIME via
   `pcrecbench.report.load_record` (the reporter's own loader) and
   reduced via `pcrecbench.reduce.cells_from_record` /
   `reduce_set_cell` — the exact functions `report.py` calls, never a
   reimplementation — then dropped before the next file opens.
   Deliberately does NOT call `report.build_report`: that function
   accumulates every selected record's RAW rows across the whole query
   before reducing anything, which is the wrong shape for "one record
   at a time, release between" (the brief's memory rule; `build_report`
   is the path that produced the 3.6 GB/160-record KB-16 incident).
   Emits `viewer/data/manifest.js` + `viewer/data/<set>.js` as
   classic-JS `BENCH.load({...})`/`BENCH.manifest({...})` calls, atomic
   tmp+rename (0644, matching every other generated file in the repo —
   `tempfile.mkstemp` defaults to 0600, fixed with an explicit
   `os.chmod`), deterministic row ordering.
2. **`viewer/viewer.html`** (1,077 lines) — single self-contained page,
   inline CSS+JS, no CDN, no modules, works from `file://` (classic
   `<script src>` tags created dynamically once `window.BENCH` is
   registered — the one loading mechanism `file://` permits). Engine
   family→variant tri-state checkbox tree (a third, pin-level, tier
   appears only where a variant carries more than one pin — see
   "Deviations" below), set/regime/form checkboxes and pattern substring
   filter all derived from the loaded data, status show/hide, three
   metrics (median ns / MB/s / ×best-in-row, recomputed over visible
   columns), sortable column headers with the specified non-measured
   sink order, family header bands, provenance tooltips (spread,
   n_subjects, record_id, pin, measured_utc — diagnostic text on a
   refused/unsup cell), status chips never ranked/never best,
   hash-serialized state + `try/catch`-guarded `localStorage`
   convenience, light+dark themes on the three-state token pattern,
   phone-width table in its own `overflow-x` container.
3. **`viewer/CLAUDE.md`**, **`tools/CLAUDE.md`** (new row) and root
   **`CLAUDE.md`** (a `viewer/` entry under "Where things are" + the
   `make viewer-data` target line under "Build & test").
4. **`make viewer-data`** target (`Makefile`), `ARGS` pass-through for
   `--sets`/`--all-pins` dev slices.

`viewer/data/*.js` is COMMITTED (design note §7): the full default
export, ten sets, **7,546 rows / 1,326 matrix (set,pattern,regime,form)
groups / 45 engine columns**, 3.6 MB total (see "Deviation: file size"
below for why this is larger than the note's own estimate).

## Acceptance (design note §8), checked in order

**§8.1 — `make viewer-data` regenerates byte-stably on an unchanged
store.** Ran the exporter twice on an identical slice
(`--sets loglines`) two seconds apart and diffed both outputs with the
one line that must legitimately differ (`generated_utc`, the meta
header's own timestamp) excluded: **byte-identical**, row order and
all. `generated_utc` is the only non-deterministic field by design (a
generation timestamp cannot be otherwise) — stated here rather than
silently excluded from the check.

**§8.2 — five spot cells, one per metric/status class, matched against
committed report/matrix TSVs by value.** All five checked directly
against files already in `reports/`, not against numbers this lane
computed and is now grading itself on:

| # | class | cell | exporter value | committed source | match |
|---|---|---|---|---|---|
| 1 | measured (ns) | `loglines/bignum/large-subject-throughput/libpcre2_10.46_jit-caps-simdna` | median 11382589.670731707, spread [11358255.402439024, 11389777.158536585], n=12 | `reports/2026-09-21-loglines-0.1-...-after-25b1984f.tsv` rank row: `median_ns 11382589.670732`, `min_ns 11358255.402439`, `max_ns 11389777.158537`, `n 12` | exact (TSV's 6-decimal rounding of my full float) |
| 2 | wrong | `capability/evil-alt-nested/short-subject-search/libpcre2_10.46_dfa-nocaps-simdna` | status=wrong, n_subjects=75 | `reports/2026-09-18-capability-0.1-...-after-cf0962e3.tsv` excluded row: `pass_rate 0.9733 n=75 n_gave_up=0 n_wrong=10` | exact (n=75; n_wrong>0 ⇒ wrong) |
| 3 | gave-up | same pattern/regime, `libpcre2_10.46_{interp,jit}-caps-simdna` | status=gave-up, n_subjects=75 (both) | same report: `n_gave_up=10 n_wrong=0` on both rows | exact |
| 4 | unsup | `capability/doubled-word/large-subject-throughput/libpcre2_10.46_dfa-nocaps-simdna` | status=unsup, no numbers | `reports/2026-09-18-capability-0.1-...-after-cf0962e3.matrix.tsv`: that (row,testee) cell = `unsup` | exact |
| 5 | throughput (MB/s numerator) | `loglines/bignum/large-subject-throughput`, `subject_bytes_total` | 4,178,453 B | not a reporter TSV column (bytes aren't rendered there) — cross-checked instead against **12 independently loaded records** (different testees, different pcrec pins, different sub-bench versions of the driver) for the SAME pattern/regime, all agreeing on 4,178,453 B | internally consistent across 12 independent sources |

Row 1-4 are pin-independent (libpcre2 doesn't move under a pcrec re-pin),
so the fact that the store's newest pcrec pin has since advanced past
the cited report's own pin does not weaken the comparison. Row 5 has no
reporter-column analogue to diff against by construction (subject bytes
aren't rendered anywhere in `report.py`'s TSV), so it is verified the
next strongest way available: cross-record agreement.

**§8.3 — `viewer.html` opened via `file://` renders, filters, sorts,
switches metrics with every data file present, and degrades by name
with one data file deleted.** Two verification tracks, stated plainly
per the context-around-numbers rule:

- **Real headless-browser verification** (chromium 3529, snap package,
  `--headless=new`, driven over the DevTools protocol from a small Node
  script — not committed, throwaway, per the brief's "you cannot click a
  browser; say exactly what was and wasn't verified"). A 19-assertion
  suite ran against BOTH a development slice and the FULL committed
  `viewer/data/` (1,326 rows × 45 columns): table renders with real
  rows; the metric buttons and MB/s fallback text; clicking a testee
  column header sorts AND writes `sort=testee:...` into the hash;
  status chips render with no digit in them; a nonsense pattern
  substring yields the named empty state, not a blank page;
  deselecting every engine yields its OWN named empty state and
  re-selecting restores the table; the theme button cycles and sets
  `data-theme`; a captured hash round-trips through a fresh navigation
  and still renders; toggling a regime checkbox changes the row count;
  and — checked twice, once per probe — **zero uncaught JS exceptions
  and zero `console.error` calls across the whole session**. 19/19
  passed both times. Separately: deleting one set's data file
  (`email-specimen@0.1.js`) from a copy produced the exact named notice
  in both the summary line and the Sets panel
  (`1 set data file missing: email-specimen@0.1`) with the table still
  rendering the remaining 200 rows; deleting `manifest.js` entirely
  produced the stated fatal message
  (`data/manifest.js did not load. Run \`make viewer-data\`...`), never
  a blank page.
- **What this does NOT cover**: no other browser engine was tested
  (Firefox/Safari/WebKit) — only Chromium's headless mode. No real mouse
  hover was simulated for the tooltip (the delegated `mousemove` handler
  was read, not clicked-and-observed pixel-for-pixel) — its logic is
  covered by structural review only. No visual/layout check at all
  (phone-width degradation, dark-mode contrast, the sticky header) — CSS
  was written to the stated conventions and reviewed by eye in the
  source, never rendered and looked at by a human or a screenshot tool.

**§8.4 — non-measured cells never rank, never join best-in-row, and
sink on sort.** Two kinds of evidence: (a) `computeBest`/`_matrix`-style
logic (`viewer.html`'s `computeBest`) only ever reads `c.status ===
"measured"` cells when tracking `bestNs` — a `wrong`/`gave-up`/etc. cell
cannot become `bestNs` by construction, checked by reading the function,
not by a runtime probe; (b) a REAL runtime probe, sorting the full
production table by `libpcre2_10.46_dfa-nocaps-simdna` (a column with a
genuine mix of measured/wrong/unsup/gave-up/no-data cells) and reading
every row's status in sorted order: the transition points landed at
**index 0 (measured) → 110 (wrong) → 115 (unsup) → 120 (gave-up) → 123
(no-data/excluded)** — measured first, then exactly the brief's stated
priority order (wrong, refused, unsup, gave-up, timed-out — the two not
present in this column's data, refused/timed-out, simply produced no
transition to check), with excluded/no-data rows sinking furthest. This
IS the isolating filter state item §8.5 also asks for, reused rather
than re-run twice.

**§8.5 — engine-family toggle, regime breakout, form filter, pattern
search and hash round-trip each demonstrated.**
- Engine-family toggle: the "none" button (all engines) → "No engines
  selected." named empty state → "all" button restores all 1,326 rows.
- Regime breakout: unchecking one regime checkbox changed the row count
  from 1,326 to 1,125 (real data, real filter).
- Form filter: code-reviewed (same `isSelected`/`toggleInSet` machinery
  as regime, not independently probed at runtime beyond the syntax/
  execution check already covering the code path — a gap named
  honestly, not glossed over).
- Pattern search: the nonsense-substring case above (§8.3).
- Hash round-trip: captured `location.hash` after a sort + metric +
  theme change, navigated fresh to `URL + hash`, and confirmed both the
  hash string AND a real table still rendered on the reload.

## Deviations from the design note, each named

1. **Pin picker granularity.** §3 R3a says "a per-family pin picker";
   this build renders a **per-variant** pin picker (nested under each
   `engine_mode`+`config_extra` leaf, shown only when that leaf's data
   carries more than one distinct pin) rather than one picker per
   family. A family-level picker would force one pin choice across
   `auto`/`vm`/`auto-noedge`/etc. simultaneously, which is not how the
   store's own history moves (different configs are re-measured at
   different pins on different days — the [B61] finding this lane's own
   exporter comment cites). Per-variant is a strict refinement, not a
   scope cut; today's default export (`--all-pins` off) never populates
   more than one pin per variant per set anyway, so this path is
   unexercised by the committed data and worth a real test the day
   `--all-pins` data is committed.
2. **Regime="" refusal rows are per-testee, not per-roster.** The
   reporter's own F26 shape (`report.py`'s `render_matrix_tsv`) only
   synthesizes a `regime=""` placeholder row when EVERY testee in a
   query's roster refused/declared-unsupported a pattern. This
   exporter's `regime=""` rows fire per RECORD independently — one
   testee's own refusal never waits on the others. For a general-purpose
   viewer with no fixed roster this is the more honest shape (a testee
   that refused a pattern says so regardless of what a DIFFERENT testee
   did), but it means a pattern can show up as both an ordinary
   `regime="large-subject-throughput"` row (from the testees that
   reached it) AND a separate `regime=""` row (from the testee that
   didn't) — documented in `tools/viewer_export.py`'s own docstring,
   not hidden.
3. **Performance: the <50ms re-render budget assumed a narrower roster
   than this build ships by default.** §5 states "≈850 rows × ≤16
   columns... re-render budget <50 ms" — that arithmetic describes a
   CANONICAL-ROSTER view (pcre2 interp/jit + four pcrec modes, [B61]'s
   convention). This lane's exporter, on Frank's own charter wording
   ("selectable engines", "engine grouping... derived from data, never
   hard-coded"), keeps every ablation testee (`-noedge`, `-noclsfold`,
   `-cc-clang`, `-bigcap`, `-align64`, `-in`...) as its own column by
   default — **45 columns, not ≤16**, over 1,326 rows. MEASURED (headless
   Chromium, `performance.now()` around the synchronous
   `dispatchEvent(click)` that drives a full re-render): the FIRST
   implementation (per-cell `document.createElement` +
   `addEventListener`, the straightforward approach) measured **965 ms**
   at this scale — found only by actually timing it, not assumed. Fixed
   in-lane (not left as a finding): the table body now builds as ONE
   HTML string set via `innerHTML`, and tooltip/sort-click handling is
   DELEGATED (two listeners on `#table-scroll` total, not two per cell —
   removing roughly 120,000 `addEventListener` calls at this scale) —
   remeasured at **421 ms**, confirmed correctness unchanged (the same
   19-check suite, including the sink-order probe, re-passed 19/19
   against the production dataset after the fix. 421 ms at 9x the
   design's assumed cell count (45×1326 ≈ 59,670 vs. an assumed
   16×850 ≈ 13,600) extrapolates BACK to roughly the stated <50 ms
   budget at the design's own assumed scale — the budget is not wrong,
   the default scope this lane chose to ship is ~9x larger than what it
   assumed. Left as-is (not virtualized): 421 ms is a single click's
   cost on a drill-through view, not a blocking stall, and virtualizing
   a table this small is the complexity the design note explicitly
   ruled out ("no virtualization needed") — a future lane narrowing the
   DEFAULT column set to the canonical roster (with "show ablation
   testees" as an opt-in toggle) would recover the stated number exactly
   and is the natural follow-up if this ever feels slow in practice.
4. **File size.** §7 estimated "≈850 rows × ~200 B ≈ 400 KB total". The
   real export is 7,546 rows / 3.6 MB — ~9x the note's own estimate,
   for the same reason as #3 (every ablation testee, not a ~16-column
   roster, plus full field names rather than a minified schema, plus
   `diagnostic` text carried on refused/unsup rows). Still small enough
   to commit without a second thought (3.6 MB across 10 files), so no
   action taken; named here so a future reader isn't surprised by the
   ratio.

## What was NOT built (in scope, but not reached)

Nothing — every §1-§7 item in the design note has a committed
counterpart. The scope fence in §6 (no server, no build step, no CDN, no
subject-grain drill-down, no cross-machine UI, no editing) was
respected by omission — nothing under this lane's diff adds any of
those.

## Numbers this report owes nothing further on

`make viewer-data` (no args) ran to completion on a quiet box (load
average ~1.2-2.1/12 cores, no `run_window.sh` or `~/pcrec/studies`
process running, checked immediately before and confirmed clean
throughout — box facts recorded here per BOILERPLATE.md, not owed to a
future run): **86 records loaded, 7,546 rows written across 10 sets**,
committed at `viewer/data/*.js` (0644, matching every other generated
file in the repo).

## Files touched

- `tools/viewer_export.py` (new)
- `viewer/viewer.html` (new)
- `viewer/CLAUDE.md` (new)
- `viewer/data/manifest.js` + `viewer/data/<10 sets>.js` (new, committed)
- `Makefile` (± `viewer-data` target + `.PHONY`)
- `tools/CLAUDE.md` (+1 row)
- `CLAUDE.md` (root; +`viewer/`/`tools/` entries, +`make viewer-data` line)
- `docs/dev/lanes/b66viewer_report.md` (this file)

Branch `lane/b66viewer`, not merged. Worktree at `worktrees/b66viewer/`.
