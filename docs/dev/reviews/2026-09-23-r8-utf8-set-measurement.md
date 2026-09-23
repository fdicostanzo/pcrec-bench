# R8 — `docs/design/utf8_set_v1.md` v0.1, MEASUREMENT VALIDITY lens

Critic: read-only, D6 panel, 2026-09-23. Subject: `docs/design/utf8_set_v1.md`
v0.1 (1,166 lines, read in full), chartered by inbox I-90
(`docs/dev/inbox_from_pcrec.md:3071-3170`). Scope: this file only; no
build, no timed anything, `~/pcrec` read-only.

Evidence sources beyond the design note itself: `docs/dev/inbox_from_pcrec.md`
I-90/I-93; `docs/dev/plan.md` [B78]/[B79]; `docs/dev/predictions/CLAUDE.md`;
`pcrecbench/interpret.py` (the `QUANTITIES`/`REDUCERS`/`OPS`/`SELECTOR_KEYS`
closed sets and the `_reduce`/`ratio_to`/`ratio_max_min_over` mechanics);
`bench/capability/captext.py` and `bench/capability/CLAUDE.md` (the only
built precedent for the throughput-text generator this note says
`utf8text.py` will copy the shape of); `store/index.tsv` (real capability@0.1
timestamps from tonight's window, as an empirical cross-check for §10).

---

## F-M1 — BLOCKER: nothing in the design guards multi-byte throughput
subjects against a byte-exact truncation that lands mid-character

**Line cite:** §4.1 (`utf8_set_v1.md:274-296`), §4.3 (`:326-349`), §8.2
(`:768-787`).

**The claim disputed.** §4.1 says `utf8text.py` is "the shared xorshift64\*
primitive in `bench/syntax/censustext.py`'s shape, which
`bench/capability/captext.py` already reuses" and composes per-script word
pools "into sentences and paragraphs" to hit the throughput sizes named in
§4.3 (64 KB/256 KB/1 MB for `mix`, a 64 KB arm per script). Nowhere does
the note require that the size-fitting step preserve UTF-8 well-formedness
at the cut point.

**Evidence, both sides checked.** I read the one built precedent for this
exact generator shape, `bench/capability/captext.py:100-118`:

```python
def text(nbytes, seed):
    ...
    while total < nbytes:
        kind = rng.choice(_LINE_KINDS)
        line = kind(rng)
        if total + len(line) + 1 > nbytes:
            remaining = nbytes - total - 1
            if remaining > 0:
                out.append(line[:remaining])
            break
        ...
    return ("\n".join(out) + "\n").encode("ascii", "replace")
```

`line[:remaining]` is a **raw byte-offset slice** applied to hit an exact
target size. This is safe today only because `captext.py`'s alphabet is
ASCII (1 byte = 1 character, `.encode("ascii", "replace")` at the end is a
no-op on well-formed input). §4.1 states `utf8text.py` is built "in
[this] shape" — i.e., the same trim-to-fit loop — over word pools whose
bytes are 2-, 3- and 4-byte UTF-8 sequences (`cyr`, `cjk`, `mix`'s emoji).
A naive port of `line[:remaining]` (or any byte-offset trim) to that
alphabet will, on most target sizes, cut inside a multi-byte sequence and
leave an **ill-formed UTF-8 tail** on the subject file.

§8.2, three paragraphs into the SAME document, states the consequence
in its own words: *"plain `PCRE2_UTF` REFUSES an ill-formed subject
outright"* — and by extension every other UTF-8-aware engine on the
roster documents some non-match behaviour on ill-formed input (§8.3).
That refusal is deliberately engineered and welcomed for growth (h)'s
hand-authored ill-formed subjects — but here it would land, unannounced,
on **every throughput subject that isn't `asc`**, at every size, because
the byte-fitting step is a generic utility this note gives no boundary
rule for. This is not a corner case: the odds that a xorshift-driven
trim of Cyrillic/CJK/emoji text happens to land on a character boundary
by chance are low, so the DEFAULT expectation, absent a fix, is that
this fires on nearly every corpus/size pair.

**Why this is a measurement-validity BLOCKER and not a build nit.** The
population this would corrupt is exactly the one §10's arithmetic, §11's
P2/P3, and §12's R3/R4 are built on — the throughput regime, the
per-script 64 KB arm, and the histogram claim (§4.2) that the whole set
exists to make checkable. A silent ill-formed tail would not surface as
a clean `did-not-compile` row (compile-time refusal, visible in the
matrix surface) — it is a **match-time** failure per subject, on a
regime with no `match` expectations to catch a wrong-answer outcome
cleanly, and depending on how the adapter's UTF error code is bucketed
by `harness.outcome_for()` it could land as an unremarked `gave-up` or
even (if a range-based give-up classifier does not recognize the
engine's specific UTF error code) as a genuine wrong-answer or crash —
none of which anyone would trace back to the generator without
inspecting raw bytes.

**Disposition proposed.** Add to §4 (and to U3's charter in §13) an
explicit requirement: the trim-to-fit step in `utf8text.py` backs off to
the last COMPLETE character at or before the byte budget (decode-and-
truncate, or a byte-by-byte `try: s[:k].encode(); except UnicodeDecodeError:
k -= 1` walk-back), and `gen_subjects.py --check` / `gen_throughput_
subjects.py --check` assert every committed subject **round-trips through
`bytes.decode("utf-8")` with no error** before its manifest row is written
— the same kind of belt-and-braces control `gen_throughput_subjects.py`'s
own `_redos_safety_check` already sets a precedent for (empirically
verify a structural argument, don't just assert it). This is a
one-paragraph fix to the design and a small, mechanical fix to the
generator; it is a BLOCKER only in the sense that U3 must not open
without it stated, not because it is hard.

---

## F-M2 — MAJOR: P1–P10 are asserted machine-scoreable but never
transcription-tested, and at least three clauses use vocabulary the
closed `QUANTITIES` set does not literally contain

**Line cite:** §1.1 clause 5 (`:78`), §11 header (`:974-985`), P2/P3
(`:995-1006`), P4 (`:1007-1013`), P5/P7/P9 (`:1014-1019`, `:1024-1031`,
`:1039-1045`).

**Checked against `pcrecbench/interpret.py`'s own closed sets**
(`QUANTITIES`, `REDUCERS`, `OPS`, `SELECTOR_KEYS`, lines 1948-1962):
there is no bare `emit_bytes` quantity (only `compile:emit_bytes`), no
`ns_per_byte`/`ns/byte` quantity of any spelling, and no `compile_outcome`
quantity at all. Every one of these appears in §11's prose:

- P2/P3 speak of "`throughput` ns/byte" — not a scoreable token by name.
- P4 speaks of "`emit_bytes`" bare — the real token is `compile:emit_bytes`.
- P5/P7/P9 speak of "`compile_outcome = unsupported-by-declaration`" /
  "`compile_outcome = did-not-compile`" — neither is a `QUANTITIES`
  member; the only path to that fact is the `section` selector key
  (a row's membership in the `unsupported_by_pattern` / `did_not_compile`
  section of the TSV), read via `quantity=section` with `reducer=count`
  or `set_of` — a mechanism this project has used before
  (`docs/dev/predictions/CLAUDE.md:106-113`'s worked example) but that
  this note never demonstrates for its own patterns.

**Both sides checked.** None of this is fatal by construction — I traced
through `_reduce`'s actual mechanics (`interpret.py:2367-2485`) and
confirmed a working path for each:
- P2/P3's "ns/byte" claims are comparisons **on the same subject**
  (`:997-998`, `:1004-1005` — "on the same subject" is stated explicitly
  both times), so the byte denominator cancels in a ratio and plain
  `median_ns` with `reducer=ratio_to(pattern=...)` scores them exactly —
  no `ns/byte` quantity is actually needed. This resolves cleanly.
- P4's `compile:emit_bytes` fix is a one-word correction.
- P5/P7/P9's `section`-based path is real (cited above) but INDIRECT
  enough — existential quantifiers ("at least one family-(f) pattern"),
  cross-testee comparisons (default-cap vs `-bigcap` sibling) — that I
  would not bet all three transcribe cleanly on the first attempt
  without a dry run.

**Why this matters for measurement validity specifically.** A prediction
that turns out inexpressible at first-run time is not merely an
inconvenience — it is exactly the failure mode `docs/dev/predictions/
CLAUDE.md`'s own opening line names as R-PRED-3's reason for existing
("a prediction nobody re-read is a prediction nobody scored"), and this
note explicitly declines to pre-commit the TSV (§11 preamble, "NOT
committed by this note … the transcription happens at first-run time").
`interpreter_v1.md`'s OWN acceptance discipline required its worked
predictions format to be "TESTED against `bench/syntax/NOTES.md`'s
P1-P13 (12 of 13 expressible)" before the interpreter shipped — i.e.
this project's own house standard is to dry-run a prediction set against
the real grammar before trusting it. This note does not do that for
P1-P10 (it cannot yet — the patterns do not exist), but it also does not
flag the gap as owed, unlike, e.g., §11's own explicit prose-only carve-out
for P1.b.

**Disposition proposed.** Before U5 authors `expectations.tsv`, hand-
transcribe P1–P10 into the real fifteen-column grammar against the built
patterns (even a stub/dry pass) and fix any clause that does not parse —
folding the fix into `NOTES.md`'s own predictions section rather than
leaving §11's prose as the only record of what was meant.

---

## F-M3 — MAJOR: §10's cell-time arithmetic is probably optimistic, not
conservative, against the only real timing evidence available tonight

**Line cite:** §10.3 (`:942-970`), §15 R3 (`:1162`).

**Recomputing the stated arithmetic.** `search_short`: 74 patterns × 6
passes × (50 ms × 90 subjects) = 74 × 6 × 4.5 s = 1,998 s ≈ **33.3 min**
— matches the table's "~33 min" exactly. `throughput` + pcrec compile
add the stated 5-12 min and 2-4 min. The internal arithmetic is
self-consistent; I found no error in it on its own terms.

**Cross-checked against real numbers, not analogy.** `store/index.tsv`
carries four `capability@0.1` records written TONIGHT (2026-09-23, the
`[B74]`/`8d716693` AFTER window, same box, same D119/BD7 machinery this
note's §10 model is copied from):

```
03:19:41Z  measured
03:55:07Z  measured   (+35m26s)
04:26:32Z  measured   (+31m25s)
05:09:23Z  measured   (+42m51s)
```

That is **31–43 min per pcrec cell**, measured, tonight, on
`bench/capability@0.1` — 64 patterns (`bench/capability/CLAUDE.md`) × 75
short subjects, `short_search_max_bytes = 512` (same as this note's
choice), 3 throughput sizes (`captext.py`, ~1.34 MB combined, no
per-script arm).

Applying §10.3's OWN formula to capability's population: `search_short`
alone = 64 × 6 × (50 ms × 75) = 64 × 6 × 3.75 s = **1,440 s ≈ 24 min**.
That leaves only **7–19 min** of the observed 31–43 min total for
capability's throughput + compile — plausible, but it means the
`search_short` component is the dominant cost on the real box, exactly
as the formula assumes.

utf8@0.1 asks for **1.39×** capability's `search_short` load (74×90 vs
64×75) and a throughput corpus that is not just bigger in bytes (~1.58 MB
vs ~1.34 MB) but structurally different (a per-script 64 KB arm crossing
four scripts, none of which is a byte-uniform ASCII/log-line mix — a CJK
64 KB subject decodes roughly 3× fewer characters per byte than
`captext`'s output, which may or may not matter for a `median_ns`-per-call
loop depending on whether the dominant cost is decode-bound or
scan-bound; this note does not say which, and it is the one place a
real per-byte cost difference between scripts could show up in the
CALIBRATION step itself, not just in the measured result). Scaling only
the `search_short` component by 1.39× (24 min → 33 min) before adding
ANY throughput/compile time already exceeds the low end of the stated
40-45 min pcrec-cell estimate, using capability's own real 7-19 min
throughput+compile allowance as a floor.

**Conclusion.** §10's model is not wrong on its own terms, and I found
no arithmetic error — but weighed against the one piece of real evidence
available (tonight's capability window), the **~40-45 min/cell estimate
reads as the optimistic end of a plausible range, not a conservative
one**, which means §15 R3's "~2× CELL_CAP headroom" is probably
overstated in the safe direction — real headroom may be closer to
1.5-1.8× than 2×.

**Disposition proposed.** Treat R3's two pre-priced levers (drop the
per-script 64 KB throughput arm; cut short subjects 90→75) as a
**default pre-cut for the first sample**, not a reserve to pull only if
a cell is observed to overrun — cheaper to under-spend the budget once
than to have a `CELL_CAP` timeout mid-window cost a full re-measure
under `run_window.sh`'s once-only retry rule.

---

## F-M4 — NOTE: Q1 (does `asc` rank) — both sides, and the practical
answer is smaller than the question suggests

**Line cite:** §14 Q1 (`:1143`), §4.2 (`:316-324`).

Arguing FOR ranking `asc` (the note's own recommendation): R3 and P8 are
both **scoring** rules, and a `pcrecbench interpret` clause can only
bound a value that exists in a ranked/scored population — a
provenance-only `asc` cannot be the target of an `op=lt/gt` clause at
all, so "RANK it" is not really a stylistic choice, it is a
precondition for R3/P8 to be machine-checkable claims rather than
eyeballed ones.

Arguing the other side, on **measurement** grounds specifically (the
lens this review is scoped to, not the provenance argument the note
already makes): a set-grain `throughput` cell sums per-subject ns/call
across the WHOLE regime's subject population per trial (`reduce.py`'s
`reduce_set_cell`, cited in `pcrecbench/CLAUDE.md`). The `mix` corpus's
1 MB subject is roughly **65% of the combined ~1.58 MB throughput byte
total** (1,024 KB of 1,600 KB across all seven subjects) — so whether
`asc`'s ~64 KB (≈4% of the total) counts toward the blended
`throughput` ranking number moves that number by a few percent at most.
The place `asc`'s inclusion or exclusion actually matters is the
PER-SUBJECT row, which `_per_subject_subtable`'s R9 rule
(`pcrecbench/CLAUDE.md`, "[B16]") already renders unconditionally on any
`large-subject-throughput` cell regardless of subject count (it fired at
5 and 12 subjects elsewhere, not only ≤3) — so a reader can already see
`asc`'s own row whether or not it is folded into the blended ranking
number.

**Disposition proposed.** Rank it, as recommended, but for the
PRECONDITION reason (R3/P8 need a scoreable row), not primarily the
provenance framing the note leans on — and say in `NOTES.md` that the
blended `throughput` ranking number is expected to move only marginally
either way, so a reader does not go looking for a large effect in the
wrong place.

---

## F-M5 — NOTE: R3 (the encoding band, §12) is well-formed at
`throughput` grain only; its `search_short` applicability is unstated

**Line cite:** §12 R3 (`:1073-1079`), §4.3 (`:335-342`).

R3 compares a pure-ASCII pattern's cell against "the SAME pattern's same
cell on the `asc` subject population." At `throughput` grain this is
exercisable exactly as designed (the per-script 64 KB arm gives every
pattern a same-size cross-corpus comparison, `asc` included). At
`search_short` grain, §4.3 says short subjects are typed "per family...
in that family's own script" (singular) — for the three named pure-ASCII
patterns (the floor, `ci-ascii-control`, `asr-b-ascii`), that script is
presumably ASCII/English by construction, so there is no OTHER-script
`search_short` population for the SAME pattern to compare against. R3 as
literally worded ("a cell", not "a `throughput` cell") reads as if it
applies at both grains; at `search_short` grain it appears structurally
inapplicable for exactly the three patterns it is about.

**Disposition proposed.** State in `NOTES.md` that R3 fires at
`throughput` grain only, or — if cross-script `search_short` subjects
for these three patterns are actually intended — say so explicitly and
add the subject count to §10.3's budget (not currently included in the
90-subject total).

---

## F-M6 — NOTE (design question, not a requirement): the null-control
band's near-term power on THIS set is structurally weaker than on a
mature set, though not foreclosed

**Line cite:** relates to `docs/dev/plan.md` [B79] (STATE:not-started)
and inbox I-93 BLOCK B (`docs/dev/inbox_from_pcrec.md:3205-3212`), and
to `utf8_set_v1.md` §9 (`:873-909`).

**Does this design leave room for a program-identical null population?**
Yes, structurally — nothing about the `-e utf8` configs (§7.2) exempts
them from the same before/after compile-row emit-hash comparison that
gave tonight's `capability@0.1` batch-1 AFTER its 56/187 program-identical
population (`docs/dev/inbox_from_pcrec.md:3183`). Every pcrec compile row
in this set carries `emit_bytes`/`emit_code_bytes` (§10.2 says so
explicitly), which is the exact input B79's plan names ("the compile
rows' emit hashes").

Two caveats worth stating as a design question, per the brief's own
framing, rather than a requirement this note must satisfy today:

1. **The four `pcrec-*-utf8` testee ids have zero re-pin history at
   first release.** A null population needs a BEFORE/AFTER pair of
   records for the same testee-id-minus-pin; `utf8@0.1`'s first sample
   is a single pin by construction (§10.3's own "first sample" framing),
   so the null band is uncomputable for this set until its SECOND
   measured pin. Not a flaw — but a reader expecting a null band from
   this set's very first report would be surprised, and the note does
   not say so anywhere.
2. **This set's own reason for existing works against the null band's
   power in exactly the window it would be most useful.** I-90's charter
   motivation (`docs/dev/inbox_from_pcrec.md:3078-3088`) is pcrec's
   ACTIVE utf8-specific optimization work — `[OPT-OFSK]`'s
   frequency-informed pick, `[OPT-REQPOS]` 2b — targeting precisely the
   code paths this set's patterns exercise. A mature set like
   `capability@0.1` gets a large program-identical population BECAUSE
   most of a given re-pin's diff is orthogonal to most of its patterns;
   `bench/utf8`'s early re-pins are disproportionately likely to be
   utf8-encoding-specific commits touching utf8-encoding-specific
   patterns, so the near-term program-identical fraction on this set
   should be expected LOWER than capability's 30% (56/187), not similar
   to it — thinning exactly the population B79 needs, exactly when
   `bench/utf8` is newest and most in need of a noise floor to read its
   own first findings against.

Neither point blocks this design. Recommend a sentence in §9 (or a new
§14 question) naming both, so the FIRST `bench/utf8` reader does not
mistake "no null band available yet" for "the band doesn't apply here."

---

## F-M7 — NOTE: v1.4 trial-agreement constants were calibrated on a
byte-mode corpus; this set is the first to exercise a decode-bound timing
profile at scale

**Line cite:** relates to `docs/design/gate_shape_v14.md` (`v1.4-group`,
k=1.5, d_min=2, share_c=3, N≥5 odd, "constants measured over the store's
68 records" per the top-level `CLAUDE.md`'s [B20] entry) and
`utf8_set_v1.md` §8.4 (`:819-853`).

The trial-agreement rule that decides `measured` vs `inconclusive-spread`
was fit to a store of byte-mode, largely ASCII/log-line-shaped timing
distributions. `bench/utf8` introduces (a) a materially different
subject byte-structure (multi-byte decode work interleaved with the
scan) and (b) per §8.4, a genuinely new find-all advance rule in both
oracle and driver. Nothing in v1.4's design assumes byte-uniform text,
and I found no reason to expect the trial-agreement arithmetic itself to
misbehave — but its constants have never been checked against a
decode-bound population, and this is the first set that is one at scale.
This is speculative, not a finding of an actual defect.

**Disposition proposed.** No design change owed. Cheap post-hoc check
once the first `bench/utf8` window runs: compare its `inconclusive-
spread` rate against the store's historical rate; a large deviation
would be worth a look at whether v1.4's constants still fit a
decode-bound cell.

---

## Verdict

One BLOCKER (F-M1: the throughput generator's byte-exact size-fitting
step, inherited in shape from a byte-mode precedent, has no stated
guard against cutting a multi-byte subject mid-character, which under
this same document's own §8.2 rule would silently corrupt the entire
throughput regime with hard refusals rather than measurements) and two
MAJOR findings (F-M2: P1-P10 are asserted machine-scoreable without ever
being transcription-tested against the interpreter's real closed
vocabulary, and at least three clauses use quantity names — bare
`emit_bytes`, `ns/byte`, `compile_outcome` — that do not exist in
`QUANTITIES` as spelled, though each has a working indirect path I could
trace by hand; F-M3: §10's cell-time arithmetic, while internally
consistent, reads as the optimistic end of the plausible range when
checked against tonight's real `capability@0.1` timings on this same
box, which thins the already-flagged R3 headroom risk further than
stated) are the substantive risks to this design's measurement claims.
The remaining four are notes worth one sentence each in the next
revision but block nothing. None of the seven findings requires
rethinking the set's shape, families, or scope — they are all about
whether the FIRST sample will produce trustworthy numbers rather than
silent refusals or an overrun window, which is exactly what a
measurement-validity pass should be checking before a build lane opens.
