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
| `probe_capability_refusal_census.py` | ([B69], Frank's ruling on the wild-codegrammar-json-number-extended finding) THE CAPABILITY REFUSAL CENSUS: a READ of pinned records only (no compile, no run, no timing) over `store/index.tsv` + `store/records/capability@0.1/*/*.jsonl`, restricted to the 13-testee roster the 2026-09-20 fullroster-25b1984f matrix report's own header names, newest record per testee on `budu-ryzen1600`. Every `kind=="compile"` row keyed by (pattern_id, form or "plain"); cross-checked against `bench/capability/patterns.rxt`'s own 64 `name` lines (all 64 accounted for); classifies every (pattern, form) with >=1 genuine `did-not-compile` row into Frank's CASE 1 (every ATTEMPTING engine refused) / CASE 2 (split), with `unsupported-by-declaration` policy intercepts counted and listed separately (never as a refusal -- no attempt was made). Runs from the repo root |
| `2026-09-21-capability-refusal-census.txt` | its archive (budu-ryzen1600, load1 0.7-0.9, read-only): 64/64 patterns accounted for, 157 non-compiled compile rows (124 `unsupported-by-declaration` policy declarations across 25 patterns, 33 genuine `did-not-compile` refusals across 7 patterns). **CASE 1 (2 rows, both instrument-fail, the (?x)-comment-eats-the-wrapper class): `wild-codegrammar-json-number-extended` and `wild-codegrammar-json-stringcontent-escape`, both `whole-subject` only** -- all 7 attempting testees (oniguruma, all four pcrec configs, rust, vectorscan; tre already `unsup` on `free-spacing`) refuse with mechanism-consistent diagnostics (oniguruma "unmatched parenthesis", pcrec "missing closing )", vectorscan "Unterminated comment", rust "parse error"), because the pattern's raw `.rxt` text ends on a `(?x)` `#...` LINE COMMENT with no trailing newline, so the harness's appended `(?:<pattern>)\z` wrapper is silently swallowed into the comment -- confirmed as a control against the corpus's other two `free-spacing` patterns (`codegrammar-xflag`, `bracket-array-define`), whose raw text ends with a newline/no trailing comment and whose whole-subject forms compile clean on every one of the same 7 testees. **CASE 2 (12 rows, all already-documented, genuine, engine-specific limitations -- no new pcrec ask)**: `wild-datetime-datefinder-alternation` (pcrec's 500,000 B emit-code-size cap, already outboxed O-31 item 5, reconfirmed at pin 25b1984f; tre's POSIX bracket-range bug, `testees/tre/CLAUDE.md` item 4), `wild-secrets-username-password-pair` / `wild-waf-crs-942500-comment-obfuscation` (the same tre bracket-range bug, both patterns named in that same CLAUDE.md entry), `balanced-parens-rec` (oniguruma's documented `(?R)` spelling gap, `testees/onig/CLAUDE.md` item 2 -- pcrec/libpcre2 compile fine, the roster-context inverse), `mojibake-curly-quote` (rust's structural UTF-8-pattern-source constraint, `testees/rust/CLAUDE.md`). See `docs/dev/lanes/b69census_report.md` for the full derivation and charter-vs-committed checklist |

- `probe_re2_capability_census.py` / `2026-09-17-re2-capability-census.txt`
  — ([B42] L6b, `testees/re2/`) THE RE2 CAPABILITY WITNESS CENSUS: one
  witness pattern per `REQUIRES_VOCAB` token plus every `bench/
  capability@0.1` (64) and `bench/syntax@0.1` (95) canonical pattern,
  compiled through the real `testees/re2/adapter.py` `compile()` path
  (compile-only, no timing, never a ranking input). Derives
  `bench/capability/gen_patterns.py`'s `re2-default`/`re2-longest`
  `EXT_BENCH_ROSTER` rows: REFUSED (RE2's own `ErrorCode`, every time) —
  `backrefs`, `lookaround`, `lookbehind-variable`,
  `possessive-quantifier`, `atomic-group`, `recursion`, `conditionals`,
  `k-reset`, `control-verbs`, `free-spacing`, `callouts`; SATISFIED —
  `unicode-properties`, `named-groups`, `span-reporting`,
  `non-utf8-subject`, `captures`, `true-end-anchor`. Corpus totals:
  `bench/capability` 39/64 compiled; `bench/syntax` 47/95 compiled.

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
- `2026-09-03-window-cross-file-derivations.txt` — ([B31] reports lane) four
  tables that no single committed report holds, because each is a division
  ACROSS two files, or across a report and a window log. Nothing here was
  measured by that lane and no engine was run: every number is read out of a
  committed artifact named beside it. (1) The altwide@0.2 cell wall clocks
  against `bench/altwide/NOTES.md`'s estimate, with a CORRECTION to the anchor
  that estimate was built on — the NOTES' "the MEASURED 0.1 auto cell was 30
  min" is pcre2-JIT's 0.1 cell; the real one was 4.8 minutes, and the 0.1
  window log's own cell lines are quoted. (2) The raised-cap compile
  projection from `2026-09-02-altwide-raised-cap-sizes.txt` section 2 against
  what the bigcap cells actually cost (both inside 4 %), plus the cell-by-cell
  evidence that the raise removes a gate and changes nothing else: auto
  artifacts byte-identical, VM artifacts exactly +1 byte (derived: the code
  cap's own extra digit in the emitted source), `K=8/default` on all 106 VM
  legend lines across both arms. (3) The `-fno-scan-edge` arm against the
  2026-09-02 ledger §7.2, where the recovered time matches the measured
  regression to three figures on all five rows and the recovered SIZE matches
  to exactly 6 bytes on all three edge-taking patterns — 6 B being the flag's
  own constant, established by the eight zero-edge patterns. Includes the
  same-pin repeatability floor (22/22 cells within 1.32 %) the small ratios
  have to clear. (4) The I-37 clang re-run against the 2026-09-02 cell, and
  the statement of which half of the disputed ratio was re-measured.
- `probe_altwide_size_census.py` — ([B35] (7) / [B39]) the altwide RAISED-CAP
  SIZE CENSUS, turned from the 2026-09-02 one-off (`census.py`, reproduced at
  that file's own foot) into a stable, RE-RUNNABLE, PIN-PARAMETRIZED probe:
  every `bench/altwide` pattern (read from `subbench.toml` via
  `pcrecbench.subbench.Subbench`, never re-parsed) x both forms x both
  engine modes, compiled at pcrec's DEFAULT emitted-size caps (read from
  `testees/pcrec/list_limits.tsv`, never retyped) and again under a probe
  raise, recording pcrec's own `emit_bytes` / `emit_code_bytes`
  (`testees/pcrec/adapter.py`'s `emit_size` port). `--pin <sha>` resolves
  through `testees/pcrec/pin.sh --path` (never asks it to BUILD);
  `--compare <old-file>` prints per-route (`auto`/`vm`) byte and percent
  deltas against a previous census's own table. Exists because pcrec inbox
  I-50 found the 2026-09-02 numbers stale by -18...-26 % per rung on the VM
  route at pin 334fd10e ([ENG-ISL] STEP 1's alternation-island trie) —
  re-derive at every re-pin (`bench/altwide/NOTES.md`'s census section has
  the command). `--dry-run` prints every argv without touching pcrec.
  Self-tested 2026-09-05 with no pcrec binary at all: `--dry-run --compare`
  against the real 2026-09-02 file parses its 80-row table and prints "0
  patterns compared" against the empty new table `--dry-run` produces
  (the parser's own end-to-end path); separately, `parse_census_table` /
  `compare_tables` were imported directly and run against a SYNTHETIC new
  table (the 2026-09-02 rows copied with `w-512`'s `vm` `emit_bytes` /
  `emit_code_bytes` scaled by 0.80, an -20 % stand-in for I-50's finding):
  the printed `vm` section read `678315 -> 542652  -135663  -20.00%` on
  exactly that row and `+0 / +0.00%` everywhere else including `w-512`'s
  own `auto` sibling — the route split, the sign and the arithmetic all
  read correctly. Neither check compiled anything or touched a pcrec pin.
- `probe_cc_gate_census.py` — ([B33] (1), `make cc-gate-census`) THE CLANG
  COMPILE-ONLY GATE, made repeatable: every `bench/<name>/` pattern (by
  `subbench_dirs()` enumeration, mirroring `tools/selfcheck.py`'s own rule)
  x THREE pcrec ENGINE MODES (`auto`/`nocaps`/`vm` -- read from
  `testees/pcrec/configs.toml`'s `pcrec-auto`/`pcrec-nocaps`/`pcrec-vm`
  entries, never retyped; this is the SAME "mode" this project already
  uses for a full-corpus 3x2 census -- `testees/pcrec/CLAUDE.md`'s [B26]
  entry ("77 patterns x 2 forms x 3 engine modes (auto, nocaps, vm) = 462
  cells") and `tools/selfcheck.py`'s `check_cc_axis`/`CC_KIND_CASES`, NOT
  the harness's regime tokens (`match`/`search_short`/`throughput`), which
  `pcrecbench.subbench.REGIME_MODE` maps onto only two match semantics and
  would either duplicate compiles or need per-set regime filtering for no
  reason -- the ORIGINAL a7e0bdf hand census this replaces found its one
  divergence on FRAMELESS VM artifacts, which only appears by forcing or
  auto-selecting the VM broadly, exactly what the engine-mode reading
  predicts and the regime reading does not) x TWO forms (`plain`,
  `whole-subject`). Per cell: emit-c ONCE (pcrec's C does not depend on
  which compiler will consume it), then gcc and clang each once on the
  SAME one-translation-unit shim+artifact command
  `testees/pcrec/adapter.py`'s phase 2 uses -- IFF pcrec's own emit
  succeeded (a pcrec-side refusal is recorded once, for both compilers,
  since neither ran). Compile-only: no phase 3 (no dlopen, no driver, no
  match run), no quiet-box gate. The GATE is refusal-set PARITY
  (`gcc_refusals == clang_refusals` as a set of (subbench, pattern, mode,
  form) keys) -- exit 0 on parity, 1 on a divergence (printed as a finding,
  never edited away). `--pin` resolves through `testees/pcrec/pin.sh
  --path` (never builds); `--subbench NAME` (repeatable) restricts the
  sweep for a rehearsal; `--dry-run` prints every argv untouched.
- `2026-09-07-cc-gate-census-d34c9131.txt` — its first archive at the
  current pin: see the file's own header/footer for the exact cell count,
  wall-clock and parity verdict (filled in by the real run this lane
  performed; docs/dev/lanes/b33cc_report.md states the numbers inline).
- `probe_rxt_format.py` — ([B42], lane b42rxtneeds) TWENTY PARSE-ONLY
  probes of pcrec's `.rxt` SOURCE GRAMMAR at the pinned binary, written
  for `docs/design/rxt_needs_v1.md` §1.9 (the `.rxt` capability feedback
  to pcrecdev1). Each probe writes a fixture of at most six lines, runs
  `pcrec --list-source` on it, and prints the fixture, the exit code,
  every data row, and — where the probe is about byte fidelity — the
  decoded `pattern` column against the bytes that went in (the decoder is
  a byte-level second implementation of `--list-source`'s own TSV-safety
  escaping, deliberately not shared with `tools/export_rxt.py`'s, so the
  two are a control on each other). NOTHING HERE IS A TIMING: no compile,
  no artifact, no dlopen, no driver, no engine run, so the archive
  carries no load samples and no gate verdict and the box's state cannot
  affect a character of it — the one respect in which it departs from
  rule 3 above, by having nothing to report rather than by omitting
  anything. `$PCREC_BIN` overrides the pin; run from a worktree it
  resolves `build/` through the git common directory; the fixture
  directory has a FIXED name (`$TMPDIR/rxtprobe`, emptied each run) so
  pcrec's path-quoting diagnostics do not put a random component in the
  archive — a re-run reproduces the committed file byte for byte except
  its `# bench:` provenance line.
- `2026-09-12-rxt-format-probes-d34c9131.txt` — its archive at
  d34c9131 (abi 23). The two findings that are SILENT DATA LOSS in
  shipped behaviour: a literal NUL in a `pattern` line TRUNCATES the
  pattern (`ab\0cd` → `ab`, exit 0, no diagnostic — the parser splits the
  slurped file into NUL-terminated C strings), and a SECOND
  `description` line in one block silently overwrites the first. Both
  are outside this project's own ask and are filed to pcrecdev1 as
  findings. Everything else round-trips byte-exactly (high bytes, a
  mid-line tab, a doubled backslash, a mid-line CR, trailing spaces); a
  CRLF line end trims the CR (documented); a duplicate block name, an
  indented continuation line and every W2/W3 keyword are refused BY NAME
  with the wave named; a `target`-less, `config`-less authored file with
  a head block scalar parses and dumps cleanly; and `--list-source`
  ACCEPTS a case line carrying a refused `@file:` subject, because the
  head parser recognises `m` and reads none of its values — so the dump
  is not a validator for case-line content.
- `2026-09-06-altwide-size-census-d34c9131.txt` — ([B39], the abi-23
  re-pin) the FIRST run of `probe_altwide_size_census.py` against a real
  re-pin: 132 rows at d34c9131 (33 patterns x both forms x both routes,
  default caps 1,000,000 / 500,000 read from the re-archived
  list_limits.tsv; ci-* the fold witnesses) with `--compare` against the
  2026-09-02 table (pin 1989c62, abi 15; 80 keys in both). THE READING:
  VM route median −15.6 % emit bytes (range −40.2 % … +2.3 %; w-256 and
  srt-256 IDENTICAL at 292,074 B, −14.4 % — the island trie; ci-512 −21.2 %
  and ci-256 359,507 B from 451,050 at 334fd10e, −20.3 % — the [FORM-CHAR]
  fold-pair lowering's own shrink on the ONE corpus witness, vs pcrec's
  __TEXT −31 % on theirs); AUTO route median +0.06 % emit bytes but
  +3.2 % CODE bytes (+627 … +886 B per DFA artifact across abi 15 → 23 —
  the cross-pin sum of STEP 2's pinned start, the uniform-fold tables and
  the edge dispatch, NOT this re-pin's, which predicts and measures the
  DFA artifact UNMOVED against 334fd10e). The refusal boundary UNCHANGED
  from 334fd10e: DFA wall at w-384 (total cap), VM wall 384 < w <= 512
  (w-512 refuses on `code`), ci-512 refuses on BOTH routes, pfx3-512 and
  w-384 compile on the VM route. This is the [B35] (7) re-derivation
  I-50 §5 asked for; the numbers replace the 2026-09-02 table's for any
  reader of the size books.
- `accept41_cd371441/` — ([B42] restart step (1), lane `b42accept`) THE
  AUTHORITATIVE RUN of `docs/design/rxt_needs_v1.md` §3's 41-check
  acceptance checklist against pcrec's delivered pin **cd371441** (abi
  23, [DD-13b.W23] full first-delivery scope): `run.sh` (reproduces the
  archive below byte for byte except its `# bench:` line; resolves the
  binary through the git common directory when run from a worktree,
  same rule as `probe_rxt_format.py`) + `fixtures/` (one `.rxt` per
  check, `b7_driver.c` — a from-scratch C driver against the generated
  matcher's own `rx_search` API, built because B7 needs a subject read
  from a FILE, which pcrec's own `tests/harness/run.sh` reads but this
  project may only invoke read-only, never build inside; C8/C9 instead
  invoke that script directly, pointed at our own fixtures with
  `TMPDIR` under our own scratch — no write ever lands in `~/pcrec`).
  Corrections from inbox I-67 (absorbed from
  `~/pcrec/docs/design/dd13_format/format_design.md` §9 at the pin,
  read-only) applied before running, not after: A2's fixture drops
  `config … testee`/`option` (D99); F2's literal set-file premise is
  DISSOLVED (D99) and re-tested on a target-bearing file instead, where
  Frank's 2026-09-15 engine-precedence ruling (inbox I-68 item 1) fires
  live; B6's premise is DISSOLVED (`pattern`/`pattern-esc` are both
  block openers, so a second one starts a new block) and the rewritten
  assertion verified true; `license` not `licence`; eleven provenance
  keys, not nine.
- `2026-09-16-b42-acceptance-41-cd371441.txt` — its archive: a 41-row
  verdict table (33 PASS / 0 FAIL / 1 DISSOLVED-but-verified-true / 8
  NOT-RUNNABLE) followed by every check's verbatim command and output.
  Superseded pcrecdev1's own dry run (25/41 runnable,
  `~/pcrec/docs/dev/lanes/w235_report.md` §3) as the pass of record
  (I-68 item 2). Findings: B3's NUL-refusal and C10's second-description
  refusal are BOTH now live exactly as asked (`rxt_needs_v1.md` P-Q7,
  P-Q9); F2's CLI-vs-file engine-precedence exception (I-68 item 1) is
  CONFIRMED LIVE, closing the one NEW finding pcrecdev1's own dry run
  raised; G2's 185/185 round-trip was re-run directly against the
  delivered pin (not the older pinned testee); G3's diff has ZERO
  unexplained hunks — two apparent regressions (M10b, M10d) are the
  ARCHIVED PROBE's OWN fixtures predating the finalized `variant`/
  `include` grammar, not a delivery defect. E1/E2/E3/E6/E7/F3/F4 are
  NOT-RUNNABLE because the `.rxt` loader and the capability@0.1 set are
  UNBUILT (Tier 1 of the restart's next step, confirmed empty by a
  grep at D2); G1 is NOT-RUNNABLE by the repository mandate (BD2: no
  build/test in `~/pcrec`'s tree from here).
- `probe_o29_verify.py` — ([B42] runbook step 3, lane b42verify,
  2026-09-16) the O-29 (+K57) fix-pin verify chain: nine parse-only
  probes (the 3-block minimal repro + the 2-block variant twin, the
  64-block corpus dump + the loader-gate refuse→load flip run against
  BOTH pins as a two-sided control, all four `#section` kinds in one
  multi-block file, B3's NUL refusal + its control, the K57 shallow-
  dedent refusal + its compliant control). Every fixture's bytes are
  literals in the script; every probe states its failing direction.
  Takes the pcrec binary as argv[1] (default: the pin's).
- `2026-09-16-o29-verify-a770139e.txt` — its archive at the fix pin:
  9/9 PASS. The corpus dumps 64/64 provenance rows (0 variants,
  matching variants.tsv); `load_rxt_source` refuses the same file at
  cd371441 citing O-29 and loads it at a770139e; the K57 diagnostic
  refuses by name, class `value-shape`. The verify I-71 asked for,
  and the gate on which the [B42] sidecar switch + first sample ran.
- `probe_mojibake_span.py` + `2026-09-17-mojibake-span-probe-a770139e.txt`
  — (O-31 ask 4, pcrecdev1's charter) the mojibake-curly-quote
  narrowing probe: NOT a span disagreement — all four pcrec configs
  DISMISS `\x93hello\x94` outright (both routes) where both pcre2
  arms match [0,7). The within-set discriminator: raw high literal
  bytes IN THE PATTERN TEXT are the failing shape (subject-side raw
  high bytes and regex-level `\xNN` pattern escapes both work —
  `utf8-lead-no-cont` is the clean control through the same loader).
- `2026-09-17-mojibake-postfix-argv-bytes.txt` — (inbox I-72) the F4
  attribution FLIP and post-fix run: the mechanism was OUR adapter's
  `pattern.decode("latin-1")` + fsencode re-encode (every pattern byte
  >= 0x80 reached pcrec's argv UTF-8-mangled; pcrec answered the
  corrupted pattern correctly). Fixed as raw-bytes argv; all six
  probe arms flip to matched-as-expected; the affected-cell census
  (exactly two capability patterns corpus-wide) and the re-measure
  plan are in the header. Guard: selfcheck's
  check_high_byte_pattern_argv. The prior probe archive's data
  stands; its attribution sentence is superseded by this file.
- `probe_onig_capability_census.py` — ([B7]/L6b, lane l6bonig, 2026-09-17)
  the ONIGURUMA ADAPTER'S capability witness census, mandatory before
  `bench/capability/gen_patterns.py`'s `EXT_BENCH_ROSTER` declares
  anything for `onig-default`: pass 1 runs one (or several, where one
  spelling would not settle the question alone) isolated witness per
  `REQUIRES_VOCAB` token through the real `onig-default` adapter; pass 2
  runs all 64 real `bench/capability` corpus patterns through the same
  adapter, cross-referenced against each pattern's own `requires-*` tags.
  Runs from the repo root; needs the `onig` adapter (built on demand).
- `2026-09-17-onig-capability-witness-census-6.9.10.txt` — its archive:
  CB5 (atomic-group) and CB6 (`\K`/k-reset) resolved by DIRECT SOURCE
  READ of Oniguruma 6.9.10's `regparse.c`/`regexec.c` (both SATISFIED,
  `(?>...)` ungated by any syntax flag, `\K` architecturally identical to
  PCRE's own reset-the-reported-start mechanism) before either is
  declared; 62/64 corpus patterns compile clean, the two refusals
  (`negation-scope-lookbehind-var`, `balanced-parens-rec`) reproduced
  exactly by isolated witnesses; 13 of 17 REQUIRES tokens SATISFIED
  (backrefs, lookaround, possessive-quantifier, atomic-group, recursion,
  conditionals, k-reset, named-groups, free-spacing, span-reporting,
  non-utf8-subject, captures, true-end-anchor), 4 NOT (lookbehind-
  variable, control-verbs, unicode-properties, callouts) — including the
  census's own "wrong first-cut" catch: `\p{Alpha}` compiles but `\p{L}`
  (a real Unicode category, the shape every PCRE corpus pattern actually
  uses) does not under `ONIG_ENCODING_ASCII`, so `unicode-properties` is
  declared UNSATISFIED despite the OP2 flag being present — and a
  documented spelling-only gap (PCRE's `(?R)` fails; `(?1)`/`(?&name)`/
  `(?0)`/`\g<n>` all work) that does not change the `recursion`
  declaration.
- `probe_vectorscan_capability_census.py` — ([B7]/L6b wave 2, lane
  l6bvs, 2026-09-17) the VECTORSCAN ADAPTER'S capability witness
  census, mandatory before `bench/capability/gen_patterns.py`'s
  `EXT_BENCH_ROSTER` declares anything for `vectorscan-block-nosom`:
  pass 1 runs one isolated witness per compile-time `REQUIRES_VOCAB`
  token through the real adapter (`span-reporting`/`captures` are
  stated as execution-model facts, not witnessed); pass 2 runs all 64
  real `bench/capability` corpus patterns through the same adapter,
  cross-referenced against each pattern's own `requires-*` tags. Runs
  from the repo root; needs the `vectorscan` adapter (built on demand,
  needs `libvectorscan-dev`).
- `probe_rust_capability_census.py` — ([B7]/L6b, lane `l6brust`/
  `l6brustfin`, 2026-09-19) the rust-regex ADAPTER'S capability witness
  census, mandatory before `bench/capability/gen_patterns.py`'s
  `EXT_BENCH_ROSTER` declares anything for `rust-default`. Same shape as
  the other three L6b censuses (one witness per `REQUIRES_VOCAB` token,
  all 64 `bench/capability` + 95 `bench/syntax` corpus patterns through
  the real adapter) plus a fourth pass this lane's own reasoning
  motivated: `census_nonutf8_discrimination()`, a real MATCH (not
  compile-only) run of two candidate high-byte patterns against a
  raw-byte subject and a UTF-8-encoded-codepoint subject, to settle
  whether `regex::bytes`'s default `unicode(true)` mode makes
  `\xHH`/`[\x80-\xff]` match a raw byte or that byte's UTF-8 ENCODING —
  an open question no prior L6b census needed to ask (RE2/Oniguruma both
  have an unconditional byte-vs-Unicode encoding SWITCH; the `regex`
  crate's is scoped per-expression via `(?-u:...)`, coexisting with
  `\p{L}` elsewhere in the same pattern, which the two probed spellings
  test for). RUN 2026-09-19 (lane `l6brustfin`, the detached
  post-battery pipeline, pcrec's I-75 battery having held the box for
  `l6brust`'s whole session) — see
  `2026-09-19-rust-capability-census-r1131.txt` below.
- `2026-09-19-rust-capability-census-r1131.txt` — its archive (regex
  1.13.1, rustc 1.98.1): 8 of 17 REQUIRES tokens SATISFIED
  (`unicode-properties`, `named-groups`, `free-spacing`,
  `span-reporting`, `non-utf8-subject`, `captures`, `true-end-anchor`,
  plus the 9 syntax refusals below); `possessive-quantifier` COMPILES
  but is WITHHELD on a real match-grain finding this file appends after
  the verbatim block: `(?:a++)a` MATCHES "aaa" at `[0,3)` end to end,
  which true PCRE possessive semantics would refuse (no backtracking
  left for the trailing `a`) — the crate's automaton has no backtracking
  to prevent, so the syntax parses for PCRE-pattern portability with no
  operational effect; 9 REFUSED (`backrefs`, `lookaround`,
  `lookbehind-variable`, `atomic-group`, `recursion`, `conditionals`,
  `k-reset`, `control-verbs`, `callouts`, all `[syntax/Syntax]`). The
  `non-utf8-subject`-DISCRIMINATION pass resolves the open question
  live: under `rust-default`'s actual (unmodified) unicode-mode-ON
  config, `[\x80-\xff]` matches the UTF-8 ENCODING of a codepoint, NOT a
  raw byte (nomatch against the raw byte, match against its two-byte
  UTF-8 form); only `(?-u:...)`-wrapped does raw-byte matching — kept
  SATISFIED at the structural API level (the driver never refuses/panics
  on a non-UTF-8 subject: the raw-byte case above answers a clean
  `nomatch`, not an error), with the semantic caveat documented
  prominently in `testees/rust/CLAUDE.md` so a future `high-byte-run`
  outlier under this config is read correctly. Also appends: the
  `foo|foobar` vs "foobar" witness confirming `perl-leftmost-first`
  (`[0,3)`, matching `MatchKind::LeftmostFirst` hardcoded in the pinned
  crate's own `Builder::build_one_bytes()`), and `size_limit`/
  `dfa_size_limit`'s 10 MiB/2 MiB defaults confirmed against
  regex-1.13.1's actual source (`nfa_size_limit`/`hybrid_cache_capacity`
  in `builders.rs`), not memory. Corpus totals: `bench/capability`
  42/64 compiled (every one of the 22 refusals ties to a withheld token
  by name except `mojibake-curly-quote`, the documented I-72
  pattern-source-UTF-8 exception under a satisfied token — the same
  "documented, not a surprise" shape the other three L6b censuses set);
  `bench/syntax` 50/95 compiled (45 `Syntax` refusals, unexamined against
  a per-token gate since `bench/syntax` is not capability-gated).
- `2026-09-17-vectorscan-capability-witness-census-5.4.11.txt` — its
  archive: 5 of 17 REQUIRES tokens SATISFIED (the narrowest on the
  roster) — `unicode-properties`, `named-groups`, `free-spacing`,
  `non-utf8-subject`, `true-end-anchor`; 12 NOT, each witnessed live
  with Vectorscan's own diagnostic text (backrefs, lookaround incl.
  lookbehind-variable, possessive-quantifier, atomic-group, recursion,
  conditionals, k-reset, control-verbs, callouts, span-reporting,
  captures). 40/64 corpus patterns compile. Carries an A/B COMPARISON
  that DECIDED the driver's compile flags: `HS_FLAG_UCP` was tried
  first and REJECTED — it broke `\b` compiling under UCP mode on 5 real
  corpus patterns carrying no unicode-properties requirement at all
  (35/64 compiled), for zero gain (`\p{L}` compiles identically with or
  without the flag); the shipped driver uses `VS_DRIVER_FLAGS = 0`.
  `unicode-properties` is the OPPOSITE finding from Oniguruma's own
  census (`testees/onig/CLAUDE.md`'s "wrong first-cut" catch): here
  `\p{L}` (a real Unicode category) compiles and `\p{Alpha}` (POSIX
  ctype name) does not — the reverse of onig's ASCII-encoding
  narrowing.

- `2026-09-18-predicate-audit-probes.txt` + `…-probe1.py` …
  `…-probe7.py` — THE PREDICATE AUDIT's seven probes (`[B42]` tail
  charter (i), lane `b50predaudit`; the derivation is
  `../../design/predicate_audit_v1.md`). Read-only, store-light (only
  probe 5 opens `store/index.tsv`, as `interpret` itself does), and
  every probe imports `pcrecbench.interpret`'s OWN functions
  (`parse_selector`, `_select`, `_sections_for`, `_keyed_values`,
  `_reduce`, `_op_holds`, `_measured_text`, `_elsewhere`,
  `r_arm_1`, `r_bucket_dominated`, `evaluate_predictions`, …) rather
  than reimplementing a predicate it is auditing. What they establish,
  over the 45 committed set-grain report TSVs + 3 `.subject-grain.tsv`
  slices + 2 predictions files: the (section × column × metric) census
  that every "can the counterevidence appear here?" answer rests on
  (`rank` 103,488 rows with ZERO `n_wrong>0`/`n_gave_up>0`, against 211
  of `excluded`'s 229; `not_ranked` and `scratch` EMPTY corpus-wide;
  each section's always-empty columns); that a `rank` cell is exactly
  SIX metric rows (17,248 cells, no exceptions) — the ×6 inflation
  behind "over N value(s)" and ruling (α)'s 100-158:1 dilution; the
  per-clause population of all 50 committed prediction clauses; 532
  arm pairs one config token apart with a REFUSED arm (R-ARM-1 cannot
  see them) and 38 cross-pin pairs with an unranked side; the two
  reports whose `floor_pattern` is `none`; and the four Δ rows whose
  partner R-BUCKET-SPAN cannot reach. Probe 6 adds the THIRD predictions
  file (`capability-0.1-ext-roster.tsv`, merged mid-lane): seven of its
  eleven failure-quantity clauses are evaluable ONLY under ruling (α),
  and `subject_or_na=(set)` is measured as the one (undocumented) way to
  keep the P-2 detail rows out of an explicit `section=excluded` read.
  Probe 7 measures the R-STATUS-4 consequence of `render_tsv` emitting
  the `did_not_compile` section only INSIDE a ranking group (lane
  `b51preds`' finding 2, re-asked as a rule-population question): **29**
  (report, pattern) pairs whose every compile cell is a refusal and which
  carry NO `did_not_compile` row anywhere — incl. `bench/bounded`'s own
  65535-cap refusal in a report R-STATUS-4 would call clean.
  Reproduce with
  `PCRECBENCH_ROOT=<checkout> python3 <probe>` (seconds each).
- `probe_rust_policy_vs_census_diff.py` / `2026-09-19-rust-policy-vs-census-diff.txt`
  — ([B58], lane `b58census`) the OWED reconciliation of the 2026-09-19
  rust-first report's two 22-item counts (`reports/CLAUDE.md`): the
  pre-compile capability policy's 22 `unsup` patterns vs the r1131
  census's raw 22 refused patterns. Read-only over the real
  `pcrecbench.subbench`/`pcrecbench.capability` functions (never a
  re-typed REQUIRES_VOCAB or roster copy) plus one live re-compile of
  the single pattern the derivation flags. FINDING: the two sets share
  21 members and disagree on exactly one each — `balanced-parens-rec`
  (`unsup`, but genuinely COMPILES: `(?R)` is a real rust-regex CRLF-mode
  flag, not rejected syntax, and is shown NOT to implement recursion —
  matched against `(a(b)c)` it returns the inner pair `[2,5)`, not the
  real-recursion span `[0,7)`) and `mojibake-curly-quote` (the report's
  own `refused` row, not a disagreement). SIDE FINDING: `bench/
  capability/subbench.toml`'s `[[patterns]]` array is stale relative to
  `patterns.rxt` (predates the b46tags REQUIRES-tag correction wave,
  missing `requires-backrefs` on `tag-depth3-bound` and five other
  tokens) but harmless at runtime since `rxt_source = "patterns.rxt"`
  makes `subbench.py` ignore that array outright — a trap for a human
  reader of `subbench.toml` directly, not a harness bug.
- `probe_o38_movertime_emit_diff.py` /
  `2026-09-20-o38-movertime-emit-diff-cf0962e3-vs-25b1984f.txt` — ([B62],
  lane `b62witness`, inbox I-79) STEP 1 of the witness for O-38's one
  isolated `vm-in` time mover (`wild-datetime-moment-iso8601`,
  +509.14 ns / x1.08, b60pinconfirm_report.md Section 3): re-emits the
  pattern at both pinned binaries already on this box (build/pcrec-
  cf0962e3, build/pcrec-25b1984f) under `pcrec-vm-in`'s real build flags,
  the pattern text checked against the store record's own
  `canonical_sha256` first. THE FLAG STORY, checked live: `-fcomments`
  is a 25b1984f/abi-27 axis that does not exist at cf0962e3 at all
  (live-verified refusal); cf0962e3 emits full comments
  UNCONDITIONALLY, matching what `EMIT_COMMENTS_FLAG` restores at
  25b1984f — so the comparison that matches the two real
  record-producing execs is cf0962e3's only mode vs. 25b1984f WITH
  `-fcomments`. FINDING: byte-identical MODULO the abi stamp line(s)
  (the provenance comment and the `.abi=` field) — checked structurally,
  not by eyeballing — exonerating the emitted program by construction.
  `emit_size()`'s comment-excluded totals (33,723/32,799) agree across
  all three emissions (both pins, both comment-flag states).
- `probe_o38_movertime_step23_prep.py` — ([B62]) STEPS 2-3 HARNESS PREP,
  NOT the timed measurement (blocked on the manager confirming the box
  is clear of lane b61matrix's renders — ambiguous from this lane's own
  checks). Reuses the REAL harness code path
  (`pcrecbench.harness.run_cell`, `testees.pcrec.adapter.Adapter`) by
  injecting two synthetic, in-memory-only `local: True` (scratch-tier-
  by-construction) testee entries pointed at the two pinned binaries via
  `$PCREC_BIN_*`, with `pcrec-vm-in`'s own buffer capacities, and
  monkeypatching `pcrecbench.adapters.discover` so the injection
  persists — since `pcrec-vm-in` is a PINNED testee (one committed pin)
  this is the only way to reach the historical cf0962e3 binary through
  the current code path at all. `--smoke` proven end to end (both pins
  compile, build and run through the real code path). Also builds and
  `gcc -fsyntax-only`-checks a SCRATCH-ONLY patched copy of
  testees/pcrec/driver.c (two `fprintf` lines after the `alloc_region()`
  calls, printing each caller-provided buffer's pointer and `% 64`) for
  step 3's placement question — the real driver.c is never touched. A
  companion static finding (in the lane report, not a separate archive):
  `git log` shows testees/pcrec/shim.c and driver.c last changed
  2026-09-16, BEFORE the cf0962e3 window even ran, and the one
  intervening adapter.py change ([B58]) touches only the phase-1 argv —
  so there is no "wrapper era" to literally cross, only a same-session
  reproduction question left to answer once the box clears. See
  `docs/dev/lanes/b62witness_report.md`.
- `probe_o38_movertime_step23_run.py` / `2026-09-21-o38-movertime-step23-interleave-buffer-placement.txt`
  — ([B62], lane `b62run`) STEPS 2-3, THE REAL RUN. Reuses the prep
  script's synthetic-testee-injection technique but bypasses
  `pcrecbench.harness.run_cell` (which would average trials into a
  set-grain median and drop the raw per-trial buffer placement):
  calls `testees.pcrec.adapter.Adapter.compile()` directly once per pin
  to get a `handle`, swaps `handle["driver"]` for the scratch-patched
  driver, calibrates through the REAL `pcrecbench.harness.calibrate()`,
  then runs 12 TRIAL-INTERLEAVED (cf0962e3, 25b1984f, cf0962e3, ...)
  driver launches per pin directly via `driverrun.run_driver()`,
  pairing each trial's SUM-over-75-subjects `ns/call` (the same
  quantity `pcrecbench.reduce`'s set-grain sum computes, since `iters`
  is constant within one trial) with that SAME trial's two buffer
  addresses' `% 64` from its own stderr. FINDING 1 (the decision rule,
  branch A): the historical x1.08 does NOT reproduce same-session —
  cf0962e3 median 6,303.58 ns/call vs 25b1984f's 6,304.74 ns/call
  (0.02% apart; 0.05% excluding one named outlier), well inside
  report.py's own R8 `unchanged (within spread)` rule — so nothing is
  filed as a pcrec item, per the agreed rule. FINDING 2 (unplanned,
  STEP 3's own instrument): `frames_addr % 64` and `trail_addr % 64`
  read EXACTLY 16 on all 24 independent process launches, both regions,
  both pins — the buffer's cache-line offset is DETERMINISTIC on this
  box for this allocation shape, even though ASLR visibly randomizes
  the addresses' higher bits. This is the opposite of I-79 (ii).3's own
  working assumption (that ASLR varies cache-line placement launch to
  launch) and independently supports branch A: there is no varying
  placement mechanism here that two separate sessions could have
  crossed differently. One outlier (cf0962e3 trial 4, 17,552.56 ns/call
  vs a ~6,300 ns baseline) is named and shown not to move the median or
  the verdict.
- `probe_altwide_rung_attribution.py` /
  `2026-09-21-altwide-rung-attribution-25b1984f.txt` — ([B65], lane
  `b65attrib`, inbox I-80) THE RUNG ATTRIBUTION for [B63]'s altwide
  DFA/auto refusal-boundary move (18 → 4 refusals, d34c9131 → 25b1984f;
  `docs/dev/lanes/b63window_report.md` §3): re-emits each of the 14
  newly-compiling patterns, both forms, through the pinned 25b1984f
  binary under `pcrec-auto`'s real phase-1 argv (the [B58] `-fcomments`
  token included), capturing every `pcrec: note:` line VERBATIM and
  classifying it against the two known drop-ladder rung texts (K53
  rung 1: drops the optional anchored match-here machine; K59 rung 2:
  additionally drops the premultiplied DFA table — I-80's own
  ordering), plus the RX_ENGINE_SEL/RX_DFA_TABLE/RX_DFA_MATCH/
  RX_DFA_PREFILTER stamps and the d34c9131 refusal's own verbatim
  diagnostic. FINDING: this project's OWN committed hypothesis
  (reports/CLAUDE.md, outbox O-40 — "cf0962e3's K59 premul drop-ladder
  rung" as THE mechanism) was **rung-2-only and wrong**: of the 14
  patterns' 28 (pattern, form) cells, 4 fit under the cap with NO rung
  at all (both forms of ci-256/cnt-64/srt-256/w-256's PLAIN forms — the
  cells that were never refused), 15 fire rung 1 ONLY, and 9 fire BOTH
  rungs — rung 1 (K53) is the one that fires on literally every
  cap-bound cell; rung 2 (K59) fires only where rung 1 alone still
  overflows. I-80's caution reproduced on its own witness pattern:
  `ci-512` plain reads `RX_DFA_TABLE "mixed"` under RUNG 1 ALONE (one
  note line), which `dfa_table=mixed` would misread as premul-rung
  evidence if read alone — every emit-byte figure MATCHES the store's
  own committed 25b1984f records byte-exactly (28/28 cells), so the
  reproduction is proven faithful, not merely plausible. Zero note
  lines matched neither known rung text (no STOP-and-flag rows). See
  `docs/dev/lanes/b65attrib_report.md` for the full per-pattern table
  and the reports/CLAUDE.md provenance correction this finding drove.

- `2026-09-22-b71-wrapfix-p1p2-scoring.py` / `.txt` — the [B71]
  capability wrapfix window's P1/P2 prediction scoring (plan.md's [B71]
  row is the pre-registration): the script joins each of the seven
  fresh 2026-09-22 records against that testee's newest prior record by
  (pattern, form) compile row and prints outcome and emit-byte deltas;
  the .txt is its verbatim output plus, in the header, the P3 timing
  method and totals (R8 spread rule over the two committed report
  TSVs). All three predictions CONFIRMED; the full reading is
  reports/CLAUDE.md's [B71] entry.

- `probe_kb27_no_expectation.py` / `2026-09-22-kb27-no-expectation-probe.txt`
  — (KB-27, docs/dev/known_issues.md, lane b75kb27) a READ of pinned
  records only (no compile, no run, no timing) over
  `store/records/capability@0.1/*/*.jsonl` for the two (pattern,
  subject) pairs the KB is about (`evil-alt-nested` x
  `rd-evil-alt-near-miss` / `sd-empty-alt-hit`, `short-subject-search`):
  prints every testee's newest record's RAW `match_outcome`/`diagnostic`
  for the pair, then runs the SAME rows through the OLD (pre-fix)
  `n_wrong` formula (reproduced literally, not imported, so the probe
  keeps demonstrating the contrast even after `reduce.py` changes again)
  and the current `pcrecbench.reduce.reduce_match_cell` side by side.
  The archive splits the 21-testee roster into three groups, unchanged
  by the fix except the third: 9 genuine give-ups and 3 `timed-out`
  reads (both unaffected either way), and 9 testees whose
  `did-not-match-as-expected` "no expectation exists" row moves from
  `n_wrong=5`/`wrong` to `n_no_expectation=5`/`no-expectation` on the
  IDENTICAL already-committed rows -- confirming no record's own raw
  fields ever changed, only the reduction reading them.
