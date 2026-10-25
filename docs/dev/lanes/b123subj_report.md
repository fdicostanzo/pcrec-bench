# Lane b123subj report -- [B123] (2026-10-25)

Branch `lane/b123subj`, worktree `worktrees/b123subj`. Box rule honoured: no
suite, no build, no `make check*`, no expectation derivation, no timing. Run
only: `gen_patterns.py`, `gen_throughput_subjects.py` (both sets; ~1 s each,
the capability one includes its redos safety check), `tools/export_rxt.py
syntax`, `build/pcrec-9ae59f5d4/build/pcrec --list-syntax`, and two probe
scripts of 30-ish oracle calls (all 0.0 s) under `/var/tmp/pcrecbench/b123subj/`.

## What changed

**bench/syntax -> 0.2**
- RE-SEED: `list_syntax_9ae59f5d4.tsv` (the pinned build's `--list-syntax`,
  verbatim under a source header) replaces `list_syntax_9a1583ba.tsv`. Diff vs
  the old seed: +4 rows (`(*UCP)a`, `(*UTF)a`, `(*UTF8)a`, `${name}`), two
  `\p{L}`/`\P{L}` `built` unbuilt -> built, header/description text. Rows 138 ->
  142. The four rows are `NOT_EXERCISED` with stated reasons in
  `gen_patterns.py` (encoding-scope verbs -> bench/utf8; `${name}` is pcrec's
  extension, not PCRE2 syntax, R-BENCH-4). No pattern moved; coverage.tsv
  re-derived (not-exercised 19 -> 23).
- DENSITY PAIR: `t-lka-dense-256k` / `t-lka-sparse-256k` (`censustext.lka_text`
  / `lka_counts`, `gen_throughput_subjects.LKA_*`). 262,144 B each, seed
  20261025, same background and same `item`->` done` conditional (4/5); `item`
  at 1 word slot in 3 vs 1 in 4096. Counts (computed from the final bytes, in the
  manifest descriptions): dense 13,159 `item` / 10,564 `item done` (lka-pos 10,564,
  lka-neg 2,595); sparse 11 / 8 (lka-pos 8, lka-neg 3). The generator asserts
  dense >= 100x sparse and sparse >= 1 of each. The three 0.1 sha256s are asserted.
- Sidecar 0.1 -> 0.2 (description, regimes comment), `export/syntax.rxt`
  regenerated (version line only), NOTES.md section "syntax@0.2" with P14-P16
  and the per-match / per-byte reading rule, CLAUDE.md.

**bench/capability -> 0.3**
- Six `t-hyb-*` throughput subjects (`captext.hyb_*`, `gen_throughput_subjects.
  hyb_subjects`): embed ladder 1,024 / 8,192 / 65,536 B; whole-subject shapes
  logline-16k, datepath-16k, digits-4k. The eleven 0.1/0.2 sha256s asserted.
- The 17 = I-125's literal list (the rule: `RX_VM_PREFILTER "hybrid"` AND
  `RX_ENGINE_WHY` containing "capture group"; pcrec's census file is not in this
  repo). 14 covered. NOT covered, by language: ipv4-owasp, us-zip-owasp,
  moment-iso8601 (bounded languages; a long `\s*` pad would be the trim-nested
  near-miss). Oracle spot check at generation (find-all counts): every covered
  pattern matches its subject (embed 1k/8k/64k: codegrammar 4/36/188, syslog 1/7/58,
  aws 1/13/75, github 2/8/64, slack 1/8/56, pair 1/7/62, `(a|)*\d` 105/1003/8231,
  email 1; whole shapes count 1).
- No `match` regime added (capability_set_v1.md 3.5 stands): Q10's "match-regime
  subject" is built as a subject the pattern MATCHES, in the throughput regime.
- Sidecar 0.2 -> 0.3, NOTES.md section "capability@0.3" with P17-P20 and R12,
  CLAUDE.md.

## Window cost (for tier 2)

From the committed records (timed work only; wall is ~2-3x):
- syntax: a 256 KiB throughput subject = 17.2 s (pcrec-auto) / 18.1 s (vm) /
  20.2 s (pcre2-jit) over ~400 rows. The pair adds ~36-40 s timed = **~2-4 min
  per testee** on a ~47-52 min cell (+~5%).
- capability: per-subject floor ~7 s (t-mixed-runs-4k, 4 KiB: 6.8 s auto / 8.2 s
  jit) + ~0.15 s per KiB; six subjects (109 KiB) = ~58 s timed = **~2-3 min per
  testee** on a ~47-49 min cell (+~5%).
- Neither moves a CELL_CAP. Backtracker give-ups are not expected on the new
  subjects (digits-4k x email-nested-plus is dismissed instantly by PCRE2's
  required '@'); if some engine lacks that check it is a P20 finding.

## OWED to the go (heavy steps; exact commands, cwd = the worktree root)

1. `/usr/bin/gnutimeout 600 python3 bench/syntax/gen_expectations.py` (writes
   `expectations.tsv`; expect +190 throughput rows, 8,265 -> 8,455; the existing
   rows must be unchanged -- verify with `git diff` showing only additions).
2. `python3 bench/syntax/gen_pattern_facts.py` (`tput_m_n` columns and `seed_*`
   move) then `--check`.
3. `/usr/bin/gnutimeout 600 python3 bench/capability/gen_expectations.py` (expect
   +426 rows = 71 x 6; existing 0.1/0.2 rows unchanged; the `method` is
   libpcre2-differential for all, no fallback needed -- else a P17 finding). Also
   `gen_provenance.py --check` and `gen_patterns.py --check` (unchanged by
   construction).
4. `make check-harness` (counts printed by the checks that enumerate subjects may
   need re-pinning: selfcheck holds no per-subject literal I found by grep, but
   it was not run) and `make check-schema`, `make check-interpret`.
5. Viewer/trend/frontpage data are generated from the store and are untouched;
   no records exist for syntax@0.2 / capability@0.3 until a window runs them.
   Window scripts that name `syntax@0.1` / `capability@0.2` by version need the
   bump (manager's).

## Charter-vs-committed checklist

| promise | committed artifact / state |
|---|---|
| 1. lka density pair, same pattern & size, dense vs sparse | `bench/syntax/censustext.py` `lka_text`, `gen_throughput_subjects.py`, `manifest_throughput.tsv` rows `t-lka-*`; commit 717ec8a8 |
| 2. 1-64 KiB match subjects for the 17 | `bench/capability/captext.py` `hyb_*`, `gen_throughput_subjects.py`, manifest rows `t-hyb-*` (14 of 17; 3 excluded with reason in NOTES) |
| 3a. generators + sha256 manifests | done, both sets regenerate clean; 0.1/0.2 sha256s asserted |
| 3b. oracle-derived expectations, method recorded | OWED (items 1, 3 above) -- owner manager, trigger = the go |
| 3c. NOTES.md predictions before any run | done: syntax P14-P16, capability P17-P20, R12 |
| 3d. sidecar version bumps | done: syntax 0.2, capability 0.3 (+ syntax export header) |
| 3e. [B142] re-seed folded in, one syntax bump | done: seed 9ae59f5d4, 4 rows reasoned, coverage.tsv re-derived; facts OWED (item 2) |
| 4. window cost estimate | above |
| 5. CLAUDE.md of every dir touched | bench/syntax, bench/capability updated; docs/dev/lanes has no CLAUDE.md index change needed beyond this report (not added) |
| report | this file |
