# b125cap report -- capability@0.2 (plan [B125], inbox I-136, outbox O-87/O-88)

Branch `lane/b125cap`, worktree `worktrees/b125cap`. Writer lane: no timed run, nothing under `store/` or `reports/` touched. No pcrec write.

## Verdict in one paragraph

Built and re-derivable, with ONE design point that did not hold and is OWED to the manager. The second method (`libpcre2-dfa-fallback`) restores the two short dropped triples and its control reads 0 disagreements. It CANNOT restore the long nested-quantifier near-misses: `pcre2_dfa_match` is itself about n^2.8 on `(...+)*`-shaped patterns (0.26 s at n=1000, 14 s at n=4000; hours at 60 KiB). So 4 triples are DROPPED BY NAME: `evil-alt-nested` x `t-evil-nearmiss-60k` and `trim-nested-star` x `t-trim-nearmiss-60k` (the two A asked for) plus `email-nested-plus` x both `t-evil-*` subjects. The long near-miss cells for those two patterns therefore stay unjudged (`n_no_expectation`), exactly as the short cell was. A proposed third rule that would close them is described under OWED. The manager was messaged about this mid-lane (msg 874a2b6b).

## Counts

| | 0.1 | 0.2 |
|---|---|---|
| patterns | 64 | 71 (+7) |
| short subjects (search_short) | 75 | 75 (unchanged) |
| throughput subjects | 3 | 11 (+8) |
| expectation rows | 4,990 | 6,102 (+1,112 = 527 search_short + 585 throughput) |
| method `libpcre2-differential` | 4,990 | 6,100 |
| method `libpcre2-dfa-fallback` | 0 | 2 |
| triples DROPPED by name | 2 | 4 |

0.1 invariants, verified: all 4,990 old rows are present byte-identical and in the same relative order; `manifest.tsv` has zero diff; the 3 old throughput rows are unchanged (asserted in `gen_throughput_subjects.py` against their sha256); `provenance.tsv` +7 rows only; the 64 old `patterns/*.rx` unchanged; `patterns.rxt` diff is 80 additions and 3 header-line changes (description text, `version=0.2`).

## Manifest summary (paste-ready for an outbox item)

New patterns (family wild-logparse, provenance authored/synthesized, sourced to I-136; `requires=true-end-anchor` on the two `\z` ones):

| pattern | text |
|---|---|
| `letters-bounded-tail-z` | `(?:[a-z]{0,1024})\z` |
| `tail-digits-eol` | `\d+$` |
| `tail-word-eoz` | `\w+\z` |
| `tail-space-eol` | `\s+$` |
| `tail-ext-lower-txt` | `[a-z]+\.txt$` |
| `tail-dotstar-txt` | `.*\.txt$` |
| `hex8-bounded` | `\b[0-9a-f]{8}\b` |

New subjects (all throughput regime only: every one is > 512 B; generator `gen_throughput_subjects.py`, text primitives in `captext.py`, new seeds `0xC0FFEE11..21`):

| subject | bytes | sha256 |
|---|---|---|
| `t-evil-match-60k` | 61,440 | 7e997b935b2b6fc8914f888a146f90163a59ee7e9a356b22880999d4c4427ee1 |
| `t-evil-nearmiss-60k` | 61,441 | 8ef8f8c74d70f0e538ef69ff157b748cba8d0d96b108af67535d73dc79e2cabf |
| `t-trim-match-60k` | 61,440 | eb6cb8751e37a9cb75812a3cb05b1a939624c1e9e6ef3f0716bb1e0739f3e80a |
| `t-trim-nearmiss-60k` | 61,441 | 5c0a8fd9f607e9c0923629e316c17065d2b588ce2dab8c7d9ff9fafbd09698e3 |
| `t-mixed-runs-4k` | 4,096 | 04db4aaa9e01339995fb7acc0dfdb216042f5913b41e938b368cbd75f411b7d5 |
| `t-tail-digits-1m` | 1,048,522 | 06a2c18097ee1b62860a53250be52e50a9be2b284e0e67b4afae3ff8c0a3dbd2 |
| `t-tail-txt-1m` | 1,048,527 | e1fc06ff899dffd8fad1239d20ca32c72f2708881c311d27cc4c9fbbe19fc057 |
| `t-tail-space-1m` | 1,048,522 | 9d6c19081540d136581fc08ba781a0d5062abf696693c4d5ace1142b7254b3b1 |

The three tails share one prose body and differ only in the last line (`total 20250614` / `saved to report.txt` / `end of file` + 3 spaces); the truth table (a match and a non-match per tail pattern) is in each manifest description and is borne out by the derived rows.

Key derived rows: `evil-alt-nested` x `t-evil-match-60k` = match (0,61440) count 1; `trim-nested-star` x `t-trim-match-60k` = match (0,61440) count 1; `hex8-bounded` counts 131 (`t-mixed-runs-4k`), 264/263/263 (the tails), 0 on the 60 KiB runs; `letters-bounded-tail-z` on `t-evil-match-60k` = first (60416,61440), count 2.

The two restored triples (method `libpcre2-dfa-fallback`, `nomatch`): `evil-alt-nested` x `rd-evil-alt-near-miss`, `evil-alt-nested` x `sd-empty-alt-hit`. The short-search cell is now judgeable for every engine.

Dropped by name (backtracker match limit AND the dfa's workspace budget exceeded): `email-nested-plus` x `t-evil-match-60k`, `email-nested-plus` x `t-evil-nearmiss-60k`, `evil-alt-nested` x `t-evil-nearmiss-60k`, `trim-nested-star` x `t-trim-nearmiss-60k`.

## The control (item B)

Over every triple the backtracker answered (6,100): 4,724 on DFA-readable patterns, 1,376 skipped by feature (atomic 344, backref 516, conditional 86, free-spacing 344, recursion 258 -- same triples counted per feature), existence+leftmost-start agree on 4,698, span+count agree on 1,239 fully-anchored triples, 26 dfa errors (declined, e.g. `negation-scope-lookbehind-var`: variable-length lookbehind, "not supported for DFA matching"; not disagreements), DISAGREEMENTS 0. On the 0.1 content alone (before the new rows): 4,990 answered, 3,724 agree, 1,123 span+count, 0 disagreements.

## The `.*\.txt$` measurement (item C-ii)

The backtracker derivation of `.*\.txt$` at ~1 MiB stays UNDER the match limit: 0.02 s per find-all on each of the three tails, no give-up (PCRE2's leading-`.*` start-of-line optimisation). So the whole tail family is `libpcre2-differential`; the fallback was not needed. Other tail timings (oracle find-all): `tail-ext-lower-txt` 0.05 s, `tail-word-eoz` 0.05 s, `tail-digits-eol`/`tail-space-eol` 0.01 s.

## Timings

- Derivation: 13 s (0.1) -> ~66 s oracle + ~110 s control = 2 m 55 s with the control (`--check` measured 2 m 55 s). Not "well under 13 s"; reasons: three new 1 MiB prose subjects x 71 patterns (datefinder alone ~24 s), and ONE design-quadratic cell, `\s+$` x `t-trim-nearmiss-60k` (25 s in the backtracker, no give-up: the repeat is auto-possessified, so it is slow, not limited). The control adds ~110 s, 93 s of it in four dfa cells that are quadratic on 60 KiB runs (`tail-ext-lower-txt`, `tail-word-eoz`, `tail-space-eol`). Levers if the manager wants it cheaper: `--no-control` (derivation only, ~66 s); shrink `_LONG` in `gen_throughput_subjects.py` for the whitespace pair (quadratic: 16 KiB would cost ~2 s); both are one-line changes and neither changes any 0.1 row.
- Cost to MEASUREMENT, flagged before any window: `tail-space-eol` x `t-trim-nearmiss-60k` costs pcre2-interp/jit seconds per call; `letters-bounded-tail-z` x the 60 KiB runs ~1.3 s per call in the oracle. Also every pattern now runs 8 more throughput subjects.
- `oracle_pcre2.py`'s dfa workspace budget is 16,000 ints (deterministic; a wall-clock budget would make the file irreproducible).
- `make check-schema` not re-run (no schema touch). `gen_expectations.py --check` for capability (2 m 55 s) and syntax (unchanged set, 2 m 50 s; shared code path) pass; `gen_patterns.py --check` (with `PCREC_BIN` at the 60366d747 build; the default cd371441 path does not exist on this box), `gen_provenance.py --check`, `gen_variants.py --check` pass; the new `check_expectation_second_method` (13 checks) passes standalone.

## What changed outside bench/capability (readers of the method vocabulary)

None restricts it (`grep libpcre2-differential`: `subbench.py` carries the column unread; no schema, reporter, harness or tool compares it). Added: `subbench.Subbench.fallback_method` + `FALLBACK_METHODS` (validated sidecar key), `expectations.py` (`pattern_structure`, `dfa_features`, `fully_anchored`, `dfa_fallback`, `DfaControl`, `--no-control`), `oracle_pcre2.Compiled.dfa_search` (+ self-check), `tools/selfcheck.py` `check_expectation_second_method` (wired into the harness list) and the `capability@0.2` records glob in `check_capability_policy`. Docs: new `docs/design/expectation_methods_v1.md`, pointers in `harness_contract.md` and `docs/design/CLAUDE.md`, `bench/capability/CLAUDE.md`, NOTES.md (0.2 section with P11-P16, R9-R11, written before any run). Other sets' derivations are unchanged (a set with no `fallback_method` takes the old path; syntax re-derives byte-identical).

Readers left alone on purpose (records-only, keyed to the 0.1 store records): `tools/program_identity.py` usage text, interpreter/catalogue fixtures and goldens, committed reports, `scripts/CLAUDE.md` prose. The sidecar `rxt_source` loader reads 71/71 provenance rows.

## Findings for the manager

1. The dfa fallback cannot answer nested-quantifier near-misses beyond ~1-2 KB (above). Decision owed: accept the 4 dropped triples, or authorise a structural rule (below).
2. I-136 says capability "has hex32-id"; there is no such pattern in the set (UUID pair is hyphen-delimited, secrets are prefixed). `hex8-bounded` is therefore new ground, not a sibling.
3. `\s+$` is quadratic for the backtracker on a long whitespace run plus one non-space: a real, well-known shape (CVE-2022-25927's trailing-trim); it will make pcre2 cells slow.
4. Throughput is "every pattern x every throughput subject", so a subject cannot be pattern-specific; the 60 KiB runs are therefore run by all 71 patterns (all derive; none hangs; four give up).

## Charter-vs-committed checklist

| item | where | state |
|---|---|---|
| Lane setup, boilerplate | worktree `worktrees/b125cap`, branch `lane/b125cap` | done |
| A: evil-alt-nested long MATCH subject | `t-evil-match-60k` (cdcff88) | done, derived |
| A: trim-nested-star long MATCH subject | `t-trim-match-60k` | done, derived |
| A: long NEAR-MISS each | `t-evil-nearmiss-60k`, `t-trim-nearmiss-60k` | subjects done; their rows for the two target patterns are DROPPED (OWED, below) |
| A: regime stated in NOTES | NOTES.md 0.2 section | done (throughput only) |
| B: method token `libpcre2-dfa-fallback`, only on give-ups | `expectations.py`, `subbench.toml` | done |
| B: restrictions as code (nomatch; fully-anchored span; else dropped by name) | `dfa_fallback`, `fully_anchored`, `dfa_features`; selfcheck arms | done |
| B: control over every answered triple, agreement count | `DfaControl`; 4,698/4,724, 0 disagreements | done |
| B: wired into derivation and `make check-harness` re-derivation | `gen_expectations.py --check` runs it; `check_expectation_second_method` | done |
| B: readers of method vocabulary widened | none restrict it; sidecar validator added | done |
| B: docs/design updated | `expectation_methods_v1.md`, `harness_contract.md` | done |
| B: restore the two dropped triples | both `nomatch`, method dfa | done |
| B: give A's long near-misses their rows | 0 of the 2 target rows restorable by the dfa | NOT MET -- OWED, owner manager, trigger: ruling on the structural rule |
| C-i: ~4 KB mixed-run subject, run vs base10num-grok family and bounded `\z` pattern | `t-mixed-runs-4k`, `letters-bounded-tail-z` | done (base10num patterns run it via throughput) |
| C-ii: tail family x ~1 MiB prose, match + non-match each | 5 patterns, `t-tail-*-1m` | done |
| C-ii: `.*\.txt$` match-limit measurement | 0.02 s, no give-up | done |
| C-iii: `\b[0-9a-f]{8}\b` over prose/throughput | `hex8-bounded` | done |
| P-rules / predictions / outlier rules before any run | NOTES.md P11-P16, R9-R11 | done |
| CLAUDE.md, manifests, version readers | `bench/capability/CLAUDE.md`, manifest_throughput.tsv, selfcheck glob | done |
| No committed report / store edits | none touched | confirmed |
| `make check` green | NOT RUN in full (long run is the manager's launch) | OWED, owner manager. Command: `cd /home/duxevents/pcrec-bench/worktrees/b125cap && make check > build/b125cap_check.log 2>&1; echo "DONE rc=$?" >> build/b125cap_check.log`. Expected new red: none known; the capability re-derivation inside takes ~3 min |
| Outbox manifest item | this report's tables | OWED, owner manager |

## OWED / proposal: structural rule (3) for the long near-misses

Not implemented (it widens the fixed design). For a fully anchored pattern whose atoms parse to a byte alphabet (classes, `\s \d \w`, literals, groups, quantifiers only), every match covers the whole subject, so a subject byte outside the alphabet means nomatch. Needs its own method token (e.g. `structural-alphabet`), the same control against the backtracker, and a decline for anything unparsed. It would restore `evil-alt-nested` x `t-evil-nearmiss-60k` and `trim-nested-star` x `t-trim-nearmiss-60k` (the trailing `!` / `x` is outside `[a-z]` / `\s`), and `email-nested-plus` x both evil subjects only if `@` absent from the subject is accepted as a required-literal argument (a second, separate rule). Roughly an hour of lane work.
