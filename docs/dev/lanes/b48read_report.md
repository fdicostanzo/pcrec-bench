# lane `b48read` — the capability-first window READ (a770139e → cf0962e3 AFTER + ext-roster first sample)

Branch `lane/b48read`, worktree `worktrees/b48read`, read-only with
respect to `store/` and `~/pcrec`. Nothing was re-run: this is a read of
the nine records the 2026-09-17/18 window landed (store 169 → 178,
committed before this lane started).

## What was produced

**Two report groups** (10 files, `reports/`), each CLI-generated
directly against `store/` (no in-process script needed: a KB-16-narrowed
query over an explicit `--testee` roster loads only the matching
records — seconds to tens of seconds per file, not the whole-store cost
KB-16 exists to warn about):

- `2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.{md,tsv,
  subject-grain.md,subject-grain.tsv,interpretation.md}` — the pcrec
  CROSS-PIN AFTER, a770139e vs cf0962e3, eleven testees (three pcre2
  baselines + four pcrec configs at each pin). Query: `--subbench
  capability --version 0.1 --since 2026-09-17T00:00:00Z --until
  2026-09-18T03:00:00Z` plus the eleven `--testee` values — 12 record(s)
  matching, 11 included, 1 superseded (the `pcre2-dfa` `inconclusive-
  spread` history row).
- `2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.{md,tsv,
  subject-grain.md,subject-grain.tsv,interpretation.md}` — the FIRST
  SAMPLE of the five new ext-bench engines (`re2-default`, `re2-longest`,
  `onig-default`, `tre-default`, `vectorscan-block-nosom`), no pcrec pin
  involved. Query: `--subbench capability --version 0.1 --since
  2026-09-18T03:00:00Z --until 2026-09-18T06:00:00Z` plus the five
  `--testee` values — 5 record(s) matching, 5 included, 0 superseded.

Both carry a `--subject-grain-slice` sibling (the catalogue-2.0 machinery,
[B47]) — the first two groups this store has produced one for since the
2026-08-25 email-specimen precedent noted in `reports/CLAUDE.md`.

**Interpretation sidecars**: both `.interpretation.md` files generated
via `pcrecbench interpret --render` against catalogue 2.0 (both carry the
matching `docs/dev/predictions/capability-0.1-first.tsv` automatically,
per the skill's own step 2 — it matches by `(subbench, version)`, not by
report identity, and this window's is not that predictions file's
intended population; §5 of the ledger states exactly what that means for
each report). Both determinism-checked (a second `interpret` invocation
to stdout diffs clean against the committed file) and both re-verified
fresh by `make check-interpret` section 3 (149/149 checks green,
including the two new sidecars — run at commit `9d91bad`).

**Ledger**: `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`
(§0 sample shape + hygiene, §1 the two I-72 erratum cells, §2 the three
KB-20 give-up flips, §3 the F1 fix, §4 the cross-pin population's noise
floor, §5 the five new engines' census + the b46tags cross-check + the
correctness findings, §6 five ranked findings, §7 candidate asks — not
sent, §8 a five-point next-sample checklist).

**Directory docs**: a `[B48] reports` wave section in `reports/CLAUDE.md`
and a row in `docs/dev/ledgers/CLAUDE.md`.

## Findings summary (full detail and citations in the ledger)

1. **Both I-72 erratum cells CONFIRMED fixed.**
   `mojibake-curly-quote`'s wrong answer flips to correct on all four
   pcrec configs (the reporter's own `R-DELTA-3` rule states "now
   measured (was: wrong)" — not this lane's inference); `wild-logparse-
   syslogbase-expanded`'s artifact genuinely shrinks (−4,096/−367 B,
   confirmed from the compile section) with flat wall-clock timing. An
   UNPREDICTED consequence rides along: mojibake's forced-VM throughput
   cell reads `slower ×2.00` cross-pin — the corrected byte pattern can
   no longer be dismissed as cheaply as the argv bug's corrupted one
   was.
2. **The three KB-20 cells CONFIRMED by value**: `timed-out` (opaque,
   `n_gave_up=0`) → `gave-up: PCREC_ERR_STEPS×2` (named, `n_gave_up=10`)
   on `auto-caps`/`vm-caps`/`vm-in-caps`, exactly the shape the fix's
   own account predicted; `auto-nocaps`'s unrelated wrong-answer path is
   unmoved.
3. **The F1 DFA-emitter fix CONFIRMED clean, and fast**:
   `wild-waf-crs-942500-comment-obfuscation` compiles on both `auto`
   arms at cf0962e3 (zero at a770139e) and ranks FASTEST of all seven
   testees on both regimes.
4. **The rest of the cross-pin population is flat**: 93.2% of 2,904
   Δ-bearing rank rows read `unchanged (within spread)`; every other Δ
   outside the two named findings sits at ×1.00–×1.04.
5. **The b46tags REQUIRES-tag correction confirmed live on the real
   corpus**: every one of the six corrected patterns' refusal reason
   matches the corrected tag; `codegrammar-xflag`/`bracket-array-define`
   on `tre-default` reproduce the exact behavioral flip
   (`free-spacing`-only → `free-spacing, named-groups`) the b46tags audit
   predicted from isolated witnesses.
6. **`evil-alt-nested` splits into a FOURTH response shape**: every
   non-backtracking automaton engine in the wider roster (RE2 ×2, TRE,
   Vectorscan) returns silently WRONG; Oniguruma (a backtracker) gives
   up gracefully on a NEW code, `-17:retry`.
7. **The family-11 semantics-divergence trio reproduces on both
   leftmost-longest engines** (`re2-longest`, `tre-default`) and on
   NEITHER leftmost-first one — the convention axis, not the engine
   identity, predicts the divergence, now confirmed on a second and
   third engine beyond `pcre2-dfa`.
8. **TRE has a substantially wider correctness gap than any other new
   engine**: `high-byte-run` reads 0% pass on throughput and 48% on
   search, plus `tag-pair-match`/`crs-942360-concat-sqli` wrong at the
   family-11-typical rate on constructs TRE declares fully satisfied.
9. **Vectorscan's boolean grain renders correctly** (`testee.grain:
   "boolean"` confirmed directly on the record; no report column shows
   it, so this was read from the JSONL, not the TSV).
10. **No predictions file exists for the ext-bench roster**: every P1-P10
    clause reads `not evaluable` against Report B (the file was authored
    for the original seven-testee roster only); Report A's two evaluable
    predictions (P1, P5, P8) carry forward the SAME verdicts as the
    first-sample ledger.

## Validation

**COMPLETE.**

- **CLI equivalence**: both groups were produced by direct
  `python3 -m pcrecbench report ...` invocations (no in-process script,
  so there is no separate CLI-vs-in-process equivalence to prove — the
  committed files ARE the CLI's own output).
- **Determinism**: both `.interpretation.md` sidecars were re-generated
  to stdout via a second, independent `interpret` invocation and diffed
  clean against the committed file (`DETERMINISM_OK` both times).
- **Freshness**: `make check-interpret` run at commit `9d91bad` —
  **149 passed, 0 FAILED** (sections 1-6; section 3, the sidecar
  freshness re-render, covers both new sidecars by directory glob, not
  a hardcoded list — confirmed by reading `catalogue/check_interpret.py`
  section 3's own `os.listdir(REPORTS)` loop before relying on it).
- Every number in the ledger is cited to a report TSV line, a
  sidecar section, a window log line, or (where the reporter's own
  bucketing deliberately excludes a fact — §5.1/§5.3 of the ledger) a
  direct read of the record's own JSONL, named as such every time.
- The b46tags cross-check (§5.2) and the compile census (§5.1) were
  built by a small read-only Python script over `store/records/
  capability@0.1/*/*.jsonl` (not committed — scratch, per the lane
  boilerplate's scratchpad rule); every number it produced was
  cross-checked against the reports themselves (§5.4's `excluded`-section
  rows) before being cited.

## Charter-vs-committed checklist

| brief item | status |
|---|---|
| 1(a) pcrec cross-pin report (erratum ×2, KB-20 ×3, crs-942500) | **COMMITTED** — `reports/2026-09-18-capability-0.1-budu-ryzen1600-after-cf0962e3.*` |
| 1(b) new-engine first-sample report(s) | **COMMITTED** — `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.*` (one file group; §5's census covers all five engines together, matching `reports/CLAUDE.md`'s existing multi-testee-in-one-file convention) |
| 2. Interpretation sidecars for every new report TSV | **COMMITTED** — both, determinism- and freshness-verified |
| 3. Window ledger draft | **COMMITTED** — `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`, report-line citations throughout, KB-21 noted as window provenance (§0.1), the erratum/KB-20/crs verifications each carry a verdict AND the population read (§1-§3, §5.5's explicit "what P8 can and cannot see" paragraph per Frank's context-around-numbers directive) |
| 4. Candidate asks list | **COMMITTED** in the ledger §7 — NOT sent to the outbox (the manager's channel, per the brief) |
| Do NOT merge | honored — branch left for the manager |
| Do NOT write the outbox | honored |
| Do NOT touch `store/` | honored — read-only throughout, confirmed by `git status` showing no `store/` changes in this branch |

**Nothing is OWED.** Every deliverable in the brief is committed on
`lane/b48read`; the candidate-asks list is written but deliberately not
sent (the manager's own channel).
