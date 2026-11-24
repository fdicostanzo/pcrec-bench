# lane b152fix report: the make-check reds at d6c5e71a5 (abi 112)

Source: /var/tmp/pcrecbench/b152chk/make_check.log (2026-11-24 08:11-08:40). None of the reds is a pcrec fault.
No check was loosened or deleted; none retired.

## Checklist (charter vs committed)

| # | item | state | commit |
|---|------|-------|--------|
| 1 | subject-timeout control | DONE | tools/selfcheck.py (check_subject_timeout) |
| 2 | four `noreqbyte:` rows | DONE | tools/selfcheck.py (check_noreqbyte_testee) |
| 3 | identity chooser abc | DONE (bound at cb32eda28's build) | tools/selfcheck.py (check_identity_chooser) |
| 4 | KB-16 test, `opened` empty | DONE (test's target choice) | pcrecbench/tests/test_report.py |
| 5 | quick-cell `inconclusive-load` | NOTED, left (known load-sensitive arm; box was busy) | - |
| 6 | stale sidecars | DONE, 131 sidecars, 0 failures | reports/*.interpretation.md |

## 1. subject-timeout
Why `b`+40`a` no longer hangs: `(a+)+b` stamps `RX_REQ_RUN "6162@1"` (the run "ab"), and the run pre-check
(abi 104-112; `RX_REQ_WHY emitted`) dismisses a subject with no "ab" substring in one scan -> `nomatch`.
(Before: [B74] abi 29's `RX_REQ_BYTE "98"` memchr, which `b`+a^40 defeated by holding a 'b'.) A subject holding
"ab" cannot fail `(a+)+b`, so the PATTERN changed: `(a+)+$` over `a`x40 + `b`. Stamps (measured): `RX_REQ_BYTE "97"`,
`RX_REQ_RUN "none"`, `RX_END_WINDOW "none"`, forced VM, no step budget -- nothing to deny, no shared source.
`s-fine` continuation arm kept; its subject changed `ab` -> `aa` because `(a+)+$` must match it at once ([0,2)).
Proven: `s-hang -> timed-out, by name` and `s-fine answered [0,2)` (2 checks, slice run).

## 2. noreqbyte rows (measured, each with its abi step)
- `foo[0-9]+bar`: req_run `626172@0` -> `[30-39]626172` (abi 104 class respelling); req_why `emitted` -> `dominated` (abi 106).
- github-pat: req_run `6875625f7061745f@7` -> `6769746875625f7061745f` + 21 x `[30-3941-5a5f61-7a]` `@10` (abi 104).
- uuid-grok: req_run `none` -> 8 x `[30-3941-4661-66]`, `2d`, 4, `2d`, 4, `2d`, 4, `2d`, 8 `@23` (abi 104);
  req_why `dominated` -> `emitted` (abi 106).
- Program identity arm: uuid-grok's two programs are no longer IDENTICAL (2a0f1822.. vs 2278d575..) -- its req_why is
  `emitted`, so the denial removes a pre-check. The NULL arm (denial removes nothing) moved to `foo[0-9]+bar`, req_why
  `dominated`, program f54a3d40.. identical on both arms; uuid-grok and github-pat (33833777.. vs c5c4c49d..) both differ.
  The control is preserved, with a new witness. Slice: 6 passed, 0 failed.

## 3. identity chooser abc
Bound at cb32eda28's own build (`_b152_hist_bin`), the way b152prep bound the other historical checks; the claim
(v2 changed / v3 identical vs 6b2dbd3e) concerns the v2-vs-v3 normalisation over abi <= 93, and at d6c5e71a5 both
hashes read `changed` (measured, log). Re-aiming to "changed/changed" would have retired the control. The adapter-row
arm stays at the canonical pin. Slice check_identity_chooser: 13 passed, 0 failed.

## 4. KB-16
Cause: the test picks the subbench with the fewest records, but queries `--machine budu-ryzen1600`. The fewest is now
`unusual` (11 records, 2026-11-02), all on `ryzen7700x`, so the query matched 0 records and opened nothing. Reporter
fine. Fix: choose the target among subbenches with records on the query's machine; `other_paths` stays all machines.
Test now passes.

## 5. Left as is
`a real quick cell on bench/email writes a MEASURED scratch record` read `inconclusive-load` (busy box).

## 6. Sidecars
`scripts/regen_sidecars.py`: 131 sidecars, 0 failures (many stale since the window's records landed). `make check-interpret`:
305 passed, 0 FAILED.

## Validation
- check_subject_timeout 2/2; check_noreqbyte_testee 6/6; check_identity_chooser 13/13; KB-16 test ok; check-interpret 305/0.
- `make check-report`: launched detached, log /var/tmp/pcrecbench/b152fix/check_report.log, completion line `DONE rc=N`.
  OWED to the manager if not complete (see the log).
- The whole `make check` is the manager's (queued after merge).
