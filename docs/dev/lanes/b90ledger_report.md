# lane b90ledger report — [B90]'s READING: I-108's K64-fix acceptance at ce658cb7

**Task**: read the [B90] acceptance window (capability@0.1 × pcrec-vm /
vm-in / auto / nocaps at ce658cb7, committed 438ba8d) against BEFORE = the
6ef76820 records; the identity census, the cross-pin report group + its
sidecar, the ledger scoring I-108's P1-P4, and a draft O-57. No measurement,
no `store/` write, no reporter change, no ~/pcrec write.

**Branch**: `lane/b90ledger` (harness worktree
`.claude/worktrees/agent-a0cc3ab002d6aeffc`), four commits:
`3c5ce5d` (census), `e0f9529` (ledger + ledgers CLAUDE.md), `8302acb`
(report group + sidecar + reports CLAUDE.md), and this report.

## 0. Headline

- **P1 CONFIRMED** — 50/50 rows `matched-as-expected` (5 subjects × 5
  trials × vm-caps/vm-in-caps; BEFORE 50/50 `gave-up -2:PCREC_ERR_STEPS`);
  all 5 are oracle `nomatch`, and libpcre2 jit/interp's own records agree;
  per-subject 10.13-11.41 ns (b1885a83 10.72-12.14); the set cell is
  ranked again: 825.05 / 892.62 ns (b1885a83 −1.20% / −0.44%).
- **P2 CONFIRMED** — the six forced-VM throughput cells read
  23,087.4-23,171.4 ns, −0.48% to +0.12% vs the b1885a83 records
  (`…_vm-caps-simdna__…20260923T125206Z`, `…_vm-in-caps-simdna__…20260923T133317Z`);
  2/6 inside b1885a83's own IQR (0.02-0.20%), all six within ±0.5%;
  vs 6ef76820 ×3.18-×837.09 slower (the accepted cost; D119 reads all
  six `regress`).
- **P3 CONFIRMED as amended** — auto-caps 112/12/4, auto-nocaps 113/12/3;
  the 24 changed auto rows are exactly the six backreference patterns ×
  2 forms × 2 configs; `RX_REQ_WHY` moves on no auto artifact; their 24
  timing cells: 22 within, 2 improve (`phone-palindrome-6` srch, −6.15% /
  −11.81%, the set's habitually noisiest group).
- **P4 CONFIRMED on programs; on timing only in the bar's self-referential
  sense** — no artifact outside the predicted 24 K64 + 48 backreference
  rows changed; the 422 program-identical cells cannot exceed the band
  they define. Out-of-sample: 9 identical cells exceed the PREVIOUS pair's
  band, two strata shifted as a whole (thr <100ns median +5.73%, 50/57
  slower; srch 100ns-1us median −1.92%, 94/101 faster), and bands widened
  (thr ≥1us ±8.18 → ±16.62%; thr <100ns ±29.68 → ±42.16%). Also: the 8
  forced-VM search cells [B84] saw regress improve beyond the bar back to
  b1885a83 (−3.10..+1.63% vs b1885a83) — cells of the predicted movers
  that I-108's text did not name.
- **Census = prediction exactly**: 512 rows, 425 / 72 / 15, per config
  identical to b90repin §3. Nothing to explain.
- **[B88] cross-check is ONE-SIDED at this pair**: the ce658cb7 records'
  `program_sha256` == census `new_sha256` on 497/497 compiled rows, but the
  6ef76820 records carry no field (schema 1.6), so the reporter's
  field-first identity did NOT fire on any cell — every cell read the
  census. The brief's premise ("the first pair carrying both") does not
  hold; the first two-sided pair is the next one. The report's identity
  bullet ("the records carry no program hash of their own") is now true of
  one side only — a wording item for a future reporter change, not made
  here.

## 1. Charter-vs-committed checklist

| # | brief item | status | where |
|---|---|---|---|
| 1 | identity census (v2), commit under reports/identity/, compare to 512 = 425/72/15 | DONE — exact match per config; `--check` re-derives byte-identical | `3c5ce5d`: `reports/identity/capability@0.1/pcrec_6ef76820__ce658cb7.tsv`; ledger §0.3 |
| 2a | cross-pin report(s) in the after-6ef76820 form/grouping (invocation found in `genb84.sh`, journal 2026-09-23 18:5x) | DONE — md, tsv, matrix.tsv, matrix.html, subject-grain md/tsv; reporter v23 | `8302acb`: `reports/2026-09-25-capability-0.1-budu-ryzen1600-after-ce658cb7.*` |
| 2b | class-pure views, null band (field first, census fallback; field-vs-census agreement stated), I-101 query | DONE — the views and query are in the group; field-first did not fire (one-sided field), agreement 497/497 on the AFTER side stated | ledger §0.4, §2, §3 |
| 2c | interpretation sidecar via /pcrec-bench-interpret | DONE — `--subject-grain` passed, no predictions file (none matches the pair; the after-6ef76820 precedent), DETERMINISM-OK; 16 rules fired | `8302acb` |
| 3 | ledger scoring P1-P4 cell by cell, CONFIRMED/REFUTED/PARTIAL with numbers + spread, population + blindness per verdict | DONE | `e0f9529`: `docs/dev/ledgers/2026-09-25-k64-fix-after-ce658cb7.md` |
| 4 | O-57 draft | DONE, §3 below (not written to the outbox) | this file |
| 5 | ledgers CLAUDE.md, reports CLAUDE.md current | DONE — ledgers: rows for this ledger AND the missing 2026-09-23 precheck-admit ledger; reports: the census line + the group paragraph | `3c5ce5d`, `e0f9529`, `8302acb` |
| 6 | `make check-interpret` 199+/0 | DONE — **200 passed, 0 FAILED** (the new sidecar joins section 3: 33) | — |
| 7 | `make check-report` only if reporter code touched | NOT RUN — no reporter code touched | — |

## 2. Method notes

- Numbers come from a standalone extraction over the twelve named records
  (b1885a83 / 6ef76820 / ce658cb7 × 4 configs) importing `pcrecbench.reduce`
  and `pcrecbench.nullband`; cross-checked against all 492 `d119` rows of
  the rendered report (0 mismatches in Δ%, IQR%, verdict) and the six
  strata (n/min/median/max identical).
- Scripts live in the session scratchpad only (`b90extract.py`,
  `b90null.py`, `b90p1.py`, `b90pcre2.py`, `b90q*.py`, `genb90.sh`); not
  committed.
- The worktree had no `build/`; the two pinned binaries were symlinked in
  from the main tree's gitignored `build/pcrec-{6ef76820,ce658cb7}` (read
  only; nothing rebuilt).
- Box: compile-only census (~1 min) and the report render (~10 min,
  detached, single core); no other heavy job of this lane ran in parallel.

## 3. DRAFT outbox item — O-57

```
## O-57 (2026-09-25, pcrec-bench manager) — I-108 ACCEPTED: the K64 fix at ce658cb7 scored on capability@0.1

The [B90] window (capability@0.1 × vm-caps / vm-in-caps / auto-caps /
auto-nocaps at ce658cb7, 4/4 measured at attempt 1, store 234) read
against BEFORE = the 6ef76820 records. Ledger:
docs/dev/ledgers/2026-09-25-k64-fix-after-ce658cb7.md; report group
reports/2026-09-25-capability-0.1-budu-ryzen1600-after-ce658cb7.*.

P1 CONFIRMED. email-nested-plus / short-subject-search: the five
subjects (sd-empty-alt-hit, sd-empty-alt-miss, sec-github-pat,
v-uuid-badnibble, v-uuid-valid; all oracle nomatch) answer as pcre2 on
vm-caps and vm-in-caps — 50/50 rows matched-as-expected, 0 give-ups
(6ef76820: 50/50 PCREC_ERR_STEPS). Scored on answers + timing as agreed:
10.13-11.41 ns/call per subject (b1885a83: 10.72-12.14). The set cell is
ranked again at 825.05 / 892.62 ns (b1885a83: 835.06 / 896.54).

P2 CONFIRMED. The six forced-VM throughput cells
(email-nested-plus, wild-validator-email-owasp, winpath-near-miss ×
vm-caps/vm-in-caps) read 23,087-23,171 ns, within ±0.5% of b1885a83
(23,119-23,201 ns). Against 6ef76820 they are ×3.18 to ×837 slower, as
you stated. The same fix also returned the eight forced-VM SEARCH cells
that regressed at 6ef76820 (ipv4-near-miss, wild-datetime-moment-iso8601,
wild-validator-email-owasp, wild-validator-ipv4-owasp srch × vm/vm-in)
to b1885a83 (−3.1% to +1.6%): 10.6-43.4% faster than 6ef76820, past the
null band. winpath-near-miss srch vm-caps went the other way, +12.5% vs
6ef76820 (inside its ±12.7% band) and −2.6% vs b1885a83.

P3 CONFIRMED as you amended it. Our v2 census (512 artifact rows):
auto-caps 112 identical / 12 changed / 4 refused, auto-nocaps 113 / 12 /
3. The changed rows are exactly the six backreference patterns on every
config (doubled-word, dup-param-detect, phone-palindrome-6,
quoted-delim-match, tag-pair-match, tag-depth3-bound), which is the [VAR]
seam's rx_span_match against our abi-31 BEFORE. RX_REQ_WHY moves on no
auto artifact. On the auto configs, 22 of the 24 backreference timing
cells are within the bar. The other two are phone-palindrome-6 srch
(−6.2% / −11.8%, improve), our noisiest trial-agreement group.

P4 CONFIRMED on programs. No artifact changed outside the 24 K64 rows
and the 48 backreference rows. On timing it is confirmed only in the
bar's own sense: the program-identical cells are the band's population,
so they cannot exceed it. Stated plainly: at this pair the band widened
(throughput ≥1µs ±8.2% → ±16.6%, throughput <100ns ±29.7% → ±42.2%).
Two strata shifted as a whole (throughput <100ns median +5.7%, 50 of 57
slower; search 100ns-1µs median −1.9%, 94 of 101 faster). 9
program-identical cells exceed the previous pair's band, e.g.
wild-codegrammar-json-array-begin thr auto −16.6%, date-nested-plus thr
vm-caps +42.2%. "Program-identical" here means the same program in a
different binary: abi 32's rx_var/rx_ctx/rx_info growth (+1,001 B on
every artifact) and our shim's rx_ctx zeroing are outside the
normalization. We do not attribute the shift.

Bench side, for your information: [B88]'s program_sha256 is on every
ce658cb7 compile row and equals our census hash on 497/497 artifacts. The
6ef76820 records predate the field, so this pair's null band still came
from the census. The first pair that carries the field on both sides is
the next one.

No asks. K64 can close on our side.
```

## 4. OWED / not done

- Nothing owed by this lane. Not run (not needed): `make check-report`
  (no reporter code touched), full `make check`.
- Manager's: send O-57, the plan.md [B90] row / journal, merge.
- A reporter wording item (not a defect in numbers): the null-band
  identity bullet says "the records carry no program hash of their own"
  even when one side does. It is harmless at this pair. Someone should
  reword it before the first two-sided pair renders.
