# bench/loglines — engine notes, the required-literal column, and what the numbers mean

Requirements §4.5 and §5: the per-engine notes, the declared variants, and the
statement of what this sub-bench exists to exercise.

## The objective, and what would defeat it

> Log-line search over mostly-FAILING text: what an engine pays to establish
> that a chunk of log lines does NOT contain the shape an operator is grepping
> for, at the sizes a log shipper hands a matcher (256 B – 4 KB) and across a
> size sweep to 1 MB. The set contains both cases the answer turns on —
> patterns whose match requires a literal byte, which a required-byte precheck
> can dismiss a subject on, and patterns built only from classes, which no
> such precheck can help.

**Where it comes from.** Inbox I-7 §1 (the pcrec manager's reading of the
first production sample) found that on the two failing 1 MB subjects of
`bench/email`, pcre2-interp answered in 17.8 µs — memchr speed over the whole
subject, because PCRE2 knows `@` must occur in any match and the subject has
none — while pcrec's DFA scanned every byte at 3.26 ns/byte, 192× slower.
pcrec's DFA has a candidate-START skip but no required-byte (any-position)
precheck. That gap is chartered in pcrec as **[OPT-5]**, and pcrec's rule is
to build under a measured need (D77): **this sub-bench's number is what
decides whether [OPT-5] gets built.** So the set has to exercise the regime
honestly and it has to contain the case a precheck cannot help.

**What would defeat the objective.** A testee that answers from anything but
the pattern and the subject: pre-indexing the subject across calls, caching an
answer keyed by the subject's identity, or hoisting the required-byte scan out
of the timed loop. Every subject is offered to the driver as bytes it did not
choose, in an in-process batched loop (requirements §3), and the harness's
per-call floor is measured by the floor pattern (below) so a suspiciously
cheap number has something to be read against.

**The second thing that would defeat it, and the reason the set is shaped the
way it is:** a failing subject whose bytes are rejected on the first byte
measures nothing. See "The background is near-misses" below.

## The patterns, and the required-literal column

`pattern_facts.tsv` is the authority and it is DERIVED from PCRE2 itself
(`gen_pattern_facts.py`, via `pcre2_pattern_info`'s `LASTCODEUNIT`/
`LASTCODETYPE` — upstream's `req_cu`), re-derived by `make check`, never
hand-typed. The table below is that file at the time of writing.

| pattern | required literal | m/n (search) | tier | hazard | what an operator is grepping for |
|---|---|---|---|---|---|
| `iso-ts` | `:` | 8/112 | base | none | an ISO-8601 / RFC 3339 timestamp with optional fraction and zone |
| `ipv4` | `.` | 10/112 | base | ambiguous-decomposition | a dotted quad with bounded octets (`25[0-5]`…) |
| `ipv6` | `:` | 7/112 | base | ambiguous-decomposition | the colon-hex address shape, full form or a `::` elision |
| `kv-quoted` | `"` | 8/112 | base+assertions | none | `key="value"` with backslash escapes |
| `level-context` | **NONE** | 8/112 | base+assertions | none | `ERROR`/`FATAL`/`CRIT` on the same line as `timeout`/`refused`/`denied`/… |
| `http-5xx` | `5` | 7/112 | base+assertions | none | an access line whose status is 5xx |
| `uuid` | `-` | 8/112 | base+assertions | none | a version-1..5 UUID |
| `stack-frame` | `)` | 7/112 | base+assertions | ambiguous-decomposition | a Java `at pkg.Class.method(File.java:42)` frame |
| `hex32-id` | **NONE** | 8/112 | base+assertions | none | a 32-hex trace id |
| `bignum` | **NONE** | 8/112 | base+assertions | none | a 10–19 digit id / epoch-ms / byte count |
| `floor` | — | 112/112 | base | none | the floor control, one byte (below) |

**The three `NONE` rows are the control** the objective names: `level-context`
is an alternation whose branches end in different bytes, and `hex32-id` and
`bignum` are built only from classes, so PCRE2's own analysis finds no byte
that every match must contain. No required-byte precheck — pcrec's [OPT-5]
included — can dismiss a subject for them; they must be scanned. Any speedup
a testee shows on the other seven and not on these three is the precheck, and
any speedup it shows on these three is something else. The control is two
DIFFERENT class-only shapes on purpose (`hex32-id` fixed-length, `bignum`
variable) so it is not one shape counted twice.

`min_length` is in `pattern_facts.tsv` too: PCRE2 also refuses a subject
shorter than the minimum match, which is a second cheap dismissal and is why
the column is there. Nothing in this set is short enough for it to fire.

**Feature tiers.** `base` is pcrec's frozen `std1` set (`classes`,
`modifiers`). Eight patterns use `\b`, whose module (`assertions`) is BUILT in
pcrec but is not in `std1`, so they are refused under a bare invocation with
`requires module 'assertions'`. Every pcrec testee already passes
`--features all` — a build/run flag of the TESTEE, not a variant of the
pattern; the pattern text handed to pcrec is byte-identical either way. Same
posture, and the same reasoning, as `bench/email`'s `--features all` note.

**Declared variants: none.** All eleven patterns are canonical PCRE2
spellings and every adapter runs the canonical text byte for byte, so every
record carries `patterns[].variant = null` — which requirements §4.5 requires
to be STATED rather than assumed.

**No capturing group participates in any match**, on any pattern, over every
subject and regime: every group in the set is `(?:…)`, and
`gen_expectations.py` re-checks that on every run and says so on stderr
(shared code, `pcrecbench/expectations.py`). So the span is the whole
observable answer here, exactly as in `bench/email`, and the general
capture-correspondence contract stays at OD-B9.

## The subjects

`gen_subjects.py`, seed **20260828**; `gen_throughput_subjects.py`, seed
**20260829** (a different seed so the sweep is not the search band's first
lines at four lengths). Both draw from one grammar, `logtext.py`, whose only
randomness primitive is `random.Random(seed).getrandbits(32)` — `choice`,
`sample` and `randrange` are avoided because their internals have moved
between CPython releases and a manifest that must reproduce byte for byte
cannot rest on that.

**Search band: 112 subjects, 279–3772 B** (mean 1456 B), four size bands of 28
(256–512, 512–1024, 1024–2048, 2048–3800 B target; feature lines are counted
INSIDE the target, so a subject carrying a stack trace is not a different size
class from one carrying nothing).

**Size sweep: 12 subjects**, 16 KB / 64 KB / 256 KB / 1 MB × three flavours —
see "The size sweep" below.

**Formats.** Mixed, as a real estate is: BSD syslog, nginx access, nginx
error, kubernetes klog, JSON-lines, journald/containerd, and Java stack-trace
blocks.

**The background is NEAR-MISSES, which is the point.** Every line the
background grammar can emit is built so that no member pattern matches it, and
built to be *nearly* a match: 12-hex container ids where `hex32-id` wants 32,
three-part version numbers where `ipv4` wants a dotted quad, `2026/08/27` and
`Aug 27` timestamps where `iso-ts` wants `2026-08-27`, hyphenated 4-4-6 short
ids where `uuid` wants 8-4-4-4-12, six-digit microsecond fields where `bignum`
wants ten. A failing corpus that any engine rejects at byte 1 would measure
the first-byte test and nothing else.

One measured consequence of taking that seriously: an unconstrained 12-hex id
is all decimal digits about once in 290 (0.625¹²), and an all-digit 12-hex id
IS a 12-digit number that `bignum` matches. The first cut had one such
accident in 112 subjects and would have had ~35 in a 1 MB failing subject — so
`logtext._shortid` forces one `a`–`f`. The oracle is what caught it and the
oracle is what confirms the fix: the realised match counts are now exactly the
designed ones, everywhere.

**Match rate: 6.2–8.9 % per member pattern, by DESIGN, not by draw.** Each
shape is injected into an exactly-chosen number of subjects (`COUNTS` in
`gen_subjects.py`, drawn without replacement). The first cut used per-subject
coin flips and the realised rate moved by 4× between retunes — at n = 112 the
Bernoulli noise is wider than the band the set is supposed to sit in, so the
match rate would have been an accident of the seed. **~93 % of the 1120 member
(pattern, subject) search cells are `nomatch`**: that is the population this
sub-bench times.

One deliberate correlation, stated because it is visible in the numbers:
`http-5xx` injects an nginx access line and an access line carries an IPv4
client, so `ipv4`'s 10 matching subjects are the union of its own 3 and
`http-5xx`'s 7. `stack-frame`'s block opens with an `ERROR` line, but with no
context word, so it does not feed `level-context`.

**Non-periodic by construction, and the manifest proves it per subject.**
Inbox I-10 asked for non-periodic subjects and a `periodic` fact in the
manifest; both manifests carry a fifth column, `periodic`, with the same
name and semantics [B17] is giving `bench/email`: **the smallest period p in
1..4096 such that `b[i] == b[i-p]` for every i ≥ p, or `no`.** All 124
subjects here read `no`. (`logtext.smallest_period` computes it as
`b[p:] == b[:-p]` behind a one-byte pre-test, which is what makes it
affordable on a 1 MB subject.) `pcrecbench/subbench.py` carries the extra
columns by header name (`Subject.extra`, `Subject.periodic`); a four-column
manifest parses exactly as it always did.

## The size sweep, and the give-up outcome

Inbox I-2 §1(b) makes a give-up a first-class outcome and asks for **the size
at which it first fires**. One subject size can only say "gave up" or "did
not"; four sizes an octave apart bracket it. Nothing here is expected to give
up — every member is a bounded shape and the two `ambiguous-decomposition`
patterns are bounded too — so an observed give-up is a finding, and the sweep
is what makes it a locatable one. A give-up is recorded as `gave-up` with the
engine's own code in `diagnostic`, is NOT timed, and is excluded from rankings
(schema v1.1; the same policy `bench/email`'s NOTES describes).

| flavour | what it is | what it measures |
|---|---|---|
| `t-<size>-fail` | mixed background, no member shape anywhere | the failing path with the precheck UNAVAILABLE: every required unit in this set (`:` `.` `-` `"` `)` and a digit) occurs in mixed log text, so no testee can dismiss these without scanning |
| `t-<size>-syslog` | a single-source BSD-syslog stream, also failing, carrying no `"` and no `)` | the failing path with the precheck AVAILABLE for exactly two patterns — `kv-quoted` and `stack-frame` — and unavailable for the other eight |
| `t-<size>-hit` | the mixed background with one instance of every shape per 4 KB | the matching-bearing counterpart at the same size and grammar |

**The `-syslog` flavour exists because the first cut could not have produced
the number this row was opened for.** With only `fail` and `hit`, all eight
throughput subjects contained every required byte in the set, so not one of
them was the analogue of `bench/email`'s `t-b-no-at` — they were all the case
where both engines must scan. `pattern_facts.tsv`'s `tput_req_absent` column
now names the four subjects where a precheck dismisses without scanning
(`t-016k-syslog` … `t-1024k-syslog`, for `kv-quoted` and `stack-frame`).

**That is itself a finding for [OPT-5], and it is the reason the column is
committed rather than assumed:** on mixed log text, most log patterns'
required byte is *structural* — `:` and `.` and a digit are in every subject
this set has — so a required-byte precheck would fire on almost none of the
search band. Its value concentrates in the patterns whose required byte is
format-specific: `"` is absent from 35 of the 112 search subjects and `)` from
16. Whatever the measured number turns out to be, the report should read it
against those counts rather than against "the precheck helps on failing text".

## The floor pattern

`patterns/floor.rx` is the one-byte literal `:`, `role = "floor"` in the
sidecar (schema v1.3, the rule for every short-subject set since [B15]). It
runs over the SAME subjects the members do, in both declared regimes.

`:` is this corpus's `@`: structural in every log format here, so it is found
early on every subject — **first-match offset 2..30 bytes, mean 7.3, on
subjects averaging 1456 B**. That is what makes it a per-CALL floor: its
number is the harness's per-call loop, the driver's dispatch and the subject
handover, and almost none of it is scanning. A member pattern's per-call
number read net of the floor is the pattern's own work.

What it is NOT: a cross-engine ranking. Each engine's floor is its own
dispatch cost, so "X's floor is smaller than Y's" is a finding about per-call
overhead, not about matching. Same reading as `bench/email`'s NOTES sets out.

In the throughput regime the floor is a find-all `:` scan over the whole
subject — a memchr-class scan with a match every few bytes (≈ 38 000 per MB),
not a regex-engine one.

## Regimes: `search_short` and `throughput`, and NOT `match`

Declared, not omitted. `match` is anchored + end-anchored over the whole
subject — "is this string, entire, an instance of the pattern" — which is a
real question about an email address and not a question anyone asks of a chunk
of log lines. Anchoring these patterns over these subjects yields `nomatch` on
every one of the 1232 cells, which measures start-state rejection and nothing
else, and it would additionally make pcrec's adapter compile a second
`(?:…)\z` artifact per pattern (11 more gcc invocations per cell) to produce
it. `subbench.py`'s `subjects_for()` and the harness's `run_cell()` take a
declared subset as-is; `quick --regime match` on this sub-bench is refused by
name.

`short_search_max_bytes = 4096`, not `bench/email`'s 256: requirements §3
sizes this regime at "~256-byte subjects (log lines, fields)" and a single log
LINE is that, but what a shipper, a `grep`, or an agent hands a matcher is a
CHUNK of lines. Every one of the 112 subjects is inside the band, so the
`search_short` set and the full short set are the same 112 here.

| regime | subjects | semantics | expectations |
|---|---|---|---|
| `search_short` | all 112 (279–3772 B) | unanchored at offset 0 | first-match span; 191 of 1232 cells match, 79 of them across the ten members |
| `throughput` | the 12 (16 KB – 1 MB) | unanchored, find-all | first span + count; 52 of 132 cells match (the floor on all 12, each member on the four `-hit`) |

## Per-engine notes

- **libpcre2 (`pcre2-interp`, `pcre2-jit`)** — none needed for the patterns:
  libpcre2 is the oracle, so it runs the canonical text under the canonical
  semantics by construction. Two behaviours a reader should expect, both
  upstream-documented and both directly relevant here:
  - the **required code unit** — upstream's `req_cu`, exposed as
    `PCRE2_INFO_LASTCODEUNIT` / `PCRE2_INFO_LASTCODETYPE` and read through
    them by `gen_pattern_facts.py`: the byte that must occur somewhere in any
    match, on which `pcre2_match` dismisses a subject without running the
    automaton. TWO SOURCES, and neither is a man page: this box has no
    `pcre2api(3)` installed (`man -w pcre2api` → no entry, the -dev package
    is absent), so the upstream document is named but NOT quoted here. What
    IS first-hand is (a) the library's own answers through
    `pcre2_pattern_info`, which is where every value in `pattern_facts.tsv`
    comes from, and (b) inbox I-7 §1's measurement of the behaviour on
    `bench/email` — 0.017 ns/byte over a 1 MB subject whose `@` was absent.
    A reader wanting the upstream wording should check `pcre2api(3)` on a box
    that has it;
  - inbox I-7 §1 also recorded that **pcre2-JIT does not get that
    whole-subject dismissal** on a 1 MB subject (144× slower than its own
    interpreter there). If that holds on this set too, the `-syslog` rows are
    where it will show, and it is an upstream finding, not a bench error.
- **pcrec (`pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`)** — none needed for the
  patterns beyond `--features all` (above). Expect the DFA under `auto` for
  all eleven (no capturing group anywhere in the set), and therefore no frame
  budget to bind: the `_in` (caller-provided frame buffer) entries have
  nothing to read on this sub-bench, exactly as on `bench/email` at pin
  692c2e8. `pcrec-vm` forces the VM and is the entry where a give-up, if one
  exists here at all, would appear first.
  One consequence of declaring no `match` regime that a reader of the RECORD
  will see: pcrec's adapter compiles both artifacts per pattern
  unconditionally (`plain` and the `(?:…)\z` `whole-subject` form), so a
  pcrec record here carries `whole-subject` COMPILE rows with no match rows
  under them. That is valid -- rule X27 requires a whole-subject match row to
  have a compile row, not the reverse -- and it is why the cell-time estimate
  below counts 110 gcc invocations rather than 55. Do not read those compile
  costs as this sub-bench's: they belong to an artifact it never measures.
- **No engine note claims a measurement.** Nothing in this file is a number
  from a run of this sub-bench; the only figures here are properties of the
  corpus and of PCRE2's compile-time analysis, all re-derived by `make check`.

## Cell-time estimate

One cell = one testee × all 11 patterns × both regimes, at `--trials 5`.
The harness calibrates iterations so the MEDIAN subject's loop is 50 ms and
caps a trial's predicted sweep at 20 s (`harness.py`). With subject costs
roughly uniform within a regime, a trial's sweep is ≈ n × 50 ms, so:

- `search_short`: 112 subjects × 50 ms × 5 trials × 11 patterns ≈ **5.1 min**
- `throughput`: the median subject sets the count, so a trial is ≈ 250 × the
  sum of the per-iteration costs ≈ 3 s; × 5 trials × 11 patterns ≈ **2.7 min**
- compile: pcrec compiles two artifacts per pattern (`plain` and
  `whole-subject`) × 5 trials = 110 gcc invocations at DFA cost ≈ **1–2 min**;
  for the pcre2 testees this term is negligible

**≈ 9 min for a pcrec cell, ≈ 8 min for a pcre2 cell**, inside the ≲ 10 min
this sub-bench was designed to. The dominant term is
`n_subjects × 50 ms × trials × patterns`, so the levers, in order, are
`--trials`, the pattern count, and the subject count — not the subject sizes.

## Origin

Nothing here is copied. The patterns were authored from the GOAL — the shapes
operators actually grep logs with — by an author working under the [B11.1]
blinding: pcrec's `docs/spec/` was read (feature tiers, the module roster,
the `--features` gate), and pcrec's `tests/`, `src/` and corpora were NOT, so
this set does not inherit pcrec's own alphabet. That is pcrec's D27 lesson
applied to a bench: tests derived from the code inherit the code author's
blind spots, and this sub-bench's whole job is to find one.
