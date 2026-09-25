# Lane b77u1 — [B77] U1, the HARNESS half of the utf8 set

Branch `lane/b77u1` (off master 3a00884). Charter:
`docs/design/utf8_set_v1.md` v0.2 §8 (the oracle), §13 (U1's row + the
byte-identical acceptance check), §14 Q9 (the option word is a PARAMETER
of the shared `oracle_pcre2.py`), §15 R1; plan row [B77]; inbox I-90/I-94.
Not touched: `store/`, inbox, outbox, `plan.md`, `bench/utf8/` (U3's lane),
the configs/roster (U2), patterns (U4), expectations/NOTES (U5), ~/pcrec.

## Charter vs committed

| # | U1 promise (§13 row / brief) | committed | where |
|---|---|---|---|
| 0 | FIRST DELIVERABLE: every existing `bench/*/expectations.tsv` re-derives BYTE-IDENTICALLY under the changed oracle with no UTF option requested, with a negative arm; committed (outputs + method) BEFORE the driver work | **DONE, commit 2aeb5c3** (before the driver commit fb285b5). 6/6 sets byte-identical — email 501, loglines 1364, bounded 4300, altwide 2772, syntax 8265, capability 4990 rows (22,192) — each through the set's OWN `gen_expectations.py`. P0 measures "no UTF option requested" (every pattern's word 0, every sidecar `encoding = byte`); N1: a one-byte-mutated copy compares UNEQUAL on all six; N2: a sabotaged word (PCRE2_ANCHORED) moves all six. Repeated independently by an earlier run (also 6/6). No set re-derived differently, so no STOP | `docs/dev/measurements/probe_b77u1_rederive.py`, `docs/dev/measurements/2026-09-25-b77u1-byte-identical-rederivation.txt` |
| 1 | the per-pattern oracle option word in `oracle_pcre2.py` | DONE: `option_word(utf=, ucp=)`, `PCRE2_UTF`/`PCRE2_UCP`/`PCRE2_ERROR_BADUTFOFFSET` (measured on this box's 10.46 in the module's `__main__` self-check), `Compiled.options`. Decided per pattern in ONE place: `expectations.oracle_option_word(sb, pattern)` — UTF iff the sidecar declares `[expectations] encoding = "utf8"` (new key, `subbench.SET_ENCODINGS = ("byte", "utf8")`, anything else refused by name), UCP iff the pattern declares `requires-unicode-class-scope`. `PCRE2_NO_UTF_CHECK` never passed (§8.2) | `pcrecbench/oracle_pcre2.py`, `pcrecbench/expectations.py`, `pcrecbench/subbench.py` |
| 2 | the character-boundary find-all advance in the ORACLE, active only under UTF | DONE: `oracle_pcre2.next_start()` = pcrec match_api.md §3.1.1's NORMATIVE utf8 rule (from `pos+1` skip 0x80-0xBF, stop at `n`); `find_all` uses it iff the compiled word has PCRE2_UTF, else `start + 1` exactly | `pcrecbench/oracle_pcre2.py` |
| 3 | the advance in EVERY driver, active only when UTF is requested | DONE: new driver-protocol flag `--utf8` (documented in `pcrecbench/adapters.py`'s protocol header). `harness.run_cell` sets `handle["utf8_advance"]` iff `expectations.utf8_advance(sb, p)` (only when true — byte sets' handles/argv unchanged); every adapter forwards `--utf8`. Implemented in pcre2, pcrec, re2, onig, tre, rust; vectorscan ACCEPTS it inertly (no find-all loop at boolean grain — `NMATCHES` is always `-` there). Drivers rebuilt via their own build paths under the worktree's `build/` | `testees/*/driver.*`, `testees/rust/src/main.rs`, `testees/*/adapter.py`, `pcrecbench/harness.py` |
| 4 | the `make check-harness` arm with its NEGATIVE case (a byte-stepping advance must FAIL) | DONE: `check_utf8_find_all_advance`, 24 checks, all PASS standalone: oracle 12 (byte) / 6 (UTF); NEGATIVE byte-stepping under UTF raises -36; every driver 6 with `--utf8`; NEGATIVE 12 without on onig/pcre2/pcrec/re2/tre; pcre2 in its own UTF mode (`--utf`) 6 with `--utf8`, NEGATIVE cut short (n=2) without; the HARNESS wiring end to end (a synthetic `encoding = "utf8"` set through the real `run_cell`: `matched-as-expected`; NEGATIVE with the wiring sabotaged: `wrong-span-or-captures`, "expected 6 … observed 12") | `tools/selfcheck.py` |
| 5 | the three REQUIRES tokens in `pcrecbench/capability.py` | DONE: `utf8-encoding`, `ascii-class-scope`, `unicode-class-scope` (vocabulary 17 → 20, GLOBAL per Q3/I-94) | `pcrecbench/capability.py` |
| 6 | full `make check` at the end (shared harness code changed), after a go from main | **see "Validation" below** | — |
| 7 | this report; CLAUDE.mds updated | DONE: `pcrecbench/`, `tools/`, `docs/dev/measurements/`, all seven `testees/*/`, root (the check-harness clause) | — |

## Design decisions a reviewer should check

1. **The advance is keyed on the SET's oracle word, not on a config's
   engine encoding.** One fact (`expectations.utf8_advance`) drives both
   the oracle and every driver, so they cannot be told two different
   things. The deciding measurement: `rust-default` — kept UNCHANGED as a
   config by §7.1 because it is already UTF-8-semantic — DOES report empty
   matches at mid-character offsets (byte-stepping count 12 on the witness,
   not 6). A config-keyed advance would have left it byte-stepping on the
   utf8 set and scored it wrong for a harness reason.
2. **`--utf8` moves the advance only, never an engine's encoding.** Engine
   encodings stay config choices (U2). The one exception is the pcre2
   driver, which ALSO gained `--utf`/`--ucp` (PCRE2_UTF/PCRE2_UCP in
   `pcre2_compile_8`'s word, `info utf/ucp on` printed only when set) —
   the driver's half of the oracle word, needed so the check can witness a
   real UTF-mode engine rejecting a byte-stepping advance. No config passes
   them; the `pcre2-utf-*` configs + `adapter.py` keys are U2's (§7.1 lists
   the driver flags under pcre2's adapter change — U2 now inherits them
   built).
3. **The option word does NOT carry multiline**: every set spells it
   inline (`(?m)`), including §5's `asr-caret-ml`/`asr-dollar-ml`.
4. `bench/email/gen_expectations.py` keeps its own pre-shared-module
   `derive()` (it calls `oracle.compile(text)` with the default word 0);
   left untouched — email is a byte set and re-derives identically.

## Findings (for U2/U5 and the manager)

- **UTF-mode derivation cost.** Informational arm I1 (PCRE2_UTF forced on
  BYTE sets — not the utf8 set's configuration): over email's 1 MB
  subjects the derivation takes ~39 s vs 1.2 s in byte mode. PCRE2
  validates the subject from the start offset on every `pcre2_match` call
  and §8.2 forbids `PCRE2_NO_UTF_CHECK`, so find-all over a large subject
  with many matches is O(n × matches) in validation. U5's
  `gen_expectations` over the 1 MB utf8 sweep will pay it; worth sizing
  before U5 plans its runtime.
- **A mid-loop negative rc silently truncates a find-all count** in every
  driver (pre-existing shape: `if (rc < 0) { if (count == 0) rc_final =
  rc; break; }`). Under `--utf` without `--utf8` the pcre2 driver reports
  `match, n=2` rather than an error — caught by the expectation (a wrong
  count), but a give-up after the first match (e.g. a match limit mid
  subject) is likewise reported as a short count, not a give-up. Not
  changed here (out of U1's scope, and it would move byte-set behavior);
  flagged as a candidate KB.
- `PCRE2_CASELESS` is NOT a usable sabotage control for "the derivation
  reads the word": loglines re-derives identically under it. Recorded in
  the archive; PCRE2_ANCHORED used instead.

## Validation

- Byte-identical re-derivation: 6/6 (above), archived.
- `check_utf8_find_all_advance` standalone: **24/24 PASS**.
- Neighbouring arms standalone (`check_driver_smokes`,
  `check_kb17_find_all_advance`, `check_high_byte_pattern_argv`): 20/20
  PASS.
- `python3 pcrecbench/oracle_pcre2.py` self-check: OK (incl. the new
  option-word/UTF-advance block).
- Full `make check`: see the handback (run after main's go; the log is
  `/var/tmp/b77u1-makecheck/make_check.log`, completion line
  `DONE rc=<n>`).


---

**VALIDATION — the full `make check` (manager-launched at the lane's
request, 2026-09-25 14:33 EDT, worktree at 50e30d8, log
/var/tmp/b77u1-makecheck/make_check.log): `DONE rc=0`** — check-harness
482 passed / 0 FAILED (458 + this lane's 24), check-report 97+7+12
OK, check-interpret 199/0.
