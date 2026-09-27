# Upstream findings — behaviour of OTHER engines observed by the bench

Findings about engines other than pcrec, each with the record that shows
it (pcrec D35 style: cite the record id and the row; the raw trials are
the transcript). Findings about pcrec itself go to the pcrec manager for
pcrec's known_issues.md, never here.

[B103] (2026-09-27): this file is the NARRATIVE half of the
upstream-findings PIPELINE, `docs/design/upstream_pipeline_v1.md` — the
machine-read REGISTRY is `docs/dev/upstream/findings.tsv` (one row per
`## U<n>` section here, kept in sync by `tools/upstream.py check` /
`make check-upstream`), reproductions live under
`docs/dev/upstream/repro/U<n>/`, and draft notes to maintainers under
`docs/dev/upstream/notes/`. The STATUS LADDER (§3 there) is
OBSERVED → REPRODUCED/UNDERSTOOD (either order) → DRAFTED → APPROVED →
REPORTED → FIXED, with three terminal outcomes that are never sent —
NOT-A-BUG, KNOWN-UPSTREAM, STALE. Nothing here is sent to a maintainer
without Frank's per-note approval (APPROVED, recorded in this file).

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

**2026-09-27 ([B103], lane b103pcre2): UNDERSTOOD → DRAFTED.** Repro `docs/dev/upstream/repro/U1/`, PRESENT on 10.46 and a from-source 10.48. Ablation: the interpreter under `no_start_optimize` is as slow as the JIT; a no-subroutine control stays instant under JIT; the ~500,000-byte cliff is NOT a resource limit (jitstack 1 KiB vs 64 MiB identical, clean no-match, no error code at any size). Tracker/ChangeLog 10.47-10.48: nothing. In `notes/pcre2-2026-09-27.md`.

**2026-09-27: APPROVED by Frank and REPORTED** as https://github.com/PCRE2Project/pcre2/issues/1015 (one issue carrying U1/U2/U4; posted from the fdicostanzo account; body = notes/pcre2-2026-09-27.md minus our header, with one sentence corrected: the hand-inlined control under JIT is linear at a few ms per MB, not sub-millisecond).

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

**2026-09-27 ([B103], lane b103pcre2): REPRODUCED → DRAFTED.** ×86-160 (JIT vs interp) on 10.46 and 10.48; tracker/ChangeLog: nothing. In `notes/pcre2-2026-09-27.md`.

**2026-09-27: APPROVED by Frank and REPORTED** as https://github.com/PCRE2Project/pcre2/issues/1015 (one issue carrying U1/U2/U4; posted from the fdicostanzo account; body = notes/pcre2-2026-09-27.md minus our header, with one sentence corrected: the hand-inlined control under JIT is linear at a few ms per MB, not sub-millisecond).

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

**2026-09-27 ([B103], lane b103pcre2): REPRODUCED (1 MB grain) → DRAFTED.** The short-subject ×1.8 did NOT reproduce robustly at pcre2test's timing resolution (stated in the README); the 1 MB throughput form is ×23-34, PRESENT on 10.48. In `notes/pcre2-2026-09-27.md`.

**2026-09-27: APPROVED by Frank and REPORTED** as https://github.com/PCRE2Project/pcre2/issues/1015 (one issue carrying U1/U2/U4; posted from the fdicostanzo account; body = notes/pcre2-2026-09-27.md minus our header, with one sentence corrected: the hand-inlined control under JIT is linear at a few ms per MB, not sub-millisecond).

## U12 — libpcre2 10.46 JIT is SLOWER than the interpreter on pure-scan find-all rows where the start-code dismissal does the work (OBSERVED 2026-08-30)

(formerly the second U2 entry — this file used `## U2` twice; renumbered
2026-09-27 by [B103]'s pipeline migration, `docs/dev/upstream/findings.tsv`.)

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
where "jit = faster" does not hold. Re-measured at the 96e44c2 window
(2026-08-30, the same binaries): csv5 3,151 vs 1,723 ns (×1.83), floor
4,063 vs 1,716 (×2.37) — stable. Next: none owed.

## U13 — libpcre2 10.46 compiles a bounded REPEATED GROUP by replication (~51 B per repetition; `(?:a|[b-z]){0,1024}` = 52,377 B, interp compile 33,030 ns, jit 108,590 ns) where a repeated CLASS is count-independent (197 B flat from `{0,256}` to `{0,65535}`) (OBSERVED 2026-08-30; NOT-A-BUG)

(formerly the second U3 entry — this file used `## U3` twice; renumbered
2026-09-27 by [B103]'s pipeline migration, `docs/dev/upstream/findings.tsv`.)

Records as U12; the compile-cost tables (`eager-jit`, `interpretive`) in
reports/2026-08-30-bounded-0.1-*-first-sample-36d5963.md; ledger §1.5.
`nest2-64` 1,298 B and `nest3-16` 4,754 B likewise grow with the count.
bench/bounded/oracle_limits.tsv predicted this from the oracle's own
first refusal per skeleton. Documented PCRE2 behaviour (a repeated group
is unrolled up to the pattern-size limit); recorded here because it is
the comparison point for pcrec's [ART-SIZE] size term (pcrec-vm does not
replicate: 22,120 B for the same pattern).

## U5 — libpcre2 10.46's INTERPRETER is quadratic on balanced-paren recursion, against a match count that is linear in subject size (OBSERVED 2026-09-07, `syntax@0.1` first sample, d34c9131; lane b36read, ledger docs/dev/ledgers/2026-09-07-b36-syntax-first-d34c9131.md §9 Q9)

`libpcre2_10.46_interp-caps-simdna` on the recursion family's throughput
runs (64 KB / 256 KB / 1 MB): per-byte cost **870.4 → 2,061.6 → 8,704.8
ns/B** (R7 ratio 10.0-10.4× across a 16× size range — the family that
should scale linearly does not), set total 9.7 s for the 1.3 MB sweep,
×109 the backref family's cost on the same subjects. pcrec's `auto`
route does not show this shape (byte-bound, no recursion re-entry cost
per byte). Also observed on the same family: `(?+1)` costs its three
verified-answer-identical spelling twins ×13.88 on the search regime
under the interpreter (×2.24 under the JIT), where pcrec's `auto` makes
the four call spellings free to ×1.001 — i.e. the interpreter's
recursion dispatch is spelling-sensitive where an AOT compiler's is not.
Reading (unverified): each `(?R)`/`(?+1)`-style re-entry likely re-walks
or re-allocates state proportional to the CURRENT match depth/position
rather than O(1) per entry, giving the observed O(n²) on subjects that
are mostly one long recursive run. Not chased further here — a read
lane's job was to surface it, not attribute it. Verified from six store
records (`store/records/syntax@0.1/*/*.jsonl`, commit 28cb034) via
`pcrecbench.reduce`'s own reduction, cross-checked against the rendered
report at the cited lines; not re-measured independently outside the
store.

**2026-09-27 ([B103], lane b103pcre2): NOT-A-BUG (pattern-inherent backtracking cost).** Four-way ablation in `docs/dev/upstream/repro/U5/`: on a balanced-only control subject (same seed) interp AND JIT are flat per byte; on the original (≈1 in 8 paren lines deliberately unbalanced) both are super-linear (interp ×9.2, JIT ×12.45 per byte for a 16× size step), and Oniguruma 6.9.10 shows the same shape. Each unbalanced `(` extends `[^()]*` through the rest of the subject under ANY backtracker. Not sent. (Side note: JIT needs jitstack > 32 KiB on the original; at default it returns PCRE2_ERROR_JIT_STACKLIMIT, correctly reported.)

## U6 — TRE 0.9.0's `high-byte-run` correctness gap is a REAL, REPRODUCIBLE property of `tre_regncompb`'s byte-mode matching, not a one-off — CONFIRMED across two independent samples one day apart (OBSERVED 2026-09-18, REPRODUCED 2026-09-19, `bench/capability@0.1`; lane b48read's ledger §5.4, lane b55extread's ledger)

**First sample** (2026-09-18, pcrec pin cf0962e3's window, record
`capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__
20260918T043931Z`): pattern `high-byte-run`, `large-subject-throughput`
regime, 3 subjects × 5 trials — `pass_rate 0.0000`, all 15 trials wrong
(`reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv`,
`excluded` section). `short-subject-search` regime, 75 subjects × 5
trials — `pass_rate 0.4800`, 195 of 375 trials wrong (same file). Two
further patterns wrong at the family-11-typical rate on the SAME
sample: `tag-pair-match` (`n_wrong=5`) and
`wild-waf-crs-942360-concat-sqli` (`n_wrong=5`), both
`short-subject-search`, both patterns TRE declares fully SATISFIED by
capability (neither is `unsupported-by-declaration` or
`did-not-compile`). First read in
`docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §5.4: "the
widest correctness gap of anything measured in this bench's history for
a capability-declared-satisfied pattern."

**Second sample** (2026-09-19, lane `b54extwindow`'s window, record
`capability@0.1__tre_0.9.0_default-caps-simdna__budu-ryzen1600__
20260919T033612Z` — the SAME testee_id, a fresh compile and match run a
day later): every number above reproduces to the exact trial count —
`high-byte-run` throughput `pass_rate 0.0000`, `n_wrong=15`;
`high-byte-run` search `pass_rate 0.4800`, `n_wrong=195`; `tag-pair-
match` search `n_wrong=5`; `wild-waf-crs-942360-concat-sqli` search
`n_wrong=5`
(`reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.tsv`,
lines 306/320/607/1418). The three-pattern `did_not_compile` set
(`wild-datetime-datefinder-alternation`,
`wild-secrets-username-password-pair`,
`wild-waf-crs-942500-comment-obfuscation`) is UNCHANGED, same
diagnostic verbatim both dates: `tre_regncompb failed (code 11):
Invalid character range`. `re2-default` and `vectorscan-block-nosom`
both stay `pass_rate 1.0000` clean on `high-byte-run` in BOTH samples —
the two engines sharing the same box and the same window infrastructure
show no analogous gap, ruling out a shared harness or box cause.

**Exact pass-rate table** (both samples, D35 archived-transcript
style):

| pattern | regime | first sample (2026-09-18) | second sample (2026-09-19) |
|---|---|---|---|
| `high-byte-run` | large-subject-throughput | 0.0000 (15/15 trials wrong) | 0.0000 (15/15 trials wrong) |
| `high-byte-run` | short-subject-search | 0.4800 (195/375 trials wrong) | 0.4800 (195/375 trials wrong) |
| `tag-pair-match` | short-subject-search | 0.9867 (5/75 wrong) | 0.9867 (5/75 wrong) |
| `wild-waf-crs-942360-concat-sqli` | short-subject-search | 0.9867 (5/75 wrong) | 0.9867 (5/75 wrong) |

Reading (unverified against the source — no `src/tre_regncompb`/
`tre_regnexecb` code was read for this finding, only the driver's
observed behavior): a SYSTEMATIC raw-high-byte handling gap in TRE's
byte-mode matcher (`tre_regncompb`/`tre_regnexecb`, `testees/tre/
CLAUDE.md`'s own convention), not confined to non-UTF-8 bytes
specifically (`tag-pair-match` and `crs-942360-concat-sqli` carry no
unusual byte content) — three independent patterns, two independent
samples, one consistent shape. Status: OBSERVED, now REPRODUCED; not
yet UNDERSTOOD (no TRE source read) or REPORTED upstream. Next: a
`testees/tre/CLAUDE.md` addendum recording the gap as confirmed
reproducible (owed, `docs/dev/ledgers/2026-09-18-capability-window-
cf0962e3.md` §7 ask 2 and `docs/dev/ledgers/2026-09-19-capability-0.1-
ext-second-cf0962e3.md` §6); a direct read of TRE 0.9.0's
`tre_regncompb`/byte-mode matching source, if this gap is ever chased
past reproduction into a cause.

**2026-09-27 ([B103], lane b103other): NOT-A-BUG.** TRE reads `\` inside `[...]` literally, which POSIX.1-2017 XBD 9.3.5 requires; glibc's regcomp gives the identical answers (control in `docs/dev/upstream/repro/U6/`). The wrong answers are a BENCH-SIDE mismatch: our tre testee receives PCRE-dialect bracket escapes. Census `docs/dev/measurements/2026-09-27-tre-bracket-escape-census.txt` (30 bench patterns carry one; 6 capability patterns reach TRE and run, 4 of them wrong). Fix queued as plan.md [B105]. No upstream note.

## U7 — vectorscan 5.4.11 refuses a `(?x)` pattern whose final line is an UNTERMINATED `#` comment (`hs_compile` code -4 "Unterminated comment") where libpcre2, pcrec, oniguruma and rust-regex all accept it — and the bench's [B70] whole-subject wrap spelling, whose trailing newline terminates the comment, makes the WRAPPED form compile while the plain form still refuses (OBSERVED 2026-09-22, `bench/capability@0.1` [B71] wrapfix window)

Record `capability@0.1__vectorscan_5.4.11_block-nosom-nocaps-simd__
budu-ryzen1600__20260922T053300Z` (pcrec-pin checkpoint 25b1984f; no
pcrec code involved in the cell): the two CASE-1 free-spacing patterns
`wild-codegrammar-json-number-extended` and
`wild-codegrammar-json-stringcontent-escape` — both `(?x)` patterns
whose canonical text ends inside a `#` comment with no trailing
newline — are `did-not-compile` on the PLAIN form with vectorscan's own
diagnostic `hs_compile failed (code -4, expression 0): Unterminated
comment.` (verbatim in the record and in
`reports/2026-09-22-capability-0.1-budu-ryzen1600-wrapfix-25b1984f.interpretation.md`'s
R-STATUS-4 section), while the WHOLE-SUBJECT form — the [B70]
`(?:…)\z` wrap, which under the free-spacing requires-tag inserts a
raw newline before its closing tokens (record_schema.md §5 ADDITIONS
3) — COMPILES: the newline terminates the comment and hands vectorscan
a parseable pattern. The oracle (libpcre2 10.46) and every other
attempter on the roster (pcrec at 25b1984f, oniguruma 6.9.10,
rust-regex 1.13.1) accept the unterminated-comment plain form; PCRE
itself defines a `(?x)` `#` comment as ending at newline OR END OF
PATTERN, so the plain form is well-formed PCRE and vectorscan's
refusal is its own stricter parse. Prior samples (through 2026-09-19,
old wrap spelling) refused BOTH forms, so the split first became
visible at this window. Filed as an engine-behavior observation, not a
bug report: hyperscan's PCRE-subset posture makes "stricter than PCRE"
a documented stance, and the bench's capability machinery already
renders the refusal as a first-class `did-not-compile` with the
diagnostic carried.

**2026-09-27 ([B103], lane b103other): REPRODUCED → DRAFTED.** Standalone repro `docs/dev/upstream/repro/U7/` PRESENT on 5.4.11; latest 5.4.13 not built (ragel/Boost absent), `Parser.rl`'s comment handling byte-identical 5.4.11→5.4.13; no tracker issue found (VectorCamp, intel/hyperscan). Draft `docs/dev/upstream/notes/vectorscan-2026-09-27.md` awaits Frank.

**2026-09-27: APPROVED by Frank and REPORTED** as https://github.com/VectorCamp/vectorscan/issues/416 (body = notes/vectorscan-2026-09-27.md minus our header, repro.c inlined).

## U8 — RE2 11.0.0 (`EncodingUTF8`) reports an empty-width `\B` BETWEEN THE BYTES of one UTF-8 character (OBSERVED 2026-09-26, `utf8@0.1` first sample)

Record `utf8@0.1__re2_11.0.0_default-caps-simdna_utf8__budu-ryzen1600__20260926T165447Z`,
pattern `asr-b-midchar` (`\B`), both regimes: excluded from ranking,
search_short pass-rate 0.9231 (35 wrong trials), throughput 0.2857 (25).
On `cls-mixed-hit` (`61 C3 A9 D0 B1`, "aéб") RE2's first `\B` is `[2,2)` —
between C3 and A9, inside é — where libpcre2 (PCRE2_UTF) answers `[3,3)`;
on `cls-space-pair` / `prp-zs-hit` (a NBSP between two ASCII letters) RE2
matches `[2,2)` inside the NBSP where the oracle has NO match. Find-all
counts rise 3.0-3.3% (`t-64k` 36,728 vs 35,660; `t-1m` 587,877 vs 569,129).
The driver's `--utf8` advance only moves the RESTART after an empty match
to a character boundary; the first reported position is RE2's own. RE2's
`\B` is ASCII-scoped (the config declares `ascii-class-scope`, satisfied)
and evaluates between bytes, so both sides of an interior byte boundary
read "not word". pcrec, pcre2-utf-interp/-jit/-dfa, rust and vectorscan
answer as the oracle. Status: OBSERVED. Not checked against RE2's issue
tracker or source. Ledger `docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md` §3.3.

**2026-09-27 ([B103], lane b103other): NOT-A-BUG.** Repro `docs/dev/upstream/repro/U8/` PRESENT on 11.0.0 and a 2025-11-05 build; RE2's `doc/syntax.txt` defines `\b`/`\B` as ASCII word-boundary tests, which the byte automaton applies between the bytes of a multi-byte character — documented design (related maintainer statement: google/re2#344). No note.

## U9 — Oniguruma 6.9.10 (`ONIG_ENCODING_UTF8`) folds `ß` to `SS` under `(?i)`; PCRE2 10.46 folds one-to-one (OBSERVED 2026-09-26, `utf8@0.1` first sample)

Record `utf8@0.1__oniguruma_6.9.10_default-caps-simdna_utf8__budu-ryzen1600__20260926T145215Z`,
pattern `ci-strasse` (`(?i)straße`), search_short: n_wrong 10, pass-rate
0.9780. It matches `STRASSE` at `[0,7)` (`ci-strasse-nearmiss`) and `DIE
STRASSE` at `[4,11)` (`lit-sharps-miss`); the oracle (simple folding, no
one-to-many) answers nomatch on both, as do pcrec, pcre2, rust, re2 and
vectorscan. A SEMANTICS difference (Unicode full vs simple case folding),
not a bug. We read it as Oniguruma's default case-fold flag including its
multi-character folds; that reading comes from the documented option and
is not checked against the source. Refutes utf8 P4.b/P4.c on this engine.
Status: OBSERVED (NOT-A-BUG candidate). Ledger §3.2.

## U10 — bare script properties read SCRIPT, not Script_Extensions, on rust-regex 1.13.1, RE2 11.0.0, Oniguruma 6.9.10 and Vectorscan 5.4.11 — on four scripts, not one (OBSERVED 2026-09-26, `utf8@0.1` first sample)

U2's witness census (2026-09-25) measured `\p{Greek}` alone. The first
sample shows the same divergence on `\p{Greek}`, `\p{Cyrillic}+` and
`\p{Latin}+` through U+0301 COMBINING ACUTE ACCENT (in
`lit-nfc-decomposed-miss`, "cafe" + U+0301), and on `\p{Han}+` through
U+3001/U+3002 (、。). A libpcre2 check over every distinct non-ASCII
character of `t-64k`/`t-256k`/`t-1m`/`t-64k-cjk` finds these two, and only
these, separating `\p{Han}` from `\p{sc=Han}`. Every cell is n_wrong 5
(short) or 20 (throughput) on rust, re2-utf8 and onig-utf8. Vectorscan's
boolean grain shows only the nomatch-vs-match cells (`prp-greek`,
`prp-cyrillic`); it cannot see `prp-latin`'s shorter span or `prp-han`'s
lower count. PCRE2 reads a bare script name as Script_Extensions; the four
engines read Script. This is a documented semantics difference, not a bug.
It refuted the utf8 set's P9/P10 transcription, which excluded `prp-greek`
alone. Status: UNDERSTOOD (the Unicode property difference; the separating
code points are verified above). Ledger §3.1.

## U11 — libpcre2 10.46's `pcre2_match()`/`pcre2_dfa_match()` built-in UTF-8 subject validation costs ~3.05-3.13× more per byte on Cyrillic text than on ASCII text of the same byte length, on ALL THREE routes — a genuine engine cost, not a driver artifact (OBSERVED and UNDERSTOOD 2026-09-26, `utf8@0.1` first sample; lane b102floor)

The addendum ledger (`docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7-
addendum-r2r7.md` §5/§8 item 4) flagged the `floor` pattern (the literal
`~`, NOT match-anything) costing ~3.05-3.12× more ns/byte on `t-64k-cyr`
than on `t-64k-asc` on `libpcre2-dfa`/`-interp`/`-jit`, all three at
`t-64k-cyr` only (extract lines 183-185: dfa ratio 3.1198, interp 3.1194,
jit 3.0481, npb 0.608/0.608/0.629 asc vs 1.897/1.897/1.918 cyr). Both
subjects are exactly 65536 bytes (`bench/utf8/subject_facts.tsv`); `~`
matches ZERO times on either (`expectations.tsv`: both `nomatch`), so the
real driver's find-all loop makes exactly ONE match call per subject —
this cost IS the whole measured cost, no loop involved.

A standalone C probe (`docs/dev/measurements/probe_libpcre2_floor_cyr.c`,
archived `2026-09-26-libpcre2-floor-cyr-probe.txt`) isolates the cause:
with `PCRE2_UTF` set and NO `PCRE2_NO_UTF_CHECK`, a single
`pcre2_match()`/`pcre2_dfa_match()` call over the SAME 65536-byte
buffers reproduces the ratio almost exactly (7 outer runs, medians
3.051/3.128/3.051 for interp/dfa/jit-via-match, within ~1.6% of the
committed report's three numbers) — using a single isolated call, no
bench harness, no store. Forcing `PCRE2_NO_UTF_CHECK` on the SAME calls
COLLAPSES the ratio to ~1.00 on all three routes AND brings the absolute
cost down to byte-mode (no `PCRE2_UTF` at all) levels: the entire gap
IS the built-in UTF-8 validation pass libpcre2 performs before its own
scan begins (man pcre2api, "PCRE2_NO_UTF_CHECK": validated "unless
PCRE2_NO_UTF_CHECK is passed", already the mechanism behind this
project's own [B94]/BD15 VALIDATE-ONCE fix — this finding is the SAME
validation call, priced by SCRIPT rather than by call count).

**pcrec-bench's own driver (`testees/pcre2/driver.c`) reaches this
validation cost on the `pcre2-jit` testee too**, and the probe confirms
why: the real driver never calls `pcre2_jit_match()` — `pcre2_match()`
dispatches to JIT-compiled code internally when present (driver.c's own
header comment, man pcre2jit). The probe's `jit_via_match` measurement
(pcre2_match() called on a JIT-compiled pattern, the ACTUAL testee call
shape) reproduces the ~3.05× ratio exactly; calling `pcre2_jit_match()`
DIRECTLY (which the real testee never does) shows FLAT cost on BOTH
scripts, check or no-check — localising the validation cost to
`pcre2_match()`'s/`pcre2_dfa_match()`'s own pre-dispatch check, which the
lower-level JIT entry point bypasses or performs far more cheaply as
part of its own vectorized code.

A negative control (the common byte `' '`, find-all loop, VALIDATE-ONCE)
shows the OPPOSITE, much smaller ratio (~1.10-1.16, ASC costlier) once
the one-time validation cost is amortised across many per-match calls
(9216 matches on asc vs 7214 on cyr in the same 65536 bytes) —
confirming the ×3 gap is specific to `floor`'s own one-call, zero-match
shape, not a property of every pattern in the set.

Status: UNDERSTOOD (confirmed live by the `PCRE2_NO_UTF_CHECK` ablation
and the `pcre2_jit_match()`-vs-`pcre2_match()` comparison; no libpcre2
source read — this is a black-box characterisation of `PRIV(valid_utf)`-
class behaviour, not a line-level attribution). NOT REPORTED upstream:
plausibly a documented ASCII-fast-path/multi-byte-slow-path
characteristic of any UTF-8 validator, not obviously a defect. Not ours
to fix or work around — `floor`'s own charter (bench/utf8/NOTES.md) is
the byte-safe control pattern, and this cost is intrinsic to what
`PCRE2_UTF` validation does, not to anything this project's driver or
harness chooses. `docs/dev/measurements/probe_libpcre2_floor_cyr.c` /
`2026-09-26-libpcre2-floor-cyr-probe.txt`.
