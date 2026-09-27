# U4 repro — libpcre2 JIT slower than its own interpreter on an
HTTP-access-line pattern over failing log text

**What it shows.** `bench/loglines/patterns/http-5xx.rx` —
`"(?:GET|POST|PUT|PATCH|DELETE|HEAD) [^ "]+ HTTP/1\.[01]" 5[0-9]{2}\b`
— compiles with `First code unit = '"'` (`pcre2test ...,info`). Over 1
MB of ordinary prose containing NO `"` byte at all, the interpreter
dismisses the whole subject in ~18-24 µs (a `memchr`-class scan for
`"` that finds nothing); the JIT-compiled matcher takes ~560-640 µs on
this box — a ~23-34× penalty for using the JIT, though the pattern's
own compiled properties (the required first code unit) are identical
either way. This is not a hang (see U1/U2 for the catastrophic and
required-code-unit variants on the email set) — the JIT's cost is
still linear in the subject length, just far higher per byte.

**A grain the original observation ALSO reports, that this repro does
NOT reproduce robustly**: pcrec-bench's own SHORT-subject-search
measurement (112 subjects, 256-512 B band) reports a milder ~1.8×
ratio (jit 104,980 ns/call vs interp 57,326 ns/call, aggregated over
many distinct subjects by the bench's own calibrated harness). This
repro's own attempt at that grain, using `pcre2test -tm 100000` over a
single 101-byte synthetic no-quote log line, found the ratio too noisy
to trust run to run (three repeats gave 2.45×, 1.04×, 1.22× on an
otherwise idle box) — the raw per-call cost at that subject size is
under 100 ns, close to `pcre2test`'s own timing-loop noise floor.
`run.sh` therefore checks the 1 MB throughput case only, which is
robust and directly reproducible; the short-subject ratio is a
real, softer, and separately-reported facet of the same underlying
mechanism that this repro does not attempt to isolate on its own.

**Engine + version.** libpcre2 10.46 (2025-08-27). System `pcre2test`
(`libpcre2-8-0`/`pcre2-utils` 10.46-1build1), the same version
pcrec-bench's own `pcre2-jit`/`pcre2-interp` testees link.

**Build/run.**

    UPSTREAM_SCRATCH=/tmp/scratch bash run.sh

Generates a 1,048,576-byte subject of repeated quote-free prose into
`$UPSTREAM_SCRATCH`, then runs `pcre2test -tm 20` (20 in-process match
calls) with and without the `jit` pattern modifier, and reports the
MEDIAN "Match time" each way. `$UPSTREAM_ENGINE_BUILD` points the same
run at a different `pcre2test` binary.

**Pattern file**: `pattern_http5xx.txt`, verbatim from
`bench/loglines/patterns/http-5xx.rx`.

**Expected PRESENT output.** stdout's final line:

    U4 PRESENT pcre2 <version> <ratio>x

`expected.txt` captures one PRESENT run (ratio 30.87x, box ubuntubudu,
2026-09-27) plus two repeats (22.97x, 34.33x) showing the ratio is
robust, not a one-off.

**What ABSENT (fixed) looks like.** The ratio drops toward ~1×. `run.sh`
exits 1 and prints `U4 ABSENT pcre2 <version> <ratio>x` when the ratio
is under 10 — comfortably below anything observed here.

**CANNOT-RUN.** No `pcre2test` binary found (on `$PATH` or at
`$UPSTREAM_ENGINE_BUILD`) — exit 2.
