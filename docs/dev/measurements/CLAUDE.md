# docs/dev/measurements/ — archived driver probes

One-off MEASUREMENTS that answer a question a `pcrecbench run` cell cannot
express (a subject set the regime does not map to, a control flag no
testee carries, a length curve), archived in pcrec's D35 style. The rule
is the same as ~/pcrec's `docs/design/*_measurements/` and its D35:

1. **Stable file name**: `YYYY-MM-DD-<topic>.txt`, never renamed; a
   re-measurement is a NEW file with a new date, and the old one stays.
2. **Verbatim output**: the driver's own stdout, every trial, unedited,
   after a source header. The summary table at the bottom is DERIVED from
   the verbatim block by the archived script and carries numbers only —
   no interpretation beyond "flat" / "proportional to length"; the reading
   is the manager's, in plan.md / dev_journal.md / the outbox.
3. **Source header**: the bench commit, the pcrec pin (commit + binary
   sha256), the engine library version, the compiler, the box, the exact
   command per arm, every flag, the load samples (`/proc/loadavg` before
   and after every sweep) and whether the box was GATED — a probe run
   beside another session's lanes says so, in the file.
4. **Reproducible**: the script that produced the archive is committed
   beside it (`probe_<topic>.py`), reuses the adapters' own compile and
   driver paths (never a second copy of a flag set or a pattern
   spelling), and runs from the repo root.
5. **NEVER a ranking input.** Nothing here is a record: no schema, no
   `store/`, no reporter. Scratch tier by construction. A number that
   matters for a ranking goes through a sub-bench version bump and a
   pinned cell.

| file | what |
|---|---|
| `probe_engabs_longsubject_match.py` | ([B18] (d)) the LONG-SUBJECT FAILING anchored `_match` probe: pcrec's [ENG-ABS] claim (inbox I-16, "O(divergence), not O(subject)") measured with the bench's own `(?:orig)\z` whole-subject artifact on the five 1 MB throughput subjects of bench/email + 64 KB / 4 KB prefixes + two short sanity subjects, six arms (pcrec-auto at the pin; the same pin with `-fno-anchored-dfa` as the CONTROL; `--engine=vm`; pcre2-jit; pcre2-interp; the set's floor pattern as the per-call floor), per-(arm, subject) iteration calibration, interleaved trials, `taskset -c 11`, the divergence byte of each subject from libpcre2 partial matching |
| `2026-08-29-engabs-longsubject-match-probe.txt` | its archive at pcrec pin 36d5963 (abi 11), 5 trials, box NOT gated (pcrecdev1's lanes running; load sampled) |
| `probe_gate_shape.py` | ([B12]/BD7, the 2026-08-30 gate-shape test run) reads PINNED RECORDS only: per record the stamped status, the occupancy instrument, both samples' judged number + verdict, the OLD 1-s gate's verdict RECOMPUTED from the per-second peaks a BD7 record keeps in `occupancy.after.raw` (first-second = the old instrument's one interval; any-second = its worst case), and the trial-spread distribution over every timed match row ((max-min)/median per (pattern, regime, subject); median / p90 / max, rows over 20 % and 50 %). Runs from the repo root on `store/records/<set>/*/*.jsonl` |
| `2026-08-30-gate-shape-test-run.txt` | its archive over bench/bounded@0.1's nine 36d5963 records: the six first-window cells (1-s instrument; three `inconclusive-load` on the after-sample) and the three BD7 re-runs (all `measured` on attempt 1; after-samples 1.81 / 2.00 / 3.81 %; the old 1-s gate recomputed from the recorded peaks: two cells pass on every second, `pcrec-vm-in` FAILS on one of its five seconds, 11.88 %); trial-spread medians 1.3-4.0 % with the re-runs matching their first runs; the `--outliers=50` listing (one trial of five, group-wide, never trial 1) |
| `probe_trial_agreement.py` | ([B20], schema v1.4 `docs/design/gate_shape_v14.md` §3) the TRIAL-AGREEMENT CENSUS: reads PINNED RECORDS only (default: every `store/records/*/*/*.jsonl`); the no-argument run is the ROW-level census — per timed row ((pattern, regime, form, subject), `iterations > 1`, ≥ 2 timed trials) the per-trial ns/iter and the median; for k in 1.25 / 1.5 / 2.0 the trials STRICTLY ABOVE k × median (slow outliers), whether the min is BELOW median / k (a fast outlier), and the row's DISAGREEING verdict (≥ 2 slow OR fast); per record the counts and fractions, every disagreeing row in full at k = 1.25 and 1.5, the worst row (the probe's own ordering, not a v1.4 field), the slowest-trial index histogram; a summary over all records per k with the worst five. `--groups` (the r3 panel, ruling R-16) prints the GROUP-level census INSTEAD: the spec's §3.5 row arithmetic (a `timed-out` trial makes the row disagree; rows with < 2 timed trials are unjudged and counted), per record the trials, row keys judged / unjudged / timed-out, the groups (one (pattern, regime, form) each) and their sizes, at every k in 1.25 … 2.0 the rows disagreeing, the largest d in any group, the worst group and the groups that would DISAGREE under each candidate (D_MIN, c) in {2,3} × {2,3,4} (`d ≥ D_MIN and c·d ≥ n`); the summary gives the group-size census per sub-bench, the per-candidate counts at every k and R-16's CONSTRAINT TABLE (per group size: the threshold in rows, whether a whole-group two-pass disturbance and a half-pass overlap flag, the margins over the store and over the half shape). Runs from the repo root |
| `2026-08-30-trial-agreement-census.txt` | its archive over the WHOLE canonical store at bench 4f2f210 — 68 records (schema 1.1 × 11, 1.2 × 3, 1.3 × 54; 59 measured + 9 inconclusive-load; five pcrec pins + libpcre2 10.46), 62,923 rows, every one with 5 trials: at k = 1.5 ZERO rows with two slow trials and ONE fast-outlier row (a 3-2 split at the timer floor), worst record 0.204 %; at k = 2.0 nothing; at k = 1.25 21 slow-pair rows and 37 fast-outlier rows over 20 records, the `loaded` email@0.2 interp record worst at 1.996 %; the slowest trial is t1 in 36 of 387 single-slow rows (the least frequent index). The constants k = 1.5 / F = 1 % of the v1.4 rule are read from this file |
| `2026-08-30-trial-agreement-census-groups.txt` | its `--groups` archive over the same 68 records at bench 409c1dd (the r3 panel, ruling R-16): 63,028 row keys, 62,928 judged (the 62,923 plus five rows whose every trial is `timed-out`, counted as disagreeing under R-19's first wording — the E-1 ruling makes them `all_timed_out` unjudged; no group verdict changes), 100 unjudged, 1,731 groups (sizes: bounded 4 / 30; email@0.1 2 / 3 / 77 / 80 / 85; email@0.2 4 / 5 / 77 / 80 / 85; loglines 12 / 112); at k = 1.5 the largest d in any group is ONE (the floor/s-081 fast row, 1 of 77; the five timed-out rows, 1 of 3 or 5), so every candidate has ZERO disagreeing groups; the loaded email@0.2 interp record is flagged under (2,3) at k ≤ 1.40 (d = 3 of its 5 floor-throughput rows) and clears at 1.45; (2,2) fails the half-pass shape at odd n and every D_MIN = 3 candidate fails it at n = 4, 5; (2,3) and (2,4) flag both shapes at every named size. The constants k = 1.5, d_min = 2, share_c = 3 of the v1.4 GROUP rule are read from this file |
| `probe_year4_elf_alignment.py` | ([B22] (f), inbox I-22 (iii)) the `year4` .so-step DERIVATION (compile-only facts; no timing, no window): re-emits `\d{4}` at BOTH pin snapshots (36d5963 / 96e44c2) with the adapter's own command shape, counts source raw + by `adapter.emit_size` (the ported `emit_size_measure`), rebuilds each .so with the ERA-CORRECT shim each store record was actually built with (the BEFORE predates [B19]'s shim: commit 4d666dd vs cb169df, extracted from git), checks against the records' `artifact_bytes`, and prints `readelf -lW`'s LOAD segments; the one-shim rebuild of both pins is the control |
| `2026-08-31-year4-elf-page-alignment.txt` | its archive: pcrec's own source grew **+33 B** (the three abi-12 stamp lines; I-22's "~+220 B" was high) while the recorded .so stepped +4,320 on both forms — reproduced EXACTLY under the era shims and decomposed as **~+384 B of [B19] SHIM growth** (the two R LOAD segments) **plus +4,096 B of ELF page alignment** (the RW segment's file offset steps one 0x1000 page, filesz unchanged); the CONTROL: both pins under ONE shim build BYTE-IDENTICAL .so files. I-22 (iii)'s mechanism CONFIRMED, the trigger attributed to the bench-side shim, not pcrec; `year4` is not a pcrec size effect at all |

| `probe_spread_rule_control.sh` | ([B23], gate_shape_v14.md §9 Q3 (a)+(b)) the v1.4 spread rule's MEASURED POSITIVE CONTROL and its measured MISS, three arms end to end via `pcrecbench run` itself on one scratch-tier cell (email-specimen@0.2 × pcre2-interp, search_short only, 5 trials, `--pin 11`): `control` (clean box), `loaded` (a memory-bandwidth competitor — python copying a 64 MiB bytearray — pinned to CPU 5, the target core 11's SMT sibling, for 22 s ≈ two SLOWED passes of the TARGET GROUP `factored / short-subject-search / plain`, named in advance), and `uniform` (Q3 (b): the same competitor covering ALL FIVE passes, event-scoped — started at the group's own "measuring" stderr line, killed by PID at the next group's "calibrating" line, gnutimeout 90 s backstop). Synchronization is the run's own progress output (rehearsed constants in the script header); gnutimeout is the competitor's parent; records go to scratch stores under `build/`; `[arms]` selects a subset |
| `2026-09-01-spread-rule-positive-control.txt` | its archive: each arm's prediction stated BEFORE its run and held — `control` `measured`/`agree` exit 0; `loaded` `inconclusive-spread` exit 4, `worst_group` factored **d = 77 of n = 77** (70 rows by two slow trials, 7 by the fast clause), the §3.4 sentence first in `status_detail`, the §3.6 timeline locating the competitor (sibling 55.69 % on the target group, < 1 % on orig/floor); `uniform` **MISSED as band 2 predicts** — every trial slowed ~1.77× (t1-t5 all ~3100-3181 vs the control's ~1790), the record stamped `measured`/`agree` exit 0 at d = 4 of 77 (fast-clause edge rows under the threshold 26), the ranked number itself ~1.77× wrong, and the timeline the ONLY instrument that shows it (sibling 99.62 % across the whole group). The kept rehearsal caveat: a pure busy-loop sibling (s ≈ 1.45) is NOT flagged — blind band 1 is real at SMT-execution magnitudes; the file is the instrument's positive case AND its stated limitation, both measured |
| `probe_hybrid_gained_edge.py` | ([B27] (3), outbox O-12 / inbox I-29 ask (v)) the HYBRID-GAINED-EDGE CENSUS: a READ of pinned records only (no compile, no run, no timing) over `store/records/<set>/*/*.jsonl` at two pins. Selects the artifacts whose VM HYBRID prefilter gained the abi-13 scan edge (`engine == "vm"` AND `dfa_scan_edge` not in (absent, `none`) -- a VM artifact carrying that stamp at all is a hybrid, by the stamp's own scope rule), and for each emits the stamps, the per-regime SET-GRAIN median before and after, the ratio and a verdict, plus per-SUBJECT rows under the hybrid arm and the same pattern's SIBLING PLAIN artifact for context. The comparable is `pcrecbench.reduce`'s own `reduce_set_cell` / `reduce_match_cell`, imported rather than re-derived (rule R5). Duplicate records per testee are resolved to the latest and the discard is NAMED in the header. `--set` / `--after` / `--before` / `--store` / `--tsv`; runs from the repo root |
| `2026-09-01-hybrid-gained-edge-census.tsv` | its archive over `bounded@0.2` at a7e0bdf vs 263b013 (eight records, source header naming each): 132 rows. The POPULATION is **two artifacts** -- `nest2-64` and `nest3-16` WHOLE-SUBJECT, both `collapsed-prefilter` / `byte-class-bounded`, edge absent -> `range` -- on the two `auto` testees, four record cells, exercised by the `match` regime ALONE |
| `2026-09-01-hybrid-gained-edge-census.md` | its reading note: (a) the ledger's "thr x1.57-1.59 faster, match x1.04-1.05 slower" is NOT one artifact's trade -- the throughput and search wins belong to the sibling PLAIN DFA artifact and the hybrid that gained the edge is only ever measured in `match`, where it only ever got slower; (b) the cost is a FIXED per-call term (+5.9..+7.9 ns on `nest2-64` across a x13 span of call cost), so the x1.53 worst case is that term on a 24 ns call; (c) it fires only on MATCHING calls -- the seven pure-digit subjects moved, the other 23 are x0.98-1.01 including those that enter the digit run before failing. One tunable term plausibly explains asks (ii) and (v) together; nothing here locates the boundary, which is what `bounded@0.3`'s low-rung sweep is built to read |

Maintenance: update this file when files are added/removed or change role.
- `2026-09-01-engine-sel-census-a7e0bdf-vs-1989c62.tsv` — ([B26] (a), lane b26repin) every bench pattern × form × engine mode compiled at both pins, the RX_ENGINE_SEL / engine / prefilter / lang stamps per cell: identical totals at both pins; NO bench artifact stamps `declined-nullable-default`; 80 refusals per pin incl. altwide's ci-512 at the 1,000,000 B emit cap.
- `2026-09-01-emit-sizes-a7e0bdf-vs-1989c62.tsv` — ([B26] (a)) the emit-size port on the ledger patterns at both pins: +202 B total / +105 B code flat (abi 15's two rx_info fields), o42's declines the only downward moves.
- `probe_bounded_cross_version.py` — ([B26] (c)) the CELL-AGAINST-CELL read of one
  `bench/bounded` set version against the next across a pcrec pin: a READ of pinned
  records (no compile, no run, no timing) that emits one row per (pattern, subject,
  regime, form, testee config) whose pattern id AND subject id exist in BOTH sets
  with EQUAL pattern `canonical_sha256` and EQUAL subject `sha256`/`bytes_offered`
  — the promise `bench/bounded/NOTES.md` makes about 0.3's no-drift redraw, checked
  rather than trusted, with every rejected id named in the header. The comparable is
  `pcrecbench.reduce.reduce_match_cell` imported (never re-derived); `ratio` is
  after/before. Exists because 0.2 and 0.3 NEVER POOL, so no reporter query can
  answer "did anything move on the surface both sets share". `--before`/`--after`
  take `<subbench>@<version>:<pin>`; runs from the repo root.
- `2026-09-02-bounded-cls-rungs-0.2-a7e0bdf-vs-0.3-1989c62.tsv` — its archive over
  bounded@0.2 at a7e0bdf vs bounded@0.3 at 1989c62 (eight records, four testee
  configs, source header naming each): 30 shared patterns and 35 shared subjects,
  ALL byte-identical on both sides, 7,670 cells. This is the [OPT-4.2]/abi-15
  CONTINUITY reading and the [OPT-5] STEP 2 BEFORE's anchor. The file carries the
  per-cell `iterations` on both sides and states its own caveat: 0.3 changed both
  calibration pools (match gains subjects to 1024 B; `short_search_max_bytes`
  512 → 258), so a ratio whose two sides differ greatly in `iters` is a calibration
  candidate, not necessarily a pin effect.
- `2026-09-02-scan-edge-attribution-census.txt` — ([B32]) where pcrec's
  `// [OPT-5] SCAN EDGE:` marker LANDS, over 57 patterns of loglines, email and
  bounded × both forms × three engine modes (342 attempted, 338 compiled, 4
  refused at the NFA cap). The measurement that establishes the adapter's
  three-function attribution table for `scan_edges` / `scan_edges_match`: a
  marker never lands outside `rx_search`, `rx_prefilter` and `rx_match`, a VM
  hybrid's edges are ALL on the search side (its `rx_prefilter` is called from
  `rx_search_run` and nowhere else), and both scan directions go into
  `rx_search` — which is why loglines `iso-ts` reads 8 search / 4 match, I-33's
  own numbers. Every row was counted TWICE, by the adapter's counter and by an
  independent reader sharing no source with it; the two agree on all 338.
  Nothing here is a timing, so the box's load does not enter it.
