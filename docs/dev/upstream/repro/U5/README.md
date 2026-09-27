# U5 repro — a super-linear per-byte cost on balanced-paren recursion,
and the ablation that shows it is PATTERN-INHERENT, not a libpcre2 defect

**CLASSIFICATION (manager review 2026-09-27, applying the new pipeline
skill's rule — "rule out intended/inherent behaviour before we tell a
maintainer something is wrong"): NOT-A-BUG.** The super-linear cost IS
real and reproducible (see below), but it is caused entirely by
DELIBERATELY UNBALANCED parenthetical lines this repro's own subject
generator plants (~1 line in ~112) — an unclosed `(` forces ANY
backtracking regex engine's `[^()]*`-style body to scan forward through
the rest of the subject before it can fail, and since the grammar
plants such opens at roughly constant density per byte, the total cost
across a subject grows faster than linearly with its size. This is
confirmed on THREE separate axes below (libpcre2 interpreter, libpcre2
JIT once its own resource cap is lifted, and independently on
Oniguruma) — it is not specific to libpcre2's interpreter, or to
libpcre2 at all. **This finding is being kept out of
`notes/pcre2-2026-09-27.md`** on this basis.

## What is actually happening (the four-way ablation `run.sh` runs)

Pattern `\((?:[^()]|(?R))*\)` (balanced parenthesised expressions via
recursion) over mixed prose/structured text at two sizes (64 KiB,
1 MiB — a 16x step), find-all ("global") mode:

| engine + subject | 64 KiB ns/byte | 1 MiB ns/byte | ratio |
|---|---|---|---|
| libpcre2 interpreter, ORIGINAL (unbalanced lines present) | 986.5 | 9,043.4 | **9.17x** |
| libpcre2 interpreter, CONTROL (unbalanced lines suppressed) | 3.5 | 3.1 | 0.87x |
| libpcre2 JIT, ORIGINAL, jitstack=65536 KiB | 55.6 | 692.6 | **12.45x** |
| libpcre2 JIT, CONTROL, jitstack=65536 KiB | 2.0 | 1.7 | 0.87x |

Both engines are FLAT (well inside the [0.7, 1.4] "still linear" band
`bench/syntax/NOTES.md`'s own R7 rule uses) on the CONTROL subject —
same seed, same statistical shape, only the deliberately-unbalanced
tails removed — and both are clearly super-linear (~9-12x for a 16x
size step) on the ORIGINAL subject. **The interpreter is not uniquely
super-linear: the JIT is too**, once it is actually allowed to finish
the same work (see next section) — this rules out "the interpreter's
recursion implementation specifically is inefficient" as the cause.

A THIRD, fully independent engine — **Oniguruma 6.9.10** (this box's
system `libonig.so.5`+headers, `onig_search` via `ONIG_SYNTAX_PERL_NG`,
`ONIG_ENCODING_ASCII` byte mode, matching this bench's own
`onig-default` convention; recursion spelled `\g<0>` rather than
`(?R)`, Oniguruma's own syntax — see `pattern_rec_onig.txt` and
`onig_probe.c`, a from-scratch find-all loop, NOT sharing code with
`pcre2test` or with this project's own harness) — shows the SAME
shape, though milder: control 8.97 → 3.79 ns/byte (flat, even
decreasing), original 150.27 → 264.29 ns/byte (**1.76x** — smaller
than libpcre2's 9-12x, but clearly above the flat control's ratio, and
in the direction the hypothesis predicts). Build and run it yourself:

    gcc -O2 -o onig_probe onig_probe.c -lonig
    ./onig_probe pattern_rec_onig.txt <a subject file>

(needs `oniguruma.h` + `libonig`; `apt install libonig-dev` on Debian/
Ubuntu, already present on this box.)

## Why the JIT needed `jitstack` raised (a real, separate, correctly-
documented resource cap — NOT the cause of the super-linearity)

At the DEFAULT JIT stack (32 KiB, `pcre2test`'s own default), the SAME
ORIGINAL subject makes the JIT abort partway through the find-all loop
with `Failed: error -46: JIT stack limit reached` (PCRE2_ERROR_JIT_-
STACKLIMIT) after only 6/117 matches at 64 KiB and 16/2068 at 1 MiB —
a real, correctly-reported resource exhaustion (deep recursive
backtracking through repeated unclosed-`(` attempts genuinely needs
more JIT stack than the 32 KiB default), NOT a silent hang and NOT
what causes the 9-12x per-byte cost. Raising `jitstack` to 65536 KiB
(`\=jitstack=65536` on the subject line, man pcre2test "Setting the
JIT stack size") lets the JIT complete the SAME 117/2068 matches the
interpreter finds, and ONLY THEN does its own super-linear per-byte
cost become visible (12.45x) — comparable to the interpreter's (9.17x)
and thus reachable on either code path once each is allowed to
actually finish the work. Stack size genuinely gates how much of the
SAME work can complete here (unlike U1's cliff, a different finding,
where jitstack size turned out to make no difference at all — see
`repro/U1/README.md`): at 64 KiB, `jitstack=1` and `jitstack=128` both
still abort at the SAME 6th match (`error -46`), but the failing call
itself takes longer with more stack available (4 microseconds at
1 KiB vs 94 microseconds at 128 KiB) — consistent with the JIT
backtracking deeper before giving up. Only `jitstack=65536` was large
enough to let all 117 matches complete without erroring; that is the
value `run.sh` uses.

## Build/run

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

Runs the full four-way ablation above (8 timed cells: {interp, jit} x
{original, control} x {64 KiB, 1 MiB}), prints every ns/byte value and
ratio to stderr, prints its own CLASSIFICATION line, then reports
`U5 PRESENT|ABSENT pcre2 <version> <ratio>x` on stdout using the
interpreter-original ratio (the finding as first observed) —
`run.sh` reports the raw phenomenon; the NOT-A-BUG determination and
its evidence live in this README, not in the exit code, so the
registry can still record "REPRODUCED" (the phenomenon is real) while
`upstream_findings.md`/`findings.tsv` record NOT-A-BUG (the manager's
to set). `$UPSTREAM_ENGINE_BUILD` points the pcre2test half at a
different binary.

Uses the bundled `gen_subject.py` — a STANDALONE transcription of
pcrec-bench's own `bench/syntax/censustext.py` line grammar (an
xorshift RNG, six line kinds weighted so prose is the background and
structured shapes — including balanced-paren expressions, 1 line in
~112 of them left deliberately UNBALANCED with a trailing unclosed
`(`, no `bench/` code imported or read at run time), now taking a
fourth CLI argument (`0`/`1`, default `1`) that suppresses the
unbalanced tail while consuming the SAME RNG draw either way, so the
control subject is byte-identical to the original except for the
removed tails. At `allow_unbalanced=1` (the default) it produces text
BYTE-IDENTICAL to pcrec-bench's own committed `t-64k`/`t-1m` throughput
subjects at the same seeds (verified when this repro was authored:
matching sha256). Each subject is embedded in a `pcre2test` input as
ONE data line with its internal newlines escaped as literal `\n`
(pcre2test's own multi-line-subject convention, man pcre2test "DATA
LINES") — this matters: an unclosed `(`'s own forward scan only
crosses into later lines' text if the subject is ONE continuous buffer
rather than one physical line per subject line.

**Pattern file**: `pattern_rec.txt`, verbatim from
`bench/syntax/patterns/rec-r-uc.rx`. `pattern_rec_onig.txt` is the same
construct in Oniguruma's own recursion spelling (`\g<0>` in place of
`(?R)`), for `onig_probe.c` only.

**Expected PRESENT output.** stdout's final line:

    U5 PRESENT pcre2 <version> <ratio>x

`expected.txt` is a captured PRESENT run (ratio 9.17x on the
interpreter-original cell) plus the full 8-cell table and the
oniguruma cross-check, box ubuntubudu, 2026-09-27.

**What ABSENT would look like.** The interpreter-original ratio drops
toward ~1x. Given the classification above, an ABSENT result here
would not by itself mean anything was "fixed" — it would need
re-checking against the SAME control-subject ablation, since the
effect is pattern-inherent rather than a libpcre2 property that a
release could change.

**CANNOT-RUN.** No `pcre2test` binary, or no `python3` — exit 2.

**Not sent upstream.** Per the classification above, this finding is
NOT included in `notes/pcre2-2026-09-27.md` and — per the design
note's status ladder — should be recorded as `NOT-A-BUG` in
`findings.tsv`/`upstream_findings.md` (owed to whoever applies
registry status, per this project's convention that lane work does not
edit those files directly).
