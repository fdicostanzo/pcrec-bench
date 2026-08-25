# testees/pcrec/ — the pcrec adapter

Provides three testees, all at the commit pinned in `configs.toml`:

| config id | pcrec flags | what it is for |
|---|---|---|
| `pcrec-auto` | `--features all` | the defaults: engine chosen automatically, captures on |
| `pcrec-nocaps` | `+ --no-captures` | the axis that recovers a pure-DFA artifact for a group-bearing pattern |
| `pcrec-vm` | `+ --engine=vm` | the VM forced, prefilter off, so the VM derives the whole span independently |

| file | role |
|---|---|
| `adapter.py` | the three configs; the pin; the engine-metadata DECLARATION |
| `pin.sh` | `git archive <commit>` from pcrec into the build root, and `make` THERE |
| `shim.c` | **the one file in this project that knows pcrec's ABI** |
| `driver.c` | the timing driver; its `dlopen` is the third AOT compile phase |
| `configs.toml` | the config ids and `pin = "<commit>"` |

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

## Give-ups

A budget give-up (`PCREC_ERR_STEPS` -2, `_FRAMES` -3, `_WORK` -4) propagates
to the driver as `giveup:<code>` and is judged `did-not-match-as-expected`,
with the code in the row's `diagnostic`. It is therefore not timed. See
`bench/email/NOTES.md` for why there is no `gave-up` outcome.

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
