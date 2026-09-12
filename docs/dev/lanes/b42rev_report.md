# Lane `b42rev` — report

**Sonnet lane, 2026-09-12. Branch `lane/b42rev`, off master b990b95
(≥ b108f7b as briefed). NOT merged — the manager merges.** Deliverable:
`docs/design/capability_set_v1.md` **v0.2**, revised in place under the
R5 D6 critic panel (`docs/dev/reviews/2026-09-12-r5-capability-set-v1.md`)
and the manager's ratification with Frank's three same-day amendments;
`docs/design/subbench_directory_model.md`'s Q4 correction; two updated
rows in `docs/design/CLAUDE.md`; this report.

## Charter-vs-committed checklist

| the brief asked for | committed | where |
|---|---|---|
| Revise `capability_set_v1.md` in place to v0.2, applying every ratified disposition (CB1-CB8, CS1-CS8, the eight WORTH-NOTING items) | **DONE** | see the step-2 table below; all 24 ids grep-confirmed applied |
| Fold in Frank's rulings: Q1 (licensing floor (c) + the inspired-pattern similarity check) into §4.1/§4.2, closing R8 | **DONE** | §4.1's `gen_provenance.py --check` description now names the similarity-check arm; §4.2's option (c) row is marked RULED, not RECOMMENDED; §13 R8 is marked RESOLVED, not an open risk |
| Q2 (NOT a ratio — realism over contrivance, families 7-12's authored members held to it too) rewrite §4.3 | **DONE** | §4.3 rewritten wholesale: the ratio table and its 80%/50%/0% options are gone, replaced by the realism rule stated once and applied to every family; §3.2's cross-reference and §11.1's L2 dependency column updated to match |
| Q3 (the set is a DRIVER of `.rxt`): §9's Option B WITHDRAWN, §9 becomes a pointer to `rxt_needs_v1.md` + outbox O-26, states the build is PARKED, gives the restart procedure | **DONE** | §9 replaced wholesale (was §9.1-§9.7, six subsections; now one section: the ruling, what v0.1's mechanics leave behind and where they travel, the restart procedure, the six roadblocks). Every internal cross-reference into the old §9.1-§9.7 elsewhere in the file (§3.1 family 6, §4.1's fidelity example, §6.1's variant-location decision, §10(d), §11.1) updated to point at the new §9 or superseded explicitly |
| §9.5's `(?x)`-flattening decision → OPEN question for Frank at the restart (`rxt_needs_v1.md` F-Q2), not a decision this note keeps | **DONE** | both citing sites (§3.1 family 6, §4.1) now say "now an OPEN question for Frank at the restart (`rxt_needs_v1.md` F-Q2)" instead of asserting the flattening as settled |
| Q10/Q11/Q12 RESOLVED/superseded | **DONE** | §12's table marks all three SUPERSEDED with the reason each is moot under Q3 |
| Q3 (Vectorscan) = BLOCK at the restart | **DONE** | §12's Q3 row: **BLOCK, asked at the RESTART**, costs nothing now, trigger stated |
| New STATUS block: v0.2, "revised under R5; BUILD PARKED..."; a revision log, one line per applied disposition id | **DONE** | top of file, lines 1-84: the STATUS paragraph plus a 24-row revision log table naming where each id landed and noting the four (CS8, F8, B6, and part of S10) that travel to `rxt_needs_v1.md`'s own restart material rather than being re-fixed in the replaced §9 |
| §12 rewritten per the consolidation's revised question list, re-marked for the parked state: which questions Frank answers at the restart, which are resolved, the two new DEFAULT items | **DONE** | §12 rewritten entirely: Q1/Q2 RESOLVED, Q10-Q12 SUPERSEDED, Q3 moved to BLOCK-at-restart, Q5/Q6/Q14 DEFAULT-amended, Q4/Q7/Q8/Q9/Q13 DEFAULT unchanged, both new DEFAULT items (family 11 scope, tags→enum) stated with their CB1/CB3 citations |
| [B29] correction: `subbench_directory_model.md` Q4 (lines ~554-560) — the import direction is NOT lossless (schema slug rule forbids `_`, `iso_ts` illegal, M11); §3.3's 63/77 count superseded (0/185 at the widened grammar, N3 §1.2) | **DONE** | a dated CORRECTION paragraph appended directly after Q4 (the note itself untouched otherwise); it corrects both the Q4 claim and, in passing, points out the actual location of the "63 of 77" count is §3.2, not §3.3 as I initially assumed — re-checked against the file's own headers before committing |
| `docs/design/CLAUDE.md`: `capability_set_v1.md` row → v0.2 (status, what changed, parked) | **DONE** | row rewritten: v0.2's status line, the disposition list condensed to one paragraph, v0.1's own summary kept as history under its own label, "Next: the restart" |
| `docs/design/CLAUDE.md`: `subbench_directory_model.md` row gets the correction noted | **DONE** | one sentence appended to the existing row, dated, citing `rxt_needs_v1.md` §1.9 M11 and the superseded 63/77 count |
| Keep every section's alternatives-and-consequences discipline; where a disposition says "state X explicitly", state it, don't merely delete | **DONE** | every drop (§2.2 reason 3, §4.3's ratio table) is replaced by prose stating why, not silently removed; every "state explicitly" disposition (CS1's scope statement, CS4's ranking argument, CS7's caveat) is a stated paragraph, not a checkbox |
| Do NOT re-litigate any disposition | **DONE** | every change traces to a specific disposition id or a named Frank ruling; no finding was second-guessed, narrowed, or reopened beyond what its own disposition specified |
| Cite the review by id where a change lands | **DONE** | every substantive edit carries its id inline (e.g. "(CB7)", "(CS4)") |
| STEP-2 VERIFICATION as a separate final section, 24 ids → section/line → RESOLVED/-WITH-DEVIATION/NOT APPLIED | **DONE** | below |
| Commit incrementally; do not merge; end with a summary | **DONE** | 17 commits on `lane/b42rev`; this report is the last one before handback |

**Nothing is OWED.** No background job, no pending run, no promised number.

## One judgment call worth flagging

The brief's revision-log instruction named `§9 (pointer)` as the landing
spot for four dispositions (CS8, F8, B6, part of S10) that targeted
mechanics of the now-withdrawn Option B. I did not silently drop these —
each is named explicitly in the new §9's "What v0.1's Option B leaves
behind, corrected rather than silently dropped" block, with a one-
sentence statement of the actual correction (CS8's row-kind vs. column
distinction; B6's `Pattern.__init__`/`pattern_bytes()` surface) and where
it travels (into `rxt_needs_v1.md`'s own acceptance checklist, which
already reasons about the delivered format directly). This is a
deliberate reading of "superseded," not an omission: fixing CS8's exact
gate wording against a format that is about to be replaced wholesale
would produce prose this note would immediately need to discard again at
the restart. The manager should treat this as the intended handling, not
a corner cut, and can check it against the CLAUDE.md rule that the
revision "keep every section's alternatives-and-consequences discipline"
— the alternative (re-fixing §9's dead mechanics anyway) and its cost
(prose with a known, dated expiration) is stated inline at each site.

## STEP-2 VERIFICATION (session_discipline.md §7(b))

Every one of the 24 consolidated disposition ids, independently re-
checked against the committed v0.2 text (not against my own memory of
having applied it) by grepping the id and reading each hit in place.

| id | disposition (one line) | v0.2 location | status |
|---|---|---|---|
| CB1 | family 11 narrowed to the shared-convention population; cross-convention scoring deferred | §3.1 (row 11 + the "Family 11's v1 scope, narrowed" note, ~line 260), §5.6's opening paragraph, §11.1's L5 row, §12's new question | **RESOLVED** |
| CB2 | §5.7's "Already built" corrected to UNBUILT; L5 reclassified from a check to a build task | §5.7 rewritten (~line 888), §11.1's L5 row, §13 R7 | **RESOLVED** |
| CB3 | wild/designed bucketing promoted from `patterns[].tags` to real enumerated fields | §4.1's "What the RECORD carries (CB3, revised)" (~line 512), §1.1's requirement-(1) row, §10(d) | **RESOLVED** |
| CB4 | `noseyparker.txt` re-fetch confirmed; family 4 raised; Appendix A's "three OWED" → two | §3.1 family 4 row (~line 229), Appendix A's family-4 row and closing sentence | **RESOLVED** |
| CB5 | `atomic-possessive` split; Oniguruma's atomic-group claim flagged for independent re-derivation | §5.1, two new rows replacing the one `atomic-possessive` row (~line 684-685) | **RESOLVED** |
| CB6 | `k-reset`'s Oniguruma gap resolved before an `onig-*` config declares it | §5.1's `k-reset` row (~line 688) | **RESOLVED** |
| CB7 | `hazard_class` assigned per family (min. 2, 10) | §3.1's new "Per-family `hazard_class` (CB7)" block (~line 242) | **RESOLVED-WITH-DEVIATION** — went beyond the minimum (2, 10) and assigned family 5 `ambiguous-decomposition` too, since that family's own stress-mechanism prose already uses that exact enum phrase verbatim; every other family is stated `none` rather than left silent, which the disposition's own "at minimum" wording invites but does not require |
| CB8 | family 10's calibration risk stated; a mitigation adopted | §3.5's new paragraph (~line 433), §13 R6 | **RESOLVED** |
| CS1 | `match`-regime family list corrected (drop 7/8); scope stated | §3.5, the bulleted list rewritten (~line 366-390) | **RESOLVED** |
| CS2 | §2.2 reason 3 dropped | §2.2, reason 3 removed, reasons renumbered 1-3, the alternatives table's "four reasons" corrected to "three" with the dropped reason's fate stated inline | **RESOLVED** |
| CS3 | Q3 re-marked BLOCK | §5.6's recommendation paragraph (~line 866), §12's Q3 row | **RESOLVED** — folded into the ratification's amendment 3 rather than treated as a separate ruling, per the brief's own framing |
| CS4 | `ru_maxrss` ranked within the native-driver population | §7.4's rewritten recommendation (~line 1105), §7.5's summary table row, §12 Q6 | **RESOLVED** |
| CS5 | TRE `named-groups`/`free-spacing` cited or marked UNCONFIRMED | §5.1, both rows (~line 691-692) | **RESOLVED** |
| CS6 | §13 R2's family list, "2, 7-10" → "2, 7-9" | §13 R2 (~line 1522) | **RESOLVED** |
| CS7 | §8.1 states the permanent `inconclusive-spread` caveat | §8.1's new closing paragraph (~line 1214), §12 Q14 | **RESOLVED** |
| CS8 | "no build directives" gate mechanism corrected | §9's "What v0.1's Option B leaves behind" bullet 1 (~line 1263) | **RESOLVED-WITH-DEVIATION** — not fixed as a standalone §9.2/§9.4 rewrite (there is no v0.2 §9.2/§9.4 to fix); the correction is stated and explicitly routed to `rxt_needs_v1.md`'s own acceptance checklist, per the ratification's own text ("CS8's row-kind correction... travel to the needs note and the restart acceptance checklist rather than to a v0.2 §9") |
| F5 | `pcre2-dfa`'s §8 row: not a dial | §8's table, the `pcre2-dfa` row rewritten (~line 1163), §1.1 | **RESOLVED** |
| F6 | pcrec's §8 row maps dials vs. diagnostic controls | §8's table, the pcrec row rewritten (~line 1164), §1.1 | **RESOLVED** |
| F8 | L3/L4 sequencing gap | §9's "What v0.1's Option B leaves behind" bullet 1, §11's new opening paragraph (~line 1370) | **RESOLVED-WITH-DEVIATION** — same shape as CS8: stated as superseded by the §9 replacement rather than fixed as a standalone sequencing patch, since the L3/L4 split itself is what the restart re-derives against the actual delivery |
| S9 | `automaton_class` column for TRE/Oniguruma | §7.1's table, a column added for every row (~line 1023-1043) | **RESOLVED** |
| S10 | family 12's `canonical_text` omission | §3.1's new "Family 12's `canonical_text` (S10)" note (~line 282) | **RESOLVED-WITH-DEVIATION** — the disposition said "state this in §9.5"; since §9.5 no longer exists (§9 replaced wholesale), the statement was relocated to §3.1's own family-12 material, which is where a reader would look for it regardless of where `.rxt` ends up |
| S11 | Vectorscan boolean-grain cost grounded in the driver protocol | §5.6's option-B row (~line 861), plus a new paragraph on the throughput-regime `NMATCHES` gap (~line 877) | **RESOLVED** |
| B6 | `subbench.py` loader surface understated | §9's "What v0.1's Option B leaves behind" bullet 1 (~line 1268) | **RESOLVED-WITH-DEVIATION** — same routing as CS8/F8: named and pointed at the restart's own scoping rather than fixed as a standalone §9.3 correction, since §9.3 (the old loader-change subsection) no longer exists |
| B7 | first production exercises of two schema values | §5.3's new "Noted, not a defect (B7)" paragraph (~line 763) | **RESOLVED** |

**24/24 RESOLVED or RESOLVED-WITH-DEVIATION; 0 NOT APPLIED.** Five
carry a stated deviation (CB7, CS8, F8, S10, B6) — every one because the
disposition targeted either a level of specificity beyond the minimum
asked (CB7) or a subsection this revision was separately instructed to
replace wholesale (CS8, F8, B6, S10's original "§9.5" home). Each
deviation is named in the table above with its reason, not silently
absorbed.

## Not touched

`bench/`, `schema/`, `pcrecbench/`, `testees/` — untouched, per the
mandate. No `make` target run (none is meaningful for a design-only
revision). `docs/design/rxt_needs_v1.md` itself is untouched — the brief
scoped this lane's writes to `capability_set_v1.md`,
`subbench_directory_model.md`'s Q4 correction, and the two
`docs/design/CLAUDE.md` rows; `rxt_needs_v1.md` is cited freely
throughout but was not in scope to edit.
