# b125cap report -- capability@0.2 (plan [B125], inbox I-136, outbox O-87/O-88)

Branch `lane/b125cap`, worktree `worktrees/b125cap`. Writer lane: no timed run, nothing under `store/` or `reports/` touched. No pcrec write.

## Verdict (second pass, after the manager's rulings)

Built, re-derives byte-identically (`gen_expectations.py --check` 6,104 rows, passes). Rulings applied: the DFA fallback is kept with its deterministic workspace budget; a third method `structural-alphabet` (NOMATCH ONLY) was built and takes precedence over the DFA; `email-nested-plus` x the evil subjects stay DROPPED BY NAME; the two near-miss subjects were cut to 16 KiB. Charter item A (long near-miss rows) is now MET for both target patterns. `make check` in full was NOT run (the manager's launch).

Precedence: `libpcre2-differential` -> `structural-alphabet` -> `libpcre2-dfa-fallback` -> dropped by name; sidecar `fallback_methods = ["structural-alphabet", "libpcre2-dfa-fallback"]`. Soundness argument: `docs/design/expectation_methods_v1.md`. By precedence the DFA fallback restores NOTHING in this set (the structural rule takes all four restorable triples; the DFA declines the other two on its budget); it stays declared and is exercised by the self-check arms.

## Counts

| | 0.1 | 0.2 |
|---|---|---|
| patterns | 64 | 71 (+7) |
| short subjects (search_short) | 75 | 75 (unchanged) |
| throughput subjects | 3 | 11 (+8) |
| expectation rows | 4,990 | 6,104 (+1,114 = 527 search_short + 587 throughput) |
| `libpcre2-differential` | 4,990 | 6,100 |
| `structural-alphabet` | 0 | 4 |
| `libpcre2-dfa-fallback` | 0 | 0 |
| triples DROPPED by name | 2 | 2 |

0.1 invariants, re-verified on the final file: all 4,990 old rows present byte-identical in the same relative order; `manifest.tsv` zero diff; the 3 old throughput hashes asserted in the generator; `provenance.tsv` +7 rows only; the 64 old `patterns/*.rx` unchanged.

## Manifest summary (paste-ready for an outbox item)

New patterns (family wild-logparse, provenance authored/synthesized, sourced to I-136; `requires=true-end-anchor` on the two `\z` ones): `letters-bounded-tail-z` `(?:[a-z]{0,1024})\z`, `tail-digits-eol` `\d+$`, `tail-word-eoz` `\w+\z`, `tail-space-eol` `\s+$`, `tail-ext-lower-txt` `[a-z]+\.txt$`, `tail-dotstar-txt` `.*\.txt$`, `hex8-bounded` `\b[0-9a-f]{8}\b`.

New subjects (all throughput regime only; generator `gen_throughput_subjects.py`, primitives in `captext.py`, seeds `0xC0FFEE11..21`):

| subject | bytes | sha256 |
|---|---|---|
| `t-evil-match-60k` | 61,440 | 7e997b935b2b6fc8914f888a146f90163a59ee7e9a356b22880999d4c4427ee1 |
| `t-evil-nearmiss-16k` | 16,385 | 7783c01caab83dfdc8bf4859f2dd1bab0e2bbd5fb6d3d12278b8c064fb2728af |
| `t-trim-match-60k` | 61,440 | eb6cb8751e37a9cb75812a3cb05b1a939624c1e9e6ef3f0716bb1e0739f3e80a |
| `t-trim-nearmiss-16k` | 16,385 | 41783dc6c35a4a0670ac026a91cf8c9569b5d479e9d0436613d0fa0e17fbcd47 |
| `t-mixed-runs-4k` | 4,096 | 04db4aaa9e01339995fb7acc0dfdb216042f5913b41e938b368cbd75f411b7d5 |
| `t-tail-digits-1m` | 1,048,522 | 06a2c18097ee1b62860a53250be52e50a9be2b284e0e67b4afae3ff8c0a3dbd2 |
| `t-tail-txt-1m` | 1,048,527 | e1fc06ff899dffd8fad1239d20ca32c72f2708881c311d27cc4c9fbbe19fc057 |
| `t-tail-space-1m` | 1,048,522 | 9d6c19081540d136581fc08ba781a0d5062abf696693c4d5ace1142b7254b3b1 |

The near-misses are the first 16 KiB of the matching run plus one terminating non-member byte (`!` / `x`). The three tails share one prose body and differ only in the last line (`total 20250614` / `saved to report.txt` / `end of file` + 3 spaces); the truth table is in each manifest description.

Rows by method: the four `structural-alphabet` rows (all `nomatch`) are `evil-alt-nested` x `rd-evil-alt-near-miss`, `evil-alt-nested` x `sd-empty-alt-hit`, `evil-alt-nested` x `t-evil-nearmiss-16k`, `trim-nested-star` x `t-trim-nearmiss-16k`. The two restored short triples are therefore method `structural-alphabet` (not the DFA). Dropped by name (no required-literal rule this revision): `email-nested-plus` x `t-evil-match-60k` and x `t-evil-nearmiss-16k` (the backtracker gives up; structural declines: no trailing `$`/`\z`; the DFA declines on its budget).

Key derived rows: `evil-alt-nested` x `t-evil-match-60k` = match (0,61440) count 1; `trim-nested-star` x `t-trim-match-60k` = match (0,61440) count 1; `hex8-bounded` counts 131 (`t-mixed-runs-4k`), 264/263/263 (the tails); `letters-bounded-tail-z` on `t-evil-match-60k` = first (60416,61440), count 2.

## Controls

- `structural-alphabet`: the pattern parses on 1,114 of the 6,100 backtracker-answered triples, states nomatch on 941 of them, and the oracle agrees on all 941; no size skip. DISAGREEMENTS 0.
- DFA: 4,724 triples on DFA-readable patterns, existence+leftmost start agree on 4,698, span+count agree on 1,239 anchored triples, 26 declined by the workspace budget / unsupported items (not disagreements; the "skipped count"), no size-bound skip was needed. DISAGREEMENTS 0.
- Self-check `check_expectation_second_method` (17 positive/decline/sabotage arms for structural-alphabet, the DFA arms, both control-sabotage arms, the committed method census): all PASS standalone.

## The `.*\.txt$` measurement

Backtracker derivation at ~1 MiB stays UNDER the match limit: 0.02 s per find-all on each tail, no give-up (leading-`.*` start-of-line optimisation). Tail family is all `libpcre2-differential`.

## Timings

- Final derivation WITH both controls: 1 m 19 s wall (`gen_expectations.py`, ~78 s CPU); `--check` the same. 13 s before. Without controls roughly the oracle share (~50-60 s). `--no-control` skips them.
- Oracle per-call time on the shrunk near-miss: `tail-space-eol` x `t-trim-nearmiss-16k` 1.83 s (25 s at 60 KiB) -- a real PCRE2 property, recorded in NOTES as a predicted pcre2 cell cost.
- Other new triples over 1 s per oracle call: `tail-ext-lower-txt` x `t-evil-match-60k` 1.7 s; `letters-bounded-tail-z` x `t-evil-match-60k` 1.2 s; `wild-waf-crs-942360-concat-sqli` x `t-trim-match-60k` 1.7 s (existing pattern, new subject); `wild-datetime-datefinder-alternation` x each of the three `t-tail-*-1m` 6.8 s (existing pattern, 1 MiB like `t-1m`). `letters-bounded-tail-z` x `t-evil-nearmiss-16k` 0.32 s.
- DFA workspace budget: 16,000 ints, deterministic.

## What changed outside bench/capability (readers of the method vocabulary)

None restricts it (`grep libpcre2-differential`: `subbench.py` carries the column unread; no schema, reporter, harness or tool compares it). Added: `subbench.Subbench.fallback_method` + `FALLBACK_METHODS` (validated sidecar key), `expectations.py` (`pattern_structure`, `dfa_features`, `fully_anchored`, `dfa_fallback`, `DfaControl`, `--no-control`), `oracle_pcre2.Compiled.dfa_search` (+ self-check), `tools/selfcheck.py` `check_expectation_second_method` (wired into the harness list) and the `capability@0.2` records glob in `check_capability_policy`. Docs: new `docs/design/expectation_methods_v1.md`, pointers in `harness_contract.md` and `docs/design/CLAUDE.md`, `bench/capability/CLAUDE.md`, NOTES.md (0.2 section with P11-P16, R9-R11, written before any run). Other sets' derivations are unchanged (a set with no `fallback_method` takes the old path; syntax re-derives byte-identical).

Readers left alone on purpose (records-only, keyed to the 0.1 store records): `tools/program_identity.py` usage text, interpreter/catalogue fixtures and goldens, committed reports, `scripts/CLAUDE.md` prose. The sidecar `rxt_source` loader reads 71/71 provenance rows.

## Findings for the manager

1. `pcre2_dfa_match` is ~n^2.8 on nested quantifiers; the structural rule is what restores the long near-misses. By precedence the DFA fallback restores nothing in capability@0.2.
2. I-136 says capability "has hex32-id"; no such pattern exists in the set. `hex8-bounded` is new ground.
3. `\s+$` is quadratic for the backtracker on a long whitespace run plus one non-space (1.8 s per call at 16 KiB); pcre2 cells will show it. See the other >1 s triples above.
4. Throughput is "every pattern x every throughput subject", so subjects cannot be pattern-specific; all 71 patterns run every new subject (all derive; two triples give up for every method).

## Charter-vs-committed checklist

| item | where | state |
|---|---|---|
| A: long MATCHING subjects | `t-evil-match-60k`, `t-trim-match-60k` | done, derived |
| A: long NEAR-MISS each, with rows | `t-evil-nearmiss-16k`, `t-trim-nearmiss-16k` (16 KiB per ruling 4); rows `structural-alphabet` | done |
| A: regime stated in NOTES | NOTES.md 0.2 section | done (throughput only) |
| B: second method, only on give-ups, restrictions as code, control with agreement count, wired into `--check`, docs | `libpcre2-dfa-fallback`; `expectations.py`; `expectation_methods_v1.md` | done |
| B (ruling 2): `structural-alphabet`, nomatch only, soundness argument, control on every answered triple, negative + sabotage arms | `expectations.py` `structural_nomatch`; design doc; selfcheck | done |
| B: restore the two dropped triples | both `nomatch`, method `structural-alphabet` | done |
| C-i / C-ii / C-iii | `t-mixed-runs-4k`, `letters-bounded-tail-z`; `tail-*` x `t-tail-*-1m`; `hex8-bounded` | done |
| C-ii: `.*\.txt$` measurement | 0.02 s, no give-up | done |
| P-rules, predictions, outlier rules before any run | NOTES.md P11-P16, R9-R11 (updated for 16 KiB / structural) | done |
| CLAUDE.md, manifests, version readers | done | done |
| No committed report / store edits | none touched | confirmed |
| Full `make check` | not run (ruling 5: the manager runs it after merge review) | OWED, owner manager |
| Outbox manifest item | this report's tables | OWED, owner manager |
