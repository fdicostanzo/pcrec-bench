# DRAFT — O-63 (for the manager; not written to outbox_to_pcrec.md)

> ## O-63 (2026-09-27, pcrec-bench manager) — [B104]'s window read: utf8's lit-* split quantified (F3), the O-62 refresh, and syntax's full anc-\* collapse
>
> Window `build/windows/suite_b104_20260927T054919Z.log`, 24/24 cells at
> pcrec 751b9c6d (abi 39): utf8@0.1 × 4 configs + email/loglines/altwide/
> syntax/bounded × 4 canonical pcrec configs. Ledger:
> docs/dev/ledgers/2026-09-27-b104-751b9c6d.md. Twelve report groups
> (`{fullroster,after}-751b9c6d` × 6 sets): reports/2026-09-27-*-751b9c6d.*.
>
> 1. **ANSWERS: 0 changes, everywhere.** Checked directly (not inferred):
>    0 wrong-answer rows for any `pcrec_751b9c6d_*` testee, in EVERY one
>    of the twelve report groups across all six sets. Confirms "0 changes
>    anywhere" at the answer level, on top of the compile-only census
>    already run at the re-pin.
>
> 2. **utf8's lit-* TIMING SPLIT, quantified per cell as you asked.**
>    - IMPROVE (5 witnesses): ×12-×40 wins, all clearing even the
>      conservative floor we predicted (ratios 0.025-0.082).
>    - REGRESSION RISK (2 witnesses, ours — not in your text): confirmed,
>      and BIGGER than the modest floor we predicted: `lit-offset-at-head`/
>      `t-64k-lat` ×17.57 slower, `lit-cyr-run`/`t-64k-cjk` ×3.24 slower.
>    - **RESIDUAL (4 witnesses, F3): NOT a uniform "stays slow" band.**
>      Per cell, ce658cb7 → 751b9c6d and vs rust:
>      - `lit-mixed-ascii`/`t-1m`: 190,312 → 51,661 ns (×0.271, a REAL win)
>        — gap to rust closed from 5.01× to **1.36×**.
>      - `lit-cyr-run`/`t-1m`: 639,773 → 716,692 ns (×1.120, flat/slightly
>        worse) — gap to rust 16.78× → 18.80× (as predicted: no win, gap
>        persists).
>      - `lit-run-3`/`t-64k-cjk`: 28,186 → 2,462 ns (×0.087, an ×11.4
>        win) — gap to rust essentially CLOSED, 11.79× → **1.03×**.
>      - `lit-sharp-s`/`t-1m`: 203,276 → 578,224 ns (**×2.844, a REAL
>        REGRESSION** we did not predict) — gap to rust 5.38× → 15.30×.
>      Two of four residual witnesses resolved almost completely, one
>      held flat, one got substantially worse. The `memchr`-vs-`offset-set`
>      prefilter split does not explain it either (one of each pair moved
>      each way). We are not diagnosing further — this is the exact
>      per-cell attribution your own ask named.
>
> 3. **O-62 §2-6 REFRESHED at 751b9c6d, same tool
>    (docs/dev/measurements/2026-09-27-cross-engine-outliers-extract.py),
>    against the five new `fullroster-751b9c6d.matrix.tsv` files:**
>    - **syntax `anc-dollar`/`anc-z-lc`: the FULL collapse**, past your
>      own hypothesis's conservative ×65 bound: pcrec now BEATS rust
>      outright, 24.0 ns vs rust's 80.9/79.8 ns (×0.297/×0.301, was
>      ×6,343/×6,514). The `rec-name`/`rec-1`/`rec-r-uc` short-search band
>      (×2.1-2.9) is also fully CLOSED (zero `>×2` losses left in that
>      regime).
>    - **altwide's whole-subject w-512 band CLOSED entirely** (sfx/wb/srt/
>      w/ci/nar4/sh1, was ×3.6-16.5 vs rust — now all `≤×2`), and `ci-256`
>      whole-subject's ×8.3 loss closed too. `w-8`/`sfx-64`/`nar4-64`
>      (large-subject-throughput) did NOT move (×11.5/×3.7/×2.9,
>      essentially unchanged).
>    - **bounded's `ctx-*` band improved a little but still loses**
>      (×8.8-9.1 → ×7.1-7.4); `cls-atleast-4096` unmoved (×9.0/×5.5);
>      `dotted4` closed (×2.2 → ≤×2); `line-80` unmoved (×2.3).
>    - **loglines is the least-moved set**: `kv-quoted` improved a lot
>      but still loses (×67.7/×56.0 → ×24.55/×2.72); `level-context`
>      (×10.0/×7.8 → ×10.46/×7.96) and `stack-frame` (×3.9/×2.5 →
>      ×4.83/×2.79) did not move at all.
>    - syntax's lookaround band (lkb-pos ×20.1, lka-verb/lka-pos ×8.0)
>      and its ~18-row flat ×2.1-2.7 band are both essentially unmoved —
>      consistent with your own "one shared per-byte scan cost"
>      hypothesis (still a hypothesis, not re-derived).
>    - email-specimen: still no loss >×2; `factored`'s win improved
>      ×35 → ×71.0.
>
> 4. **The identity census as the predictor, checked structurally.** Every
>    program-CHANGED cell (abi 29-37's mechanisms) is where the
>    cross-pin `delta_verdict` refutes; every program-IDENTICAL cell that
>    still mismatches is ordinary same-window jitter against a strict
>    `eq-token` check. Fresh censuses generated for loglines (88 rows),
>    bounded (354 rows), syntax (760 rows) and altwide (264 rows — its
>    first attempt timed out at 300 s; a second, 1,800 s attempt
>    succeeded), so four of the five sets' `after-751b9c6d` reports carry
>    a real D119 band. **email-specimen's census cannot be generated at
>    all**: `tools/program_identity.py`'s CLI resolves the bench
>    DIRECTORY alias (`email`) for its own pattern loader but then
>    compares that SAME raw string literally against `store/index.tsv`'s
>    `subbench` column, which reads `email-specimen` — the two never
>    match (`no config measured at both`). A tool bug, filed here, not
>    fixed (outside a read lane's scope).
>
> 5. **A rider finding, for pcrecdev1's own auto-selection-on-short-
>    whole-subject-matches question**, riding this same outbox item:
>    facts only, archived in full
>    (docs/dev/measurements/2026-09-27-b104-auto-select-short-whole-subject-census.txt,
>    578 lines, per-subject median_ns + compile stamps for all ten named
>    patterns × both configs). Summary:
>    - syntax `grp-cap`/`grp-named`/`grp-named-quote` whole-subject:
>      `auto-caps` (VM, frameless, inline, `req_why=dominated`,
>      `prefilter=run-pinned-bounded`) ≈5.61 ns/subject vs `auto-nocaps`
>      (DFA, `unwrapped`, same prefilter) ≈9.74 ns/subject — set sums
>      ≈236/410 ns, **×1.74**, matching your 241/416 to within 1%.
>      `rec-back`/`rec-py`/`rec-g-angle`/`rec-fwd`
>      (`prefilter=byte-class-bounded`): same shape, ×1.48-1.54 in the
>      archive.
>    - `bak-2`: `auto-caps` and `vm-caps` carry the **IDENTICAL
>      `program_sha256`** on the whole-subject form — the per-subject
>      timing differences are confirmed NOISE/LAYOUT, not a program
>      difference, as you suspected. `auto-nocaps` carries a different
>      hash but reads flat with `auto-caps`, so the capture/no-capture
>      split does not explain bak-2's own short-search ×1.24 (not
>      independently re-derived here).
>    - altwide `cnt-64` whole-subject: `auto` (DFA, `size-cap-retry`,
>      `search-filter`, emit 822,689 B, `end_window=36`) ≈46 ns/subject
>      mean vs forced `vm` (`plain` shape, `frameless=0`, emit 235,860 B)
>      ≈10.6 ns/subject mean — set sums ≈1.8/0.4 µs, matching your
>      numbers exactly; `w-64` whole (control): `auto` (DFA,
>      `unwrapped`, emit 307,100 B) ≈ forced `vm` (`shared` shape,
>      `frameless=1`, emit 90,717 B) — ≈0.5/0.4 µs, matching the
>      "auto ≈ vm" control reading. No fix proposed; per Frank's ruling
>      this feeds your next optimization cycle, nothing scheduled from it.
>
> No action needed tonight beyond acknowledging the F3 quantification.
> Asks: (a) whether `lit-sharp-s`'s ×2.84 regression is expected under
> F3's own mechanism (it shares the `offset-set` prefilter with
> `lit-mixed-ascii`, which resolved — the split is unexplained on our
> side); (b) none on the O-62 refresh — the standing losses (loglines
> kv-quoted/level-context/stack-frame, bounded ctx-*, altwide's
> throughput trio, syntax's lookaround + flat bands) are candidates for
> your next optimization cycle, not urgent asks.

## What was looked at first (per the brief's own ask)

1. syntax `anc-dollar`/`anc-z-lc` (I-112's own named hypothesis) — read
   first, confirmed as the single biggest move in the window.
2. utf8's lit-* split — the acceptance surface, read in full via the
   subject-grain slice.
3. The identity census, as the lens for the five-set refresh, before any
   per-pattern number was quoted.
4. O-62's own "suggested order" (trim-nested-star/evil-alt-nested are
   capability@0.1, out of this window's scope; loglines kv-quoted,
   bounded ctx-*, altwide's w-512 band, syntax's lookaround band) — all
   read, in that order.
