# DRAFT — O-65 (for the manager; not written to outbox_to_pcrec.md)

> ## O-65 (2026-09-28, pcrec-bench manager) — O-64's owed roster fix: the capability twin re-measured, all eight FLAT cells now readable
>
> **Context**: O-64 (2026-09-27/28's [OPT-LITSCAN] S2a window) found that
> our `bench/capability` set's `ext bench` roster omitted
> `pcrec-auto-nolitrun`, so 27 of 64 patterns were skipped on the deny arm
> and 7 of your item 2's 8 named FLAT cells could not be read same-window.
> That is fixed now.
>
> **What changed here**: `bench/capability/patterns.rxt`'s roster gained
> `pcrec-auto-nolitrun` (mirroring `pcrec-auto`'s own feature tokens), and
> the one cell was re-measured — 2/2 `measured` at attempt 1, `agree`,
> window 2026-09-28 04:10-05:21 EDT. `pcrec-auto-nolitrun` now attempts
> all 64 patterns on both arms (was 37). Both arms compile-refuse
> identically: `negation-scope-lookbehind-var` is
> `unsupported-by-declaration` on both (a pre-existing, shared
> limitation, not a roster gap), and `wild-datetime-datefinder-alternation`
> behaves exactly as O-64's item 9 already reported (its plain form
> refused on both arms; its whole-subject VM form compiles under `auto`
> only) — the fix changed nothing about that finding.
>
> **Where it is**: report
> `reports/2026-09-28-capability-0.1-budu-ryzen1600-litrun2-a32bc86e.*`
> (the same query as O-64's `-litrun` twin, restricted to the new pair by
> the reporter's own newest-wins dedup), ADDENDUM section of
> `docs/dev/ledgers/2026-09-28-b108-a32bc86e.md`.
>
> 1. **All eight of your item 2 (FLAT) cells are now scoreable
>    same-window: 7 of 8 confirmed.**
>
>    | cell | ratio (auto ÷ auto-nolitrun, throughput) | verdict (band 0.85-1.05) |
>    |---|---|---|
>    | email-local-nodup | 1.0236 | confirmed |
>    | tag-pair-match | 0.9998 | confirmed |
>    | nested-comment-rec | 1.0029 | confirmed |
>    | logparse-atomic | 0.9708 | confirmed |
>    | logparse-atomic-removed | 1.1174 | **refuted** (outside 1.05) |
>    | tag-depth3-bound | 1.0019 | confirmed |
>    | quotedstring-grok | 0.9283 | confirmed |
>    | syslogbase-expanded | 1.0004 | confirmed |
>
>    `logparse-atomic-removed` is the one clause O-64 already scored
>    (refuted, 1.107) — this fix supplied the other seven for the first
>    time; its own verdict is unchanged.
>
> 2. **Does the new pair reproduce O-64's readings? Yes, on 5 of 6 already-scored cells, with one threshold-straddle:**
>
>    | cell | O-64 (first window) | this window | agree? |
>    |---|---|---|---|
>    | username-password-pair | 1.001 | 1.0010 | yes, exact |
>    | aws-access-key-id | 1.037 | 1.0361 | yes, exact |
>    | github-pat | 1.001 (refuted, `lte 1.0`) | 0.9997 (confirmed) | both null-band (±0.03%); the verdict flips only because the ratio crosses the exact 1.0 line, not a real change |
>    | slack-webhook-url | 1.001 | 1.0009 | yes, exact |
>    | logparse-atomic-removed | 1.107 (thr) / 1.082 (srch) | 1.1174 (thr) / 1.0833 (srch) | yes, within a point |
>    | router-prefix-order (DFA null control) | 1.000 | 1.0003 | yes, exact |
>
> 3. **One real finding: O-64's cross-pin stand-in for `logparse-atomic` did not hold up.** O-64 (§3.4/§8) used a weaker cross-pin
>    (02902356→a32bc86e) reading of the 7 then-unscoreable cells, and
>    read `logparse-atomic` at +6.74% throughput / +3.37% search there,
>    calling it "the same shape as its `-removed` sibling" (which reads
>    +11.7%/+8.3% at the pinned tier). **The true same-window twin reads
>    `logparse-atomic` throughput at −2.9% (0.9708, inside the confirmed
>    band) — the OPPOSITE direction from its `-removed` sibling's
>    +11.7%.** The two patterns move together on short-subject-search
>    (`logparse-atomic` +3.20%, `-removed` +8.33% — same sign, smaller
>    size) but not on throughput. This is a case of O-64's own §5.4
>    caveat firing for real: the cross-pin AFTER's ±7-17% band can and
>    did land on the wrong side of null for one cell.
>
>    Six of the other seven cross-pin stand-ins (all effectively null)
>    do agree with this window's true readings.
>
> `make check-interpret`: 232 passed, 0 FAILED (was 231; +1 for this
> report group's sidecar).
