# Lane `b92vsom` — delivery report

[B92] (`docs/dev/plan.md`; Frank's ruling on `docs/dev/lanes/
b72smalls_report.md` §4 / `capability_set_v1.md` §5.6 — option (b) of the
two live candidates the earlier lane found and left BLOCKED-ON-RULING):
wire the documented, unbuilt `vectorscan-block-som` config
(`HS_FLAG_SOM_LEFTMOST`) to answer the driver protocol's EXISTING
non-overlapping find-all count (NMATCHES) and first-match span, leaving
`vectorscan-block-nosom` unchanged (it still measures the SOM-free fast
path, `NMATCHES = -`). No new protocol mode.

Worked in this session's ambient worktree
(`.claude/worktrees/agent-a668f0546b32bf80c`, branch
`worktree-agent-a668f0546b32bf80c`) rather than a manually created
`worktrees/b92vsom` — the environment placed me there directly; BOILERPLATE's
worktree ritual is for a manager-spawned lane creating its own, and this
session's environment already provided one. Base commit `a73b3ab` (master).
Three commits, all incremental:

- `a2b0cf1` — the driver/adapter/config/selfcheck change, the census
  script + archive.
- `68bbf9b` — the CLAUDE.md roster updates (testees/vectorscan/,
  testees/, root).
- (this report, committed next.)

## Charter-vs-committed checklist

1. **`vectorscan-block-som`: block mode with `HS_FLAG_SOM_LEFTMOST`,
   answering the driver protocol's existing non-overlapping find-all
   count (NMATCHES) and first-match spans.** BUILT.
   `testees/vectorscan/driver.c`'s new `--som` flag ORs
   `HS_FLAG_SOM_LEFTMOST` into the compile flags word and switches the
   per-subject match loop to a full-scan-and-reduce path
   (`on_match_som`/`vs_match_list`/`vs_cmp_match`): the callback never
   stops early, accumulates every `(from, to)` Hyperscan reports for the
   whole subject, then reduces it to (a) a first-match span (MINIMUM
   `from`, then MAXIMUM `to` among matches sharing that `from` — leftmost,
   then longest) and (b) under `--find-all`, a real NMATCHES via a sort +
   single-pass walk implementing pcrec match_api.md S3.1's advance rule
   (KB-17: cursor advances to the match's own end when non-empty, else to
   `from + 1`, or the next UTF-8 character boundary under `--utf8` —
   [B77] U1, now LIVE for this config, unlike `nosom`'s inert one).
   `testees/vectorscan/adapter.py`'s `_compile_one`/`measure` pass `--som`
   iff `engine_mode == "block-som"`; `testees/vectorscan/configs.toml`
   adds the `[testees.vectorscan-block-som]` entry. `describe()` sets NO
   `grain` key for it (the schema default, `"full"`) — verified live: a
   real matching span is compared against the expectation the ordinary
   way, and a genuine leftmost-longest-vs-leftmost-first mismatch scores
   `wrong-span-or-captures`, visibly, never suppressed by a `grain`
   relaxation.
   Live end-to-end smoke (via the real adapter, and via the raw driver
   binary): `a+` over "aaa" → `match 0 3 ... 1`; `a` over "aaaa" (find-all)
   → `match 0 1 ... 4`; `a|ab` over "ab" → `match 0 2 ... 1` (the oracle
   answers `[0,1) count 1` — the documented divergence, matched exactly);
   the whole-subject form (`^(?:foo|bar)\z`) confirmed too: "foo" matches
   `[0,3)`, "xfoo" correctly `nomatch` (the `^` anchor).

2. **`nosom` unchanged, still printing `NMATCHES = -`; proof its
   testee_id and argv are byte-identical to before.** BUILT AND PROVEN,
   two independent ways.
   `driver.c`'s `else` branch (reached whenever `--som` is absent, which
   is `nosom`'s own argv, always) is the pre-[B92] code verbatim — the
   `if (som_mode) {...} else {...}` split is the ONLY fork point, so
   `nosom`'s own compiled behaviour is provably unreached by anything new.
   `adapter.py` never appends `--som` for `vectorscan-block-nosom`
   (`som = cfg["engine_mode"] == "block-som"`, False for `nosom`'s own
   `engine_mode = "block-nosom"`). `describe()`'s `build_flags` string for
   `nosom` is confirmed BYTE-IDENTICAL to the pre-lane text (the template
   substitution reduces to the exact original string when `som=False` —
   checked by direct string comparison, not just by eye). PROOF, both
   directions: (a) `tools/selfcheck.py:check_encoding_axis` — an
   EXISTING, unrelated control ([B77] U2's own frozen-table arm) — still
   passes unmodified after this lane's change, independently re-deriving
   `nosom`'s id/`build_flags`/`config_extra` against a table frozen
   BEFORE this lane started; (b) the new `check_vectorscan_som`'s own
   arm 1 re-derives, live, that a genuine `nosom` match under
   `--find-all` still prints `NMATCHES = -` and `span = None,None`.

3. **SOM's documented restrictions declared honestly: first-class
   refusals by name, never errors; a census over bench/capability.**
   BUILT.
   A pattern `HS_FLAG_SOM_LEFTMOST` itself refuses lands on the EXISTING
   generic `did-not-compile` path in `_compile_one` — no new code needed,
   since the compile-time difference is only the flags word passed into
   the SAME `hs_compile()` call already there. Two distinct restriction
   shapes found and named, both Vectorscan's own diagnostic text
   verbatim: an isolated witness (`.*a.{40,}`, "Pattern is too large" —
   an unbounded-history-tracking budget) and TWO real corpus patterns
   (`evil-alt-nested`, `trim-nested-star`, "Start of match is not
   currently supported for patterns which match an empty buffer" — a
   different mechanism, empty-matching inside an unbounded repeat).
   Census: `docs/dev/measurements/probe_vectorscan_som_witness_census.py`
   / `2026-09-26-vectorscan-som-vs-nosom-census.txt` (source header:
   commit, box, load samples, compile-only exemption per
   `probe_vectorscan_capability_census.py`'s own precedent) — of
   bench/capability's 64 patterns, 38 compile under both configs, 2
   compile under `nosom` ONLY (SOM's real cost), 0 under `som` only, 24
   under neither (the same 24 `nosom` already refuses on its own terms —
   SOM adds nothing to that population).

4. **A UTF-8 sibling only if trivially consistent with [B77] U2's
   shape.** NOT ADDED, stated why.
   MECHANICALLY verified consistent (`--som --encoding utf8` composes
   cleanly on the shared driver, smoke-tested by hand: `hs_flags` ORs
   both `HS_FLAG_SOM_LEFTMOST` and `HS_FLAG_UTF8` with no conflict,
   real spans/counts produced) — but "the mechanism composes" is a
   different claim from "the capability declaration and the UTF-8-
   specific divergences are known", which is exactly what U2's own
   lane spent a dedicated witness census establishing for `nosom`'s
   sibling (`docs/dev/measurements/2026-09-25-b77u2-utf8-witness-
   census.txt`). Not trivial by that bar. Documented as OWED in
   `testees/vectorscan/CLAUDE.md`'s new section, not silently skipped.

5. **CONTROLS in `make check`**: som answers agree with the libpcre2
   oracle on a representative sample with divergences documented; nosom
   still prints `-`. BUILT.
   `tools/selfcheck.py:check_vectorscan_som` (new, wired into
   `check-harness`'s `main()` right after `check_boolean_grain_scoring`),
   6 checks: (1) `nosom`'s degenerate shape re-derived live; (2) `som`'s
   identity (`grain` absent, derived testee_id
   `vectorscan_5.4.11_block-som-nocaps-simd`); (3) agreement with the
   real libpcre2 oracle (`pcrecbench.oracle_pcre2`) on three unambiguous
   witnesses (`a+`/"aaa", `a`/"aaaa", `foo`/"xfooy"), span AND NMATCHES
   both exact; (4) the `a|ab`/"ab" leftmost-longest divergence, asserted
   BY VALUE (oracle `[0,1)`/1, som `[0,2)`/1 — the count agrees, the span
   doesn't, exactly as documented); (5) the SOM-only refusal, first-class
   by name. All through the REAL adapter, never a stand-in.

6. **Update `testees/vectorscan/CLAUDE.md`, `testees/CLAUDE.md`, and the
   root `CLAUDE.md` roster lines.** BUILT.
   `testees/vectorscan/CLAUDE.md` gained a full new "`vectorscan-block-som`
   -- [B92]" section (the ruling, the shared-driver split, full grain, the
   reduction, the documented divergence, the restriction census, the
   controls, the UTF-8-sibling deferral) and the pre-existing NMATCHES/
   span-reporting sections were updated to point at it rather than repeat
   the now-stale "OWED" note for `nosom`'s own (still-real) gap.
   `testees/CLAUDE.md`'s vectorscan roster row and the root `CLAUDE.md`
   `testees/<name>/` bullet both gained a clause naming the new config.

## Verification run (targeted, per the brief — not the full `make check-harness`)

- `tools/selfcheck.py:check_vectorscan_som` standalone: **6/6 PASS**.
- Targeted vectorscan-adjacent arms, standalone: `check_high_byte_
  pattern_argv` (includes the vectorscan-nosom transport arm, 1d),
  `check_boolean_grain_scoring`, `check_encoding_axis` (the frozen-table
  control on `nosom`'s own identity) — run together with
  `check_vectorscan_som`: **27/27 PASS, 0 FAIL**.
- `make check-schema`: **6 examples accepted, 74 sabotages rejected for
  the intended rule, 0 wrong** (unaffected, as expected — no schema
  change in this lane).
- `make check-interpret`: **200 passed, 0 FAILED** (six sections;
  unaffected, as expected).
- The full `make check-harness` (~20 min, every engine) was NOT run —
  the brief scoped validation to "the targeted harness sections for
  vectorscan" plus the two `make` targets above. It is the manager's to
  launch per BOILERPLATE's "long runs at the end of a lane" rule; this
  lane's own change touches only `testees/vectorscan/` and
  `tools/selfcheck.py` (one new, additive, self-contained check
  function), so the risk to the rest of the ~300+ check suite is low,
  but it is NOT independently confirmed here.

Store/records: untouched, as instructed — no `pcrecbench run`, no
`quick`, no pinned window.

## Delivery

Branch: this session's ambient worktree branch,
`worktree-agent-a668f0546b32bf80c` (see the note under "Worked in" above
for why there is no separate `lane/b92vsom` branch this time). Three
commits (`a2b0cf1`, `68bbf9b`, and this report), all incremental, working
tree clean at each step. Not merged (the manager's job); not pushed.

## Owed / follow-ups (named, not silently absorbed)

- `vectorscan-block-som-utf8` (item 4 above): needs its own witness
  census before it can ship, the same bar U2 cleared for `nosom-utf8`.
- Adding `vectorscan-block-som` to `bench/capability/gen_patterns.py`'s
  `EXT_BENCH_ROSTER` (the `ext bench` pre-compile capability-policy
  declaration) is a SEPARATE, larger task (its own full witness census
  matching the rigor every other roster row on that file cites) —
  deliberately not built here; `som` still compiles/refuses honestly via
  the ordinary path regardless of whether it has a roster row.
- The full `make check-harness` run (~20 min) is OWED to the manager per
  BOILERPLATE, to confirm the new check function and the driver.c change
  do not interact badly with the other ~300 checks that build/prepare
  adapters in sequence — nothing in this lane's own targeted runs
  suggests a problem, but the full suite was not run here.
