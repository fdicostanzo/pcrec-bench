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

STATUS: step 1 of [B140] (the set). NOT yet a harness sub-bench: the
sidecar is `subst.toml`, not `subbench.toml`, so `tools/selfcheck.py`'s
generic `bench/*/` gates (`subbench_dirs()`) do not enumerate it until
schema v1.9 (regime `substitution`), the driver `--mode subst` and the
TOOLS runner land; renaming the sidecar is the integration step. Its own
gate is `tools/check_subst.py` (called from `check-harness`). No driver,
no timing, no store record exists for it.

| file | role |
|---|---|
| `NOTES.md` | the set's statement: cases, IR spec, densities + predictions (stated before any run), calibration, oracle, divergences, design gaps |
| `subst.toml` | the sidecar (fields only) |
| `cases.tsv` | the case table: id, dir, label, ERE-safe?, what the pattern needs, planted-or-natural, what it isolates |
| `cases/<dir>/PATTERN.rx` | the pattern text, ONE line, the same bytes for every engine (cases 1-6 are POSIX-ERE-clean: capturing groups only) |
| `cases/<dir>/TEMPLATE.neutral` | the engine-neutral template (IR: `lit`/`grp`/`upper`/`cond`/`else`/`end`), rendered per dialect by `pcrecbench/subst_template.py` |
| `logsim.py` | the access-log SIMULATOR: one deterministic infinite stream of interleaved sessions (browsers, crawlers, feed readers, drive-bys, heavy users) with the planted structures; `K` is its calibration knob table |
| `gen_subjects.py` | writes `subjects/acc-small.log` + `acc-main.log` (gitignored) from one stream, `manifest.tsv`, `planted.tsv`; `--check` reproduces them and runs the calibration when the reference is present |
| `manifest.tsv` | `id len sha256 description periodic` for the two subjects (the harness's five-column shape) |
| `planted.tsv` | per-subject oracle-INDEPENDENT planted counts (rare paths, e-mails, the four case-7 URL populations) |
| `calibrate.py` | measures a generated window against the real Apache log: entropy, gzip/xz/zstd ratios, line lengths, field variety, status mix, each case's matches per line; stated tolerances; run with `python3 -I` |
| `fetch_reference.sh` | downloads the reference at the pinned commit and verifies BOTH its sha256 and its git blob hash, refusing on mismatch (never run by `make check`) |
| `gen_expectations.py` | `expectations.tsv` from the libpcre2 oracle (`Compiled.substitute`) with an independent count per row and case 7's composition control; `--check` re-derives acc-small |
| `expectations.tsv` | per (case, subject): nsubst, out_bytes, out_sha256 + the independent count |
| `divergences.tsv` | the declared per-(case, competitor) expectations: `agrees` / `unsupported:<token>` / `pending`; basis `declared` (the oracle), `verified-small` (a tool run on acc-small by `check_subst.py`) or `predicted` |

`subjects/` is GENERATED and gitignored (`bench/*/subjects/`). The real log
lives in `build/subst-ref/` (gitignored) and is never committed.

Engine-neutral (R-BENCH-4): no engine is named in a case, a subject or an
expectation. The calibration archive is
`docs/dev/measurements/2026-10-24-b140-subject-calibration/`.
