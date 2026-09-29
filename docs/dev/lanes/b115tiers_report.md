# b115tiers report — [B115] FINDINGS-BENCH-TIERS scratch-tier tooling

Charter: inbox I-118 (`docs/dev/inbox_from_pcrec.md`), answered as outbox
O-72 (`docs/dev/outbox_to_pcrec.md`), plan row [B115] (`docs/dev/plan.md`).
Team-lead's task brief named the pcrec commit **f7f5a143** (post-[FINDINGS]
B6, abi 44) as unblocking the row. Everything below is SCRATCH TIER: no
`store/` write, no `configs.toml` change, no pinned testee added or moved.

## Charter-vs-committed checklist

| part | charter | committed artifact |
|---|---|---|
| (a) | build the named commit `pin.sh`-style; confirm `pcrec-analyze`, `--help` lists `--analysis`/`-I`/`--tune`; configs.toml/registries unchanged | `testees/pcrec/pin.sh f7f5a143` run under `gnutimeout 900`; built `build/pcrec-f7f5a143/build/{pcrec,pcrec-analyze}` (confirmed both exist and run: `pcrec --help` lists `--tune=N` and `--lib-path DIR, -I DIR`; `docs/spec/cli.md`/`findings.md` at this commit confirm `--analysis`/`--list-analysis`; `pcrec-analyze` produces bundles, `pcrec --list-analyses` lists `default`/`log`/`weblog`). `git diff` against HEAD shows `configs.toml`/`list_axes.tsv`/`list_definitions.tsv`/`list_limits.tsv`/`list_schema.tsv` untouched — **DONE** |
| (b) | `pcrec-local` id gains `tune-<n>`/`an-<name>` tokens; ids frozen elsewhere; FINDINGS stamp recorded and cross-checked | `testees/pcrec/adapter.py`: `effective_tune`/`effective_analysis`/`findings_stamp` + wiring into `config()`/`describe()`/`_emit_facts`/`METADATA_DECL`/`compose_config_extra`. `tools/selfcheck.py:check_b115_tune_analysis_axis` (3 arms, all green standalone — see "Validation" below) — **DONE** |
| (c) | `--seed S --out DIR` on the three generators; defaults byte-identical; TRAIN seed disjoint, recorded in NOTES.md | `bench/loglines/gen_subjects.py` (`TRAIN_SEED = 20260930`), `bench/loglines/gen_throughput_subjects.py` (`TRAIN_SEED = 20260931`), `bench/email/gen_throughput_subjects.py` (`TRAIN_SEED = 20261001`); defaults re-verified byte-identical against the committed manifests (`git diff --stat` empty after a bare re-run of all three); NOTES.md paragraphs in both sets — **DONE** |
| (d) | `testees/pcrec/findings/{loglines,email}/`: PROFILED bundle + `--list-analysis` for weblog/log/each bundle + disjointness manifest + CLAUDE.md; testees/pcrec/CLAUDE.md updated | Both directories committed with `.rxt` bundle, three/one archived `list_analysis_*.tsv`, `disjointness.tsv`, `README.md`, `CLAUDE.md`; `testees/pcrec/CLAUDE.md` gained a `## [B115]` section — **DONE** |
| (e) | `scripts/findings_tiers.sh` (the sweep) + a post-reduce ORACLE-BEST matrix script; `--dry-run` prints every arm's argv/testee_id | `scripts/findings_tiers.sh`, `scripts/findings_tiers_matrix.py`, both committed and documented in `scripts/CLAUDE.md` — **DONE** |
| (f) | smoke only (no timed sweep): 2-3 arm subset, matrix over it, then `make check-harness` | 3-arm loglines smoke (`default`/`declared-weblog`/`profiled`, `--trials 1 --iters 1 --force-unquiet`) into `/var/tmp/b115/smoke-store`, matrix run over it (22 rows, `ORACLE-BEST` correctly `n/a` + `excluded-from-min:30-arms` since the sweep arms were not run) — **DONE**. `make check-harness` launched under `gnutimeout 1800` in the background at commit time — see "OWED" below |

## Arm counts per set (confirmed via `--dry-run`)

| set | arms | shape |
|---|---|---|
| loglines | **34** | 1 default + 30 (3 engines × 5 tune positions × 2 caps arms, capture-free) + 2 declared + 1 profiled |
| email | **32** | 1 default + 30 (3 × 5 × 2, capture-free... **see finding below**) + 0 declared + 1 profiled |
| bounded (`--extended`) | 31 | 1 default + 30 (capture-free) |
| altwide (`--extended`) | 31 | 1 default + 30 (capture-free) |
| capability (`--extended`) | 16 | 1 default + 15 (3 × 5, NOT capture-free — no `-nocaps` twin) |
| syntax (`--extended`) | 16 | 1 default + 15 (3 × 5, NOT capture-free) |

**34 for loglines matches outbox O-72's own estimate ("about 34 cells")
exactly** — a good cross-check that the arm-generation logic matches what
was promised.

**A correction to my own arm design, found while writing this table**:
email's capture census (`viewer_export._pattern_capture_count` over
`bench/email/patterns/*.rx`) reads **1 of 3 patterns capture-bearing**
(`orig`/`factored` DO capture; `floor` does not) — so email is NOT
capture-free at the SET level, and `CAPTURE_FREE_SETS` in
`findings_tiers.sh` correctly excludes it from the `-nocaps` twin (32
arms, not 34+). This is by design and confirmed working, not a bug — flagged
here only because the table above needed the caveat spelled out rather
than asserting "capture-free (3×5×2)" for email by copy-paste.

## Estimated sweep duration per set, and its basis

**Important finding for the manager's scheduling decision.** No per-arm
timed number exists yet (only the `--trials 1 --iters 1` smoke was run,
which is NOT representative — the harness auto-calibrates each subject's
loop to a ~50 ms target, so a 5-trial cell costs far more than 5× a
1-iteration one). The basis below is `scripts/CLAUDE.md`'s own measured
per-CELL table for pcrec-family testees at 5 trials (same route family as
every `pcrec-local` arm here — auto/vm/dfa all compile a real pcrec
artifact and run the same calibrated loop):

| set | measured per-cell (pcrec, gcc, 5 trials) | arms | **estimated full sweep** |
|---|---|---|---|
| loglines@0.1 | 8.8 min (`vm-in`) – 10.6 min (`vm-clang`) | 34 | **~5.0–6.0 hours** |
| email-specimen@0.2 | 7.2–11.3 min | 32 | **~3.8–6.0 hours** |
| bounded@0.3 | **42.3–49.4 min** | 31 (`--extended`, engine×tune only) | **~21.8–25.5 hours** |
| altwide@0.1/0.2 | 5.0 min (`auto`) – 41.9 min (interp; pcrec route unmeasured at this extreme) | 31 | **~2.6+ hours, plausibly far more at wide rungs** |
| capability@0.1 | not in that table (a different set); no pcrec-family figure cited there | 16 | not estimated — no basis in hand |
| syntax@0.1 | not in that table | 16 | not estimated — no basis in hand |

**bounded's estimate is the one that matters most**: at ~45 min/cell × 31
arms, a full `--extended` engine×tune sweep on `bounded` alone is
**most of a day**, which is far past anything this project's `CELL_CAP`
default (5400 s = 1.5 h) tolerates per cell but well within it per
cell — the RISK is wall-clock budget for the whole sweep, not any single
cell timing out. **Recommendation**: run loglines + email first (the
charter's own primary target, ~9–12 h combined worst case, likely less
since `--tune=` and `--no-captures` are answer-preserving and should not
move compile time much beyond the plain `auto`/`vm`/`dfa` baseline this
table already has); treat `--extended` (bounded/altwide/capability/syntax)
as a SEPARATE, later window, and consider trimming the tune ladder (e.g.
just `{-2, 0, 2}` instead of all five positions) before running it, since
tune is documented as answer-identity-preserving and the ×5 factor is the
single biggest cost driver in every set's arm count.

## The adapter and abi 44 — what moved, and what did not

- **No new stamp reading was needed for abi 44 itself.** `f7f5a143` is
  three abi steps ahead of this project's pinned a32bc86e (41→44); this
  lane did not audit what those three steps stamp (out of scope — a
  re-pin question, not a scratch-tier one), and the shim/driver were not
  touched at all. `PB_SHIM_MIN_ABI` stays 16; a real compile at abi 44
  loaded and ran cleanly through the UNMODIFIED shim in every smoke and
  selfcheck run above (`abi: 44` observed directly in a written record's
  `engine_metadata`), which is the practical confirmation the floor rule
  predicts: abi rises without a shim edit are always safe to READ, never
  a compile-time requirement to widen anything.
- **`--tune`'s CLI grammar has one asymmetry worth flagging**: `--tune=N`
  is the ONLY accepted form (`--tune -1` with a space is refused by pcrec
  itself, "takes its value with '='"), where `--analysis` accepts BOTH
  `--analysis NAME` and `--analysis=NAME`. `effective_tune`/
  `effective_analysis` reflect this correctly (confirmed live against the
  f7f5a143 binary before either function was written), but a future
  reader changing one to "look like" the other would silently break the
  identity claim `--tune` makes — noted in `adapter.py`'s own comment,
  repeated here because it is the one surprise in an otherwise
  symmetrical-looking pair of functions.
- **`RX_FINDINGS` is read from emitted TEXT, not through `shim.c`.**
  [B108]'s own note (the abi-40 arrival) already found no shim getter
  reads `rx_info.findings` (D77's precedent: no run-time consumer). Rather
  than add one for [B115] (a live ABI edit, non-trivial risk for a
  scratch-tier lane), `findings_stamp()` greps the emitted `.c`/`.h` for
  the `#define <PREFIX>_FINDINGS "..."` line — the SAME shape
  `scan_edge_counts()` already uses for a different macro, and safe
  because the value is a static string fixed at emit time (never a
  runtime fact `rx_info.findings` would be needed for). Confirmed correct
  against `--list-analysis`'s own printed digest on two real compiles
  (weblog, loglines-profiled) — see "Validation".

## Surprises

1. **loglines's arm count (34) landed EXACTLY on O-72's own estimate.**
   Worth stating plainly since it is easy for an estimate and an
   implementation to drift apart without anyone noticing until a report
   reads oddly; here they agree to the cell.
2. **email is not capture-free at the set level** (see the arm-count
   table's correction above) — `--no-captures` is correctly withheld from
   every email arm by the same `CAPTURE_FREE_SETS` check that includes
   loglines/bounded/altwide, and this was confirmed by an actual capture
   census over the patterns (`viewer_export._pattern_capture_count`),
   not asserted from memory of the charter's prose alone.
3. **`bounded`'s per-cell cost (42–49 minutes) makes its `--extended`
   engine×tune sweep almost a full day of wall clock**, which the charter
   did not flag and which changes the shape of "run this tonight" if the
   manager intends to include `--extended` sets in the first window.
4. **PCREC_MAX_FIND_BUNDLE_BYTES (1 MiB) is a `-I` FILE size cap, not a
   corpus cap** — the loglines TRAIN corpus fed to `pcrec-analyze` is
   4.3 MB and compiled fine; only the resulting `.rxt` BUNDLE (2.3 KB)
   is subject to the 1 MiB limit. Not a problem here, but worth recording
   since a much bigger TRAIN corpus (or a `bigram` scan, once B4 lands)
   could plausibly approach it.
5. **The `weblog`/`log` bundles both declare `serves byte-rate when
   byte,utf8`** even though they were scanned with plain `--scan freq`
   (no `cpfreq`), because their corpora are ASCII-only — matches the
   design note's own "on an ASCII-only sample this is exactly the freq
   view" rule, confirmed by building `loglines-profiled` the same way
   (`--scan freq` alone) and finding it ALSO auto-declares `utf8`
   coverage. Harmless for `bench/loglines` (byte-mode only), but a future
   reader should not read that `serves ... utf8` line as evidence the
   bundle was scanned for genuine multi-byte content — it was not.

## Validation run standalone (before the full suite)

```
$ python3 -c "... selfcheck.check_b115_tune_analysis_axis() ..."
-- the tune dial + the findings analysis ([B115], --tune= / --analysis) --
   PASS  b115 axis: effective_tune/effective_analysis recognise every spelling ...
   PASS  b115 axis: every PINNED pcrec config's tune_extra/analysis_extra read None ... 30 configs
   PASS  b115 axis: pcrec-local --analysis weblog stamps FINDINGS naming weblog ...
        findings='byte-rate=weblog:6b85ed6b33993164', digest 6b85ed6b33993164 matches --list-analysis weblog,
        testee_id='pcrec_local-1f730a57146a_auto-caps-simdna_an-weblog'
```

Generator defaults re-verified byte-identical (`git diff --stat` empty
after a bare re-run of all three generators with no arguments). The
3-arm smoke (part f) is reproduced in full in this lane's commit history
(`/tmp/b115_check_harness.log`-shaped output was not committed — it is a
scratch log by design, per this project's own "session-temporary files
go in the session scratchpad" mandate).

## OWED

**`make check-harness` (the full ~324+ check suite, ~20 min).** Launched
in the background at commit time:

```
cwd:     /home/duxevents/pcrec-bench/worktrees/b115tiers
command: gnutimeout 1800 make check-harness
log:     /tmp/b115_check_harness.log
marker:  the log's own final line, "DONE rc=<N>" (appended unconditionally
         by the launching command, so its absence means still-running,
         never a silent failure)
```

If this report is read before that marker line exists, the numbers this
section would otherwise carry (pass/fail counts, whether
`check_b115_tune_analysis_axis` survives inside the full run the way it
did standalone, and whether ANY pre-existing check regressed) are OWED —
re-run `tail -40 /tmp/b115_check_harness.log` to check, or re-launch the
same command if the log is gone (a `/tmp` path, not durable across a
reboot).

**The timed sweep itself is OWED to the manager**, per this lane's brief
("DO NOT run the timed sweep; the manager launches it"). Exact commands:

```
# loglines, full 34-arm sweep, real trials
scripts/findings_tiers.sh
python3 scripts/findings_tiers_matrix.py --store /var/tmp/b115/store --set loglines --out /tmp/loglines_matrix.tsv

# email, full 32-arm sweep (loglines already swept if run together)
SETS="email" scripts/findings_tiers.sh
python3 scripts/findings_tiers_matrix.py --store /var/tmp/b115/store --set email --out /tmp/email_matrix.tsv

# the four --extended sets, LATER window (see the duration table above)
SETS="bounded altwide capability syntax" scripts/findings_tiers.sh --extended
```

Launch under `setsid ... &` (multi-hour run, same as any `run_window.sh`
window); the script's own `FINDINGS_TIERS_COMPLETE cells=W/N` line in its
log is the completion marker, matching `run_window.sh`'s own convention.

No `store/` or `reports/` write anywhere in this lane, confirmed
(`git status` inside `store/`/`reports/` is clean; every write in this
lane's own testing went to `/var/tmp/b115/` or `build/scratch-store/`,
both outside the repository).
