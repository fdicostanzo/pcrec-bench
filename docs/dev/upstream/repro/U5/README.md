# U5 repro — libpcre2's interpreter is quadratic on balanced-paren
recursion, against a match count that is linear in subject size

**What it shows.** `bench/syntax/patterns/rec-r-uc.rx` —
`\((?:[^()]|(?R))*\)`, balanced parenthesised expressions via `(?R)`
recursion — costs **~10× more nanoseconds per subject byte** on a
1 MiB mixed-text subject than on a 64 KiB one (a 16× size step), when
run with `pcre2test`'s `global` (find-all) mode under the plain
interpreter (no JIT). A linear-time construct would cost the SAME
ns/byte at both sizes (ratio ~1, comfortably inside
`bench/syntax/NOTES.md`'s own [0.7, 1.4] "still linear" band); this one
does not. The number of matches found also scales roughly linearly
with subject size (117 at 64 KiB, 2,068 at 1 MiB — ~17.7×, close to
the 16× size step), so the blow-up is a PER-MATCH cost that grows with
subject position/size, not merely "more matches, same unit cost."

**Engine + version.** libpcre2 10.46 (2025-08-27), the plain
interpreter (`pcre2_match`, no JIT). System `pcre2test`
(`libpcre2-8-0`/`pcre2-utils` 10.46-1build1), the same version
pcrec-bench's own `pcre2-interp` testee links.

**Build/run.**

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

Generates two subjects (64 KiB seed 20260905, 1 MiB seed 20260907)
via the bundled `gen_subject.py` — a STANDALONE transcription of
pcrec-bench's own `bench/syntax/censustext.py` line grammar (an
xorshift RNG, six line kinds weighted so prose is the background and
structured shapes — including balanced-paren expressions, 1 line in
~112 of them left deliberately UNBALANCED with a trailing unclosed
`(`, no `bench/` code imported or read at run time). At the same
(seed, byte-count) pair this produces text BYTE-IDENTICAL to
pcrec-bench's own committed `t-64k`/`t-1m` throughput subjects
(verified when this repro was authored: matching sha256). Each subject
is embedded in a `pcre2test` input as ONE data line with its internal
newlines escaped as literal `\n` (pcre2test's own multi-line-subject
convention, man pcre2test "DATA LINES") — this matters: the
recursion's own catastrophic behaviour is driven by an unclosed `(`
scanning FORWARD PAST its own line into the rest of the buffer looking
for a closer, which only happens if the subject is presented to
`pcre2test` as one continuous buffer rather than one physical line per
subject line. `run.sh` then runs `pcre2test -tm 1` with the `global`
modifier at each size, sums every reported per-match "Match time", and
divides by the subject's byte count. `$UPSTREAM_ENGINE_BUILD` points
the same run at a different `pcre2test` binary.

**Pattern file**: `pattern_rec.txt`, verbatim from
`bench/syntax/patterns/rec-r-uc.rx`. Two spelling twins in the same
bench family, `rec-1.rx` (`(\((?:[^()]|(?1))*\))`, calling a numbered
group) and `rec-name.rx` (`(?<p>\((?:[^()]|(?&p))*\))`, calling a
named group) are NOT exercised by this repro — the original
observation's own P3 ("spelling parity") predicts they cost the same;
untested here.

**Expected PRESENT output.** stdout's final line:

    U5 PRESENT pcre2 <version> <ratio>x

where `<ratio>` is the 1 MiB-ns/byte : 64 KiB-ns/byte ratio.
`expected.txt` is a captured PRESENT run (869.9 -> 8828.6 ns/byte,
ratio 10.15x, box ubuntubudu, 2026-09-27) — within 1.4% of
pcrec-bench's own original 870.4 -> 8704.8 ns/byte reading over its
own (byte-identical) subjects.

**What ABSENT (fixed) looks like.** The ratio drops toward ~1× (a
truly linear per-byte cost). `run.sh` exits 1 and prints
`U5 ABSENT pcre2 <version> <ratio>x` when the ratio is under 3.0 —
comfortably below the ~10x observed here and comfortably above the
[0.7, 1.4] band a linear cost would show.

**CANNOT-RUN.** No `pcre2test` binary, or no `python3` (needed for
`gen_subject.py`) — exit 2.

**Not chased to a source-level mechanism.** No libpcre2 source was
read for this repro (matching the original narrative's own
"Reading (unverified)" caveat) — the hypothesis on record (each
`(?R)`-style re-entry re-walks or re-allocates state proportional to
the CURRENT match depth/position) is plausible and consistent with
what is measured here, but this repro only demonstrates the
measured effect, reproducibly, not its internal cause.
