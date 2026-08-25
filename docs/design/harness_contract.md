# The harness contract — sub-bench layout, adapter interface, store, CLI

STATUS: manager design, 2026-08-25, written for the [B3]/[B4]/[B5] lanes
to build against in parallel. Refines APPROACH.md §4 and requirements.md
§5-§6, §8-§9. A lane that finds a contradiction with the record schema
(docs/design/record_schema.md) reports it; the schema wins on field
names and enums, this note wins on interfaces. Panel at the M1 close.

## 1. Code layout (python 3, BD4)

- `pcrecbench/` — the python package: `harness.py` (run cells), `quiet.py`
  (the quiet-box instrument), `subbench.py` (load a sub-bench directory),
  `adapters.py` (the adapter interface + discovery), `store.py` (write /
  index records), `report.py` (query → report), `__main__.py` (CLI).
- `bench/<name>/` — sub-benches (data + generators + sidecar).
- `testees/<name>/` — adapters (python module + C driver + pin).
- `schema/` — the record schema + validator ([B2]).
- `store/` — the record store (data; committed for the first cut —
  OD-B6 revisits when size demands).
- `Makefile` — `check-schema` ([B2]), `check` (all self-checks), `deps`.

## 2. A sub-bench directory: `bench/<name>/`

```
bench/email/
  subbench.toml        # the SIDECAR: fields only, no grammar (req. §5)
  patterns/orig.rx     # canonical pattern(s), PCRE2 spelling, raw bytes
  patterns/factored.rx
  gen_subjects.py      # deterministic; writes subjects/ + manifest.tsv
  manifest.tsv         # committed: id, len, sha256, description
  subjects/            # GENERATED, gitignored (regenerate = identical)
  gen_expectations.py  # runs the oracle over subjects → expectations.tsv
  expectations.tsv     # committed: pattern, subject id, regime, expected
                       #   (match start end | nomatch), method, oracle version
  throughput/          # GENERATED large subjects, gitignored; listed in
                       #   manifest_throughput.tsv (committed)
  NOTES.md             # per-engine notes; declared variants (req. §4.5)
  CLAUDE.md
```

`subbench.toml` (read with stdlib `tomllib`) carries exactly the fields
requirements §5 names — `id`, `version` (integer, bumped deliberately),
`objective` (free prose + an `objective_kind` enum: mechanism / hazard /
feature / realworld), `description`, `regimes` (subset of
`throughput`, `search_short`, `match`), `[[patterns]]` (name, file,
tags: feature tier, hazard class, size class, convention), `[subjects]`
(generator, manifest), `[expectations]` (file, default method),
`[testees.<id>]` optional per-testee: `variant` (file), `variant_kind`
(`syntax-only` / `restructured`), `objective_preserved` (prose,
required with a variant), `capture_map`, `options` (engine-native
runtime options), `unsupported = "reason"`. Nothing else; a new field
is a design change.

Regime → subject mapping: `throughput` uses `throughput/` subjects with
SEARCH semantics; `search_short` uses `subjects/` entries ≤ 256 B with
SEARCH semantics; `match` uses `subjects/` with MATCH (anchored, whole-
subject) semantics. Expectations are per (pattern, subject, regime).

The email sub-bench (`bench/email/`) is the specimen from pcrec
docs/design/subroutines_measurements/email_specimen/ (read-only source;
COPY the generators and patterns, cite the origin in CLAUDE.md): 85
subjects, three 1 MB throughput subjects, objective_kind = realworld,
objective = "RFC 5322-shaped email validation: the hand-inlined
original and its subroutine-factored form; the factored form's
objective is calls-as-factoring (a testee may not run the inlined
original in its place)". Expectations via the libpcre2 oracle (pcrec's
ctypes binding docs/design/eng_brep_measurements/probes/pcre2_ctypes.py,
copied into `pcrecbench/oracle_pcre2.py` with attribution), method
`libpcre2-differential`, oracle version recorded.

## 3. The adapter interface: `testees/<name>/`

```
testees/pcre2/
  adapter.py     # class Adapter (below)
  driver.c       # the batched in-process timing driver (dlopen libpcre2)
  configs.toml   # testee ids this adapter provides, with their config
  CLAUDE.md
testees/pcrec/
  adapter.py, driver.c (throughput_driver.c / driver.c shape),
  configs.toml   # pcrec-auto, pcrec-nocaps, pcrec-vm — each with
                 #   pin = "<commit>", flags = [...]
  pin.sh         # git archive <commit> from /home/duxevents/pcrec into
                 #   build/pcrec-<commit>/ (gitignored) and make it there
                 #   (-j4, gnutimeout 900); NEVER builds in pcrec's tree
```

```python
class Adapter:
    name: str                       # "pcre2", "pcrec"
    def testees(self) -> dict[str, dict]      # id → config from configs.toml
    def describe(self, testee_id) -> dict     # the record's testee block:
        # every schema field: engine, version (PROBED from the binary/
        # library, never typed), execution_model, automaton_class,
        # openness, license, conventions, captures, engine_mode, simd,
        # build_flags, runtime_options, plus pin (pcrec commit)
    def prepare(self, testee_id, workdir) -> None   # build driver / pin
    def compile(self, testee_id, pattern: bytes, options: dict,
                trials: int) -> CompileResult
        # outcome (compiled / did-not-compile / crashed / timed-out),
        # diagnostic, per-trial seconds by phase, execution_model class,
        # engine_metadata: list[(name, value)] (pcrec: read from the
        # emitted artifact's structured stamps), handle for measure()
    def measure(self, handle, regime: str, subjects: list[Subject],
                iters: int, trials: int) -> list[MatchRow]
        # runs the DRIVER once per (regime, trial); the driver loops
        # `iters` times over each subject IN-PROCESS and reports per
        # subject: outcome-relevant answer (start, end, ncaps, caps),
        # consumed_length, total seconds for the iters; python turns
        # answers into outcomes against expectations
```

DRIVER PROTOCOL (both drivers, so numbers are comparable): invoked by
python as `driver --pattern FILE --mode search|match --list SUBJECTS.tsv
--iters N` (compile-only: `--compile-trials T`); it reads all subjects
into memory first, compiles once (timed, per phase), then for each
subject runs `iters` iterations with a monotonic clock around the loop,
and prints one TSV line per subject: `id  answer  start  end  ncaps
consumed  iters  seconds`, plus a `compile  phase  seconds` line per
phase per trial. Iteration count: `iters` chosen so one subject's loop
is ≥ 50 ms (auto-calibrated by python from a probe run, recorded in the
record); trials default 5. Timeouts: `gnutimeout` on the driver process
only (requirements §3). pcrec's compile = `pcrec` CLI (timed) + `gcc`
(timed) + dlopen of the .so (timed) — three phases; libpcre2 =
`pcre2_compile` (+ `pcre2_jit_compile` for the jit testee) — timed
in-driver. Execution model: pcrec compiled-AOT; pcre2-interp
interpretive; pcre2-jit eager-JIT.

libpcre2 driver: dlopen `libpcre2-8.so.0`, hand-declared prototypes
(precedent: pcrec tests/fuzz/pcre2_abi.h and the specimen's
pcre2_throughput.c — no pcre2.h on this box); version via
`pcre2_config(PCRE2_CONFIG_VERSION)`. Match semantics: search =
pcre2_match at offset 0 unanchored; match = PCRE2_ANCHORED |
PCRE2_ENDANCHORED. pcrec driver: the artifact's `<prefix>_search` /
`_match` entries (pcrec docs/spec/match_api.md) — match regime uses the
artifact's match entry; captures per config.

## 4. Records and the store

`python3 -m pcrecbench run --subbench email --testee pcre2-jit [--trials 5]
[--regimes match,search_short,throughput] [--force-unquiet]` →
(1) load the sub-bench; (2) `quiet.check()` — load1 sampled, mpstat
per-core, refuse (exit 3, message) unless quiet or `--force-unquiet`
(then status `inconclusive-load`); (3) prepare + compile + measure;
(4) load sampled after; (5) build the record (setup + rows), VALIDATE it
with schema/validate.py (a record that fails validation is never
written — the failure is a harness bug); (6) write
`store/records/<subbench>@<version>/<testee-id>/<UTC ts, basic ISO>-<hash8>.jsonl`;
(7) `python3 -m pcrecbench index` regenerates `store/index.tsv` (one
line per record: path, subbench, version, testee, machine, timestamp,
status, rows) — committed with the records.

`quiet.py` (OD-B8): measure the idle baseline of THIS box (load1 over a
quiet minute, per-core %idle from mpstat) at [B3] and set the default
thresholds from it (proposal: quiet iff load1 < 1.0 AND every core's
%idle ≥ 90 over a 1 s mpstat sample; the numbers are the lane's to
measure and report, not to assume); both samples go into the record.

## 5. The reporter (`report.py`, [B5])

`python3 -m pcrecbench report --subbench email [--version N] [--where
field=value ...] [--group-by field] [--regime R] [--format md|tsv]` —
loads the index, filters records on any setup-layer field (enumerated
or normalized), reduces raw trials per (pattern, subject-set, regime)
cell to comparables (median, min, max, stddev, n; iters), computes
per-cell outcome counts and pass-rate, EXCLUDES expectation-failing
cells from ranking columns and lists them, shows N + pass-rate whenever
< 100%, labels compile-cost rows with their execution-model class and
never reduces different classes together, refuses mixed schema
versions, and prints a self-describing header (query, record ids,
sub-bench versions, reduction). Ranking = per pattern × regime, best
median first, ratios to libpcre2-interp as the reference column when
present. It builds and tests against synthetic records made from
schema/examples/ plus its own fixtures; it never runs an engine.

## 6. Self-checks (`make check`)

check-schema ([B2]); `bench/*/` each: generators reproduce the
committed manifests byte for byte; expectations.tsv re-derivable;
adapters: each driver has a smoke (compile a trivial pattern, one
subject, iters 1) and a POSITIVE CONTROL (a subject whose expected
answer is deliberately wrong in a fixture yields `did-not-match-as-
expected`); reporter: fixtures with a known reduction. All under
gnutimeout; all with LC_ALL=C.
