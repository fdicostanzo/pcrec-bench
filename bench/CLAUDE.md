# bench/ — the sub-benches

One directory per sub-bench (harness contract §2, requirements §5): a
self-contained unit with a GOAL, its canonical patterns, its
deterministically generated subjects, its oracle-verified expectations,
and its per-engine notes. Versioned as a unit; records compare only
within one `id@version`.

`pcrecbench/subbench.py` is the loader and the ONE place the regime →
subject mapping and the two regime spellings (the directory's
`match`/`search_short`/`throughput` and the record schema's
`match-compliance`/`short-subject-search`/`large-subject-throughput`)
are translated.

| directory | what it is |
|---|---|
| `email/` | the RFC 5322 specimen: `orig.rx` (hand-inlined) and `factored.rx` (the same language via `(?&name)` calls), 85 short subjects + five 1 MB throughput subjects (three periodic + two generated-prose non-periodic, [B17]/I-10) |
| `loglines/` | LOG-LINE SEARCH over mostly-failing text ([B11.1], inbox I-7 §1): ten patterns operators grep logs with + the floor, 112 chunks of mixed-format log text at 279-3772 B (~93 % of the member cells `nomatch`) and a 16 KB - 1 MB size sweep in three flavours. Shaped around ONE axis -- whether PCRE2's required-code-unit dismissal is available for a pattern -- with three patterns where it is not available at all as the control; the measurement pcrec's [OPT-5] is built or not on. Declares `search_short` + `throughput` only, and `short_search_max_bytes = 4096` |
| `bounded/` | BOUNDED REPEATS on both axes ([B11.4]): ten everyday bounded shapes (`\d{4}`, `[0-9a-f]{32}`, `.{8,64}`, `.{80,}`, a dotted quad, a CSV record, and a bounded lazy gap before a `\b` alternation at counts 64 / 256 / 1024 + its greedy twin), a nine-pattern SHORT-RUN DIGIT FAMILY (`\d{k}` and `\d{1,k}` at k = 2 .. 32, @0.3/[B27] -- `year4` shaped into the ladder the per-run scan-edge boundary is read off) and a twenty-three-rung COUNT LADDER (`[a-z]{0,n}` for n = 4 .. 65535 -- fifteen factor-of-2 rungs to PCRE2's own ceiling: the @0.2/[B21] KNEE-bracketing ladder plus @0.3's four LOW rungs, with `[a-z]{0,1024}` beside the group body `(?:a|[b-z]){0,1024}` as the group-vs-class pair -- the open and lazy forms, two- and three-deep nests, an ambiguous letters nest) + the floor; 49 generated short subjects (fields with near-misses that fail at the last repetition, ≤ 256 B lines of near-miss ops prose, and class runs on every rung: letters 4 .. 1024 B, digits as a 1 .. 33 length ladder) and five large runs (a small and a large on BOTH content axes since @0.2) in a `throughput` regime that is the ladder's top rungs under find-all, NOT a size sweep. The give-up axis is the COUNT: the predicted first pcrec refusal (the abi-11 emitted-size cap) is at the 32768 rung, and the oracle's own edges per skeleton are a committed, re-derived table (`oracle_limits.tsv`). `short_search_max_bytes = 258` -- which since @0.3 is also the line that makes a long run MATCH-ONLY (`subjects_for()` filters the search band by it and does not filter `match`), the whole mechanism behind the STEP 2 acceptance cells |

| `altwide/` | WIDE ALTERNATIONS on both axes ([B11.2]): an eight-rung WIDTH ladder of nested slices of one word pool (`w-8` .. `w-2048` over 3-12 byte branch literals, `s-2048`/`s-4096` over 3-6 byte ones -- libpcre2 itself REFUSES 4096 branches of 3-12 byte words, "regular expression is too large", so the short pool is how the brief's 4096-way rung is reachable and `s-2048` beside `w-2048` is the controlled length pair), five STRUCTURE arms at two widths (one shared first byte / a shared 3-byte prefix / four first bytes / a shared SUFFIX -- the only patterns here PCRE2 gives a required code unit / first bytes spread over all 26), an ORDER control pair (`srt-512` is `w-512`'s own branches sorted by first byte: identical bytes, trie and answers, `max_first_run` 28 against 2), three wrappers (`(?i)`, `{1,3}` -- the bridge to `bounded` -- and `\b...\b`) and the floor. 38 short subjects whose prose background is BRANCH-FREE by construction and asserted per subject, with twelve carrying one branch at a designed POSITION and branch INDEX (the leftmost-first arm), and four large prose subjects crossing hit DENSITY (0 / 1 per 8 KB / 1 per 128 B) with SIZE (128 KB, 512 KB). The patterns are DERIVED and committed (`gen_patterns.py --check`) because `s-4096` is 24 KB of alternation. The give-up axis is the WIDTH, and the oracle's own edges per skeleton are a committed, re-derived table (`oracle_limits.tsv`). `short_search_max_bytes = 512` |
| `syntax/` | THE SYNTAX CENSUS ([B36], inbox I-42, 2026-09-05): ninety-five patterns in eighteen mechanism families, ONE construct each in an otherwise plain body, ENUMERATED from pcrec's `--list-syntax` registry at our pin (`list_syntax_334fd10e.tsv`, the seed, copied verbatim; `coverage.tsv` is DERIVED from the pattern table x the seed and `gen_patterns.py --check` fails BY NAME on any seed row no pattern covers and no reason excuses -- the seed enumerates and shapes nothing, R-BENCH-4). Anchors, assertions, classes, quantifiers with the possessive suffixes and their control, groups (atomic, comment, branch-reset, callout), alternation, backreferences four ways, lookaround, a conditional, recursion and subroutine calls eight ways, ten option settings, escapes, `\R` `\X` `\C`, `\p{L}` in byte mode, two verbs, an extended class, `lit-cat` as the literal every `cat`-language spelling is read against, the five FOLD-PAIR WITNESSES (`(?i)cat`, `(?i)c[aeiou]t`, `c[aA]t`, its non-pair control `c[ac]t`, `c[a-zA-Z]t` -- the abi-23 [FORM-CHAR] shapes no other set carries), and the floor; 30 typed FIELDS (one construct's whole-string hit or semantic edge each) + 12 typed LINES of one vocabulary, and a 64 KB / 256 KB / 1 MB SIZE SWEEP of the same grammar. The OUTLIER RULE (R0-R7) and P1-P13 are stated in NOTES.md before any run; the output of the first sample is a ranked list of mechanism QUESTIONS (algorithmic first, SIMD last). Room for a utf sibling set (`bench/syntaxutf/`, the `encoding-bytes` tag) is documented, not built. `short_search_max_bytes = 256` |

`subjects/` and `throughput/` are GENERATED and gitignored; the
generators and their sha256 manifests are committed, and `make check`
regenerates both and requires the manifests to reproduce byte for byte --
for EVERY directory here, by enumeration (`tools/selfcheck.py`'s
`subbench_dirs()`, [B11.1]), never by name. The same pass re-derives each
sub-bench's `expectations.tsv` and any other `gen_*.py --check` table the
directory carries (`altwide` uses that same generic hook for its PATTERNS,
which are derived rather than typed; `syntax` uses it for its pattern
table's coverage of the registry seed and for its sidecar block), and smokes a real driver on each set's
floor pattern against the oracle. `altwide` is the slow one: its expectation
derivation is minutes rather than the sub-second the others take, because
the oracle is an interpreter and the widest rungs enter thousands of
branches per candidate start over 128 KB and 512 KB subjects.

A sub-bench's regimes need not see the SAME subjects. `subjects_for()`
filters `search_short` by `short_search_max_bytes` and applies no filter to
`match`, so a short-manifest subject longer than that cap is a MATCH-ONLY
subject -- which is how `bounded@0.3` got long-subject match cells for
pcrec's two-pass elision without a fourth regime or a schema change
(bench/bounded/NOTES.md, "What 0.3 added", argues the alternative it
declined).

A sub-bench declares WHICH REGIMES it exercises and a SUBSET is legitimate:
`loglines` declares no `match` regime (a chunk of log lines is not a
candidate string to validate whole -- its NOTES.md says so at length), and
`subbench.py`'s `subjects_for()`, `harness.run_cell()` and the record schema
(`regimes`, `minItems: 1`) all take the declared subset as-is. The
`throughput` regime need not be a SIZE sweep either: `bounded` declares it
for four runs sitting on its count ladder's top rungs ([B11.4]).

The manifests may carry COLUMNS BEYOND the contract's four: `periodic`
(inbox I-10) is the first. The loader reads the header and carries the
extras by name (`Subject.extra`, `Subject.periodic`); a four-column manifest
parses exactly as it always did. A sixth column is NOT accepted (the loader
takes 4 or 5), which is why `bounded` puts a subject's family and ARM into
the `description` column in a fixed spelling rather than a column of its own.
