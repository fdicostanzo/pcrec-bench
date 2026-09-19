# THE LEDGER — capability@0.1's ext-bench roster SECOND SAMPLE (TRE `high-byte-run` reproducibility)

Read-only extraction over lane `b54extwindow`'s 2026-09-18/19 window
(`build/windows/window_capability_ext2_20260919T032134Z.log`,
23:21:34 EDT 2026-09-18 → 00:16:31 EDT 2026-09-19), charter
`docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` §8 item 2 (the
prior ledger, hereafter **LEDGER-1**) — the SECOND SAMPLE on
`re2-default`, `tre-default`, `vectorscan-block-nosom` alone, no pcrec/
pcre2 arm, re-checking whether TRE's `high-byte-run` correctness gap
(0% throughput / 48% search pass rate on the first sample) is
reproducible or was a one-off box artifact. Also answers LEDGER-1 §8
item 3 (a DOC CHECK: does `onig-default`'s `-17:retry` give-up code
correspond to Oniguruma 6.9.10's own documented retry-limit-in-match
mechanism) — that check touches no record from this window and is
read entirely from `testees/onig/`'s own committed sources, per its own
brief item 3.

Three new pinned records, `store/index.tsv` **178 → 181** (per lane
`b54extwindow`'s own report — confirmed here directly:
`grep -c $'\t'` over `store/index.tsv`'s body reads 180 data rows, the
header excluded).

Numbers only; the manager's interpretation and the outbox item are not
this lane's to write — §4 below is a RECOMMENDATION only, per this
lane's own brief item 4.

**Ratio convention: `A ÷ B`, so > 1 means A is SLOWER (or larger),
unless stated otherwise.** No ratio is computed in this ledger — every
number cited below is a pass-rate or a wrong-answer count read directly
from a committed TSV, compared cell for cell across two dates.

**CONTEXT-AROUND-NUMBERS (Frank's directive, memory
`feedback-context-around-numbers`): every population this ledger reads
is stated explicitly below, not only its result.** §1's reproduction
table names both samples' `n` (subject count) and trial count
explicitly, not only the pass-rate; §2's doc check states exactly which
files were read and which were not (no network fetch, no source outside
`testees/onig/`).

---

## 0. SOURCES, SAMPLE SHAPE, HYGIENE

### 0.1 Records and window

| cell | testee | timestamp | status |
|---|---|---|---|
| 1 | `re2_11.0.0_default-caps-simdna` | 2026-09-19T03:22:09Z | measured, attempt 1 |
| 2 | `tre_0.9.0_default-caps-simdna` | 2026-09-19T03:36:12Z | measured, attempt 1 |
| 3 | `vectorscan_5.4.11_block-nosom-nocaps-simd` | 2026-09-19T03:55:52Z | measured, attempt 1 |

(`store/index.tsv`, grepped directly.) Per-cell EDT wall clock, from
lane `b54extwindow`'s own committed report (`docs/dev/lanes/
b54extwindow_report.md`, its charter-vs-committed checklist row 1):
`re2-default` 23:22:04–23:35:52, `tre-default` 23:36:07–23:55:32,
`vectorscan-block-nosom` 23:55:47–00:16:16 — three cells back to back,
total window wall 23:21:34 EDT 2026-09-18 → 00:16:31 EDT 2026-09-19
(54 min 57 s), all rc=0, five trials each.

### 0.2 Reports and their query

| cite | file |
|---|---|
| `TSV2:<line>` | `reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.tsv` (this window) |
| `MD2:<line>` | `reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.md` |
| `SIDE2:<line>` | `reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.interpretation.md` (catalogue 2.0, reporter v18) |
| `TSV1:<line>` | `reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv` (the FIRST sample, LEDGER-1's Report B) |
| `LEDGER-1:<§>` | `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md` |
| `LOG:<line>` | `build/windows/window_capability_ext2_20260919T032134Z.log` |
| `KB:<n>` | `docs/dev/known_issues.md` |

Query (both `.md2`'s own header and `MD2:1-13`): `report --subbench
capability --version 0.1 --since 2026-09-18T06:00:00Z --until
2026-09-19T05:00:00Z --testee re2_11.0.0_default-caps-simdna --testee
tre_0.9.0_default-caps-simdna --testee
vectorscan_5.4.11_block-nosom-nocaps-simd` — **3 record(s) matching this
query; 3 included; 0 superseded** (`MD2:7-9`). `worst_other_core_busy:
33.33%` (`re2_11.0.0_default-caps-simdna` / `logparse-atomic-removed` /
`large-subject-throughput`, `MD2:7`) — a single reading, not shown to
move any number below (no re-run, no retry fired on any of the three
cells). Schema version: `1.6` on all three (`TSV2` header comment,
matching cf0962e3's abi-26 pin — no new pcrec record is in this
population at all: this is a THREE-ENGINE, NO-PCREC, NO-PCRE2 report,
same narrowed no-reference-arm shape as LEDGER-1's Report B).

### 0.3 Hygiene

All three records read `agreement: agree` (`MD2:9-11`): `re2-default`
"agree (0 of 77 groups; 0 of 3037 rows; 5 unjudged; k=1.5, 2/3; 5
trials)", `tre-default` "agree (0 of 79 groups; 0 of 3142 rows; 56
unjudged; k=1.5, 2/3; 5 trials)", `vectorscan-block-nosom` "agree (0 of
80 groups; 0 of 3118 rows; 2 unjudged; k=1.5, 2/3; 5 trials)". No
`disagree`, no failed after-sample, no scratch-tier row
(`SIDE2:203-206`, the `R-STATUS-9`/`R-STATUS-10`/`R-STATUS-11`
no-matching-rows lines). The one `worst_other_core_busy` reading
(33.33%) is well under the pre-flight's 10% RUN-time gate — an
AFTER-sample, provenance-only reading (schema v1.4's own rule), not
shown to move any cell here.

---

## 1. LEDGER-1 §8 ITEM 2 ANSWERED: THE TRE `high-byte-run` GAP REPRODUCES BYTE-IDENTICAL, ACROSS TWO INDEPENDENT SAMPLES, ONE DAY APART

LEDGER-1 §5.4 flagged `high-byte-run`'s TRE pass rate — 0% on
`large-subject-throughput`, 48% on `short-subject-search` — as "the
widest correctness gap of anything measured in this bench's history for
a capability-declared-satisfied pattern" and its own §8 item 2 named the
open question directly: is the split (0% vs 48% on the SAME pattern)
reproducible, or a one-off box artifact. This window is that re-check,
and the answer is that the gap reproduces to the exact wrong-answer
count on both regimes:

| cell | first sample (2026-09-18) | second sample (2026-09-19) | reproduces? |
|---|---|---|---|
| `high-byte-run` / `large-subject-throughput` / `tre-default` | `pass_rate 0.0000`; n=3 subjects; `n_wrong=15` (`TSV1:` `excluded` row, verified directly: `awk` over `TSV1` for `$1=="excluded" && $2=="high-byte-run"` prints `large-subject-throughput … pass_rate 0.0000 3 0.0000 0 15 0`) | `pass_rate 0.0000`; n=3; `n_wrong=15` (`TSV2:306`) | **YES, byte-identical**: `n_wrong` counts TRIALS (3 subjects × 5 trials = 15, not 3 — the reporter's own `n_gave_up`/`n_wrong` convention, `SIDE2:27`'s parenthetical), and both samples read the identical 15/15 |
| `high-byte-run` / `short-subject-search` / `tre-default` | `pass_rate 0.4800`; n=75; `n_wrong=195` (`TSV1:`, same `awk` filter, `short-subject-search` row) | `pass_rate 0.4800`; n=75; `n_wrong=195` (`TSV2:320`) | **YES, byte-identical**: 195 of 375 trials wrong (75 subjects × 5 trials), both samples |
| `tag-pair-match` / `short-subject-search` / `tre-default` | `pass_rate 0.9867`; `n_wrong=5` (LEDGER-1 §5.4 table, `B-TSV:1073`) | `pass_rate 0.9867`; `n_wrong=5` (`TSV2:607`) | **YES** |
| `wild-waf-crs-942360-concat-sqli` / `short-subject-search` / `tre-default` | `pass_rate 0.9867`; `n_wrong=5` (LEDGER-1 §5.4 table, `B-TSV:2480`) | `pass_rate 0.9867`; `n_wrong=5` (`TSV2:1418`) | **YES** |
| `tre-default` `did_not_compile` set | `{wild-datetime-datefinder-alternation, wild-secrets-username-password-pair, wild-waf-crs-942500-comment-obfuscation}`, diagnostic `tre_regncompb failed (code 11): Invalid character range` on all three, both regimes (LEDGER-1 §5.1, `B-TSV` compile census) | the SAME three patterns, the SAME diagnostic verbatim, both regimes (`TSV2:811,825,991,1005,1432,1446`, six rows checked directly) | **YES, unchanged** |

**`re2-default` and `vectorscan-block-nosom` both stay CLEAN on
`high-byte-run` in both samples**: neither testee has an `excluded` row
for `high-byte-run` in either `TSV1` or `TSV2` (checked directly, both
files — the reporter's own rule puts any cell with a wrong answer under
`excluded`, so absence from that section at either date is the pass-rate
1.0000 confirmation), and both rank normally on the `large-subject-
throughput` and `short-subject-search` groups for that pattern in this
window (`TSV2:294-305,308-318` — `vectorscan` rank 1, `re2-default` rank
2, both `measured`/`pinned`, no exclusion).

**VERDICT: the gap is TRE-SPECIFIC and NOT a one-off box artifact.**
Two independent samples, measured a day apart under two different
window runs, on the SAME pattern, SAME regimes, SAME subject counts,
return the IDENTICAL wrong-answer count to the trial — the strongest
form of reproduction this bench's own trial-agreement machinery can
show (every trial in both samples separately passed its own
`agree`-gate at k=1.5, §0.3), and the two clean engines on the same
pattern rule out a shared box/harness cause. LEDGER-1's own next-sample
checklist item 2 is answered: NOT a one-off; TRE's own byte-mode
matching (`tre_regncompb`) reads `high-byte-run` wrong on the same
fraction of subjects every time it is asked.

---

## 2. LEDGER-1 §8 ITEM 3 ANSWERED (DOC CHECK, NO MEASUREMENT): `onig-default`'s `-17:retry` code DOES correspond to Oniguruma 6.9.10's own documented retry-limit-in-match mechanism

LEDGER-1 §5.4 read `onig-default`'s `evil-alt-nested` give-up as a "NEW
code, `-17:retry×2 (smallest: rd-evil-alt-near-miss, 18 B)`" without
checking the code against Oniguruma's own documentation; its §8 item 3
named that check as owed. **This ledger touches no record from this
window** — the check is read entirely from `testees/onig/`'s own
committed adapter sources, per the brief's own scope ("from the
vendored/pinned Onig sources or docs under `testees/onig/` ONLY (do not
fetch the network)"). No network fetch was made; every citation below is
a file already committed in this checkout.

**CONFIRMED, by direct citation of three files, all inside
`testees/onig/`:**

1. `testees/onig/driver.c:50-76` (a source-header comment on the
   driver's own give-up handling, dated 2026-09-17, "by DIRECT SOURCE
   READ of this box's installed Oniguruma 6.9.10... + a direct read of
   src/regparse.c and src/regexec.c"): names four match-time
   resource-limit codes raised in `regexec.c`, including
   `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER (-17) DEFAULT budget 10,000,000
   (regint.h DEFAULT_RETRY_LIMIT_IN_MATCH) -- NOT unlimited: a
   catastrophic-backtracking witness CAN give up under onig-default with
   no special config."
2. `testees/onig/adapter.py:107-111` (`GAVE_UP_CODES`, the dict the
   adapter's own driver-output parser reads to classify a negative
   `onig_search`/`onig_match` return as `gave-up` rather than `crashed`):
   `-17: "ONIGERR_RETRY_LIMIT_IN_MATCH_OVER"`, with the same "DEFAULT
   budget 10,000,000" comment, sourced (per the file's own preceding
   comment block, lines 101-106) from "DIRECT SOURCE READ of this box's
   installed Oniguruma 6.9.10 (`/usr/include/oniguruma.h`... `src/
   regexec.c` cross-referenced at the same tag)... every code below is
   where regexec.c's own `MATCH_AT_ERROR_RETURN`/direct `return` sites
   raise it."
3. `testees/onig/CLAUDE.md`'s own `## \`gave-up\`: MEASURED to fire at
   DEFAULT settings...` section: states the same four codes from
   `src/regexec.c`, and adds a LIVE confirmation this ledger did not
   itself re-run but that is already committed evidence: "the classic
   catastrophic-backtracking witness `(a+)+$` over 40 `a`s followed by a
   non-matching byte gives up under `onig-default`'s UNMODIFIED defaults
   in ~0.21 s — `giveup:-17:retry-limit-in-match over`." — the EXACT
   string-shape (`-17:retry...`) the capability window's own
   `evil-alt-nested` finding (LEDGER-1 §5.4) prints.

**READING**: `-17:retry` is not an ad hoc or under-documented code — it
is Oniguruma's own named error `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER`,
raised in `src/regexec.c` when the match-time retry count exceeds
`DEFAULT_RETRY_LIMIT_IN_MATCH` (10,000,000, defined in `src/regint.h`),
a genuine, intentional, documented resource-limit guard that ships
active by default (not merely available via the later, unwired
`onig-lowretry` config `testees/onig/CLAUDE.md` names as a "LATER
config"). The correspondence LEDGER-1 §8 item 3 asked about is
CONFIRMED — the code the capability window observed on
`evil-alt-nested` IS the library's own documented mechanism, not a
harness misreading or an undocumented internal.

**What this check did NOT do**: it did not re-run `evil-alt-nested`
through `onig-default` (that cell is not in this window's population —
`onig-default` was not part of this lane's three-testee roster), and it
did not read Oniguruma's upstream web documentation or issue tracker
(scope forbids network fetch) — the confirmation rests entirely on the
adapter's own already-committed, already-cited direct source reads
(2026-09-17, lane `l6bonig`), which this ledger re-verifies by re-citing
the same three files rather than taking the adapter's word for it
uncited.

---

## 3. THE TWO OPERATIONAL INCIDENTS

### 3.1 The subject-tree refusal (first launch attempt, not committed, no store change)

Per lane `b54extwindow`'s own report (`docs/dev/lanes/
b54extwindow_report.md`, "Two incidents" item 1): the lane's FIRST
launch attempt refused all three cells instantly, rc=1, because its
worktree had never run `bench/capability/gen_subjects.py` /
`gen_throughput_subjects.py` (the gitignored subject trees are per-
worktree, not per-repo). Nothing was measured, nothing was written to
the store; the lane generated both trees (manifests reproduced
byte-identical to the committed ones, confirmed by the lane's own `git
diff` check) and relaunched. This left no record and no report trace —
the only evidence is the lane's own report and (per §3.2 below) the
window log's line count.

### 3.2 KB-23's own sentinel finding: `WINDOW_RUN_COMPLETE` fired over the all-refused first attempt

`docs/dev/known_issues.md` KB-23 (filed by the manager this session,
titled "the window sentinel fires over all-refused cells") is the
DIRECT account of §3.1's incident, not a separate one: `scripts/
run_window.sh` printed `WINDOW_RUN_COMPLETE` after all three cells of
the first launch attempt exited `rc=1` inside one second each — the
script's own end-of-window sidecar-regeneration step ran regardless, and
the sentinel line means "control flow reached the end of the script",
not "cells succeeded". KB-23 is OPEN (no fix landed): the manager caught
the false-positive from outside by the attempt's 76-second wall time,
not from the sentinel. KB-23's own text states the standing workaround
until a ruling on shape lands: "never judge a window by its sentinel;
read the per-cell rc lines." This ledger's own §0.1/§1 tables are built
from `store/index.tsv` and the committed report TSVs — the per-cell
truth — never from a sentinel line, consistent with KB-23's own
prescription.

(The lane's report also names two background-notification stalls during
its OWN run — waiting on a relaunched window's completion marker once,
waiting on a report-CLI render once, both cases where the underlying
command had actually finished before the lane noticed. Those cost real
wall time but moved no store or report content; they are not part of
this window's own measurement record and are not treated as findings
here — the brief names only the subject-tree refusal and KB-23's
sentinel as this section's two incidents.)

---

## 4. PREDICTIONS: NONE SCORED FOR THIS WINDOW, AND WHY

`docs/dev/predictions/capability-0.1-ext-roster.tsv` (19 evaluable
clauses P1-P10, authored by lane `b51preds`, landed 2026-09-18 —
`docs/dev/wake.md`'s own standing fact, §"Standing facts": "The ext-roster
predictions file CANNOT be CLI-scored until F27's fix lands (that's F27,
not a file bug)") is the file that WOULD score this window's own
reproduction question directly: its `P2.a`/`P2.b` clauses (read from the
file itself,
`docs/dev/predictions/capability-0.1-ext-roster.tsv`) state, verbatim:

- `P2.a`: selector `pattern=high-byte-run;regime_or_na=large-subject-
  throughput;...testee=tre_*_default-caps-simdna`, quantity `n_wrong`,
  op `eq`, value **15** — "REPRODUCTION reading: high-byte-run's
  throughput cell reads n_wrong=15 again... a ONE-OFF box artifact would
  instead read a value strictly between 0 and 15".
- `P2.b`: same shape for `short-subject-search`, value **195**.

Both clauses are EXACTLY the comparison §1 of this ledger made by hand
above, and both would score **CONFIRMED** against `TSV2:306,320` if run
through `pcrecbench interpret` today. **They were not, deliberately**:
this lane's brief and `docs/dev/wake.md`'s standing fact both say the
gate that would let `interpret` join `capability-0.1-ext-roster.tsv`
against a report's population is blocked on pcrec's **F27** fix (named
in `docs/design/predicate_audit_v1.md` v1.1 §7 as "the F27 gate fix
(OD-B15 dedup-key anchor + signature change)", still awaiting Frank's
ruling per `docs/dev/wake.md` READ item 3) — scoring the file today
would either silently mis-score against the wrong dedup anchor or exit
on the known gate defect, per the standing fact's own wording. Lane
`b54extwindow`'s own sidecar (`SIDE2`) was generated against
`docs/dev/predictions/capability-0.1-first.tsv` only (the OLD
seven-testee-roster file, whose P1-P10 clauses are ALL `not evaluable`
against this three-engine population — `SIDE2:183-193`, `R-PRED-3`
firing 9 times, none of which name `re2`/`tre`/`vectorscan` at all), not
against the ext-roster file — consistent with the brief's explicit "do
not touch/score" instruction.

**What WILL score it later**: once F27 lands and the predicate-audit fix
wave (chartered per `docs/dev/wake.md` work-queue item 2) closes, a
fresh `pcrecbench interpret --report reports/2026-09-19-capability-0.1-
budu-ryzen1600-ext-second-cf0962e3.tsv --predictions
docs/dev/predictions/capability-0.1-ext-roster.tsv` run should machine-
confirm `P2.a`/`P2.b` (and, if the dedup-key anchor change does not
alter which record this query resolves to, every other evaluable clause
in that file against this window's population) — this ledger's §1 is
the manual proof that the machine scoring, once unblocked, will agree.

---

## 5. RANKED FINDINGS

1. **LEDGER-1 §8 item 2 ANSWERED**: TRE's `high-byte-run` correctness
   gap reproduces byte-identical across two independent samples one day
   apart (§1) — `n_wrong=15`/`195` on both dates, both regimes, plus the
   two family-11-shaped patterns (`tag-pair-match`,
   `wild-waf-crs-942360-concat-sqli`) at the identical `n_wrong=5`, and
   the same three-pattern `did_not_compile` set with the identical
   diagnostic. `re2-default` and `vectorscan-block-nosom` stay clean on
   the same pattern both times, ruling out a shared box cause. This is
   settled TRE behavior, not a one-off.
2. **LEDGER-1 §8 item 3 ANSWERED**: `onig-default`'s `-17:retry` code IS
   Oniguruma 6.9.10's own documented `ONIGERR_RETRY_LIMIT_IN_MATCH_OVER`
   (§2), confirmed from three files already committed under
   `testees/onig/`, no network fetch, no new measurement.
3. **Two operational findings, already filed**: the per-worktree
   subject-tree generation step is a real setup dependency that silently
   refuses a fresh lane's first launch (§3.1), and `scripts/
   run_window.sh`'s `WINDOW_RUN_COMPLETE` sentinel is not evidence of
   success (§3.2, KB-23, OPEN) — both already have their own accounts
   (the lane's own report; `docs/dev/known_issues.md` KB-23) and neither
   is a new finding of this ledger.
4. **No prediction clause was machine-scored this window** (§4), by
   design — the file that would score it exists and its two relevant
   clauses would both read CONFIRMED by hand, but CLI scoring stays
   blocked on pcrec's F27 fix, a pre-existing, already-tracked gate
   defect.

---

## 6. OUTBOX DISPOSITION (RECOMMENDATION ONLY — not sent by this lane)

**Recommend NO new item to pcrecdev1's inbox from this window.** TRE's
correctness gap is bench-side, ext-engine material — it belongs in
`docs/dev/upstream_findings.md` (added as U6 alongside this ledger, §7
below), never in pcrec's own inbox, exactly as this lane's brief states
("TRE findings are OUR upstream_findings.md material, NOT pcrec's
inbox"). The one item that DOES touch pcrec — the F27 gate fix blocking
predictions scoring — is already tracked in
`docs/design/predicate_audit_v1.md` v1.1 §7 and `docs/dev/wake.md`'s
work queue item 2; this window adds no new information to that item (it
confirms the block is still in effect, nothing more) and does not
warrant a second outbox entry. The two operational incidents (§3) are
bench-side harness/tooling matters (KB-23 already filed); neither
implies a pcrec-side ask.

**What the manager may want to do with this ledger's own findings**:
mark `docs/dev/wake.md`'s work-queue item 3 ("the next capability window
... the ledger §8 checklist — TRE-gap reproduction is the headline")
as answered for its reproduction half, leaving the predictions-scoring
half open pending F27; consider whether `testees/tre/CLAUDE.md` should
gain a second addendum line noting the gap is now CONFIRMED reproducible
(LEDGER-1 §7 candidate ask 2 already recommended a first addendum after
the first sample — this ledger's finding strengthens that recommendation
without changing its content).

---

## 7. NEXT-SAMPLE CHECKLIST

1. Once pcrec's F27 fix lands and the predicate-audit gate reopens,
   re-run `pcrecbench interpret` against
   `docs/dev/predictions/capability-0.1-ext-roster.tsv` and this
   window's report — confirm `P2.a`/`P2.b` score `R-PRED-1` CONFIRMED
   (§4's prediction) and check whether the OTHER 17 evaluable clauses in
   that file, authored before F27's fix, still resolve to the same
   records this ledger's dedup expects.
2. A `testees/tre/CLAUDE.md` addendum recording the `high-byte-run` gap
   as CONFIRMED (not merely observed once) is still owed (LEDGER-1 §7
   ask 2, unchanged by this window — no bench-side doc edit was made by
   this read-only lane).
3. KB-23 is still OPEN: the next window script change or manual
   `run_window.sh` invocation should either land the ruling on sentinel
   shape or continue the standing workaround (read per-cell rc lines,
   never the sentinel alone).
4. If a THIRD sample of this three-engine roster is ever taken, extend
   §1's table rather than re-deriving it — the byte-identical shape
   across two samples makes a third mainly a confirmation of stability
   over time, not a new mechanism question.

---

## Source header (D35 style)

This file is a READING of one committed report group plus the prior
ledger, the prior report group, one lane report, one known-issue entry,
and three files under `testees/onig/` — never a measurement. Sources:
`reports/2026-09-19-capability-0.1-budu-ryzen1600-ext-second-cf0962e3.{md,
tsv,subject-grain.md,subject-grain.tsv,matrix.tsv,interpretation.md}`
(sha256 stamps in the sidecar's own header),
`reports/2026-09-18-capability-0.1-budu-ryzen1600-ext-first-cf0962e3.tsv`,
`store/index.tsv`,
`build/windows/window_capability_ext2_20260919T032134Z.log`,
`docs/dev/lanes/b54extwindow_report.md`, `docs/dev/known_issues.md`
(KB-23), `docs/dev/ledgers/2026-09-18-capability-window-cf0962e3.md`
(LEDGER-1, §5.4/§8 items 2-3), `docs/dev/predictions/
capability-0.1-ext-roster.tsv`, `docs/dev/wake.md` (the F27 standing
fact, READ item 3, work-queue items 2-3), `docs/design/
predicate_audit_v1.md` v1.1 §7, `testees/onig/driver.c` (lines 50-76),
`testees/onig/adapter.py` (lines 95-122), `testees/onig/CLAUDE.md` (the
`gave-up` section). No store file, report, or code was modified by this
lane; no network fetch was made.
