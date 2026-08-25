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
