# bench/litrun/ — notes (`litrun@0.1`)

## Objective

pcrec's [OPT-LITSCAN] S2a (inbox I-113, pcrec `docs/dev/lanes/
s2a_report.md` at pin a32bc86e, abi 41) makes the VM's own literal run of
`L >= 2` consecutive exact bytes ONE `pos + L <= n` bounds check plus one
`memcmp`, replacing a per-byte compare chain. The lane report's own D77
section (S7) asks a bench for two things it could not measure itself:

1. **§7.1 — does a factoring pass and the literal-run lowering INTERACT?**
   Factoring decides what the runs S2a lowers actually ARE (pulling a
   shared prefix out of an alternation changes run boundaries), so a gain
   measured with factoring on may not transfer with it denied, and vice
   versa. The lane's own compile-time stamps predict which of the two 2×2
   cells below is most likely to FLIP SIGN.
2. **§7.2 — does the compare itself carry a per-call constant, or a
   toolchain-specific length cliff?** `docs/dev/memcmp_lowering_study.md`
   (merged on pcrec's main the same day) found gcc-16 inlines every literal
   length from 1 to 64 EXCEPT `L = 31`, which calls `memcmp()` out of line
   at every optimization level from `-O1` to `-O3` — a narrow, real,
   gcc-specific cliff nothing in pcrec's own corpus needs today, but worth
   bracketing on a real artifact rather than a synthetic C loop alone.

**This set is deliberately NOT BLINDED** the way every other `bench/*/` set
under this project is (pcrec's D27 discipline, `bench/altwide/CLAUDE.md`'s
own "WHERE IT CAME FROM" is the usual shape). Blinding exists so a bench
result isn't shaped by knowing what an engine's own optimizer expects to
see; here the whole point is the OPPOSITE — pcrec's own engineers named the
exact cells and lengths they want measured, in a lane report this set
transcribes as literally as an engine-neutral set format allows (S7.1's
four patterns, S7.2's nine lengths, both the exact numbers in the report).
Nothing here is a blind test of pcrec; it is an ACCEPTANCE INSTRUMENT for a
specific, already-landed optimization, the same role `bench/bounded@0.3`
played for [OPT-5] STEP 2.

## The 2×2 set (§7.1)

Four patterns, crossed by the WINDOW (not this set — R-BENCH-4: an
engine-neutral set declares no pcrec flag) against
`{default, -fno-altcls-factor} × {default, -fno-lit-run}`:

| id | text | role | why |
|---|---|---|---|
| `alt-foo-tails` | `foo.x\|foobar\|foo.` | cell (a) | tails are not all literal, so factoring pulls out a shared `foo` and lit-run sees either 2 runs (factored: `foo`+`bar`) or 3 (unfactored: each branch's own `foo…`/`foobar`) |
| `wild-secrets-aws-access-key-id` | `\b((?:A3T[A-Z0-9]\|AKIA\|AGPA\|AIDA\|AROA\|AIPA\|ANPA\|ANVA\|ASIA)[A-Z0-9]{16})\b` | cell (a′) | copied VERBATIM from `bench/capability/patterns/` — see `provenance.tsv`. An island-shaped alternation; the lane report's own stamps (islands/runs/program bytes) name this the cell MOST LIKELY to flip the sign of `-fno-altcls-factor` under lit-run |
| `ctrl-abc-dollar` | `abc$` | cell (b), control | no alternation: `-fno-altcls-factor` must read null (the stamps confirm it on the lane compiler); only the lit-run column may move. Same text as pcre2's own testdata pattern (testinput1:1463) `bench/capability`'s `wild-semdiv-dollar-trailing-newline-pcre2` already carries |
| `wild-secrets-github-pat` | `\b(github_pat_[0-9a-zA-Z_]{82})\b` | cell (b′), control | copied VERBATIM from `bench/capability/patterns/` — see `provenance.tsv`. One 11-byte run behind an exact hybrid window: expect a small gain at most, never a factoring interaction (no alternation) |

The lane report's own predicted stamps at pin a32bc86e (compiler-measured,
NOT re-derived here — this set carries no pcrec-specific stamp reading;
that is the window's job):

| cell | default (islands/runs/bytes) | `-fno-altcls-factor` | `-fno-lit-run` | both denied |
|---|---|---|---|---|
| (a) | 0/2/1,357 | 0/3/1,537 | 0/0/1,955 | 0/0/2,915 |
| (a′) | 1/7/5,475 | 0/9/4,519 | 1/0/7,403 | 0/0/8,465 |
| (b) | 0/1/434 | 0/1/434 | 0/0/728 | 0/0/728 |
| (b′) | 0/1/1,770 | 0/1/1,770 | 0/0/3,330 | 0/0/3,330 |

Every subject built for these four is a hand-typed HIT or NEAR-MISS field
(`gen_subjects.py`), never generated prose — this is a correctness-and-
throughput cell, not a failing-scan one, so there is no background text to
construct. `aws-match` is AWS's own PUBLISHED example access key id
(`AKIAIOSFODNN7EXAMPLE`, the placeholder AWS's SDK/CLI documentation itself
uses) — a well-known, intentionally-fake value, never a real credential.

## The L-sweep (§7.2)

Nine exact literals, `lit-l2` .. `lit-l40`, `L ∈ {2, 3, 4, 7, 8, 10, 16,
31, 40}` (verbatim from the lane report), each the first `L` bytes of a
52-character, no-repeated-byte alphabet (`littext.ALPHABET` =
`ascii_lowercase + ascii_uppercase`). `L = 31` is a NAMED WATCH CELL: the
one length in `memcmp_lowering_study.md`'s whole 1–64 sweep where gcc-16
calls `memcmp()` out of line at every optimization level — a real,
narrow, gcc-specific cliff, not a boundary (that study's §4 traces the
mechanism: a 16-byte NEON chunk plus a 15-byte scalar remainder needing 4
more pieces tips gcc's own inliner threshold). Expect a regression against
`-fno-lit-run` there, on every subject kind, largest on first-byte
mismatch — and expect NOTHING like it at 25–30 or 32–40, which the study
already swept and found clean.

### Regime choice, and why not S2a's own micro-subjects

pcrec's `memcmp_lowering_study.md` times its candidate forms with a tight C
loop calling one comparison directly — an instrument this project does not
have. This harness times ONE driver invocation over ONE subject; at 2–40
bytes that invocation would compile, run and answer in far under a
microsecond, well under any per-call floor this harness can resolve (see
the floor pattern's own reading), and the reported median would be noise.

So every `lit-l<L>` gets THREE THROUGHPUT-SCALE subjects (`gen_
throughput_subjects.py`), each ~64 KiB, DENSE IN CANDIDATE STARTS by
tiling one small unit back-to-back — the same fix this project already
uses whenever it needs a per-call number against a busy background
(`bench/loglines`' size sweep, `bench/altwide`'s throughput arm):

| id | unit (length L) | what every ALIGNED window does |
|---|---|---|
| `mat-l<L>` | the literal itself | FULL MATCH — this is S7.2's "the literal itself (matching)" arm, tiled rather than singular |
| `fbf-l<L>` | the literal's own tail, byte 0 replaced by `#` | fails at the FIRST compared byte — S7.2's "first-byte flipped" arm |
| `lbf-l<L>` | the literal's own head, LAST byte replaced by `#` | matches `L-1` bytes then fails on the last — S7.2's "last-byte flipped" arm |

**Why the tiling cannot accidentally match or miss at the wrong offset**
(checked mechanically at generation time, `check_no_accidental_match` in
`gen_throughput_subjects.py`, not merely argued): every `lit-l<L>`
literal is drawn from a 52-DISTINCT-BYTE alphabet, so it has no internal
repeat and is not a rotation of itself. Tiling it (`mat`) therefore
matches at every ALIGNED window and at no other offset — a periodic string
with no smaller period has no other self-alignment. `fbf`/`lbf` replace
one byte with `#`, a byte that occurs in NO literal in this set
(`gen_patterns.py` asserts this for every pattern at generation time); a
full-length window over a period-`L` stream always contains exactly one
complete copy of the unit in some rotation, so it always contains the `#`
guard somewhere, and the (guard-free) literal can therefore never equal
ANY window, aligned or not. A brute-force check over two full periods
confirms this for every one of the eighteen `fbf`/`lbf` subjects at
generation time (zero exceptions raised); a direct Python `re.findall`
count against all 27 throughput subjects independently confirms the
predicted match count on every one (`mat-l<L>`: `65536 // L` byte for
byte on `len_of_subject // L`; `fbf`/`lbf`: exactly 0), reported in the
lane's own report rather than repeated here.

**S7.2's "length L-1" arm is realized differently, and NOT tiled**
(`bnd-l<L>`, `gen_subjects.py`): pcrec's P8 guard is `pos + L <= n`, where
`n` is the WHOLE subject's length — a property of where the buffer ENDS,
which happens exactly ONCE per subject, not something tiling can multiply.
`bnd-l<L>` is therefore a SHORT (`match`/`search_short`-regime) subject of
exactly `L-1` bytes (the literal's own first `L-1` bytes), scored
`nomatch` on `lit-l<L>` by length alone regardless of content — the
boundary-guard case S7.2 asks for, at throughput-irrelevant scale on
purpose.

## Subjects

27 short subjects (`manifest.tsv`, 1–100 B: the 2×2 set's 18 typed
hit/near-miss fields plus the L-sweep's 9 `bnd-l<L>` boundary subjects) and
27 throughput subjects (`manifest_throughput.tsv`, ~64 KiB each, 1,769,391
B total: the L-sweep's 9×3 dense tiled subjects). No prose, no random
draw — every byte here is an explicit, named construction
(`gen_patterns.py`'s header explains why this set carries no `Rng`, unlike
every other generator sub-bench).

**An emergent cross-term, not a bug, worth flagging so a future reader
doesn't mistake it for one**: `lit-l3`'s literal is `"abc"`, byte-identical
to `ctrl-abc-dollar`'s own literal prefix, so `bnd-l4` (`"abc"`, 3 bytes)
and `dollar-match` (`"abc"`) both genuinely match BOTH `lit-l3` and
`ctrl-abc-dollar` under `match`, and `mat-l3` (`"abc"` tiled ~21,845
times, ending exactly at the subject's own end) genuinely matches
`ctrl-abc-dollar`'s `$` exactly ONCE — the only tiled `lit-l<L>` subject
where a `$`-anchored pattern from a DIFFERENT cell finds anything at all,
because it is the only one whose tail happens to spell `abc`. The oracle
catches this correctly (`pattern_facts.tsv`'s `tput_mn` column for
`ctrl-abc-dollar` reads `1/27`, not `0/27`); no expectation here is
hand-computed, so no such coincidence needed to be anticipated for the
file to be correct.

## Predictions (I-113, transcribed before any run)

pcrec's inbox item I-113 (`docs/dev/inbox_from_pcrec.md`, 2026-09-27; full
text pcrec `docs/dev/lanes/s2a_report.md` §7) states five predictions.
**Only P4 and P5 are scored against THIS set** — P1, P2 and P3 name
patterns that live in `bench/bounded@0.3`, `bench/loglines@0.1` and
`bench/capability@0.1` (existing sets), and are scored against THOSE
sets' own reports, not litrun's. They are transcribed here in full anyway
so a reader has the whole ask in one place, and machine-readable rows for
them belong in `docs/dev/predictions/<that-set>-*.tsv` files, not this
one.

- **P1 — FASTER**: `ctx-lazy-*`/`ctx-greedy-*` (`bench/bounded`),
  `level-context` (`bench/loglines`) — the named population, largest on
  the no-context-word worst case. `wild-secrets-username-password-pair`
  and `wild-secrets-aws-access-key-id` (`bench/capability`, auto-caps):
  faster throughput. `wild-secrets-github-pat`/`slack-webhook-url`
  (`bench/capability`): small gain at most. **Scored against**:
  `bounded@0.3`, `loglines@0.1`, `capability@0.1`'s own reports.
- **P2 — FLAT to slightly faster**: `email-local-nodup`, `tag-pair-match`,
  `nested-comment-rec` (`bench/capability`, most likely to show it),
  `logparse-atomic(-removed)`, `tag-depth3-bound`, `quotedstring-grok`,
  `syslogbase-expanded` (`bench/loglines`/`bench/capability`). WATCH: a
  small regression on 2-byte runs on subjects failing at the first byte.
  **Scored against**: `capability@0.1`, `loglines@0.1`.
- **P3 — NULL**: every DFA-routed cell, in EVERY set. **Scored against**:
  every set's own report (a structural claim, not a named-pattern one).
- **P4 — the 2×2 (§7.1)**, litrun's own cells, above:
  - P4.a: `alt-foo-tails` — lit-run gains MORE with factoring DENIED (3
    runs, longer, each re-compared per branch retry) than with it ON (2
    runs, the shared `foo` compared once); factoring gains LESS with
    lit-run on than off.
  - P4.b: `wild-secrets-aws-access-key-id` — the cell MOST LIKELY to flip
    the sign of `-fno-altcls-factor` under lit-run (nine one-load 4-byte
    compares vs. an island's first-byte dispatch plus 3-byte tails).
  - P4.c/P4.d: `ctrl-abc-dollar`/`wild-secrets-github-pat` — controls:
    `-fno-altcls-factor` reads NULL (no alternation); only the lit-run
    column moves, a small gain at most on the github-pat control (one
    verify per match behind an exact hybrid window).
- **P5 — the L-sweep (§7.2)**, litrun's own cells, above:
  - P5.a: matching and last-byte-mismatch — faster from `L=4` up, growing
    with `L` (gcc's own decomposition: `L=7` is 3 pieces, `L=10` is 2,
    `L=16` is 2 or one NEON, `L=40` is 32+8).
  - P5.b: first-byte mismatch — flat, with a POSSIBLE small regression at
    `L=2`/`L=3` (a halfword load and the P8 test against one byte
    compare) — the per-call constant this sweep exists to catch.
  - P5.c: `L=31` — a named WATCH cell, expect a REGRESSION against
    `-fno-lit-run` on every subject kind, largest on first-byte mismatch
    (the gcc-specific `memcmp()`-out-of-line cliff).
  - P5.d: `L-1` (`bnd-l<L>`) — null (both forms fail on one bounds test).
  - **The pre-check confound, stated explicitly because the lane report
    itself flags it**: under DEFAULT pcrec flags, a NECESSARY run's
    failing subject is answered by the whole-window `req_run`/`req_byte`
    precheck — itself a P4-shaped memcmp — before the VM's own per-
    position compare is ever reached, so the default-flags row measures
    the PRECHECK, not S2a. Every L-sweep cell must therefore be read on
    TWO labelled arms: `default` and `-fno-req-run -fno-req-byte`
    (both build variables of the WINDOW's testee configs, not this set).

`docs/dev/predictions/litrun-0.1-first.tsv` carries P4/P5 as
machine-readable clauses, scorable against this set's own first report.

## Cell-time estimate

14 patterns × (27 match + 27 search_short + 27 throughput) subjects =
1,134 (pattern, subject, regime) cells per testee config. Every short
subject is <= 100 B (sub-millisecond per trial on any testee); the 27
throughput subjects are ~64 KiB each (1.73 MB total per config) — small
next to `bench/altwide`'s 128 KiB/512 KiB throughput arm or
`bench/syntax`'s 1 MB sweep, chosen deliberately small because the L-sweep
needs MANY independent per-attempt samples, not a large one-off scan
(NOTES.md above, "Regime choice"). `gen_expectations.py`'s own run over
this set completes in well under a second on this box (14 patterns, no
recursion, no unbounded class repeat) — this is the FAST set among
`bench/*/`, not the slow one `bench/altwide`/`bench/syntax` are.
