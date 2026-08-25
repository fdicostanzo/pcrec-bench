# pcrecbench/tests/fixtures/ -- a small synthetic store for the reporter

Every record here is SYNTHETIC (`synthetic: true`, `note` says so,
`machine_id: "repfix-box"`, `run_id` prefixed `fixture-run-`). No engine
was ever run; every number was invented by hand specifically so the
reducer's arithmetic can be checked (`pcrecbench/tests/test_report.py`'s
`test_known_reduction`). Nothing here may be cited as a measurement.
Generated once by a scratch script (not committed -- see
`docs/dev/pcrec_references.md`-style provenance note below) and then
hand-edited for the failing/unsupported cells; regenerating it from
scratch would need to reproduce those by-hand choices, so the FILES are
the source of truth now, not the generator.

The sub-bench they describe (`fixture-mini@1.0`) is INVENTED for this
suite only -- two tiny patterns (`p-digits` = `^[0-9]{3}$`, `p-word` =
`^[a-z]{3}$`), three subjects, two regimes (`match-compliance`,
`short-subject-search`). It is not the email specimen and not derived
from any real pcrec-bench sub-bench.

## Layout

- `store/` -- the MAIN fixture store, WITH `store/index.tsv` (exercises
  the index-based discovery path). Three testees over `fixture-mini@1.0`:
    - `pcrec_1.0.0-gdeadbee_vm-caps-simdna` (`compiled-aot`) -- every
      cell passes. `p-digits`/`s-num-1`/`match-compliance` is the
      HAND-COMPUTED cell `test_known_reduction` checks exactly (trials
      100000/110000/90000 ns over 1000 iterations -> ns/call
      [100,110,90] -> median 100, min 90, max 110).
    - `libpcre2_10.46_interp-caps-simdna` (`interpretive`) -- the
      `p-word`/`s-word-1`/`match-compliance` cell is DELIBERATELY WRONG
      (`did-not-match-as-expected` on all 3 trials) to exercise the
      expectation-failing exclusion from ranking.
    - `libpcre2_10.46_jit-caps-simdna` (`eager-jit`) -- `p-word` is
      `unsupported-by-declaration` (a fictional declaration reason, purely
      to exercise the outcome and the "no cost for an unsupported
      pattern" rule) with no match rows for that pattern on this testee.
  Together: a compile-cost mix of `compiled-aot` and `interpretive`
  (plus `eager-jit` as a bonus third class), all three testees × 1
  sub-bench × 2 regimes, one failing cell, one unsupported-by-declaration
  cell.
- `store_walk_only/` -- ONE record (the pcrec one, byte-identical to
  `store/`'s copy), with NO `index.tsv`, to exercise the reporter's walk
  fallback over `store/records/`.
- `mixed_version/records/` -- TWO records for the "refuses mixed schema
  versions" test, under `records/` with no index.tsv (so `--store
  fixtures/mixed_version` walks both):
    - `...20260825T110000Z.jsonl` -- `schema_version: "1.0"`, otherwise
      identical in shape to the pcrec record above. VALID; passes
      `schema/validate.py` cleanly.
    - `...20260825T110500Z.jsonl` -- `schema_version: "2.0"`.
      **INTENTIONALLY schema-INVALID** -- this repo's schema only defines
      1.0 (`schema/record.schema.json`'s `x-record-schema-version`), so
      there is no way to construct a genuinely-valid 2.0 record without
      extending the schema (out of this lane's scope). This mirrors the
      `[B2]` lane's own convention
      (`schema/examples/bad/x17-future-major-version.jsonl`): the file's
      `note` field says so, and `test_all_fixtures_validate` asserts it
      is rejected by rule X17, not just "rejected". `make check-report`
      does NOT run `schema/validate.py --check-filename` over this
      directory as if it were a normal fixture store for exactly this
      reason -- see the Makefile target.

## Editing

If a match/compile row's timing values change, the setup line's
`content_hash` must be restamped or `schema/validate.py` fails on rule
X6 (this is deliberate -- it is what caught an unplanned tamper during
this lane's own positive-control exercise, see
`test_report.py`'s `_POSITIVE_CONTROL_LOG`):

    python3 schema/validate.py --print-hash <file>

and patch the printed value into `content_hash.value`.

Maintenance: update this file when files are added/removed or change
role.
