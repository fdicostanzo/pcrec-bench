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

### MEASURED against pin 8da6120, 2026-08-25 — verified, not assumed

| pattern / form | config | engine | ncaps | emitted C |
|---|---|---|---|---|
| `orig` plain | auto | **dfa** | 1 | 43 669 B |
| `orig` `\z` | auto | **dfa** | 1 | 49 090 B |
| `orig` plain | nocaps | dfa | 1 | 43 671 B |
| `orig` `\z` | nocaps | **dfa** | 1 | 49 092 B |
| `orig` `\z` | vm | vm | 1 | 46 974 B |
| `factored` plain / `\z` | auto | vm | 5 | 44 102 / 44 238 B |

1. **`orig`'s `\z` form still selects the DFA engine** under `auto` and
   `nocaps`. The prediction holds.
2. **The byte-class skip prefilter is still there**, and its
   `rx_can_begin_match` table is BYTE-IDENTICAL between the two forms
   (same sha256 over the table body). But the skip LOOP is not identical
   and the difference is load-bearing: the plain form skips while
   `scan_position < subject_length` and `return 0`s when it runs off the
   end; the `\z` form skips only while `scan_position + 1 <
   subject_length` and cannot early-exit, because the end-of-subject
   "end view" state (`rx_forward_end_view`) has to be evaluated. **The
   prefilter is present but strictly weaker in the `\z` form** — it can
   never skip the final byte. Expect the `\z` artifact to cost slightly
   more per scan, and do not read a difference between the two forms as
   an engine-selection effect.
3. The `\z` form costs **+12.4 % emitted C** on `orig` and **+0.3 %** on
   `factored`.
4. **`\z` requires pcrec's `assertions` module.** Every pcrec config
   already passes `--features all`, so no config change was needed — but
   a future config that narrowed the feature set would break the match
   regime rather than the pattern.

### The gap this measurement found

**The DFA prefilter is NOT observable through any structured stamp, so
`engine_metadata` cannot say whether it is on.** `RX_VM_PREFILTER` is a
VM-only stamp (record_schema.md §7: the `VM_*` stamps are emitted on VM
artifacts only), and a DFA artifact's only `#define`s are
`RX_ALTCLS_MERGES` / `RX_ALTCLS_FACTORED`. The prefilter's presence above
was established by reading the emitted skip LOOP — prose and code, not a
stamp — which is exactly what requirements §4.2 says a metadata pair must
not be built from. Requirements §4.2 wants reports to "bucket outliers by
MECHANISM", and the DFA prefilter is one of this sub-bench's headline
mechanisms (pcrec's own srEmail measured a ~23× prefilter loss). **A
DFA-side prefilter stamp is a candidate request to the pcrec manager**;
until it exists, no pcrec DFA record can be filtered on it.

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
