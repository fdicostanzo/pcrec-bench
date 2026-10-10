# b134support report ([B134] part 2, front-page pattern-support table)

Branch lane/b134support. Files: tools/frontpage.py (`support_counts`, `render_support`, `support` region), tools/tests/test_frontpage.py, README.md (new "## Pattern support" section + generated region, after the chart caption, before "Explore the full results"), tools/CLAUDE.md. No change to store/, harness, methodology.md, provenance TSV (same records as the headline; `make frontpage-check` clean).

## Columns (all from the plain-form compile rows plus the set cells of the headline records)
- Patterns: compile rows on the plain form, one per pattern (71). Regimes and forms collapse to the pattern.
- Compiled: `compile_outcome == compiled`, count and % of Patterns. Cross-checked at generation: it must equal the methodology compile table's "Patterns compiled" (`len(compile_ns)`), else the generator exits.
- Unsupported feature: `unsupported-by-declaration`. Refused to compile: `did-not-compile`. The two plus Compiled must sum to Patterns (fail-loud). The records distinguish these two outcomes, so both are shown; they do not separate "size limit" from other refusals, so no methodology breakdown was added (would be guesswork).
- Verified correct (of compiled): compiled patterns whose every (pattern, regime) cell in the headline universe has a verified numeric median, i.e. no wrong answer, no give-up, an oracle expectation present. Six columns instead of five because unsupported and refused are separate.

## Cross-checks
Compiled counts equal the methodology table for all 11 rows (69/65/71/71/69/45/45/48/41/47/44). They do not equal the README table's Excluded column or the Excluded breakdown's "unsupported or refused": that counts (pattern, regime) pairs, attributes a failing pair to the pcrec side first, and includes cells excluded for other reasons; the new table counts patterns per engine independently. Not a disagreement, different units.
Verified correct is below 100% for PCRE2 (95.8%) even though it compiles everything: 3 patterns give up on PCRE2 JIT, plus the one pattern with no oracle expectation counts against every engine. Leftmost-longest RE2 and TRE lose more to the semantics difference (linked to methodology#engines).

## Number identity
`git diff README.md` is 17 inserted lines, 0 deleted: every pre-existing number, table and sentence unchanged. methodology.md and the provenance TSV did not change.

## Validation
`make check-frontpage` all PASS (new: denominator, compiled/unsupported/refused split, correct counts wrong/give-up/unmeasured against, percentages). `make frontpage` ran detached, rc=0; `make frontpage-check` clean. Markdown not rendered on GitHub here.

## Departures
Six columns (brief suggested ~5). No methodology breakdown (see above). Section heading "Pattern support".

## Charter-vs-committed
Renderer + region + README section + tests + CLAUDE.md + regeneration + check: committed. Nothing OWED.
