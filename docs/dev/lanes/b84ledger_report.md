# lane b84ledger report — [B84] the ledger: I-102 acceptance grid at 6ef76820

**Task**: read-only extraction lane, score pcrec's [OPT-PRECHECK-ADMIT]
fix (pin `6ef76820`, abi 31) against inbox I-102's acceptance grid on
`bench/capability@0.1`, against BEFORE = the four `pcrec_b1885a83_*`
records. No worktree needed (read-only, no build, no measurement); wrote
exactly one new file in the main tree plus this report. **Did not
commit** — per the brief, the manager reviews and commits.

**Delivered**: `docs/dev/ledgers/2026-09-23-precheck-admit-after-
6ef76820.md` (uncommitted, present in the working tree).

## Change request (team-lead, second pass) — four fixes, applied

1. **The "4 G1 cells" are NAMED — remove the `floor-byte` inference.**
   DONE. `cycle1_ledger_reading.md` §4.3's own "duplicated pass (G1)"
   rows name `wild-codegrammar-json-array-begin`/`large-subject-
   throughput` × all four testees — the withdrawn `floor-byte` reading
   is replaced (§1.6). This population is IDENTICAL to letter (c)'s own
   (§1.3): re-scored by cross-reference, not re-measured. Result
   unchanged in substance (3/4 MEET, `vm-in-caps` +1.84% MISS), but now
   correctly attributed. Every downstream reference (summary table,
   §2's sweep exclusion note, finding 4, finding 7) updated to match.

2. **The 29 G2 cells, reconstructed by name where possible.** DONE.
   Re-read §2.2/§4.2/§4.3's own explicit "(G2)"/carve-out labels and
   pulled 12 of the 29 by exact citation (§1.5's table: `uuid-near-
   miss`/`ipv4-near-miss` DFA route × both regimes = 8 cells, §2.2/§4.2;
   `winpath-near-miss`/srch × 2 testees, `wild-validator-ipv4-owasp`/
   srch/`auto-nocaps`, `logparse-atomic-removed`/srch/`auto-nocaps` = 4
   more, all from §4.3's table). These 12 are now the PRIMARY (e)
   population: **12/12 MEET.** The 72-cell 9-pattern superset is kept as
   the SECONDARY table (§1.5b) exactly as instructed, with the 17-cell
   gap stated explicitly (§2.1's own table shows zero attributable
   regressions and cites patterns outside the G2 9-pattern list, so "8
   of §2.1"/"13 of §2.2" could not be traced to specific additional
   rows beyond the 12 already found). Secondary result: 21/72 regress
   under before-IQR; 17/72 also exceed pcrec's own null band (fix 4).

3. **The give-up: facts only.** DONE. Removed the "double duty / fast
   correctness short-circuit" causal sentence from §1.5 and from
   finding 3. Replaced with: the per-subject outcome table (BEFORE
   matched 5/5 vs AFTER `gave-up` 5/5 `PCREC_ERR_STEPS`, 50 gave-up rows
   total = 5 subjects × 5 trials × 2 testees), and a stamp table (`req_
   byte`/`req_run`/`req_why`/`end_window` BEFORE vs AFTER, all four
   testees) with an explicit closing line: "what the removed pre-check
   did for these five subjects... is not established by these records
   and is not claimed here; it is pcrec's own to diagnose."

4. **Whole-population sweep: null band made explicit and separate.**
   DONE. §2 now states up front that the primary 133/414 sweep count is
   IQR-only, no null band applied. Added a secondary count under `|Δ| >
   max(IQR, 8.4605%)` — pcrec's own cited band (`cycle1_ledger_
   reading.md` §9(B)/O-48 Block B, 120 program-identical cells, min
   −5.7393%/max +8.4605%/median −0.0806%), labelled explicitly as
   PCREC's measured band, not this ledger's/[B79]'s own: **1 improve, 17
   regress** (vs 88/133 under IQR-only) — both counts stated side by
   side, neither hidden. The same secondary count was applied to the
   (e) superset's 21 regressions (17 of 21 survive the null band, 4
   fall inside it — table column added, §1.5b).

## Original charter-vs-committed checklist (first pass, still valid)

1. **BEFORE/AFTER sourced from the named record files, not the whole
   store.** DONE — ledger §0.1, no CLI, no whole-store load.
2. **Follow the prior ledger's shape and discipline.** DONE — ledger
   §0.2/§0.3 (Type-7 IQR, `(after-before)/before`, before-IQR as the
   bar), cross-checked against the committed cross-pin report TSV.
3. **Score (a)-(h) from I-102's own text, EXPECT stated, cells named.**
   DONE — §1.1-§1.9 (now including §1.5b), updated per fixes 1-3 above.
4. **Whole-population regression sweep, count and list.** DONE — §2,
   updated per fix 4 above.
5. **REQ_WHY census, fourth (now stated as fifth) independent
   derivation.** DONE — §3: 79/27, 67/27, 27/9, 14/7 over 187
   artifact-configs, digit-exact, unaffected by this change request.
6. **Summary table at top, met/missed/partial.** DONE — updated to
   carry the primary-12/secondary-72 split and the NAMED G1 row.
7. **State what was read and not read.** DONE — §4 updated: the G1 gap
   is now closed (fully resolved), the G2 gap is now 17/29 (down from
   "the full 29"), stated as such.
8. **Numbers only — no diagnosis, no outbox prose.** Tightened by fix 3
   above; the one remaining mechanism note (DFA-vs-forced-VM dominance
   scope in §3, explaining why `floor-byte`'s REQ_WHY diverges by
   config) is a direct reading of the compile-row stamps, not a causal
   claim about timing.

## Beyond the charter — one finding not explicitly asked for

Section 1.5 surfaces a **new give-up** (not a D119 timing question) on
`email-nested-plus`/`short-subject-search`/forced-VM: 5 of 75 subjects
that passed BEFORE now read `gave-up` / `PCREC_ERR_STEPS` AFTER. This
was found by a full before/after per-subject scan across every
`(pattern, regime, testee)` cell present on both pins (not just the
named populations) — confirmed to be the ONLY such newly-broken cell
anywhere, named or swept, with no cell resolving in the reverse
direction. Flagged prominently at the top of the ledger's summary since
it is a correctness-adjacent regression the D119 bar's timing framing
does not itself surface.

## Not done / OWED

- **Not committed** — the ledger and this report sit uncommitted in the
  working tree per the brief ("DO NOT commit — the manager reviews and
  commits").
- **The "4 G1 cells" identity is now RESOLVED** (§1.6) — no gap remains
  there. **17 of the 29 G2 cells remain un-locatable by name** in the
  two `~/pcrec` documents read in full (`cycle1_ledger_reading.md`,
  `cycle2_batch2_reading.md`); the gap is named explicitly (§1.5, §1.5b,
  §4) with the 12-cell primary population and its citations, rather than
  silently guessed or omitted. If a more granular source exists
  elsewhere in `~/pcrec` (not found by this lane's search), the manager
  or a follow-up lane can re-score §1.5b's remaining 17-cell gap
  against it.
- **The class-pure views (I-99) / cross-class anomaly query (I-101)
  render** — I-102's own "standing practice" note asks for these IF
  [B82]'s reporter change has merged; this lane did not check [B82]'s
  merge status or attempt that render, since the brief's own deliverable
  is the ledger's numbers, not a report regeneration. OWED to whoever
  owns that render, if not already done.
- No `store/` record written or modified; no measurement run; no
  `~/pcrec` write of any kind (two `git show <commit>:<path>` reads
  against already-fetched history only).

## For the manager, on review

- The ledger's own top-level verdict is **mixed, not a clean pass**:
  the four literal target letters (a)/(b)/(d), the NAMED "4 G1 cells"
  (now = letter (c)'s own population), the (e) population's PRIMARY 12
  named cells, and controls (f)/(g)/(h) are all clean, near-clean, or
  trivial — but the (e) population's SECONDARY 72-cell superset still
  MISSES "improvement or flat, none regressing" (21/72 regress
  before-IQR, 17/72 beyond pcrec's own null band too), and a genuine new
  give-up appears on one forced-VM cell. This is a materially different
  headline than a pure "[OPT-PRECHECK-ADMIT] accepted" reading would
  suggest from (a)-(d) alone.
- The "4 G1 cells" gap is now closed; the G2 gap narrowed from "all 29
  unlocatable" to "17 of 29 unlocatable" — the remaining 17 sit
  somewhere in the 72-cell superset (§1.5b), which this ledger scores
  in full. Worth a line back to pcrec only if the manager wants the
  exact remaining 17 identified: `cycle1_ledger_reading.md`'s own
  "8 of §2.1, 13 of §2.2" phrase references row counts this lane could
  not trace to specific cells beyond the 12 found (§2.1's own table
  shows zero attributable regressions and cites patterns outside the G2
  9-pattern list) — either a source this lane did not find carries the
  itemized rows, or the phrase is a summary count without an underlying
  itemized table.
