# tools/ — repo tooling that is not the harness

| file | role |
|---|---|
| `selfcheck.py` | `make check-harness`: the [B3] half of the self-check suite |

`selfcheck.py`'s organising principle is pcrec's check-design lesson: every
gate is exercised against an input it must REJECT in the same run that
exercises it against one it must accept. A check with no failing case proves
nothing, and a control that passes because the judge dislikes everything
proves nothing either — which is why the wrong-answer control runs each
falsified expectation AND its committed counterpart.

Three of its controls have already failed a real implementation and changed
the code: the two-patterns control (both patterns shared one workdir), the
store race control (a shared staging directory lost 2 of 8 records), and the
per-subject timeout control (nothing in the corpus hangs, so the alarm path
had never run). A fourth, the v1.1-readiness control, exists to stop
`record.project()` becoming dead code before the schema version flips.

The frame-buffer block (`check_frame_buffer`, [B8]) follows the same rule:
its "buffer matters" arm was sabotaged once on purpose — the shim made to
pass a NULL descriptor — and the configured-capacities arm failed exactly as
it must (the deep subject gave up as under the default), so the control is
known to see a shim that ignores the buffer. Its other arms: the `_in`
entries agree with the plain ones on the smoke pattern; a tiny caller buffer
gives up `PCREC_ERR_FRAMES` BY NAME; every pcrec compile row at the pin reads
ONE abi with the four sizing pairs; a DFA artifact stamps a frame size of
0 and records no `buffer_*` pair; a VM artifact records the configured
capacities. Seven PASS lines, all needing the pin's `_in` surface (pcrec
17469b6 or later).

That abi arm used to read `abi == 3` as a literal, and was edited at every
re-pin ([B16] removed it): a check that has to be edited to keep passing is
a check of this file's edit history. It now READS the abi and holds what
actually matters — one abi across four artifacts of both engines (a mixed
set would mean two pcrecs got into one run), at or above the floor
IMPORTED from `shim.c`'s `PB_SHIM_MIN_ABI` rather than retyped here.

The [B10] blocks (schema v1.2, the tiers, `quick`, `pcrec-local`) add
sixteen PASS lines, every gate with its sabotage: the two tier controls
are rejected FOR X28 / X29 by name and the 1.1 examples with no `tier`
still validate; the canonical store refuses a scratch record on write
and refuses to INDEX one planted by hand (the control: a scratch store
takes the same record, validated); the shared reduction reproduces a
hand-computed median (3 trials × 2 subjects → 220) and EXCLUDES a set
with one give-up while naming its code; a `quick` cell completes under
`gnutimeout 300` and the median it printed is recomputed from the record
file with the same function; `pcrec-local` errors cleanly without
`$PCREC_BIN`, describes the pin's binary as `local:<sha12>` with no
`+describe`, describes a scratch-built repository as `+<sha>` with HEAD
when clean and `+…-dirty` with a null commit when dirty, runs a quick
cell, and is REFUSED into a canonical store (a temp one carrying the
marker, so a broken refusal cannot reach the real `store/`).

The [B16] blocks (2026-08-28, the abi-8 re-pin) add thirteen PASS lines
across three checks, each built around the failure it would otherwise
miss:

- `check_mechanism_stamps` compiles a real artifact of each KIND at the
  pin — pure DFA, VM HYBRID, non-hybrid VM, provably-empty — and asserts
  each stamp's VALUE, not its presence. A presence-only check would pass
  a `dfa_prefilter` filled from the wrong macro (it would read `hybrid`,
  which is not in that pair's value set at all), and would pass an
  adapter that dropped a pair the driver prints — a real failure this
  bench shipped for five pins, since `engine_stamp` was printed from abi
  4 and never recorded. Both directions of match_api.md §6.3 (a)'s IFF
  are asserted (a hybrid carries all three `_DFA_*` pairs; a non-hybrid
  VM carries none), and so is the fast tier's own scope. Its witnesses
  are small hand-chosen patterns rather than `bench/email`'s, because a
  check whose witness is a corpus pattern stops being a check the day
  engine selection moves under it — which is exactly what happened to
  `factored` between 8da6120 and 692c2e8.
- `check_dfa_table_deny_flag` is the control that keeps `dfa_table` from
  being indistinguishable from a constant. pcrec's own form census
  measured `indexed` and `mixed` at ZERO corpus population, so nothing
  this bench measures will ever move that stamp; `-fno-premul-table`
  (tuning.md §2.13) reaches `indexed` on the census's own witness
  pattern, through `pcrec-local` at the pin's binary.
- `check_abi_floor_refusal` is the SABOTAGE, and the path is unreachable
  without one: the pin is abi 8, so nothing in the corpus can be below
  the floor. A real artifact's `.abi = 8` is edited to `5` in a copy,
  built with the ordinary shim and run by the ordinary driver, and must
  be refused BY NAME carrying both numbers — with the unmodified
  artifact loading in the same run as the positive control (a refusal
  that fired on everything would pass a check written without it), and
  the token the adapter watches for checked against the diagnostic the
  driver actually produced, since that is two copies of one string in
  two languages with nothing else enforcing that they agree.
