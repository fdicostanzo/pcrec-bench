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
  `bounded@0.3`, `loglines@0.1`, `capability@0.1`'s own reports —
  `docs/dev/predictions/bounded-0.3-litrun-a32bc86e.tsv`,
  `loglines-0.1-litrun-a32bc86e.tsv`,
  `capability-0.1-litrun-a32bc86e.tsv` (lane b108pred, 2026-09-27). All
  four named `bounded`/`loglines` cells and all eleven named `capability`
  cells were CONFIRMED to compile to the VM under `auto` at this pin,
  `RX_VM_LIT_RUNS` > 0 on every one (direct build against
  `build/pcrec-a32bc86e/build/pcrec`), so `pcrec-auto` vs
  `pcrec-auto-nolitrun` IS the vm/vm-nolitrun pair I-113 item 5 asks for
  wherever a named cell is VM — no separate forced-`--engine=vm` testee
  was needed for any of them.
- **P2 — FLAT to slightly faster**: `email-local-nodup`, `tag-pair-match`,
  `nested-comment-rec` (`bench/capability`, most likely to show it),
  `logparse-atomic(-removed)`, `tag-depth3-bound`,
  `wild-logparse-quotedstring-grok`, `wild-logparse-syslogbase-expanded`
  (`bench/capability` — the last two carry the `wild-logparse-` prefix in
  `bench/capability/patterns.rxt`; I-113's own text elides it). WATCH: a
  small regression on 2-byte runs on subjects failing at the first byte —
  already scored generically by this set's own P5.b/P5.g (no capability
  cell is a 2-byte-run pattern, so the watch names no NAMED cell here).
  **Scored against**: `capability@0.1`'s own report —
  `docs/dev/predictions/capability-0.1-litrun-a32bc86e.tsv`. (I-113's own
  text also lists `logparse-atomic(-removed)` under `bench/loglines`
  alongside `syslogbase-expanded`; both patterns were found ONLY under
  `bench/capability`'s `patterns.rxt` — confirmed by grep across every
  `bench/*/patterns.rxt`/`subbench.toml` — so all eight P2 cells are
  scored against `capability@0.1` alone, none against `loglines@0.1`.)
- **P3 — NULL**: every DFA-routed cell, in EVERY set. **Scored against**:
  one representative DFA-routed control per set (confirmed `RX_ENGINE
  "dfa"` by direct build), since the claim names no specific pattern:
  `cls-upto-64` (bounded), `iso-ts` (loglines), `router-prefix-order`
  (capability) — the same three predictions files as P1/P2.
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
  - All four clauses are scored on the DEFAULT pair (`pcrec-vm` vs
    `pcrec-vm-nolitrun`, exact testee ids `pcrec_a32bc86e_vm-caps-simdna`
    / `..._nolitrun`) — a compile-time byte-count claim, unaffected by
    the pre-check confound below.
- **P6 — the 2×2's TIMING half, NEW (lane b108pred, 2026-09-27)**: P4
  above is a compile-fact claim (`emit_bytes`); this scores `median_ns`
  over the same throughput subjects the L-sweep uses (set-grain, all 27,
  no filter — these four patterns carry `tput_mn` 0/27 or 1/27 in
  `pattern_facts.tsv`, so this is a failing/near-failing SCAN cost, where
  a per-candidate literal-run compare is visible), on all FOUR corners of
  `{default, -fno-altcls-factor} × {default, -fno-lit-run}`, on BOTH
  engine routes (`vm` and `auto`):
  - P6.a-d: `alt-foo-tails`, both routes × both factoring columns —
    lit-run faster than `-fno-lit-run` WITHIN each factoring column
    (the per-column direction, not the cross-column one P4.a reads).
  - P6.e-h: `wild-secrets-aws-access-key-id`, the same four cells — **NO
    DIRECTION PREDICTED**. I-113 §7.1 names this pattern's cell (a') the
    one MOST LIKELY TO FLIP THE SIGN of factoring under lit-run, an
    explicitly OPEN empirical question in the lane report's own text;
    scored `op present` (the ratio must be MEASURABLE, nothing about its
    direction) rather than inventing a `lt`/`gt` this project has no
    grounds to state (R-BENCH's "must not happen" rule).
  - P6.i-l: the two controls (`ctrl-abc-dollar`, `wild-secrets-github-pat`),
    both routes — the FACTORING axis reads NULL (`between 0.85 1.15`,
    default vs `-fno-altcls-factor`, lit-run held at its own default on
    both arms), restating P4.c/P4.d's own "factoring reads NULL there"
    as a timing claim.
- **P5 — the L-sweep (§7.2)**, litrun's own cells, above:
  - P5.a: matching and last-byte-mismatch — faster from `L=4` up, growing
    with `L` (gcc's own decomposition: `L=7` is 3 pieces, `L=10` is 2,
    `L=16` is 2 or one NEON, `L=40` is 32+8).
  - P5.b: first-byte mismatch — flat, with a POSSIBLE small regression at
    `L=2`/`L=3` (a halfword load and the P8 test against one byte
    compare) — the per-call constant this sweep exists to catch.
  - P5.c: `L=31` — the named WATCH cell, **RESTATED** (lane b108pred,
    2026-09-27): pcrec's own `docs/dev/memcmp_lowering_study.md` cliff is
    ARM64 GCC-16 ONLY. This box is x86_64 gcc 15.2.0 at -O2 (the
    project's own phase-2 compile flags), where `memcmp(p,q,L)==0` is
    INLINED at every `L = 1..64` — confirmed twice: on a synthetic loop
    (`docs/dev/measurements/2026-09-27-x86-gcc15-memcmp-lowering.txt`,
    merged from master) and, this lane, on the REAL `lit-l31` forced-VM
    artifact itself, built through the harness's own adapter compile path
    (`objdump -T`/`readelf -r`/`objdump -d`, zero memcmp references —
    `docs/dev/measurements/2026-09-27-litrun-l31-artifact-memcmp.txt`,
    `probe_b108_litrun_l31_memcmp.py`; `lit-l16` as the control, same
    result). **On this box L=31 is predicted IN LINE with its L=16/L=40
    neighbours** — split into `c.matlbf` (same "faster" threshold as
    P5.a's own L=16/L=40 rows) and `c.fbf` (same "flat" threshold as
    P5.b's own L=4/L=40 rows) rather than the old single combined-subject
    regression claim. Kept named as the WATCH cell: a toolchain, flag or
    gcc-version change on this box should re-run the archived probe
    before trusting either clause again.
  - P5.d: `L-1` (`bnd-l<L>`) — null (both forms fail on one bounds test).
  - **The pre-check confound, stated explicitly because the lane report
    itself flags it**: under DEFAULT pcrec flags, a NECESSARY run's
    failing subject is answered by the whole-window `req_run`/`req_byte`
    precheck — itself a P4-shaped memcmp — before the VM's own per-
    position compare is ever reached, so the default-flags row measures
    the PRECHECK, not S2a. Every L-sweep cell is therefore read on TWO
    labelled arms (lane b108pred, 2026-09-27 — re-aimed and split
    explicitly rather than left as a stated caveat):
    - **PRIMARY** (P5.a/b/c/d, above): `pcrec-vm-noreqbyte-noreqrun` vs
      `pcrec-vm-noreqbyte-noreqrun-nolitrun` — both whole-window
      pre-checks denied, so a failing subject reaches the VM's own P4
      compare (or, on the nolitrun sibling, the pre-abi-41 chain) instead
      of being answered by the pre-check first. This is the pair that
      isolates S2a on its own.
    - **DEFAULT, a LABELLED SECOND ROW** (P5.e/f/g): `pcrec-vm` vs
      `pcrec-vm-nolitrun`, no denial. On this pair the pre-check answers
      a failing subject before the VM compare is ever reached, so
      **fbf/lbf read NULL here** (P5.f, P5.g: `between(0.85, 1.15)`) and
      **mat is the only faster claim** (P5.e: same threshold as P5.a) —
      the pre-check's own prefix-scoped scanned byte/run does not move
      on a last-byte flip, so P5.f's reasoning differs from P5.g's (see
      each clause's own note in the TSV) even though both read NULL.

`docs/dev/predictions/litrun-0.1-first.tsv` carries P4/P5/P6 as
machine-readable clauses (53 rows: P4 a-d; P5 a/b/c/d on the PRIMARY pair,
e/f/g on the DEFAULT pair; P6 a-l, the §7.1 2×2's timing half), scorable
against this set's own first report.
Every `testee=` selector spells the EXACT derived testee id at this pin
(`pcrec_a32bc86e_...`, verified against `pcrecbench.record.
derive_testee_id`/`testees/pcrec/adapter.py`'s own `describe()`) rather
than a `pcrec_*_...` pin wildcard: unlike this file's own first cut, a
wildcard here would ALSO match a future re-pin's own `-nolitrun` sibling
(every prior deny testee — `-noreqbyte`, `-noclsfold`, … — has kept its
config across every later re-pin), silently pooling two different pins'
programs under one `ratio_to` the moment a report spans both — the same
class of cross-pin-pairing defect [B87]/I-108 fixed for the null-control
band's own cross-class query. `check_testee_globs` reads
`pcrec_a32bc86e_...` as NONE-YET-MEASURED for `bounded`/`loglines`/
`capability@0.1` today (those sets already carry OTHER pins' measured
records, so the check is non-vacuous and fires until this pin's own
window runs) — expected, not a defect: the SAME shape every fresh-pin
predictions file in this directory has at authoring time (confirmed
against `capability-0.1-noreqbyte-twin-02902356.tsv`, whose own pin has
SINCE been measured). `litrun-0.1-first.tsv` itself is vacuous either way
(litrun@0.1 has never been measured at any pin).

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
