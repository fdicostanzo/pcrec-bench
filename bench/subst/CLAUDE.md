# bench/subst/ — the SUBSTITUTION set (`subst@0.1`, plan row [B140])

WHAT IT IS FOR. Every other set times a MATCHER and compares ANSWERS (a
span, a count). This one times a TRANSFORM: a global substitution over a
few-hundred-MB Apache access log, whose answer is an OUTPUT BYTE STRING
gated by its sha256 against the libpcre2 oracle's. Built per
`docs/design/subst_bench_v1.md` v0.2 with Frank's §8a rulings (320 MB; the
generated subject CALIBRATED against a real log; case 5b e-mail masking;
case 7 `url-tld-fix`, the backreference-in-a-negative-lookahead shape).
**Read `NOTES.md` first** — the cases, the neutral-template IR, the stated
densities and predictions, the calibration outcome, the divergence table.

STATUS: step 1 of [B140] (the set) BUILT (lane b140set2, 2026-10-24): subjects generated and hashed (`manifest.tsv`), expectations derived for both subjects (22 rows), calibration archived with two STATED DEVIATIONS (NOTES.md).
STEP 3 (lane b140drv, 2026-10-25): the pcre2 LIBRARY-TIER driver mode, the
`timed_subst()` instrument, the harness side (`pcrecbench/substrun.py`) and a
scratch-tier dry run exist; `pcrecbench run --subbench subst` WORKS
(`subbench.py` builds the harness's "patterns" from `cases.tsv`: pattern id =
the case DIRECTORY name, the case id `5b` etc. is `Pattern.case`, the key of
`expectations.tsv` / `divergences.tsv` and the record's `subst.case`). The
sidecar is `subbench.toml` since [B143] (2026-10-25; it was staged as
`subst.toml`): `tools/selfcheck.py`'s generic `bench/*/` gates
(`subbench_dirs()`) now enumerate the set, and `SUBST_GATE_SKIPS` names the
four gates it skips (manifests, floor quick cell, floor oracle smoke, rxt
export) with the reason printed; every other gate applies. The reporter reads
it with `report --grain subst`. Its own
gate is `tools/check_subst.py` (called from `check-harness`). Subjects:
`$PCRECBENCH_SUBST_SUBJECTS` or `subjects/` (`<id>.log`); trial 1's output
files: `$PCRECBENCH_SUBST_OUT` or `build/subst-out/`. No timing run and no
store record exists for it.

| file | role |
|---|---|
| `NOTES.md` | the set's statement: cases, IR spec, densities + predictions (stated before any run), calibration, oracle, divergences, design gaps |
| `subbench.toml` | the sidecar (fields only; renamed from `subst.toml` at [B143]) |
| `cases.tsv` | the case table: id, dir, label, ERE-safe?, what the pattern needs, planted-or-natural, what it isolates |
| `cases/<dir>/PATTERN.rx` | the pattern text, ONE line, the same bytes for every engine (cases 1-6 are POSIX-ERE-clean: capturing groups only) |
| `cases/<dir>/TEMPLATE.neutral` | the engine-neutral template (IR: `lit`/`grp`/`upper`/`cond`/`else`/`end`), rendered per dialect by `pcrecbench/subst_template.py` |
| `logsim.py` | the access-log SIMULATOR: one deterministic infinite stream of interleaved sessions (browsers, crawlers, feed readers, drive-bys, heavy users) with the planted structures; `K` is its calibration knob table |
| `gen_subjects.py` | writes `subjects/acc-small.log` + `acc-main.log` (gitignored) from one stream, `manifest.tsv`, `planted.tsv`; `--check` reproduces them and runs the calibration when the reference is present |
| `manifest.tsv` | `id len sha256 description periodic` for the two subjects (the harness's five-column shape) |
| `planted.tsv` | per-subject oracle-INDEPENDENT planted counts (rare paths, e-mails, the case-7 URL populations) |
| `calibrate.py` | (STATED_DEVIATIONS: verdict DEVIATION) measures a generated window against the real Apache log: entropy, gzip/xz/zstd ratios, line lengths, field variety, status mix, each case's matches per line; stated tolerances; run with `python3 -I` |
| `fetch_reference.sh` | downloads the reference at the pinned commit and verifies BOTH its sha256 and its git blob hash, refusing on mismatch (never run by `make check`) |
| `gen_expectations.py` | `expectations.tsv` from the libpcre2 oracle (`Compiled.substitute`) with an independent count per row and case 7's composition control; `--check` re-derives acc-small |
| `expectations.tsv` | per (case, subject): nsubst, out_bytes, out_sha256 + the independent count |
| `divergences.tsv` | the declared per-(case, competitor) expectations: `agrees` / `unsupported:<token>`; basis `declared` (the oracle), `verified-small` (a tool run on acc-small by `check_subst.py`) or `predicted` (pcrec's cases 6 and 7 are `verified-small` since b140pcrec, 2026-10-25: sha256 equality on acc-small, four arms) |

`subjects/` (or `$PCRECBENCH_SUBST_SUBJECTS`, e.g. under /var/tmp/pcrecbench/) is GENERATED and gitignored (`bench/*/subjects/`). The real log
lives in `build/subst-ref/` (gitignored) and is never committed.

Engine-neutral (R-BENCH-4): no engine is named in a case, a subject or an
expectation. The calibration archive is
`docs/dev/measurements/2026-10-24-b140-subject-calibration/`.
