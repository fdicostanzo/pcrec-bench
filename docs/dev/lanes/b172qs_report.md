# b172qs report -- capability@0.4, the URL query-string subjects (inbox I-172)

Lane b172qs, branch lane/b172qs, writer. No timing, no pinned run, no pcrec build, `store/` untouched.
Single core (`taskset -c 3`), every command under `gnutimeout`.

## Charter vs committed

| promise | artifact |
|---|---|
| ~1 MB query-string subject, one `k=v&...` per line, deterministic seeded generator in the set's style | `bench/capability/captext.py` `qs_text` (xorshift64*, fresh Rng per subject), `gen_throughput_subjects.qs_subjects`; `t-qs-1m`, 1,048,501 B, seed 0xC0FFEE41 |
| realistic vocabulary: utm_*, id, page, q, sort, session-ish, percent-encoded values, empty values | 30 weighted stems; values: empty 8 %, int 30 %, hex 17 %, word 25 %, %-encoded 12 %, %-encoded e-mail 8 % |
| most lines no dup; a declared 2-5 % minority with a dup at varied distances incl. far | 3.5 % planted per line; realised 298/7,799 = **3.8 %** of lines carry a second occurrence (302 duplicate keys); same line 40 %, next line 25 %, 2-40 lines 30 %, 300-3,000 lines 5 % |
| a few long lines (hundreds of params) | one line in 300 has 150-400 params; longest 386 |
| distribution stated in NOTES.md before anything measured | NOTES.md "capability@0.4" section (no engine timing was run; oracle probes only) |
| near-miss subject, with the reasoning | `t-qs-nearmiss-256k`, 262,092 B, seed 0xC0FFEE42, zero duplicate keys, prefix-sharing keys; reasoning in NOTES.md (set's match/near-miss convention; 256 KiB because a failing start scans to subject end, cost quadratic) |
| manifest + sha256, version bump, expectations for EVERY pattern, provenance, CLAUDE.md | `manifest_throughput.tsv` +2 rows; `subbench.toml` 0.3 -> 0.4; `expectations.tsv` +142 lines; provenance.tsv unchanged (patterns unchanged, `gen_provenance --check` clean); `bench/capability/CLAUDE.md` |
| grep `capability@0.3` and update what must move | readers that must move: `subbench.toml`, `captext.py`/`gen_throughput_subjects.py` headers, `NOTES.md`, `CLAUDE.md` (all updated). Left as history, by design: journal, plan, ledgers, lane reports, `docs/dev/measurements/2026-10-29-b147read/*`, `frontpage.py --set capability@0.2` argument. No code in tools/, pcrecbench/, catalogue/, viewer/ names 0.3 |

## Subject stats (generator output; oracle for the match count)

| | `t-qs-1m` | `t-qs-nearmiss-256k` |
|---|---|---|
| bytes | 1,048,501 | 262,092 |
| lines | 7,799 | 1,628 |
| params | 52,936 | 13,206 |
| duplicate keys | 302 | 0 |
| lines with a duplicate | 298 (3.8 %) | 0 |
| longest line (params) | 386 | 396 |
| dup-param-detect oracle find-all | match, first span 1034-1112, **119 matches** | nomatch, 0 |
| oracle time, one core (probe) | ~14 s | ~2.6 s |

The semantics the generator is built around (NOTES.md has them in full): `[^&]` crosses the newline, so the pattern is line-blind and
greedy; a realistic repeating vocabulary would make one match swallow the file. Each key text is therefore unique per subject
(stem, then `stem_<base36 tag>`), and the only repeats are the planted duplicates. 119 matches < 302 planted pairs because
long-range spans swallow nearer pairs.

## Expectations, before / after

6,530 rows + header (6,531 lines) -> 6,672 rows: +142 = 71 patterns x 2 new subjects (throughput regime), 0 removed, 0 changed
(`git diff --numstat` 142/0). On the new subjects: 22 `match`, 120 `nomatch`, no oracle give-up, no fallback method used.
The six give-ups in the derive log (4 restored by `structural-alphabet`, 2 dropped for `email-nested-plus` on the 0.2 evil texts) are 0.2's, unchanged.

## Checks run (all green)

- `gen_subjects.py` 75 subjects, manifest unchanged.
- `gen_throughput_subjects.py`: 19 texts, the 17 earlier sha256s asserted, redos safety check OK; manifest committed = regenerated.
- `gen_patterns.py --check` 71 patterns; `gen_provenance.py --check` 71 rows; `gen_variants.py --check` 0 rows.
- `gen_expectations.py --check`: 6,672 expectations re-derive from libpcre2 10.46 2025-08-27 (dfa control: 6,668 backtracker-answered triples, existence+start agree on 5,130, span+count 1,327, 34 dfa errors all pre-existing 0.2 cells).
- `make check-schema`: 12 examples accepted, 104 sabotages rejected for the intended rule, 0 wrong; check_fields/check_rules OK (53 rules, 104 controls).
- NOT run (as instructed): `make check`, the full `check-harness`. The capability parts of check-harness that matter are exactly the generator/expectation re-derivations above.

## Owed / for the manager

1. Full `make check` after pcrec's suite. Expect check-harness's `check_manifests` and `check_expectations` to pass for capability (verified directly), and the generic gates that enumerate `bench/*/` to see 19 throughput texts.
2. The cell: `capability/dup-param-detect` x `t-qs-1m` / `t-qs-nearmiss-256k` joins the next pinned run on the usual roster. NOTES.md P21-P23 are stated; the quadratic failing path (~14 s / ~2.6 s at the oracle per find_all) is the cell-time hazard for the backtracking testees; a `CELL_CAP` decision is the manager's.
3. Worktree `worktrees/b172qs` is merge-ready; subjects dir is gitignored (regenerate with the two generators).
4. Design note for the reader: duplicates are line-blind and key texts are unique by construction. If pcrec wants a variant where common keys repeat across lines (the pattern then matches almost immediately and the file is swallowed by few huge matches), that is a different subject.
