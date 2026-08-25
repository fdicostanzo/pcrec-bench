# testees/pcre2/ — the libpcre2 adapter

Provides two testees:

| config id | execution model | compile phases |
|---|---|---|
| `pcre2-interp` | `interpretive` | `compile` |
| `pcre2-jit` | `eager-jit` | `compile`, `jit-compile` |

| file | role |
|---|---|
| `adapter.py` | `describe`/`prepare`/`compile`/`measure`; the engine-metadata DECLARATION |
| `driver.c` | the batched in-process timing driver (the protocol is in `pcrecbench/adapters.py`) |
| `configs.toml` | the two config ids; **no version is written here** |

## Why dlopen and hand-declared prototypes

This box has the PCRE2 8-bit RUNTIME (`libpcre2-8.so.0`) but not the `-dev`
package: no `pcre2.h`, no unversioned `.so`, no pkg-config file. The
precedent is pcrec's `tests/fuzz/pcre2_abi.h` and the email specimen's
`pcre2_throughput.c`. Every function is read off the library's exported
symbols; every constant that is not a symbol — the anchoring bits, the
`pcre2_pattern_info` codes, `PCRE2_CONFIG_VERSION` — carries a `[measured]`
note in `driver.c` saying how its value was established by probing.

## The compile-cost definition

- **`pcre2-interp`** — one phase: `pcre2_compile_8`, timed in-driver.
- **`pcre2-jit`** — two: that call, then
  `pcre2_jit_compile_8(PCRE2_JIT_COMPLETE)`. An eager JIT has a separable
  call, so there is a number to take. `warmup_trials` is 0: nothing warms
  after the compile. (A LAZY JIT is the one whose cost is "trial 1 minus
  steady state" — pcre2's is not one, and modelling it as one would put a
  fabricated number on the compile axis.)

## `consumed_length`: the convention, stated plainly

**`consumed_length` is the subject length the driver passed and pcre2
accepted — i.e. the whole subject.** `pcre2_match` takes a `size_t` length,
has no subject-size ceiling to truncate against, and exposes no scan
high-water mark. So the honest claim behind a `truncation_check = verified`
row is *"no byte was withheld or refused"*, never *"the engine looked at
every byte"*. Anyone comparing a throughput number against an engine that
DOES report a scan position should read this paragraph first.

## Engine metadata

Three structured facts, all from `pcre2_pattern_info_8`, all declared in
`adapter.py` before use (record_schema.md §7 rule 1):
`capturecount`, `compiled_size_bytes` (requirements §4.2's "program size" for
this engine) and `jit_size_bytes` (jit testee only — an ABSENT pair is not an
error; an UNDECLARED one is).
