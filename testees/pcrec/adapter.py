"""testees/pcrec/adapter.py -- the pcrec adapter (harness contract 3).

Provides `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, their clang siblings
`pcrec-auto-clang` / `pcrec-nocaps-clang` / `pcrec-vm-clang`, their
raised-emitted-size-cap siblings `pcrec-auto-bigcap` / `pcrec-vm-bigcap`,
and the caller-provided frame-buffer variants `pcrec-auto-in` /
`pcrec-vm-in`, all at the pin in `configs.toml` -- and `pcrec-local`, a
PROVIDED binary at no pin at all.

THE COMPILEE TOOLCHAIN AXIS ([B24]; pcrec [CC-CLANG]). pcrec emits C and
stops, so the compiler that turns that C into a .so is OURS -- phase 2 below
-- and it is a property of the testee, spelled `cc = "gcc" | "clang"` in
configs.toml (whose comment carries the ruling and the precedence). A config
that declares none behaves exactly as it did before the key existed ($CC,
else gcc; no `config_extra`; the same build_flags string). A config that
declares one PINS it: `config_extra = "cc-<name>"` joins the derived
testee_id, build_flags names the compiler and its `--version` first line, and
a conflicting `$CC` is refused rather than allowed to make the id lie. The
timing driver is built by `build_driver()` from `$CC` on every config, so a
clang testee differs from its gcc sibling in exactly one variable.

THE EMITTED-SIZE CAP AXIS ([B31]; pcrec [ART-SIZE], limits.md 8). pcrec's
two size caps are raise-only per compile, and a config may raise them:
`max_emit_bytes = N` / `max_emit_code_bytes = N`, both optional, both
BYTES. Absent, nothing changes -- no flag on the argv, no clause in
build_flags, no `config_extra`, the same derived testee_id. Present, the
flags ride in `flags` (one list feeds argv, build_flags and
runtime_options), the VALUES join `config_extra`, and a value below
pcrec's archived default is refused BY NAME before anything is measured.
It is an AXIS and not a gate removed: a raise also moves the size-term
ladder's own abort bound, so two artifacts built under different caps are
two artifacts. `compose_config_extra` is the ONE place `config_extra`'s
parts are ordered -- the axes in chartering order, so the slug only ever
grows by appending.

THE LOCAL TESTEE (Frank's I-4 (c), [B10]; record_schema.md 6.2 and 6.8).
`$PCREC_BIN` names the binary, `$PCREC_LOCAL_FLAGS` adds flags; pin.sh is
never called. `describe()` reports `engine_version = local:<first 12 hex of
the binary's sha256>`, plus `+<git describe --always --dirty --tags>` when a
repository sits beside the binary (walking up from its directory to a `.git`
FILE or directory -- a pcrec worktree has a file; a `git archive` pin has a
`PIN.tsv` and no repository, and the walk stops there), `engine_commit` =
HEAD when that tree is clean and null when it is dirty, `tier: scratch`, and
`testee.binary` = {path, sha256}. SCRATCH BY CONSTRUCTION: the harness reads
`tier()` before it gates or measures, and the store refuses the record into
the canonical tree. `engine_mode` and `captures` are DERIVED from the
effective flags (`--engine=vm` -> `vm`, `--no-captures` -> `off`) so the
testee_id says what ran -- and so are the two emitted-size caps, from the
same flag list. Everything after describe() -- emit-c / gcc / load,
shim.c, driver.c, the metadata, the `_in` buffers -- is the same code path as
the pinned testees: `binary_for()` is the one place the binary is chosen.

THE `_in` TESTEES (pcrec docs/spec/match_api.md 10, [DD-14.FB]): a config
carrying `buffer_frames = N` and `buffer_trail = M` -- CAPACITIES in frames
and trail entries, never bytes -- makes the driver allocate two regions once
per run and call `<prefix>_search_in` / `<prefix>_match_caps_in` with them in
every regime. The sizes are THE KNOB and they go in the record twice: as
`testee.runtime_options` (the configuration) and as the `buffer_frames` /
`buffer_trail` engine_metadata pairs on the compile row (what the driver
actually ran with; ABSENT means the stamped default storage ran, which is
also what happens on a DFA artifact, whose stamped frame size is 0 and which
takes no buffers at all -- 10.4). requirements 4.2: it is a separate
(engine, version, configuration) triple, hence a separate roster entry with
its own engine_mode slug (`auto-in`, `vm-in`) so the derived testee_id is
distinct.

COMPILE COST -- AOT, THREE PHASES (requirements 3: "pattern -> C -> gcc ->
loadable object, all phases, each timed"):

    emit-c   the `pcrec` CLI turning the pattern into artifact.c/.h   [python]
    gcc      $CC -O2 -fPIC -shared shim.c (which #includes artifact.c)
             -> artifact-N.so                                         [python]
    load     dlopen of that .so                                       [driver]

Each TRIAL builds its own `artifact-<trial>.so`. That is not tidiness: the
dynamic loader caches by path, so a second dlopen of one path is free and a
per-trial `load` number taken that way would be a measurement of the cache.

ENGINE METADATA comes from the artifact's STRUCTURED fields only
(requirements 4.2) -- `rx_info` read through `shim.c`, and the D46 `RX_VM_*`
preprocessor stamps read the same way. The prose `RX_ENGINE_WHY` is
explicitly NOT a metadata pair: it lands in the compile row's unindexed
`diagnostic`, which is where record_schema.md 7 puts it.

THE ABI FLOOR AND THE TWO SPELLINGS ([B16], pin 35e1ab1 = pcrec abi 8).
pcrec grew five pins' worth of observability between this bench's 692c2e8
pin and 35e1ab1, and this adapter absorbs all of it at once:

  abi 4 ([DD-13])   `RX_ENGINE` on EVERY artifact; `RX_DFA_SCAN` /
                    `RX_DFA_PREFILTER` on DFA artifacts.
  abi 5 ([OPT-1])   `RX_FAST_FRAMES` / `RX_FAST_TRAIL` on every VM artifact
                    -- the two-tier default entry's fast capacities.
  abi 6 ([DD-13c])  `RX_DFA_SCAN "empty"`; the two `_DFA_*` macros extended
                    to VM HYBRIDS; `rx_info.scan` / `.prefilter` appended.
  abi 7 ([OPT-3])   `RX_DFA_TABLE`.
  abi 8 ([ENG-FORM]) nothing a consumer reads -- the emitted scan loop moved.

[B18] (pin 36d5963 = pcrec abi 11) absorbed three more in one change:

  abi 9 ([OPT-K])    `RX_DFA_PREFILTER` gains `offset-set` /
                     `offset-set-bounded`; `RX_DFA_PREFILTER_OFFSETS`
                     (`"0,8*,13"` / `"none"`) on every artifact that
                     contains a DFA scan; `-fno-offset-skip` (bit 16).
  abi 10 ([ENG-ABS]) `RX_DFA_MATCH` (`unwrapped` / `search-filter`) on every
                     DFA artifact and NO VM artifact, hybrids included;
                     `rx_info.match_form` appended as its mirror (NULL where
                     the macro is absent); `-fno-anchored-dfa` (bit 17).
  abi 11 ([ART-SIZE]) `RX_UNROLL_K` / `RX_UNROLL_K_WHY` (seven values) and
                     `RX_MAX_EMIT_CODE_BYTES` on every VM artifact;
                     `RX_MAX_EMIT_BYTES` on every artifact; `-fno-size-term`
                     (bit 18) denies the K selection, never the caps.

[B19] (pin 96e44c2 = pcrec abi 12, inbox I-18) absorbed one more, plus two
adapter-side facts that are not stamps at all:

  abi 12 ([OPT-4])   `RX_ENGINE_SEL` on EVERY artifact, both engines -- one
                     token from the registry's `engine-route` axis
                     (`selected` / `forced` / `overflowed-dfa` /
                     `overflowed-prefilter` / `collapsed-prefilter`): the
                     decision `RX_ENGINE_WHY` narrates, as a closed set
                     (O-8 6(d), RULED). `RX_VM_PREFILTER_LANG` (`exact` /
                     `count-collapsed`) and `RX_VM_PREFILTER_LANG_WHY` on
                     every VM HYBRID -- where `RX_VM_PREFILTER` reads
                     `hybrid` -- and on NO other artifact (match_api.md 6.3;
                     I-18 said "every VM artifact", the artifacts and the
                     spec say hybrids: a forced `--engine=vm` artifact has
                     no prefilter and stamps neither). `-fno-prefilter-
                     collapse` (bit 19) denies both retry rungs;
                     `-fprefilter-collapse` (bit 20) forces the collapse.
  (adapter)          `emit_bytes` / `emit_code_bytes`: the artifact's C
                     source measured by pcrec's OWN definition (compile.c's
                     `emit_size_measure`, ported to `emit_size()` below and
                     CONTROLLED against the pin's `--warn-emit-bytes`
                     message, which prints both numbers, wherever it fires):
                     total bytes minus comment bytes (the size log's
                     quantity, what `RX_MAX_EMIT_BYTES` caps), and that
                     minus table initializers (what `_CODE_BYTES` caps).
                     Both files pcrec emits (.c + .h) are summed, as pcrec
                     sums them. `warned_emit_bytes`: present ONLY when the
                     compile printed the advisory `--warn-emit-bytes` line
                     (default 250,000; the warning is NEVER a failure, the
                     exit code is 0 and the artifact is what it would have
                     been); the value is the total the message names, and
                     the line itself is appended to the row's diagnostic.

[B22] (pin 263b013, still abi 12; inbox I-21 correction / I-22 / I-25)
absorbed two new VALUES and one new surface -- no new stamp, no abi bump:

  (values)           `RX_ENGINE_SEL` gains `declined-nullable` ([OPT-4.1]:
                     a retry rung OFFERED the count-collapsed prefilter and
                     DECLINED it because the collapsed language is nullable;
                     no prefilter survives, so the artifact reads
                     `RX_VM_PREFILTER "none"` and carries NO language pair
                     -- the 6.3 iff, both directions) and `size-cap-retry`
                     ([LIM-1]: the [OPT-4] size rung's SUCCESS, which
                     stamped `selected` at 96e44c2 -- the mislabel O-8/O-10
                     flagged, closed; the fallback bucket reads the VALUE
                     now, never the `_LANG_WHY` prefix). And
                     `RX_VM_PREFILTER_LANG_WHY` gains `nullable collapsed
                     language` (`-fprefilter-collapse` with no rung: the
                     flag reached a POLICY, the prefilter is kept and built
                     from the EXACT language -- pcrec tuning.md 2.17).
  (surface)          `pcrec --list-limits`, the 44-row numeric-limits table
                     (pcrec D90), archived as `list_limits.tsv` -- the
                     THIRD registry archive target beside list_axes /
                     list_definitions.

[B25] (pin a7e0bdf = pcrec abi 13, inbox I-27) absorbed one more:

  abi 13 ([OPT-5])   `RX_DFA_SCAN_EDGE` on every artifact that CONTAINS a
                     DFA scan -- the scan family's own iff, joined
                     unchanged (match_api.md 6.3): HOW the scan tests the
                     class of a SCAN EDGE, the address-only bounded-scan
                     block that replaced a counted class run's interior
                     states (STEP 1; the states are DELETED, so this is
                     the first abi bump that moved a MACHINE and not only
                     emitted text). `range` (contiguous class: subtract-
                     and-compare, no memory but the subject) / `bitmap`
                     (a 256-byte membership read, VALUE-addressed) /
                     `mixed` (machines took both forms) / `none` (no
                     collapsible run; `attempt` / `empty` scans; or
                     denied). TWO registry axes (tuning.md 2.18, D82):
                     `scan-edge` (per state -- what `-fno-scan-edge`,
                     bit 21, denies) and `scan-body` (per edge -- what
                     the stamp reports); `PCREC_MAX_SCAN_EDGES` (4)
                     joined --list-limits (45 rows). No rx_info mirror
                     (struct rx_info byte-identical 12 -> 13), so the
                     shim floor stays 10.

[B26] (pin 1989c62 = pcrec abi 15, inbox I-29/I-30) absorbs TWO pins in one
adapter change -- cc/o42 (abi 14) and w12 (abi 15):

  abi 14 ([OPT-4.2]) an EIGHTH `RX_ENGINE_SEL` value and nothing else a
                     consumer sees: `declined-nullable-default` -- the same
                     nullability policy as [OPT-4.1]'s `declined-nullable`
                     with NO RUNG involved. Nothing overflowed; the ORDINARY
                     hybrid's own EXACT prefilter language is nullable (it
                     matches the empty string, so the forward+reverse pair
                     could never dismiss a position), so the prefilter is
                     declined: the artifact reads `RX_VM_PREFILTER "none"`
                     and carries NO language pair -- match_api.md 6.3's iff
                     both ways, asserted in both directions here. The
                     `--list-axes` engine-route row joins at ORDER 2, right
                     after `forced`, and every later row's order shifts by
                     one (the only registry movement at this pin). pcrec's
                     [CC-CLANG] `&&label` fix rides the same abi and adds no
                     stamp: its bench-visible consequence is that every VM
                     artifact now compiles under clang ([B24]'s refusal set
                     goes EMPTY).
  abi 15 ([DD-13b.W1.2]) `rx_info.name` and `rx_info.nentries` APPENDED
                     after `match_form` -- read-only additions, no existing
                     member's offset moved. The FIRST rx_info growth since
                     abi 10, so the standing floor rule ("it rises iff a
                     FIELD joins what the shim reads") fires for the second
                     time in this file's life: shim.c reads both, and
                     `PB_SHIM_MIN_ABI` goes 10 -> 15. They are PROVENANCE,
                     not selection: `artifact_name` is what the artifact IS
                     as against what its symbols are called (never NULL by
                     contract -- asserted), `nentries` is the whole
                     `groups[]` length of which `nnames` counts a prefix
                     (`nentries >= nnames` asserted; equality is today's
                     MEASURED fact, checked by value in selfcheck rather
                     than assumed here). Neither has a macro spelling, so
                     neither is a two-spellings pair.
  (sizes)            NOT a stamp change, but the size books move at this pin
                     in two predicted ways: w12's 519 B/artifact comment fix
                     lowers `emit_bytes` tree-wide, and an artifact whose
                     language o42 declines SHRINKS dramatically. Both are
                     re-derived here against the pin's own
                     `--warn-emit-bytes` numbers, so a movement that is NOT
                     one of those two fails by name.

Two rules govern how they are read, and both exist because they were paid
for on the pcrec side first:

1. NEVER INFER A FACT FROM A STAMP'S ABSENCE (pcrec I-5: it broke four of
   pcrec's own checks the day the stamps landed). READ THE VALUE. A macro
   this adapter does not see is recorded as no pair at all -- which
   record_schema.md 7 already defines as "not stamped", a fact distinct
   from every value. The single reading that IS taken from an absence is
   the spec's own iff and comes from a FIELD, printed on every artifact so
   it is never taken from silence: `rx_info.scan == NULL` on a VM artifact
   IS "not a hybrid" (match_api.md 6, consequence 2).
2. ONE DERIVATION PER COLUMN, and where pcrec publishes a fact TWICE the
   two spellings are CHECKED AGAINST EACH OTHER rather than both recorded.
   `engine` is `rx_info.engine`, checked against `RX_ENGINE`; `dfa_scan` /
   `dfa_prefilter` are the macros, checked against `rx_info.scan` /
   `.prefilter`; `dfa_match` is the macro, checked against
   `rx_info.match_form`. A disagreement is an AdapterError naming both
   values -- pcrec asserts field == macro on every artifact of both engines
   (`tests/codegen/run_dfa_stamps.sh`), so a disagreement seen here is a
   pcrec bug or a shim bug and is worth stopping for, not averaging.
3. AN UNCONDITIONAL STAMP THAT IS MISSING IS A CONTRACT VIOLATION, NOT A
   BLANK ([B18]). pcrec stamps its selection facts whether or not they
   fired (its D81), each with a scope and the abi it landed at.
   `STAMP_SCOPE` states both per pair; `_check_agreement` asserts that at
   the artifact's own abi every such pair IS present within its scope and
   ABSENT outside it (the exclusive scopes: `dfa_match` on no VM artifact,
   the size term's VM-only trio on no DFA artifact, [B19]'s language pair
   on no artifact that is not a VM hybrid). The shim still reads
   the macros through #ifdef so an artifact between the floor and a
   macro's abi links and records "not stamped" -- and this rule is what
   keeps that #ifdef from ever hiding a stamp that should have been there.
4. A STAMP WITH NO MIRROR IS CHECKED AGAINST WHAT IT IMPLIES ([B19]).
   `RX_ENGINE_SEL` has no rx_info field, so its control is the CONFIG and
   the stamps beside it: `forced` IFF the testee named `--engine=`;
   `collapsed-prefilter` and ([B22]) `size-cap-retry` imply a VM hybrid
   whose language is `count-collapsed`; the two `overflowed-*` values,
   ([B22]) `declined-nullable` and ([B26]) `declined-nullable-default`
   imply a VM artifact with no prefilter -- and the two DECLINE values
   imply the absence of the language pair as well, the iff's other
   direction (match_api.md 6.3's table, read as implications).
5. A FIELD WITH NO STAMP IS CHECKED AGAINST ITS OWN CONTRACT ([B26]).
   `rx_info.name` and `.nentries` (abi 15) are spelled nowhere else, so
   there is no second spelling to check them against; what the spec DOES
   give is a contract per field -- `name` is never NULL, and `nnames`
   counts a PREFIX of `groups[]` so `nentries >= nnames`. Both are
   asserted. The stronger fact (they are EQUAL on every artifact pcrec
   emits today) is deliberately NOT asserted here: it is true of this
   pin's corpus and is checked by value in tools/selfcheck.py, so `.rxt`
   composition landing later separates the two without the adapter
   refusing the first artifact that does it.

The ABI FLOOR lives in `shim.c` (`PB_SHIM_MIN_ABI`, 15 since [B26] -- the
abi that appended `name` and `nentries`, the fourth and fifth fields it
reads; 10 from [B18] for `match_form`, 6 before that for `scan` /
`prefilter`) and is enforced in `driver.c`, which
refuses a lower artifact by name before printing anything else. This file
does NOT keep a second copy of the number: it recognises the driver's
refusal line and re-raises it as an AdapterError carrying pcrec's own two
numbers. Two copies of one floor is exactly the shape of check that has
failed this project before.
"""

import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))

from pcrecbench import adapters as _ad                       # noqa: E402
from pcrecbench import record as _rec                        # noqa: E402
from pcrecbench.driverrun import (C_ENV, build_driver,       # noqa: E402
                                  per_trial, run_driver)

HERE = os.path.dirname(os.path.abspath(__file__))
PIN_SH = os.path.join(HERE, "pin.sh")
PCREC_SRC = os.environ.get("PCREC_SRC", "/home/duxevents/pcrec")
BENCH_ROOT = os.path.dirname(os.path.dirname(HERE))

# record_schema.md 6.3's registry for pcrec: what `--engine=` may name.
ENGINE_MODES = ("auto", "dfa", "vm")

# record_schema.md 7's worked example, as a DECLARATION. Every pair the
# driver can emit is here with its type, scope and SOURCE; an undeclared pair
# is a validator error (X15), so this table and shim.c move together.
RXINFO_SRC = "rx_info.%s, read through testees/pcrec/shim.c's pb_%s()"
METADATA_DECL = {
    "engine": {
        "type": "enum", "scope": "pattern", "values": ["dfa", "vm", "unknown"],
        "source": "rx_info.engine (PCREC_ENGINE_DFA=1 / PCREC_ENGINE_VM=2), "
                  "read through pb_engine(); CHECKED against <PREFIX>_ENGINE "
                  "(pb_engine_stamp(), unconditional since pcrec abi 4) -- "
                  "the macro is not a second pair, it is this one's control",
        "description": "the engine the artifact was built with",
    },
    "abi": {"type": "integer", "scope": "pattern",
            "source": RXINFO_SRC % ("abi", "abi"),
            "description": "the reflection struct's layout version"},
    "ncaps": {"type": "integer", "scope": "pattern",
              "source": RXINFO_SRC % ("ncaps", "ncaps"),
              "description": "caps[] slot count, all-in (== <PREFIX>_NCAPS)"},
    "ngroups": {"type": "integer", "scope": "pattern",
                "source": RXINFO_SRC % ("ngroups", "ngroups"),
                "description": "capturing groups in the pattern TEXT, a "
                               "lexical fact independent of --no-captures"},
    "nnames": {"type": "integer", "scope": "pattern",
               "source": RXINFO_SRC % ("nnames", "nnames"),
               "description": "named groups in rx_info.groups[]"},
    # -- the abi-15 PROVENANCE fields ([DD-13b.W1.2], pin 1989c62, [B26]).
    # Neither has a macro spelling, so neither is a two-spellings pair: they
    # are recorded, and their own contracts (`name` never NULL, `nentries >=
    # nnames`) are what `_check_agreement` asserts instead of a stamp.
    "artifact_name": {
        "type": "string", "scope": "pattern",
        "source": RXINFO_SRC % ("name", "info_name"),
        "description": "what the ARTIFACT is, as against what its symbols "
                       "are CALLED (`<prefix>`): a `.rxt` definition built "
                       "under three configs is three prefixes and ONE name, "
                       "which is what a consumer walking several "
                       "`<prefix>_info` symbols in one binary needs. NEVER "
                       "NULL by contract -- a compile that supplies no name "
                       "stamps its own `<prefix>` -- so a NULL is a contract "
                       "violation, not an `unnamed` artifact. On this bench "
                       "every artifact is compiled `-p rx` from pattern "
                       "TEXT, never from a `.rxt` source, so the value is "
                       "`rx` on every record until a set charters one",
    },
    "nentries": {
        "type": "integer", "scope": "pattern",
        "source": RXINFO_SRC % ("nentries", "info_nentries"),
        "description": "rows in rx_info.groups[], ALL of them. `nnames` "
                       "counts the PRIMARY pattern's own named groups, which "
                       "are a PREFIX of the array, so `nentries >= nnames` "
                       "always (asserted) and the two are EQUAL on every "
                       "artifact pcrec emits today (measured, not assumed -- "
                       "what will separate them is `.rxt` composition "
                       "injecting a definition's own named groups, "
                       "[DD-13b.W1.3])",
    },
    "step_budget": {"type": "integer", "scope": "pattern",
                    "source": RXINFO_SRC % ("step_budget", "step_budget"),
                    "description": "backtrack resumptions before "
                                   "PCREC_ERR_STEPS; -1 = none"},
    "work_budget": {"type": "integer", "scope": "pattern",
                    "source": RXINFO_SRC % ("work_budget", "work_budget"),
                    "description": "forward work units before PCREC_ERR_WORK; "
                                   "-1 = none"},
    "frame_capacity": {"type": "integer", "scope": "pattern",
                       "source": RXINFO_SRC % ("frame_capacity", "frame_capacity"),
                       "description": "resume-stack capacity; -1 = unbounded"},
    "subject_ceiling": {"type": "integer", "scope": "pattern",
                        "source": RXINFO_SRC % ("subject_ceiling", "subject_ceiling"),
                        "description": "stamped honest ceiling, 0 = unset"},
    "prefilter": {
        "type": "enum", "scope": "pattern", "values": ["hybrid", "none"],
        "source": "<PREFIX>_VM_PREFILTER, read through pb_vm_prefilter()",
        "description": "the [M4.6f] prefilter decision, in the VM's OWN "
                       "vocabulary: does the VM run a capture-erased DFA "
                       "ahead of its program at all. VM artifacts ONLY -- a "
                       "DFA artifact emits no such stamp, and an ABSENT pair "
                       "is not an error. It is a DIFFERENT SELECTION from "
                       "`dfa_prefilter`, not a coarser spelling of it "
                       "(match_api.md 6.3 (a)): a hybrid answers both, and "
                       "the answers are independent",
    },
    "vm_rungs": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_RUNG_CURSOR", "PCREC_VM_RUNG_FRAMES_BOUNDED",
                 "PCREC_VM_RUNG_FRAMES_UNBOUNDED", "PCREC_VM_RUNG_REVDET",
                 "PCREC_VM_RUNG_COUNTER"],
        "source": "<PREFIX>_VM_RUNGS (D46), read through pb_vm_rungs()",
        "description": "the rungs used, OR'd per quantifier body",
    },
    "vm_strats": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_STRAT_POSSESSIVE", "PCREC_VM_STRAT_BACKTRACKING"],
        "source": "<PREFIX>_VM_STRATS, read through pb_vm_strats()",
        "description": "the ladder's first-rung strategy, per quantifier",
    },
    "vm_prunes": {
        "type": "mask", "scope": "pattern",
        "bits": ["PCREC_VM_PRUNE_CLAMPED", "PCREC_VM_PRUNE_UNCLAMPED"],
        "source": "<PREFIX>_VM_PRUNES, read through pb_vm_prunes()",
        "description": "length-prune form, per quantifier",
    },
    # -- THE DFA SCAN's own selection facts ([DD-13] abi 4, extended to VM
    # HYBRIDS at [DD-13c] abi 6; [OPT-3]'s table at abi 7). match_api.md 6.3
    # (a) states the scope as an IFF: these are on every artifact that
    # CONTAINS a DFA scan -- every DFA artifact AND every VM hybrid -- and on
    # no other artifact. An absent pair therefore means "this artifact has no
    # DFA scan" OR "this pcrec did not stamp it"; the adapter never collapses
    # the two, and never reads either as an engine. `rx_info.scan` /
    # `.prefilter` are the runtime mirrors and are used as the CONTROL on the
    # two macros, not recorded a second time.
    "dfa_scan": {
        "type": "enum", "scope": "pattern",
        "values": ["unanchored", "attempt", "empty"],
        "source": "<PREFIX>_DFA_SCAN, read through pb_dfa_scan(); CHECKED "
                  "against rx_info.scan (pb_info_scan(), abi 6+)",
        "description": "WHICH DFA scan this artifact contains: the O(n) "
                       "forward+reverse table pair (`unanchored`), the "
                       "per-start computed-goto loop an anchored pattern "
                       "takes (`attempt`), or a provably-empty body that is "
                       "one `return 0` (`empty`). Different loops with "
                       "different cost curves, and nothing else a consumer "
                       "can read distinguishes them",
    },
    "dfa_prefilter": {
        "type": "enum", "scope": "pattern",
        "values": ["none", "memchr", "byte-class", "memchr-bounded",
                   "byte-class-bounded", "offset-set", "offset-set-bounded"],
        "source": "<PREFIX>_DFA_PREFILTER, read through pb_dfa_prefilter(); "
                  "CHECKED against rx_info.prefilter (pb_info_prefilter()); "
                  "the value set is CHECKED against `pcrec --list-axes` "
                  "(testees/pcrec/list_axes.tsv, axis `prefilter`)",
        "description": "the CANDIDATE-START mechanism that DFA scan carries. "
                       "`none`'s largest cause is that the start state "
                       "ACCEPTS (no skip is sound), not that no filter was "
                       "wanted. The two `-bounded` values are a real "
                       "difference in what the mechanism buys under a "
                       "$/\\Z/\\z view -- every skip stops one byte short "
                       "and the memchr arm loses its early-out -- and not a "
                       "spelling of the unbounded pair. The two `offset-set` "
                       "values ([OPT-K], pcrec abi 9) scan for ONE byte at a "
                       "chosen offset k* inside the fixed-length prefix and "
                       "verify the other offsets per candidate; WHICH offsets "
                       "is `dfa_prefilter_offsets`",
    },
    "dfa_prefilter_offsets": {
        "type": "string", "scope": "pattern",
        "source": "<PREFIX>_DFA_PREFILTER_OFFSETS ([OPT-K], pcrec abi 9+), "
                  "read through pb_dfa_prefilter_offsets(); same scope as "
                  "dfa_scan (every artifact that CONTAINS a DFA scan, VM "
                  "hybrids included); CHECKED to be \"none\" iff "
                  "dfa_prefilter is not an offset-set value",
        "description": "WHICH byte offsets from the candidate's own start the "
                       "offset-set filter tests, ascending, comma-separated, "
                       "`*` marking the one the scan searches for -- "
                       "`0,8*,13` on the uuid shape -- or `none` on every "
                       "artifact whose dfa_prefilter is not one of the two "
                       "offset-set values. A fact about the individual "
                       "MACHINE (free text), deliberately not folded into "
                       "dfa_prefilter's closed value set",
    },
    "dfa_scan_edge": {
        "type": "enum", "scope": "pattern",
        "values": ["none", "range", "bitmap", "mixed"],
        "source": "<PREFIX>_DFA_SCAN_EDGE ([OPT-5] STEP 1, pcrec abi 13+), "
                  "read through pb_dfa_scan_edge(); same scope as dfa_scan "
                  "(every artifact that CONTAINS a DFA scan, VM hybrids "
                  "included -- match_api.md 6.3: the iff joined unchanged); "
                  "no rx_info mirror; the value set is CHECKED against "
                  "`pcrec --list-axes` (axis `scan-body`)",
        "description": "HOW that scan tests the class of a SCAN EDGE -- a "
                       "maximal run of states differing only in how many "
                       "bytes of ONE fixed class have been counted, "
                       "replaced by a bounded cursor loop whose only "
                       "loop-carried value is the cursor and DELETED from "
                       "the transition table (tuning.md 2.18): `range` "
                       "(every edge tests a contiguous byte range -- "
                       "subtract-and-compare against two immediates), "
                       "`bitmap` (at least one edge's class is not "
                       "contiguous: a 256-byte membership read, addressed "
                       "by the byte just read, never by a previous load's "
                       "result), `mixed` (an artifact-level composition: "
                       "its machines took both forms), `none` (no machine "
                       "carries a collapsible run, an `attempt`/`empty` "
                       "scan, or -fno-scan-edge). The stamp reports the "
                       "`scan-body` axis; the companion `scan-edge` axis "
                       "(per STATE: edge at all?) is the one the deny "
                       "flag removes",
    },
    "dfa_match": {
        "type": "enum", "scope": "pattern",
        "values": ["unwrapped", "search-filter"],
        "source": "<PREFIX>_DFA_MATCH ([ENG-ABS], pcrec abi 10+), read "
                  "through pb_dfa_match(); CHECKED against rx_info.match_form "
                  "(pb_info_match_form()), which is NULL wherever the macro "
                  "is absent. Scope: every artifact whose engine is `dfa`, "
                  "and NO VM artifact, hybrids included -- it describes the "
                  "_match ENTRY, not a scan (match_api.md 6.3)",
        "description": "HOW `<prefix>_match` / `_match_caps` answer on a DFA "
                       "artifact: `unwrapped` (a THIRD, anchored forward "
                       "machine run from ctx->pos -- no reverse pass, a "
                       "failing probe stops at the first byte that cannot "
                       "continue a match here) or `search-filter` (the "
                       "unanchored search with non-pos starts rejected: "
                       "`attempt` and `empty` scans, an anchored machine "
                       "over PCREC_ANCHORED_MAX_STATES, or -fno-anchored-dfa)",
    },
    "unroll_k": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_UNROLL_K ([ART-SIZE], pcrec abi 11+), read "
                  "through pb_unroll_k(); VM artifacts only",
        "description": "the unroll factor the VM counter rung was emitted "
                       "at (8 by default); `unroll_k_why` says who chose it",
    },
    "unroll_k_why": {
        "type": "enum", "scope": "pattern",
        "values": ["default", "option", "denied", "size-model",
                   "size-model-declined", "cap-rescue", "capacity-declined"],
        "source": "<PREFIX>_UNROLL_K_WHY ([ART-SIZE], pcrec abi 11+), read "
                  "through pb_unroll_k_why(); VM artifacts only. The seven "
                  "values are match_api.md 6.3's / limits.md 8's; since pin "
                  "263b013 the registry's `size-term` axis carries a "
                  "stamp_value on every row ([B18]'s documented gap, closed "
                  "by pcrec [REG-SV]), so the value set is CHECKED against "
                  "`pcrec --list-axes` like the other name-valued macros",
        "description": "WHY unroll_k is what it is: `default` (the term ran, "
                       "the artifact was under its 120,000-code-byte "
                       "threshold), `option` (--unroll=K), `denied` "
                       "(-fno-size-term), `size-model` (the ladder's K was "
                       "taken), `size-model-declined` (the materiality bar "
                       "rejected it), `cap-rescue` (a size cap took it "
                       "anyway), `capacity-declined` (the K it wanted would "
                       "have lowered the declared frame_capacity / "
                       "subject_ceiling below the default's -- limits.md 8a)",
    },
    "max_emit_code_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_MAX_EMIT_CODE_BYTES ([ART-SIZE], pcrec abi 11+), "
                  "read through pb_max_emit_code_bytes(); VM artifacts only, "
                  "like the quantity it bounds",
        "description": "the EFFECTIVE cap on comment-excluded C bytes OUTSIDE "
                       "table initializers this artifact was built under "
                       "(500,000 by default; --max-emit-code-bytes=N is "
                       "raise-only). An emergency failsafe, not a tuned "
                       "threshold (pcrec D84)",
    },
    "max_emit_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_MAX_EMIT_BYTES ([ART-SIZE], pcrec abi 11+), read "
                  "through pb_max_emit_bytes(); EVERY artifact, both engines",
        "description": "the EFFECTIVE cap on total comment-excluded emitted "
                       "bytes this artifact was built under (1,000,000 by "
                       "default; --max-emit-bytes=N is raise-only), so an "
                       "artifact that fitted is distinguishable from one "
                       "built with a raised cap without the command line",
    },
    # -- [OPT-4] (pcrec abi 12, [B19]): the engine ROUTE as a closed set,
    # and the prefilter LANGUAGE pair. The route is on EVERY artifact; the
    # language pair is on every VM HYBRID and no other artifact -- a THIRD
    # independent selection beside `prefilter` (does the VM run a DFA ahead
    # of its program) and `dfa_prefilter` (what candidate-start filter that
    # DFA's scan carries): WHICH LANGUAGE that DFA recognises.
    "engine_sel": {
        "type": "enum", "scope": "pattern",
        "values": ["selected", "forced", "overflowed-dfa",
                   "overflowed-prefilter", "collapsed-prefilter",
                   "declined-nullable", "size-cap-retry",
                   "declined-nullable-default"],
        "source": "<PREFIX>_ENGINE_SEL ([OPT-4], pcrec abi 12+; two values "
                  "added at 263b013 -- [OPT-4.1]'s `declined-nullable` and "
                  "[LIM-1]'s `size-cap-retry` -- with no abi bump, and an "
                  "EIGHTH at abi 14 -- [OPT-4.2]'s "
                  "`declined-nullable-default`), read "
                  "through pb_engine_sel(); EVERY artifact, both engines; no "
                  "rx_info mirror -- CHECKED against the config (`forced` iff "
                  "--engine= was named) and against the prefilter stamps it "
                  "implies; the value set is CHECKED against `pcrec "
                  "--list-axes` (axis `engine-route`)",
        "description": "HOW the engine was chosen, as one token: `selected` "
                       "(auto chose on the AST and nothing overflowed -- the "
                       "common case on both engines), `forced` (--engine=vm "
                       "or =dfa, so auto selected nothing), `overflowed-dfa` "
                       "(auto, the DFA was to be the ENGINE, its build "
                       "overflowed a cap and no prefilter survived -- "
                       "[SEL-1]), `overflowed-prefilter` (auto, the VM was "
                       "already chosen and only its prefilter's DFA "
                       "overflowed, so the prefilter was dropped), "
                       "`collapsed-prefilter` (auto, a DFA build overflowed "
                       "a STATE cap and the [SEL-1] retry KEPT a prefilter "
                       "by rebuilding it from the count-collapsed language "
                       "-- [OPT-4]), `declined-nullable` (auto, a [SEL-1] OR "
                       "[OPT-4] retry OFFERED the count-collapsed prefilter "
                       "and DECLINED it because the collapsed language is "
                       "NULLABLE -- it matches the empty string, so the "
                       "filter could never dismiss a position; no prefilter "
                       "survives -- [OPT-4.1]), `size-cap-retry` (auto, an "
                       "emitted-SIZE cap refused the exact artifact and the "
                       "[OPT-4] size rung's count-collapsed prefilter "
                       "SURVIVED -- [LIM-1], replacing the `selected` "
                       "mislabel this bench's O-8/O-10 flagged), and "
                       "`declined-nullable-default` (abi 14, [OPT-4.2]: the "
                       "SAME nullability policy with NO rung involved -- "
                       "nothing overflowed, and the ORDINARY hybrid's own "
                       "EXACT prefilter language is nullable, so the "
                       "prefilter is declined; like `declined-nullable` the "
                       "artifact reads prefilter `none` and carries no "
                       "language pair). FIVE of the eight are `fell back` "
                       "in pcrec's own reading (match_api.md 6.3 excludes "
                       "`declined-nullable-default` from that five: nothing "
                       "overflowed on that path). THIS BENCH'S ask-(b) "
                       "bucket is the WIDER one Frank spelled -- `not in "
                       "(selected, forced)`, so the eighth value IS in it: "
                       "the question the bucket answers is `did auto end up "
                       "somewhere other than its ordinary choice`, and a "
                       "declined prefilter is such a place whether or not a "
                       "cap was hit. The divergence from pcrec's five is "
                       "DELIBERATE and stated here so a reader of the "
                       "report is never left to guess which reading the "
                       "column took. Since 263b013 the bucket reads the "
                       "VALUE and nothing else (never the `_why` prefix: "
                       "the size-cap rescue has its own token now)",
    },
    "vm_prefilter_lang": {
        "type": "enum", "scope": "pattern",
        "values": ["exact", "count-collapsed"],
        "source": "<PREFIX>_VM_PREFILTER_LANG ([OPT-4], pcrec abi 12+), read "
                  "through pb_vm_prefilter_lang(); every VM HYBRID (where "
                  "`prefilter` reads `hybrid`) and NO other artifact -- "
                  "match_api.md 6.3's own iff for this pair, checked in "
                  "both directions by STAMP_SCOPE; the value set is CHECKED "
                  "against `pcrec --list-axes` (axis `prefilter-lang`)",
        "description": "WHICH LANGUAGE the VM's prefilter DFA recognises: "
                       "`exact` (the pattern's own -- the DEFAULT under "
                       "ruling B, prefilter_count_independence.md 10a) or "
                       "`count-collapsed` (a sound SUPERSET: every X{m,n} "
                       "lowered to X{min(m,1),}, so the machine does not "
                       "scale with the count; the filter's rejection is "
                       "still sound and the answers identical, but it "
                       "cannot bound the match END, so the artifact reads "
                       "`RX_VM_PRUNE_CEILING subject-end`). Reached only by "
                       "-fprefilter-collapse or by a retry rung of "
                       "compile_driver's ladder -- `vm_prefilter_lang_why` "
                       "says which",
    },
    "vm_prefilter_lang_why": {
        "type": "string", "scope": "pattern",
        "source": "<PREFIX>_VM_PREFILTER_LANG_WHY ([OPT-4], pcrec abi 12+), "
                  "read through pb_vm_prefilter_lang_why(); same scope as "
                  "vm_prefilter_lang. FREE TEXT (two of its values carry a "
                  "number), so a `string` pair rather than an enum",
        "description": "WHY the language is what it is: `exact` / `no "
                       "counted repeat` (the default, nothing to collapse "
                       "or nothing collapsed), `forced` (-fprefilter-"
                       "collapse), `dfa overflow retry, exact nfa N` (the "
                       "[SEL-1] rung: a DFA STATE cap overflowed and the "
                       "retry rebuilt the prefilter from the collapsed "
                       "language -- N is the exact prefilter NFA's state "
                       "count), `size cap retry, exact N > cap` (the "
                       "[OPT-4] rung: an emitted-size cap refused the exact "
                       "artifact at N bytes), `nullable collapsed language` "
                       "([OPT-4.1], 263b013: -fprefilter-collapse asked for "
                       "the collapse and the POLICY declined it -- the "
                       "collapsed language is nullable -- so the prefilter "
                       "is kept and built from the EXACT language; exists "
                       "ONLY under that flag, because on a ladder rung the "
                       "same decline leaves no prefilter at all and stamps "
                       "`engine_sel declined-nullable` instead -- pcrec "
                       "tuning.md 2.17). The two `retry` prefixes are "
                       "the RESCUES; `-fno-prefilter-collapse` denies both "
                       "rungs (the state-cap one then drops the prefilter, "
                       "the size-cap one then REFUSES the pattern)",
    },
    # -- the ADAPTER's own two size facts and the warning ([B19], I-18
    # (iv)/(3)): not stamps, measured on the emitted files by pcrec's own
    # definition. Every compiled artifact carries the first two.
    "emit_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "adapter.emit_size() over the emitted .c and .h -- a port "
                  "of pcrec src/core/compile.c's `emit_size_measure` (total "
                  "minus comment bytes; tests/lib/size_count.sh's rule), "
                  "CONTROLLED byte-exactly against the `--warn-emit-bytes` "
                  "message's first number wherever that warning fires",
        "description": "the artifact's emitted C source in bytes, comments "
                       "EXCLUDED, .c + .h summed as pcrec sums them -- the "
                       "quantity `max_emit_bytes` caps and the size log / "
                       "[ART-SIZE] census measure; beside `artifact_bytes` "
                       "(the .so) so gcc time and object size can be read "
                       "against the source that produced them",
    },
    "emit_code_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "adapter.emit_size() -- `emit_bytes` minus every byte of "
                  "a `static const ... rx_*[N] = {` initializer (the table "
                  "rule of artifact_size_term.md 4.2); CONTROLLED against "
                  "the `--warn-emit-bytes` message's second number",
        "description": "the comment-excluded bytes OUTSIDE table "
                       "initializers -- the quantity `max_emit_code_bytes` "
                       "caps (the one that tracks gcc time; a table-"
                       "dominated DFA artifact has a large `emit_bytes` "
                       "and a small one of these)",
    },
    "warned_emit_bytes": {
        "type": "integer", "scope": "pattern",
        "source": "the `pcrec: warning: large artifact: B bytes ...` line on "
                  "the emit-c step's stderr (limits.md 8, `--warn-emit-"
                  "bytes`, default 250,000; exit code unchanged), parsed by "
                  "WARN_RE; the whole line is also appended to the row's "
                  "diagnostic",
        "description": "PRESENT ONLY when pcrec printed its advisory "
                       "large-artifact warning for this compile; the value "
                       "is the total the message names (== emit_bytes, "
                       "checked). ABSENT means no warning -- never a "
                       "failure either way",
    },
    # -- [B32] THE SCAN-EDGE COUNT: the covariate the full-suite regression
    # family needs. `dfa_scan_edge` is one token per artifact and cannot
    # separate a pattern with eight edges from one with a single edge;
    # pcrec's I-33 says the cost is one compare per edge per scan-loop
    # iteration, so the COUNT is the regressor. Split by machine because
    # the cost showed in the SEARCH band and a hybrid's edges are all on
    # that side.
    "scan_edges": {
        "type": "integer", "scope": "pattern",
        "source": "adapter.scan_edge_counts() -- pcrec's own `[OPT-5] SCAN "
                  "EDGE:` marker (src/gen/emit_dfa.c `emit_scan_edge`, one "
                  "block per edge per machine) counted in the emitted .c, "
                  "attributed to the function it lands in: `rx_search` (a "
                  "DFA artifact's search loop, both scan directions) and "
                  "`rx_prefilter` (a VM hybrid's inlined candidate-start "
                  "scan, called only from `rx_search_run`). A marker in any "
                  "other function is an AdapterError, never a dropped edge",
        "description": "how many [OPT-5] SCAN EDGES this artifact's "
                       "SEARCH-side machines carry. 0 is a real value and "
                       "is recorded on every artifact that emitted -- a "
                       "forced-VM one, a `-fno-scan-edge` build, and a scan "
                       "with no collapsible run all read 0 -- so the pair "
                       "is a REGRESSOR (the per-iteration compare count) "
                       "and not a filter. Beside `dfa_scan_edge`, which "
                       "says what SHAPE the edges took",
    },
    "scan_edges_match": {
        "type": "integer", "scope": "pattern",
        "source": "adapter.scan_edge_counts() -- the same marker counted in "
                  "`rx_match`, the ANCHORED machine",
        "description": "how many [OPT-5] SCAN EDGES the anchored machine "
                       "carries -- the `match` regime's half of the count, "
                       "kept apart from `scan_edges` because the measured "
                       "[OPT-EDGE] regression is in the SEARCH band and a "
                       "hybrid puts every edge it has on that side (its "
                       "`_match` entry is the VM's own body, so this reads "
                       "0 there). 0 is a real value, as above",
    },
    "dfa_table": {
        "type": "enum", "scope": "pattern",
        "values": ["premultiplied", "indexed", "mixed", "none"],
        "source": "<PREFIX>_DFA_TABLE ([OPT-3], pcrec abi 7+), read through "
                  "pb_dfa_table(). NO rx_info mirror exists, deliberately "
                  "(match_api.md 6.3 records the trigger that would make one "
                  "owed), so this macro is the only surface and its absence "
                  "means an artifact from a pcrec before abi 7",
        "description": "the ENCODING of that scan's transition table: "
                       "`premultiplied` (the step is table[state + class]), "
                       "`indexed` (the step multiplies -- the form pcrec "
                       "emitted before [OPT-3]), `mixed` (forward and "
                       "reverse machines took different forms), or `none` "
                       "(no numeric transition table at all: an `attempt` or "
                       "`empty` scan)",
    },
    # -- the two-tier default entry's fast capacities ([OPT-1], abi 5).
    # 6.3 family (b): VM artifacts ONLY, and NEVER ABSENT on one. The
    # un-suffixed entries run on this tier and escalate to the stamped
    # default on PCREC_ERR_FRAMES (match_api.md 10.9), so a subject above the
    # boundary pays two runs; the `_in` entries never had a tier.
    "fast_frames": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_FAST_FRAMES ([OPT-1], pcrec abi 5+), read "
                  "through pb_fast_frames()",
        "description": "the resume capacity, in FRAMES, that the un-suffixed "
                       "entries' fast tier runs on. Equal to `resume_frames` "
                       "IS the statement `this artifact has one tier` -- and "
                       "is the only spelling of it",
    },
    "fast_trail": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_FAST_TRAIL ([OPT-1], pcrec abi 5+), read through "
                  "pb_fast_trail()",
        "description": "the fast tier's trail capacity, in ENTRIES; the "
                       "companion of `fast_frames`",
    },
    # -- the caller-provided frame buffer's sizing surface (match_api.md
    # 10.4, abi 3). Stamped on EVERY artifact at abi 3, both engines; a DFA
    # artifact stamps 0 for all four ("this engine takes no buffers").
    "resume_frames": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_RESUME_FRAMES (== rx_info.resume_frames at abi 3), "
                  "read through pb_resume_frames()",
        "description": "the stamped DEFAULT resume-stack capacity, in FRAMES; "
                       "0 on a DFA artifact",
    },
    "trail_frames": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_TRAIL_FRAMES (== rx_info.trail_frames at abi 3), "
                  "read through pb_trail_frames()",
        "description": "the stamped DEFAULT trail capacity, in ENTRIES; 0 on "
                       "a DFA artifact",
    },
    "resume_frame_size": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_RESUME_FRAME_SIZE (== rx_info.resume_frame_size "
                  "at abi 3), read through pb_resume_frame_size()",
        "description": "bytes per resume frame FOR THIS ARTIFACT (per-artifact: "
                       "24 or 40 measured so far); 0 = the engine takes no "
                       "buffers",
    },
    "trail_frame_size": {
        "type": "integer", "scope": "pattern",
        "source": "<PREFIX>_TRAIL_FRAME_SIZE (== rx_info.trail_frame_size at "
                  "abi 3), read through pb_trail_frame_size()",
        "description": "bytes per trail entry FOR THIS ARTIFACT; 0 = the "
                       "engine takes no buffers",
    },
    # -- what the driver actually ran with. Present ONLY when a caller-
    # provided buffer was in use for this artifact.
    "buffer_frames": {
        "type": "integer", "scope": "pattern",
        "source": "the driver's --buffer-frames, from configs.toml "
                  "`buffer_frames`, echoed as `info buffer_frames` only when "
                  "the regions were allocated and the _in entries used",
        "description": "the caller-provided resume-frame CAPACITY (frames, "
                       "not bytes) this testee ran with; ABSENT means the "
                       "default stamped buffers were used",
    },
    "buffer_trail": {
        "type": "integer", "scope": "pattern",
        "source": "the driver's --buffer-trail, from configs.toml "
                  "`buffer_trail`, echoed as `info buffer_trail` only when "
                  "the regions were allocated and the _in entries used",
        "description": "the caller-provided trail CAPACITY (entries, not "
                       "bytes) this testee ran with; ABSENT means the default "
                       "stamped buffers were used",
    },
}

# The bit VALUES, from pcrec docs/spec/match_api.md 2 (the emitted
# PCREC_RX_ABI_H block). record_schema.md 7 rule 3: a `mask` value is an
# ARRAY OF BIT NAMES, never the integer -- the reporter must not need pcrec's
# bit table to filter on it.
MASK_BITS = {
    "vm_rungs": [("PCREC_VM_RUNG_CURSOR", 0x1),
                 ("PCREC_VM_RUNG_FRAMES_BOUNDED", 0x2),
                 ("PCREC_VM_RUNG_FRAMES_UNBOUNDED", 0x4),
                 ("PCREC_VM_RUNG_REVDET", 0x8),
                 ("PCREC_VM_RUNG_COUNTER", 0x10)],
    "vm_strats": [("PCREC_VM_STRAT_POSSESSIVE", 0x1),
                  ("PCREC_VM_STRAT_BACKTRACKING", 0x2)],
    "vm_prunes": [("PCREC_VM_PRUNE_CLAMPED", 0x1),
                  ("PCREC_VM_PRUNE_UNCLAMPED", 0x2)],
}
INT_PAIRS = ("abi", "ncaps", "ngroups", "nnames", "nentries", "step_budget",
             "work_budget", "frame_capacity", "subject_ceiling",
             "resume_frames", "trail_frames", "resume_frame_size",
             "trail_frame_size", "buffer_frames", "buffer_trail",
             "fast_frames", "fast_trail",
             "unroll_k", "max_emit_code_bytes", "max_emit_bytes",
             "emit_bytes", "emit_code_bytes", "warned_emit_bytes",
             "scan_edges", "scan_edges_match")

#: The `info` names carrying a STRING-valued pair, and the declared name each
#: lands under. Kept beside INT_PAIRS so a pair can never be printed by the
#: driver and silently dropped here (`engine_stamp` was, from abi 4 until
#: [B16]: the driver printed it and `_metadata` had no line for it, so the
#: unconditional engine stamp reached no record for five pins).
STR_PAIRS = ("engine", "prefilter", "dfa_scan", "dfa_prefilter", "dfa_table",
             "dfa_prefilter_offsets", "dfa_scan_edge", "dfa_match",
             "unroll_k_why", "artifact_name",
             "engine_sel", "vm_prefilter_lang", "vm_prefilter_lang_why")

#: THE SCOPE TABLE ([B18]): for every stamp pcrec emits UNCONDITIONALLY
#: (its D81 -- a selection fact is stamped whether or not it fired), the abi
#: it landed at and the artifact population it is on. `_check_agreement`
#: asserts, at the artifact's own abi, presence INSIDE the scope and -- for
#: the exclusive scopes -- absence OUTSIDE it. Scopes:
#:   every     every artifact, both engines
#:   dfa-scan  every artifact that CONTAINS a DFA scan: rx_info.scan non-NULL
#:             (every DFA artifact and every VM hybrid; match_api.md 6.3 (a))
#:   dfa       every artifact whose engine is `dfa` -- and NO other, hybrids
#:             included (RX_DFA_MATCH describes the _match ENTRY, 6.3)
#:   vm        every VM artifact -- and no DFA artifact (6.3 family (b);
#:             the size term's VM-only trio)
#:   vm-hybrid ([B19]) every VM artifact whose `prefilter` reads `hybrid` --
#:             and NO other artifact: not a forced-VM one (no prefilter at
#:             all), not a DFA one (6.3, [OPT-4]: "on every artifact with a
#:             VM PREFILTER DECISION that came out hybrid"). Exclusive.
#: The abi thresholds are the spec's (match_api.md 6.3, limits.md 8): the
#: `dfa-scan` rows start at 6 because before [DD-13c] hybrids did not stamp.
STAMP_SCOPE = {
    "engine":                ("every",    4),
    "dfa_scan":              ("dfa-scan", 6),
    "dfa_prefilter":         ("dfa-scan", 6),
    "dfa_table":             ("dfa-scan", 7),
    "dfa_prefilter_offsets": ("dfa-scan", 9),
    "dfa_scan_edge":         ("dfa-scan", 13),
    "dfa_match":             ("dfa",      10),
    "fast_frames":           ("vm",       5),
    "fast_trail":            ("vm",       5),
    "unroll_k":              ("vm",       11),
    "unroll_k_why":          ("vm",       11),
    "max_emit_code_bytes":   ("vm",       11),
    "max_emit_bytes":        ("every",    11),
    "engine_sel":            ("every",    12),
    "vm_prefilter_lang":     ("vm-hybrid", 12),
    "vm_prefilter_lang_why": ("vm-hybrid", 12),
}

#: The scopes an artifact OUTSIDE of must NOT carry the pair (the others,
#: `every` and `dfa-scan`, have no outside worth asserting on: `dfa-scan`'s
#: iff is checked directly against rx_info.scan in _check_agreement 3).
EXCLUSIVE_SCOPES = ("dfa", "vm", "vm-hybrid")

#: Frank's ask-(b) bucket: the `engine_sel` values that are NOT the ordinary
#: outcome -- spelled by him as `not in (selected, forced)`, and kept as an
#: explicit tuple so the set is greppable and a new pcrec value cannot join
#: it by accident. SIX values since pin 1989c62 (abi 14): the three 96e44c2
#: values, [OPT-4.1]'s `declined-nullable` (the collapse offered and refused
#: as useless -- a DIFFERENT outcome from `overflowed-dfa`, where no rescue
#: was available), [LIM-1]'s `size-cap-retry` (the size rung's SUCCESS,
#: which stamped the `selected` mislabel until 263b013 -- O-8/O-10's
#: finding, closed), and [OPT-4.2]'s `declined-nullable-default`.
#:
#: THE EIGHTH VALUE AND PCREC'S OWN FIVE: A DELIBERATE DIVERGENCE, [B26].
#: match_api.md 6.3 says of `declined-nullable-default` that it is
#: "deliberately NOT among the five" -- nothing overflowed on that path, so
#: in pcrec's vocabulary it did not FALL BACK. This bench's bucket is the
#: WIDER predicate Frank actually asked for, and the eighth value is in it:
#: an artifact whose own prefilter a policy declined did not get auto's
#: ordinary answer, and a reader comparing it against its `selected`
#: siblings needs to see that. So the bucket's RENDERING carries the
#: distinction rather than hiding it (report.py's legend names the two
#: readings), and the value is never silently folded into "a cap was hit".
#: The reporter derives its `DFA fallback tripped` bucket from this set, and
#: since 263b013 the bucket reads the VALUE and nothing else -- the
#: [B19]-era `vm_prefilter_lang_why` `size cap retry` prefix special-case is
#: RETIRED (inbox I-25: "your bucket reads the value now, not the _LANG_WHY
#: prefix").
ENGINE_SEL_FALLBACK = ("overflowed-dfa", "overflowed-prefilter",
                       "collapsed-prefilter", "declined-nullable",
                       "size-cap-retry", "declined-nullable-default")

#: The subset of ENGINE_SEL_FALLBACK that pcrec itself calls "fell back" --
#: its five, the ones where a CAP was hit (match_api.md 6.3). The complement
#: within the bucket is [OPT-4.2]'s rungless nullability decline. Kept
#: separate so the reporter can name which reading a cell is in, and so the
#: two sets are checked against each other rather than drifting.
ENGINE_SEL_OVERFLOW_FALLBACK = ("overflowed-dfa", "overflowed-prefilter",
                                "collapsed-prefilter", "declined-nullable",
                                "size-cap-retry")

#: `dfa_prefilter` values for which `dfa_prefilter_offsets` is NOT "none"
#: (match_api.md 6.3's iff, checked from both sides).
OFFSET_SET_VALUES = ("offset-set", "offset-set-bounded")

#: The committed copy of `pcrec --list-axes` at the pin -- the FOURTH
#: registry surface (pcrec docs/spec/registry.md 6; I-15 (5)). The stamp
#: value sets declared above are CHECKED against it (`registry_check`), and
#: `make check-harness` diffs this copy against the pin's live output, so a
#: candidate pcrec adds appears here as a failing check by name rather than
#: as an X15 rejection of the first record that carries it.
LIST_AXES_TSV = os.path.join(HERE, "list_axes.tsv")

#: Which declared pair each registry `stamp_macro` lands in. Only the
#: NAME-valued macros (a registry row with a non-empty `stamp_value`);
#: the count-valued ones (`RX_FAST_FRAMES`, `RX_ALTCLS_MERGES`, ...) and
#: the masks (`RX_VM_RUNGS`/`_STRATS`) are declared with their own types.
REGISTRY_STAMP_PAIRS = {
    "RX_ENGINE": "engine",
    "RX_VM_PREFILTER": "prefilter",
    "RX_DFA_PREFILTER": "dfa_prefilter",
    "RX_DFA_TABLE": "dfa_table",
    "RX_DFA_MATCH": "dfa_match",
    # [B19] (abi 12): both `predicate` axes, so the registry gets the
    # one-way check (every registry value declared); the reverse direction
    # is the by-value witnesses in tools/selfcheck.py.
    "RX_ENGINE_SEL": "engine_sel",
    "RX_VM_PREFILTER_LANG": "vm_prefilter_lang",
    # [B22] (pin 263b013): the `size-term` axis's rows now carry
    # stamp_values (pcrec [REG-SV] closed [B18]'s documented gap), so
    # RX_UNROLL_K_WHY joins the checked macros -- a `predicate` axis, the
    # one-way check.
    "RX_UNROLL_K_WHY": "unroll_k_why",
    # [B25] (abi 13, [OPT-5]): the `scan-body` axis enumerates all four
    # values -- `range`/`bitmap` as `list` candidates, `none`/`mixed` as
    # `predicate` outcome rows -- so both directions of the check cover
    # the whole declared set. (The companion `scan-edge` axis carries no
    # stamp_macro: it is the per-state selection `-fno-scan-edge` denies,
    # and the deny-control row reads its flag spelling from it.)
    "RX_DFA_SCAN_EDGE": "dfa_scan_edge",
}

#: The committed copy of `pcrec --list-definitions | grep -v '^#'` at the
#: pin -- the FIFTH registry surface ([DD-11], pcrec registry.md 9; I-18
#: (4)): one row per construct DEFINED in terms of another (`\d` = `[0-9]`,
#: the POSIX classes, `\R`, ...). Nothing this adapter reads depends on it;
#: it is archived beside `list_axes.tsv` under the same rule (re-archive at
#: every re-pin, the diff is what moved) and `make check-harness` diffs it
#: against the pin's live output. The bench's own `#` source header is
#: skipped by the same rule as list_axes.tsv's; pcrec's own `#` comment
#: lines are NOT in this file (the grep strips them), so the data rows are
#: the whole body.
LIST_DEFINITIONS_TSV = os.path.join(HERE, "list_definitions.tsv")

#: The committed copy of `pcrec --list-limits` at the pin -- the SIXTH
#: registry surface (pcrec D90 / [LIM-1], table_contract.md) and the THIRD
#: archive target ([B22], inbox I-25): one row per numeric limit in pcrec's
#: src/core/limits.def (44 at 263b013; 45 at a7e0bdf -- [OPT-5]'s
#: PCREC_MAX_SCAN_EDGES joined), in the table's own order. Nothing a
#: RECORD carries is read from it (every cap and capacity a record needs is
#: STAMPED per artifact); archived under the same rule as the other two
#: (re-archive at every re-pin, the diff is what moved) and diffed against
#: the pin's live output by `make check-harness`
#: (`check_list_limits_registry`).
#:
#: ONE thing does read it, and only to REFUSE ([B31]): the raise-only
#: check on a config's `max_emit_bytes` / `max_emit_code_bytes` needs the
#: pin's built-in defaults to say "below the default" in the bench's own
#: words, and the archive is the pin's own printout of exactly those two
#: numbers. Reading them here rather than typing them keeps this repo from
#: holding a second copy of a pcrec constant that could fall out of step --
#: the same rule the abi floor is written to (`_compile_one`'s comment).
LIST_LIMITS_TSV = os.path.join(HERE, "list_limits.tsv")

#: Declared values the registry's candidate lists do NOT enumerate because
#: they are OUTCOMES rather than candidates the selector walks. EMPTY since
#: pin 263b013: the `table` axis gained `none` / `mixed` OUTCOME rows (kind
#: `predicate` beside the two `list` candidates -- I-18 (iii), pcrec
#: [REG-SV]), so [B18]'s two entries here are now ordinary registry rows
#: and the reverse direction of `registry_check` covers them directly. The
#: mechanism stays for the next outcome value a stamp grows before its
#: registry row does.
REGISTRY_OUTCOME_VALUES = {}

#: The driver's refusal token for an artifact below shim.c's PB_SHIM_MIN_ABI.
#: The NUMBER lives in shim.c and nowhere else; this is only how the refusal
#: is recognised.
ABI_FLOOR_TOKEN = "abi-below-shim-floor"


#: The advisory large-artifact line pcrec writes to stderr past both caps
#: (limits.md 8, `--warn-emit-bytes=N`, default 250,000; 0 disables): the
#: two numbers are the SAME two quantities `emit_size()` computes, in the
#: same order, which is what makes the message a control on that port.
WARN_RE = re.compile(
    r"pcrec: warning: large artifact: (\d+) bytes of emitted C source "
    r"\((\d+) of code\), over --warn-emit-bytes=(\d+)\.")


def _emit_size_table_open(ln):
    """Does this line open a table initializer? pcrec's rule verbatim
    (src/core/compile.c `emit_size_table_open`): after leading blanks the
    line starts `static const `, has a `[` somewhere after that, and an
    `=` followed (blanks allowed) by `{` somewhere after the `[` -- not
    necessarily at the line's end, because the emitter writes a
    computed-goto jump table (`static const void *const rx_targets_7[11] =
    { &&rx_s1, ... };`) on ONE line. Anchored on `static const ` rather
    than on a type spelling, for the reason pcrec's own comment gives (a
    type pattern is what its first instrument could not cross)."""
    kw = b"static const "
    p = ln.lstrip(b" \t")
    if not p.startswith(kw):
        return False
    lb = p.find(b"[")
    if lb < 0:
        return False
    q = lb
    while True:
        q = p.find(b"=", q)
        if q < 0:
            return False
        r = q + 1
        while r < len(p) and p[r:r + 1] in (b" ", b"\t"):
            r += 1
        if r < len(p) and p[r:r + 1] == b"{":
            return True
        q += 1


def emit_size(paths):
    """-> (emit_bytes, emit_code_bytes) over the emitted files, by pcrec's
    OWN definition -- a port of src/core/compile.c's `emit_size_measure`
    ([ART-SIZE], artifact_size_term.md 4.2; tests/lib/size_count.sh's
    comment rule), summed over the files the way pcrec sums its .c and .h
    buffers before it compares them with the caps or prints the warning.

    The rules, verbatim from the C: every line counts its bytes INCLUDING
    its newline; a line whose first non-blank opens a block comment is
    PROSE in full, and a block opener that does not close on its own line
    runs to the line that closes it; a `//` line is prose; a line that
    opens a table initializer (`_emit_size_table_open`) is TABLE, and so
    is every line until the braces balance (the closing line included).
    total = the artifact minus its prose (the size log's quantity, what
    `max_emit_bytes` caps); code = that minus its tables (what
    `max_emit_code_bytes` caps). Bytes, never characters (K35: the
    emitter's comments carry multi-byte punctuation), which is why the
    files are read in binary.

    Why a port and not the size log's awk: the C is the definition the
    caps and the warning ENFORCE, the awk only the size log's half of it
    (no table split). The control that the port IS the C: wherever the
    `--warn-emit-bytes` line fires, `_compile_one` asserts its two numbers
    equal this function's, and tools/selfcheck.py forces the warning at
    `--warn-emit-bytes=1` on artifacts of each kind (a table-dominated DFA,
    a one-line jump table, a VM hybrid) for the same comparison."""
    total = prose = tables = 0
    for path in paths:
        with open(path, "rb") as f:
            src = f.read()
        in_comment = False
        in_table = 0
        i, n = 0, len(src)
        while i < n:
            j = src.find(b"\n", i)
            if j < 0:
                ln, lb, i = src[i:], n - i, n
            else:
                ln, lb, i = src[i:j], j - i + 1, j + 1
            total += lb
            t = ln.lstrip(b" \t")
            if in_comment:
                prose += lb
                if b"*/" in ln:
                    in_comment = False
            elif t.startswith(b"/*"):
                prose += lb
                # closed on its own line? the C scans from two past the
                # opener, so `/*/` does not count as closed.
                k = (len(ln) - len(t)) + 2
                if b"*/" not in ln[k:]:
                    in_comment = True
            elif t.startswith(b"//"):
                prose += lb
            elif in_table:
                tables += lb
                in_table += ln.count(b"{") - ln.count(b"}")
                if in_table < 0:
                    in_table = 0
            elif _emit_size_table_open(ln):
                tables += lb
                d = ln.count(b"{") - ln.count(b"}")
                in_table = d if d > 0 else 0
    tot = total - prose
    return tot, (tot - tables if tot > tables else 0)


#: [B32] THE SCAN-EDGE MARKER. pcrec's emitter writes one comment block
#: beside every scan edge it emits -- once per edge per MACHINE, which its
#: own comment bounds at twelve per artifact (src/gen/emit_dfa.c,
#: `emit_scan_edge`: "It is emitted once per edge per machine, i.e. up to
#: twelve times per artifact") -- and both spellings of that block, the
#: `span < 0` one and the other, open with this text.
#:
#: WHY THE MARKER AND NOT THE LOOP. The loop's shape is what
#: `RX_DFA_SCAN_EDGE` already names (`range` subtracts and compares,
#: `bitmap` reads a 256-byte table), so counting loop bodies would mean
#: keeping a second copy of the body taxonomy here and re-deriving it at
#: every pin. The marker is ONE line the emitter writes unconditionally
#: beside each edge, whatever body it chose.
SCAN_EDGE_MARKER = b"[OPT-5] SCAN EDGE:"

#: The artifact's symbol prefix. `_compile_one` passes `-p rx` on every
#: exec, and the scan-edge attribution below reads function names, so the
#: two must not drift: this constant is the one place it is spelled.
ARTIFACT_PREFIX = "rx"

#: A top-level C function DEFINITION in an emitted artifact: a line whose
#: first byte is neither blank nor a newline, and whose first
#: identifier-followed-by-`(` is the function's name. A line ending in `;`
#: is a DECLARATION and names nothing; a column-0 line that matches neither
#: (`}`, `#define`, a table opener, a comment) ENDS the current function,
#: which is what makes a marker outside every function detectable.
_C_DEF_RE = re.compile(rb"^[A-Za-z_][^;]*?\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")

#: WHICH MACHINE a scan edge belongs to, read from the emitted function it
#: lands in. MEASURED at pin 1989c62 (2026-09-02) over bench/loglines and
#: bench/email, both forms, three engine modes, plus eleven hand-cut shapes
#: (a pure DFA, an anchored `attempt` DFA, four VM hybrids, a forced VM, a
#: denied build): every marker in that corpus lands in exactly one of these
#: three functions and no marker ever lands anywhere else.
#:
#:   `<prefix>_search`     the DFA artifact's own search loop -- BOTH scan
#:                         directions are emitted into it (`iso-ts` puts 4
#:                         forward and 4 reverse edges there)
#:   `<prefix>_prefilter`  a VM HYBRID's inlined candidate-start scan. It is
#:                         called from `<prefix>_search_run` and from
#:                         NOWHERE else (measured: the hybrid's `_match`
#:                         path is the VM's own body), so a hybrid's edges
#:                         are a cost of the SEARCH band, not the match one
#:   `<prefix>_match`      the anchored machine, which `<prefix>_match`
#:                         entries walk
#:
#: Anything else is an AdapterError rather than a silently dropped edge:
#: pcrec moving the loop into a fourth function is exactly the event this
#: covariate would otherwise mis-attribute, and a mis-attributed covariate
#: is worse than none (the [B16] `engine_stamp` lesson -- a pair the driver
#: printed and this file had no line for reached no record for five pins).
SCAN_EDGE_SEARCH_FNS = ("search", "prefilter")
SCAN_EDGE_MATCH_FNS = ("match",)


def scan_edge_counts(paths, prefix=ARTIFACT_PREFIX):
    """-> (scan_edges, scan_edges_match) over the emitted files ([B32]).

    The number of [OPT-5] SCAN EDGES in this artifact's SEARCH-side
    machines, and in its anchored one. This is a COVARIATE, not a stamp:
    `RX_DFA_SCAN_EDGE` says what SHAPE the edges took and whether there are
    any at all, and the full suite at 1989c62 found the regression family
    it names (every loglines pattern stamping a non-`none` edge is slower,
    every one stamping `none` is flat) -- but the stamp is one token per
    artifact, so it cannot separate `iso-ts` from `ipv6`. pcrec's I-33 gives
    the mechanism: one compare per edge PER SCAN-LOOP ITERATION, so it is
    the COUNT that predicts the cost. This function is that count.

    0 is a real value and is recorded as one, on every artifact that
    emitted: a forced-VM artifact (no DFA scan at all), a `-fno-scan-edge`
    build, and an artifact whose scans had no collapsible run all carry 0
    -- which is what makes the covariate usable as a regressor rather than
    a filter."""
    search = match = 0
    for path in paths:
        fn = None
        with open(path, "rb") as f:
            for ln in f:
                head = ln[:1]
                if head == b"}":
                    # a column-0 close brace ENDS the function; the opening
                    # `{` is on its own line too and must NOT (it is the
                    # line right after the signature this reader just read)
                    fn = None
                elif head.isalpha() or head == b"_":
                    if ln.rstrip().endswith(b";"):
                        fn = None                 # a declaration names none
                    else:
                        m = _C_DEF_RE.match(ln)
                        fn = (m.group(1).decode("ascii", "replace")
                              if m else None)
                if SCAN_EDGE_MARKER not in ln:
                    continue
                base = None
                if fn and fn.startswith(prefix + "_"):
                    base = fn[len(prefix) + 1:]
                if base in SCAN_EDGE_SEARCH_FNS:
                    search += 1
                elif base in SCAN_EDGE_MATCH_FNS:
                    match += 1
                else:
                    raise _ad.AdapterError(
                        "%s carries a %s marker inside %s, which is neither "
                        "a SEARCH-side machine (%s) nor the anchored one "
                        "(%s). pcrec has moved the [OPT-5] scan-edge loop; "
                        "the `scan_edges` covariate would mis-attribute it, "
                        "so it is refused here rather than recorded wrong "
                        "(testees/pcrec/adapter.py SCAN_EDGE_SEARCH_FNS)."
                        % (path, SCAN_EDGE_MARKER.decode(),
                           ("`%s`" % fn) if fn else "no function this "
                           "reader could name",
                           "/".join("%s_%s" % (prefix, s)
                                    for s in SCAN_EDGE_SEARCH_FNS),
                           "/".join("%s_%s" % (prefix, s)
                                    for s in SCAN_EDGE_MATCH_FNS)))
    return search, match


def parse_warn_line(stderr_text):
    """-> (warned_total, warned_code, threshold, line) for pcrec's advisory
    large-artifact warning on `stderr_text`, or None when it did not
    fire. The warning is NOT a failure (limits.md 8: exit code unchanged,
    nothing emitted differently); it is a fact about the artifact and is
    recorded as one."""
    for line in (stderr_text or "").splitlines():
        m = WARN_RE.search(line)
        if m:
            return int(m.group(1)), int(m.group(2)), int(m.group(3)), line.strip()
    return None


# ------------------------------------------------ the compilee toolchain axis
#
# [B24] (pcrec [CC-CLANG], their docs/testing.md "CLANGGEN"). pcrec emits C
# and stops; whoever runs a C compiler on that C is the COMPILEE toolchain,
# and here that is this file's phase 2. So the axis is a property of the
# TESTEE and lives in configs.toml as `cc`, whose long comment carries the
# ruling. Two functions, because the resolution and the naming are asked for
# separately (describe() wants both, _compile_one only the first).
CC_VALUES = ("gcc", "clang")


def effective_cc(testee_id, cfg):
    """-> (compiler, config_extra_or_None) for one testee.

    ABSENT `cc` -> ($CC or gcc, None): today's behaviour byte for byte, and
    `None` is what keeps an existing config's `build_flags` and derived
    `testee_id` unchanged. PRESENT `cc` -> (it, "cc-<it>"): an IDENTITY
    claim, so a conflicting `$CC` is REFUSED rather than silently winning
    (which would put a compiler in the testee_id that never ran). `$CC` may
    be a path; only its basename is compared."""
    declared = cfg.get("cc")
    env = os.environ.get("CC") or ""
    if declared is None:
        return (env or "gcc"), None
    if declared not in CC_VALUES:
        raise _ad.AdapterError(
            "%s: cc = %r is not a compilee toolchain this adapter knows "
            "(%s; testees/pcrec/configs.toml). The value is part of the "
            "derived testee_id, so it is a closed set on purpose."
            % (testee_id, declared, ", ".join(CC_VALUES)))
    if env and os.path.basename(env) != declared:
        raise _ad.AdapterError(
            "%s declares cc = %r in testees/pcrec/configs.toml but $CC=%r "
            "is set. That key is an IDENTITY -- it names the compiler in "
            "the derived testee_id -- so it is not something $CC may "
            "override behind the record's back. Unset $CC (or set it to "
            "%s) and run again; $CC still decides the compiler for every "
            "config that declares none, and it always builds the timing "
            "driver." % (testee_id, declared, env, declared))
    return declared, "cc-" + declared


def cc_version_line(cc):
    """The compiler's `--version` FIRST LINE, verbatim -- the same string
    `environment.compiler_raw` carries for the box's toolchain
    (record_schema.md 6.7), computed by the same function, so the artifact's
    compiler and the driver's are comparable side by side."""
    from pcrecbench import env as _env
    return _env.compiler_raw(cc)


# --------------------------------------------------- the emitted-size caps
#
# [B31] (pcrec [ART-SIZE] / limits.md 8, inbox I-32 (vii)). pcrec refuses
# rather than emit past either of two caps -- 1,000,000 comment-excluded
# bytes TOTAL, 500,000 of them outside table initializers (CODE) -- and both
# are RAISE-ONLY per compile: `--max-emit-bytes=N` / `--max-emit-code-bytes=N`
# accept a larger artifact and can never manufacture a refusal that would not
# have happened anyway.
#
# On bench/altwide@0.1 those caps refuse 50 of 80 (pattern x form x mode)
# compiles at this pin, so the wide rungs are unmeasurable without the
# raise. The raise is therefore an AXIS of the testee, exactly like `cc`:
# a raised-cap record is not the same record with a gate removed, because
# raising `--max-emit-bytes` also moves the [ART-SIZE] size-term ladder's
# own abort bound (pcrec src/core/compile.c: `3 * cap`, saturating) and can
# change the K it selects. Two artifacts built under different caps are two
# artifacts, and the testee_id says which.
#
#   max_emit_bytes = N          OPTIONAL, per config, BYTES
#   max_emit_code_bytes = N     OPTIONAL, per config, BYTES
#
# ABSENT means today's behaviour byte for byte: no flag on the argv, no
# clause in `build_flags`, no `config_extra`, the same derived `testee_id`.
# PRESENT is an IDENTITY CLAIM, and the flag rides in `flags` so ONE list
# feeds the argv, `build_flags` and `runtime_options` alike.
#
#: (config key, pcrec flag, the archived limit that is its FLOOR, slug word).
#: The order is the order of the slug parts and of the build_flags clause.
CAP_KEYS = (
    ("max_emit_bytes", "--max-emit-bytes", "PCREC_MAX_EMIT_BYTES", "emitcap"),
    ("max_emit_code_bytes", "--max-emit-code-bytes",
     "PCREC_MAX_VM_EMIT_CODE_BYTES", "codecap"),
)


def limits_rows(path=LIST_LIMITS_TSV):
    """The committed `--list-limits` TSV as a list of dicts (`#name\\t...`
    is the header; every other `#` line -- pcrec's own comment block and
    the bench's source header above it -- is skipped)."""
    rows, cols = [], None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("#name\t"):
                cols = line[1:].split("\t")
                continue
            if not line or line.startswith("#"):
                continue
            if cols is None:
                raise _ad.AdapterError(
                    "%s: a data row before the `#name` header" % path)
            vals = line.split("\t")
            if len(vals) != len(cols):
                raise _ad.AdapterError(
                    "%s: row has %d columns, header %d: %r"
                    % (path, len(vals), len(cols), line))
            rows.append(dict(zip(cols, vals)))
    return rows


def archived_limit(name, path=LIST_LIMITS_TSV):
    """The pin's own value for one numeric limit, read from the archive.

    The archive is diffed against the pin's live `--list-limits` on every
    `make check-harness` (`check_list_limits_registry`), so a stale number
    here is a named failure there rather than a wrong refusal message."""
    for r in limits_rows(path):
        if r.get("name") == name:
            try:
                return int(r["value"])
            except (KeyError, ValueError):
                break
    raise _ad.AdapterError(
        "%s has no numeric row for %s -- the emitted-size cap axis reads "
        "pcrec's own defaults from the archived --list-limits table rather "
        "than keeping a second copy of them, so a renamed or reshaped limit "
        "must be seen here, not silently defaulted"
        % (os.path.basename(path), name))


def effective_caps(testee_id, cfg, flags):
    """-> (extra_flags, config_extra_or_None) for one testee's size caps.

    `flags` is the config's EFFECTIVE flag list -- which for `pcrec-local`
    already carries whatever `$PCREC_LOCAL_FLAGS` put there, so a locally
    raised cap is derived from the flags exactly as `engine_mode` and
    `captures` are and there is ONE code path.

    A declared key and a flag already in `flags` may AGREE (the flag is not
    added twice) but never DISAGREE: the value is part of the derived
    testee_id, and an id that names a cap the compile did not run under is
    worse than no record. A value BELOW pcrec's archived built-in default
    is refused HERE, by name, before anything is measured -- pcrec would
    refuse it too, but a caller who mistyped a bench config should be told
    so by the bench, in the bench's words, at the moment the config is
    read."""
    extra, parts = [], []
    for key, flag, limit_name, word in CAP_KEYS:
        declared = cfg.get(key)
        in_flags = None
        for f in flags:
            if f.startswith(flag + "="):
                try:
                    in_flags = int(f.split("=", 1)[1])
                except ValueError:
                    raise _ad.AdapterError(
                        "%s: %r is not an integer byte count -- pcrec's %s "
                        "takes bytes" % (testee_id, f, flag))
        if declared is not None and not isinstance(declared, int):
            raise _ad.AdapterError(
                "%s: %s = %r must be an integer -- BYTES of emitted C "
                "source (testees/pcrec/configs.toml)"
                % (testee_id, key, declared))
        if declared is not None and in_flags is not None and declared != in_flags:
            raise _ad.AdapterError(
                "%s declares %s = %d in testees/pcrec/configs.toml but its "
                "effective flags already carry %s=%d. That value is an "
                "IDENTITY -- it names the cap in the derived testee_id -- so "
                "the two may agree but never disagree; drop one of them."
                % (testee_id, key, declared, flag, in_flags))
        value = declared if declared is not None else in_flags
        if value is None:
            continue
        floor = archived_limit(limit_name)
        if value < floor:
            raise _ad.AdapterError(
                "%s: %s = %d is BELOW pcrec's built-in %s of %d. Both "
                "emitted-size caps are RAISE-ONLY (pcrec docs/spec/"
                "limits.md 8: an override exists to accept a larger "
                "artifact, never to make a build refuse one it would have "
                "accepted), and this bench will not write a record whose "
                "testee_id claims a cap pcrec cannot have been under. The "
                "default is the pin's own, read from the archived "
                "--list-limits table (testees/pcrec/list_limits.tsv)."
                % (testee_id, key, value, limit_name, floor))
        if value <= 0:
            raise _ad.AdapterError(
                "%s: %s must be a positive byte count, got %d"
                % (testee_id, key, value))
        if in_flags is None:
            extra.append("%s=%d" % (flag, value))
        parts.append("%s-%d" % (word, value))
    return extra, ("-".join(parts) if parts else None)


# ---------------------------------------------------------------------------
# THE SCAN-EDGE DENY AXIS -- `-fno-scan-edge` ([B32]; pcrec [OPT-5] /
# [OPT-EDGE], docs/spec/tuning.md 2.18, --list-axes bit 21).
#
# The full suite at pin 1989c62 found ONE regression family with an exact
# stamp: every bench/loglines pattern whose artifact stamps a non-`none`
# `RX_DFA_SCAN_EDGE` is slower than its pre-[OPT-5] self (`iso-ts` x1.06 /
# x1.09, `http-5xx`, `ipv6` x1.03-1.09) and every one that stamps `none` is
# flat. pcrec's I-33 gives the mechanism -- one compare per edge per
# scan-loop iteration -- and chartered [OPT-EDGE] on their side. A testee
# that DENIES the axis is that work's BEFORE, measured here rather than
# reconstructed from an older pin: `-fno-scan-edge` restores the
# pre-[OPT-5] machine (the run's interior states go back into the table)
# at the SAME commit, so the pair differs in the transform and in nothing
# else -- no abi, no shim, no other pin's fixes riding along.
#
# THERE IS NO NEW CONFIG KEY. The flag is spelled in the config's own
# `flags` list, which is already the ONE list that feeds pcrec's argv,
# `build_flags` and `runtime_options`; the axis is DERIVED from those
# effective flags, exactly as `engine_mode` and `captures` are for
# `pcrec-local`. So a `$PCREC_LOCAL_FLAGS="-fno-scan-edge"` reaches the
# derived testee_id down the same code path, with no second spelling of
# the flag anywhere in this repo.
#
#: (pcrec flag, slug word, what the build_flags clause says it MEANS).
DENY_FLAGS = (
    ("-fno-scan-edge", "noedge",
     "the [OPT-5] SCAN EDGE denied (--list-axes `scan-edge`, bit 21): the "
     "pass leaves every state where it was and the counted run's interior "
     "stays in the transition table, so this artifact is the pre-[OPT-5] "
     "machine built by the SAME compiler -- [OPT-EDGE]'s BEFORE, and the "
     "one denial on this axis that changes the MACHINE and not only "
     "emitted text"),
)


def effective_denies(flags):
    """-> (config_extra_or_None, [(flag, word)]) for the generation axes a
    config's EFFECTIVE flag list DENIES ([B32]).

    Read off `flags` rather than from a config key of its own: the flag is
    a bare pcrec option with no value, so spelling it in `flags` already
    puts it on the argv, in `build_flags` and in `runtime_options`, and a
    key beside it would be a second truth to keep in step. A denial is an
    IDENTITY claim all the same -- a denied artifact is a DIFFERENT machine
    from its sibling, not the same machine measured twice -- so the word
    joins `config_extra` and the derived testee_id says which."""
    parts = [(f, word) for f, word, _why in DENY_FLAGS if f in flags]
    return ("-".join(w for _f, w in parts) if parts else None), parts


def cap_values(cfg):
    """-> [(flag, limit_name, value)] for the caps an EFFECTIVE config
    raises, in CAP_KEYS order; empty where it raises neither. Read back off
    the effective `flags`, which is where `config()` put them, so a
    declared key and a `$PCREC_LOCAL_FLAGS` raise read the same."""
    out = []
    for _key, flag, limit_name, _word in CAP_KEYS:
        for f in cfg.get("flags", []):
            if f.startswith(flag + "="):
                out.append((flag, limit_name, int(f.split("=", 1)[1])))
                break
    return out


def compose_config_extra(*parts):
    """`testee.config_extra` from the axis tokens a config carries, in a
    FIXED order: the axes in the order they were chartered ([B24] `cc`,
    then [B31] the emitted-size caps, then [B32] the denied generation
    axes), joined by `-`.

    Chartering order is the rule because it makes the slug APPEND-ONLY: a
    testee that already had a token keeps it where it was when a later axis
    joins, so an id in the store never has a part inserted ahead of the one
    a reader knows it by. The separator is `-` because `_` is what
    record_schema.md 6.4 splits the whole id on and the slug charset
    (`$defs/slug`) is `[a-z0-9-]`; the schema never learns the PARTS -- X5
    derives the id from `config_extra` whole, so composition is entirely
    this adapter's business."""
    return "-".join(p for p in parts if p) or None


def buffer_capacities(cfg):
    """-> (frames, trail) from a config's `buffer_frames` / `buffer_trail`,
    or None when the config has neither. Both or neither: a non-NULL
    descriptor requires BOTH regions (match_api.md 10.2), and the trail is
    the array that binds first, so a frames-only knob would be inert."""
    f, t = cfg.get("buffer_frames"), cfg.get("buffer_trail")
    if f is None and t is None:
        return None
    if f is None or t is None:
        raise _ad.AdapterError(
            "buffer_frames and buffer_trail go together (match_api.md 10.2: "
            "both regions are required); got frames=%r trail=%r" % (f, t))
    if not (isinstance(f, int) and isinstance(t, int)) or f < 1 or t < 1:
        raise _ad.AdapterError(
            "buffer_frames / buffer_trail must be positive integers -- "
            "CAPACITIES in frames and entries, never bytes; got %r / %r"
            % (f, t))
    return f, t


def runtime_options(flags):
    """`testee.runtime_options` (record_schema.md 4.3): the engine's OWN
    option names, as {name, value} pairs.

    KB-1 (docs/dev/known_issues.md), FIXED: a BARE flag (no `=`) is paired
    with the FOLLOWING token when that token is itself not a flag --
    `["--features", "all"]` -> {"name": "--features", "value": "all"}. The
    previous rule split on `=` only, so a bare flag's value -- the very
    next argv token -- was never looked at and the pair recorded
    `{"value": true}` instead, losing `all` to `runtime_options` (it
    stayed readable in `build_flags` as text, which is why this was not
    urgent). `--engine=vm` is unchanged: an `=` flag's value is what
    follows the `=`, consumed alone. A trailing bare flag, or one
    immediately followed by another flag, has no following value and is
    `true`, same as before.

    [B32]: a flag is a token starting with `-`, not with `--`. pcrec's
    generation-axis denials are single-dash (`-fno-scan-edge`), and under
    the old test they were skipped as if they were somebody's VALUE -- so
    a denied testee's `runtime_options` would not have said what it
    denied. Nothing measured before [B32] moves: no config that predates
    it carries a single-dash flag, which `check_noedge_axis` arm 1 proves
    against the frozen renderer and against every committed record."""
    out = []
    i, n = 0, len(flags)
    while i < n:
        f = flags[i]
        if not f.startswith("-"):
            i += 1
            continue
        if "=" in f:
            name, _, value = f.partition("=")
            out.append({"name": name, "value": value})
            i += 1
            continue
        if i + 1 < n and not flags[i + 1].startswith("-"):
            out.append({"name": f, "value": flags[i + 1]})
            i += 2
            continue
        out.append({"name": f, "value": True})
        i += 1
    return out


def buffer_args(cfg):
    """The driver's `--buffer-frames N --buffer-trail M`, or []."""
    caps = buffer_capacities(cfg)
    if caps is None:
        return []
    return ["--buffer-frames", str(caps[0]), "--buffer-trail", str(caps[1])]


def _mask_names(name, value):
    out = [bit for bit, mask in MASK_BITS[name] if value & mask]
    unknown = value & ~sum(m for _b, m in MASK_BITS[name])
    if unknown:
        raise _ad.AdapterError(
            "%s carries bit(s) 0x%x this adapter has no name for. pcrec grew "
            "a stamp bit; add it to MASK_BITS and to METADATA_DECL together, "
            "or the record would claim a mask it cannot spell." % (name, unknown))
    return out


def registry_rows(path=LIST_AXES_TSV):
    """The committed `--list-axes` TSV as a list of dicts (the `#axis ...`
    line is the header; every other `#` line is pcrec's own comment and
    is kept verbatim in the file but skipped here). The bench's own source
    header at the top of the file is `#`-prefixed too and is skipped the
    same way."""
    rows, cols = [], None
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("#axis\t"):
                cols = line[1:].split("\t")
                continue
            if not line or line.startswith("#"):
                continue
            if cols is None:
                raise _ad.AdapterError(
                    "%s: a data row before the `#axis` header" % path)
            vals = line.split("\t")
            if len(vals) != len(cols):
                raise _ad.AdapterError(
                    "%s: row has %d columns, header %d: %r"
                    % (path, len(vals), len(cols), line))
            rows.append(dict(zip(cols, vals)))
    return rows


def registry_check(rows=None):
    """The declared stamp VALUE SETS against the registry ([B18], I-15 (5)):
    every `stamp_value` the registry lists for a macro in
    REGISTRY_STAMP_PAIRS must be a declared value of that pair, and every
    declared value of a pair whose axis is `kind = list` (the emitter's
    own candidate arrays, read live by the dump) must appear in the
    registry or in REGISTRY_OUTCOME_VALUES -- a value this adapter declares
    that pcrec no longer has is as much a drift as one it lacks.
    `predicate` axes are hand-stated prose on pcrec's side and get the
    one-way check only. Returns a list of problem strings; empty means the
    map agrees with the registry."""
    rows = registry_rows() if rows is None else rows
    problems = []
    seen = {}
    kinds = {}
    for r in rows:
        macro, val = r.get("stamp_macro", ""), r.get("stamp_value", "")
        if macro in REGISTRY_STAMP_PAIRS and val:
            seen.setdefault(macro, set()).add(val)
            kinds.setdefault(macro, set()).add(r.get("kind", ""))
    for macro, pair in REGISTRY_STAMP_PAIRS.items():
        declared = set(METADATA_DECL[pair].get("values") or [])
        reg = seen.get(macro, set())
        if not reg:
            problems.append("%s: the registry lists no stamp_value for it "
                            "(pair %s)" % (macro, pair))
            continue
        for v in sorted(reg - declared):
            problems.append("%s stamps %r in the registry; pair %s does not "
                            "declare it -- add it to METADATA_DECL"
                            % (macro, v, pair))
        # [B22]: an axis may mix `list` candidate rows with `predicate`
        # OUTCOME rows (the `table` axis since 263b013); the reverse check
        # applies wherever a candidate list exists at all.
        if "list" in kinds.get(macro, set()):
            extra = declared - reg - REGISTRY_OUTCOME_VALUES.get(pair, set())
            for v in sorted(extra):
                problems.append("pair %s declares %r; the registry's `list` "
                                "axis for %s does not have it and it is not "
                                "a documented outcome value "
                                "(REGISTRY_OUTCOME_VALUES)" % (pair, v, macro))
    return problems


def _find_repo_beside(start):
    """The repository a binary sits in, or None: walk UP from `start` to a
    directory holding `.git` (a FILE in a worktree, a directory in a main
    tree). Two stops, both deliberate: a directory holding `PIN.tsv` is a
    `git archive` snapshot pin.sh made, which has no repository by design
    (the walk must not climb out of it into whatever tree holds build/);
    and this bench's own checkout is never "the repository beside a pcrec
    binary", however the binary got under it."""
    bench_tops = set()
    for d in (BENCH_ROOT,):
        try:
            proc = subprocess.run(["git", "-C", d, "rev-parse", "--show-toplevel",
                                   "--git-common-dir"], capture_output=True,
                                  text=True, env=C_ENV, timeout=30)
            for line in (proc.stdout or "").splitlines():
                line = line.strip()
                if line:
                    if not os.path.isabs(line):
                        line = os.path.join(d, line)
                    bench_tops.add(os.path.realpath(
                        line[:-5] if line.endswith("/.git") else line))
        except (OSError, subprocess.SubprocessError):
            pass
        bench_tops.add(os.path.realpath(d))
    d = os.path.realpath(start)
    while True:
        if os.path.exists(os.path.join(d, "PIN.tsv")):
            return None
        if os.path.realpath(d) in bench_tops:
            return None
        if os.path.exists(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def _git_at(repo, *args):
    """A READ-ONLY git query against the repository beside a local binary
    (BD2: pcrec's tree is never written from here; `describe` and
    `rev-parse` read)."""
    try:
        proc = subprocess.run(["git", "-C", repo] + list(args),
                              capture_output=True, text=True, env=C_ENV,
                              timeout=60)
    except (OSError, subprocess.SubprocessError):
        return ""
    return proc.stdout.strip() if proc.returncode == 0 else ""


def local_provenance(binary):
    """-> (engine_version, engine_commit, describe_raw, repo) for a provided
    binary (record_schema.md 6.2, the `local:` shape)."""
    sha = _ad.sha256_file(binary)
    version = "local:" + sha[:12]
    repo = _find_repo_beside(os.path.dirname(os.path.realpath(binary)))
    commit = None
    desc = ""
    if repo:
        desc = _git_at(repo, "describe", "--always", "--dirty", "--tags")
        if desc:
            dirty = desc.endswith("-dirty")
            slug = re.sub(r"[^a-z0-9._+-]", "-", desc.lower()).strip("-")
            version = (version + "+" + slug)[:64].rstrip("+-.")
            if not dirty:
                head = _git_at(repo, "rev-parse", "HEAD")
                commit = head if re.fullmatch(r"[0-9a-f]{40}", head) else None
    return version, commit, desc, repo


class Adapter(_ad.Adapter):
    name = "pcrec"

    # ------------------------------------------------------- local vs pinned

    def is_local(self, testee_id):
        return bool(_ad.Adapter.config(self, testee_id).get("local"))

    def config(self, testee_id):
        """The EFFECTIVE config. For a local testee the flags are the base
        list plus `$<extra_flags>` split on whitespace, and `engine_mode` /
        `captures` are DERIVED from them, so every consumer of `flags`,
        `engine_mode` and `captures` -- describe(), the compile phases, the
        buffer plumbing -- sees one truth and the derived testee_id says
        what actually ran.

        [B24]: `cc` is RESOLVED here too, for every config -- the compiler
        that will build the artifact, and the `config_extra` slug that puts
        it in the testee_id (None where the config declares no `cc`, which
        is every config that existed before the axis and is why their ids
        and build_flags are unchanged).

        [B31]: so are the two EMITTED-SIZE CAPS, and by the SAME rule the
        local flags already follow -- `effective_caps` is handed the
        effective flag list, so a config's declared `max_emit_bytes` and a
        `$PCREC_LOCAL_FLAGS` that carries `--max-emit-bytes=` reach the
        derived id down one path. The raise flags are APPENDED TO `flags`
        rather than kept beside them, because `flags` is the single list
        `_compile_one`'s argv, `build_flags` and `runtime_options` are all
        built from: adding them anywhere else would need three edits and
        would eventually drift into two."""
        cfg = dict(_ad.Adapter.config(self, testee_id))
        flags = list(cfg.get("flags", []))
        if cfg.get("local"):
            extra_var = cfg.get("extra_flags")
            if extra_var:
                flags += os.environ.get(extra_var, "").split()
            mode = cfg.get("engine_mode", "auto")
            for f in flags:
                if f.startswith("--engine="):
                    mode = f.split("=", 1)[1].strip().lower()
            if mode not in ENGINE_MODES:
                raise _ad.AdapterError(
                    "%s: --engine=%s is not a pcrec engine mode this adapter "
                    "knows (%s; record_schema.md 6.3)"
                    % (testee_id, mode, ", ".join(ENGINE_MODES)))
            cfg["engine_mode"] = mode
            cfg["captures"] = "off" if "--no-captures" in flags else "on"
        cap_flags, cfg["cap_extra"] = effective_caps(testee_id, cfg, flags)
        cfg["flags"] = flags + cap_flags
        cfg["cc"], cfg["cc_extra"] = effective_cc(testee_id, cfg)
        # [B32]: the DENIED generation axes, derived from the effective
        # flags (which by here carry the local extras and the cap raises),
        # so `-fno-scan-edge` reaches the testee_id whether a config
        # spelled it or `$PCREC_LOCAL_FLAGS` did.
        cfg["deny_extra"], cfg["deny_flags"] = effective_denies(cfg["flags"])
        return cfg

    def local_binary(self, testee_id):
        """`$PCREC_BIN` (the variable is named by the config), checked."""
        cfg = _ad.Adapter.config(self, testee_id)
        var = cfg.get("binary") or "PCREC_BIN"
        path = os.environ.get(var, "")
        if not path:
            raise _ad.AdapterError(
                "%s needs $%s: the path of the pcrec binary to bench "
                "(e.g. %s=/home/you/pcrec/worktrees/x/build/pcrec). It is "
                "not set." % (testee_id, var, var))
        if not os.path.isfile(path) or not os.access(path, os.X_OK):
            raise _ad.AdapterError(
                "%s: $%s=%r is not an executable file" % (testee_id, var, path))
        return os.path.abspath(path)

    def binary_for(self, testee_id):
        """THE ONE PLACE the pcrec binary is chosen: the provided one for a
        local testee, the pin's for every other. Everything downstream
        (emit-c, gcc, load, the driver) is one code path."""
        if self.is_local(testee_id):
            return self.local_binary(testee_id)
        return self.pin_binary()

    def tier(self, testee_id):
        return "scratch" if self.is_local(testee_id) else "pinned"

    # ------------------------------------------------------------- the pin

    def pin(self):
        p = self.cfg.get("pin")
        if not p:
            raise _ad.AdapterError("testees/pcrec/configs.toml declares no pin")
        return p

    def pin_binary(self, build=True):
        """-> the path of the pinned `pcrec`. Delegates to pin.sh, which
        reuses an existing build and never writes inside pcrec's tree."""
        argv = [PIN_SH] + ([] if build else ["--path"]) + [self.pin()]
        proc = subprocess.run(argv, capture_output=True, text=True,
                              env=C_ENV, timeout=1200)
        if proc.returncode != 0:
            raise _ad.AdapterError("pin.sh %s failed:\n%s"
                                   % (self.pin(), proc.stderr))
        return proc.stdout.strip()

    def pin_provenance(self):
        """(full_commit, describe). From the pin tree's PIN.tsv when pin.sh
        wrote one; otherwise from a READ-ONLY git query against pcrec -- the
        commit is a fact about pcrec's history, not something to type."""
        tree = os.path.dirname(os.path.dirname(self.pin_binary(build=False)))
        tsv = os.path.join(tree, "PIN.tsv")
        if os.path.exists(tsv):
            d = {}
            with open(tsv, "r", encoding="utf-8") as f:
                for line in f:
                    k, _, v = line.rstrip("\n").partition("\t")
                    d[k] = v
            if d.get("commit"):
                return d["commit"], d.get("describe") or self.pin()
        full = self._git("rev-parse", "%s^{commit}" % self.pin())
        desc = self._git("describe", "--always", full) or self.pin()
        return full, desc

    def _git(self, *args):
        try:
            proc = subprocess.run(["git", "-C", PCREC_SRC] + list(args),
                                  capture_output=True, text=True, env=C_ENV,
                                  timeout=60)
        except (OSError, subprocess.SubprocessError):
            return ""
        return proc.stdout.strip() if proc.returncode == 0 else ""

    def binary_identity(self, testee_id, workdir=None):
        """`testee.binary` (schema v1.2, X29): the `pcrec` this testee runs
        -- the pin script's build, or the provided one -- and its sha256."""
        path = self.binary_for(testee_id)
        return {"path": os.path.realpath(path), "sha256": _ad.sha256_file(path)}

    # ------------------------------------------------------------- describe

    def describe(self, testee_id, workdir=None):
        cfg = self.config(testee_id)
        local = self.is_local(testee_id)
        if local:
            binary = self.local_binary(testee_id)
            version, full, desc_raw, repo = local_provenance(binary)
            desc = ("%s (%s, %s)" % (desc_raw, "DIRTY" if desc_raw.endswith("-dirty")
                                     else "clean", repo)
                    if desc_raw else "no repository beside the binary")
        else:
            full, desc = self.pin_provenance()
        caps = buffer_capacities(cfg)
        # [B24] the compilee toolchain. A config that declares no `cc` gets
        # the literal `$CC` this file has always written and NO cc clause,
        # so its build_flags string is byte-identical to the pre-[B24] one;
        # a config that declares one names it, states its `--version` first
        # line, and says in the same breath that the DRIVER did not move
        # (run.driver_compiler is the other half of the pair).
        cc_text, cc_extra = "$CC", cfg.get("cc_extra")
        cc_note = ""
        if cc_extra:
            cc_text = cfg["cc"]
            cc_note = ("; COMPILEE TOOLCHAIN pinned by configs.toml to `%s` "
                       "-- %s -- while the timing driver stays on $CC "
                       "(run.driver_compiler), so this testee differs from "
                       "its gcc sibling in exactly one variable ([B24], "
                       "pcrec [CC-CLANG])"
                       % (cfg["cc"], cc_version_line(cfg["cc"])))
        # [B31] the emitted-size caps. Same shape as the cc note and for
        # the same reason: absent -> the empty string, so a config that
        # declares neither key renders the pre-[B31] build_flags byte for
        # byte. The VALUES are already visible in `pcrec flags` above (the
        # raise rides in `flags`); this clause states what they MEAN, so a
        # reader of a record does not have to know limits.md 8 to see that
        # this artifact was allowed to be larger than pcrec ships for.
        cap_note = ""
        if cfg.get("cap_extra"):
            named = ", ".join(
                "%s raised to %d B (pcrec default %d)"
                % (flag, value, archived_limit(limit_name))
                for flag, limit_name, value in cap_values(cfg))
            cap_note = ("; EMITTED-SIZE CAPS raised per compile ([B31], pcrec "
                        "limits.md 8, raise-only): %s -- an artifact this "
                        "testee accepts may be one its plain sibling REFUSES, "
                        "and the raise also moves the [ART-SIZE] size-term "
                        "ladder's own abort bound, so the two are different "
                        "artifacts and not one artifact with a gate removed"
                        % named)
        # [B32] the denied generation axes. Same shape as the two notes
        # above and for the same reason: absent -> the empty string, so a
        # config that denies nothing renders the pre-[B32] build_flags byte
        # for byte. The flag is already visible in `pcrec flags`; this
        # clause states what denying it MEANS, because a reader comparing
        # two rows needs to know that the denied one is a different MACHINE
        # and not the same one with an accelerator turned off.
        deny_note = ""
        if cfg.get("deny_flags"):
            deny_note = ("; GENERATION AXES DENIED ([B32]): "
                         + "; ".join(
                             "%s -- %s" % (flag, why)
                             for flag, word, why in DENY_FLAGS
                             if word in [w for _f, w in cfg["deny_flags"]]))
        buffer_note = ""
        runtime = runtime_options(cfg.get("flags", []))
        if caps:
            buffer_note = ("; caller-provided frame buffer (match_api.md 10): "
                           "%d resume frames, %d trail entries -- CAPACITIES, "
                           "sized per artifact from its stamped frame sizes; "
                           "the _in entries used in every regime"
                           % caps)
            runtime += [{"name": "buffer_frames", "value": caps[0]},
                        {"name": "buffer_trail", "value": caps[1]}]
        # record_schema.md 6.2: where a testee is pinned to a VCS revision
        # rather than a release -- "which is pcrec ALWAYS" -- engine_commit
        # carries the 40-hex and engine_version a git-describe-shaped string,
        # and the binding rule is that the version be REPRODUCIBLE from the
        # commit. `git describe --always` is exactly that function of it.
        # A LOCAL binary has no such commit: its version is the `local:`
        # shape (the binary's own digest), computed above.
        if not local:
            version = re.sub(r"[^A-Za-z0-9._+-]", "-", desc)
        provenance = ("local binary $%s=%s (sha256 %s); %s"
                      % (_ad.Adapter.config(self, testee_id).get("binary", "PCREC_BIN"),
                         binary, _ad.sha256_file(binary)[:16], desc)
                      if local else "pin %s (%s)" % (self.pin(), desc))
        block = {
            "engine_name": "pcrec",
            "engine_version": version,
            "engine_commit": full or None,
            "execution_model": "compiled-aot",
            # pcrec ships both a DFA engine and a backtracking VM and chooses
            # per pattern (`--engine=auto`), so the TESTEE's class is hybrid
            # even where one artifact turns out to be pure DFA. Which engine
            # a given artifact used is the per-pattern `engine` metadata pair.
            "automaton_class": "hybrid",
            "openness": "open-source",
            "license_id": "MIT",
            "conventions": ["perl-leftmost-first"],
            "captures": cfg.get("captures", "on"),
            "engine_mode": cfg["engine_mode"],
            "simd": "n-a",
            "build_flags": "%s; pcrec flags %s; artifact built with "
                           "%s -O2 -fPIC -shared%s%s%s%s"
                           % (provenance, " ".join(cfg.get("flags", [])),
                              cc_text, cc_note, buffer_note, cap_note,
                              deny_note),
            "runtime_options": runtime,
            "compile_cost_definition": (
                "AOT (requirements 3): every phase from pattern text to a "
                "loadable object, each timed -- `emit-c` (the pcrec CLI), "
                "`gcc` (the artifact + shim into a .so -- the phase's NAME, "
                "fixed so a clang testee's phase compares against its gcc "
                "sibling's; which compiler ran it is in `build_flags` and "
                "in the testee_id, [B24]), `load` (dlopen). Each "
                "trial builds its own .so, because the dynamic loader caches "
                "by path and a repeated dlopen of one path measures the cache. "
                "Median of N with spread is the REPORTER's reduction; the "
                "record keeps the raw trials. A REFUSAL's cost (KB-4, "
                "docs/dev/known_issues.md; pcrec I-20: it prints no timing "
                "on any path) is the bench's own clock around the pcrec "
                "exec -- `emit-c` only, since a refused compile never "
                "reaches `gcc`/`load`."),
            "compile_phases": ["emit-c", "gcc", "load"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }
        # record_schema.md 6.4's `config_extra`: "the escape hatch for two
        # testees that differ ONLY in build_flags (which is never
        # filtered)". BOTH added axes are exactly that case -- same engine,
        # same version, same mode, same captures, same simd -- so without
        # this a clang sibling and its gcc one, or a bigcap sibling and its
        # plain one, would DERIVE THE SAME testee_id and land on top of
        # each other in the store. `compose_config_extra` is the ONE place
        # the parts are ordered ([B31]); the schema only ever sees the
        # whole slug.
        extra = compose_config_extra(cc_extra, cfg.get("cap_extra"),
                                     cfg.get("deny_extra"))
        if extra:
            block["config_extra"] = extra
        if local:
            # SCRATCH BY CONSTRUCTION (record_schema.md 6.8, X28/X29): the
            # harness lifts `tier` to the setup layer; `binary` stays here.
            block["tier"] = "scratch"
            block["binary"] = self.binary_identity(testee_id, workdir)
        return block

    # -------------------------------------------------------------- prepare

    def prepare(self, testee_id, workdir):
        self.config(testee_id)
        os.makedirs(workdir, exist_ok=True)
        self.binary_for(testee_id)
        build_driver(os.path.join(HERE, "driver.c"),
                     os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])

    # -------------------------------------------------------------- compile

    def compile(self, testee_id, pattern_id, pattern, options, trials,
                workdir):
        r"""TWO artifacts per pattern: `plain` and `whole-subject`.

        pcrec has no end-anchored generation axis (a ratified but unbuilt
        option, pcrec [OS-4]), so "does the WHOLE subject match" cannot be
        answered by the plain artifact: its anchored entry returns the
        leftmost-first match at position 0, and testing `== n` is sufficient
        but NOT necessary. MEASURED: `a|ab` over `ab` returns length 1, so
        `== n` says NO where PCRE2 under ANCHORED|ENDANCHORED says YES.

        So the match/compliance regime gets its own artifact compiled from
        `(?:<pattern>)\z`, and BOTH are timed and given their own compile
        rows -- they are different compiles of different text, and folding
        their costs together would report a compile cost for an artifact the
        record does not witness (rule X27)."""
        forms = {}
        for form, text in ((_ad.FORM_PLAIN, pattern),
                           (_ad.FORM_WHOLE_SUBJECT,
                            _rec.whole_subject_text(pattern))):
            forms[form] = self._compile_one(testee_id, pattern_id, form, text,
                                            trials, workdir)
        return _ad.CompiledPattern(forms)

    def _compile_one(self, testee_id, pattern_id, form, pattern, trials,
                     workdir):
        import time
        cfg = self.config(testee_id)
        pcrec = self.binary_for(testee_id)
        drv = build_driver(os.path.join(HERE, "driver.c"),
                           os.path.join(workdir, "pcrec_driver"), extra=["-ldl"])
        # [B24]: the config decides the COMPILEE toolchain, falling back to
        # `$CC` and then gcc for a config that declares none (`config()`
        # resolves it; `effective_cc` is the one rule). The shim is compiled
        # by the same command -- it #includes the artifact, they are one
        # translation unit -- so the pair can never drift apart.
        cc = cfg["cc"]
        bufargs = buffer_args(cfg)

        phase_seconds = []
        libs = []
        meta = {}
        engine_why = None
        artifact_bytes = None

        for t in range(1, trials + 1):
            # per-PATTERN, per-FORM, per-TRIAL scratch: see Adapter.compile's
            # docstring for the bug the per-pattern part exists to prevent,
            # and this method's for why the form must not share either.
            cdir = os.path.join(workdir, "p-" + pattern_id, form, "t%d" % t)
            os.makedirs(cdir, exist_ok=True)
            art_c = os.path.join(cdir, "artifact.c")

            # phase 1: emit-c ------------------------------------------------
            argv = ([pcrec, "-p", "rx"] + list(cfg.get("flags", []))
                    + ["-o", art_c, "--"] + [pattern.decode("latin-1")])
            t0 = time.monotonic()
            proc = subprocess.run(argv, capture_output=True, env=C_ENV,
                                  timeout=600)
            t1 = time.monotonic()
            # KB-4 (docs/dev/known_issues.md, adapter half; I-20's ruling):
            # the pcrec exec is timed regardless of exit code -- `t1 - t0`
            # is computed above whether or not `proc` refused -- so a
            # REFUSAL carries that number forward as its `phase_seconds`,
            # in the same one-dict-per-trial shape a `compiled` result uses
            # (record.compile_row reads phase_seconds[t-1] the same way
            # either way; harness.py already forces trial count to 1 for a
            # non-`compiled` outcome). `emit-c` is the ONLY phase that ran
            # before this refusal, so it is the only key: never invent a
            # `gcc`/`load` number for a phase pcrec never reached.
            if proc.returncode != 0:
                diag = (proc.stderr or b"").decode("utf-8", "replace").strip()
                return _ad.CompileResult("did-not-compile",
                                         phase_seconds=[{"emit-c": t1 - t0}],
                                         diagnostic=diag or "pcrec exit %d"
                                         % proc.returncode)
            if t == 1:
                # [B19] the two source-bytes facts and the advisory warning,
                # measured on the files THIS trial's emit produced (every
                # trial emits the same bytes; the first is read). The .h is
                # emitted beside the .c and pcrec sums both before it caps
                # or warns, so both are summed here.
                emit_files = [art_c]
                art_h = art_c[:-2] + ".h"
                if os.path.exists(art_h):
                    emit_files.append(art_h)
                emit_meta = self._emit_facts(
                    emit_files,
                    (proc.stderr or b"").decode("utf-8", "replace"))

            # phase 2: gcc ---------------------------------------------------
            so = os.path.join(cdir, "artifact-%d.so" % t)
            # ONE translation unit: shim.c #includes the artifact's .c, so
            # the D46 stamps (which pcrec emits into the .c only) are
            # preprocessor-visible. See shim.c's header comment.
            gargv = [cc, "-O2", "-std=gnu11", "-fPIC", "-shared", "-o", so,
                     os.path.join(HERE, "shim.c"),
                     "-DPB_ARTIFACT=\"%s\"" % art_c, "-I", cdir]
            g0 = time.monotonic()
            gproc = subprocess.run(gargv, capture_output=True, text=True,
                                   env=C_ENV, timeout=900)
            g1 = time.monotonic()
            if gproc.returncode != 0:
                # KB-4 again: the pcrec exec DID succeed on this path (only
                # gcc/clang refused), so its emit-c timing is a real number
                # too -- carried the same way as the emit-c refusal above.
                return _ad.CompileResult(
                    "did-not-compile",
                    phase_seconds=[{"emit-c": t1 - t0}],
                    diagnostic="the artifact did not build:\n%s\n%s"
                               % (" ".join(gargv), gproc.stderr))

            # phase 3: load, timed by the driver -----------------------------
            # The buffer options ride along so the load-only run's `info`
            # block -- which is where the compile row's engine_metadata comes
            # from -- says what the measuring runs will actually use.
            out = run_driver([drv, "--lib", so, "--trial", str(t)] + bufargs,
                             timeout=120, cwd=cdir)
            if out.returncode != 0:
                # THE ABI FLOOR is a REFUSAL, not a crashed measurement.
                # driver.c compares rx_info.abi against shim.c's own
                # PB_SHIM_MIN_ABI before it reads anything else and says so by
                # name; carrying pcrec's two numbers straight through means
                # this file keeps no second copy of the floor to fall out of
                # step with (the check-design failure this project has paid
                # for). Anything else from the driver stays `crashed`.
                diag = out.diagnostic() or ""
                if ABI_FLOOR_TOKEN in diag:
                    raise _ad.AdapterError(
                        "pcrec artifact refused by testees/pcrec/shim.c: %s"
                        % diag.strip())
                return _ad.CompileResult("crashed",
                                         diagnostic=diag
                                         or "the driver could not load %s" % so)
            load_s = 0.0
            for _trial, phase, secs in out.compile_lines:
                if phase == "load":
                    load_s = secs
            phase_seconds.append({"emit-c": t1 - t0, "gcc": g1 - g0,
                                  "load": load_s})
            libs.append(so)
            if t == 1:
                forced = any(f.startswith("--engine=")
                             for f in cfg.get("flags", []))
                meta, engine_why = self._metadata(out.info, forced=forced)
                pairs, warn_line = emit_meta
                meta.update(pairs)
                if warn_line:
                    engine_why = ((engine_why + "\n") if engine_why else "") \
                        + "pcrec stderr: " + warn_line
                self._giveup_bounds = (int(out.info.get("err_floor", -5)),
                                       int(out.info.get("err_giveup_top", -2)))
                artifact_bytes = os.path.getsize(so)

        handle = {"driver": drv, "lib": libs[0],
                  "giveup_range": getattr(self, "_giveup_bounds", (-5, -2)),
                  "buffer_args": bufargs}
        return _ad.CompileResult("compiled", phase_seconds=phase_seconds,
                                 engine_metadata=meta, handle=handle,
                                 artifact_bytes=artifact_bytes,
                                 diagnostic=engine_why)

    @staticmethod
    def _emit_facts(emit_files, stderr_text):
        """-> ({emit_bytes, emit_code_bytes[, warned_emit_bytes]}, warn_line)
        for one emit-c run ([B19]). The port is CONTROLLED here on every
        compile whose warning fired: pcrec's two numbers must equal the
        port's, or the record would carry a size computed by a definition
        that is not the one the caps enforce -- an AdapterError, never a
        number."""
        tot, code = emit_size(emit_files)
        # [B32] the scan-edge covariate, on EVERY compile row that reached
        # emission: 0 is a real value (a forced-VM artifact, a
        # `-fno-scan-edge` build, a scan with no collapsible run), which is
        # what lets a reader regress time on the count instead of merely
        # splitting rows on `dfa_scan_edge`.
        edges, edges_match = scan_edge_counts(emit_files)
        pairs = {"emit_bytes": tot, "emit_code_bytes": code,
                 "scan_edges": edges, "scan_edges_match": edges_match}
        warn = parse_warn_line(stderr_text)
        if warn is None:
            return pairs, None
        w_tot, w_code, _thr, line = warn
        if (w_tot, w_code) != (tot, code):
            raise _ad.AdapterError(
                "pcrec's --warn-emit-bytes line says the artifact is %d "
                "bytes (%d of code) but this adapter's port of pcrec's "
                "emit_size_measure counts %d (%d of code) over %s. The two "
                "must agree byte for byte (the same definition, src/core/"
                "compile.c); re-derive emit_size() against the pin."
                % (w_tot, w_code, tot, code, ", ".join(emit_files)))
        pairs["warned_emit_bytes"] = w_tot
        return pairs, line

    def _metadata(self, info, forced=False):
        """The driver's `info` pairs -> declared engine_metadata, plus the
        prose `engine_why` which is returned SEPARATELY: requirements 4.2 is
        explicit that it is kept only as an unindexed diagnostic string.
        `forced` is whether the CONFIG named `--engine=` -- the control on
        `engine_sel` ([B19]), which has no rx_info mirror.

        Every pair recorded here is DECLARED in METADATA_DECL (rule X15
        rejects an undeclared one), comes from a STRUCTURED field or a
        preprocessor stamp, and is recorded ONCE. Where pcrec publishes a
        fact in two places the second is spent on `_check_agreement` instead
        of on a second column."""
        meta = {}
        for name in INT_PAIRS:
            if name in info:
                meta[name] = int(info[name])
        for name in STR_PAIRS:
            if name in info:
                meta[name] = info[name]
        for name in MASK_BITS:
            if name in info:
                meta[name] = _mask_names(name, int(info[name], 0))
        self._check_agreement(info, meta, forced=forced)
        why = info.get("engine_why")
        return meta, ("RX_ENGINE_WHY: %s" % why) if why else None

    @staticmethod
    def _check_agreement(info, meta, forced=False):
        """pcrec publishes three facts TWICE -- once as a preprocessor stamp
        and once as an `rx_info` field -- and asserts on its own side, over
        its whole corpus and on both engines, that the two agree
        (`tests/codegen/run_dfa_stamps.sh`; match_api.md 6's "ONE DERIVATION,
        TWO SPELLINGS"). This bench reads BOTH and checks them here, because
        a disagreement is a compiler or shim bug rather than a measurement,
        and a record that quietly kept one of the two would carry the bug
        forward as a number.

        The four claims checked, each an AdapterError naming both values:

        1. `<PREFIX>_ENGINE` == the string form of `rx_info.engine`.
        2. `rx_info.prefilter` is NEVER NULL (match_api.md 6, consequence 1).
        3. `<PREFIX>_DFA_SCAN` is present IFF `rx_info.scan` is non-NULL, and
           equal to it when both are there. This is the iff 6.3 (a) states,
           and it is the reason "not a hybrid" can be read from a VALUE.
        4. `rx_info.prefilter` == `<PREFIX>_DFA_PREFILTER` where the artifact
           contains a DFA scan, and == `<PREFIX>_VM_PREFILTER` (which is
           `"none"` there) where it does not. The field reports the mechanism
           that ACTUALLY RUNS and never the coarse `"hybrid"`, so on a hybrid
           it is the DFA's vocabulary that must match -- consequence 3.

        [B18] added three more, in the same spirit:

        5. `<PREFIX>_DFA_MATCH` is present IFF `rx_info.match_form` is
           non-NULL, and equal to it ([ENG-ABS]; the field is NULL on every
           VM artifact, hybrids included, and that NULL is read as a value).
        6. `dfa_prefilter_offsets` is `"none"` IFF `dfa_prefilter` is not an
           offset-set value ([OPT-K], 6.3's iff from both sides), and names
           a scanned offset (`*`) when it is one.
        7. THE SCOPE TABLE (`STAMP_SCOPE`): at the artifact's own abi, every
           stamp pcrec emits unconditionally is present inside its scope
           and absent outside an exclusive one. This is how "never infer
           from absence" and "the shim reads macros through #ifdef" coexist:
           the #ifdef keeps an older artifact linking, and this rule makes
           a missing unconditional stamp an error instead of a blank.

        [B19] added two for the abi-12 stamps, which have no rx_info mirror:

        8. `engine_sel` is `forced` IFF the config named `--engine=` (the
           registry's `engine-route` order-1 row: "the caller named the
           engine, so auto selected nothing").
        9. `engine_sel` implies its neighbours (match_api.md 6.3's table):
           `collapsed-prefilter` / `size-cap-retry` ([B22]) -> engine vm,
           prefilter hybrid, language `count-collapsed`; `overflowed-dfa` /
           `overflowed-prefilter` / `declined-nullable` ([B22]) /
           `declined-nullable-default` ([B26], [OPT-4.2]) ->
           engine vm, prefilter `none` (no prefilter survived, or the
           offered rescue was declined as nullable, or -- the eighth value
           -- the ORDINARY hybrid's own exact language was). Both DECLINE
           values additionally imply NO language pair, asserted directly
           here as well as by the scope table's `vm-hybrid` row.

        [B26] added one more, for the abi-15 FIELDS, which have no macro
        mirror at all:

        10. `rx_info.name` is never NULL ([DD-13b.W1.2] makes that a
            contract, not an observation) and `nentries >= nnames` (the
            named rows are a PREFIX of the array). Their EQUALITY, true on
            every artifact this pin emits, is checked by value in
            tools/selfcheck.py rather than asserted here.

        A pcrec too old to stamp a given macro is not a disagreement: an
        absent macro is checked only against the field's own absence, never
        against a value, and the scope table applies from each stamp's own
        abi. That is rule 1 of the module docstring, applied to the control
        rather than to the datum."""
        engine = meta.get("engine")
        stamp = info.get("engine_stamp")
        if stamp is not None and engine is not None and stamp != engine:
            raise _ad.AdapterError(
                "pcrec artifact disagrees with itself about its ENGINE: "
                "<PREFIX>_ENGINE is %r but rx_info.engine reads %r. One "
                "emitter writes both (match_api.md 6.3 (a)), so this is a "
                "compiler or shim bug, not a measurement." % (stamp, engine))

        if info.get("rxinfo_prefilter_present") == "0":
            raise _ad.AdapterError(
                "pcrec artifact has rx_info.prefilter == NULL. match_api.md "
                "6 consequence 1 states it is NEVER NULL -- every artifact "
                "has an answer to 'what candidate-start mechanism do you "
                "carry', including \"none\".")

        field_scan = info.get("rxinfo_scan")           # None when NULL
        macro_scan = meta.get("dfa_scan")              # None when unstamped
        has_field = info.get("rxinfo_scan_present") == "1"
        if macro_scan is not None and not has_field:
            raise _ad.AdapterError(
                "pcrec artifact stamps <PREFIX>_DFA_SCAN %r but rx_info.scan "
                "is NULL. match_api.md 6.3 (a) states the relation as an "
                "IFF; on this artifact it does not hold." % (macro_scan,))
        if macro_scan is not None and field_scan != macro_scan:
            raise _ad.AdapterError(
                "pcrec artifact disagrees with itself about its DFA SCAN: "
                "<PREFIX>_DFA_SCAN is %r, rx_info.scan reads %r."
                % (macro_scan, field_scan))

        field_pf = info.get("rxinfo_prefilter")
        macro_dfa_pf = meta.get("dfa_prefilter")
        macro_vm_pf = meta.get("prefilter")
        if macro_dfa_pf is not None:
            if field_pf != macro_dfa_pf:
                raise _ad.AdapterError(
                    "pcrec artifact disagrees with itself about its "
                    "CANDIDATE-START mechanism: <PREFIX>_DFA_PREFILTER is "
                    "%r, rx_info.prefilter reads %r. The field reports the "
                    "mechanism that actually runs and must equal the DFA "
                    "scan's own stamp, hybrid included (match_api.md 6, "
                    "consequence 3)." % (macro_dfa_pf, field_pf))
        elif macro_vm_pf is not None and field_pf is not None:
            if field_pf != macro_vm_pf:
                raise _ad.AdapterError(
                    "pcrec artifact has no DFA scan, so rx_info.prefilter "
                    "should be <PREFIX>_VM_PREFILTER's value %r; it reads "
                    "%r." % (macro_vm_pf, field_pf))

        # 5. ([B18], [ENG-ABS]) `<PREFIX>_DFA_MATCH` is present IFF
        #    `rx_info.match_form` is non-NULL, and equal to it. The field is
        #    printed on every artifact, so a VM artifact's NULL is a value.
        field_mf = info.get("rxinfo_match_form")
        has_mf = info.get("rxinfo_match_form_present") == "1"
        macro_mf = meta.get("dfa_match")
        if macro_mf is not None and not has_mf:
            raise _ad.AdapterError(
                "pcrec artifact stamps <PREFIX>_DFA_MATCH %r but "
                "rx_info.match_form is NULL (match_api.md 6.3: the field "
                "mirrors the macro)." % (macro_mf,))
        if macro_mf is None and has_mf:
            raise _ad.AdapterError(
                "pcrec artifact has rx_info.match_form %r but no "
                "<PREFIX>_DFA_MATCH stamp." % (field_mf,))
        if macro_mf is not None and field_mf != macro_mf:
            raise _ad.AdapterError(
                "pcrec artifact disagrees with itself about its _match "
                "FORM: <PREFIX>_DFA_MATCH is %r, rx_info.match_form reads "
                "%r." % (macro_mf, field_mf))

        # 6. ([B18], [OPT-K]) `dfa_prefilter_offsets` is "none" IFF
        #    `dfa_prefilter` is not an offset-set value (6.3's iff, both
        #    sides), whenever both are recorded.
        ofs = meta.get("dfa_prefilter_offsets")
        if ofs is not None and macro_dfa_pf is not None:
            is_set = macro_dfa_pf in OFFSET_SET_VALUES
            if is_set and ofs == "none":
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_DFA_PREFILTER %r but "
                    "<PREFIX>_DFA_PREFILTER_OFFSETS \"none\" -- an offset-set "
                    "filter with no offsets (match_api.md 6.3's iff)."
                    % (macro_dfa_pf,))
            if not is_set and ofs != "none":
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_DFA_PREFILTER %r (not an "
                    "offset-set value) but <PREFIX>_DFA_PREFILTER_OFFSETS %r "
                    "-- the offsets stamp must read \"none\" there."
                    % (macro_dfa_pf, ofs))
            if is_set and "*" not in ofs:
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_DFA_PREFILTER_OFFSETS %r "
                    "with no `*` -- no offset is marked as the scanned one."
                    % (ofs,))

        # 8. ([B19], [OPT-4]) `engine_sel` "forced" IFF the config named
        #    --engine= -- the stamp has no field mirror, so the CONFIG is
        #    its control.
        sel = meta.get("engine_sel")
        if sel is not None:
            if forced and sel != "forced":
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_ENGINE_SEL %r but this "
                    "testee named --engine= on the command line; the "
                    "registry's engine-route axis says a named engine "
                    "stamps \"forced\" (auto selected nothing)." % (sel,))
            if not forced and sel == "forced":
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_ENGINE_SEL \"forced\" "
                    "but this testee named no --engine= -- nothing forced "
                    "it; a compiler or shim bug, or a flag this adapter did "
                    "not pass on purpose.")
            # 9. the implications of the non-ordinary tokens ([B22]: the
            #    263b013 pair joins them -- `size-cap-retry` is a surviving
            #    collapsed prefilter like `collapsed-prefilter`, and
            #    `declined-nullable` leaves no prefilter like the two
            #    `overflowed-*` values; the language pair's absence on a
            #    declined artifact is the scope table's vm-hybrid row).
            #    [B26]: `declined-nullable-default` ([OPT-4.2], abi 14) is
            #    the SAME implication as `declined-nullable` -- match_api.md
            #    6.3 says the ordinary hybrid's own EXACT language was the
            #    thing declined, so no prefilter survives -- and the check
            #    asserts BOTH directions of that iff: vm / prefilter `none`
            #    here, and NO language pair via the scope table's vm-hybrid
            #    row (a `none` prefilter is not `hybrid`, so the pair must
            #    be absent). The two decline values differ only in whether
            #    a RUNG was involved, which is exactly why pcrec kept them
            #    apart, and nothing in this check collapses them.
            lang = meta.get("vm_prefilter_lang")
            if sel in ("collapsed-prefilter", "size-cap-retry") and not (
                    engine == "vm" and macro_vm_pf == "hybrid"
                    and lang == "count-collapsed"):
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_ENGINE_SEL %r (the retry "
                    "KEPT a prefilter rebuilt from the collapsed language) "
                    "but reads engine "
                    "%r, <PREFIX>_VM_PREFILTER %r, <PREFIX>_VM_PREFILTER_LANG "
                    "%r -- match_api.md 6.3's table says vm / hybrid / "
                    "count-collapsed." % (sel, engine, macro_vm_pf, lang))
            if sel in ("overflowed-dfa", "overflowed-prefilter",
                       "declined-nullable",
                       "declined-nullable-default") and not (
                    engine == "vm" and macro_vm_pf == "none"):
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_ENGINE_SEL %r (no "
                    "prefilter survived the fallback, or the offered rescue "
                    "was declined as nullable) but reads engine %r, "
                    "<PREFIX>_VM_PREFILTER %r -- match_api.md 6.3's table "
                    "says vm / none." % (sel, engine, macro_vm_pf))
            if sel in ("declined-nullable",
                       "declined-nullable-default") and lang is not None:
                raise _ad.AdapterError(
                    "pcrec artifact stamps <PREFIX>_ENGINE_SEL %r (the "
                    "prefilter was DECLINED, so none survives) but also "
                    "carries <PREFIX>_VM_PREFILTER_LANG %r -- match_api.md "
                    "6.3's iff runs both ways: no prefilter, no language "
                    "pair." % (sel, lang))

        # 10. ([B26], abi 15 / [DD-13b.W1.2]) the two new FIELDS carry
        #     their own contracts instead of a macro control, and both
        #     are asserted rather than assumed: `rx_info.name` is NEVER
        #     NULL (a compile that names nothing stamps its own
        #     `<prefix>`), and `groups[0 .. nnames)` is a PREFIX of the
        #     whole array, so `nentries >= nnames`. Equality is the TODAY
        #     fact and is asserted by value in tools/selfcheck.py, not
        #     here: `.rxt` composition ([DD-13b.W1.3]) will separate the
        #     two without breaking this invariant, and an adapter that
        #     asserted equality would refuse the first such artifact as a
        #     bug.
        if info.get("rxinfo_name_present") == "0":
            raise _ad.AdapterError(
                "pcrec artifact has rx_info.name == NULL. match_api.md 6 "
                "([DD-13b.W1.2]) makes it a CONTRACT that the field is "
                "never NULL -- a compile that supplies no name stamps its "
                "own <prefix> -- so this is a pcrec or shim bug, not an "
                "unnamed artifact.")
        n_entries, n_names = meta.get("nentries"), meta.get("nnames")
        if n_entries is not None and n_names is not None \
                and n_entries < n_names:
            raise _ad.AdapterError(
                "pcrec artifact has rx_info.nentries %d < rx_info.nnames "
                "%d. match_api.md 6 says groups[0 .. nnames) is a PREFIX "
                "of the whole array, so the whole can never be shorter "
                "than its prefix." % (n_entries, n_names))

        # 7. ([B18]) THE SCOPE TABLE: every unconditional stamp is present
        #    within its scope at the artifact's own abi, and the exclusive
        #    scopes are empty outside it. An absence here is a contract
        #    violation (pcrec's D81), never "not stamped".
        abi = meta.get("abi")
        if abi is None:
            return
        in_scope = {
            "every": True,
            "dfa-scan": has_field,
            "dfa": engine == "dfa",
            "vm": engine == "vm",
            "vm-hybrid": engine == "vm" and macro_vm_pf == "hybrid",
        }
        scope_name = {"every": "every artifact",
                      "dfa-scan": "every artifact containing a DFA scan",
                      "dfa": "every DFA artifact",
                      "vm": "every VM artifact",
                      "vm-hybrid": "every VM HYBRID (RX_VM_PREFILTER "
                                   "\"hybrid\")"}
        for pair, (scope, since) in STAMP_SCOPE.items():
            if abi < since:
                continue
            present = pair in meta
            if in_scope[scope] and not present:
                raise _ad.AdapterError(
                    "pcrec artifact at abi %d is missing the `%s` pair, "
                    "which pcrec stamps UNCONDITIONALLY on %s since abi %d "
                    "(D81). An unconditional stamp that went silent is a "
                    "compiler or shim bug, not a blank."
                    % (abi, pair, scope_name[scope], since))
            if scope in EXCLUSIVE_SCOPES and present and not in_scope[scope]:
                raise _ad.AdapterError(
                    "pcrec artifact (engine %r, RX_VM_PREFILTER %r) carries "
                    "the `%s` pair, which is scoped to %s only (match_api.md "
                    "6.3)." % (engine, macro_vm_pf, pair, scope_name[scope]))

    # -------------------------------------------------------------- measure

    def measure(self, handle, regime, subjects, iters, trials, timeout=None):
        from pcrecbench.subbench import REGIME_MODE
        argv = [handle["driver"], "--lib", handle["lib"],
                "--mode", REGIME_MODE[regime], "--iters", str(iters)]
        if regime == "throughput":
            argv.append("--find-all")
        argv += list(handle.get("buffer_args") or [])
        return per_trial(argv, subjects, trials, timeout=timeout,
                         pin=handle.get("pin"),
                         subject_timeout=handle.get("subject_timeout"))
