# testees/pcrec/ — the pcrec adapter

Provides five testees at the commit pinned in `configs.toml`, and one —
`pcrec-local` — at no pin at all:

| config id | pcrec flags | what it is for |
|---|---|---|
| `pcrec-auto` | `--features all` | the defaults: engine chosen automatically, captures on |
| `pcrec-nocaps` | `+ --no-captures` | the axis that recovers a pure-DFA artifact for a group-bearing pattern |
| `pcrec-vm` | `+ --engine=vm` | the VM forced, prefilter off, so the VM derives the whole span independently |
| `pcrec-auto-in` | `--features all` + `buffer_frames = 32768`, `buffer_trail = 131072` | the defaults, matched through the `_in` entries with a caller-provided frame buffer. INERT wherever `auto` picks the DFA — which is still every artifact of `bench/email` (RE-VERIFIED at pin 35e1ab1, 2026-08-28: all six `auto`/`nocaps` artifacts stamp `RX_ENGINE "dfa"`), so it is DEFINED but NOT MEASURED there (the checks use it; it goes live on a sub-bench with VM-selected patterns under `auto`) |
| `pcrec-vm-in` | `+ --engine=vm` + the same two capacities | RULED 2026-08-25 (manager + pcrec manager; Frank's word pending via the inbox): the VM forced with the buffer, the one entry on `bench/email` where the depth path is reachable and the capacities were measured — the sixth cell of the [B8] window |
| `pcrec-local` | `--features all` + `$PCREC_LOCAL_FLAGS` | **a PROVIDED binary, `$PCREC_BIN`** ([B10], Frank's I-4 (c)): the edit-test loop's testee. No pin, SCRATCH TIER BY CONSTRUCTION, never in `store/`, never ranked. See below |

| file | role |
|---|---|
| `adapter.py` | the six configs; the pin; `binary_for()` (the ONE place the binary is chosen: the pin's, or `$PCREC_BIN`); `local_provenance()` (the `local:` version); the engine-metadata DECLARATION; the `buffer_*` config → driver argv plumbing |
| `pin.sh` | `git archive <commit>` from pcrec into the build root, and `make` THERE |
| `shim.c` | **the one file in this project that knows pcrec's ABI** |
| `driver.c` | the timing driver; its `dlopen` is the third AOT compile phase; `--buffer-frames N --buffer-trail M` allocate the caller-provided regions once per run |
| `configs.toml` | the config ids, `pin = "<commit>"`, the `_in` testees' capacities with the measurement that chose them, and `[testees.pcrec-local]` (`local = true`, `binary = "PCREC_BIN"`, `extra_flags = "PCREC_LOCAL_FLAGS"`) |

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

### MEASURED against pin 692c2e8, 2026-08-25 — verified, not assumed

Re-measured at the re-pin (pcrec's [DD-14] close merge; its compiler is
byte-identical to 17469b6, the [DD-14.FB] merge). "Emitted C" is the byte
size of the `artifact.c` that `pcrec -p rx <flags> -o artifact.c -- <text>`
writes; it does not embed the output path.

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

Each is an `AdapterError` naming both values. An absent MACRO is checked
only against the field's own absence — rule 1, applied to the control
rather than to the datum.

### The ABI FLOOR, and where it lives

`shim.c` reads `rx_info.scan` / `.prefilter`, appended at pcrec abi 6, so 6
is the lowest artifact it can read and `PB_SHIM_MIN_ABI` says so ONCE.
`driver.c` compares `pb_abi()` against it before reading anything else and
refuses a lower artifact by name (`error abi-below-shim-floor: …`, carrying
both numbers, exit 3); `adapter.py` recognises that line and re-raises it
as a clean `AdapterError` **without keeping a second copy of the number**.
An artifact older still (abi < 6) does not link this shim at all — the
field access is a compile error, which is the loudest form of the same
refusal and cannot be mistaken for a measurement.

`make check-harness`'s `abi floor` block is the SABOTAGE that keeps the
path exercised: a real artifact's `.abi = 8` edited to `5` in a copy, built
with the ordinary shim and run by the ordinary driver, must be refused by
name — with the unmodified artifact loading in the same run as the positive
control, and the token the adapter watches for checked against the
diagnostic the driver actually produced (two copies of one string, in two
languages, with nothing else enforcing that they agree).

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
`check_dfa_table_deny_flag` uses `-fno-premul-table` (tuning.md §2.13, an
answer-identity-preserving deny flag) through `pcrec-local` to reach
`indexed` on the census's own witness pattern.

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
