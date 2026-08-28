# tools/ — repo tooling that is not the harness

| file | role |
|---|---|
| `selfcheck.py` | `make check-harness`: the [B3] half of the self-check suite |

THE GENERIC GATES ENUMERATE (`subbench_dirs()`, [B11.1]). Harness contract 6
says "bench/*/ each", and the checks that belong to the sub-bench CONTRACT --
the generators reproduce their committed manifests, any other `gen_*.py` in
the directory re-derives under `--check`, `expectations.tsv` re-derives, both
drivers answer the set's floor pattern exactly as the oracle says -- discover
every `bench/<name>/` with a `subbench.toml` instead of naming one. They named
`email`, and the count this suite prints would not have moved on the day a
second sub-bench landed: a check that silently covers half of what it claims
is the shape of failure this file's organising principle exists to prevent.
The email-SPECIFIC arms (the wrong-answer fixture, the two-patterns control,
the frame-buffer block, the `whole-subject` form control) stay named, because
they are about that set's own fixtures and not about the contract.

The per-sub-bench floor smoke is also the per-sub-bench DRIVER smoke: a real
adapter compiles a real pattern of the set and answers real subjects of it,
and it picks its two subjects BY THE EXPECTATION rather than by looking for a
byte -- a set whose floor matches every subject (bench/loglines' is `:`) has
no missing one, and the check says so rather than failing.

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
