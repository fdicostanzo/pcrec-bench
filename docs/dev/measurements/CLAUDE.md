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
| `probe_trial_agreement.py` | ([B20], schema v1.4 `docs/design/gate_shape_v14.md` §3) the TRIAL-AGREEMENT CENSUS: reads PINNED RECORDS only (default: every `store/records/*/*/*.jsonl`); per timed row ((pattern, regime, form, subject), `iterations > 1`, ≥ 2 timed trials) the per-trial ns/iter and the median; for k in 1.25 / 1.5 / 2.0 the trials STRICTLY ABOVE k × median (slow outliers), whether the min is BELOW median / k (a fast outlier), and the row's DISAGREEING verdict (≥ 2 slow OR fast — the v1.4 rule's row test); per record the counts and fractions, every disagreeing row in full at k = 1.25 and 1.5, the worst row, the slowest-trial index histogram; a summary over all records per k with the worst five. Runs from the repo root with no arguments |
| `2026-08-30-trial-agreement-census.txt` | its archive over the WHOLE canonical store at bench 4f2f210 — 68 records (schema 1.1 × 11, 1.2 × 3, 1.3 × 54; 59 measured + 9 inconclusive-load; five pcrec pins + libpcre2 10.46), 62,923 rows, every one with 5 trials: at k = 1.5 ZERO rows with two slow trials and ONE fast-outlier row (a 3-2 split at the timer floor), worst record 0.204 %; at k = 2.0 nothing; at k = 1.25 21 slow-pair rows and 37 fast-outlier rows over 20 records, the `loaded` email@0.2 interp record worst at 1.996 %; the slowest trial is t1 in 36 of 387 single-slow rows (the least frequent index). The constants k = 1.5 / F = 1 % of the v1.4 rule are read from this file |

Maintenance: update this file when files are added/removed or change role.
