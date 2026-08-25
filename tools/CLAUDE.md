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
`abi == 3` with the four sizing pairs; a DFA artifact stamps a frame size of
0 and records no `buffer_*` pair; a VM artifact records the configured
capacities. Seven PASS lines, all needing the pin's `_in` surface (pcrec
17469b6 or later).

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
