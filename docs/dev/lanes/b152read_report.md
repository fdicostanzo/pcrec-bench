# b152read -- [B152] the READ of the window at pcrec d6c5e71a5 (abi 112) (lane report)

Branch `lane/b152read` (worktree `worktrees/b152read`), Sonnet, not pushed, not merged. Window 2026-11-24 01:50-07:50 EST (chain log `/var/tmp/pcrecbench/b152win/chain.log`, `CHAIN_DONE`; 17/17 cells measured, store commit 104f2e65; utf8 skipped by deadline).
Nothing was timed. Ledger `docs/dev/ledgers/2026-11-24-b152-d6c5e71a5.md` (the derivation; everything below is its summary). Scratch + logs `/var/tmp/pcrecbench/b152read/` (`gen_*.log` each ending `DONE rc=0`, `interp.log` ending `DONE`).
Renders ran `nice -n 19`, detached (`setsid nohup gnutimeout`), two at a time at most; no `make check*`. Analysis: `docs/dev/measurements/2026-11-24-b152read/` (`gen.py` renderer, `an.py` altwide/movers/sentinel, `interp.sh`, `out/*`).

## Headline findings

1. **Window usable, never quiet**: every cell started at load1 1.1-2.8 and NOT QUIET; the target-core pre-flight refused 0-11 times per cell, then passed; 17/17 `measured`, trial agreement `agree` on every record; all five tonight's altwide records carry a failed AFTER sample (provenance).
2. **I-176 (1)**: against the capturing class, pcrec-auto is best on 31/34 short cells and ties/wins 16/34 large cells; behind RE2 by x1.04-x2.04 on 14 large cells beyond noise (13 RE2, 1 pcre2-jit); no short or whole-subject loss to another engine. Pooled with the non-capturing class (vectorscan SOM, rust) the large gap is x6.9-x29.3 (w-8 worst).
3. **I-176 (2)**: forced VM (flag on unchanged patterns, not the wrapped variant) is x2.1-x5.2 slower than auto on the `w-N` large ladder, x1.4-x2.8 short, ~equal on whole-subject; it compiles to w-1024 (x39 faster than pcre2-jit there) where auto refuses. `ci-256` forced VM is x482 slower than auto (860 ns/B, interp-class), unchanged since 6b2dbd3e.
4. **Wrong answers**: none in altwide. Re-baseline sets carry the same 2 wrong subjects (`asr-k-uc` x `f-kv`, `rec-r-uc` x `f-parens`, whole-subject) and FRAMES give-ups as at cb32eda28. 30 altwide `did-not-compile` rows, all size-cap/limit.
5. **109 beyond-bar movers, all on program-CHANGED rows, all attributed by census** (chained b147/b149/b152 censuses for the four 9ae59f5d4 sets). Big wins: hex32 -76..-81 %, float-literal-bound -86 %, syslogbase -93 %, `lit-l*` -31..-67 %; regressions: `dig-exact-8` +34 % / +75 % (b149 abi 92 cover, not this pin range), syntax whole-subject sub-200 ns cluster +13..+17 % (five cells), `cls-range` +18.6 %, slack-webhook large +15.3 %.
6. **Cross-window offset is not zero on program-identical cells**: median +4.4 % syntax short, +6.95 % bounded large (p95 +11.8 / +15.9 %), ~0 on capability; sentinel (short only) x1.00-x1.02. Loglines has no null band at all, so its +3..+8 % regress cells are not distinguishable from offset.
7. The b149 cover scan rewrote the `floor` pattern on loglines/email/litrun (-41/-44/-49 % large): floor is not constant across pins in those sets.

## Charter-vs-committed checklist (session_discipline.md 7(c))

| brief item | status |
|---|---|
| BOILERPLATE read first; worktree `lane/b152read`; toplevel printed; explicit-path commits; no push/merge; no timing; detached renders, <=2 at once, `nice -n 19` | done |
| 1(a) altwide@0.3 full roster group, pcre2 jit/interp reused with timestamps stated | `reports/2026-11-24-altwide-0.3-ryzen7700x-fullroster-d6c5e71a5.{tsv,md,matrix.tsv,subject-grain.md,subject-grain.tsv,interpretation.md}`; reuse + timestamps in ledger section 2 (jit 2026-10-19T06:49:21Z, interp 07:50:39Z); NOT stated inside the report header (the reporter has no field for it; a render cannot carry it) |
| 1(b) six cross-pin groups, cross-window said | `reports/2026-11-24-{capability-0.4,syntax-0.2,bounded-0.3,loglines-0.1,email-specimen-0.2,litrun-0.1}-ryzen7700x-d6c5e71a5.*` (same six files each); previous pin cb32eda28 for capability and syntax, **9ae59f5d4 for bounded/loglines/email/litrun** (no cb32eda28 record exists; newest pcrec-auto by pin order); ledger section 7 |
| 1(c) sentinel group | `reports/2026-11-24-sentinel-0.1-ryzen7700x-d6c5e71a5.{tsv,md,matrix.tsv,interpretation.md}` (`--all-records`, 6 records) |
| sidecars | 8 via the skill recipe, repo-relative paths, `--subject-grain` where it exists, determinism `cmp` CMP_OK x8; **no predictions file passed**: those matching set@version score earlier pins (litrun-0.1-first, loglines/email/bounded older pins) |
| 2 ledger with I-176 (1)(2)(3), non-measured outcomes, movers attributed, "not read" | `docs/dev/ledgers/2026-11-24-b152-d6c5e71a5.md` sections 3, 4, 5, 6, 7, 9 |
| 3 outbox DRAFT in report, outbox file untouched | below; `docs/dev/outbox_to_pcrec.md` NOT edited |
| 4 this report + checklist | here |
| CLAUDE.md rows (reports, ledgers, measurements, lanes) | done |
| `make check-interpret` | NOT run; stale-sidecar status of the 117+ older sidecars is the manager's [B41] regeneration; this lane's eight are stamped against the live index at this branch point |
| OWED (manager) | merge; [B41] sidecar regen; trend/frontpage/viewer for the d6c5e71a5 records (not run); `make check` without taskset (owed per plan); a nocaps/`-fno-landmark-walk`/vm arm window for the six re-baseline sets; utf8 at d6c5e71a5; a large-regime sentinel |

## O-n DRAFT (for the manager; NOT written to the outbox)

> ## O-nnn (2026-11-24, bench manager) -- the window at d6c5e71a5 (abi 112): altwide full roster, the named losses, the re-baseline
>
> Window b152win, 2026-11-24 01:50-07:50 EST, `ryzen7700x`. 17 of 17 cells measured, all `agree`; utf8 skipped by deadline.
> The box was never quiet (load1 1.1-2.8); the target core passed the pre-flight at every cell. Ledger `docs/dev/ledgers/2026-11-24-b152-d6c5e71a5.md`.
>
> **Verdict.** No wrong answer in altwide. The re-baseline movers are all on rows whose program changed,
> and every one matches your census. The census held on our side: 936 identical, 575 changed, 0 unattributed.
> `wild-datetime-datefinder-alternation` now compiles (it was 591,151 B code at cb32eda28).
>
> **I-176, one: ratio to the best engine.** Against capturing engines, pcrec-auto is best on 31 of 34 short cells
> and ties or wins 16 of 34 large cells. No loss to another engine on short or whole-subject cells.
> Against the non-capturing class (vectorscan, rust), the large gap is x6.9 to x29.3.
> The worst is `w-8` at x29.3. We list it pooled, not as a ranking.
>
> **I-176, two: forced VM.** This is `--engine=vm` on the same patterns. It is not the wrapped variant.
> Forced VM is x2.1 to x5.2 slower than auto on the `w-N` large ladder. It reaches `w-1024` where auto refuses.
> There it is x39 faster than the JIT. `ci-256` forced VM is x482 slower than auto (860 ns/B).
> That cell was the same at 6b2dbd3e (+4.6 %, within spread).
>
> **I-176, three: named losses of pcrec-auto** (behind another capturing engine, beyond noise, large throughput):
> `cnt-64` x2.04, `wb-512` x2.02, `clsd-64` x1.96, `w-64` x1.96, `clsa-64` x1.93, `w-96` x1.69, `wb-256` x1.68,
> `w-128` x1.54, `w-8` x1.25, `srt-256` x1.25, `w-192` x1.17, `srt-512` x1.13 (all to RE2), `pfx3-256` x1.09 (to pcre2-jit).
> RE2 beats pcrec's flat 1.8 ns/B scan on these shapes. From `w-256` up, auto is the best capturing engine.
> Forced-VM losses: 47 of 70 cells, led by `cnt-64` x7.4, `clsd-64` x7.1, `clsa-64` x6.9, `w-96` x6.7.
> Full lists are in the ledger, section 5.
>
> **Refusal walls.** Auto refuses at `w-1024`, `clsa/clsd-1024` and `w-2048` (C source over 1,000,000 B).
> The VM refuses at `ci-512`, `w-2048`, `s-2048`, `s-4096` (code over 500,000 B).
>
> **Re-baseline.** 109 cells moved beyond the reporter's bar, all on changed programs.
> Wins: `hex32` -76 to -81 %, `float-literal-bound` -86 %, `lit-l*` -31 to -67 %.
> Regressions to look at: `dig-exact-8` +34 % large and +75 % short (abi 92 cover),
> five syntax whole-subject cells at +13 to +17 % (`grp-cap`, `grp-named`, `grp-named-quote`, `qnt-poss-plus`, `rec-fwd`),
> `cls-range` large +18.6 %, `wild-secrets-slack-webhook-url` large +15.3 %.
> The cross-window null is +4 to +7 % on some strata (syntax short, bounded large), so small moves there are offset.
>
> **Two non-timing re-pin findings from the prep.**
> 1. The landmark walk adds +44.3 KB of emit on `wild-secrets-username-password-pair` nocaps plain
>    (564,961 B with `-fno-landmark-walk`, 609,262 B default). We did not time that arm tonight. Is the size intended?
> 2. `char-step` (the character-stepped DFA for UCP `\b` under `-e utf8`) has no `locate` axis row.
>    Please list it, or say why it is absent.
>
> **Ours.** The pcre2 altwide cells are from 2026-10-19 (libpcre2 10.46 unchanged). The short sentinel bounds that offset at x1.005 to x1.03.
> We have no large-regime sentinel. Loglines has no program-identical cell, so it has no null band.
