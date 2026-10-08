# b127front report -- the public front page ([B127])

Branch `lane/b127front`. Nothing pushed, no GitHub API calls, nothing written to `store/`.

## PLACEHOLDER DATA

README.md, docs/methodology.md, docs/img/speedup_distribution.svg and docs/frontpage_provenance.tsv are generated from the **capability@0.1 slice** (pcrec `c4c70f2c`, 2026-10-05; competitors 2026-09-17..22), the one set with the full roster. The `litrun@0.1` region is the single other-set test. All of it is replaced by the manager's final run. The loss table's "Why" column reads "cause not yet analysed" everywhere: `docs/frontpage_why.tsv` is empty by design (see below).

## Command for the manager after the window

    cd ~/pcrec-bench/worktrees/<merged tree>   # or the main tree after merge
    setsid gnutimeout 3000 make frontpage > /var/tmp/frontpage.log 2>&1 ; echo "DONE rc=$?" >> /var/tmp/frontpage.log

(defaults: `FRONT_SET=capability@0.2 FRONT_PIN=255bcdd8`, other sets email-specimen@0.2 loglines@0.1 bounded@0.3 altwide@0.2 syntax@0.1 utf8@0.1 litrun@0.1). Then `make frontpage-check` (expects exit 0), `make check-frontpage`, `make viewer-data`, commit. Memory: one record's rows at a time, ~11 records per set; run detached. Measured here: the capability@0.1 slice plus litrun takes well under 5 minutes under `nice`.

## Charter vs committed

| Item | State |
|---|---|
| README sections 1-10 + "Second look" | README.md; generated regions headline/table/chart/losses/othersets, prose static |
| Generated headline sentence, per-competitor table, run date + pin | `headline`, `table` regions |
| SVG strip+box, log scale, 1x line, light/dark safe | docs/img/speedup_distribution.svg (opaque white background rect, fixed neutral/blue/orange palette; XML-parses; NOT viewed in a browser -- no renderer on the box) |
| Viewer link, index.html at site root | README; viewer/index.html (meta-refresh to viewer.html); all viewer paths relative (`data/...`), no absolute URLs, so a `/pcrec-bench/` prefix works |
| Where pcrec loses, grouped by family, why only when cited | `losses` region; family from bench/<set>/provenance.tsv; `docs/frontpage_why.tsv` (quote must be found verbatim in the cited committed file or the run aborts) |
| Methodology (engines, hw, timed axes, compile table, provenance, trials, correctness, caveats) | docs/methodology.md (generated: env, engines, trials, compile) |
| Fairness note | README "Fairness" |
| Reproduce / Status / How it was built | README; 0.2.0-beta verified (`255bcdd8:lib/pcrec.h`; `git describe` = v0.2.0-beta-1123-g255bcdd8f); pcrec default branch `main` |
| tools/frontpage.py, `--check`, `make frontpage` | done (+ `make frontpage-check`, `make check-frontpage`) |
| Unit test | tools/tests/test_frontpage.py, 16 checks pass (not wired into `make check`; manager's call) |
| .github/workflows/pages.yml | done: push to master touching viewer/** (and the workflow), workflow_dispatch; upload-pages-artifact@v3 + deploy-pages@v4 |
| LICENSE | RULED by Frank: MIT, committed on master (c135813); merged in, one-line License note at README foot. |
| CLAUDE.md updates | root, tools/, docs/, viewer/ |
| Provenance file | docs/frontpage_provenance.tsv (section, set, testee, record path, timestamp, version, machine, content hash) |

## Metric as implemented (deviations flagged)

- Cases are PLAIN-form cells only (the whole-subject form is a separate artifact for a few patterns). Say so if you want it included.
- A case needs a numeric set-grain median both sides (reduce_set_cell: any expectation-failing subject voids the cell). Wrong/gave-up/unsupported/not-measured are counted; unsupported includes `did-not-compile` refusals. A pair failing on both sides is attributed to the pcrec side.
- The universe is every (pattern, regime) any selected testee has a cell for, so denominators are identical across competitors.
- Compile table: median over patterns of each pattern's median-over-trials `cost.total_ns`, plain form, plus the median per-pattern ratio over patterns both compiled.
- Competitor testees: every non-pcrec testee with a `measured` record for the set on pcrec's machine, latest each. That includes both re2 configs and all three libpcre2 modes, so "all pairs" counts them separately.
- Rounding: Decimal half-even, 3 significant digits for ratios, 1 decimal for percentages.

## Findings worth knowing

- The brief says the other sets measured "only PCRE2 and Rust regex". The store disagrees: utf8@0.1 also has oniguruma, re2 and vectorscan records. The sentence under that table is therefore generated from the records ("competitors measured: ...") rather than typed.
- litrun@0.1 test row: 14 of 42 pairs excluded as "pcrec side: not measured" (the pcrec-auto record has no cell for those keys while the libpcre2-jit record does). Not investigated; check after the real run that this is expected.
- On the slice, vectorscan-nosom dominates the worst-loss list on throughput regimes (e.g. x0.0000351). Its driver stops at the first match (testees/vectorscan/CLAUDE.md), so it does less work there; the page says so beside the table and in the methodology caveats.
- Win-rate headline on the slice: 753 of 850 pairs (88.6%), ties 2, losses 95, 302 excluded. Compile: pcrec median 224 ms vs 2.68 us..1.07 ms for the others; shown.

## Why "cause not yet analysed"

The committed ledger statements about these patterns concern older pins and the capability@0.1 set; the final worst-cell list at 255bcdd8 on capability@0.2 does not exist yet. Citing an old-pin cause against a new-pin number would be a guess. After the window, add rows to docs/frontpage_why.tsv (pattern_id, engine, regime, cite, quote); the generator refuses a quote it cannot find.

## Could not verify

- The SVG's appearance in GitHub light and dark (no renderer on this box; colours chosen for an opaque white plate).
- That GitHub Pages serves viewer/ correctly (no API calls allowed); the relative-path claim is from reading viewer.html for absolute URLs/fetch (none).
- Hand-written methodology statements about engines were taken from testees/*/CLAUDE.md greps (re2/rust lack backrefs/lookaround; vectorscan nosom stops at first match; pcre2-dfa is nfa-simulation); the re2-longest "excluded as wrong answer" sentence rests on the slice showing 3 wrong-answer cells for that config, not on a per-pattern audit.
