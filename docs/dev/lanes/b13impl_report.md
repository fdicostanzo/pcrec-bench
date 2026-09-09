# Lane `b13impl` — the interpreter, part 1 ([B13.3])

Branch `lane/b13impl`, from master at `2827029`. Delivered 2026-09-09.
Charter: `docs/design/interpreter_v1.md` v1.2 part (1), the deterministic
fact-finder `pcrecbench interpret`, its versioned rule catalogue, the
facts TSV and the rendered sidecar, the predictions input, the opinion
firewall as code, `make check-interpret`, and §10's acceptance test RUN.

**Headline: §10's acceptance test passes 25 of 25 items**, and Report A
reproduces §9.2's hand-written specimen exactly — twelve rules fire with
the specimen's own counts, nineteen do not — while Reports B and C
reproduce every aggregation number in §5.2's measured table. Nothing in
the note was weakened or rewritten to fit the build.

---

## 1. Charter-vs-committed checklist

| # | the brief asked for | committed | state |
|---|---|---|---|
| 1 | `catalogue/rules.toml`: every §4 rule, load-time checks | `catalogue/rules.toml` — 31 rules in 7 classes, `catalogue_version = "1.0"`, `[[pin_order]]` with the eleven pcrec pins; loaded by `load_catalogue()` with every check §3.2.1/§3.2.2/§8(1) requires | DONE |
| 2 | `pcrecbench/interpret.py` + the `interpret` subcommand | `pcrecbench/interpret.py` (~1,900 lines), dispatched before argparse in `__main__.py` the way `report` is | DONE |
| 3 | the predictions reader + the P1-P13 transcription + the load-error fixture | `docs/dev/predictions/syntax-0.1-first.tsv` (35 clause rows, 13 parents), `catalogue/fixtures/predictions-inexpressible.tsv` (P9's span, P12's answer-equality), the `stated_utc` check against the earliest INDEX timestamp incl. superseded rows | DONE |
| 4 | `catalogue/fixtures/gen.py --check` + the fixture dirs + `catalogue/golden/` | 58 fixtures (181 files), `catalogue/golden/index@2026-09-09.tsv` (frozen), four `*.facts.tsv` goldens incl. Report C with predictions; Report D is `CLEAN__all-measured` | DONE |
| 5 | `make check-interpret`, fast, wired into `make check` | 129 checks in six sections, **28.4 s** wall, never loads the record store | DONE |
| 6 | §10's acceptance test RUN, every item with its actual firing | `catalogue/acceptance_10.py`, **25 of 25 PASS**; the table is §3 below | DONE |
| 7 | docs: three CLAUDE.mds, the Makefile help line, the note's STATUS block, this report | `catalogue/CLAUDE.md`, `docs/dev/predictions/CLAUDE.md`, `pcrecbench/CLAUDE.md`, root `CLAUDE.md`, `docs/dev/CLAUDE.md`, `docs/design/CLAUDE.md`, the `## check-interpret:` help line, the note's STATUS → IMPLEMENTED, this file, and the `[B13.3]` plan row | DONE |

Nothing is OWED. No background run is outstanding.

**Validation as run, on this branch, in this worktree:**

```
make check-interpret   129 passed, 0 FAILED   (12 / 8 / 1 / 103 / 4 / 1 by section)   28.4 s
make check-schema      4 example(s) accepted, 72 sabotage(s) rejected, 0 WRONG        unchanged
python3 catalogue/acceptance_10.py   §10 acceptance: 25 of 25 items PASS
```

`pcrecbench/tests/test_report.py` was NOT run (it loads the store; the
manager runs it). `make check-harness` was not run: nothing in this lane
touches the harness, the adapters or a bench set, and `check-harness`
costs ~20 minutes of box time.

---

## 2. What was built, in one paragraph each

**The catalogue.** 31 rules, seven classes, each carrying its `grain`,
`aggregate` key, exact `inputs`, prose `predicate`, `threshold` and
`threshold_src`, `slots`, `arith`, `template`, `no_fire`, `links` and a
worked `example` citing a real committed report row. No rule introduces a
constant: every threshold is a token or number the reporter already
printed, a comparison of two measured quantities from one report, or a
boundary named as definitional. R-ARM-1 is the one rule that computes,
and it copies `_cross_pin_verdict`'s own `2 × max(stddev)` rather than
choosing a bound.

**The module.** `ReportTsv` parses the header with §2.1's NORMATIVE
known-key split, whose key list is DERIVED from `report.py`'s own header
block at import (`header_keys_from_source`) rather than retyped — so a
reporter bump that adds a key fails section 1 instead of silently
re-joining the new key into the previous key's value. `RuleView` hands
each rule function `rows()` / `header()` / `index_rows()` that raise
`UndeclaredColumn` on any column outside that rule's declared `inputs`.
The 31 rule functions are named exactly `r_<id>`; the correspondence is
checked both ways.

**The output.** `--format tsv` (default) emits one row per slot per
firing with `firing_seq` and `prediction_id`, and one `fired=0` row per
non-firing rule carrying its reason token — a rule is never silently
absent. `--format md` / `--render` emits the sidecar: the stamp, one
heading per firing rule, §5.2's counted collapse, the appended `See:`
links, and the did-not-fire table. Exit 0 on a successful read, 2 on a
malformed input, an unknown column, an unresolvable link, a pin absent
from `[[pin_order]]`, or a catalogue/code mismatch.

**The firewall.** The renderer is `template.format(**slots)` with a
strict missing/extra slot check, plus validated `links`. Rendering reads
numbers back out of the rendered slot STRINGS, so the whole sidecar is a
function of the facts TSV — which is what lets section 5 re-render the
document from the facts alone and require byte equality, a stronger form
of §8(5)'s no-prose check than line-by-line matching.

---

## 3. §10 THE ACCEPTANCE TEST — run, 25 of 25

Reproduce with `python3 catalogue/acceptance_10.py`.

| item | verdict | the actual firing |
|---|---|---|
| **A.1** three inconclusive records by id, as R-STATUS-2 | PASS | R-STATUS-2 fires **3×**, all `inconclusive-load`: `libpcre2_10.46_interp-caps-simdna` @ 20260825T173402Z; `pcrec_692c2e8_auto-caps-simdna` @ T175131Z; `pcrec_692c2e8_auto-nocaps-simdna` @ T175534Z |
| **A.2** the collapse: R-DELTA-2 ×6, R-DELTA-3 ×4, co-firing | PASS | R-DELTA-2 **6** firings, R-DELTA-3 **4**, and **4 cells carry both clauses** of the compound verdict |
| **A.3** all thirteen excluded cells by code and smallest subject | PASS | R-STATUS-3 **13** firings; all three codes present (`-2:PCREC_ERR_STEPS`, `-3:PCREC_ERR_FRAMES`, `-4:PCREC_ERR_WORK`); the `libpcre2_10.46_jit-caps-simdna` throughput row renders at pass-rate 0.6667 **with no fabricated cause** |
| **A.3b** the STEPS-vs-WORK pairing as R-STATUS-12, three testees | PASS | **3** firings, on `pcrec_692c2e8_vm-caps-simdna`, `pcrec_692c2e8_vm-in-caps-simdna`, `pcrec_8da6120_vm-caps-simdna`; subject `t-c-long-atom-run`, STEPS on `factored` vs WORK on `orig` |
| **A.4** the vm-in result as R-ARM-1, by rule and by number | PASS | R-ARM-1 **14** firings → 8 bullets. `orig`/short-search: vm-in **12,546.2** vs vm **28,996.9** ns = **×2.31**, beyond **862.2** ns. `orig`/compliance: vm-in **62,732.3** vs vm **80,227.6** = **×1.28**, beyond **318.8** ns |
| **A.5** the unpredicted Δ as R-DELTA-1, THREE firings | PASS | `faster ×1.19` (factored/short-search), `faster ×1.26` (orig/compliance), `faster ×1.00` (orig/compliance, auto-nocaps) — the third included, which is where v1's own specimen disagreed with the data |
| **A.6** the regime artifact as R-BUCKET-FORM, per GROUP | PASS | 2 firings: `factored`/match-compliance 3 separate + 2 same; `orig`/match-compliance **7 separate + 2 same** |
| **A.7** the mixed schema population as R-STATUS-6 | PASS | `schema_versions 1.1,1.2`; **9 of 9** records read `n/a (v<schema>)` |
| **A.8** R-STATUS-9 must NOT fire | PASS | `no-matching-rows` — all nine records read `n/a (v1.x)`, provenance about their age, reported by R-STATUS-6 |
| **B.1** R-RANK-1 on cls-upto-8192 / compliance / whole-subject | PASS | `334fd10e` **1.788241** → `d34c9131` **0.269358**; the R-STATUS-13 guard does not engage (`no-matching-rows`) |
| **B.2** R-DELTA-2 on that same cell | PASS | `pcrec_d34c9131_auto-caps-simdna`: `selection changed (dfa → vm)` on the same (pattern, regime, form, config) cell |
| **B.3** R-BUCKET-SPAN on the vm-in rows | PASS | **129** firings, every one config `vm-in-caps-simdna`, every one `288d505 → d34c9131`, span **2**; `cls-upto-1024` throughput `faster ×1.53` and short-search `faster ×1.25` |
| **B.4** R-BUCKET-VSBEST on every ≥2-slug group | PASS | **129** firings → 1 bullet; the `cls-upto-1024`/short-search inversion is among them (288d505, 334fd10e, d34c9131) |
| **B.5** R-RANK-1 on ≥5 `dig-*` throughput rows (vm-in) | PASS | `dig-exact-8` 1.081314→0.643200, `dig-upto-8` 1.058010→0.619855, `dig-exact-16` 1.590991→0.945559, `dig-upto-16` 1.603386→0.950768, `dig-exact-32` 1.769867→0.926231 (7 R-RANK-1 firings in all) |
| **B.6** R-DELTA-1's 202 firings as 17 aggregated bullets | PASS | **202 firings → 17 bullets**, 1,818 slot rows in the facts TSV — nothing dropped |
| **B.7** R-DELTA-4 must NOT fire with no predictions file | PASS | `input-absent` |
| **C.1** R-STATUS-4: 60 pairs, four aggregated firings | PASS | **60** distinct (pattern, testee) pairs → **4 bullets**, 15 patterns on each of the four pcrec testees; `cnd-group` carries pcrec's own diagnostic verbatim |
| **C.2** R-STATUS-3 on the 23 excluded cells | PASS | **23** firings; `rec-1`/throughput on 5 testees at pass_rate 0.0000 with 15 wrong; `asr-k-uc`/compliance on 4 pcrec arms at 0.9762 with 5 wrong |
| **C.3** R-BUCKET-KB does NOT fire (a STATED KNOWN GAP) | PASS | `no-registered-signatures` — catalogue 1.0 registers none, by design |
| **C.4** R-FLOOR-2 on `anc-caret` / short-search / vm-caps | PASS | **5.868** ns/subject against the floor pattern `floor`'s **19.050** → **×0.308** (103 R-FLOOR-2 firings in the report) |
| **C.5** R-FLOOR-1 on the 190 timer-floor compile rows | PASS | **190** firings → **2 bullets**, 95 rows on each libpcre2 arm |
| **C.6** R-STATUS-9 must NOT fire | PASS | `no-matching-rows` — all six records read `agree (0 of N groups …)` |
| **C.7** R-ARM-1's 635 firings as 12 aggregated bullets | PASS | **635 → 12**, all 635 in the facts TSV |
| **D** the synthetic clean report | PASS | **31 rules named, 0 fired** |
| **MUST-NOT** (A, B, C) | PASS | No template in the catalogue contains `because`, `due to`, `caused by`, `better`, `worse`, `should`, `wave G` or `splice`; every cause a sidecar can carry is a `links` entry to a committed file. No template names a preference, and R-ARM-1 states a ratio and a spread and stops |

**§9.2's specimen, reproduced.** On Report A the tool fires exactly the
twelve rules the note's hand-written specimen fires, with its counts:
R-STATUS-2 3, R-STATUS-3 13, R-STATUS-5 1, R-STATUS-6 1, R-STATUS-12 3,
R-DELTA-1 3, R-DELTA-2 6, R-DELTA-3 4, R-ARM-1 14→8, R-BUCKET-FORM 2,
R-BUCKET-VSBEST 4→1, R-FLOOR-1 2→1. Nineteen do not fire.

**§5.2's aggregation table, reproduced.** Every measured number in it:
R-DELTA-1 202→17, R-ARM-1 14→8 / 432→9 / 635→12, R-FLOOR-1 2→1 / 81→2 /
190→2, R-BUCKET-VSBEST 4→1 / 129→1, R-STATUS-4 60 pairs→4.

---

## 4. Deviations from the note, with reasons

None changes a rule's predicate or threshold, and none weakens §10.

1. **`threshold_src` cites SYMBOLS, not line numbers, in `report.py`.**
   The note's own citations are stale at reporter v16 by roughly +100
   lines, which is exactly the failure a line citation invites. The
   catalogue cites `report.py `_cross_pin_verdict``, "render_tsv's
   header block", etc.; only `reduce.py`'s five agreement strings keep
   line numbers, re-read for this lane and correct (§5 below).
2. **The known-key list is derived from `report.py`'s SOURCE, not by
   running `report --format tsv` over a fixture store** (§8(1)). Running
   the reporter needs a store, and the reporter's whole-store load is the
   memory-heavy motion the lane boilerplate warns about; parsing the
   header block's own f-string literals is hermetic, needs no store, and
   is checked three ways (against the frozen `HEADER_KEYS`, and against
   every acceptance report's own header parsing to the full key set).
3. **`extremal` is declared on every aggregating rule with a numeric
   slot, R-ARM-1 included, and the render reads only the declared name.**
   §5.2's prose says R-ARM-1 keeps the default `median_ns`; its own §9.2
   worked bullets pick the largest RATIO and the smallest RATIO
   (×11.05 extremal, ×4.73 minimum, where the median-ordered minimum
   would have been a different row). The data wins: `extremal = "ratio"`.
   The invariant "a rule that aggregates and carries a numeric slot must
   declare an extremal" is enforced at run time (`check_extremal`).
4. **An aggregated bullet for a rule with NO numeric slot renders the
   first firing's template output plus the remaining firings' KEYS**, not
   a bare key list. A bare list drops the sentence (R-DELTA-2's six
   groups would have rendered without the words "selection changed",
   failing §10 A.2's own requirement that the collapse be surfaced);
   rendering all N sentences would defeat the collapse (R-FLOOR-1 would
   print 95 sentences per bullet on Report C). Count + one sentence +
   the full sorted key list + the facts-TSV pointer satisfies §5.2's
   three required elements and drops nothing.
5. **The minimum is shown only when a group has MORE THAN TWO members**,
   per §5.2's normative sentence. §9.2's hand-rendered R-ARM bullets show
   a minimum for two-member groups as well; the spec sentence wins.
6. **`no_fire` sentences are static and slot-free**, per §7.1. §9.2's
   did-not-fire table shows report-specific numbers in two rows ("all 6
   ranking groups…", "highest compile jitter ratio is 0.645"); a slot-
   free sentence cannot carry them, and §7.1 is the rule.
7. **R-BUCKET-DOMINATED declares `grain = ["set", "subject"]`**, not
   subject-only. Its input is a subject-grain SIDECAR, not the report
   being interpreted, so on a set-grain report the honest token is
   `input-absent` (which is what §9.2 renders and what Q2 ruled) rather
   than `grain`. The rule evaluates properly if a `--subject-grain` TSV
   is ever supplied; no such file exists in the repository today, so that
   path is unexercised by real data and is stated here as such.
8. **R-DELTA-4 is evaluated after the four rules it reads**, then placed
   back in its declaration position. It is a cross-class rule by
   definition (§4.2) and its declaration order sits before R-RANK-1,
   R-ARM-1 and R-FLOOR-2; without the deferral it read an empty firing
   set. Output order is unchanged.
9. **R-RANK-1 reads the group's arms from the `median_ns` rows**, the
   same population R-STATUS-13 reads, so the guard engages on exactly the
   rows that rule reports about. Reading them from the
   `ratio_vs_baseline` rows instead would let the two rules disagree
   about what a group contains.
10. **A prediction whose selector does not name a `section` reads
    `rank`**, and R-PRED-3 then reports WHERE the cell went (excluded /
    not-ranked / did-not-compile / scratch) by looking in those sections;
    a selector that names `section` reads exactly that section and is
    evaluated normally. §6.3 does not say which section a section-less
    selector reads; this is the reading that makes §6.6's own P2
    transcription work (P2.a is an `excluded` cell by construction,
    P2.d lands in `did_not_compile` and must be `not-evaluable`).
11. **`rank_over(<key>)` ranks a row among the population its selector
    describes with the ranked key WILDCARDED**, not among the selected
    rows alone. §6.3 says "orders the selected rows"; read literally,
    P5.a ("the three cheapest cells IN THE SET") would rank three rows
    against each other and pass trivially. Likewise
    `ratio_to_median_over(<key>)` takes the median WITHIN each group and
    `ratio_to(<selector>)` joins the two populations on every key column
    the two selectors agree about, so P4's ratio is per (regime, form,
    testee) rather than one number over the whole report.
12. **The fixture declaration is one authored file
    (`catalogue/fixtures/fixtures.toml`); each fixture's `source.toml` is
    MATERIALISED from it** by `gen.py` and checked by `--check`. §8(4)
    shows per-directory `source.toml`s; 58 hand-authored copies of one
    table would be 58 chances for a declaration to drift from the corpus
    it declares.
13. **"Exactly one declared field differs" is checked as one declared
    MUTATION plus at most one differing COLUMN**, not one differing cell.
    A mutation with `all = true` changes one column across several rows
    (R-FLOOR-1's control changes 16 `jitter` cells) and is still one
    declared field; counting cells would call it sixteen.
14. **Section 5 re-renders the whole sidecar from its facts TSV and
    requires byte equality**, rather than checking each line against some
    `render(rule_id, slots)`. It is the same property, checked more
    strictly, and it is why the renderer parses numbers back out of the
    rendered slot strings.
15. **`docs/dev/pcrec_references.md` is linked without an anchor.**
    §9.2's specimen renders `See: docs/dev/pcrec_references.md (pcrec
    [OS-4])`; the string `OS-4` does not occur in that file, and §7.3
    requires an anchor to resolve, so the link is to the file.
16. **P12 rolls up to `refuted`, not `partial`.** §6.6 predicts
    `partial` because it counts P12's agreement clause; that clause is
    INEXPRESSIBLE and is therefore absent from the committed file, so the
    parent has one clause. Everything else in §6.6's table reproduces:
    the committed P1-P13 file scores 4 confirmed / 4 refuted / 5 partial
    against Report C, with P1, P4 and P6 disagreeing with the ledger's
    human tally exactly as §6.6 says they should.
17. **Section 3 (sidecar freshness) currently checks ZERO files.** No
    `reports/*.interpretation.md` is committed — those are [B13.4]'s
    deliverable, explicitly out of this lane. The section is implemented
    and will bind the moment one lands.

## 5. Citation corrections (the note's line numbers at reporter v16)

The note's `report.py` citations predate reporter v14/v15/v16 and are
low by ~100 lines. Re-read for this lane:

| the note cites | reads at v16 |
|---|---|
| `render_tsv` at 4065 | **4199** |
| the header comment block 4068-4091 | **4202-4228** |
| the 18-column header list 4092-4094 | **4229-4232** |
| the ranking / excluded split 4123-4124 | **4260** |
| `ref_ns` fallback 4133-4136 | **4272** |
| `rank_or_na` 4137 / the six metric rows 4146-4153 | **4288** / **4283-4285** |
| `delta_verdict` set-grain only 4143-4145 | **4280-4282** |
| the lazy-jit compile metric 4177 | **4330** |
| `_cross_pin_verdict` 2234-2248 | **2334-2348** |
| `_set_cell_failure_reason` 2251-2264 | **2351-2364** |
| `_jitter_flag` 2150-2165 | **2250-2265** |
| `_TIMER_FLOOR_NS` 1927 | **2027** |
| `_DOMINANCE_SHARE` 2326 | **2426** |
| `_floor_mean_for` 2582-2595 | **2682-2695** |
| `_is_reference` 3153-3159 | **3265-3270** |
| `_ranking_groups` 3161-3176 | **3273-3300** |
| `_n_and_pass_rate` 3196-3200 | **3308-3311** |
| `_agreement_display` 2788-2792 | **2899** |
| `_gave_up_cell_summary` 1216-1222 | **1306** (and P-2's `_gave_up_cell_detail` at **1280**) |
| `REPORTER_VERSION` 896 | **978** |
| `reduce.py:372-376` (the `agree (…)` string) | **correct as cited** — v1.2's own fix verified |

The catalogue therefore cites symbols. `check-interpret` section 1 reads
the two things that MUST not drift (the header key list and the 18-column
list) out of the source itself.

## 6. Findings worth the manager's eye

- **P1 is REFUTED at d34c9131, and the tool prints the measured set.**
  The refusal set on every pcrec testee is the fifteen `NOTES.md` names
  **minus `esc-hex-braced`, plus `mod-x`**. Neither half is a surprise
  on its own — `NOTES.md` predicted the first ("at the abi-23 re-seed it
  moves to the base grammar and this one becomes an R1 candidate"), and
  `mod-x`'s refusal is KB-15's known instrument defect (the `(?x)`
  comment swallowing the whole-subject wrapper's own `)\z`; pcrec's
  diagnostic reads `missing closing ) for group (pattern offset 0)` on
  all four arms). What is worth having is that the prediction AS STATED
  is now scored refuted by rule, with both differences named, rather
  than left to a reader who has to remember two separate facts.
- **R-RANK-1 fires SEVEN times on Report B, not five.** §10 B.5 says "at
  least five"; the two beyond the `dig-*` set are B.1's `cls-upto-8192`
  cell and `dig-upto-32` on `vm-caps-simdna` (0.998949 → 1.007854), a
  genuine crossing the note's census did not name.
- **R-BUCKET-SPAN fires 129 times on Report B, all on one config.** The
  note's §10 B.3 names the fact; the count says every `vm-in` cell in the
  report is a two-pin span, which is what makes it a config-level caveat
  rather than a per-cell one. Its `aggregate = ["config"]` renders it as
  one bullet.
- **`make check-interpret` is 28 s, not "seconds".** The four goldens
  total ~37,000 fact rows and each is produced twice (determinism) and
  rendered twice more (sections 2 and 5). Still two orders below
  `check-harness`, and it never loads the store, but the note's "this
  target is seconds" is optimistic by about a factor of ten.

## 7. What [B13.4] inherits

The skill `/pcrec-bench-interpret` and the committed
`reports/*.interpretation.md` sidecars for §11 Q5's three acceptance
reports. `check-interpret` section 3 already re-renders any sidecar from
its own stamp and requires byte equality, so the sidecars can land
without a further check change. The stamp's `report:` / `index:` /
`predictions:` values are the paths as given on the command line, so the
skill should invoke `interpret` from the repository root with
repo-relative paths.
