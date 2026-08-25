# testees/pcrec/ — the pcrec adapter

Provides five testees at the commit pinned in `configs.toml`, and one —
`pcrec-local` — at no pin at all:

| config id | pcrec flags | what it is for |
|---|---|---|
| `pcrec-auto` | `--features all` | the defaults: engine chosen automatically, captures on |
| `pcrec-nocaps` | `+ --no-captures` | the axis that recovers a pure-DFA artifact for a group-bearing pattern |
| `pcrec-vm` | `+ --engine=vm` | the VM forced, prefilter off, so the VM derives the whole span independently |
| `pcrec-auto-in` | `--features all` + `buffer_frames = 32768`, `buffer_trail = 131072` | the defaults, matched through the `_in` entries with a caller-provided frame buffer. INERT wherever `auto` picks the DFA — which at pin 692c2e8 is every artifact of `bench/email`, so it is DEFINED but NOT MEASURED there (the checks use it; it goes live on a sub-bench with VM-selected patterns under `auto`) |
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
