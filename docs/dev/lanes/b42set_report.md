# [B42] restart lane L3 — bench/capability@0.1, the SET (lane `b42set`)

Branch `lane/b42set`, worktree `worktrees/b42set`, from `master` tip
`4e4e52c`. Brief: turn L1's wild imports (`curation/wild/`) and L2's
designed members (`curation/designed/`) into the real, runnable sub-bench
`bench/capability@0.1`, built ON pcrec's delivered `.rxt` format
(pin cd371441, abi 25) as the pattern source of truth. Nothing measured;
generators + smoke only.

**STATUS: COMPLETE.** All deliverables built, generated, and smoke-checked
(55/55 generic gates green, `expectations.tsv` committed). Nothing owed.

## What this lane built

- `bench/capability/patterns.rxt` — 64 pattern blocks (63 members + the
  floor), each with a native `provenance` sub-block (the format's own
  nine pattern-scope fields) and a `tag family=/hazard=/requires=`
  line, plus one file-scope `vocabulary`/`ext bench` head. **Passes
  `pcrec --list-source patterns.rxt` cleanly (exit 0)** and every
  block's decoded `pattern` column round-trips byte-for-byte against
  the authoring table's own canonical bytes — checked programmatically
  in `gen_patterns.py --check` (the DD-13b.W23.5 dump-value seam),
  including the one genuinely raw-non-UTF-8-byte member
  (`mojibake-curly-quote`, `pattern-esc` with `\x93`/`\x94`), AND
  cross-checked against `curation/designed/patterns/SHA256SUMS.txt`'s
  own independently-staged hash for every designed member (the second
  finding below is why that cross-check now exists).
- `bench/capability/gen_patterns.py` — the master table: parses both
  curation TSVs, applies the twin-pairing reconciliation (below) and a
  REQUIRES-tag derivation, renders `patterns.rxt` + `patterns/*.rx`
  (a derived export for today's pre-`.rxt`-loader harness), and
  `--sidecar`/`--provenance` modes feeding `subbench.toml` and
  `gen_provenance.py`.
- `bench/capability/subbench.toml` — `id="capability"`, `version="0.1"`,
  `regimes = ["search_short", "throughput"]` (no `match`, per the
  design's own set-wide exclusion), `short_search_max_bytes = 512`,
  64 `[[patterns]]` entries.
- `bench/capability/captext.py`, `gen_subjects.py` (75 typed short
  subjects), `gen_throughput_subjects.py` (3 throughput texts, with an
  empirical redos-safety timing guard).
- `bench/capability/gen_expectations.py` → **`expectations.tsv`,
  COMMITTED**: 4,990 oracle-verified rows, `method =
  libpcre2-differential`, derived in **12.7 seconds** (see "What went
  wrong, and the real finding" below for why this number matters).
- `bench/capability/gen_provenance.py` → `provenance.tsv`: the licence
  allowlist, `fidelity`/`adaptation` and CC-BY-SA/`attribution` gates,
  plus the Q1 similarity-check arm — all clear on the real 64-pattern
  population.
- `bench/capability/gen_variants.py` → `variants.tsv` (deliberately
  empty; no v1 testee needs a rewrite).
- `bench/capability/NOTES.md` — objective, twelve families as built, the
  twin-pairing reconciliation, blinding statements, subjects, the
  outlier rule (R0-R8), predictions P1-P10, what is deferred, and the
  corrected finding below.
- `bench/capability/CLAUDE.md` — rewritten from the staging stub.
- `docs/dev/predictions/capability-0.1-first.tsv` — 15 clause rows,
  structurally validated against `pcrecbench.interpret.load_predictions`.
- `bench/capability/_diag_worker.py` + `diag_expectations_timing.py` —
  the diagnostic tooling this lane built under the manager's
  intervention (below); kept committed as project-local diagnostic
  tooling (per-pattern `gnutimeout`-wrapped timing), not part of the
  generator chain `make check-harness` runs.

## What went wrong, and the real finding (manager intervention)

The first `gen_expectations.py` attempt was launched in the foreground
WITHOUT `gnutimeout` (a boilerplate violation this report does not
hide) and ran past 1h39m before the manager intervened: killed by
verified PID (`readlink /proc/<pid>/cwd` confirmed the worktree first),
with clear instructions to re-run instrumented and find the actual hot
cell(s) rather than accept a multi-hour generator as committable.

**Built two diagnostic tools** (`_diag_worker.py`: one pattern's full
oracle derivation, timing every cell to stdout; `diag_expectations_
timing.py`: the driver, wrapping each pattern in `gnutimeout 90`) and
ran the sweep. Result: **63 of 64 patterns completed in well under a
second each; exactly one, `codegrammar-flat`, timed out at 90s**,
stuck on just the 64 KB throughput text after completing all 77 of its
other cells instantly.

**Root cause, found by direct profiling (not a pcrec/oracle defect —
this lane's own generator bug)**: `gen_patterns.py`'s `_read_tsv()`
used Python's `csv.DictReader` with CSV's DEFAULT quoting rules on a
plain TAB-DELIMITED curation file. Exactly one field across both
curation TSVs starts with a literal `"` —
`codegrammar-flat`'s canonical text, `"([^"\\]+)"\s*:\s*` — and CSV's
default quoting silently treated that leading `"` as an OPENING QUOTE
CHARACTER and swallowed it. The pattern this lane had actually been
compiling and shipping (in the commit already sent to the team lead
as "structurally stable") was `([^\\]+)"\s*:\s*`, missing its leading
literal. Without that leading `"`, PCRE2 has no required-first-byte
optimization at all (the pattern now starts with a capturing group
matching almost every byte), so an unanchored search over 1 MB of
background text containing no `"` anywhere backtracks QUADRATICALLY
over the entire unbroken run — measured at 37s for 64 KB alone,
projecting to hours at 1 MB. This, not the originally-suspected
`wild-datetime-datefinder-alternation` pattern (which is real but
genuinely fast, 9.3s for its whole 79-cell run), was the actual
multi-hour cost. **The earlier interim message to the team lead and
this report's own first draft both named the wrong pattern as the
concern — corrected here and in NOTES.md rather than left standing.**

**Fixed three ways**, all committed:

1. `_read_tsv()` now passes `quoting=csv.QUOTE_NONE` — TSV is not CSV,
   and this is the correct fix for the actual bug.
2. `load_designed()` now cross-checks every pattern's parsed text
   against `curation/designed/patterns/SHA256SUMS.txt`'s own
   independently-staged hash (L2 computed these at authoring time,
   before this lane's parser existed), so a future parsing regression
   of this shape fails LOUDLY at generation time by name, not silently.
3. `captext.py`'s `_source_line` now emits a double-quoted string
   literal (`log.info("word_123")`, a genuinely common real source-code
   shape) in roughly half its generated lines — a belt-and-braces fix
   that bounds ANY future `[^"...]+`-shaped pattern's worst-case
   unanchored backtrack to one line's length, so this HAZARD CLASS
   cannot recur even from a different cause.

With all three fixes, `gen_expectations.py` completes in **12.7
seconds** (4,990 rows) and the diagnostic sweep confirms **zero
timeouts, every pattern under 10s**. The 41-check acceptance round-trip
(`gen_patterns.py --check`, including the real-binary `--list-source`
comparison) was re-run and stays green with the corrected text — the
fix changed what the `.rxt` file and every derived artifact actually
contain, not merely how fast they generate.

**A second, smaller finding surfaced by the same corrected run**: the
oracle GAVE UP (PCRE2's own match-limit, a bounded and expected
outcome, not a hang) on two triples involving `evil-alt-nested`
(`^(([a-z]+)*)+$`) — its own short near-miss subject and an unrelated
family-11 subject authored for a different pattern. Both rows are
correctly DROPPED from `expectations.tsv` and listed on stderr, per the
shared derivation's own existing rule. No further mitigation needed;
recorded in NOTES.md as confirmation that family 10's already-planned
fixed-`--iters` mitigation (CB8) is the right and sufficient plan.

## The twin-pairing reconciliation

Full table in `NOTES.md`; summary:

| designed twin | guessed partner | real partner | verdict |
|---|---|---|---|
| `uuid-near-miss` | grok UUID | `wild-validator-uuid-grok` (family 1) | CONFIRMED — real divergence on a bad-nibble subject |
| `ipv4-near-miss` | an OWASP IPv4 shape | `wild-validator-ipv4-owasp` (family 1) | CONFIRMED but WEAKER than designed: the two are answer-identical on every subject tried (OWASP's own pattern already range-bounds each octet) — a finding, not a defect, per the design's own R1 rule |
| `base10num-near-miss` | grok BASE10NUM | `wild-logparse-base10num-grok` (family **2**, not 1) | **MISMATCH, REPAIRED**: family metadata corrected to `wild-logparse`, text untouched |
| `winpath-near-miss` | grok WINPATH | `wild-logparse-winpath-grok` (family **2**, not 1) | **MISMATCH, REPAIRED**, same shape |

Per the brief's own instruction ("flag it in your report rather than
re-authoring"): both mismatches are repaired by FAMILY METADATA
CORRECTION only, never by rewriting either pattern's text. Total set
membership is unaffected (64); per Frank's Q2 ruling (realism, not a
ratio), a per-family count target was never binding.

## Deviations from the design, each stated and reasoned

1. **75 short subjects, not 36** (`capability_set_v1.md` §3.4). Sixty-four
   heterogeneous real-world patterns do not share one small vocabulary
   the way `bench/syntax`'s 95 do. Re-derived cell-time arithmetic in
   `NOTES.md`: `search_short` grows to roughly ~23 min/cell, still
   comfortably inside `CELL_CAP`'s 5,400 s default (~2-2.5× headroom).
2. **The twin-pairing family corrections** (above).
3. **The `ext bench` capability matrix is a first cut**, inferred from
   `bench/syntax`'s census findings and pcrec's D26 compatibility
   posture, not independently re-derived from a real compile census.
   Flagged in `NOTES.md` for L5 to re-verify before any harness wiring
   trusts it.
4. **`gen_variants.py`'s table is empty** — no v1 roster testee needs a
   rewrite.
5. **`captext.py`'s source-line grammar now includes quoted strings**
   (the belt-and-braces fix above) — a deliberate, documented departure
   from the first-committed grammar, not an oversight.

## Safety check: family 10 (`redos-nested`) and the oracle

Every one of the six `redos-nested` patterns is authored `^`-anchored.
Verified three ways now: `gen_subjects.py`'s near-miss subjects capped
at ≤ 20 bytes; `gen_throughput_subjects.py`'s empirical `find_all`
timing guard against all three throughput texts; and, this lane's own
diagnostic sweep, which independently confirmed every `redos-nested`
pattern completes in well under a second against every subject and
text in the set (the two oracle give-ups above are PCRE2's own bounded
match-limit, not a timeout or a hang).

## What ran (charter-vs-committed) — final state

- `gen_patterns.py --check`: **PASS** (round-trips `patterns.rxt`
  against the real pinned binary, resolved via `git rev-parse
  --git-common-dir` — a path bug this lane found and fixed, since
  `build/` is not per-worktree).
- `gen_subjects.py`, `gen_throughput_subjects.py`: **PASS**.
- `gen_expectations.py`: **PASS**, 4,990 rows, 12.7s (was: multi-hour
  runaway, root-caused and fixed — see above).
- `gen_provenance.py --check`: **PASS** (64/64 rows).
- `gen_variants.py --check`: **PASS** (0/0, the checked-empty case).
- `tools/selfcheck.py`'s generic per-set gates, run individually
  (`run_generic_gates.py`, a lane scratch driver, NOT committed —
  `check_manifests`, `check_patterns_distinct`, `check_floor_pattern`,
  `check_id_preflight`): **55/55 PASS**, including the floor-pattern
  quick-cell smoke (needed `expectations.tsv`, now present) and the id
  preflight over all 64 patterns + 75 short subjects + 3 throughput
  subjects. Every OTHER set's own generic gates were incidentally
  re-run by the same enumeration and stayed green.
- `python3 -c "... pcrecbench.interpret.load_predictions(...)"`: **PASS**
  (15 rows load clean, re-validated after the P3 correction below).
- Full `make check` / `make check-harness`: **NOT run** — the brief's
  own allowance for a lane this size; the generic gates above are the
  targeted equivalent for this set specifically, run twice (before and
  after the fix) to confirm the regression closed.

## Mandate compliance

Touched only `bench/capability/`, `docs/dev/predictions/`,
`docs/dev/lanes/b42set_report.md`, and (read/build only, never write)
the shared `build/pcrec-cd371441/` binary already delivered by the
restart's earlier lanes. `~/pcrec` was never read or written directly.
No `schema/`, `pcrecbench/` or `testees/` file was touched. The
runaway process was killed by verified PID only (never `pkill -f`),
per the box rules.

## For L4 (the loader) — unchanged from the interim message

`patterns.rxt`'s STRUCTURE is stable and unaffected by the
`codegrammar-flat` fix (only that one block's `pattern` line's bytes
changed; the grammar, the provenance sub-block shape and the `ext
bench` head are untouched). L4 can charter against the shape already
described in the earlier interim message to the team lead.
