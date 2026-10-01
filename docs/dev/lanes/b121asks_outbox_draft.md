# lane b121asks — DRAFT outbox items (NOT committed to outbox_to_pcrec.md)

For the manager's review and wording at merge time. Numbered as O-80
provisionally (the live file's last entry is O-79); the manager assigns
the real number when sending.

---

## O-80 (DRAFT) — I-125 A1-A5 + bench-only questions: answers, two new
testees, altwide@0.3, and three asks back

Full derivation: `docs/dev/lanes/b121asks_report.md`. Summary for the
inbox:

**A1/Q1 — already satisfied.** `bench/email`'s `t-d-prose-sparse-addrs`
([B17], email-specimen@0.2) is already the non-periodic 1 MiB
address-bearing subject you asked whether we had: 496 matches on `orig`,
generator `gen_throughput_subjects.py`'s `build_prose`, seed 20260828,
sha256 `d55c0e8f...9d94242`. We can time `orig`/`auto`/find-all on it
against `pcre2-jit`/`re2` whenever a window opens; say so if you still
want that cell specifically (it would otherwise ride our own standing
re-measure).

**A2/Q7 — the nest family is NOT the shape you're asking about.** A real
structural parse (not a text regex) of every pattern in every sub-bench
finds exactly ONE `(?:ab){m,n}`-shaped (or all-singleton-alternation)
counted repeat anywhere: `bench/utf8`'s `qnt-counted-3b`,
`(?:日本){2,}`. **`bench/bounded`'s `nest2-*`/`nest3-*` family — which
you named as "the candidate instrument" since 2026-08-31 — is a
DIFFERENT mechanism shape**: every nest pattern is `(?:CLASS{p,q}){m,n}`
(e.g. `(?:\d{1,4}){1,4}`), a counted repeat of a bounded CLASS that
itself carries an inner counted repeat, not a repeated literal STRING or
an all-singleton alternation. **Ask: is [OPT-5]'s period-k trigger meant
to fire on the nest family's own `(?:class){m,n}{p,q}` shape, or
specifically on a `(?:ab){m,n}`-shaped literal-string repeat?** If it's
the latter, the nest family was never going to trigger it and
`qnt-counted-3b` is the bench's only candidate cell today — small (6
UTF-8 bytes × a 2+ repeat), so a timed reading is cheap whenever useful.

**A3/Q6 — confirmed, one witness, nothing new.** The same real-parse
discipline over the whole corpus finds EXACTLY the one cell you already
named, `wild-waf-crs-942360-concat-sqli`, and no second one. The row
stays a single-witness candidate by your own stated rule.

**A4/Q8 — no clean witness existed; we built one.** Every real
>=8-branch alternation with a class-tail/member branch in the corpus is
a complex hand-authored pattern where the class shape is a minority
among differently-structured branches (five hits, three distinct
patterns — see the report). We built `altwide@0.3`: six patterns,
`clsa-{64,256,1024}` (trailing `[a-z]`) / `clsd-{64,256,1024}` (trailing
`[0-9]`), the clean isolated shape. **A compile-only census against your
own fc719ca4 binary already confirms your own prediction directly**:
`RX_VM_ALT_ISLANDS "0"` / `RX_VM_ENTRY_SHAPE "plain"` on every forced-VM
member at every width it compiles — the island is declined, exactly as
your inbox text said it would be. `clsa-1024`/`clsd-1024` refuse on
BOTH engine routes (both within 2.2% of your two emitted-size caps — a
knife-edge rung, not a design accident). A TIMED reading (the VM route's
actual chain cost on this shape, against the plain `w-256` and its
`-fno-alt-island` denied sibling) is queued for our next window.

**Q2/Q3 — built, with one honest finding.** `pcrec-vm-nocaps`(-in) and
forced `pcrec-dfa`/`pcrec-dfa-nocaps` are now pinned testees, witness-
verified per REQUIRES token (not inferred). The "reverse population"
your own Q3 named — auto picks VM, a forced DFA would have won — is
**measured EMPTY on `bench/capability@0.1` and `bench/syntax@0.1`, both
forms, as of fc719ca4**: your `auto` selector already prefers the DFA
whenever it can represent the pattern at all under `--no-captures`, and
wherever both configs compile they are PROGRAM-IDENTICAL (byte for
byte, not just same-answer). We're keeping the testee anyway — an empty
population on two corpora isn't proof it stays empty on `altwide` or
under a future heuristic change — but as of today there is no cell
where this instrument reads anything `pcrec-nocaps` doesn't already.

**Q4 — `lka-neg` is a match-dense cell, `lka-pos` is match-sparse, by a
factor of ~60-110×.** From the oracle's own expectations (both patterns
have a fixed 4-byte match width, the lookahead being zero-width):
`lka-pos` density 0.009-0.018% across the three throughput subjects,
`lka-neg` density 1.03-1.07% (flat across all three sizes). That is a
real execution-side asymmetry behind "identical compile-time stamps,
opposite large-subject-throughput verdicts" worth folding into whatever
reading explains the two cells diverging.

**Q5 — we could not find the exact citation.** `esc-octal-0 1.047×` on
a `short-subject-search` cell does not appear verbatim in any committed
syntax report or ledger we could locate; the nearest match is
`esc-octal-0`'s ×0.959 against the floor on
`pcrec_751b9c6d_vm-in-caps-simdna` (`...fullroster-751b9c6d.interpretation.md`
line 294), which is a different number and testee. **Could you name the
report/date/testee the four "other"-bucket cells are read from?** In
the meantime: the substance is that a `measured` (not
`inconclusive-spread`) 5-trial pinned record has already passed our
v1.4 trial-agreement gate, which is specifically built to catch the
single-launch CPU-governor bimodality O-69 found — so a ratio in that
1.03-1.23× range on such a record sits structurally above what a raw
single-launch artifact could produce, though we have not separately
characterised a tighter floor for a 5-trial median the way O-69
characterised the single-launch one.

**Q9 — no bench consumer waits on any DD-13 residual** (composed
delivery W1.3.1, `(?&site.group)`, grouplist W1.4); your own
`w13_report.md` §7's "`floor` collides exactly once, and that collision
is CROSS-SET" still holds, re-verified structurally at our current
corpus size.

**Q10 — not a bug, a declared absence.** `bench/capability@0.1` declares
NO `match` regime at all (`search_short` + `throughput` only), so a
`match`-grain lookup for `date-nested-plus` or any of the 17
capture-forced hybrids correctly returns nothing. **If you want a
realistic (1 KiB-64 KiB) match-regime subject for the 17 hybrids, that's
a real ask** — a `capability@0.1` set-version bump we haven't built
(not assuming you want it; say so and we will).

**Q11 — folded into our next window**, same `capability@0.1` cell your
own standing re-measure already needs.

**Q12 — no separate slot to negotiate.** Frank's standing ruling
(our I-35) already partitions our blocking windows to overnight and
your lanes/tests to daytime; our own plan.md queue puts [B121]'s A5
window right after today's [B117] olevel read, at the unchanged
fc719ca4 pin, in our next night window.

**A5 — the standing re-measure is mostly OWED, not run yet.** Only
`capability@0.1`'s `auto`/`vm` (caps) pair has an fc719ca4 record today
(from [B117]'s own olevel window); `utf8@0.1`, `syntax@0.1`, `loglines`,
`bounded`, `altwide`, `email` have zero. Full plan (cells, per-cell
duration estimates from each set's own NOTES.md, suggested chunking) is
in `docs/dev/lanes/b121asks_report.md`'s own A5 section — roughly two
nights, `syntax@0.1` alone filling one. **One gap found while planning
it: `bench/utf8` has no `-utf8` sibling for the new `pcrec-vm-nocaps`/
`pcrec-dfa`/`pcrec-dfa-nocaps` testees** (Q2/Q3's testees are byte-mode
only) — if you want a forced-DFA/VM-nocaps reading on `utf8@0.1`
specifically, those three testees need building first; we did not build
them speculatively since I-125 named `syntax@0.1`/`bench/capability`,
not `bench/utf8`, for this pair.

Nothing in this item changes a pinned tier or a pin; everything above
is compile-only or read-only, no timing taken.
