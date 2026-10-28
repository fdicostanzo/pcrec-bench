# bench/unusual/ -- the UNUSUAL-FEATURES set (unusual@0.1, [B148], lane b148l3)

Realistic patterns whose feature is outside the common regex subset: recursion,
callouts, caller variables. Design: `docs/design/unusual_set_v1.md` v0.2. THIS
directory is the L3 skeleton: patterns, subjects, oracle, expectations. Nothing is
timed; the drivers (L4), callees (L5), vars value streams (L7) and gates (L8) are other
lanes. Read `NOTES.md` first (members, subjects, expectation methods, the declarations
made before any run, dependencies).

## Files

- `subbench.toml` -- GENERATED sidecar (`gen_patterns.py`); regimes `search_short` +
  `throughput` only (the `call-stream` regime is declarable since L1 but not yet declared: L4). Tags (b148land): vars members carry `requires-vars` + `requires-unusual-<member>`; callout arms carry `twin_of-<root>`; the generic gates `rxt-export`, `capability-policy-noop`, `vars-surface` skip this set via `UNUSUAL_GATE_SKIPS` (tools/selfcheck.py).
- `members.py` -- THE member table (pattern bytes, family, provenance, oracle route);
  `gen_patterns.py` writes `patterns/*.rx`, `provenance.tsv`, `patterns.rxt` (the
  `ext bench` capability matrix ONLY, copied from bench/capability), `subbench.toml`.
- `unusual_lib.py` -- splitmix64 `Rng`; `ref_scan` (the regex-free cscan reference
  scanner); host references (S-expression, JSON, Luhn, ISBN-13, member, netstring);
  `Rx`, the libpcre2 oracle with an optional Python callout function.
- `unusual_text.py` -- the deterministic text generators (C bodies, F3 pathologicals,
  S-expression / JSON / callout / netstring corpora). `subjgen.py` -- the shared
  write/--check routine.
- `gen_subjects.py` (161 short subjects, `manifest.tsv`), `gen_throughput_subjects.py`
  (30 large subjects, `manifest_throughput.tsv`), `gen_streams.py` (the F1 call streams,
  `manifest_streams.tsv`, `calls/`). Subject trees (`subjects/`, `throughput/`,
  `streams/`, `calls/`) are GENERATED and gitignored.
- `gen_expectations.py` -- `expectations.tsv`, `expectations_stream.tsv`, `applies.tsv`
  (which large subjects belong to which patterns). The full derivation takes MINUTES
  (libpcre2's interpreter is super-quadratic on deep brace nesting; NOTES.md section 3).
- `check_set.py` -- the set's own checks (`--full` re-derives all expectations).
- `fetch_sqlite.py`, `fetch_kernel.py` -- the F2 fetchers. `fetch_sqlite.py` is PINNED and RUN
  (SQLite 3.54.1, approved by Frank 2026-10-27): `vendor/sqlite3.c.xz` + `.sha256` + `SQLITE.md`.
  `fetch_kernel.py`: empty pin table, refuses by name until Frank approves each URL + sha256.
  The F2 subjects themselves (locator + expectations) are still OWED to a lane.
  `skipped_subjects.tsv` names the F2 subjects skipped. `vendor/pcrec/` -- cscan.rxt +
  gen_cscan.py, byte-verbatim, MIT (PROVENANCE.md). `values/users.tsv` -- the
  co-member callee's runtime set.
- `provenance.tsv` -- the capability-set provenance columns for every pattern.

Not here yet (other lanes): `assists/` (L2/L6), `callees/` (L5), the `--mode calls`
driver support (L4), `expectations` for the vars members (L7).
