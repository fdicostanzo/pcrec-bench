# lane b121asks — plan.md [B121], inbox I-125 — report

Branch `lane/b121asks`, pin fc719ca4 throughout (build/pcrec-fc719ca4).
No timing in this lane (the manager's window rule); every pcrec call here
is compile-only, run at `nice -n 19`, single process, no `-j`.

## A1 / Q1 — the non-periodic 1 MiB email subject

**Already satisfied, no build needed.** `bench/email/manifest_throughput.tsv`
(email-specimen@0.2, [B17]) has TWO non-periodic 1 MiB throughput subjects:

| id | bytes | sha256 | periodic | match on `orig` |
|---|---|---|---|---|
| `t-d-prose-sparse-addrs` | 1,048,576 | `d55c0e8f...9d94242` | `no` | **496 matches** (expectations.tsv: `nmatches=496`, span e.g. `[2046,2067)`) |
| `t-e-prose-no-at` | 1,048,576 | `ee92cda7...bcafe34` | `no` | 0 matches (no `@` anywhere — the prefilter-rejection control) |

`t-d-prose-sparse-addrs` **is address-bearing** (496 valid dot-atom
addresses, seed 20260828, generator `bench/email/gen_throughput_subjects.py`
`build_prose`/`GEN_SEED`). It answers I-125 A1 (1)-(3) directly:

1. File/generator: `bench/email/gen_throughput_subjects.py`, function
   `build_prose`, `GEN_SEED = 20260828`, sha256 above, 1,048,576 B.
2. Match structure: 496 matches on `orig` (from `expectations.tsv`; same
   count on `factored`, checked — both patterns are one language,
   NOTES.md's own rule).
3. Since an address-bearing non-periodic subject already exists, no new
   one is proposed.

(1.) with no address-bearing subject was the fallback A1 asked for if
none existed; it is moot here.

## A2 / Q7 — counted-repeat-of-literal/singleton census

Script + archive: `docs/dev/measurements/probe_b121_counted_repeats.py`,
`2026-10-01-b121-counted-repeats-census.txt` (real structural parser,
`pcre_mini_parser.py`, not the flat text regex I-125's own text quotes).

**ONE hit in the whole corpus (339 patterns, all 7 sub-benches):**
`bench/utf8`'s `qnt-counted-3b`, `(?:日本){2,}` — a MULTI-LITERAL repeat
(2 CJK characters = 6 UTF-8 bytes, each a separate literal atom).

**`bench/bounded`'s `nest2-*`/`nest3-*` family — pcrec's own named
"candidate instrument" — does NOT match either shape**, confirmed
structurally: every nest pattern is `(?:CLASS{p,q}){m,n}`
(e.g. `(?:\d{1,4}){1,4}`), a counted repeat of a bounded CLASS carrying
its own inner counted repeat — a different mechanism shape from
`(?:ab){m,n}` (one literal STRING, one counted repeat). This is itself
an answer worth sending back: **ask pcrec whether [OPT-5]'s period-k
trigger is meant to fire on the nest family's own shape, or specifically
on a literal-string repeat** (see outbox draft).

(2) the timed comparison (`pcrec-auto` vs `--engine=vm` vs `pcre2-jit` vs
the fastest algorithmic engine, ns/B) is OWED — see the A5 window plan,
"A2(2)" row.

(3) loglines `-fno-scan-edge` vs default (I-32 (iv)) — **OWED**, not
measured in this lane (needs a timing window on `bench/loglines` ×
`{pcrec-auto, pcrec-auto-noedge}`; see the window plan).

## A3 / Q6 — non-top-level `^` census

Script + archive: `docs/dev/measurements/pcre_mini_parser.py` (shared),
`probe_b121_parser_selftest.py` + `probe_b121_nontop_caret.py`,
`2026-10-01-b121-nontop-caret-census.txt`. The parser is validated clean
over all 339 patterns first (0 parse failures, 0 carets hidden inside an
unparsed construct, 0 unexplained cross-check mismatches against an
independent dumb scan).

**EXACTLY ONE pattern in the whole corpus has a non-top-level `^`:**
`capability@0.1`'s `wild-waf-crs-942360-concat-sqli` — the same single
witness A3's own text already names. Its `^` sits in the LAST branch of
a top-level alternation whose other branches are unanchored.

Ratio (already known, from A3's own text, not re-derived here):
`pcrec-auto` vs `re2-longest` — throughput 5.41×, search 1.53×.

**No second losing cell exists outside the WAF family on this corpus as
it stands today.** Per A3's own decision rule, this row stays a
single-witness candidate; nothing escalates it.

## A4 / Q8 — class-tail/member census, and altwide@0.3

Census script + archive: `probe_b121_altwide_class_branches.py`,
`2026-10-01-b121-altwide-class-branches-census.txt`. Five hits (three
distinct real-world patterns: `wild-logparse-syslogbase-expanded`,
`wild-secrets-aws-access-key-id` ×2 (capability + litrun, identical
text), `wild-datetime-datefinder-alternation` ×2 Alt nodes). **None is
the clean, isolated shape pcrec's ask describes** (`ab[cd]|abx`) — class
branches are always a minority among many differently-shaped branches.

**Built the fallback: `altwide@0.3`.** Six new patterns, `clsa-{64,256,
1024}` (trailing `[a-z]`) and `clsd-{64,256,1024}` (trailing `[0-9]`),
each `w`'s own first 64/256/1024 `main` words — see
`bench/altwide/NOTES.md` "What 0.3 added" and P19-P22, and
`bench/altwide/CLAUDE.md`. Zero new subjects (documented cost: `clsd-*`
reads `nomatch` everywhere, `clsa-*` only 4 incidental `search_short`
hits — P19). A COMPILE-ONLY census against the pinned pcrec
(`2026-10-01-b121-altwide-clstail-compile.txt`) confirms the mechanism
directly: **`RX_VM_ALT_ISLANDS "0"` on every forced-VM member** — the
[ENG-ISL] STEP 2 island is DECLINED, exactly as pcrec's own ask
predicted (P20). `clsa-1024`/`clsd-1024` refuse on BOTH engine routes
(a knife-edge rung, within 2.2% of both emitted-size caps — P22).
`gen_oracle_limits.py` gained two skeleton rows: both refuse at 2048
branches, half `w`'s own 4096-branch ceiling.

All generic gates green for this set (`gen_patterns`/`gen_subjects`/
`gen_throughput_subjects`/`gen_pattern_facts`/`gen_oracle_limits`/
`gen_expectations --check`; `check_manifests`/`check_rxt_export` from
`tools/selfcheck.py`). Every 0.1/0.2 `.rx`/manifest/expectation byte
confirmed unmodified (pure appends, `git diff --stat`).

The TIMED comparison (`clsa-256`/`clsd-256` vs the plain `w-256` and the
`-fno-alt-island` denied arm, and the fastest algorithmic engine) is
OWED — see the window plan, "A4 ratios" row.

## Q2 / Q3 — `pcrec-vm-nocaps`(-in) and forced-`pcrec-dfa`(-nocaps)

**Built.** Four new pinned testees in `testees/pcrec/configs.toml`:
`pcrec-vm-nocaps`, `pcrec-vm-nocaps-in`, `pcrec-dfa`, `pcrec-dfa-nocaps`.
Witness census: `docs/dev/measurements/probe_b121_dfa_nocaps_census.py` +
`_identity.py` + `probe_b121_reverse_population.py`, archived in
`2026-10-01-b121-dfa-nocaps-census.txt`.

- `pcrec-vm-nocaps`'s compiling population is cell-for-cell IDENTICAL to
  `pcrec-auto`'s on both `bench/capability@0.1` (124/128) and
  `bench/syntax@0.1` (83/95).
- `pcrec-dfa` (captures on, forced DFA) refuses every capturing-group
  pattern outright, by name ("this pattern requires captures ... pass
  --no-captures ... or omit --engine=dfa") — a diagnostic request,
  REFUSED rather than silently downgraded, unlike `auto`.
  `pcrec-dfa-nocaps`'s broader population (93/128, 64/95) additionally
  compiles every capturing-group pattern that carries no backref/
  lookaround/`\K`/true-recursion (all four VM-only regardless of
  captures, witness-confirmed on all three real recursion patterns and
  on an isolated `\K`).
- **Q3's own "reverse population" (auto picks VM, a forced DFA would
  have won) is MEASURED EMPTY** on both corpora, both forms: `auto`
  already prefers the DFA whenever it can represent the pattern under
  `--no-captures`. Confirmed structurally too — wherever `pcrec-nocaps`
  and forced `pcrec-dfa-nocaps` both compile, they are PROGRAM-IDENTICAL
  (`tools/program_identity.py` v2: 93/93 + 64/64, 0 changed). An empty
  population on two corpora is not proof it stays empty everywhere
  (altwide, or a future pcrec heuristic change, could populate it), so
  the testee is kept.
- Capability roster rows added and witness-verified PER TOKEN (not
  inferred from the base rows' own token sets, which would have been
  wrong here): `pcrec-dfa` excludes `captures`/`named-groups`/
  `recursion`/`k-reset`/`backrefs`/`lookaround`/`lookbehind-variable`;
  `pcrec-dfa-nocaps` keeps `named-groups` (a plain capturing group
  compiles fine with captures off — witnessed on the real corpus
  pattern `codegrammar-xflag`) but still excludes `recursion`/`k-reset`
  (VM-only by construction, witnessed on all three real recursion
  patterns refusing identically caps-on/caps-off).
- `check_capability_roster_coverage`, `gen_patterns.py --check`,
  `check_mechanism_stamps`, `check_deny_flag_controls` all green.
  All four testees smoke-tested end to end via `pcrecbench quick`
  (scratch tier, real compile+run).
- **Gap found, not closed in this lane**: `bench/utf8`'s own `-utf8`
  siblings do NOT exist for these two new pairs (`pcrec-vm-nocaps-utf8`,
  `pcrec-dfa-utf8`, `pcrec-dfa-nocaps-utf8`) — only the byte-mode
  versions were added, since I-125 Q2/Q3 named `syntax@0.1` and the
  existing `bench/capability` caps pair, not `bench/utf8`. If A5's utf8
  arms want a forced-DFA/vm-nocaps reading, those three testees are
  OWED first.

## Q4 — `lka-pos`/`lka-neg` throughput match density

From `bench/syntax/expectations.tsv` (regime `throughput`) and
`manifest_throughput.tsv` (subject bytes). Both patterns' match width is
constant at 4 bytes (`item(?= done)` / `item(?! done)` — the lookahead is
zero-width, only `item` is consumed; `end - start = 4` on every row,
confirmed on all six rows), so density = `nmatches × 4 / subject_bytes`:

| subject | bytes | `lka-pos` nmatches | `lka-pos` density | `lka-neg` nmatches | `lka-neg` density |
|---|---|---|---|---|---|
| `t-64k` | 65,536 | 3 | 0.0183% | 176 | 1.074% |
| `t-256k` | 262,144 | 6 | 0.0092% | 675 | 1.030% |
| `t-1m` | 1,048,576 | 27 | 0.0103% | 2,706 | 1.032% |

**`lka-neg`'s match density is ~58-112× `lka-pos`'s**, roughly flat
itself (1.03-1.07%) across all three sizes while `lka-pos`'s is both two
orders of magnitude smaller AND itself non-monotone (0.018% → 0.009% →
0.010%) — consistent with the generated prose's own per-draw variance at
a very low hit count (3, 6, 27 matches total) rather than a real
size-dependent trend. This directly supports SEL-COST's own framing:
`lka-neg` is a match-DENSE cell (every ~100 bytes) where `lka-pos` is
match-SPARSE (every several KB to tens of KB) despite "identical
compile-time stamps" — exactly the kind of execution-side asymmetry
that would make one win and the other lose on large-subject-throughput
even with the same compiled shape.

## Q5 — do the four `other`-bucket cells sit above or inside the bimodality floor?

**Answered in substance; the exact citation ("`esc-octal-0` 1.047×")
could not be located verbatim in any committed syntax report or ledger**
(searched every `reports/*syntax*` and `docs/dev/ledgers/*` file; the
closest match found is `esc-octal-0`'s `short-subject-search` ratio of
×0.959 against the floor on `pcrec_751b9c6d_vm-in-caps-simdna`,
`reports/2026-09-27-syntax-0.1-budu-ryzen1600-fullroster-751b9c6d.interpretation.md:294`
— not 1.047× and not obviously "the four other-bucket cells"). **Asking
pcrecdev1 to name the report/date this reading is from** (outbox draft).

The substance, from O-69/[B112] (`docs/dev/outbox_to_pcrec.md` O-69,
`docs/dev/measurements/2026-09-28-b112-bimodality-diagnostic.txt`): a
SINGLE driver launch has ~13-20% odds of running on a cold core at
~0.40× clock (a ~2.5× slowdown from CPU-frequency-governor ramp, not
layout) — which is why "effects under about 1%" are read as noise for a
SINGLE-launch arm (`docs/dev/outbox_to_pcrec.md` O-74's FINDINGS-tiers
reading states this explicitly: "each arm is one driver launch, so the
per-launch governor bimodality from O-69 applies. Effects under about 1%
are not findings"). But a STANDARD PINNED record is a MEDIAN over 5
TRIALS, gated by the v1.4 trial-agreement rule (`k=1.5`, `d_min=2`,
`share_c=3`) specifically built to catch exactly this kind of
contamination and demote a contaminated cell to `inconclusive-spread`
rather than let it report `measured`. **A ratio in the 1.03-1.23× range
on a cell that reads `measured` therefore sits ABOVE (outside) what the
single-launch bimodality floor can produce as a pure artifact** — the
v1.4 gate already certifies the cell's own trials agreed with each
other, which a genuine 2.5× single-launch contamination event would not
have passed. This does not rule out a SMALLER noise contribution from
e.g. two of five trials catching a brief partial ramp-down without
tripping the group threshold; the honest answer is "above the floor the
single-launch diagnostic measured, but the record-level floor for a
5-trial median specifically has not been separately characterised" —
an ask, not a number, for pcrec (outbox draft).

## Q6 — see A3 above.

## Q7 — see A2 above.

## Q8 — see A4 above.

## Q9 — DD-13 residuals

**No bench consumer is waiting on any of the three** (composed delivery
W1.3.1, `(?&site.group)`, grouplist semantics W1.4). A repo-wide search
for `W1.3.1`/`W1.4`/`(?&site.group)`/`grouplist` finds zero hits outside
this inbox question itself and `docs/design/subbench_directory_model.md:241`,
which states plainly: "`[DD-13b.W1]` is `STATE:started` on pcrec's plan
(W1.3 and W1.4 remain); W2 and W3 are unchartered" — acknowledged pcrec-
side future work, nothing here blocked on it.

**The `floor` prefix collision is still CROSS-SET only.** Confirmed in
two places: pcrec's own `w13_report.md` §7 item 3 (via the pin tree,
`build/pcrec-fc719ca4/docs/dev/lanes/w13_report.md:234-238`): "the
mapping collides exactly once, on `floor`, and that collision is
CROSS-SET — each of the four sets has its own `floor.rx` — so a per-set
export never collides"; and `tools/export_rxt.py` (I-43's rules, §
implementing exactly this: exports per sub-bench, never merged). Still
true at 185+ ids across now 8 sub-benches (re-verified structurally by
this lane's own `check_rxt_export` run, which exercises the SAME
collision-refusal control: `rxt-export-collision-control: pattern ids
'a-b' and 'a.b' both derive the target prefix 'a_b'` — passed).

## Q10 — `date-nested-plus` lookup / the 17 capture-forced hybrids' subject size

**Not missing data, not a lookup key mismatch — a declared absence.**
`bench/capability/subbench.toml` declares `regimes = ["search_short",
"throughput"]` for capability@0.1: **there is no `match` regime at all**
for this set. `search_short` rows for `date-nested-plus` DO exist
(`expectations.tsv`, all `nomatch`); any `match`-regime lookup for this
pattern — or any of the 17 capture-forced hybrids — correctly returns no
row, because the harness never generated one. "M-B" (pcrecdev1's own
reduction-step label) assumed a per-pattern match subject that this set
does not have.

**Subject sizes: nothing in the 1 KiB-64 KiB match-regime band exists.**
`manifest.tsv`'s longest subject is 93 B (search_short, cap 512 B);
`manifest_throughput.tsv` has only `t-64k`/`t-256k`/`t-1m` (65,536 /
262,144 / 1,048,576 B) and those are `throughput` (find-all) subjects,
not match ones. `t-64k` sits at the TOP of the 1 KiB-64 KiB band I-125
names but is the wrong regime. **None exists; adding one is a real ask**
if pcrec wants a realistic-size whole-string match reading on the 17
hybrids (outbox draft; it is a `capability@0.1` set-version bump, not
this lane's to do unasked).

## Q11 — does `lka-pos` stay a losing cell after [OPT-HYB-RESEED] (abi 49)?

**OWED** — needs a timed `capability@0.1` cell at fc719ca4 (abi 50,
already past 49) on `lka-pos`, large-subject-throughput, `pcrec-auto`
vs the comparison the original finding used. Folds into the A5 standing
re-measure's own `capability@0.1` pass (same cell population, same
window) — see the plan below; not separately scheduled.

## Q12 — the re-measure cadence / window

Pin: **fc719ca4**, confirmed unchanged by pcrec's own inbox I-126: "Keep
the pin. [B117] stays at fc719ca4 ... Do NOT re-pin for [B117]. A re-pin
ask for the next windows will come after pcrec's Friday 2026-10-02
checkpoint." **No separate "non-colliding day slot" exists to find**:
Frank's standing ruling (inbox I-35) is that this project's blocking
measurement windows run OVERNIGHT, pcrec's own lanes/tests/batteries run
during the day — the two are already partitioned by time of day, not by
a negotiated slot. `plan.md`'s own queue (`[B121]` "AFTER [B117]") is
the only other ordering fact: [B117]'s own window (the olevel read)
completed today, so A5 is next in the night-window queue, at the
unchanged fc719ca4 pin, whenever the manager opens the next window.

---

## A5 — the standing re-measure window plan

**Existing fc719ca4 records** (checked against `store/index.tsv`):
ONLY `capability@0.1` has any — `pcrec-auto` (caps) and `pcrec-vm` (caps)
plus their four `-o{0,1,3,s}` siblings, from [B117]'s own olevel window
(9 `measured` + 1 `inconclusive-spread` retry). **`utf8@0.1`,
`syntax@0.1`, `loglines`, `bounded`, `altwide`, `email` have ZERO fc719ca4
records** — the whole standing re-measure is effectively a fresh window
at this pin, except `capability@0.1`'s `auto`/`vm` caps pair.

### Per-(set, testee) cells, duration estimates, and OWED/EXISTS

Per-cell wall time cited from each set's own `NOTES.md` "Cell-time
estimate" section (`bench/altwide`, `bench/bounded`, `bench/loglines`,
`bench/syntax`, `bench/capability`, `bench/utf8`); `bench/email` has no
such section (not separately estimated below — historically fast, under
~10 min by the same per-subject model, given ~90 short subjects against
loglines' 112).

| set | testee | status at fc719ca4 | est. wall time |
|---|---|---|---|
| capability@0.1 | `pcrec-auto` | **EXISTS** (measured) | ~23-30 min |
| capability@0.1 | `pcrec-nocaps` | OWED | ~23-30 min |
| capability@0.1 | `pcrec-vm` | **EXISTS** (measured) | ~25-35 min (compile-heavy) |
| capability@0.1 | `pcrec-vm-nocaps` | OWED (new testee, [B121]) | ~25-35 min |
| capability@0.1 | `pcrec-dfa-nocaps` | OWED (new testee, [B121]) | ~23-30 min |
| capability@0.1 | `pcrec-dfa` | OWED (new testee, [B121]; refuses more, likely FASTER) | ~15-25 min |
| utf8@0.1 | `pcrec-auto-utf8` | OWED | ~41-53 min |
| utf8@0.1 | `pcrec-nocaps-utf8` | OWED | ~41-53 min |
| utf8@0.1 | `pcrec-vm-utf8` | OWED | ~45-55 min (compile-heavy) |
| utf8@0.1 | forced-vm-nocaps / forced-dfa | **GAP**: no `-utf8` sibling exists for `pcrec-vm-nocaps`/`pcrec-dfa`/`pcrec-dfa-nocaps` (Q2/Q3's testees are byte-mode only) — OWED as a BUILD before this arm can run |
| syntax@0.1 | `pcrec-auto` | OWED | ~52 min |
| syntax@0.1 | `pcrec-nocaps` | OWED | ~52 min |
| syntax@0.1 | `pcrec-vm` | OWED | ~55-60 min (compile-heavy) |
| syntax@0.1 | `pcrec-vm-nocaps` | OWED (new) | ~55-60 min |
| syntax@0.1 | `pcrec-dfa-nocaps` | OWED (new) | ~50-55 min |
| syntax@0.1 | `pcrec-dfa` | OWED (new; more refusals) | ~40-50 min |
| loglines | `pcrec-auto` + comparison (pcre2-interp/jit) | OWED | ~8-9 min/cell × 3 |
| bounded@0.3 | `pcrec-auto` + comparison | OWED | ~12-18 min/cell × 3 |
| altwide@0.3 | `pcrec-auto` + comparison | OWED (first-ever window on 0.3) | ~8 min + ~25-35 min compile + comparison engines |
| email@0.2 | `pcrec-auto` + comparison | OWED | ~5-10 min/cell × 3 (not separately estimated in NOTES.md) |

**Rough total**: capability ~2-2.5 h (6 cells), utf8 ~2.5-3 h (3 cells,
the forced-dfa/vm-nocaps arm blocked on a build), syntax ~5 h (6 cells,
matching the committed 2026-09-03 full-roster window's own "~5 h for six
pinned testees" estimate), loglines/bounded/altwide/email ~1.5-2 h
combined (3 cells each, smaller sets) — **call it two nights**
(syntax alone is a full night by itself per its own NOTES.md estimate;
everything else fits a second night with margin).

### Suggested chunking for `scripts/run_window.sh` / `run_suite.sh`

1. **Night 1**: `syntax@0.1` alone, all six testees (`auto`, `nocaps`,
   `vm`, `vm-nocaps`, `dfa-nocaps`, `dfa`) as one `TESTEES_syntax` list —
   matches the precedent (`CELL_CAP` default 5,400 s / 90 min is
   comfortable per cell per NOTES.md's own ~52 min estimate; no raise
   needed).
2. **Night 2 morning slot**: `capability@0.1`'s four OWED cells
   (`nocaps`, `vm-nocaps`, `dfa-nocaps`, `dfa`) — the two EXISTING cells
   (`auto`, `vm`) are not re-run; `TESTEES_capability` set to just the
   four.
3. **Night 2 remainder**: `utf8@0.1` × `{auto-utf8, nocaps-utf8,
   vm-utf8}` (the forced-dfa/vm-nocaps `-utf8` arm needs its own
   testees built first — flag this as a prerequisite, not silently
   drop it), then `loglines` / `bounded@0.3` / `altwide@0.3` / `email@0.2`
   each as its own short `run_suite.sh` pass with `pcrec-auto` plus
   whatever comparison engines each set's existing window convention
   already uses (pcre2-interp/jit at minimum; re2/onig/vectorscan where
   the set's own roster already includes them).
4. `altwide@0.3`'s own first window should ALSO include
   `pcrec-auto-noisland`/`pcrec-vm-noclsfold`-style comparisons if the
   manager wants P20's VM-island decline read as a timed BEFORE/AFTER
   against the plain `w-256`/`-fno-alt-island` denied arm immediately —
   otherwise that is a second, smaller follow-up window, not part of
   this night's cost estimate above.

### Cells A2/A3/A4 need their own RATIO reading from (beyond the standing re-measure)

- **A2(2)**: `bench/utf8`'s `qnt-counted-3b`, `search_short` +
  `throughput`, `pcrec-auto` vs `pcrec --engine=vm` vs `pcre2-jit` vs
  the fastest algorithmic engine on this set (likely `re2-utf8` or
  `onig-utf8` — not determined here). Covered by the utf8@0.1 window
  above if all relevant testees are included in `TESTEES_utf8`.
- **A3**: `wild-waf-crs-942360-concat-sqli` vs `re2-longest` — ALREADY
  KNOWN (thr 5.41×, srch 1.53×, cited in A3's own inbox text); no new
  cell needed unless pcrec wants it RE-measured at fc719ca4 specifically
  (it is part of `capability@0.1`'s own standing re-measure population
  either way).
- **A4**: `clsa-256`/`clsd-256` (the compiling anchor width) vs
  `pcrec --engine=vm` vs the `-fno-alt-island` denied arm (NOT YET A
  PINNED TESTEE on altwide@0.3 — `pcrec-auto-noisland`/
  `pcrec-vm-noclsfold`-style denial already exists repo-wide but has
  never been pointed at `altwide@0.3`'s new patterns) vs the fastest
  algorithmic engine. This is `altwide@0.3`'s own first window, item 4
  above.
- **Q11**: `capability@0.1`'s `lka-pos`, large-subject-throughput,
  `pcrec-auto` — covered by `capability@0.1`'s own re-measure.

## Charter-vs-committed checklist

| item | status |
|---|---|
| A1/Q1 (non-periodic address-bearing subject) | **COMPLETE** — answered from existing data, nothing to build |
| A2/Q7 (counted-repeat census) | **COMPLETE** (census + archive); timed ratio **OWED** (window plan) |
| A3/Q6 (non-top-level `^` census) | **COMPLETE** (census + archive, ratio already known) |
| A4/Q8 (class-tail census + altwide@0.3) | **COMPLETE** (census + build + compile-only confirmation); timed ratio **OWED** (window plan) |
| Q2/Q3 (pcrec-vm-nocaps/pcrec-dfa testees) | **COMPLETE** (built, roster-verified, smoke-tested); utf8 `-utf8` siblings **OWED** as a build prerequisite |
| Q4 (lka-pos/lka-neg density) | **COMPLETE** |
| Q5 (bimodality floor) | **PARTIAL** — substance answered; exact source citation not located, asked back |
| Q9 (DD-13 residuals) | **COMPLETE** |
| Q10 (date-nested-plus lookup / hybrid subject size) | **COMPLETE** (explained; a new subject is an ASK, not built here) |
| Q11 (lka-pos post-[OPT-HYB-RESEED]) | **OWED** — folds into A5's capability@0.1 window |
| Q12 (re-measure cadence/window) | **COMPLETE** |
| A5 (window plan) | **COMPLETE** (this document's own section) |

## Commits on this branch

1. `[B121] Q2/Q3 prep: compile-only census for pcrec-vm-nocaps/pcrec-dfa(-nocaps)`
2. `[B121] Q2/Q3: add pcrec-vm-nocaps(-in) and pcrec-dfa(-nocaps) testees`
3. `[B121] A3/Q6: non-top-level ^ census via a real structural parser`
4. `[B121] A2/Q7: counted-repeat-of-literal/singleton census`
5. `[B121] A4/Q8: >=8-branch class-tail/member census (prep for altwide@0.3)`
6. `[B121] A4/Q8: build altwide@0.3, the class-tail arm`

All `--check` modes and `tools/selfcheck.py` checks this lane touched are
green (see each commit's own message for the exact invocations and
results). No store write, no timing, no `make check` full run (the
generic-gate subset relevant to this lane's changes — `check_manifests`,
`check_rxt_export`, `check_capability_roster_coverage`,
`check_mechanism_stamps`, `check_deny_flag_controls` — was run directly
and is green; a full `make check` was not run in this lane to avoid a
~500 s cost on a box other lanes are sharing).

Branch tip: see `git log lane/b121asks` (six commits above this report's
own, which is the seventh).
