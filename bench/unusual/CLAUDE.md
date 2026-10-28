# bench/unusual/ -- the UNUSUAL-FEATURES set (unusual@0.1, [B148], lane b148l3)

Realistic patterns whose feature is outside the common regex subset: recursion,
callouts, caller variables. Design: `docs/design/unusual_set_v1.md` v0.2. THIS
directory is the L3 skeleton: patterns, subjects, oracle, expectations. Nothing is
timed here; the drivers' `--mode calls` and the `deep` arms are L4's (landed, below), callees (L5), vars value streams (L7) and gates (L8) are other
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

Not here yet (other lanes): `assists/` (L2/L6), `callees/` (L5), `expectations` for the
vars members (L7).

L4 (lane b148l4): `--mode calls` in the pcre2/pcrec/onig/re2/rust/vectorscan-som drivers,
the `deep` arms (`pcre2-{interp,jit}-deep`, `pcrec-{auto,vm}-deep`, `onig-default-deep`,
`unusual_only`), limits read back on every compile row, the untimed 6.4 high-water pass on
every match row (`deep_mem_bytes`/`_method`/`deep_maxrss_kb`), give-ups named by limit, the
O(segment) pre-flight (every engine `native`), and the dry run whose durations set
`CELL_CAP_unusual` -- docs/dev/lanes/b148l4_report.md.
