# bench/unusual/ -- the UNUSUAL-FEATURES set (unusual@0.1, [B148], lane b148l3)

Realistic patterns whose feature is outside the common regex subset: recursion,
callouts, caller variables. Design: `docs/design/unusual_set_v1.md` v0.2. THIS
directory is the L3 skeleton: patterns, subjects, oracle, expectations. Nothing is
timed here; the drivers' `--mode calls` and the `deep` arms are L4's (landed, below), callees (L5, landed, below), vars value streams (L7) and gates (L8) are other
lanes. Read `NOTES.md` first (members, subjects, expectation methods, the declarations
made before any run, dependencies).

## Files

- `subbench.toml` -- GENERATED sidecar (`gen_patterns.py`); regimes `search_short`,
  `throughput` and (since L4) `call-stream` -- the two F1 streams (seg-s, seg-l) replayed per
  call, a cell only for the patterns with a stream expectation (cscan, cscan-onig;
  `Subbench.applies`). Tags (b148land): vars members carry `requires-vars` + `requires-unusual-<member>`; callout arms carry `twin_of-<root>`; the generic gates `rxt-export`, `capability-policy-noop`, `vars-surface` skip this set via `UNUSUAL_GATE_SKIPS` (tools/selfcheck.py).
- `members.py` -- THE member table (pattern bytes, family, provenance, oracle route);
  `gen_patterns.py` writes `patterns/*.rx`, `provenance.tsv`, `patterns.rxt` (the
  `ext bench` capability matrix ONLY, copied from bench/capability, plus -- L4 `DEEP_ARMS` -- a
  row for each `deep` limits arm copying its default sibling's block), `subbench.toml`.
- `unusual_lib.py` -- splitmix64 `Rng`; `ref_scan` (the regex-free cscan reference
  scanner); host references (S-expression, JSON, Luhn, ISBN-13, member, netstring);
  `Rx`, the libpcre2 oracle with an optional Python callout function.
- `unusual_text.py` -- the deterministic text generators (C bodies, F3 pathologicals,
  S-expression / JSON / callout / netstring corpora). `subjgen.py` -- the shared
  write/--check routine.
- `gen_subjects.py` (161 short subjects, `manifest.tsv`), `gen_throughput_subjects.py`
  (30 large subjects, `manifest_throughput.tsv`), `gen_streams.py` (the F1 call streams + the F2 sqlite ones,
  `manifest_streams.tsv`, `calls/`). Subject trees (`subjects/`, `throughput/`,
  `streams/`, `calls/`) are GENERATED and gitignored.
- `gen_expectations.py` -- `expectations.tsv`, `expectations_stream.tsv`, `applies.tsv`
  (which large subjects belong to which patterns). The full derivation takes MINUTES
  (libpcre2's interpreter is super-quadratic on deep brace nesting; NOTES.md section 3).
- `check_set.py` -- the set's own checks (`--full` re-derives all expectations).
- `fetch_sqlite.py`, `fetch_kernel.py` -- the F2 fetchers. `fetch_sqlite.py` is PINNED and RUN
  (SQLite 3.54.1, approved by Frank 2026-10-27): `vendor/sqlite3.c.xz` + `.sha256` + `SQLITE.md`.
  `fetch_kernel.py`: empty pin table, refuses by name until Frank approves each URL + sha256.
  The F2 SQLITE streams (`sqlite-bodies`, `-s`: locator in `gen_streams.py`, expectations in
  `expectations_stream.tsv`) are built (b148f2); `skipped_subjects.tsv` names the F2 KERNEL subjects skipped. `vendor/pcrec/` -- cscan.rxt +
  gen_cscan.py, byte-verbatim, MIT (PROVENANCE.md). `values/users.tsv` -- the
  co-member callee's runtime set.
- `provenance.tsv` -- the capability-set provenance columns for every pattern.
- `gen_vars.py` ([B148] L7) -- the caller-VARIABLES half: the Python resolver for vars.md 2/5
  (`parse`, `resolve`, `esc_pcre2`/`esc_py`), the five deterministic value streams (`STREAMS`:
  `tenant-d4/-d64/-d4096`, `route-zipf`, `term-zipf`), `Built` (subject, calls, bindings table,
  `facts()` = refused + distinct resolved). Imported by `gen_streams.py` (which writes the subjects,
  `calls/`, `values/<id>.tsv`, `values/streams.tsv` and the manifest rows) and `gen_expectations.py`
  (per-call expectations, libpcre2 vs Python `re`; `--streams-only` regenerates just
  `expectations_stream.tsv`). `values/<id>.tsv` is the bindings table (COMMITTED, hashed);
  `values/streams.tsv` the per-(stream, member) summary (calls, bindings, distinct values, distinct
  resolved = the miss count, refused, reuse). `gen_vars_samples.py` -- the PUBLIC 80-case sample
  (`assists/problems/vars-samples.tsv`) next to `assists/problems/vars.md`, the engine-neutral problem
  statement the L6 author lanes receive. NOTES.md section 8 states the call, the streams and D-5.

- `callees/` (L5) -- `callees.h`/`callees.c`: one shared C body per callee (luhn, isbn13,
  member, netstr (pcrec consume), netstr-end (the assisted check-at-end), stub), pure
  functions of an engine-neutral view; `-DUB_COUNT` builds the counting twin (fire log to
  `$UB_FIRE_LOG`). Built ONCE by `pcrecbench/callees.py`. `replay.c` -- the callee-cost
  microbench `tools/callout_calib.py` runs. The `[callouts]` table in the sidecar binds
  sites to callees per arm (real / pass); `-nofn` arms bind none.

Not here yet (other lanes): the authored `assists/<member>/<engine>/` (L6).

b148aw (lane b148aw): the assist pipeline -- `assists/templates/`, `assists/AUTHORS.md`, the
runner and the five `-assist-v01` configs (testees/assist/), `pcrecbench/assists.py` +
`assist-init`/`assist-selftest`, `tools/check_assist.py`. `members.py`/`gen_patterns.py`:
every member an assist can cover now declares `requires-unusual-<member>`; `ASSIST_ARMS` adds
the five assisted ids to the roster. The census shows 0 admission changes over the 15
existing configs -- docs/dev/lanes/b148aw_report.md.

L4 (lane b148l4): `--mode calls` in the pcre2/pcrec/onig/re2/rust/vectorscan-som drivers,
the `deep` arms (`pcre2-{interp,jit}-deep`, `pcrec-{auto,vm}-deep`, `onig-default-deep`,
`unusual_only`), limits read back on every compile row, the untimed 6.4 high-water pass on
every match row (`deep_mem_bytes`/`_method`/`deep_maxrss_kb`), give-ups named by limit, the
O(segment) pre-flight (every engine `native`), and the dry run whose durations set
`CELL_CAP_unusual` -- docs/dev/lanes/b148l4_report.md.

L7 (lane b148l7): the vars members' five value streams and per-call expectations, pcrec's NATIVE vars path
(`testees/pcrec`: the shim's `pb_vars_*` entries, `timed_calls_vars.c`, the driver's `run_calls_vars`;
`testees/common/vars_io.h`), the `vars` + `unusual-va-*` capability on the six native pcrec configs, the
public sample and problem statement for L6, `tools/check_vars.py` (in `check-harness`) --
docs/dev/lanes/b148l7_report.md.

L5 (lane b148l5): the callout arms -- `callees/`, the `-nofn` arms, the native wrappers
(pcre2, onig, pcrec), the fire pass, `tools/check_callouts.py`, the calibration
(`tools/callout_calib.py`) -- NOTES.md 6a, docs/dev/lanes/b148l5_report.md.
