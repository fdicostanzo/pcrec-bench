"""testees/pcrec/adapter.py -- the pcrec adapter (harness contract 3).

Provides `pcrec-auto`, `pcrec-nocaps`, `pcrec-vm`, and the caller-provided
frame-buffer variants `pcrec-auto-in` / `pcrec-vm-in`, all at the pin in
`configs.toml` -- and `pcrec-local`, a PROVIDED binary at no pin at all.

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
testee_id says what ran. Everything after describe() -- emit-c / gcc / load,
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
   the size term's VM-only trio on no DFA artifact). The shim still reads
   the macros through #ifdef so an artifact between the floor and a
   macro's abi links and records "not stamped" -- and this rule is what
   keeps that #ifdef from ever hiding a stamp that should have been there.

The ABI FLOOR lives in `shim.c` (`PB_SHIM_MIN_ABI`, 10 since [B18] -- the
abi that appended `match_form`, the third field it reads; 6 before, for
`scan` / `prefilter`) and is enforced in `driver.c`, which
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
                  "values are match_api.md 6.3's / limits.md 8's; the "
                  "registry (`--list-axes`, axis `size-term`) names the "
                  "macro but carries NO stamp_value for it",
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
INT_PAIRS = ("abi", "ncaps", "ngroups", "nnames", "step_budget",
             "work_budget", "frame_capacity", "subject_ceiling",
             "resume_frames", "trail_frames", "resume_frame_size",
             "trail_frame_size", "buffer_frames", "buffer_trail",
             "fast_frames", "fast_trail",
             "unroll_k", "max_emit_code_bytes", "max_emit_bytes")

#: The `info` names carrying a STRING-valued pair, and the declared name each
#: lands under. Kept beside INT_PAIRS so a pair can never be printed by the
#: driver and silently dropped here (`engine_stamp` was, from abi 4 until
#: [B16]: the driver printed it and `_metadata` had no line for it, so the
#: unconditional engine stamp reached no record for five pins).
STR_PAIRS = ("engine", "prefilter", "dfa_scan", "dfa_prefilter", "dfa_table",
             "dfa_prefilter_offsets", "dfa_match", "unroll_k_why")

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
#: The abi thresholds are the spec's (match_api.md 6.3, limits.md 8): the
#: `dfa-scan` rows start at 6 because before [DD-13c] hybrids did not stamp.
STAMP_SCOPE = {
    "engine":                ("every",    4),
    "dfa_scan":              ("dfa-scan", 6),
    "dfa_prefilter":         ("dfa-scan", 6),
    "dfa_table":             ("dfa-scan", 7),
    "dfa_prefilter_offsets": ("dfa-scan", 9),
    "dfa_match":             ("dfa",      10),
    "fast_frames":           ("vm",       5),
    "fast_trail":            ("vm",       5),
    "unroll_k":              ("vm",       11),
    "unroll_k_why":          ("vm",       11),
    "max_emit_code_bytes":   ("vm",       11),
    "max_emit_bytes":        ("every",    11),
}

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
}

#: Declared values the registry's candidate lists do NOT enumerate because
#: they are OUTCOMES rather than candidates the selector walks (MEASURED at
#: 36d5963, [B18]): `RX_DFA_TABLE "none"` is stamped on an `attempt` or
#: `empty` scan (no numeric table exists to have chosen a form for -- the
#: provably-empty witness in tools/selfcheck.py reads it) and `"mixed"` is
#: the forward and reverse machines taking different forms (match_api.md
#: 6.3), while the registry's `table` axis lists only `premultiplied` /
#: `indexed`. Listed here so the reverse direction of `registry_check` still
#: fires on any OTHER declared value the registry lacks; a finding for pcrec
#: (the axis's candidate list under-covers its stamp's value set).
REGISTRY_OUTCOME_VALUES = {
    "dfa_table": {"none", "mixed"},
}

#: The driver's refusal token for an artifact below shim.c's PB_SHIM_MIN_ABI.
#: The NUMBER lives in shim.c and nowhere else; this is only how the refusal
#: is recognised.
ABI_FLOOR_TOKEN = "abi-below-shim-floor"


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
    `true`, same as before."""
    out = []
    i, n = 0, len(flags)
    while i < n:
        f = flags[i]
        if not f.startswith("--"):
            i += 1
            continue
        if "=" in f:
            name, _, value = f.partition("=")
            out.append({"name": name, "value": value})
            i += 1
            continue
        if i + 1 < n and not flags[i + 1].startswith("--"):
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
        if kinds.get(macro) == {"list"}:
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
        what actually ran."""
        cfg = dict(_ad.Adapter.config(self, testee_id))
        if not cfg.get("local"):
            return cfg
        flags = list(cfg.get("flags", []))
        extra_var = cfg.get("extra_flags")
        if extra_var:
            flags += os.environ.get(extra_var, "").split()
        cfg["flags"] = flags
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
                           "$CC -O2 -fPIC -shared%s"
                           % (provenance, " ".join(cfg.get("flags", [])),
                              buffer_note),
            "runtime_options": runtime,
            "compile_cost_definition": (
                "AOT (requirements 3): every phase from pattern text to a "
                "loadable object, each timed -- `emit-c` (the pcrec CLI), "
                "`gcc` (the artifact + shim into a .so), `load` (dlopen). Each "
                "trial builds its own .so, because the dynamic loader caches "
                "by path and a repeated dlopen of one path measures the cache. "
                "Median of N with spread is the REPORTER's reduction; the "
                "record keeps the raw trials."),
            "compile_phases": ["emit-c", "gcc", "load"],
            "warmup_trials": 0,
            "engine_metadata_declaration": dict(METADATA_DECL),
        }
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
        cc = os.environ.get("CC", "gcc")
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
            if proc.returncode != 0:
                diag = (proc.stderr or b"").decode("utf-8", "replace").strip()
                return _ad.CompileResult("did-not-compile",
                                         diagnostic=diag or "pcrec exit %d"
                                         % proc.returncode)

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
                return _ad.CompileResult(
                    "did-not-compile",
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
                meta, engine_why = self._metadata(out.info)
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

    def _metadata(self, info):
        """The driver's `info` pairs -> declared engine_metadata, plus the
        prose `engine_why` which is returned SEPARATELY: requirements 4.2 is
        explicit that it is kept only as an unindexed diagnostic string.

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
        self._check_agreement(info, meta)
        why = info.get("engine_why")
        return meta, ("RX_ENGINE_WHY: %s" % why) if why else None

    @staticmethod
    def _check_agreement(info, meta):
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
        }
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
                    % (abi, pair, {"every": "every artifact",
                                   "dfa-scan": "every artifact containing a "
                                               "DFA scan",
                                   "dfa": "every DFA artifact",
                                   "vm": "every VM artifact"}[scope], since))
            if scope in ("dfa", "vm") and present and not in_scope[scope]:
                raise _ad.AdapterError(
                    "pcrec artifact (engine %r) carries the `%s` pair, which "
                    "is scoped to %s only (match_api.md 6.3)."
                    % (engine, pair, "DFA artifacts" if scope == "dfa"
                       else "VM artifacts"))

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
