# testees/pcrec/ — the pcrec adapter

Provides fourteen testees at the commit pinned in `configs.toml`, and one —
`pcrec-local` — at no pin at all:

| config id | pcrec flags | what it is for |
|---|---|---|
| `pcrec-auto` | `--features all` | the defaults: engine chosen automatically, captures on |
| `pcrec-nocaps` | `+ --no-captures` | the axis that recovers a pure-DFA artifact for a group-bearing pattern |
| `pcrec-vm` | `+ --engine=vm` | the VM forced, prefilter off, so the VM derives the whole span independently |
| `pcrec-auto-in` | `--features all` + `buffer_frames = 32768`, `buffer_trail = 131072` | the defaults, matched through the `_in` entries with a caller-provided frame buffer. INERT wherever `auto` picks the DFA — which is still every artifact of `bench/email` (RE-VERIFIED at pin 36d5963, 2026-08-29: all six `auto`/`nocaps` artifacts stamp `RX_ENGINE "dfa"`, both forms), so it is DEFINED but NOT MEASURED there (the checks use it; it goes live on a sub-bench with VM-selected patterns under `auto` — and since 36d5963 `bench/loglines` HAS one: `level-context` is a VM artifact under `auto`, the [SEL-1] fallback) |
| `pcrec-vm-in` | `+ --engine=vm` + the same two capacities | RULED 2026-08-25 (manager + pcrec manager; Frank's word pending via the inbox): the VM forced with the buffer, the one entry on `bench/email` where the depth path is reachable and the capacities were measured — the sixth cell of the [B8] window |
| `pcrec-auto-clang`, `pcrec-nocaps-clang`, `pcrec-vm-clang` | the same flags as their gcc siblings, plus `cc = "clang"` | ([B24]) THE COMPILEE TOOLCHAIN AXIS: the same pcrec artifact, compiled by clang instead of gcc. See below |
| `pcrec-auto-bigcap`, `pcrec-vm-bigcap` | the same flags as `pcrec-auto` / `pcrec-vm`, plus `max_emit_bytes = 8388608` and `max_emit_code_bytes = 8388608` | ([B31]) THE EMITTED-SIZE CAP AXIS: pcrec's two raise-only per-compile overrides, at 8 MiB, so `bench/altwide`'s wide rungs emit an artifact instead of a refusal. See below |
| `pcrec-auto-noedge` | the same flags as `pcrec-auto`, plus `-fno-scan-edge` | ([B32]) THE SCAN-EDGE DENY AXIS: the [OPT-5] scan edge denied, so the artifact is the pre-[OPT-5] machine built at the SAME pin — [OPT-EDGE]'s BEFORE. See below |
| `pcrec-auto-noisland` | the same flags as `pcrec-auto`, plus `-fno-alt-island` | ([B37]) THE ALTERNATION-ISLAND DENY AXIS: pcrec [ENG-ISL] STEP 1's VM alternation island (abi 18, a trie over a flat literal alternation's bytes instead of vm_alt's resume chain) DENIED, so the artifact is the pre-[ENG-ISL] VM program built at the SAME pin — the island's BEFORE on bench/altwide (the ORDER pair w-256/srt-256, the VM refusal wall, the island/chain code-byte ratios), with the lowering as the one variable. Derives `pcrec_334fd10e_auto-caps-simdna_noisland`. At this pin the denial also moves `vm_frameless` (a prefix-free island pushes nothing; the chain does) and `vm_entry_shape` (a framed artifact is `plain`) — the frame discipline and the entry chain travel with the lowering |
| `pcrec-auto-align64` | the same flags as `pcrec-auto`, plus `cflags = ["-falign-functions=64"]` | ([B35]) THE COMPILEE-FLAGS AXIS: OUR OWN phase-2 `$CC` compile of the artifact+shim gains one extra flag, never passed to pcrec — pcrec I-39 (v)'s layout probe for the disputed `floor` / match / `auto` cell. See below |
| `pcrec-local` | `--features all` + `$PCREC_LOCAL_FLAGS` | **a PROVIDED binary, `$PCREC_BIN`** ([B10], Frank's I-4 (c)): the edit-test loop's testee. No pin, SCRATCH TIER BY CONSTRUCTION, never in `store/`, never ranked. See below |

| file | role |
|---|---|
| `adapter.py` | the thirteen configs; the pin; `effective_cc()` (the compilee-toolchain rule); `effective_caps()` + `effective_denies()` + `effective_cflags()` + `compose_config_extra()` (the emitted-size cap rule, the deny-axis rule, the compilee-flags rule, and the ONE place `config_extra`'s parts are ordered); `scan_edge_counts()` (the [B32] covariate: pcrec's own `[OPT-5] SCAN EDGE:` marker counted in the emitted C and attributed to the machine it lands in); `binary_for()` (the ONE place the binary is chosen: the pin's, or `$PCREC_BIN`); `local_provenance()` (the `local:` version); the engine-metadata DECLARATION; the `buffer_*` config → driver argv plumbing |
| `pin.sh` | `git archive <commit>` from pcrec into the build root, and `make` THERE |
| `shim.c` | **the one file in this project that knows pcrec's ABI** |
| `driver.c` | the timing driver; its `dlopen` is the third AOT compile phase; `--buffer-frames N --buffer-trail M` allocate the caller-provided regions once per run |
| `configs.toml` | the config ids, `pin = "<commit>"`, the optional per-config `cc` and its precedence ruling ([B24]), the optional per-config `max_emit_bytes` / `max_emit_code_bytes` with the measured derivation of the 8 MiB bound ([B31]), the `_in` testees' capacities with the measurement that chose them, and `[testees.pcrec-local]` (`local = true`, `binary = "PCREC_BIN"`, `extra_flags = "PCREC_LOCAL_FLAGS"`) |
| `list_axes.tsv` | ([B18]) pcrec's `--list-axes` output at the pin, VERBATIM under a source header — the FOURTH registry surface (pcrec registry.md §6). `adapter.registry_check()` checks the declared stamp value sets against it; `make check-harness` diffs it against the pin's live output and reads the deny flags' spellings from it. Re-archive at every re-pin: the diff is the list of what moved |
| `list_definitions.tsv` | ([B19]) pcrec's `--list-definitions \| grep -v '^#'` output at the pin, VERBATIM under a source header — the FIFTH registry surface ([DD-11], pcrec registry.md §9): one row per construct DEFINED in terms of another. Nothing the adapter reads depends on it; `make check-harness` diffs it against the pin's live output (`check_list_definitions_registry`). Re-archive at every re-pin |
| `list_limits.tsv` | ([B22]) pcrec's `--list-limits` output at the pin, VERBATIM under a source header — the SIXTH registry surface (pcrec D90 / [LIM-1], table_contract.md) and the THIRD archive target (inbox I-25): one row per numeric limit in pcrec's `src/core/limits.def` (44 at 263b013, 45 at a7e0bdf — [OPT-5]'s `PCREC_MAX_SCAN_EDGES` joined), the table this bench's overflow readings (`>32000 states` = `PCREC_MAX_DFA_STATES_TABLE`, the K7 budget = `PCREC_MAX_SUBSET_ELEMS`, the [ENG-ABS] 4096 = `PCREC_ANCHORED_MAX_STATES`, the [ART-SIZE] caps) now resolve against by name. Nothing a RECORD carries is read from it (every cap/capacity a record needs is stamped per artifact); the ONE thing that reads it is the [B31] cap axis' raise-only FLOOR check, which refuses a below-default config value in the bench's own words and takes pcrec's two defaults from here rather than keeping a second copy of them. `make check-harness` diffs it against the pin's live output (`check_list_limits_registry`). Re-archive at every re-pin |

## `pin.sh` never writes inside pcrec

`/home/duxevents/pcrec` is read-only to this project. `pin.sh` extracts a
detached snapshot with `git archive` into
`$PCRECBENCH_BUILD_ROOT/pcrec-<commit>/` (default: the repo's MAIN tree's
`build/`, resolved via `git rev-parse --git-common-dir` so a worktree lands
in the same place its main tree does) and builds it there under
`gnutimeout 900`. Two consequences, both deliberate: a pcrec session running
its test batteries in that tree cannot be disturbed by a bench run, and a
bench number can never come from a dirty working tree. An existing build is
REUSED — the test is "the binary exists", which a half-finished extraction
cannot satisfy. `PIN.tsv` beside the tree carries the full commit, because a
`git archive` snapshot has no `.git` to ask.

## `pcrec-local`: a provided binary, scratch by construction ([B10])

    PCREC_BIN=~/pcrec/worktrees/mylane/build/pcrec \
    PCREC_LOCAL_FLAGS="--engine=vm" \
    python3 -m pcrecbench quick --subbench email --pattern orig \
        --regime search --testee pcrec-local --vs pcre2-jit

`$PCREC_BIN` is REQUIRED at run time (a missing or non-executable path
is a clean `AdapterError` naming the variable); `pin.sh` is never
called. The effective flags are `--features all` plus whatever
`$PCREC_LOCAL_FLAGS` adds (split on whitespace), recorded in
`build_flags` and `runtime_options`; `engine_mode` is DERIVED from them
(`--engine=vm` → `vm`, else `auto`) and `captures` from `--no-captures`,
so the derived `testee_id` says what ran. `describe()` reports:

- `engine_version` = `local:<first 12 hex of the binary's sha256>`, and
  when a git repository sits beside the binary — walking up from its
  directory to a `.git` FILE (a worktree) or directory — `+<git describe
  --always --dirty --tags>`, lowercased and sanitised. A `git archive`
  pin has a `PIN.tsv` and no repository, and the walk STOPS there (it
  must not climb into the tree that holds `build/`); this bench's own
  checkout is never taken as "the repository beside a pcrec binary". The
  queries are READ-ONLY (BD2): `describe` and `rev-parse`, nothing else.
- `engine_commit` = `git rev-parse HEAD` when the tree is clean, `null`
  when `describe` said `-dirty` — a dirty tree has no single commit.
- `tier: scratch` and `testee.binary = {path, sha256}` (schema v1.2,
  X28/X29). The harness reads `tier()` BEFORE it gates or measures, so
  `run --testee pcrec-local --store store` is refused with nothing
  touched; with no `--store` the record goes to the scratch store.

Everything after `describe()` — emit-c / gcc / load, `shim.c`,
`driver.c`, the metadata, the `_in` buffers — is the SAME code path as
the pinned testees: `binary_for()` is the only branch. `make
check-harness`'s `pcrec-local` block proves the five claims above
(missing variable; the pin's binary with no `+`; a scratch-built
repository clean then dirty; a quick cell; the canonical refusal).

## The compilee toolchain axis: `cc` ([B24]; pcrec [CC-CLANG])

pcrec is an ahead-of-time compiler. It emits C and stops — it has no
`--cc` flag and never invokes a compiler itself. Whoever runs a C
compiler on that emitted C is the **compilee toolchain**, and on this
bench that is us: `adapter.py`'s phase 2, the one command line that
builds `shim.c` (which `#include`s the artifact's `.c`) into the `.so`
we then `dlopen` and time. So the compiler is a property of the
**testee**, exactly like `--engine=vm` or `--no-captures`, and it is
spelled in `configs.toml`:

    cc = "gcc" | "clang"        # optional, per config

**Absent** it is today's behaviour, byte for byte: `$CC` if set, else
`gcc`; no `config_extra`; the same derived `testee_id`; the same
`build_flags` string (checked against a frozen copy of the pre-[B24]
renderer, so the store's committed `a7e0bdf` records stay comparable
with everything measured after).

**Present** it is an IDENTITY claim, and three things follow:

- `config_extra = "cc-<name>"` joins the derived `testee_id`
  (`record_schema.md` §6.4's escape hatch for two testees differing only
  in build flags). `pcrec-vm-clang` derives
  `pcrec_a7e0bdf_vm-caps-simdna_cc-clang` — its gcc sibling's id plus the
  token. Without it the pair would collide in the store.
- `build_flags` names the compiler and its `--version` first line
  (`env.compiler_raw()`, the same function `environment.compiler_raw`
  uses).
- the artifact and the shim are compiled by the SAME command, because
  they are one translation unit; they can never drift apart.

**Precedence, and why it is not pcrec's.** Under pcrec's `CLANGGEN=1`
(their `docs/testing.md`) an explicit `CC=` on the command line always
wins, because there `CLANGGEN` is a default. Here `cc` is part of the
testee's identity, and a `pcrec-vm-clang` record built by gcc would
carry a `testee_id` that lies. So a config with no `cc` still takes
`$CC` (unchanged), a config with `cc` takes that compiler, and a `$CC`
that CONTRADICTS a declared one is a clean `AdapterError` naming both,
raised before anything is measured.

**Exactly one variable moves.** `driver.c` is built by
`build_driver()` from `$CC` on every config, so a clang testee's timing
instrument is the same gcc-built driver as its sibling's. The record
says both: `run.driver_compiler` (the driver's) beside
`testee.build_flags` (the artifact's). The `gcc` compile PHASE keeps its
name on a clang testee too — it names the phase, not the compiler, so
the two siblings' phase times compare.

`environment.compiler` stays the BOX's toolchain dimension (§6.7): on a
clang testee it still reads gcc. That is the schema's own §11.4 open
question ("is the box's C compiler still an environment dimension") now
made concrete; it is FLAGGED for the panel, not worked around here.

**The `-in` variants stay gcc-only** on purpose: the frame-buffer axis
crossed with the compiler axis gives four cells whose differences no
single comparison can attribute.

### A clang refusal is a first-class outcome

MEASURED at pin `a7e0bdf` (abi 13) with clang 21.1.8, 2026-09-01: a VM
artifact that never pushes a resume frame emits

    goto *run->resume_stack[frame_index].resume_label;

into a function containing no `&&label` expression, and clang refuses:

    error: indirect goto in function with no address-of-label expressions

That is a `did-not-compile` compile row carrying clang's own diagnostic,
which is exactly what the bench is for. The same artifacts also draw a
cosmetic `unknown attribute 'noclone' ignored [-Wunknown-attributes]`
(no `-Werror` on this path, so it is not a failure). pcrec's [CC-CLANG]
step 1 fixed the `has_push` derivation at abi 14, so once this bench's
pin crosses that, the refusals stop and the rows become numbers.

`make check-harness`'s `check_cc_axis` holds this to a NAMED expected
refusal: a clang refusal passes only when its diagnostic carries that
cause verbatim, and any other refusal FAILS as a finding nobody has
read. The set of refusing kinds is PRINTED, never frozen, so the check
is green both before and after the pin crosses abi 14.

## The emitted-size cap axis: `max_emit_bytes` / `max_emit_code_bytes` ([B31]; pcrec [ART-SIZE])

pcrec REFUSES rather than emit past either of two caps — 1,000,000
comment-excluded bytes TOTAL and 500,000 of them OUTSIDE table
initializers (CODE) — and both are RAISE-ONLY per compile
(`docs/spec/limits.md` §8: "no caller can manufacture someone else's
refusal"). Two optional keys per config carry the raise:

    max_emit_bytes = N          # optional, per config, BYTES
    max_emit_code_bytes = N     # optional, per config, BYTES

**Why the bench needs them.** MEASURED 2026-09-02 at pin `1989c62` over
all of `bench/altwide@0.1` — 20 patterns × both forms × both engine modes
— **50 of 80 compiles REFUSE at the default caps** (26 auto rows at the
total cap, 24 forced-VM rows at the code cap). Without the raise the
set's whole point, the wide end of the branch-count ladder, has no
numbers at all. The census is
`docs/dev/measurements/2026-09-02-altwide-raised-cap-sizes.txt`.

**Absent** the keys, it is today's behaviour byte for byte: no flag on
pcrec's argv, no clause in `build_flags`, no `config_extra`, the same
derived `testee_id`. That is checked two ways — the pre-[B31] configs
directly, and every pcrec `testee_id` with a COMMITTED RECORD at this
pin re-derived byte-identically, `build_flags` included, because a
silent rename is the one damage this axis could do that no later reader
could detect.

**Present** they are an IDENTITY claim, and four things follow:

- the flags ride in the config's `flags` list, so ONE list feeds pcrec's
  argv, `build_flags` and `runtime_options` alike;
- `config_extra` carries both VALUES —
  `emitcap-8388608-codecap-8388608` — so two raises that differ cannot
  collide in the store;
- `build_flags` states what the raise MEANS, naming pcrec's default
  beside each raised value;
- and the ARTIFACT itself stamps the effective cap
  (`RX_MAX_EMIT_BYTES` on every artifact, `RX_MAX_EMIT_CODE_BYTES` on VM
  artifacts only), which is the witness nothing on this side can fake.

**A value BELOW pcrec's default is refused BY NAME, before anything is
measured** — an `AdapterError` naming the config, the key, both numbers
and the limit's own registry name. pcrec would refuse it too; the point
is that the bench refuses it first, at config-read time. The defaults
come from `list_limits.tsv`, the pin's own `--list-limits` printout,
rather than from a second copy of a pcrec constant in this repo.

**It is an AXIS, not a gate removed.** Raising `--max-emit-bytes` also
raises the [ART-SIZE] size-term ladder's own scratch abort bound (pcrec
`src/core/compile.c`: `3 × cap`, saturating), so a raised-cap compile
may explore — and select — an unroll K the default-cap compile aborted
out of. Two artifacts built under different caps are TWO ARTIFACTS. The
plain configs therefore stay, and their default-cap refusals stay
first-class `did-not-compile` rows.

**Why 8,388,608 for both.** The largest artifact in the whole census is
`s-4096`'s whole-subject forced-VM form at 3,741,164 bytes; a forced-VM
artifact has no table initializers, so its total and its code bytes are
one number and one maximum settles both caps. The bound is the smallest
power of two at or above twice that. The auto route's own code maximum
(37,621 B) is *below* pcrec's 500,000 default, so a per-mode code bound
would have been an illegal lowering — which is why both configs carry
the same pair, and why `pcrec-auto-bigcap` and `pcrec-vm-bigcap` are one
variable apart from each other exactly as their plain siblings are.

**Composition with `cc`.** `compose_config_extra()` is the one place
`config_extra`'s parts are ordered: the axes in the order they were
chartered (`cc` first, then the caps), joined by `-`. Chartering order
makes the slug APPEND-ONLY, so a testee that already had a token keeps
it where a reader knows it. The schema never learns the parts — X5
derives the id from `config_extra` whole. There is no `-bigcap-clang`
config (BD3's one-variable rule), but the composition is exercised on a
synthesised config and written through `store.write` in
`check_cap_axis`, because a composition nobody has run is a composition
that is wrong.

**`pcrec-local` derives its caps from the EFFECTIVE flags**, the way
`engine_mode` and `captures` already do, so a `$PCREC_LOCAL_FLAGS`
carrying `--max-emit-bytes=` lands in the derived id down the same code
path (`pcrec_local-<digest>_vm-caps-simdna_emitcap-8388608`). A declared
key and a flag may AGREE but never DISAGREE: the value is part of the
id, and an id naming a cap the compile did not run under is worse than
no record.

**What a window will pay for them (MEASURED 2026-09-02; section 2 of the
same measurements file).** The two routes have OPPOSITE cost structures
under the raise, so they need separate budgets: a forced-VM artifact is
straight-line code, emitted in 0.01-0.06 s and costing gcc 5.1-333.8 s;
an auto-route artifact of the same pattern is a table, emitted in
11.0-36.6 s and costing gcc 0.6-1.0 s. gcc is SUPERLINEAR in emitted code
bytes and accelerates, so a rate times a total under-projects badly — a
per-rung sum over altwide@0.2's thirteen wide rungs at five trials is
4,499 s for `pcrec-vm-bigcap` (over the 5,400 s per-cell cap before match
and throughput) and 705 s for `pcrec-auto-bigcap`. The lever that keeps
the trial count is splitting `w-2048` and `s-4096` — 75 % of the VM bill —
into a cell of their own, which leaves the other eleven at 1,143 s.

**Running them.** The bigcap cells belong to `bench/altwide`'s window and
nowhere else — every other set compiles inside the default caps, where a
bigcap testee would measure the same artifact as its plain sibling and be
a trap for a reader. `scripts/run_window.sh` already takes the roster as
`$TESTEES`, and `scripts/run_suite.sh` already takes a per-set
`$TESTEES_altwide` (or a labelled second pass, `altwide:bigcap` with
`$TESTEES_altwide_bigcap`), so no script change is needed.

## The scan-edge deny axis: `-fno-scan-edge` ([B32]; pcrec [OPT-5] / [OPT-EDGE], I-33)

**What the full suite found.** At pin `1989c62` the 29-cell suite turned up
ONE regression family, and it has an exact stamp: every `bench/loglines`
pattern whose artifact stamps a non-`none` `RX_DFA_SCAN_EDGE` is SLOWER
than its pre-[OPT-5] self — `iso-ts` ×1.06 search / ×1.09 throughput,
`http-5xx` and `ipv6` ×1.03-1.09 — and every pattern that stamps `none` is
flat. pcrec's I-33 gives the mechanism: the emitted scan edge costs **one
compare per edge per scan-loop iteration**, so it is the edge COUNT, not
the edge's presence, that predicts the cost.

**Why a testee and not a re-pin.** [OPT-EDGE] needs a BEFORE. Denying the
axis at the SAME COMMIT is the honest one: `-fno-scan-edge` (bit 21)
restores the pre-[OPT-5] machine — the counted run's interior states go
back into the transition table — with the same abi, the same shim, the same
emitted-text fixes, where re-pinning to a7e0bdf's predecessor would move a
dozen things at once. It is the one deny flag on any DFA axis whose denial
changes the MACHINE rather than only emitted text, which is exactly what
lets it stand in for a pin.

**One variable (BD3).** `pcrec-auto-noedge` is `pcrec-auto` plus the flag:
same pin, same `--features all`, same engine mode, same captures, gcc like
its sibling. It derives `pcrec_1989c62_auto-caps-simdna_noedge` — its
sibling's id plus the token.

**No config key of its own.** The flag is spelled in the config's `flags`
list, which is already the ONE list feeding pcrec's argv, `build_flags` and
`runtime_options`; the adapter DERIVES the axis from the effective flags
(`effective_denies`), so a `$PCREC_LOCAL_FLAGS="-fno-scan-edge"` reaches
the derived testee_id down the same code path. Absent, nothing moves: no
flag on the argv, no deny clause in `build_flags`, no `config_extra`, the
same derived id — checked against a FROZEN pre-[B32] renderer and against
every committed record at this pin.

`runtime_options` now treats a **single-dash** token as a flag. pcrec's
generation-axis denials are spelled `-f...`, and under the old `--` test
they were skipped as if they were somebody else's VALUE, so a denied
testee's `runtime_options` would not have said what it denied. No config
that predates [B32] carries a single-dash flag, which `check_noedge_axis`
arm 1(c) proves against a frozen copy of the old renderer.

**Composition.** `noedge` joins `config_extra` LAST, after `cc` and after
the caps: `compose_config_extra` orders the parts by the order the axes
were chartered, so a slug only ever grows by appending.

**The control that matters.** The scan edge DELETES states from the
transition table, so a denial that restored them wrong is the one damage
this testee could do that a timing comparison would happily report as a
speed-up. `check_noedge_axis` therefore runs the denied artifact against
the libpcre2 oracle on both forms of `iso-ts` before it believes any
number from it.

## The scan-edge COUNT: `scan_edges` / `scan_edges_match` ([B32])

Every pcrec compile row that reached emission carries two integer metadata
pairs: how many [OPT-5] SCAN EDGES the artifact's **search-side** machines
carry, and how many its **anchored** one does.

`RX_DFA_SCAN_EDGE` is one token per artifact — it says what SHAPE the edges
took and whether there are any — so it cannot separate `iso-ts` from
`ipv6`, and I-33's mechanism says the difference between them is the whole
effect. These pairs are the regressor.

**How they are counted.** By pcrec's OWN marker: `emit_scan_edge`
(`src/gen/emit_dfa.c`) writes a comment block beside every edge it emits,
once per edge per machine, and both spellings of that block open with
`[OPT-5] SCAN EDGE:`. `scan_edge_counts()` counts those lines in the
emitted C and attributes each to the top-level function it lands in:

| function | bucket | why |
|---|---|---|
| `rx_search` | `scan_edges` | a DFA artifact's own search loop — BOTH scan directions are emitted into it (`iso-ts` puts 4 forward and 4 reverse edges there) |
| `rx_prefilter` | `scan_edges` | a VM HYBRID's inlined candidate-start scan. MEASURED: it is called from `rx_search_run` and from nowhere else, so a hybrid's edges are a cost of the SEARCH band and its `_match` entry (the VM's own body) has none |
| `rx_match` | `scan_edges_match` | the anchored machine |

A marker anywhere else is an `AdapterError`, never a dropped edge: pcrec
moving the loop into a fourth function is precisely the event this
covariate would otherwise mis-attribute, and a mis-attributed covariate is
worse than none.

**0 is a value, and is recorded as one** on every artifact that emitted — a
forced-VM artifact (no DFA scan at all), a `-fno-scan-edge` build, and a
scan with no collapsible run all read 0. A pair that were silently ABSENT
where it reads 0 would turn every regression on it into a comparison of
populations.

**MEASURED at pin 1989c62, 2026-09-02**, and cross-checked against an
independent census over 338 compiles (loglines, email and bounded × both
forms × auto / forced-VM / denied) with zero mismatches — no marker in that
corpus ever landed outside the three functions above. The census is
archived row by row at
`docs/dev/measurements/2026-09-02-scan-edge-attribution-census.txt`:

| artifact | `dfa_scan_edge` | `scan_edges` | `scan_edges_match` |
|---|---|---|---|
| loglines `iso-ts`, `pcrec-auto` | `range` | **8** | **4** |
| loglines `http-5xx`, `pcrec-auto` | `range` | 1 | 1 |
| loglines `ipv6`, `pcrec-auto` | `bitmap` | 1 | 0 |
| loglines `floor`, `pcrec-auto` | `none` | 0 | 0 |
| loglines `iso-ts`, `pcrec-vm` | (absent) | 0 | 0 |
| loglines `iso-ts`, `pcrec-auto-noedge` | `none` | 0 | 0 |
| bounded `cls-upto-16384`, `pcrec-auto` | `range` | 2 | 0 |

The 8 / 4 on `iso-ts` are I-33's own numbers to the letter, which is why it
is the family's worst row.

The REPORTER's column is lane b32rep's; the CONTRACT here is the two pair
NAMES.

## The alternation-island deny axis: `-fno-alt-island` ([B37]; pcrec [ENG-ISL] STEP 1, I-43)

**What the island is.** A flat alternation whose whole subtree matches a
FINITE set of literal byte strings is lowered by the VM as a TRIE over those
strings' bytes — a byte compare at a one-child node, a `switch` at a
many-child node, one try site per node where an alternative ends — instead
of `vm_alt`'s CHAIN of one resume frame per untried branch, where matching
the last of 512 branches cost 511 push/fail/pop round trips on ONE subject
byte (tuning.md §2.20). `RX_VM_ALT_ISLANDS` counts the islands an artifact
took. The island DECLINES, as selection outcomes and never refusals: a
class-leading alternation (a caseless one is class-leading by D23 — `ci-*`
stays [FORM-CHAR]'s), a prefix-bearing one under `VM_ISL_MIN_BRANCHES_PREFIXED`
(4) words, and any island over `VM_ISL_SIZE_FACTOR` (2×) the chain's
estimated size or over the cap.

**Why a testee.** [B37] absorbs SIX abi steps in ONE pin, so "one change
per pin per night" cannot hold for the pin itself; Frank ruled (I-47) the
AFTER is split by DENY FLAG within it. `pcrec-auto-noisland` is
`pcrec-auto` plus `-fno-alt-island` — same pin, same `--features all`,
same engine mode, same captures, gcc like its sibling — so the pair
ISOLATES the island's share on bench/altwide. MEASURED at the re-pin
(2026-09-05, `check_mechanism_stamps` / `check_deny_flag_controls`):

| fact | at 288d505 (chain) | at 334fd10e (island) |
|---|---|---|
| `w-256` vs `srt-256`, forced VM, emit_bytes | 341,201 vs 302,047 | **292,043 vs 292,043** — IDENTICAL (I-43 predicted "within 2 B"); program bytes 305,686 both; only `RX_ALTCLS_FACTORED` (11 vs 57) differs, which the island consumes |
| island / chain code bytes at the SAME pin (`-fno-alt-island` arm) | — | w-256 0.8557, pfx3-256 0.8114, s-256 0.7631 — I-43's 0.856 / 0.812 / 0.764 to three decimals |
| the VM refusal wall | `w-384` REFUSED (508,607 B of code > 500,000) | `w-384` COMPILES at 427,824 B (`shared`, 456,975 program bytes); `w-512` still refused (563,823); `w-384` under `-fno-alt-island` refused again (508,715) — the wall moved 256<w≤384 → **384<w≤512** BECAUSE of the island |
| the DFA route's wall | `w-384` refused at the TOTAL cap (1,431,646) | unmoved: refused at 1,432,392 — the island is a VM lowering the DFA never sees |
| `foo\|bar` forced VM (the deny control) | framed, 18,783 B | islands 1, `vm_frameless` 1, `forward`, 1,532 program bytes, 18,611 B → denied: islands 0, frameless 0, `plain`, 1,233 / 18,881 B — FOUR pairs move with the lowering |
| level-context under `auto` (the [SEL-1] hybrid) | — | islands **2** (a count, not a boolean); denied: 0 |

**What the denial changes besides the dispatch.** A PREFIX-FREE island's
candidate chain has one entry and pushes nothing, so an artifact that
takes it comes out `vm_frameless 1` where the chain's was 0 — and a framed
artifact is `vm_entry_shape plain` by construction (abi 22). A `noisland`
row therefore differs from its sibling in the program, the frame discipline
AND the entry chain together, which is exactly what the pre-[ENG-ISL]
machine was; the pair is answer-identical "modulo which budget binds" (I-43:
a budget-bound cell may differ in the island's favour only, since the
island does strictly less stepping).

**One variable (BD3), no config key of its own, composition.** The same
shape as `pcrec-auto-noedge`: the flag rides in `flags`, the adapter
derives the axis (`effective_denies`, the `DENY_FLAGS` row), and `noisland`
joins `config_extra` in chartering order — after `cc`, the caps, `noedge`
and `nopin` — so a slug only ever grows by appending.
`$PCREC_LOCAL_FLAGS="-fno-alt-island"` reaches the derived testee_id down
the same code path.

## The compilee-flags axis: `cflags` ([B35]; pcrec inbox I-39 (v))

pcrec is an ahead-of-time compiler: it emits C and stops. Whoever runs a C
compiler on that emitted C decides how the compiled FUNCTION lands in
memory — alignment, layout — and that is US, the adapter's phase 2, exactly
as `cc` ([B24]) already says WHICH compiler runs. `cflags` says what EXTRA
flags that compiler gets, for our own phase-2 compile only:

    cflags = ["-falign-functions=64", ...]      # optional, per config, a LIST

**Why.** pcrec's inbox I-39 (v) is a layout probe for a disputed cell —
`floor` / match / `auto` — where gcc read 503.3 ns on this bench and
307 ns in pcrec's own hand harness, on BYTE-IDENTICAL artifacts (clang
matched to within 1.4 %). A 48-instruction loop straddling a 64-byte cache
line can cost exactly that ratio depending on where the compiler happens
to land it, and `-falign-functions=64` pins the landing so the before/
after can be read without re-pinning pcrec or changing one byte of what
it emits. `pcrec-auto-align64` is `pcrec-auto` plus the flag: same pin,
same `--features all`, same engine mode, same captures, gcc like its
sibling — one variable moved, and it is the COMPILER's, not pcrec's.

**These flags are NEVER passed to pcrec.** pcrec's own `flags` (its argv —
`--features all`, `--engine=`, the [B31] cap raises, the [B32] denials) is
a wholly different list; `cflags` rides on `_compile_one`'s phase-2 argv
only (`$CC -O2 -fPIC -shared <cflags> shim.c`, which `#include`s the
artifact, so the artifact and the shim always get the same extra flags and
can never drift apart). A config may carry `cflags` and any of the other
axes independently.

**The driver does not move.** `build_driver()` still builds `driver.c`
from `$CC` with no extra flags on every config, so an aligned testee
differs from its plain sibling in exactly ONE variable — the artifact+shim
compile — the same one-variable shape `cc` already has for the compiler
choice itself.

**Absent** means today's behaviour byte for byte: no extra token on the
REAL argv, no clause in `build_flags`, no `config_extra`, the same derived
`testee_id` — checked against a FROZEN pre-[B35] shape and against every
committed record at this pin (`check_cflags_axis` arm 1).

**Present** is an identity claim, and three things follow:

- the flags join `build_flags` NAMED (`adapter.py`'s `cflags_note`) rather
  than silently folded into the fixed `-O2 -fPIC -shared` text, so a
  reader does not have to diff two `build_flags` strings to see WHAT moved;
- a deterministic slug token joins `config_extra` LAST — after `cc`, the
  [B31] caps and the [B32] denials, `compose_config_extra`'s own
  chartering-order rule — computed by `cflags_token`: strip leading
  dashes, then a leading bare `f` immediately followed by a letter (GCC/
  clang's `-f<name>` family — the same one the [B32] deny words already
  strip: `-fno-scan-edge` → `noedge`), replace every run of characters
  outside `[a-z0-9]` with `-`, trim, and prefix `cf-`.
  `-falign-functions=64` → `cf-align-functions-64`;
- and `runtime_options` is UNCHANGED — these are our own compile flags,
  never one of pcrec's own option names, so they never appear there
  (unlike the [B32] deny flags, which are pcrec's own argv and do).

**`pcrec-local` derives this axis from a CONFIG KEY only, never from an
environment variable.** `$PCREC_LOCAL_FLAGS` is pcrec's own argv (what
`engine_mode` / `captures` / the caps / the denials all read from), not
the compilee toolchain's, so there is no local equivalent to widen — a
provided binary compiles under whatever `cflags` its OWN `configs.toml`
entry (if any) declares, exactly like every other testee. `pcrec-local`'s
entry declares none, so it is unaffected by this axis by construction,
the same way it is unaffected by `cc`.

`make check-harness`'s `check_cflags_axis` proves: the twelve pre-[B35]
configs untouched (argv, `build_flags`, id, and every committed record's
`build_flags` re-deriving byte-identically); `pcrec-auto-align64` carrying
the token, the clause and the flag, one variable apart from `pcrec-auto`,
with NO clause in `runtime_options`; a REAL compile watched at the
`subprocess` boundary — the flag present in the actual `gcc`/`clang` argv,
positioned between `-shared` and `-o`, and ABSENT from pcrec's own argv on
the same compile; the aligned artifact answering a hand-built smoke set
exactly as the libpcre2 oracle does (the control — an alignment flag that
broke codegen would otherwise pass as a speed change); one whole cell into
a scratch store with the token reaching the written record; and
`python3 -m pcrecbench testees` listing the new config.

## `shim.c` includes the artifact's `.c`, and that is load-bearing

`driver.c` must not re-declare `struct rx_info` or the `<prefix>_*`
signatures — a second, drifting copy of somebody else's ABI is exactly the
failure pcrec's own `pcre2_abi.h` header comment was written about. So the
shim is compiled as ONE translation unit with the artifact and exports a
flat `pb_*` surface in terms of nothing but `<stddef.h>` types.

It includes the artifact's **`.c`**, not its `.h`, because the D46
observability stamps (`RX_ENGINE`, `RX_VM_PREFILTER`, `RX_VM_RUNGS`,
`RX_VM_STRATS`, `RX_VM_PRUNES`) are emitted into the `.c` only and never into
the `.h` (pcrec `docs/spec/match_api.md` §1, §6.3). MEASURED: a header-only
shim compiled cleanly and reported a VM artifact as carrying no mechanism
stamps at all.

## The compile-cost definition — AOT, three phases

`emit-c` (the pcrec CLI) → `gcc` (shim + artifact into a `.so`) → `load`
(dlopen). **Each trial builds its own `artifact-<trial>.so`**: the dynamic
loader caches by path, so a repeated dlopen of one path measures the cache
and not the load.

**A REFUSAL carries a cost too (KB-4, docs/dev/known_issues.md, fixed
2026-09-01, [B28]).** pcrec prints no timing on any path and has no exit
convention beyond 0/1 (inbox I-20), so a refused compile's cost is the
BENCH's own clock around the pcrec exec — `_compile_one` times phase 1
(`emit-c`) regardless of exit code and carries that number forward on
BOTH `did-not-compile` paths: pcrec's own refusal (e.g. the bounded
`cls-upto-65535` rung, `NFA exceeds 131072 states`) and a compiler
refusal one phase later (pcrec succeeded; only gcc/clang refused — see
"A clang refusal is a first-class outcome" above). The record row's
`cost` carries `total_ns` ONLY, never a `cost.phases` array: rule X12
requires `phases[].name` to equal `compile_phases` EXACTLY when the key
is present at all, and a refusal never ran every declared phase.

## The MATCH regime uses a SECOND artifact — `(?:<pattern>)\z`

RULED by the manager, 2026-08-25, from the pcrec manager: pcrec has no
`PCRE2_ENDANCHORED` equivalent (a ratified but UNBUILT generation axis,
pcrec [OS-4]; this bench is recorded there as its first customer), so the
match/compliance regime compiles a SECOND artifact from `(?:<pattern>)\z`
and uses the anchored entry on it. `search_short` and `throughput` use the
PLAIN artifact. The two forms never share a row: schema v1.1's `form` enum
(`plain` | `whole-subject`) labels compile and match rows, and pcrec emits
compile rows for BOTH forms of every pattern, both timed, all phases.

`\z` and not `$`: at `options = 0`, `$` also matches before a final
newline, so `$` would silently accept a subject with a trailing `\n` that
the oracle rejects. `(?:...)` and not bare concatenation: a top-level
alternation would otherwise bind only its last branch to the anchor.

### MEASURED against pin 692c2e8, 2026-08-25 — verified, not assumed

Re-measured at the re-pin (pcrec's [DD-14] close merge; its compiler is
byte-identical to 17469b6, the [DD-14.FB] merge). "Emitted C" is the byte
size of the `artifact.c` that `pcrec -p rx <flags> -o artifact.c -- <text>`
writes.

**It DOES depend on the output file's BASENAME, by exactly that name's
length** — corrected [B16], 2026-08-28; this sentence used to end "it does
not embed the output path", which is true of the DIRECTORY and false of
the name. In the split form the CLI produces by default, the `.c` opens
with `#include "<basename>.h"`, so `-o a.c` and `-o aaaaaaaaaa.c` on one
pattern at one pin differ by 9 bytes — the difference in the names.
MEASURED at 692c2e8 as well as 35e1ab1, so it is long-standing, not new.
The consequence for anyone re-deriving these tables: use the SAME output
basename throughout, as every row here does (`artifact.c`) — which is why
the 692c2e8 column of the re-measurement below reproduces this table to
the byte.

| pattern / form | config | engine | ncaps | emitted C |
|---|---|---|---|---|
| `orig` plain | auto | **dfa** | 1 | 44 786 B |
| `orig` `\z` | auto | **dfa** | 1 | 50 199 B |
| `orig` plain / `\z` | nocaps | dfa | 1 | 44 786 / 50 199 B |
| `orig` plain / `\z` | vm | vm | 1 | 52 521 / 52 651 B |
| `factored` plain | auto | **dfa** (was vm at 8da6120) | 5 | 45 453 B |
| `factored` `\z` | auto | **dfa** (was vm at 8da6120) | 5 | 50 866 B |
| `factored` plain / `\z` | nocaps | **dfa** (was vm) | 1 | 45 076 / 50 489 B |
| `factored` plain / `\z` | vm | vm | 5 | 65 288 / 65 416 B |

**THE HEADLINE CHANGE vs 8da6120: `factored` now compiles to a DFA
artifact under `auto` AND `nocaps`, in both forms.** pcrec's wave G
([DD-14.G], merged at 08ddcbd: "dead-capture elision, prefilter restored
for call-bearing patterns") is what did it — at 8da6120 the `{0}` callee
groups were captures and forced the VM (`engine_why`: "capture group at
pattern offset 3"); at 692c2e8 the four named groups are still reported
(`ngroups` 4, `nnames` 4, `ncaps` 5 under captures-on) but the artifact is
`engine = 1`, `frame_capacity = -1`, and every frame-sizing field stamps
`0`. Consequences a reader of before/after numbers must hold in mind:

1. **`pcrec-auto` and `pcrec-nocaps` no longer give up anywhere on
   `bench/email`.** MEASURED (smoke, `--trials 1 --iters 1`, match
   regime): `pcrec-auto` at 692c2e8 answers 170/170 `matched-as-expected`;
   at 8da6120 the same cell had 5 `gave-up` (`PCREC_ERR_FRAMES`) rows on
   `factored` whole-subject (s-058, s-059, s-061, s-063, s-064). Those
   five are NOT fixed by a bigger buffer; they are fixed by a different
   engine. A before/after on `factored` under `auto` compares a VM
   artifact with a DFA artifact, not one engine's two versions.
2. **`pcrec-vm` still gives up on exactly those five** (MEASURED, same
   smoke: 5 × `giveup:-3:PCREC_ERR_FRAMES`, all `factored`
   whole-subject), so the VM-forced config is the only one on this
   sub-bench where the frame budget — and the `_in` caller-provided
   buffer — is reachable at all.
3. **`orig`'s `\z` form still selects the DFA** under `auto` and `nocaps`
   (unchanged), and now so does `factored`'s.
4. **`abi` reads 3** (was 2): `rx_info` gained `resume_frames`,
   `trail_frames`, `resume_frame_size`, `trail_frame_size` ([DD-14.FB],
   §10.4). Nothing in this adapter hardcodes the number; CONFIRMED from
   the smoke record's `engine_metadata.abi == 3` on all four compile rows.
5. **The give-up bounds did NOT change**: `PCREC_ERR_FLOOR` -5, top -2,
   `PCREC_ERR_INTERNAL` -6, read from the emitted header at 692c2e8.
   `PCREC_ERR_RECURSE` (-5) is still "reserved: no producer yet".
6. **The byte-class skip prefilter** is present on all four DFA `auto`
   artifacts and its `rx_can_begin_match` table is BYTE-IDENTICAL between
   `orig` and `factored` (same sha256 over the table body per form:
   `6404d2dc…` plain, `7164c398…` `\z`). The skip-LOOP asymmetry stands:
   the plain form skips while `scan_position < subject_length`, the `\z`
   form only while `scan_position + 1 < subject_length` — the `\z`
   prefilter can never skip the final byte. Do not read a plain-vs-`\z`
   difference as an engine-selection effect.
7. The `\z` form costs **+12.1 % emitted C** on `orig` and **+11.9 %** on
   `factored` (both DFA now; at 8da6120 `factored` was VM and paid +0.3 %).
   `RX_ALTCLS_FACTORED` stamps 2 on `orig` and 1 on `factored`.
8. **`\z` requires pcrec's `assertions` module** and `factored` still
   requires `named-groups` under the default `std1` set (re-verified at
   692c2e8: "(?<...) requires module 'named-groups' (pattern offset 3)").
   Every config passes `--features all`, so nothing changed.

### The gap this measurement found — CLOSED at the 35e1ab1 re-pin

**It said: the DFA prefilter is NOT observable through any structured
stamp, so `engine_metadata` cannot say whether it is on.** The prefilter's
presence had to be established by reading the emitted skip LOOP — prose
and code, not a stamp — which is exactly what requirements §4.2 says a
metadata pair must not be built from, while §4.2 also wants reports to
"bucket outliers by MECHANISM". It was filed to the pcrec manager, came
back as pcrec's inbox I-3, and closed as [DD-13] / [DD-13c] / [OPT-3]:
`RX_DFA_SCAN`, `RX_DFA_PREFILTER` and `RX_DFA_TABLE` are on every
artifact that CONTAINS a DFA scan — VM HYBRIDS included — and
`rx_info.scan` / `.prefilter` mirror the first two at run time. **Every
pcrec record at this pin can be filtered on its candidate-start
mechanism**, from a structured field, on both engines. See "The mechanism
stamps" below.

The part worth keeping after the closure: the VM HYBRID is the artifact
kind where the DFA scan does the WORK (the email specimen's ~23×), and it
was the one kind that could stamp nothing about it until [DD-13c]. A
bench that had settled for "DFA artifacts only" would have bucketed every
artifact by scan shape EXCEPT the ones that needed it.

## `consumed_length`, and the MATCH-regime asymmetry you must know about

`consumed_length` is the subject length the artifact's entry was given and
accepted. `<prefix>_search` takes a `size_t n` and exposes no scan
high-water mark — same convention, and same caveat, as `testees/pcre2/`.

**The one real semantic gap.** The `match` regime is whole-subject:
`PCRE2_ANCHORED | PCRE2_ENDANCHORED`. pcrec has no end-anchor option, so the
driver answers the question as `<prefix>_match_caps(...) == n`. That is a
SUFFICIENT test, not a necessary one: a pattern whose leftmost-first anchored
match is a strict prefix, but which could reach the subject's end by
backtracking, answers *no* here where PCRE2 answers *yes*. Such a
disagreement would be recorded as `did-not-match-as-expected` — a finding
about the harness, not about pcrec. **MEASURED on `bench/email`: it does not
bite. `pcrec-auto` answers 85/85 as expected on `orig` in the match regime.**
Reported to the manager as a contract gap for a future sub-bench.

## The `_in` path: the caller-provided frame buffer (pcrec match_api.md §10)

pcrec's generated matcher never allocates (§5.2): the VM's resume stack
and its undo trail are sized at compile time (`RX_RESUME_FRAMES` 2048 /
`RX_TRAIL_FRAMES` 3072 by default) and live in the entry's own stack frame,
so a deep subject returns `PCREC_ERR_FRAMES` in constant time rather than
recursing. [DD-14.FB] (pcrec 17469b6, in this pin) lets the CALLER supply
that storage instead: every artifact exports `<prefix>_search_in`,
`<prefix>_match_in`, `<prefix>_match_caps_in`, each its un-suffixed sibling
plus one argument, a descriptor

    typedef struct { void *frames; size_t nframes;   /* CAPACITY in frames */
                     void *trail;  size_t ntrail; }  /* capacity in ENTRIES */
    rx_buffers;

**The counts are capacities, not bytes** (§10.2). Both regions are required
when the descriptor is non-NULL, and pcrec's own measurement says why a
frames-only knob would be inert: on `^(a(?1)?b)$` the TRAIL binds first, at
~9 entries per nesting level against ~2 frames, so the default runs out of
trail with two thirds of the resume stack unused (pcrec
`docs/design/frame_buffer_design.md` §4). This bench's measurement below
found the same ~4.5 : 1 ratio on the email pattern.

### The four promises of §10.3 this adapter relies on

1. **`buf == NULL` IS the plain call** — "not similar to, the same call".
   The driver's no-option path calls the plain entries anyway, so the
   existing configs' output is byte-identical to before the feature.
2. **A give-up is retryable** and the buffers are **pure scratch**: nothing
   survives a call, nothing needs re-initialising, so ONE pair of regions
   per driver run, reused across every subject and iteration, is correct.
3. **`PCREC_ERR_FRAMES` does not say whose buffer ran out**, and the count
   that would have sufficed is not reported. Sizing is therefore by
   measurement (below), and a give-up under a caller buffer is recorded
   exactly as one under the default — same code, same `gave-up` outcome.
4. **On a DFA artifact the surface is present and inert**, and every
   sizing field stamps `0` — "this engine takes no buffers". §10.4's
   documented mistake is dividing by that 0; `driver.c` tests the size
   first and, when it is 0, allocates nothing, prints
   `info buffer_inert stamped-size-0`, and runs the plain path. That is
   why `pcrec-auto-in` on `bench/email` at 692c2e8 records no
   `buffer_frames` pair on any compile row: all four artifacts are DFA.

### Where the pieces live

- **`shim.c`** builds the descriptor (it is the one file that knows the
  type) and exports `pb_search_in(...)` / `pb_match_caps_in(...)` taking
  `(frames, nframes, trail, ntrail)`, plus the sizing surface READ from
  the artifact's own macros — `pb_buffer_align()`, `pb_resume_frames()`,
  `pb_trail_frames()` (the stamped defaults), `pb_resume_frame_size()`,
  `pb_trail_frame_size()` (per-artifact bytes; never hardcoded — pcrec
  documents 24 on a call-free and 40 on a call-bearing VM artifact, and
  the email `factored` VM artifact at 692c2e8 stamps **24**, see the
  findings). Everything is `#ifdef RX_BUFFER_ALIGN`-guarded: against a
  pre-FB artifact `pb_has_in_entries()` is 0, the sizes are 0, and the
  `_in` wrappers return `PB_UNSUPPORTED` (-1000000, below every pcrec
  code) — which the driver never reaches because it refuses `--buffer-*`
  on such an artifact up front.
- **`driver.c`**: `--buffer-frames N --buffer-trail M` (both or neither).
  Allocates once per run, `posix_memalign` to `pb_buffer_align()`, sized
  `N × resume_frame_size` and `M × trail_frame_size` bytes, and touches
  every page once OUTSIDE any timed loop so the first subject does not pay
  page faults for storage the match may never fill. Then the `_in` entries
  in all three modes — search, find-all, match — with the same protocol
  lines and the same give-up propagation. Prints `info resume_frames /
  trail_frames / resume_frame_size / trail_frame_size / buffer_align`
  whenever the artifact stamps them, and `info buffer_frames /
  buffer_trail` ONLY when the regions were allocated and used.
- **`adapter.py`**: `buffer_capacities(cfg)` validates the config (both
  or neither, positive integers), `buffer_args()` turns it into driver
  argv, which rides on the load-only run (so the compile row's
  `engine_metadata` says what ran) and on every `measure()` call. The
  declaration gains the six integer pairs; `describe()` puts the
  capacities in `build_flags` and `runtime_options`. The `engine_mode`
  slug (`auto-in`, `vm-in`) is what makes the derived `testee_id`
  distinct: `pcrec_692c2e8_vm-in-caps-simdna`.

### The measurement that chose 32768 / 131072 (pin 692c2e8, 2026-08-25)

On the VM artifact of `factored`'s `\z` form (the match regime's), the
five subjects that give up at the stamped default were binary-searched for
the smallest capacity of each array that matches, with the other held at
4 194 304 (`--trials 1 --iters 1`, a smoke's settings — these are
capacities, not timings):

| subject | bytes | what it is | smallest frames | smallest trail |
|---|---|---|---|---|
| s-058 | 4 011 | 2000-deep dotted local part | 4 005 | 20 020 |
| s-059 | 5 134 | 5 KB quoted string of qchars | **10 245** | **46 100** |
| s-061 | 2 008 | 500-label domain | 1 504 | 5 020 |
| s-063 | 5 135 | 5 KB quoted string, unescaped quote (expected `nomatch`) | 5 122 | 23 044 |
| s-064 | 4 110 | alternating escaped chars, 4 KB | 2 053 | 18 452 |

Trail/frames is 4.5 on every row (pcrec's ratio); the per-byte cost is
~2 frames and ~9 trail entries on the quoted-string subjects and ~1 / ~5
on the dotted and labelled ones. Power-of-two sweep on all five at once:
2048/3072 (the default) 0 of 5 answered; 4096/8192 → 1; 8192/16384 → 1;
16384/32768 → 4 (s-059 still short on TRAIL); **16384/65536 → 5 of 5**,
the smallest power-of-two pair; **32768/131072** is one doubling above it
and is the config: 32768 × 24 B + 131072 × 16 B = 2.75 MiB per run.
Every answer at those sizes agrees with the oracle's expectation (four
`match` over the whole subject, s-063 `nomatch`).

What the buffer does NOT fix, measured on the same artifacts:
`t-c-long-atom-run` (1 MB of `a`, no `@`) gives up `PCREC_ERR_STEPS` in
the throughput regime with or without the buffer — a step budget, not a
frame budget — and stays a `gave-up` row on every VM config.

## Give-ups

A budget give-up propagates to the driver as
`giveup:<code>:<NAME>` (e.g. `giveup:-3:PCREC_ERR_FRAMES`) and is not timed.

**Classification is by RANGE, never by a list** (ruled 2026-08-25): a
negative return is a give-up iff it lies in `[PCREC_ERR_FLOOR, -2]`, and
`shim.c` exports `pb_err_floor()` / `pb_err_giveup_top()` /
`pb_err_internal()` / `pb_err_name()` so the bounds come from the artifact
itself. Anything strictly below the floor — `PCREC_ERR_INTERNAL` (-6),
which the artifact states outright is not a give-up — is `crashed`. A
give-up code pcrec adds later is then classified correctly with no adapter
edit, and a reserved code can never be laundered into `gave-up`.

MEASURED at pin 692c2e8 (unchanged since 8da6120): floor -5, top -2, internal -6. `PCREC_ERR_WORK`
(-4) is inside the range; `PCREC_ERR_RECURSE` (-5) is inside it but has no
producer yet. Schema v1.1 gives these rows their own `gave-up` outcome;
until it lands they are `did-not-match-as-expected` — see
`bench/email/NOTES.md`.

## Engine metadata

From STRUCTURED fields only (requirements §4.2): `rx_info`'s
`abi`/`ncaps`/`ngroups`/`nnames`/`engine`/`step_budget`/`work_budget`/
`frame_capacity`/`subject_ceiling`, plus the VM-only stamps `prefilter`,
`vm_rungs`, `vm_strats`, `vm_prunes` — the three masks recorded as ARRAYS OF
BIT NAMES, never integers (record_schema.md §7 rule 3). A mask bit the
adapter has no name for is a hard error, not a silently dropped bit.

The prose `RX_ENGINE_WHY` is **not** a metadata pair: it goes into the
compile row's unindexed `diagnostic`, exactly where record_schema.md §7 puts
it.

### The mechanism stamps, and the two rules for reading them ([B16], abi 8)

pcrec grew five pins of observability between this bench's 692c2e8 pin and
`35e1ab1`, absorbed here in ONE adapter change (pcrec asked for one rather
than five). What arrived, and where each pair comes from:

| pcrec abi | what appeared | pairs recorded here |
|---|---|---|
| 4 ([DD-13]) | `RX_ENGINE` on EVERY artifact; `RX_DFA_SCAN` / `RX_DFA_PREFILTER` on DFA artifacts | `dfa_scan`, `dfa_prefilter` (and `RX_ENGINE` as `engine`'s control) |
| 5 ([OPT-1]) | `RX_FAST_FRAMES` / `RX_FAST_TRAIL` on every VM artifact | `fast_frames`, `fast_trail` |
| 6 ([DD-13c]) | `RX_DFA_SCAN "empty"`; the two `_DFA_*` macros extended to VM HYBRIDS; `rx_info.scan` / `.prefilter` appended | (the fields are CONTROLS, not pairs) |
| 7 ([OPT-3]) | `RX_DFA_TABLE` | `dfa_table` |
| 8 ([ENG-FORM]) | nothing a consumer reads — the emitted scan loop moved | — |
| 9 ([OPT-K], [B18]) | `RX_DFA_PREFILTER` gains `offset-set` / `offset-set-bounded`; `RX_DFA_PREFILTER_OFFSETS` (`"0,8*,13"` / `"none"`) on every artifact that contains a DFA scan; `-fno-offset-skip` (bit 16) | `dfa_prefilter_offsets` (a `string` pair: a fact about the machine, not a closed set) |
| 10 ([ENG-ABS], [B18]) | `RX_DFA_MATCH` (`unwrapped` / `search-filter`) on every DFA artifact and NO VM artifact, hybrids included; `rx_info.match_form` appended (NULL where the macro is absent); `-fno-anchored-dfa` (bit 17) | `dfa_match` (the field is its CONTROL, and it raised the shim's floor to 10) |
| 11 ([ART-SIZE], [B18]) | `RX_UNROLL_K` / `RX_UNROLL_K_WHY` (seven values) / `RX_MAX_EMIT_CODE_BYTES` on every VM artifact; `RX_MAX_EMIT_BYTES` on every artifact; `-fno-size-term` (bit 18) denies the K selection, never the caps | `unroll_k`, `unroll_k_why`, `max_emit_code_bytes`, `max_emit_bytes` |
| 12 ([OPT-4], [B19]) | `RX_ENGINE_SEL` on EVERY artifact (one `engine-route` token: `selected` / `forced` / `overflowed-dfa` / `overflowed-prefilter` / `collapsed-prefilter` — O-8 6(d) ruled as a stamp); `RX_VM_PREFILTER_LANG` (`exact` / `count-collapsed`) + `RX_VM_PREFILTER_LANG_WHY` on every VM HYBRID and no other artifact; `-fno-prefilter-collapse` (bit 19) denies both retry rungs, `-fprefilter-collapse` (bit 20) forces the collapse; `--warn-emit-bytes=N` (advisory stderr line, default 250,000) | `engine_sel`, `vm_prefilter_lang`, `vm_prefilter_lang_why` (a `string`: two of its values carry a number) — and the adapter's own `emit_bytes` / `emit_code_bytes` (pcrec's size definition, ported and controlled) + `warned_emit_bytes` (present only when the warning fired) |
| 14 ([OPT-4.2] + [CC-CLANG], [B26]) | `RX_ENGINE_SEL` gains an EIGHTH value, `declined-nullable-default` — the nullability decline with NO RUNG: nothing overflowed, and the ORDINARY hybrid's own EXACT prefilter language is nullable, so the prefilter is declined. Such an artifact reads `RX_VM_PREFILTER "none"` and carries NO language pair (match_api.md §6.3's iff both ways). NO new stamp and no new axis; the `--list-axes` `engine-route` row joins at ORDER 2 (right after `forced`), renumbering the six below it. [CC-CLANG] rides the same abi with no stamp at all: its `&&label` fix is why the clang refusal set goes EMPTY here | `engine_sel` (a new VALUE in an existing pair) |
| 15 ([DD-13b.W1.2], [B26]) | `rx_info.name` and `rx_info.nentries` APPENDED after `match_form` — read-only additions, no member's offset moved. `name` is what the ARTIFACT is (as against `<prefix>`, what its symbols are CALLED); NEVER NULL by contract. `nentries` is the WHOLE `groups[]` length, of which `nnames` counts a PREFIX. NEITHER has a macro spelling | `artifact_name`, `nentries` — PROVENANCE pairs, and **the fields that raised the shim's floor to 15** |
| 16 ([OPT-5] STEP 2, [B34], pin 288d505, 2026-09-03) | `RX_DFA_START` (`pinned` / `reverse-pass` — a SELECTION FACT, match_api.md §6.3: whether the search entry is start-pinned or runs the reverse pass), `rx_info.search_form` APPENDED after `nentries` (guarded on has-dfa-scan, so hybrids stamp it; read by value off the driver beside `match_form`), `RX_VM_FRAMELESS` (0/1, VM route, unconditional — what the program CONTAINS, not what it was SIZED for: it agrees with `resume_frames == 1` on all 170 corpus VM artifacts but the `(?=abc)x+` witnesses stamp 1 with RX_RESUME_FRAMES 2 — the [B32] grep it replaces was run one last time against it, 18/18), `-fno-start-pinned` (bit 22, masked out of rx_info.flags — the deny control: cls-upto-2048 whole moves `pinned` → `reverse-pass`, 16,307 → 19,807 B, scan_edges 1 → 2), `RX_ALTCLS_MERGES` / `RX_ALTCLS_FACTORED` (pcrec I-39: in the COMMON stamp block since [OPT-ALTCLS], emitted before either engine is built — DFA and VM alike, a `--no-captures` build included; this shim started reading them at this pin, though pcrec has stamped them unconditionally since long before it) | `dfa_start`, `search_form`, `vm_frameless`, `altcls_merges`, `altcls_factored` — **`search_form` is the field that raises the floor to 16; the ALTCLS pair has no field mirror and does not**. Size: a pinned artifact −3,392 B total on cls-upto-16384 (16,554 → 13,162; code 13,214 → 11,492), a plain VM artifact +90 B (+51 .c, +39 .h); the −fno-scan-edge deny row roughly halved (724,939 → 367,390 B denied) because both arms are now pinned. **ALTCLS MEASURED** (`check_mechanism_stamps`, [B34] follow-up): `altcls_merges` is engine-independent (the SAME pattern reads the SAME count under `auto` and under `--engine=vm` — the pass runs before engine selection forks) and reaches both 0 and 1 on real artifacts (`a(b|c)+d`'s `(b|c)` merges to one class); bench/altwide's ORDER PAIR `w-256`/`srt-256` (identical 256 branches, generation vs sorted order — the 2026-09-03 ledger's `srt-256` ×8.87-faster-on-the-VM pair) compile to DFA artifacts that are byte-for-byte IDENTICAL except the embedded pattern-text comments and ONE line: `RX_ALTCLS_FACTORED` 11 (`w-256`) vs 57 (`srt-256`) — subset construction canonicalises the machine regardless of source order, so the factoring count is a fact about the REWRITE and not about the artifact it feeds; `sh1-64` (every branch starts `k`) factors into 3 runs, not 1 (`PCREC_MAX_ALTCLS_FACTOR_DEPTH`'s own cap); `floor` (no alternation) reads 0/0. bench/altwide/NOTES.md's **P1 HOLDS**: `altcls_merges` is 0 on every altwide witness measured |
| 13 ([OPT-5] STEP 1, [B25]) | `RX_DFA_SCAN_EDGE` (`range` / `bitmap` / `mixed` / `none`) on every artifact that CONTAINS a DFA scan — the scan family's iff, joined unchanged (match_api.md §6.3); the SCAN EDGE is a maximal run of states differing only in how many bytes of ONE fixed class have been counted, replaced by a bounded cursor loop and DELETED from the transition table (the first abi bump to move a MACHINE, not only emitted text — tuning.md §2.18); TWO registry axes (`scan-edge` per state, `scan-body` per edge); `-fno-scan-edge` (bit 21) denies the per-state axis and restores the pre-[OPT-5] machine; `PCREC_MAX_SCAN_EDGES` (4) joins `--list-limits` | `dfa_scan_edge` (the `scan-body` axis's value; no rx_info mirror) |
| 17 ([CC-DIFF] STEP 1, [B37], pin 334fd10e, 2026-09-05) | `RX_DFA_UNIFORM_FOLDS` — an INTEGER 0..6 on every artifact that CONTAINS a DFA scan (RX_DFA_TABLE's own scope, the scan family's iff a FOURTH time): how many of the artifact's DFA tables (`<m>_next_state` / `<m>_is_accepting`, two per machine it contains) had ALL-EQUAL cells and were NOT EMITTED, the accessor returning the constant. `RX_DFA_TABLE` keeps naming the encoding SELECTED, so `premultiplied` + folds 4 is an artifact with no transition table. Family (b) (discovered while emitting), a COUNT not a mask. The same step put `always_inline` on the frameless VM helpers (no stamp of its own; `RX_VM_FRAMELESS 1` now means ELIGIBLE, abi 22's shape stamp says what was emitted). No rx_info mirror; the floor does not move | `dfa_uniform_folds` (MEASURED: 4 on a pinned `unwrapped` rung, 2 on the pinned `search-filter` 16384 rung, 6 under `-fno-start-pinned`, 0 on every reverse-pass corpus DFA; a folds-4 artifact's `-O2` object carries NO `.rodata` section) |
| 18 ([ENG-ISL] STEP 1, [B37]) | `RX_VM_ALT_ISLANDS` — a COUNT on every VM artifact, hybrids included, never on a DFA one: how many flat alternations the VM lowered as an ALTERNATION ISLAND (a trie over the alternatives' literal bytes, tuning.md §2.20) rather than as vm_alt's serial resume chain; selected PER ALTERNATION on its LANGUAGE (a finite literal set within the enumeration budget), declining class-leading, prefix-bearing-under-four-words and over-budget alternations as selection outcomes. The FIRST abi bump whose change reaches the VM PROGRAM region. `-fno-alt-island` (bit 23) denies it; the registry gains the `alt-island` axis (two `predicate` rows, no stamp_value: 72/24 → 74/25) and `--list-limits` nine `VM_ISL_*` knees/budgets | `vm_alt_islands` (MEASURED: 1 on every altwide VM form incl. w-384, 0 on `floor`; 2 on level-context's and ctx-greedy-256's [SEL-1] hybrids under `auto`; the deny control on `foo\|bar` moves islands 1→0, frameless 1→0, shape forward→plain) |
| 19 / 21 ([OPT-EDGE] STEP 1 / 1.1, [B37]) | NO NEW STAMP: the scan-edge ENTRY DISPATCH (edge heads renumbered to the machine's top rows, one `<m>_is_stop` accessor, the per-edge blocks moved off the generic path; 1.1 narrowed precondition (8) and generalised the entry seed to `is_stop && !is_dead`). An edge-bearing machine's state NUMBERS and loop shape move; an edge-free artifact is byte-identical. `PCREC_MIN_SCAN_CHAIN` 2 joins `--list-limits`; `PCREC_MAX_SCAN_EDGES`'s desc is reworded (an edge costs NO compare on the generic path now) | — (the `scan_edges` / `scan_edges_match` covariate reader survives: the `[OPT-5] SCAN EDGE:` marker still sits inside `rx_search` / `rx_match`, iso-ts reads 8/4 at this pin as at 288d505) |
| 20 ([DD-13b.W1.3], [B37]) | NO NEW STAMP: .rxt COMPOSITION — on a `--source` compile `groups[]` gains rows the target did not declare, `nentries` counts the whole array, `nnames` the caller-scope prefix. Invisible on every non-composed compile, which is all this adapter does (`-p rx` from pattern text): `nentries == nnames` still holds by value | — |
| 22 ([CC-DIFF] STEP 2 + [OPT-DIAL] STEP 0, [B37]) | `RX_VM_ENTRY_SHAPE` (a CLOSED TOKEN: `plain` / `shared` / `forward` / `inline` — the entry-chain rung the emitter TOOK, tuning.md §2.21) and `RX_VM_PROGRAM_BYTES` (the emitted VM program size, THE quantity AUTO compared against `VM_INLINE_CHAIN_MAX_BYTES` 4,096 to choose the rung: `forward` at or below, `shared` above; `inline`/`plain` where a forward rung is illegal because the program WRITES its storage — an RX_SET is enough; a FRAMED program is `plain` whatever is asked). Both on every VM artifact, hybrids included, never on a DFA one. NOT a flags bit (`--vm-entry-shape=N` is an ordinal option): no deny row, no registry axis — the four tokens are declared from match_api.md §6.3's own enum. No rx_info mirror; **the floor STAYS 16** (struct rx_info gained no member across abi 17-22) | `vm_entry_shape`, `vm_program_bytes` (MEASURED at each token: `forward` foo\|bar 1,532 B / floor 236 B; `inline` (abc)(def) 1,524 B; `plain` (a+)+b 3,079 B, K41 witness 2 144,137 B; `shared` w-256 305,686 B; claim 11: framed ⇒ plain) |

**Rule 1: never infer a fact from a stamp's ABSENCE. Read the VALUE.**
This is pcrec's own inbox I-5 hazard, which broke four of pcrec's checks
the day the stamps landed. A macro this adapter does not see is recorded
as NO PAIR, which record_schema.md §7 already defines as "not stamped" — a
state distinct from every value. The one reading taken from an absence is
the spec's own IFF and comes from a FIELD (printed on every artifact, so it
is never taken from silence): `rx_info.scan == NULL` on a VM artifact IS
"not a hybrid" (match_api.md §6, consequence 2).

The scope rules those absences obey, exactly (match_api.md §6.3 (a)):

- `RX_ENGINE` — **every** artifact pcrec emits.
- `RX_DFA_SCAN` / `_PREFILTER` / `_TABLE` — every artifact that **contains
  a DFA scan**: every DFA artifact AND every VM HYBRID, and no other. A
  non-hybrid VM artifact carries none of the three.
- `RX_FAST_FRAMES` / `_TRAIL` — every **VM** artifact, single-tier ones
  included. `RX_FAST_FRAMES == RX_RESUME_FRAMES` IS "this artifact has one
  tier", and is the only spelling of it.
- `RX_VM_PREFILTER` and `RX_DFA_PREFILTER` are **two different selections**,
  not two spellings. The first says whether the VM runs a capture-erased DFA
  ahead of its program at all; the second says what candidate-start filter
  THAT scan carries. A hybrid answers both, independently, and both are
  recorded.
- `RX_DFA_PREFILTER_OFFSETS` — the scan family's scope (abi 9): with the
  three above, hybrids included. `"none"` IFF `RX_DFA_PREFILTER` is not an
  `offset-set` value; the adapter checks that iff from both sides.
- `RX_DFA_SCAN_EDGE` — the scan family's scope again (abi 13, [B25]):
  every artifact that contains a DFA scan, hybrids included — match_api.md
  §6.3 says the iff "joins unchanged". `none` is FOUR causes, none a
  failure: no collapsible run, an `attempt` scan (label dispatch — no
  loop-carried table load to shorten), an `empty` scan, or
  `-fno-scan-edge`. MEASURED: the same `[0-9]+` run stamps `range`
  unanchored and `none` under `^` (the attempt cause, on the same
  pattern text).
- `RX_DFA_MATCH` — a DIFFERENT iff, and the difference is the fact (abi
  10, match_api.md §6.3): it describes the `_match` ENTRY, not a scan, so
  it is on every artifact whose `RX_ENGINE` is `"dfa"` and on NO VM
  artifact — a hybrid contains a DFA scan but its `_match` is the VM's own
  body. `rx_info.match_form` is NULL exactly where the macro is absent.
- `RX_UNROLL_K` / `_UNROLL_K_WHY` / `_MAX_EMIT_CODE_BYTES` — every **VM**
  artifact and no DFA one (a DFA artifact has no counter rung to have
  chosen a K for; the code-bytes cap bounds a VM quantity).
  `RX_MAX_EMIT_BYTES` — **every** artifact, both engines.
- ([B19]) `RX_ENGINE_SEL` — **every** artifact, both engines (D81:
  `"selected"` is a fact). No `rx_info` mirror; its controls are the
  CONFIG and the stamps beside it (rules 8-9 below).
- ([B19]) `RX_VM_PREFILTER_LANG` / `_LANG_WHY` — every **VM HYBRID** (where
  `RX_VM_PREFILTER` reads `"hybrid"`) and **no other artifact** — narrower
  than "every VM artifact" (I-18's wording) and narrower than the scan
  family's "contains a DFA scan" (which a plain DFA artifact satisfies):
  a DFA artifact takes no VM-prefilter decision, and a forced `--engine=vm`
  artifact has no prefilter and no language to name. MEASURED at 96e44c2
  on the forced `level-context`: `RX_VM_PREFILTER "none"`, neither macro.

**Rule 2: one derivation per column; a second spelling is spent as a
CONTROL.** pcrec publishes three facts twice and asserts on its own side
that the two agree, over its whole corpus and on both engines
(`tests/codegen/run_dfa_stamps.sh`). This adapter reads both and checks
them (`Adapter._check_agreement`), because a disagreement is a compiler or
shim bug rather than a measurement, and a record that quietly kept one of
the two would carry the bug forward as a number:

1. `<PREFIX>_ENGINE` == the string form of `rx_info.engine`.
2. `rx_info.prefilter` is never NULL (consequence 1).
3. `<PREFIX>_DFA_SCAN` present IFF `rx_info.scan` is non-NULL, and equal to
   it when both are there.
4. `rx_info.prefilter` == `<PREFIX>_DFA_PREFILTER` where a DFA scan exists,
   == `<PREFIX>_VM_PREFILTER` (`"none"`) where it does not. The field
   reports the mechanism that ACTUALLY RUNS and never the coarse `"hybrid"`
   (consequence 3).

5. ([B18]) `<PREFIX>_DFA_MATCH` present IFF `rx_info.match_form` is
   non-NULL, and equal to it.
6. ([B18]) `dfa_prefilter_offsets` is `"none"` IFF `dfa_prefilter` is not
   an offset-set value, and names a scanned offset (`*`) when it is one.
7. ([B18]) **THE SCOPE TABLE** (`adapter.STAMP_SCOPE`): at the artifact's
   own abi, every stamp pcrec emits UNCONDITIONALLY (its D81) is present
   inside its scope and absent outside an exclusive one. This is what lets
   the shim keep reading macros through `#ifdef` (so an artifact between
   the floor and a macro's abi links and records "not stamped") without
   ever letting a stamp that should be there go quietly blank: a missing
   unconditional stamp is an `AdapterError`, never a "not stamped".
8. ([B19]) `engine_sel` is `forced` IFF the config named `--engine=` —
   the stamp has no field mirror, so the CONFIG is its control (the
   registry's `engine-route` order-1 row: "the caller named the engine,
   so auto selected nothing").
9. ([B19]) `engine_sel` implies its neighbours (match_api.md §6.3's table
   read as implications): `collapsed-prefilter` → engine `vm`, prefilter
   `hybrid`, language `count-collapsed`; `overflowed-dfa` /
   `overflowed-prefilter` → engine `vm`, prefilter `none`. The language
   pair's own iff is the scope table's `vm-hybrid` row (both directions).

Each is an `AdapterError` naming both values. An absent MACRO is checked
only against the field's own absence — rule 1, applied to the control
rather than to the datum — and the scope table applies from each stamp's
own abi.

### The ABI FLOOR, and where it lives

`shim.c` reads three `rx_info` FIELDS pcrec appended after abi 2: `scan` /
`prefilter` (abi 6) and, since [B18], `match_form` (abi 10, the runtime
mirror of `RX_DFA_MATCH`, read so the macro has its control) — so **10 is
the lowest artifact it can read** and `PB_SHIM_MIN_ABI` says so ONCE. The
rule that moved it: the floor rises iff a FIELD is added to what the shim
reads; the abi 9 and abi 11 MACROS it also gained did not move it, because
a macro read through `#ifdef` has a legitimate "not stamped" absence — and
neither did abi 12's three ([B19]: `RX_ENGINE_SEL` and the language pair
have no `rx_info` mirror; an abi-10/11 artifact still links and records
them as "not stamped", the scope table saying at which abi that stops
being legitimate). **`PB_SHIM_MIN_ABI` is 16 at pin 288d505** ([B34]; it was 15 at 1989c62, [B26]): the rule's OTHER
direction fired for the second time in this file's life. It held at 10
through 96e44c2, 263b013 and a7e0bdf — [B22] added VALUES not stamps,
abi 13's `RX_DFA_SCAN_EDGE` is a macro with no rx_info mirror (`struct
rx_info` MEASURED byte-identical between 263b013 and a7e0bdf), and abi 14's
eighth `RX_ENGINE_SEL` value is a new string in an existing macro — and it
MOVED at abi 15, where `rx_info.name` and `.nentries` were appended and
this shim reads both. A `pcrec-local` binary older than abi 15 is now
REFUSED by name rather than measured. **UNCHANGED at pin 334fd10e**
([B37], abi 22): six abi steps, four new MACROS (`RX_DFA_UNIFORM_FOLDS`,
`RX_VM_ALT_ISLANDS`, `RX_VM_ENTRY_SHAPE`, `RX_VM_PROGRAM_BYTES`), no new
FIELD — `struct rx_info` is byte-identical between abi 16 and 22
(MEASURED at the re-pin), so the rule's first direction fired six times
and the floor did not move. (Why
that `#ifdef` is not an inference from absence: the scope table above.)
`driver.c` compares `pb_abi()` against it before reading anything else and
refuses a lower artifact by name (`error abi-below-shim-floor: …`, carrying
both numbers, exit 3); `adapter.py` recognises that line and re-raises it
as a clean `AdapterError` **without keeping a second copy of the number**.
An artifact older still (abi < 10) does not link this shim at all — the
field access is a compile error, which is the loudest form of the same
refusal and cannot be mistaken for a measurement. Consequence for the
edit-test loop: `pcrec-local` pointed at a pcrec before 808740c (abi 10)
is refused — at gcc for abi < 10 (no `match_form` member), never as a
number.

`make check-harness`'s `abi floor` block is the SABOTAGE that keeps the
path exercised: a real artifact's `.abi = 11` edited to `5` in a copy, built
with the ordinary shim and run by the ordinary driver, must be refused by
name — with the unmodified artifact loading in the same run as the positive
control, the floor the refusal must name read out of `shim.c` by the check
rather than retyped, and the token the adapter watches for checked against
the diagnostic the driver actually produced (two copies of one string, in
two languages, with nothing else enforcing that they agree).

### MEASURED at pin 35e1ab1, 2026-08-28 — one artifact of each KIND

Asserted by VALUE in `make check-harness` (`check_mechanism_stamps`), on
small hand-chosen patterns rather than on `bench/email`'s: a check whose
witness is a corpus pattern stops being a check the day engine selection
moves under it, which is exactly what happened to `factored` between
8da6120 and 692c2e8.

| kind | pattern / config | stamps |
|---|---|---|
| pure DFA | `foo[0-9]+bar`, auto | `engine=dfa`, `dfa_scan=unanchored`, `dfa_prefilter=memchr`, `dfa_table=premultiplied`; no `fast_*` |
| VM HYBRID | `a(b\|c)+d`, auto | `engine=vm`, `prefilter=hybrid`, `dfa_scan=unanchored`, `dfa_prefilter=memchr`, `dfa_table=premultiplied`, `fast_frames=1`, `fast_trail=3` |
| VM, no DFA scan | `a(b\|c)+d`, `--engine=vm` | `engine=vm`, `prefilter=none`, NO `_DFA_*` pair, `fast_frames=1`, `fast_trail=3` |
| provably-empty | `[^\x00-\xff]`, auto | `engine=dfa`, `dfa_scan=empty`, `dfa_prefilter=none`, `dfa_table=none` |

`abi` reads **8** on all four. `--engine=vm` disabling the DFA prefilter
(so the VM derives the whole span independently) is visible directly for
the first time: the same pattern is a HYBRID under `auto` and carries no
DFA scan at all under `--engine=vm`.

**`dfa_table` needs its own control, and has one.** pcrec's form census
measured `indexed` and `mixed` at ZERO corpus population — every ordinary
pattern is small enough that the pre-multiplied form wins — so a check that
only ever sees `premultiplied` cannot tell a working stamp from a constant,
and this bench would then be filtering on a column that never varies.
`check_deny_flag_controls` (`check_dfa_table_deny_flag` until [B18]) uses
`-fno-premul-table` (tuning.md §2.13, an answer-identity-preserving deny
flag) through `pcrec-local` to reach `indexed` on the census's own witness
pattern — and, since [B18], the same shape for every stamp the re-pin
added a deny flag for (next section).

### MEASURED at pin 36d5963, 2026-08-29 — the abi 9-11 stamps ([B18])

Asserted by VALUE in `make check-harness` (`check_mechanism_stamps`), on
the four kinds above plus an anchored `attempt` one, and — new — on the
bench's OWN patterns, because these are the rows pcrec's inbox
I-15/I-16/I-17 made predictions about (`LEDGER_STAMP_CASES`): on those a
corpus witness moving IS the finding.

| kind / pattern | config | engine | dfa_prefilter | offsets | dfa_match | K / why | caps (code / total) |
|---|---|---|---|---|---|---|---|
| `foo[0-9]+bar` | auto | dfa | memchr | none | **unwrapped** | — | — / 1,000,000 |
| `a(b\|c)+d` (hybrid) | auto | vm | memchr (the scan's) | **none** (present: a hybrid has the scan) | **absent**, `match_form` NULL | 8 / default | 500,000 / 1,000,000 |
| `a(b\|c)+d` | `--engine=vm` | vm | — (no scan) | absent | absent, NULL | 8 / default | 500,000 / 1,000,000 |
| `[^\x00-\xff]` (empty) | auto | dfa | none | none | **search-filter** | — | — / 1,000,000 |
| `^foo[0-9]+bar` (attempt) | auto | dfa | none | none | **search-filter** | — | — / 1,000,000 |
| loglines `uuid` | auto, nocaps | dfa | **offset-set-bounded** | **`0,8*,13`** | unwrapped | — | — / 1,000,000 |
| loglines `iso-ts` | auto, nocaps | dfa | **offset-set** | **`0,4*`** | unwrapped | — | — / 1,000,000 |
| loglines `stack-frame` | auto, nocaps | dfa | **offset-set-bounded** | **`0,1*`** | unwrapped | — | — / 1,000,000 |
| loglines `ipv6` | auto | dfa | byte-class | none | unwrapped | — | — / 1,000,000 |
| loglines `kv-quoted`, `bignum`, `hex32-id` | auto | dfa | byte-class-bounded | none | unwrapped | — | — / 1,000,000 |
| loglines `ipv4` | auto | dfa | byte-class | none | unwrapped | — | — / 1,000,000 |
| loglines `http-5xx` | auto | dfa | memchr-bounded | none | unwrapped | — | — / 1,000,000 |
| loglines `level-context` | **auto, nocaps** | **vm** (was did-not-compile at 35e1ab1) | — (no scan; `RX_VM_PREFILTER none`) | absent | absent, NULL | 8 / default | 500,000 / 1,000,000 |
| email `orig`, `factored` | auto, nocaps | dfa | byte-class (plain) / byte-class-bounded (`\z`) | **none** (declined: `@` sits at a variable offset) | unwrapped | — | — / 1,000,000 |
| email `floor` | auto, nocaps | dfa | memchr / memchr-bounded | none | unwrapped | — | — / 1,000,000 |
| every pattern | `--engine=vm` | vm | — | absent | absent, NULL | **8 / default** | 500,000 / 1,000,000 |

`abi` reads **11** on all of them. The `\z` form of every DFA artifact
carries the same offsets as its plain form and the `-bounded` prefilter
value (the [B16] asymmetry, unchanged: `iso-ts` is `offset-set` plain and
`offset-set-bounded` under `\z`); `uuid` and `stack-frame` are `-bounded`
in BOTH forms because their `\b` is a word-context accept.

**Every I-15/I-16/I-17 prediction about a stamp VALUE held**: the three
offset strings, the six declined loglines rows, both email patterns
declined, `unwrapped` on every DFA artifact of both sub-benches,
`K=8`/`default` on every VM artifact, 54/54 emits accepted, and
`level-context` under `auto` compiling as a VM artifact whose diagnostic
is `RX_ENGINE_WHY: dfa overflowed: >32000 states at pattern offset 0`
(the [SEL-1] fallback; Frank's ask (b) has its first row). Three things
the inbox said that the artifacts and the spec say differently:

1. **`RX_MAX_EMIT_CODE_BYTES` is NOT on every artifact.** I-17 (4) and
   pcrec `limits.md` §8 say both caps are stamped "on every artifact";
   the artifacts (and `match_api.md` §6.3 + `artifact_size_term.md` §7.1,
   which say "VM-artifact-scoped for the first two … `_MAX_EMIT_BYTES` is
   on BOTH engines") put `_CODE_BYTES` on VM artifacts only. The adapter
   follows the artifacts; `limits.md` §8's sentence is the stale one.
2. **The registry's `size-term` axis carries no `stamp_value`** for
   `RX_UNROLL_K_WHY` (both rows empty), although the macro is name-valued
   (seven values). `unroll_k_why`'s declared set is therefore the spec's,
   and `registry_check` cannot cover it. Likewise the `table` axis lists
   only the two candidates the selector walks; `none` (an `attempt` /
   `empty` scan, measured above) and `mixed` are OUTCOME values the
   registry does not enumerate (`adapter.REGISTRY_OUTCOME_VALUES`).
3. **Registry.md §6 says "45 rows / 18 axes"**; the live dump at 36d5963
   prints 47 / 19 (I-17's number), the `size-term` axis being the new one.

### The deny-flag controls at 36d5963 ([B18])

Each of the four stamps whose corpus population is one-sided has a deny
flag that reaches the OTHER value on a real artifact, and
`check_deny_flag_controls` proves each, through `pcrec-local` at the
pin's binary, with the flag's SPELLING read from `list_axes.tsv` (the
axis's order-1 row) rather than typed:

| axis / flag (bit) | witness | default | denied |
|---|---|---|---|
| `table` / `-fno-premul-table` (15) | `(?:[a-z]+)@(?:[a-z]+)` | `dfa_table premultiplied` | `indexed` |
| `prefilter` / `-fno-offset-skip` (16) | loglines `uuid` | `offset-set-bounded`, offsets `0,8*,13` | `byte-class-bounded`, offsets `none` (TWO pairs move: the iff seen from the flag's side) |
| `match` / `-fno-anchored-dfa` (17) | email `floor` | `dfa_match unwrapped` | `search-filter` (and the artifact is 4,824 B smaller: the third machine is gone) |
| `size-term` / `-fno-size-term` (18) | email `orig`, `--engine=vm` | `unroll_k_why default`, K 8 | `denied`, K 8 (the flag denies the SELECTION; nothing was selected here, so K does not move) |

`--unroll=4` on the same VM artifact reads `unroll_k 4` / `option`, the
third value reachable on this corpus; `size-model`, `size-model-declined`,
`cap-rescue` and `capacity-declined` need a pattern over the 120,000-code-
byte threshold, which nothing in either sub-bench is ([B11.4]
bounded-repeat is where they will first be seen).

### MEASURED at pin 96e44c2, 2026-08-30 — the abi-12 stamps ([B19])

Asserted by VALUE in `make check-harness` (`check_mechanism_stamps`), on
the kinds above plus two new ones, and on the ledger rows pcrec's inbox
I-18 made predictions about. `abi` reads **12** on all of them;
`PB_SHIM_MIN_ABI` stays 10.

| kind / pattern | config | engine / `engine_sel` | `prefilter` | `vm_prefilter_lang` / `_why` | emit / code bytes |
|---|---|---|---|---|---|
| `foo[0-9]+bar`, `[^\x00-\xff]`, `^foo[0-9]+bar`, every loglines/email DFA row | auto | dfa / **selected** | — | absent (not a hybrid) | e.g. email `orig` 81,673 / 13,146 |
| `a(b\|c)+d` (hybrid) | auto | vm / selected | hybrid | **exact** / `no counted repeat` | 26,267 / 22,745 |
| `a(b\|c){2,5}d` (hybrid, a counted repeat) | auto | vm / selected | hybrid | **exact** / `exact` | 26,317 / 22,795 |
| `a(b\|c)+d`, email `orig`, loglines `level-context` | `--engine=vm` | vm / **forced** | none | **absent** (no prefilter, no language) | `level-context` 29,270 / 28,807 |
| loglines `level-context` | **auto, nocaps** | vm / **collapsed-prefilter** | **hybrid** (was `none` at 36d5963) | **count-collapsed** / `dfa overflow retry, exact nfa 462` | 75,812 / 33,983 |
| bounded `cls-upto-32768` (`[a-z]{0,32768}`) | auto | vm / **collapsed-prefilter** | hybrid | count-collapsed / `dfa overflow retry, exact nfa 65538` | 32 KB (a `[a-z]*` prefilter; the set's predicted first refusal, RESCUED) |
| bounded `cls-upto-16384`, plain | auto | dfa / selected | — | absent | **724,699 / 11,589 — WARNS** (`warned_emit_bytes 724699`; over `--warn-emit-bytes=250000`; outcome `compiled`) |
| bounded `cls-upto-16384`, `\z` form | auto | vm / **collapsed-prefilter** | hybrid | count-collapsed / `dfa overflow retry, exact nfa 32771` | 26,128 / 22,617 — the K7 element budget, not the state cap (`RX_ENGINE_WHY "dfa overflowed: subset construction exceeds 48000000 state-set elements"`) |
| K41's fuzz-gate witness 2 (the SIZE-CAP rung) | auto | vm / **selected** | hybrid | count-collapsed / `size cap retry, exact 671050 > 500000` | 158,756 / 152,409 (the exact artifact was refused at 671,050 code bytes) |

**I-18 (ii)'s prediction for `level-context` HELD to the letter**: engine
`vm`, `_ENGINE_SEL collapsed-prefilter`, `_LANG count-collapsed`,
`_LANG_WHY "dfa overflow retry, exact nfa 462"` (the `\z` form reads
`463`). So did (v)'s class-ladder rows the check reaches (32768 rescued as
a collapsed-prefilter hybrid at `exact nfa 65538`; 16384 a DFA that
warns; the emitted byte count differs from the table's 725,692 because
the adapter names its files `artifact.c`/`.h` and the count includes the
emitted `#include` line). Four things the inbox said that the artifacts
and the spec say differently — each now a check that asserts what IS
true:

1. **The language pair is NOT on every VM artifact.** I-18 (2) says "on
   every VM artifact"; match_api.md §6.3 ("on every artifact with a VM
   PREFILTER DECISION that came out hybrid … and on no DFA artifact") and
   the forced artifacts say VM HYBRIDS only. `STAMP_SCOPE`'s `vm-hybrid`
   scope is exclusive in both directions, and the [B18]-style scope check
   proves it on 5 hybrids vs 17 others. The letter's "`--engine=vm` →
   `sel=forced`, `lang=exact`" is therefore half right: `forced`, and NO
   `lang` at all.
2. **`-fno-prefilter-collapse` does not turn every rescue into a
   refusal.** limits.md §8 says which: the [SEL-1] rung's alternative is
   NO PREFILTER, the size-cap rung's is the cap's refusal. Measured:
   `level-context` denied → `overflowed-dfa` / `prefilter none` / no
   language pair (the 36d5963 shape; still `compiled`); K41 witness 2
   denied → `did-not-compile`, "pattern too large: 671050 bytes of
   emitted code (limit 500000)". Both are `check_deny_flag_controls` rows.
3. **The size-cap rescue stamps `engine_sel "selected"`**, not
   `collapsed-prefilter` — match_api.md's table reserves that token for a
   DFA BUILD overflow, and an emitted-size refusal is not one. Frank's
   ask (b) bucket (`_ENGINE_SEL not in (selected, forced)`) therefore does
   NOT see this rescue; its only structured trace is `_LANG_WHY`'s
   `size cap retry` prefix, which is why `vm_prefilter_lang_why` is
   recorded as its own pair and the reporter's legend note names the gap.
   The `bucket:` check asserts the bucket is exactly the two state-cap
   rescues and that the size-cap witness is outside it. An outbox item.
4. **`_LANG_WHY` has a sixth value**, `no counted repeat` (a hybrid with
   nothing to collapse), beside I-18's `exact`; a `string` pair, not an
   enum.

**The two source-bytes pairs and the warning ((d), (e)).** `emit_bytes` /
`emit_code_bytes` are measured by `adapter.emit_size()`, a port of pcrec
`src/core/compile.c`'s `emit_size_measure` (the ONE definition the two
caps enforce and the size log / [ART-SIZE] census use: total minus comment
bytes; that minus `static const … rx_*[N] = {` initializers, a
computed-goto jump table's one-liner included), summed over the `.c` and
`.h` as pcrec sums its two buffers. The control that the port IS the
definition: `_emit_facts` refuses any compile whose `--warn-emit-bytes`
line disagrees with it, and `check_emit_size_port` forces that line at
`--warn-emit-bytes=1` on four kinds × two forms (a table-dominated DFA, an
`attempt` DFA with the one-line jump table, a hybrid, a forced-collapse
hybrid) — 8/8 byte-exact — plus a hand-classified probe (a comment inside
a table, a `= {` that is not `static const`, a block comment closing on a
later line). `warned_emit_bytes` is present ONLY where the line fired; the
line itself is appended to the compile row's `diagnostic` after
`RX_ENGINE_WHY`; the exit code and the artifact are what they would have
been (limits.md §8: never a refusal). On both flat sets nothing warns at
the default 250,000; on bounded, `cls-upto-16384`'s plain form does.

### The deny-flag controls at 96e44c2 ([B19])

`check_deny_flag_controls` grew a sixth column (`deny` / `force`) because
the `prefilter-lang` axis's order-1 row carries BOTH spellings in one
`cli_flag` cell (`-fno-prefilter-collapse / -fprefilter-collapse`): the
flag is picked by prefix, and the registry's `stamp_value` is checked
against the arm in which that candidate was CHOSEN (the default arm of a
deny, the flagged arm of a force). The four [B18] rows are unchanged.

| axis / flag (bit) | witness | default | flagged |
|---|---|---|---|
| `prefilter-lang` / `-fno-prefilter-collapse` (19) | loglines `level-context` | `count-collapsed` / `dfa overflow retry, exact nfa 462`, `collapsed-prefilter`, `hybrid` | language pair ABSENT, `overflowed-dfa`, `none` — the [SEL-1] rung denied drops the prefilter (THREE pairs move: the scope iff seen from the flag's side) |
| `prefilter-lang` / `-fno-prefilter-collapse` (19) | K41 witness 2 | `count-collapsed` / `size cap retry, exact 671050 > 500000` | **REFUSED**, `did-not-compile` "pattern too large … (limit 500000)" — the size-cap rung denied restores the cap's refusal |
| `prefilter-lang` / `-fprefilter-collapse` (20) | `a(b\|c){2,5}d` | `exact` / `exact`, `selected` | `count-collapsed` / `forced`, `selected` (the route token does not move: nothing overflowed) |

`overflowed-prefilter` (the VM already chosen, only its prefilter's DFA
overflowed) is the one `engine_sel` value no witness in reach produces —
noted, not asserted (still true at 263b013 and a7e0bdf, one of SEVEN
values).

### MEASURED at pin 263b013, 2026-08-31 — the [OPT-4.1] + [LIM-1] VALUES ([B22])

The pin adds NO stamp and NO abi (still 12); it adds two `RX_ENGINE_SEL`
VALUES, one `_LANG_WHY` value, and the `--list-limits` surface. Asserted
by VALUE in `check_mechanism_stamps` on the I-21-corrected DECLINE/KEEP
sets (stamped 11/11 as pcrec predicted — inbox I-23/I-25):

| kind / pattern (form) | `engine_sel` | `prefilter` | lang / why | notes |
|---|---|---|---|---|
| bounded `cls-upto-32768` plain AND whole | **`declined-nullable`** | none | **absent** (no pair) | was a 32 KB `collapsed-prefilter` hybrid at 96e44c2 — the artifact CHANGED KIND (I-22 (ii)); emit = code = 18,291 / 18,496 B (no table initializers at all) |
| bounded `cls-upto-16384` whole, `cls-lazy-16384` whole | `declined-nullable` | none | absent | the two other nullable declines; their PLAIN forms are unchanged (16384 = the DFA that WARNS, 724,699 B) |
| bounded ctx rungs ×4, plain | `collapsed-prefilter` | hybrid | count-collapsed / `dfa overflow retry, exact nfa 174 / 558 / 558 / 2094` | the KEEP set: minw 8, non-nullable |
| bounded `nest2-64` / `nest3-16` whole | `collapsed-prefilter` | hybrid | count-collapsed / `exact nfa 8258` / `8466` | minw 1, non-nullable (the I-21 CORRECTION's two rows; nest3-16 is still the corpus's one K mover: K=1 / size-model) |
| loglines `level-context`, auto | `collapsed-prefilter` | hybrid | count-collapsed / `exact nfa 462` | unchanged from 96e44c2 |
| K41 witness 2 (the size-cap rung) | **`size-cap-retry`** | hybrid | count-collapsed / `size cap retry, exact N > cap` | [LIM-1]: its OWN token, replacing the `selected` mislabel O-8/O-10 flagged ([B19] finding 3, CLOSED) |
| `(x){0,5}` under `-fprefilter-collapse` | `selected` | hybrid | **exact** / **`nullable collapsed language`** | the flag reached a POLICY, not the collapse: the prefilter is kept on the EXACT language (tuning.md §2.17); a `check_deny_flag_controls` force row (`reg_arm skip`) |

Three readings a consumer of 263b013 records needs:

1. **The fallback bucket reads the VALUE, and nothing else.** Frank's
   ask (b) (`engine_sel not in (selected, forced)`) now covers all FIVE
   fallbacks, the size-cap rescue included; the [B19]-era rule that also
   bucketed a `selected` artifact on its `_LANG_WHY`'s `size cap retry`
   prefix (I-19 (3)) is RETIRED (inbox I-25). `ENGINE_SEL_FALLBACK` has
   five members; the reporter's `_engine_sel_display` follows.
2. **The plain and `\z` forms of the declined class rungs overflow by
   DIFFERENT caps**, read in `RX_ENGINE_WHY` (the diagnostic): plain
   `dfa overflowed: >32000 states` (`PCREC_MAX_DFA_STATES_TABLE`), whole
   `subset construction exceeds 48000000 state-set elements (K7)`
   (`PCREC_MAX_SUBSET_ELEMS`) — both now resolvable by name against
   `list_limits.tsv`. Asserted distinct.
3. **A declined artifact is read by "nullable AND no prefilter", never
   minw alone** (I-22 (iv)'s census caveat: three nullable hybrids have
   WORKING prefilters — the `$`-view shapes; `(x){0,5}` above is the
   in-reach witness of a nullable hybrid whose prefilter exists).

The REGISTRY moved 54 → 63 rows / 21 axes (the diff is list_axes.tsv's
header): `engine-route` 5 → 7 (the two new values), `size-term` 2 → 7
with `stamp_value` on every row ([B18]'s documented gap CLOSED — so
`RX_UNROLL_K_WHY` joined `REGISTRY_STAMP_PAIRS` and the `-fno-size-term`
flag row moved off order 1, which `check_deny_flag_controls` now finds
by its `cli_flag` cell), `table` 2 → 4 (the `none`/`mixed` OUTCOME rows;
`REGISTRY_OUTCOME_VALUES` is now empty). `list_definitions.tsv` is
byte-identical below its header. The same-pin emit-size re-comparison
(I-22 (ii)) is `check_emit_size_port`'s fifth witness: the declined
`{0,32768}` artifact, both forms, the pin's own `--warn-emit-bytes=1`
numbers vs the port, byte-exact, counting rule stated (comment-excluded,
`.c` + `.h` summed — pcrec opt41_report.md §15's "split `.c` + `.h`"
reading). `year4`'s +4,096 B (I-22 (iii)) is CLOSED by derivation:
docs/dev/measurements/2026-08-31-year4-elf-page-alignment.txt — ELF page
alignment triggered by the [B19] SHIM's own +384 B, pcrec's source +33 B,
and a one-shim control building both pins byte-identical.

### MEASURED at pin a7e0bdf, 2026-08-31 — the abi-13 stamp ([B25], [OPT-5] STEP 1)

The pin bumps the abi 12 → 13 for ONE new stamp, `RX_DFA_SCAN_EDGE`, and
is the first bump that changed a MACHINE: on any DFA scan whose machine
carries a counted class run, the run's interior states are deleted and
one in-loop bounded scan block replaces them. Asserted by VALUE in
`check_mechanism_stamps` on every stamp/ledger case (`abi` reads **13**
on all of them; `PB_SHIM_MIN_ABI` stays 10):

| witness | `dfa_scan_edge` | why that value |
|---|---|---|
| `foo[0-9]+bar`, `a(b|c){2,5}d` (hybrid), loglines `iso-ts`, `http-5xx`, bounded `nest2-64` plain + both nest wholes, bounded `grp-upto-1024` | **`range`** | a contiguous-class run collapsed — down to the unbounded ONE-STATE form (`[0-9]+`), tuning.md §2.18's own example |
| loglines `ipv6` | **`bitmap`** | the ONLY `bitmap` witness in reach: its hex class is not contiguous, so the edge's test is a 256-byte membership read (VALUE-addressed — the cursor stays the only loop-carried register) |
| `^foo[0-9]+bar` (attempt), `[^\x00-\xff]` (empty), K41 witness 2 (its prefilter scan is an `attempt` scan) | `none` | no loop-carried table load to shorten — the same `[0-9]+` run that stamps `range` unanchored |
| loglines `uuid`, `stack-frame`, `kv-quoted`, `bignum`, `ipv4`, `hex32-id`, both email patterns, `level-context`'s collapsed prefilter, the four bounded ctx rungs, `a(b|c)+d` | `none` | no run the pass takes (`hex32-id`'s 32-count hex run stays `none` where `ipv6`'s stamps `bitmap` — the selection is per RUN, pcrec's boundary to explain) |
| every `--engine=vm` artifact, every `declined-nullable` artifact | **absent** | no DFA scan, no stamp — the scope iff, both directions |

`mixed` is the one value no witness in reach produces (like
`overflowed-prefilter` among the route tokens) — noted, not asserted; the
registry's `scan-body` axis enumerates it as a `predicate` row, so
`registry_check` still covers the declared enum both ways.

**THE HEADLINE, and the acceptance window's size half (I-27 (2)/(5),
verified per rung):** the counted class ladder's emitted source is now
FLAT where it was linear in the count. Same method as every table here
(`artifact.c` naming; comment-excluded port bytes, `.c`+`.h` summed),
263b013 → a7e0bdf, plain forms under `auto`:

| rung | 263b013 emit/code | a7e0bdf emit/code | Δ total |
|---|---|---|---|
| `cls-upto-64` | 21,045 / 12,399 | 19,481 / 14,468 | −1,564 (−7.4 %) |
| `cls-upto-256` | 32,566 / 12,400 | 19,488 / 14,475 | −13,078 (−40 %) |
| `cls-upto-1024` | 80,228 / 12,401 | 19,495 / 14,482 | −60,733 (−76 %) |
| `cls-upto-4096` | 185,828 / 11,588 | 16,347 / 13,007 | −169,481 (−91 %) |
| `cls-upto-16384` | 724,699 / 11,589 | **16,352 / 13,012** | −708,347 (**−97.7 %, ×44**) |
| `grp-upto-1024` | 80,235 / 12,408 | 19,502 / 14,489 | −60,733 (O-11's ≡ cls-upto-1024 holds at this pin too) |
| `cls-atleast-4096` | 171,183 / 11,855 | 18,630 / 13,828 | −152,553 (−89 %) |

CODE bytes RISE ~+1.4-2.1 KB per rung (the edge's in-loop block is code
where the deleted states were table). Consequently **the DFA that WARNS
is gone**: `cls-upto-16384` plain compiled 724,699 B with the advisory
warning at every pin since [B19]; at a7e0bdf it is 16,352 B, silent, and
the warn-capture path's positive witness moved to the `-fno-scan-edge`
deny row (below). Its `dfa_prefilter none` / `dfa_match search-filter`
were already so at 263b013 (RE-MEASURED against the old binary — only
size, the warning and the new stamp moved). Compile TIME did not move
(~7 s both arms, MEASURED): the cost is DFA construction, which still
builds the run before `scanedge.c` deletes it.

**What did NOT move, asserted (I-27 (3): the caps fire DURING
construction, before the edge can act — [OPT-5] STEP 3, unchartered, is
the rung that moves them):** the four `declined-nullable` rows
byte-identical (18,291 / 18,496 / both 16384 wholes), the six
`collapsed-prefilter` keeps at the same exact-nfa whys (174 / 558 / 558 /
2094 / 8258 / 8466), the plain-vs-`\z` overflow ROUTES still distinct
(state cap vs K7), `cls-upto-65535` still refused by
`PCREC_NFA_MAX_STATES` 131072 with identical wording (now asserted BY
NAME in `check_mechanism_stamps` — the day that check fails with a
compiled artifact is the day STEP 3 lands), and every emit-size port
comparison byte-exact (10/10 + probe; K41 witness 2's `_LANG_WHY` count
moved 671,050 → 671,082, the stamp line's own bytes, absorbed by the
regex). Every hybrid/DFA artifact grows ~+32-38 B (the stamp line);
VM non-hybrids and declined artifacts do not move at all.

### The deny-flag control at a7e0bdf ([B25])

| axis / flag (bit) | witness | default | denied |
|---|---|---|---|
| `scan-edge` / `-fno-scan-edge` (21) | bounded `cls-upto-16384` plain | `dfa_scan_edge range`, 16,352 B, no warning | `none`, **724,737 B, the warning RETURNS** (`warned_emit_bytes 724737`) — the one DFA axis whose denial changes the MACHINE: the denied build is the pre-[OPT-5] compiler plus the stamp line |

The flag's registry row (the `scan-edge` axis's order-1 candidate)
carries NO `stamp_value` — the stamp lives on the companion `scan-body`
axis — which is the deny-table's "no stamp_value" note path, exercised
for the first time.

**Emitted-C size, 36d5963 → 96e44c2.** I-18 (1): "nothing that compiled
at 36d5963 changes language, size or speed by default" — true of every
artifact whose route is `selected` or `forced` (the abi-12 stamps are
three `#define` lines). The exception is the [SEL-1] fallback itself,
which now KEEPS a prefilter: `level-context` under `auto` went from a
32,761 B plain-VM `.c` to a 88,438 B hybrid (a count-collapsed prefilter
DFA's tables), `.so` 39,448 vs 26,480 for the forced VM. Not surveyed
beyond that row; the window's `emit bytes` column is the survey.

### RE-MEASURED at 35e1ab1: `bench/email`'s own artifacts

Compile-only facts (no timing, no measurement window). The `692c2e8`
column reproduces the table under "MEASURED against pin 692c2e8" above to
the byte, which is what makes the deltas trustworthy: same method, same
box, same command shape.

| pattern / form / config | 692c2e8 | 35e1ab1 | Δ | stamps at 35e1ab1 |
|---|---|---|---|---|
| `orig` plain / auto, nocaps | 44,786 | 74,593 | +29,807 (+66.6 %) | dfa, unanchored, byte-class, premultiplied |
| `orig` `\z` / auto, nocaps | 50,199 | 85,060 | +34,861 (+69.4 %) | dfa, unanchored, **byte-class-bounded**, premultiplied |
| `orig` plain / vm | 52,521 | 57,595 | +5,074 (+9.7 %) | vm, `RX_VM_PREFILTER none`, no DFA scan |
| `orig` `\z` / vm | 52,651 | 57,725 | +5,074 (+9.6 %) | as above |
| `factored` plain / auto | 45,453 | 75,260 | +29,807 (+65.6 %) | dfa, unanchored, byte-class, premultiplied |
| `factored` `\z` / auto | 50,866 | 85,727 | +34,861 (+68.5 %) | dfa, unanchored, **byte-class-bounded**, premultiplied |
| `factored` plain / vm | 65,288 | 70,362 | +5,074 (+7.8 %) | vm, `none`, no DFA scan |
| `floor` plain / auto | 13,318 | 16,466 | +3,148 (+23.6 %) | dfa, unanchored, **memchr**, premultiplied |
| `floor` `\z` / auto | 14,280 | 18,324 | +4,044 (+28.3 %) | dfa, unanchored, **memchr-bounded**, premultiplied |
| `floor` plain / vm | 19,647 | 19,739 | +92 (+0.5 %) | vm, `none`, no DFA scan |

Four things a reader of the re-pin's numbers needs:

1. **Engine selection did NOT move.** Every `auto` and `nocaps` artifact
   of all three patterns is still a DFA artifact, both forms — so
   `pcrec-auto-in` stays INERT on this sub-bench and the roster note above
   stands. `--engine=vm` still yields a NON-hybrid artifact
   (`RX_VM_PREFILTER "none"`), the corpus-wide behaviour pcrec documents
   for that flag, which is why the `vm` configs carry no `_DFA_*` stamps.
2. **The `\z` form's prefilter is now READABLE, and it is a different
   mechanism, not a different pattern.** The plain form stamps
   `byte-class` and the `\z` form `byte-class-bounded` (and `floor`:
   `memchr` vs `memchr-bounded`). That IS the plain-vs-`\z` skip-loop
   asymmetry the [B8] measurement had to establish by reading the emitted
   loop — under a `$`/`\Z`/`\z` view every skip stops one byte short and
   the `memchr` arm loses its early-out. A reader comparing the two forms
   must not attribute that difference to engine selection; the stamp now
   says so in the record.
3. **DFA artifacts grew far more than pcrec's I-11 predicted.** That note
   said "DFA artifacts +~5 KB (the accept table grows ×classes)"; measured
   here it is **+29.8 KB plain / +34.9 KB `\z`** on both email patterns
   (+66 %..+69 %) and +3.1/+4.0 KB (+24 %/+28 %) on the much smaller
   `floor` pattern. The span covers five pins, not [OPT-3] alone — see
   the attribution below.
4. **VM artifacts grew +5,074 B, flat**, on both patterns and both forms
   (and +92 B on `floor`), which is [OPT-1]'s deep tier as a second
   noinline function — I-11's "+1-2 KB" for the VM side, also low.

#### Where the growth came from (attributed pin by pin)

Compiled at each of the four pins that span the re-pin, in a scratch build
root, same command shape throughout (`orig` and `floor`, plain form):

| artifact | 692c2e8 (abi 3) | 6e8edfb (abi 6) | 3e0b256 (abi 7) | 35e1ab1 (abi 8) |
|---|---|---|---|---|
| `orig` / auto (DFA) | 44,786 | 44,957 **+171** | 72,452 **+27,495** | 74,593 **+2,141** |
| `orig` / vm | 52,521 | 57,595 **+5,074** | 57,595 **+0** | 57,595 **+0** |
| `floor` / auto (DFA) | 13,318 | 13,481 **+163** | 14,327 **+846** | 16,466 **+2,139** |
| `floor` / vm | 19,647 | 19,739 **+92** | 19,739 **+0** | 19,739 **+0** |

- **abi 4-6 costs a DFA artifact ~170 B** — the three stamps and the two
  `rx_info` pointers, which is what one would expect of them.
- **abi 7 ([OPT-3], the pre-multiplied tables) is the whole story on the
  DFA side, and it is not "+~5 KB": +27,495 B on `orig` (+61 %)** against
  +846 B on the much smaller `floor` pattern. It scales with the machine,
  as the mechanism says it should (the accept table grows ×classes) — the
  prediction in pcrec's I-11 appears to have been made against a pattern
  the size of `floor` rather than of `orig`. A VM artifact is untouched by
  it, because `--engine=vm` yields a NON-hybrid artifact here and a
  non-hybrid VM artifact contains no DFA table at all.
- **abi 8 ([ENG-FORM]) costs ~2.14 KB per DFA artifact, FLAT** (+2,141 on
  `orig`, +2,139 on `floor`) — the file-scope typedef and inline accessor
  block per machine. I-13 said "nothing you read" moved, which is true of
  every VALUE, and is what that note was about; the artifact still grew.
- **[OPT-1]'s deep tier costs a VM artifact +5,074 B on `orig`** and only
  +92 B on `floor` (a single-tier artifact: its stamped default already
  fits a page), and nothing after abi 6 moves a VM artifact at all.

The consequence for a re-pin report: the compile-cost columns will move on
the DFA rows by much more than the ±5 % pcrec's notes predict, and
`artifact bytes` ([B14] R7) is the column that says why.

### RE-MEASURED at 36d5963 ([B18], 2026-08-29): emitted-C size, 35e1ab1 → 36d5963

Compile-only, same method both columns (`-o artifact.c`, the bench's own
flag sets, the size of the `.c` as written — comments INCLUDED, which is
why these read ~1.4× pcrec's own `bench_acceptance.sh` numbers, which
count comment-excluded bytes: its `level-context` 22,905 B is this
table's 32,761 B). Every number here is 4 B below the [B16] table's
method on every row (a pattern-text difference in how the two scripts
invoked the CLI), so the DELTAS are the comparable quantity.

| pattern / form / config | 35e1ab1 (abi 8) | 36d5963 (abi 11) | Δ |
|---|---|---|---|
| `orig` plain / auto, nocaps | 74,589 | 88,719 | **+14,130 (+18.9 %)** |
| `orig` `\z` / auto, nocaps | 85,056 | 101,061 | **+16,005 (+18.8 %)** |
| `orig` plain / vm | 57,587 | 57,740 | +153 (+0.3 %) |
| `factored` plain / auto | 75,256 | 89,386 | +14,130 (+18.8 %) |
| `factored` `\z` / auto | 85,723 | 101,728 | +16,005 (+18.7 %) |
| `factored` plain / vm | 70,354 | 70,507 | +153 (+0.2 %) |
| `floor` plain / auto | 16,462 | 21,433 | +4,971 (+30.2 %) |
| `floor` `\z` / auto | 18,320 | 24,147 | +5,827 (+31.8 %) |
| `floor` plain / vm | 19,731 | 19,884 | +153 (+0.8 %) |
| loglines `uuid` plain / auto (offset-set) | 28,279 | 40,596 | +12,317 (+43.6 %) |
| loglines `iso-ts` plain / auto (offset-set) | 25,520 | 36,068 | +10,548 (+41.3 %) |
| loglines `stack-frame` plain / auto (offset-set) | 52,944 | 73,286 | +20,342 (+38.4 %) |
| loglines `ipv4` plain / auto (declined) | 23,053 | 30,345 | +7,292 (+31.6 %) |
| loglines `http-5xx` plain / auto (declined) | 40,096 | 59,177 | +19,081 (+47.6 %) |
| loglines `level-context` plain / auto | did-not-compile | 32,761 | now a VM artifact ([SEL-1]) |
| every VM artifact, both sets | | | **+153 B flat** (I-16 said +63 for abi 10, artifact_size_term.md +128 for abi 11) |

**DFA artifacts grew far more than I-15 + I-16 predicted** ("+1.4-1.9 KB
where the k-set is selected, +40 B declined" and "+2,605 B source median,
p99 +6.7 KB"): +14.1 KB on both email patterns (declined), +5.0 KB on
`floor`, +7-20 KB across loglines, with the `http-5xx` control (declined)
growing +19.1 KB. The pin-by-pin attribution is below; the reading is the
same as [B16]'s finding 3 — pcrec's medians are over a corpus of small
patterns, and the [ENG-ABS] third machine scales with the machine. The
`.o` delta is the smaller quantity (I-16: 2-11 % of the source delta —
the anchored table is verbose decimal C), and `artifact bytes` ([B14] R7)
is the column that says which.

#### Where the growth came from (attributed pin by pin)

Compiled at each of the three pins that span the re-pin, in a scratch
build root (`pin.sh --build-root`), same command shape throughout:

| artifact | 35e1ab1 (abi 8) | 8ab6152 (abi 9, [OPT-K]) | 808740c (abi 10, [ENG-ABS]) | 36d5963 (abi 11, [ART-SIZE]) |
|---|---|---|---|---|
| `orig` plain / auto (DFA, declined) | 74,589 | 74,629 **+40** | 88,685 **+14,056** | 88,719 **+34** |
| `orig` `\z` / auto | 85,056 | 85,096 **+40** | 101,027 **+15,931** | 101,061 **+34** |
| `floor` plain / auto (DFA, declined) | 16,462 | 16,502 **+40** | 21,399 **+4,897** | 21,433 **+34** |
| loglines `uuid` / auto (offset-set `0,8*,13`) | 28,279 | 30,488 **+2,209** | 40,562 **+10,074** | 40,596 **+34** |
| loglines `iso-ts` / auto (offset-set `0,4*`) | 25,520 | 27,222 **+1,702** | 36,034 **+8,812** | 36,068 **+34** |
| loglines `stack-frame` / auto (offset-set `0,1*`) | 52,944 | 53,061 **+117** | 73,252 **+20,191** | 73,286 **+34** |
| loglines `http-5xx` / auto (declined) | 40,096 | 40,136 **+40** | 59,143 **+19,007** | 59,177 **+34** |
| loglines `ipv4` / auto (declined) | 23,053 | 23,093 **+40** | 30,311 **+7,218** | 30,345 **+34** |
| `orig` plain / vm | 57,587 | 57,587 **+0** | 57,612 **+25** | 57,740 **+128** |
| `floor` plain / vm | 19,731 | 19,731 **+0** | 19,756 **+25** | 19,884 **+128** |
| loglines `level-context` / auto ([SEL-1] VM fallback) | did-not-compile | 32,608 | 32,633 **+25** | 32,761 **+128** |

- **abi 9 ([OPT-K]) costs exactly what I-15 said**: +40 B on every
  declined DFA artifact (the stamp line), +2.2 KB / +1.7 KB where the
  k-set is selected on `uuid` / `iso-ts` (I-15: "+1.4-1.9 KB") — and only
  +117 B on `stack-frame`, whose `0,1*` set has one verified offset. A VM
  artifact does not move (+0). It is also the pin at which
  `level-context` under `auto` starts compiling ([SEL-1]).
- **abi 10 ([ENG-ABS]) is the whole story on the DFA side**: +4.9 KB on
  the tiny `floor` pattern, +14.1 KB on both email patterns, +7.2 KB to
  +20.2 KB across loglines — the third (anchored) machine's table,
  scaling with the machine. I-16's "+2,605 B source median, p99 +6.7 KB"
  was over pcrec's corpus; every DFA artifact of both sub-benches but
  `floor` is above that p99. A VM artifact pays +25 B (I-16 said +63).
- **abi 11 ([ART-SIZE]) is +34 B per DFA artifact and +128 B per VM
  artifact, FLAT** — the design note's own estimate for the VM side
  (artifact_size_term.md §7: "≈ 130 B … +128 B on 1,689 artifacts") to
  the byte.

### MEASURED at pin 1989c62, 2026-09-01 — abi 14 + 15 in one change ([B26])

Two pcrec pins absorbed at once: cc/o42 (abi 14) and w12 (abi 15). Six
findings, each measured at the re-pin against the a7e0bdf binary in the
same run.

**1. THE EIGHTH ROUTE TOKEN HAS NO CUSTOMER IN THIS CORPUS.** The whole
`RX_ENGINE_SEL` census — 77 patterns × 2 forms (plain, `(?:…)\z`) × 3
engine modes (auto, nocaps, vm) = 462 cells per pin, across all four
sub-benches — is **byte-identical between a7e0bdf and 1989c62**:

| value | cells (both pins) |
|---|---|
| `selected` | 220 |
| `forced` | 130 |
| `collapsed-prefilter` | 24 |
| `declined-nullable` | 8 |
| `declined-nullable-default` | **0** |
| (pcrec refused) | 80 |

The predicted population — the `cls-*` hybrids O-10 measured at 1.2-9.9×
loss — does NOT stamp it, and the reason is structural: those patterns are
chosen as the DFA **engine** under `auto`, so they never reach a VM
prefilter decision to have one declined. [OPT-4.2] is real and works; this
corpus simply contains no shape that exercises it. **Consequence for the
window: there is no cls-* AFTER to read for [OPT-4.2].** A set that wants
one needs a VM-forcing construct (lookaround or a backreference) wrapped
around a nullable body.

**2. THE BY-VALUE WITNESS, and its one-character control** (hand-chosen,
in `STAMP_CASES` — the corpus has none):

| pattern | a7e0bdf | 1989c62 | emit total/code |
|---|---|---|---|
| `(?=abc)x*` | `selected`, hybrid, `lang=exact`, `dfa_prefilter none` | **`declined-nullable-default`**, prefilter `none`, **no language pair** | 25,897/22,605 → **18,682/18,682** (−27.8 %) |
| `(?=abc)x+` | `selected`, hybrid, `lang=exact`, `dfa_prefilter memchr` | unchanged | 26,272/22,952 → 25,967/22,647 |

The lookahead forces the VM and leaves the artifact hybrid-eligible; the
only thing that moves between the two rows is whether the body is
NULLABLE. The a7e0bdf row is exactly the useless filter [OPT-4.2] exists to
remove — a hybrid whose `dfa_prefilter` reads `none`. Both directions of
match_api.md §6.3's iff are asserted (prefilter `none`, language pair
ABSENT), and the `\z` form behaves identically (26,813 → 18,794).

**3. THE OLD RUNG-SCOPED VALUE IS STILL DISTINGUISHABLE.** All four
[B22] `declined-nullable` artifacts still stamp `declined-nullable` at this
pin — `cls-upto-32768` plain and whole, `cls-upto-16384` whole,
`cls-lazy-16384` whole — so the two values are told apart on real
artifacts, not by construction. The plain-vs-`\z` overflow ROUTES are
still distinct (state cap vs K7), and `cls-upto-65535` still refuses by
`PCREC_NFA_MAX_STATES` 131072 with identical wording.

**4. `nullable collapsed language` IS NOW UNREACHABLE — an ask for
pcrec.** [B22]'s force control for the collapse POLICY (`(x){0,5}` under
`-fprefilter-collapse` → `lang=exact` / `_why "nullable collapsed
language"`) FAILS at this pin, because [OPT-4.2] declines the prefilter one
step EARLIER: both arms now read `declined-nullable-default` with no
language pair, so the flag moves nothing. The gap is structural, not
accidental — the collapse lowers `X{m,n}` to `X{min(m,1),}`, which can only
introduce nullability when `m == 0`, and such a pattern's EXACT language is
nullable too. MEASURED over ten shapes chosen to separate the two
nullabilities (`(x){0,5}`, `a(x){0,5}`, `(x){0,5}a`, `(x){0,5}\1`,
`(?=y)(x){0,5}`, `(x){0,5}?y`, `(?:x|){0,5}`, `(x{0,3}){0,5}`,
`a(b|c){0,5}d`, `(x){0,5}(?:)`): every one either declines under [OPT-4.2]
or collapses cleanly with `_why "forced"`. None reaches the documented
value. The force-control row is RETIRED and
`check_opt42_preempts_collapse_policy` records the new behaviour in its
place, including the assertion that the flag is INERT on the witness — so
the day a reachable witness exists again (or pcrec retires the value) a
check says so by name. `-fprefilter-collapse` still works where the
language is non-nullable (`a(b|c){2,5}d` → `count-collapsed (forced)`),
which is what makes this a finding and not a broken flag.

**5. THE SIZE BOOKS MOVED UP, NOT DOWN — the brief's expectation was the
wrong sign.** w12's 519 B/artifact comment fix cannot move `emit_bytes` at
all: the measure EXCLUDES comment bytes by definition (`emit_size_measure`,
what the caps enforce). What DOES move it is abi 15's two new `rx_info`
members and their initialisers, and the movement is **+202 B, flat, on
every artifact whose route did not change** — measured on eleven ledger
patterns × two forms, on both engines, on hybrids and plain DFAs alike, and
on both arms of the `-fno-scan-edge` control:

| artifact | a7e0bdf | 1989c62 | Δ |
|---|---|---|---|
| `cls-upto-16384` plain (the collapsed DFA) | 16,352 / 13,012 | 16,554 / 13,214 | **+202** |
| the same, `-fno-scan-edge` (the warning returns) | 724,737 | **724,939** | **+202** |
| ctx rungs ×4, `level-context`, `nest2-64` / `nest3-16` wholes | — | — | **+202 each** |
| `year4` plain / whole | 20,855 / 21,608 | 21,057 / 21,810 | **+202** |
| `cls-upto-32768` plain / whole (declined) | 18,291 / 18,496 | **17,889 / 18,094** | **−402** |
| `cls-lazy-16384` whole (declined) | 18,615 | 18,720 | **+105** |

The DOWNWARD movement the brief predicted is real but is o42's, not w12's,
and it lands only where a prefilter is declined — dramatically on the
witness above (−27.8 %), modestly and unevenly on the already-declined
`cls-*` rungs. **Every expected number in `check_mechanism_stamps` and the
deny-flag table was re-derived at this pin**; the emit-size port agrees
with pcrec's own `--warn-emit-bytes` numbers byte-exactly on all 10
witness/form pairs plus the hand-counted probe.

**6. THE CLANG REFUSAL SET IS EMPTY.** `check_cc_axis`'s named
expected-refusal arm reports **0 refused / 8 agreed** at 1989c62 (clang
21.1.8) — at a7e0bdf it was the frameless-VM `&&label` incompatibility on
every artifact that never pushes a resume frame. [CC-CLANG] step 1 is in
this pin, and the three `-clang` configs now compile every artifact KIND.
The gcc and clang `.so` of each kind agree on every smoke row — answer,
span AND captures — and the agreement arm is non-vacuous (four VM kinds
among the eight).

**Also re-verified at this pin:** the `--features all` refusal wording
(`(?<...) requires module 'named-groups' (pattern offset 3)`; `\Q requires
module 'quoting'`), and the three registry archives (axes 69 → **70** rows
/ 23 axes, ONE new `engine-route` row at order 2 renumbering the six below
it; limits **45 rows byte-identical**; definitions **50 rows
byte-identical** — o42 and w12 added no numeric limit and no definition).

**[B37] at 334fd10e (2026-09-05), the abi 17-22 re-pin.** Registries:
axes 72/24 → **74/25** (ONE new axis, `alt-island`, two `predicate` rows
with no stamp_value — the macro is a count); definitions **50 rows
byte-identical** for the fifth pin running; limits 45 → **55** (nine
`VM_ISL_*` / `VM_INLINE_CHAIN_MAX_BYTES` knees and budgets, [OPT-EDGE] STEP
1.1's `PCREC_MIN_SCAN_CHAIN` 2, and `PCREC_MAX_SCAN_EDGES`'s desc reworded:
an edge costs NO compare on the generic path since the dispatch). The
`--features all` refusal wordings re-verified (`named-groups` offset 3,
`quoting` offset 0). The size books: +275 B flat on every plain frameless
VM artifact (three stamp lines + the `forward` chain), +31 B on every
edge-free DFA artifact (the folds line), the edge dispatch's own bytes on
edge-bearing machines (iso-ts +1,468 over 8+4 edges; `foo[0-9]+bar` +384),
and the fold witnesses SHRINK in the OBJECT rather than the source
(cls-upto-4's `-O2` object: `.text` 681 → 537, `.rodata` 580 → NONE;
dig-upto-16 forced-VM `.text` 1,449 → 633 — I-41 predicted 627 → 47 and
1,561 → 1,417 on pcrec's own gcc; the direction reproduces, the numbers are
this box's). The `-fno-scan-edge` deny row's denied arm 367,390 → 252,587
(folds 2 → 1: the restored tables fold where uniform) and STILL warns at
the 250,000 default, by 2,587 B. The clang refusal set stays EMPTY. The
65535 NFA wall, the plain/`\z` overflow routes and every 288d505 stamp
value are unchanged.
