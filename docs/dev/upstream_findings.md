# Upstream findings — behaviour of OTHER engines observed by the bench

Findings about engines other than pcrec, each with the record that shows
it (pcrec D35 style: cite the record id and the row; the raw trials are
the transcript). Findings about pcrec itself go to the pcrec manager for
pcrec's known_issues.md, never here. Status vocabulary: OBSERVED (seen in
records) → UNDERSTOOD (cause explained by reading the engine's source or
a maintainer's answer) → REPORTED (filed upstream) / NOT-A-BUG.

## U1 — libpcre2 10.46 JIT: 60 s per-subject timeout on the subroutine-factored email pattern over 1 MB of `a`, where the interpreter answers in ~18 µs (OBSERVED 2026-08-25)

Record `email-specimen@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260825T062944Z`,
pattern `factored`, subject `t-c-long-atom-run` (1,048,576 × `a`),
regime large-subject-throughput: outcome `timed-out` on 5/5 trials
("the per-subject alarm fired", 60 s each). The interpreter record
(`...interp-caps-simdna__...T062213Z`) answers the same cell with
elapsed 6,785,472 ns over 381 iterations (17.8 µs/iteration) — a clean
nomatch. The hand-inlined `orig` pattern is fine on BOTH testees for the
same subject. Reading (unverified): the interpreter's start-of-match
optimizations (the START-OPTIMIZE prescan pcrec's K34 work met) reject
the subject before matching; the JIT enters the `atom+(\.atom+)*`-shaped
backtracking through the subroutine calls and does not return within
60 s. Next: reproduce with pcre2test (`jit`, `no_start_optimize`) to
separate the two hypotheses; if the JIT genuinely lacks the prescan on
call-bearing patterns, that is reportable. Reporter note: the reporter
labels this cell "(other)" — `timed-out` needs its own label (OD-B11).

## U2 — libpcre2 10.46 JIT does NOT get the interpreter's whole-subject required-code-unit dismissal on a 1 MB failing subject: 2.4-3.2 ms where the interpreter answers in 18 µs (OBSERVED 2026-08-25 at 692c2e8, re-observed 2026-08-28 on `email-specimen@0.2`)

Records `email-specimen@0.2__libpcre2_10.46_{interp,jit}-caps-simdna__budu-ryzen1600__20260828T14{5051,1718}Z`,
pattern `orig`, subjects `t-b-no-at`, `t-c-long-atom-run`, and the
non-periodic `t-e-prose-no-at` (1 MB each, no `@`; `@` is the
pattern's required code unit per `pcre2_pattern_info`). Interpreter:
17,985 / 17,957 / 18,077 ns per call — a memchr over the subject and a
clean nomatch (0.017 ns/byte). JIT: 2,563,985 / 2,819,272 / 3,157,857
ns — the full scan (2.4-3.0 ns/byte), 142-175× the interpreter on the
same failing text. First stated in pcrec's inbox I-7 §1 (2026-08-26)
from the 0.1 records. Reading (unverified against the source): the
required-code-unit check (`req_cu`) is applied in `pcre2_match`'s
start-of-match phase and is not part of the JIT's compiled prologue, or
is capped by REQ_CU_MAX (5000) there while the interpreter's memchr
path is not. Next: `pcre2test` with `jit` vs `no_jit` and
`no_start_optimize` on the same subject; if the JIT genuinely lacks
the check on a plain (non-call-bearing) pattern, that is reportable.
Status: OBSERVED.

## U3 — libpcre2 10.46 JIT pays ~2.8 ms/MB MORE on prose with 496 sparse addresses than on address-free prose, where pcrec's DFA pays the same on both (OBSERVED 2026-08-28, `email-specimen@0.2`)

Same records; `orig`, `t-d-prose-sparse-addrs` (1 MB generated prose,
496 valid addresses, seed 20260828) vs `t-e-prose-no-at` (the same
generator, no `@`). JIT: 5,966,412 vs 3,157,857 ns (5.69 vs 3.01
ns/byte, +2.81 ms); pcrec DFA (auto): 3,138,983 vs 3,106,092 (2.99
vs 2.96 — bytes, not matches); interpreter 93,875,421 vs 18,077 (the
required-unit check turns off once `@` is present, and the backtracking
on `word.` near-miss tokens costs 89.5 ns/byte). 496 find-all matches
cannot explain 2.8 ms (5.6 µs per match), so the JIT's extra cost is
per NEAR-MISS token (every `word.`/`word,` before a `@`-bearing address
is found), the same backtracking shape the interpreter pays 30× more
for. Status: OBSERVED; a pcre2test `find-all` count over t-d with
`jit` timing per iteration would separate per-match from per-near-miss
cost.

## U4 — libpcre2 10.46 JIT is 1.8× SLOWER than its own interpreter and 15× slower than pcrec's DFA on the HTTP-access-line pattern over log text (OBSERVED 2026-08-28, `loglines@0.1`)

Records `loglines@0.1__libpcre2_10.46_{interp,jit}-caps-simdna__budu-ryzen1600__20260828T1{50050,50927}Z`,
pattern `http-5xx` = `"(?:GET|POST|PUT|PATCH|DELETE|HEAD) [^ "]+ HTTP/1\.[01]" 5[0-9]{2}\b`,
short-subject-search over 112 subjects (set ns/call): jit 104,980,
interp 57,326, pcrec-auto 7,013 (memchr-bounded on the first byte `"`).
At 1 MB: jit 791-819 µs on all three flavours (including the syslog
subject with NO `"` at all, where the interpreter and pcrec both answer
in 17.6-17.8 µs — the JIT scans the whole subject regardless), interp
206 µs / 17.8 µs / 1,228 µs. Reading (unverified): the JIT's start
optimization for a pattern beginning with a literal `"` followed by an
alternation is a per-position attempt with the alternation unrolled,
not a memchr for `"`; the interpreter's start-of-match memchr is what
makes it faster. Status: OBSERVED; `pcre2test` with `jit` /
`no_start_optimize` separates the hypotheses.

## U2 — libpcre2 10.46 JIT is SLOWER than the interpreter on pure-scan find-all rows where the start-code dismissal does the work (OBSERVED 2026-08-30)

Records `bounded@0.1__libpcre2_10.46_jit-caps-simdna__budu-ryzen1600__20260830T092238Z`
and `...interp-caps-simdna__...T032115Z`, regime large-subject-throughput
(4 KB / 16 KB / 64 KB letters + 16 KB digits, find-all), set medians:
`csv5` (`\d{1,5}(?:,\d{1,5}){4}`-class shape; see bench/bounded/patterns)
jit 3,151 ns vs interp 1,729 ns (×1.82); the floor pattern `:` jit 4,052
vs interp 1,710 (×2.37). On these subjects the pattern's required/first
code unit never occurs, so the whole call is the start-of-match scan; the
JIT's entry cost exceeds the interpreter's memchr-class dismissal. Ledger
docs/dev/ledgers/2026-08-30-bounded-0.1-first-sample-36d5963.md §2.7.
Reading (unverified): JIT call overhead + its own scan loop vs the
interpreter's `memchr`/first-code-unit fast path. Not a bug; a shape
where "jit = faster" does not hold. Next: none owed.

## U3 — libpcre2 10.46 compiles a bounded REPEATED GROUP by replication (~51 B per repetition; `(?:a|[b-z]){0,1024}` = 52,377 B, interp compile 33,030 ns, jit 108,590 ns) where a repeated CLASS is count-independent (197 B flat from `{0,256}` to `{0,65535}`) (OBSERVED 2026-08-30; NOT-A-BUG)

Records as U2; the compile-cost tables (`eager-jit`, `interpretive`) in
reports/2026-08-30-bounded-0.1-*-first-sample-36d5963.md; ledger §1.5.
`nest2-64` 1,298 B and `nest3-16` 4,754 B likewise grow with the count.
bench/bounded/oracle_limits.tsv predicted this from the oracle's own
first refusal per skeleton. Documented PCRE2 behaviour (a repeated group
is unrolled up to the pattern-size limit); recorded here because it is
the comparison point for pcrec's [ART-SIZE] size term (pcrec-vm does not
replicate: 22,120 B for the same pattern).
