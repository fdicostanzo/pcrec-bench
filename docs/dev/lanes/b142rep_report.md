# b142rep -- report wave, [B142] first window at pcrec 9ae59f5d4 (abi 84)

Branch lane/b142rep. Reporter v28. No timing, no store write, nothing run on the box beyond report/interpret (nice 10, detached, sequential).

## Commands (exact)

Driver (scratch, not committed): /var/tmp/pcrecbench/b142rep/gen.py, which reuses `scripts/regen_reports.py`'s `build()` and the reporter's own renderers (same path as `regen_reports.py`; sequential detached chain /var/tmp/pcrecbench/b142rep/chain.sh, log `log`, ended `DONE all`, every group rc=0). Per group the CLI-equivalent query is:

    pcrecbench report --subbench <set> --version <ver> --machine ryzen7700x \
      --since 2026-10-25T19:30:00Z --until 2026-10-26T08:00:00Z \
      --testee <id> [--testee <id> ...] [--grain set|subject|subst]

Files per set group: `.tsv`, `.md`, `.matrix.tsv` (set grain), `.subject-grain.md` (subject grain), `.subject-grain.tsv` (`--subject-grain-slice` form, as in the 2026-10-13 precedent). Sentinel: no subject-grain pair, no precedent. subst: `--grain subst` `.tsv` + `.md` (no matrix/subject-grain exist for it).

Rosters (explicit `--testee`): P6=pcrec_6b2dbd3e_, P9=pcrec_9ae59f5d4_.
- capability-0.2: P6/P9 auto-caps-simdna, P6/P9 auto-nocaps-simdna
- loglines-0.1, litrun-0.1, syntax-0.1, email-specimen-0.2, bounded-0.3: P6/P9 auto-caps-simdna
- utf8-0.1: P6/P9 auto-caps-simdna_utf8
- sentinel-0.1: libpcre2_10.46_jit-caps-simdna, P6 auto-caps, P9 auto-caps, P9 auto-nocaps, re2_11.0.0_default-caps-simdna, rust_1.13.1_default-caps-simdna
- subst-0.1: no `--testee` (all 15 records in the window)

Sidecars, per the skill, repo-relative, run from the worktree root, no `--predictions` (no prediction file states anything for this window), `--subject-grain` where the slice exists, then the same command to stdout byte-compared (`cmp`):

    python3 -m pcrecbench interpret reports/<name>.tsv --index store/index.tsv [--subject-grain reports/<name>.subject-grain.tsv] --render --out reports/<name>.interpretation.md

Determinism: identical for all 8 set groups. subst-0.1: REFUSED BY NAME, rc 2: `interpret: ...subst-0.1-...tsv: unexpected column list ['section','tier','subject','case',...]` -> no sidecar (catalogue 3.20 / interpret v2 do not read the subst TSV; a catalogue item, not patched).

## Files (reports/, base `2026-10-26-<set>-ryzen7700x-first-9ae59f5d4`)

capability-0.2, loglines-0.1, litrun-0.1, syntax-0.1, utf8-0.1, email-specimen-0.2, bounded-0.3: `.tsv .md .matrix.tsv .subject-grain.md .subject-grain.tsv .interpretation.md`. sentinel-0.1: `.tsv .md .matrix.tsv .interpretation.md`. subst-0.1: `.tsv .md`. Largest: syntax `.subject-grain.md` 5.1 MB, capability `.subject-grain.tsv` 6.9 MB.

## Record counts / header facts (from each .tsv header)

| group | index rows matched | records used | notes |
|---|---|---|---|
| bounded-0.3 | 2 | 2 | null_band 126 null of 126 cells |
| capability-0.2 | 5 | 4 | superseded 1 (the P6 nocaps `inconclusive-spread` record; newest-wins keeps the re-measure); dropped_triples: 2 triples / 40 rows (email-nested-plus x t-evil-match-60k, x t-evil-nearmiss-16k); null_band 246 null of 276 |
| email-specimen-0.2 | 2 | 2 | null_band 9 of 9; strata ok=0 insufficient=5 empty=4 |
| litrun-0.1 | 2 | 2 | null_band 40 of 42 |
| loglines-0.1 | 2 | 2 | null_band 22 of 22 |
| sentinel-0.1 | 22 | 6 | superseded 16 (sentinel was run repeatedly in the window; newest per testee kept -- NOT checked which regimes/why); null_band 14 of 15 |
| subst-0.1 | 15 | 15 | 10 library + 5 tools records, all measured/pinned, trial agreement `agree` on all |
| syntax-0.1 | 2 | 2 | null_band 236 null of 243 |
| utf8-0.1 | 2 | 2 | null_band 138 null of 138 |

Every set group's header has `null_band: pcrec 6b2dbd3e -> 9ae59f5d4: field program_sha256` and `x13_rules: v1.4 ... mixed_x13: False`; no "NO NULL BAND" line, so no identity census was written. No refusal or warning from the reporter in any run (log has none). Sentinel's identity criterion is stated in its null_band row (v3 on 15 cells, v2 on 0, disagreements 0). Not checked for the other groups' criterion lines.

## Facts for pcrec-main (copied from the reports' `rank` section, `median_ns` rows of the 9ae59f5d4 testee; "verdict" = the row's delta_verdict vs 6b2dbd3e; all listed rows are `same program` unless marked; key = file, pattern | regime | form)

Shown: verdicts outside "unchanged (within spread)" of >= x1.10 only; smaller moves are in the .tsv (counts of moved median rows: bounded 42, capability 64, litrun 8, sentinel 3, syntax 69, utf8 63, email 0, loglines 0).

bounded-0.3 (testee P9 auto-caps; 15 rows >= x1.10; 6b2dbd3e-only comparator, no non-pcrec testee in the group)
- cls-upto-256 | short-subject-search | plain: faster x1.20 (med 470.0 ns); | large-subject-throughput: faster x1.19 (83160.2)
- cls-upto-512 | large: faster x1.17; cls-upto-128 | short, large: faster x1.12 each; cls-upto-1024/2048/4096/8192/16384 | short: faster x1.15 each; cls-upto-2048 | large: faster x1.15; grp-upto-1024 | short: faster x1.16
- line-80 | match-compliance | whole-subject ("separate artifact"): slower x1.18 (1758.8)
- cls-upto-4 | large: slower x1.11 (134175.9)

capability-0.2 (auto-caps and auto-nocaps; 30 rows >= x1.10; no non-pcrec testee in the group)
- tail-space-eol | large-subject-throughput | plain: slower x6.09 (caps, med 72939.2) / x6.12 (nocaps, 72946.9); same program; | short-subject-search: faster x1.48 both
- faster: tail-ext-lower-txt | large x1.39 caps / x1.44 nocaps, short x1.26 both; wild-semdiv-dollar-trailing-newline-pcre2 | large x1.42 both, short x1.32 both; tail-dotstar-txt | large x1.32 both, short x1.28 both; tail-digits-eol | large x1.28 caps / x1.27 nocaps, short x1.22 caps / x1.21 nocaps
- slower: wild-semdiv-altorder-foo-foobar-rustregex | large x1.30 (caps, 479593.3); evil-alt-nested | large x1.22 (nocaps), short x1.13 (nocaps); file-ext-order | large x1.18, short x1.10 (caps); router-prefix-order | large x1.14 (caps); phone-list-nested-plus | short x1.11 (caps); wild-validator-ipv4-owasp | large x1.11 (caps); keyword-prefix-order | short x1.10 (caps); wild-waf-crs-942360-concat-sqli | large x1.10 (nocaps)

litrun-0.1: ctrl-abc-dollar | large faster x1.32, | short faster x1.30 (6 `separate artifact` rows also moved, all < x1.10)

sentinel-0.1 (P9 auto-caps vs jit/re2/rust): 
- LOSES to best non-pcrec: wild-waf-crs-942360-concat-sqli | short-subject-search | plain: P9 median 2685.2 ns (rank 4) vs rust_1.13.1 2133.7 (rank 1), x1.26 -- the only cell where a non-pcrec testee's median is below P9 auto-caps in my scan (scan compared every non-pcrec testee's `rank` median per cell against P9 auto-caps)
- moved: wild-semdiv-dollar-trailing-newline-pcre2 | short: faster x1.32 (229.4); ipv4-near-miss | short: slower x1.15 (249.0)

syntax-0.1: faster anc-dollar | large x1.35, short x1.28; anc-z-uc | large x1.30, short x1.27; slower qnt-poss-quest | short x1.24, large x1.23. (32 `separate artifact` rows moved, none >= x1.10.)

utf8-0.1 (`_utf8` testee): slower lit-anchored-run | short x1.21, large x1.19; ci-greek-run | short x1.11; ci-kelvin | short x1.11; cls-s-nbsp | short x1.10; faster cls-neg-allhigh | large x1.11.

email-specimen-0.2, loglines-0.1: no moved rows (all "unchanged (within spread)"); the loglines/email cells have 9/22 cells all inside the null band.

subst-0.1 (`ratio_vs_baseline`, library tier baseline libpcre2 jit: values > 1 = faster than baseline, e.g. interp 0.65 at higher ns; columns from the TSV `cell`/`summary` rows; acc-main / acc-small agree within 0.01-0.1):
- pcrec_9ae59f5d4 auto-caps, acc-main: 1-literal 1.097; 2-rare 0.375; 3-dense 2.147 (vm-caps 2.566); 4-reorder 1.175; 5-mask-ipv4 1.469; 5b-mask-email 0.631 (summary best-other = rust_1.13.1, pcrec-vs-best-other 0.316); 6-upper 1.410; 7-url-tld-fix 0.257.
- Cases below 1.0 vs the jit baseline: 2-rare, 5b-mask-email, 7-url-tld-fix (acc-small the same: 0.423, 0.642, 0.261). All gates `agrees`.

## What I did NOT read
Neither the .md renderings, the subject-grain files, nor the interpretation sidecars' content (I read only the stamp of one and the determinism result); the `compile`, `compile_stamp`, `d119`, `query_yes_beats_nocaps`, and `null_band` rows beyond sentinel's three; any mover below x1.10; the tools-tier subst rows; why sentinel superseded 16 records; whether any sentinel cell had a pcre2-jit rank above P9 outside the `rank` section scan. No interpretation of causes is made.

## Charter vs committed
1. Nine groups named `2026-10-26-<set>-<ver>-ryzen7700x-first-9ae59f5d4.*`, `--machine`, explicit since/until: committed (51261845).
2. subst via `--grain subst`: committed (.tsv, .md).
3. Detached sequential nice'd runs with log + marker: done (/var/tmp/pcrecbench/b142rep/log, `DONE all`).
4. Sidecars + determinism: 8 of 9 committed; subst-0.1 OWED -- refused by name (owner: catalogue/interpret; trigger: interpret learning the subst TSV).
5. reports/CLAUDE.md entry: committed.
6. This report: committed with the tables above.
Reports/CLAUDE.md note: `scripts/regen_reports.py` would not regenerate a `--grain subst` group (it reads grain via `grain: (\w+)` and calls the set renderer paths); not tested.
