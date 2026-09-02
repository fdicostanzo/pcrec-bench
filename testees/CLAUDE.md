# testees/ — the adapters

One directory per ENGINE (harness contract §3). An engine directory
provides several TESTEES — an (engine, version, build/run configuration)
triple each (requirements §2) — enumerated in its `configs.toml`.

| directory | testees it provides |
|---|---|
| `pcre2/` | `pcre2-interp`, `pcre2-jit` |
| `pcrec/` | `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm` (the plain three, gcc); `pcrec-auto-in`, `pcrec-vm-in` (the caller-provided frame-buffer variants, [B8]); `pcrec-auto-clang`, `pcrec-nocaps-clang`, `pcrec-vm-clang` (the compilee-toolchain axis, [B24]); `pcrec-auto-bigcap`, `pcrec-vm-bigcap` (the emitted-size cap axis at 8 MiB, [B31] — bench/altwide's window only); `pcrec-auto-noedge` (the scan-edge deny axis, [B32] — [OPT-EDGE]'s BEFORE on bench/loglines and bench/bounded); and `pcrec-local`, a PROVIDED binary at no pin (scratch tier by construction, [B10]). Twelve pinned configs + one local; `testees/pcrec/configs.toml` is the roster, `python3 -m pcrecbench testees` prints it |

An adapter is `adapter.py` (a subclass of `pcrecbench.adapters.Adapter`),
`configs.toml`, usually a `driver.c`, and a `CLAUDE.md` that states its
compile-cost definition and its `consumed_length` convention. Discovery
is by directory: `pcrecbench/adapters.py` imports `testees/*/adapter.py`
and asks each for its `testees()`.

`pcrecbench/adapters.py` is also where the DRIVER PROTOCOL both drivers
implement is specified, in full, at the top of the file. Read that
before writing a third driver: the point of the protocol is that two
engines' numbers are produced by the same shape of loop, so a difference
between them is the engine and not the harness.

## The one rule that is not obvious

**Every version is PROBED, never typed.** `describe()` reads the engine's
own version out of the built artifact or the loaded library
(`pcre2_config(PCRE2_CONFIG_VERSION)`; pcrec's pinned commit +
`git describe`). A hand-typed version in a `configs.toml` would be a
claim the record could not check, and `testee_id` is DERIVED from it
(record_schema.md §6.4, rule X5) — so a wrong version silently renames
the testee.
