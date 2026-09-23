# lane b74repin report — RE-PIN to 8d716693 (abi 27 -> 29), [OPTLOOP.1] batch 1

**Task**: plan row [B74] (a) / inbox I-87. Re-pin the pcrec testees from
`25b1984f` (abi 27) to pcrec main `8d716693` (abi 29) — the [OPTLOOP.1]
batch-1 pin (`OPT-ANCHOR-VM`, `OPT-ENDWIN`, `OPT-REQBYTE` as three new
axes). [B74] (b), the capability re-measurement window, is explicitly
OUT OF SCOPE for this lane per the brief.

**Branch**: `lane/b74repin`, `worktrees/b74repin`, five commits
(`6132618` the adapter/shim/driver/selfcheck/registry/catalogue change,
`f3bf61d` the CLAUDE.md updates, `da84364` this report's first cut,
`95c69c4` the subject-timeout control fix item 13 found, this report's
final cut next). **DELIVERED**: `make check` run to completion twice
(item 12/14) — `check-schema` 5/73/0, `check-harness` 456/0,
`check-report` OK, `check-interpret` 163/27 (all 27 the expected
sidecar-staleness class, named and classified in item 14); `make`'s own
exit is 2, entirely attributable to those 27.

## Predictions, stated before the build (boilerplate discipline)

From I-87's own text and the brief, before compiling anything:

1. abi 28→29 across the batch-1 merge `6ab2464e` + one landing commit;
   three new stamp lines in every artifact (`RX_REQ_BYTE`, `RX_VM_START`,
   `RX_END_WINDOW`); "nothing else in the prologue moved" (`struct
   rx_info` byte-identical, shim floor stays 16).
2. The brief itself flagged uncertainty: "check for any abi-28 movement
   we never absorbed too."
3. Size books: "the three new stamp lines should account for a flat
   per-artifact constant."

**Scored below**: (1) held for the *specific* three stamps, but the jump
is TWO abi steps, not one (see finding 1). (2) was right to ask —
finding 2 is exactly that movement, and it is much larger than "one more
abi step": a whole CLI reshape. (3) was WRONG for two of the three axes:
see finding 3, "the size books are not flat this time."

## Charter-vs-committed checklist

1. **Fetch + confirm the commit.** DONE. `git -C ~/pcrec fetch origin`
   confirmed `8d716693` on `origin/main` with `6ab2464e` as its ancestor
   (`batch 1 landing: recursion identity (B) re-pinned to 6ab2464e +
   reference-grammar probe (first post-D118 pin); ...`); `origin/main`'s
   tip is one commit further, `2ce98a7b` ("session close: wake.md
   rewritten; journal close entry (batch 1 merged, I-87 sent, gate on
   8d716693 detached") — a journal-only commit, not a move of the pin.
   No write to `~/pcrec` beyond the sanctioned `git fetch`.

2. **`pin.sh 8d716693`.** DONE. `build/pcrec-8d716693/build/pcrec`,
   `rx_info.abi` 29 confirmed on a plain `abc` witness.

3. **FINDING 1 — abi 28 movement never absorbed, and it is NOT just one
   more abi step.** Read directly off pcrec's own (read-only) git
   history: `25b1984f..8d716693` is **300 commits**, not the single
   merge I-87's text suggested. Two real abi steps:
   - **abi 27→28**: pcrec's REL-1.4 (`c26b5216`, "version plumbing:
     PCREC_VERSION, --version, abi 27->28 stamp"), merged as `579588da`
     ("(B) FILEPIN re-pinned to the merge a70982c9"). No `rx_info` field
     — confirmed by diffing `struct rx_info` field for field between the
     two pins' emitted `.h` (byte-identical). This project's own inbox
     already carried advance notice (I-82/I-83, 2026-09-21: "pcrec main
     has since moved further (abi 28, [REL-1.4], D115)... HELD UNPUSHED
     until O-43 lands").
   - **abi 28→29**: `b7f46d6b` + `6ab2464e` ([OPTLOOP.1] batch 1) —
     exactly I-87's own ask.

4. **FINDING 2 — a MAJOR, unscoped break: pcrec's whole REL-1 release
   milestone landed in the same range and reshaped the CLI (D118).**
   Between the two pins pcrec ran a full release-prep milestone
   (REL-1.1 through REL-1.11, `v0.1.0-beta` tagged at `fe1dbb7a`) that
   I-87's text never mentioned. The load-bearing piece for this project:
   **D118** (`docs/dev/decisions.md`, pcrec, read-only: "The CLI takes
   the gcc SHAPE: positional operands are INPUT FILES, the literal
   pattern moves behind `--pattern`... pcrec does NOT invoke gcc
   itself"), landed `f364d122`/REL-1.10 stages 1-4, gated at `735f199c`.
   MEASURED directly: the OLD invocation shape every adapter call in
   this project used —

       pcrec -p rx <flags> -o artifact.c -- 'PATTERN'

   — is now REFUSED outright:

       pcrec: PATTERN: not an existing file; a literal pattern is given with --pattern

   because a bare positional after `--` is now parsed as a candidate
   FILE operand, never a pattern. This is NOT the same finding as (3)'s
   abi movement — it is a CLI syntax break that would have made every
   single pcrec compile in this project fail (`make check`, every
   `pcrecbench run`, every `quick` cell) had it gone unnoticed. **This
   project had prior warning it did not yet act on**: inbox I-84
   (2026-09-21) already told this project "the beta's CLI shape:
   `--pattern`, file operands, `--version`; abi 28" while executing a
   pcrec-side stranger-clone check — but nothing in `testees/pcrec/`
   was updated for it until this lane.

   **Fix, in the same commit as the re-pin** (`testees/pcrec/
   adapter.py`'s `_compile_one`, phase 1's argv, plus SIX direct pcrec
   invocations found by grep in `tools/selfcheck.py` using the same old
   shape — the abi-floor sabotage witness, the emit-size-port probe, the
   subject-timeout control, and three altwide/fold ratio witnesses):
   every one now spells `["-o", art, "--pattern", pattern]` in place of
   `["-o", art, "--", pattern]`. Verified: `--pattern` consumes the very
   next argv token unconditionally (no `--` separator needed — confirmed
   on a pattern beginning with `-`, and on a raw high-byte value passed
   as a `bytes` argv element, the I-72 convention, which is unaffected:
   subprocess still accepts a mixed str/bytes argv list on POSIX).
   `--list-source` (`pcrecbench/rxt_source.py`) was ALREADY file-operand
   shaped (`[binary, "--list-source", rxt_path]`) and needed no change —
   confirmed by running it against `bench/email/export/email.rxt`.
   `--features all` semantics (REL-1.11's own internal refactor,
   per-call gating instead of a process-global read) are UNCHANGED,
   confirmed by a smoke compile of a named-group pattern with and
   without the flag: same refusal wording, same acceptance.

   **The grep for the old shape is exhaustive** (the mandated step):
   searched `pcrecbench/`, `testees/`, `tools/` for a bare `"--"` /
   `"--",` token beside a pcrec argv build. The only other `"--",` hit
   in the tree is `catalogue/check_interpret.py`'s `git diff ... --`,
   unrelated.

5. **Re-archive and diff all four registry surfaces.** DONE, commit
   `6132618`. Every data row diffed directly against this build's live
   `--list-*` output — every delta accounted for by name:
   - `list_axes.tsv`: **80/28 → 87/31.** SEVEN rows added, THREE new
     axes, exactly I-87's own description: `vm-anchor-bound` (order 1
     `anchored`, order 2 `gstart`, order 3 `unanchored` fallback — stamp
     `RX_VM_START`, deny `PCREC_NO_VM_ANCHOR_BOUND` bit 28, cli
     `-fno-vm-anchor-bound`); `end-window` (order 1 `window` — stamp
     `RX_END_WINDOW`, deny `PCREC_NO_END_WINDOW` bit 29, cli
     `-fno-end-window`; order 2 `none` fallback); `req-byte` (order 1
     `byte` — stamp `RX_REQ_BYTE`, deny `PCREC_NO_REQ_BYTE` bit 30, cli
     `-fno-req-byte`; order 2 `none` fallback). Every other row
     byte-identical.
   - `list_limits.tsv`: **58 rows, count unchanged.** FOUR rows reworded
     in their `override` column only (`PCREC_MAX_AUTO_DFA_ELEMS`,
     `PCREC_MAX_VM_EMIT_CODE_BYTES`, `PCREC_DEFAULT_WARN_EMIT_BYTES`,
     `PCREC_MAX_EMIT_BYTES`: `-D` → `flag+-D`) plus one appended note
     each. Traced to pcrec commit `d2cd3c81` ("[LIM-OVR]: FLAG_D token +
     override-honesty check for the two-lever shape", lane admin1,
     landing in the same commit range) — NOT part of [OPTLOOP.1]: each
     of the four already had a real per-compile caller lever the old
     `-D` token's description denied existed; `flag+-D` names the true
     two-lever shape honestly. No numeric value moved. Same shape as
     [REVW.4]'s +1 row at the 25b1984f re-pin — a co-landing,
     independently-explained delta, not silently absorbed.
   - `list_definitions.tsv`: 50 rows, **byte-identical** — the eleventh
     pin running.
   - `list_schema.tsv`: 71 rows, **byte-identical** — D118 changes how
     pcrec is INVOKED on a `.rxt` file, never the file's own grammar,
     which is exactly what this table describes.

6. **The shim/adapter: `rx_info.abi` and the floor.** DONE. `struct
   rx_info` diffed field for field between the two pins' emitted `.h`
   (the `abc` witness) — zero hunks in the struct body. `PB_SHIM_MIN_ABI`
   confirmed unchanged source, `16`. None of the three new abi-29
   stamps has an `rx_info` mirror (verified: all three are read only via
   the `#ifdef`-guarded macro, driver-printed as `info` lines, never off
   a struct field), so the floor-raising rule (a FIELD addition, never a
   macro) does not apply.

7. **The three new stamp readers, added per the D81 pattern.**
   `testees/pcrec/shim.c`: `pb_req_byte()` / `pb_end_window()` /
   `pb_vm_start()`, the same `#ifdef MACRO / return MACRO; #else /
   return NULL` shape as `pb_dfa_start()`. `testees/pcrec/driver.c`:
   three declarations, three `SYM()` registrations, two `info` prints
   beside `pb_engine_stamp()` (the "every" scope) and one beside the
   fast-tier block (the "vm" scope), plus the header comment's `info`
   line inventory. `testees/pcrec/adapter.py`: `req_byte` / `end_window`
   / `vm_start` added to `STR_PAIRS`, `STAMP_SCOPE` (`req_byte`/
   `end_window` → `("every", 29)`, `vm_start` → `("vm", 29)`),
   `METADATA_DECL` (full descriptions, each citing its shim accessor and
   scope) and `REGISTRY_STAMP_PAIRS` — `vm_start` ONLY (its three
   candidates are all enumerable name values in the registry;
   `req_byte`/`end_window` carry a variable value on their order-1 row,
   the same shape as `dfa_prefilter_offsets`, which is likewise absent
   from that dict).

8. **Stamp spot-checks, by value, on hand-chosen witnesses** (matching
   `check_mechanism_stamps`'s own precedent of small hand-chosen
   patterns rather than corpus ones):

   | witness | config | req_byte | end_window | vm_start |
   |---|---|---|---|---|
   | `abc` | auto (DFA) | `114` (`c`) | `none` | absent (DFA route) |
   | `foo[0-9]+bar` | auto (DFA) | `114` (`r`) | `none` | absent |
   | `a(b\|c)+d` | auto (hybrid, vm route) | `100` (`d`) | `none` | `unanchored` |
   | `foo\|bar` | `--engine=vm` | `none` | `none` | `unanchored` |
   | `^foo` | `--engine=vm` | `111` (`o`) | `none` | **`anchored`** |
   | `\Gfoo` | `--engine=vm` | `111` (`o`) | `none` | **`gstart`** |
   | `foo\z` | `--engine=vm` | `111` (`o`) | **`3`** | `unanchored` |
   | `x[ac]y` | `--engine=vm` | `121` (`y`) | `none` | `unanchored` |
   | `[a-z]{0,32768}\z` (whole) | auto (declined-nullable) | `none` | **`32768`** | `unanchored` |

   Every deny flag flips its stamp to the fallback (`check_deny_flag_
   controls`, 3 new rows, all passing): `-fno-req-byte` on
   `foo[0-9]+bar` → `req_byte none`; `-fno-end-window` on `foo\z` under
   `--engine=vm` → `end_window none`; `-fno-vm-anchor-bound` on `^foo`
   under `--engine=vm` → `vm_start unanchored`.

9. **FINDING 3 — the size books are NOT flat this time, and that is
   itself the finding.** The brief's own prediction ("the three new
   stamp lines should account for a flat per-artifact constant") holds
   for the *stamp lines themselves* only when every value is `"none"`/
   the shortest token — MEASURED as **`B74_STAMP_LINES_DFA = 56`** (the
   two "every"-scope lines, both `"none"`) and **`B74_STAMP_LINES_VM =
   89`** (the same two plus `RX_VM_START`'s line). But TWO of the three
   axes are REAL OPTIMIZATIONS, not informational stamps: MEASURED
   directly (`pfx3-256` forced-VM, `x[ac]y`, diffed byte for byte
   against their 25b1984f artifacts) that a non-`"none"` `req_byte`
   emits one `#include <string.h>` line AND a functional memchr guard
   block ahead of the search entry —

       /* [OPT-REQBYTE] every match of this pattern contains the byte
        * 120, so a window without it holds no match at all. */
       if (subject_length <= search_from ||
           !memchr(subject + search_from, 120, subject_length - search_from))
           return 0;

   — and a non-`"none"` `end_window` (the `cls-upto-32768` whole-subject
   witness, `end_window "32768"`) costs **+217 B**, far more than the
   flat term, implying [OPT-ENDWIN] likewise emits a real `search_from`
   clamp rather than only a comment. Because [OPT-REQBYTE]'s guard's own
   byte count varies with the required byte's digit count (MEASURED:
   `+242 B` on a 3-digit byte, `+240 B` on a 2-digit one), **no single
   flat formula covers the firing population** — this lane did not
   attempt to derive one; every affected `tools/selfcheck.py` assertion
   (20 in `STAMP_CASES`/`LEDGER_STAMP_CASES`, 3 in `DENY_CONTROLS`) was
   individually RE-MEASURED against the live pin and the literal
   documented inline with which case it is (flat / memchr-firing /
   end-window-firing) and why. This is worth flagging for the
   [OPTLOOP.1] cycle-1 measurement window in [B74] (b): the timing
   effect of a real memchr guard or search_from clamp is exactly what
   that window exists to read, and the ONE variable it moves is the
   compile pipeline this lane just finished absorbing.

10. **`catalogue/rules.toml`'s `[[pin_order]]`.** DONE, commit `6132618`.
    `8d716693` appended after `25b1984f`. `catalogue_version` 3.2 →
    **3.3** (MINOR: a `[[pin_order]]` append only).

11. **`testees/pcrec/CLAUDE.md` / root `CLAUDE.md`.** DONE, commit
    `f3bf61d`. Both gain a dated section following the established
    per-re-pin narrative shape (findings 1-3, item 5's registry deltas).
    `docs/dev/plan.md`'s `[B74]` row and the STATUS narrative are the
    manager's, per the brief.

12. **Full `make check` at the new pin — RUN TWICE; the second run is
    the delivered one.**

    **First run** (launched 20:37 EDT, box load 0.80/1.16/0.99 —
    elevated vs. a typical quiet-box re-pin launch, e.g. b58repin's
    0.09/0.21/1.22, but `make check` is the smoke suite,
    `--trials 1 --iters 1`, correctness not timing, so not a BD3
    violation) completed `DONE rc=2` at 20:53: `check-harness` **455
    passed, 1 FAILED**. The one failure —

        FAIL  subject-timeout control  s-hang did not time out: nomatch

    — is a REAL regression this lane's own re-pin caused, in a
    pre-existing check `check_subject_timeout` never touched by items
    1-11 above. See item 13.

    **FINDING 4 — the abi-29 re-pin silently defeated the subject-timeout
    control.** `check_subject_timeout` (`tools/selfcheck.py`) compiles
    `(a+)+b` (`--engine=vm --fno-step-budget --backtrack-frames=100000`,
    NO step budget by design) and feeds it a 40-`a` subject with no
    trailing `b`, which must exhaust the per-subject `SIGALRM` at 3 s and
    come back `timed-out` BY NAME — the one place this project's whole
    per-subject-timeout ALARM PATH (the signal, the `siglongjmp`, the
    attribution to the right subject, the driver continuing to the next
    one) is exercised at all. MEASURED directly (`hangwit.c`, the exact
    compile the check performs): at 8d716693 `(a+)+b` now stamps
    `RX_REQ_BYTE "98"` ('b') — every match must contain a 'b' on every
    path — so the emitted entry runs

        if (subject_length <= search_from ||
            !memchr(subject + search_from, 98, subject_length - search_from))
            return 0;

    ahead of the VM, and the 40-`a` fixture (no 'b' anywhere) is dismissed
    as an instant `nomatch` before the catastrophic-backtracking VM this
    control exists to exercise ever runs. Neither `RX_END_WINDOW`
    (`"none"`) nor `RX_VM_START` (`"unanchored"`) is implicated — verified
    by reading `hangwit.c`'s full stamp block, not merely the one that
    fired.

13. **Fix, same lane, before delivery — commit `95c69c4`.** The fixture's
    subject changes from `b"a" * 40` to **`b"b" + b"a" * 40`** (41 bytes,
    `S("s-hang", hang, 41)`). The guard only asks whether the required
    byte appears ANYWHERE in `[search_from, subject_length)`, never
    where, so a leading `'b'` the match can never actually use satisfies
    it; the unanchored search still finds no completion starting at
    offset 0 (a literal `'b'`, but `(a+)` needs an `'a'` first) and then
    explores the SAME exponential split of the trailing 40-`a` run
    starting at offset 1 that hung before this pin — the control is
    restored without sharing any source with `[OPT-REQBYTE]` itself (a
    subject BYTE, never a flag or a stamp read, matching the file's own
    "no failing case proves nothing" / independent-control discipline).
    `s-fine` (`"ab"`) already contains a `'b'` and was never affected.
    Verified standalone (`check_subject_timeout` alone): `s-hang ->
    timed-out, by name`; `s-fine` answered right after it. Re-verified
    `check_mechanism_stamps` (114/114) and `check_deny_flag_controls`
    (14/14) unmoved by the fixture edit.

14. **Second `make check` run — THE DELIVERED NUMBERS.** Relaunched
    22:xx EDT (box load 0.60/0.40/0.18 at launch, quieter than the
    first), polled by a bounded foreground `until grep -q "DONE rc="`
    loop rather than waited on a background-task notification (the
    first run's own notification arrived only once the manager had
    already read the log directly — a stall this project's boilerplate
    already names as a known mode). Completed `DONE rc=2`:

    | check | result | vs. gate of record (5/73/0 · 450/450 · 84+7+8 · 190/190) |
    |---|---|---|
    | `check-schema` | 5 example(s) accepted, 73 sabotage(s) rejected, 0 WRONG | **matches** |
    | `check-harness` | **456 passed, 0 FAILED** | **+6** — exactly the 3 new `DENY_CONTROLS` rows (req_byte/end_window/vm_start deny flags) + the 3 new `STAMP_CASES` witnesses (VM-route anchored/gstart start, the end-window numeric-value witness); no other line moved |
    | pytest-style suites (report/matrix/etc., inside `check-report`) | 84 + 7 + 8 = **99** | **matches**, unmoved (this lane never touched `report.py`/`reduce.py`) |
    | `check-report` | OK | **matches** |
    | `check-interpret` | **163 passed, 27 FAILED** (190 total, unchanged) | see below |

    `make`'s own exit is **2**, solely from the 27 `check-interpret`
    failures — every one section 3 ("sidecar freshness"), every one
    reading `re-renders byte-identical` as its printed assertion name
    (the label states the check's claim, not its outcome, exactly as
    b58repin's report already explained for this class):

        2026-08-25-email-specimen-0.1-budu-ryzen1600-repin-692c2e8.interpretation.md
        2026-09-06-bounded-0.3-budu-ryzen1600-after-d34c9131.interpretation.md
        2026-09-07-syntax-0.1-budu-ryzen1600-first-d34c9131.interpretation.md
        2026-09-19-capability-0.1-budu-ryzen1600-rust-first-cf0962e3.interpretation.md
        2026-09-20-altwide-0.2-budu-ryzen1600-fullroster-d34c9131.interpretation.md
        2026-09-20-altwide-0.2-budu-ryzen1600-rust-first-25b1984f.interpretation.md
        2026-09-20-bounded-0.3-budu-ryzen1600-fullroster-d34c9131.interpretation.md
        2026-09-20-bounded-0.3-budu-ryzen1600-rust-first-25b1984f.interpretation.md
        2026-09-20-capability-0.1-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-20-capability-0.1-budu-ryzen1600-pinconfirm-25b1984f.interpretation.md
        2026-09-20-email-specimen-0.2-budu-ryzen1600-fullroster-d34c9131.interpretation.md
        2026-09-20-email-specimen-0.2-budu-ryzen1600-rust-first-25b1984f.interpretation.md
        2026-09-20-loglines-0.1-budu-ryzen1600-fullroster-d34c9131.interpretation.md
        2026-09-20-loglines-0.1-budu-ryzen1600-rust-first-25b1984f.interpretation.md
        2026-09-20-syntax-0.1-budu-ryzen1600-fullroster-d34c9131.interpretation.md
        2026-09-20-syntax-0.1-budu-ryzen1600-rust-first-25b1984f.interpretation.md
        2026-09-21-altwide-0.2-budu-ryzen1600-after-25b1984f.interpretation.md
        2026-09-21-altwide-0.2-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-21-bounded-0.3-budu-ryzen1600-after-25b1984f.interpretation.md
        2026-09-21-bounded-0.3-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-21-email-specimen-0.2-budu-ryzen1600-after-25b1984f.interpretation.md
        2026-09-21-email-specimen-0.2-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-21-loglines-0.1-budu-ryzen1600-after-25b1984f.interpretation.md
        2026-09-21-loglines-0.1-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-21-syntax-0.1-budu-ryzen1600-after-25b1984f.interpretation.md
        2026-09-21-syntax-0.1-budu-ryzen1600-fullroster-25b1984f.interpretation.md
        2026-09-22-capability-0.1-budu-ryzen1600-wrapfix-25b1984f.interpretation.md

    **This is the SAME class b58repin's report classified at the
    25b1984f re-pin** (`docs/dev/lanes/b58repin_report.md` lines
    ~212-272): `catalogue_version`'s `[[pin_order]]`-append rule
    (3.2 → **3.3**, this lane's item 10) is MINOR/additive by the
    catalogue's own versioning clause, but "every bump regenerates every
    committed sidecar in the same commit" is a MANAGER'S merge-time step
    per the manager's explicit, standing instruction on this lane (never
    the re-pin lane's own) — the 27 failures are that gap surfacing
    exactly as expected, not a defect this lane introduced. Confirmed
    (per the manager's own read): the four `capability-0.1-*-first-*`
    sidecars `check_interpret.py`'s `_SIDECARS_BLOCKED_ON_CAPABILITY_
    FIRST_RULING` names (the pre-existing, unrelated [B72] stopgap for
    the `capability-0.1-first.tsv` predictions-file defect) are NOT in
    this lane's 27 — that stopgap holds unchanged at the bumped
    catalogue version, exactly as it must. `check-interpret section 1`
    21, `section 2` 8, `section 3` 2 (down from the pre-lane count —
    every OTHER sidecar moved to section 3's failing side, none to a
    different section), `section 4` 127, `section 5` 4, `section 6` 1 —
    163 + 27 = 190, the SAME total as the gate of record: no check was
    added, removed or silently dropped by this bump.

## Not done / OWED

- **OWED-1 — RESOLVED.** The full `make check` run's four counts are
  in item 14 above; `make`'s exit code is 2, entirely attributable to
  the 27 named, classified sidecar-staleness failures.
- **OWED-2** (same precedent as b58repin's OWED-2, and the SAME shape):
  sidecar regeneration for the catalogue 3.2 → 3.3 bump — the 27 files
  named in item 14, MINOR/additive per the catalogue's own rule, and per
  the manager's explicit instruction on this lane this lane does NOT
  regenerate them — that runs at the manager's merge, exactly as
  b58repin's OWED-2 did not either.
- No `store/` record needed re-deriving — this lane touches no `store/`
  record; the re-pin itself never runs a measurement window.
- `docs/dev/plan.md`'s `[B74]` row and the STATUS narrative are
  explicitly the manager's job per the brief; left untouched.
- **[B74] (b)**, the capability re-measurement window, is explicitly out
  of scope for this lane and NOT started.

## For the manager, on review

- **Two findings beyond I-87's stated scope, both explained and
  resolved in this same lane**: (1) an unannounced abi 27→28 step
  (REL-1.4's version stamp, no field, no floor move) this project had
  prior warning of (inbox I-84) but had not yet absorbed; (2) pcrec's
  D118 CLI reshape, landing in the same commit range as [OPTLOOP.1],
  which broke every pcrec compile call in this project outright and
  required a real fix (seven call sites, `--pattern` replacing the old
  `-- 'PATTERN'` shape) before ANY of the ritual's later steps (build a
  witness, read a stamp, run `make check`) could proceed at all. Worth a
  line back through the inbox: pcrec's own D118 landed with real
  call-site-migration cost on the consumer side, the same shape [B32]'s
  comment-marker fix or [B58]'s `-fcomments` protocol-token fix were —
  the difference is that a *silent* CLI shape change is a much sharper
  edge than a *silent* comment-default change, because it fails LOUD
  (every compile refuses) rather than quiet (a covariate silently reads
  zero). This project happened to catch it because a re-pin necessarily
  compiles something; a hypothetical future pin bump landing between two
  measurement windows with NO re-pin lane in between would have caught
  it at the next `pcrecbench run` instead, with a less legible failure
  mode.
- **A THIRD finding for [B74] (b)'s own read, when it runs**: the
  size-book non-flatness (finding 3) means [OPTLOOP.1]'s three axes are
  not merely observability — two of the three change the emitted
  MACHINE (a real memchr guard, a real search_from clamp) exactly the
  way [OPT-5] STEP 1's scan edge did at a7e0bdf. The window should
  expect real timing movement wherever `req_byte`/`end_window` fire on
  the named target cells (I-87 (b)'s router-prefix-order witness is
  explicitly named as carrying `RX_REQ_BYTE "114"` — confirmed by this
  lane: `router-prefix-order` under `pcrec-auto` reads `req_byte 114`
  directly, per item 8's method applied to that corpus pattern).
- **A FOURTH finding, caught by `make check` itself rather than by this
  lane's own review**: [OPT-REQBYTE] silently defeated a pre-existing
  harness control (`check_subject_timeout`, items 12-13) — the one
  place this project's per-subject `SIGALRM`/`siglongjmp`/attribution
  path is exercised at all. The mechanism (a required-byte memchr guard
  ahead of the VM) is exactly the same shape that will make some
  cross-pin cells in [B74] (b)'s own window answer `nomatch` FASTER for
  a reason that has nothing to do with the VM getting faster — a reader
  of that window should expect a `req_byte`-bearing pattern's `nomatch`
  subjects to show large wins from the guard alone, separate from
  whatever the VM-side axes move. Worth a line to pcrec too: a
  required-byte optimization that turns a catastrophic-backtracking
  witness into an instant rejection is the INTENDED behaviour for a real
  subject, but it is exactly the shape that silently retires a
  test-suite's own hang-detection fixture elsewhere — the same class of
  risk [OPT-5]'s scan edge and [ENG-ISL]'s island posed to this
  project's own stamp constants, now posed to a CONTROL instead of a
  size-book number.
- The `list_limits.tsv` four-row rewording (item 5) and the D118 CLI
  break (finding 2) are both worth a line in whatever goes back through
  the inbox ack — the registry delta is new-but-explained (like
  `list_schema.tsv`'s +1 row at cf0962e3), and the CLI break is a real
  functional bug this pin would otherwise have introduced silently into
  every pcrec compile this project makes, worth pcrec knowing a
  consumer outside their own test suite depends on the old `-- 'PATTERN'`
  shape (now migrated, but a documentation note in pcrec's own D118
  entry about downstream consumers might save the next one this trip).
- **This lane is COMPLETE.** Both charter-vs-committed checklist items
  are DONE or explicitly OWED-and-explained (OWED-2, the sidecar
  regeneration, per the manager's own standing instruction that this is
  a merge-time step); no further work is planned unless review surfaces
  something new. `[B74] (b)` — the capability re-measurement window — is
  the manager's next step.
