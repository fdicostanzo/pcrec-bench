# Expectation verification methods (v1, [B125])

Every row of a sub-bench's `expectations.tsv` carries a `method` column and
the oracle version. Until capability@0.2 every row of every set was
`libpcre2-differential`. This note is the vocabulary and the rules.

| method | engine | speaks for | declared by |
|---|---|---|---|
| `libpcre2-differential` | `pcre2_match` (backtracker) of the pinned libpcre2 | every triple it answers | `[expectations] default_method` |
| `libpcre2-dfa-fallback` | `pcre2_dfa_match` of the SAME libpcre2 | only a triple the backtracker GAVE UP on (match/depth limit), and only what rule 1/2 below allow | `[expectations] fallback_method` |

A set that declares no `fallback_method` is derived exactly as before; the
give-up of the backtracker drops the triple, listed by name on stderr.

## The fallback's restrictions (code: `pcrecbench/expectations.py`)

`pcre2_dfa_match` reports the LONGEST match at the leftmost start, records no
captures, treats atomic groups and possessive quantifiers as plain ones, and
refuses backreferences/recursion. So it may state only:

1. NOMATCH, for a pattern whose DFA reading is exact (`dfa_features(text)`
   empty: no backreference, recursion, atomic group, possessive quantifier,
   `\K`, `\C`, `\G`, verb, conditional, callout, branch reset, free-spacing,
   `\Q`; anything the scanner cannot parse counts as ineligible).
2. A MATCH, only when every match provably starts at 0 and ends at the
   subject end (`fully_anchored`: leading `^`, trailing `\z` or `$` at depth
   0, no top-level alternation, no multiline flag, and for `$` a subject not
   ending in `\n`). The span is (0, N), a find-all count is 1; the dfa's own
   reported span is asserted equal to it.

Only `search_short` and `throughput` are served. Anything else stays DROPPED
and is listed by name with the reason.

THE WORK BUDGET. The dfa's workspace is capped (`oracle_pcre2._DFA_WS_MAX`,
16000 ints): a triple that needs more is declined, deterministically. A
wall-clock budget would make the file irreproducible. Measured reason: on
nested quantifiers the dfa is about n^2.8 (`^(([a-z]+)*)+$` over a^n + `!`:
0.26 s at n=1000, 14 s at n=4000), so it cannot answer the 60 KiB
near-misses; those triples stay dropped by name (see the lane report).

## The control (shares no matching algorithm with what it checks)

Over every triple the BACKTRACKER answered, for every DFA-readable pattern,
`DfaControl` requires the dfa's existence answer and leftmost start to equal
the backtracker's, and, where `fully_anchored` holds, the span and the
find-all count too. It runs on every derivation of a set that declares a
fallback (`--no-control` skips it) and a disagreement fails the run, nothing
written. Triples whose dfa work exceeds the budget are counted as `dfa
errors` (declined, not disagreements). The summary line prints the counts.

## Readers

No reader restricts the method column: `subbench.Expectation.method` is
carried, never compared. `subbench.FALLBACK_METHODS` validates the sidecar key.
