/* testees/pcrec/shim.c -- the one file in this project that knows pcrec's ABI.
 *
 * Compiled ONCE PER PATTERN, into the .so the driver dlopens:
 *
 *     $CC -O2 -fPIC -shared -o artifact-N.so shim.c \
 *         -DPB_ARTIFACT='"artifact.c"' -I<the artifact's directory>
 *
 * IT INCLUDES THE ARTIFACT'S `.c`, NOT ITS `.h`, and that is load-bearing
 * rather than a shortcut. The D46 observability stamps -- `RX_VM_PREFILTER`,
 * `RX_VM_RUNGS`, `RX_VM_STRATS`, `RX_VM_PRUNES`, `RX_ENGINE` -- are emitted
 * into the artifact's `.c` ONLY and never into its `.h` (pcrec
 * docs/spec/match_api.md 1, 6.3). A shim that included the header would
 * compile cleanly, see none of them, and silently report a VM artifact as
 * carrying no mechanism stamps at all. MEASURED: it did exactly that before
 * this line was written. One translation unit, and the stamps are
 * preprocessor-visible -- which record_schema.md 7 names as one of the two
 * permitted sources, the other being the linked `rx_info` symbol; both are
 * used here and the declaration's `source` says which for each pair.
 *
 * WHY A SHIM AT ALL. `driver.c` must not re-declare `struct rx_info` or the
 * `<prefix>_*` entry signatures: that would be a second, drifting copy of
 * somebody else's ABI in this repo, which is precisely the failure pcrec's
 * own `tests/fuzz/pcre2_abi.h` header comment was written about ("two
 * descriptions of one thing, with nothing enforcing that they agree"). So the
 * shim `#include`s the artifact's OWN generated source -- the authoritative
 * copy, regenerated with every artifact -- and exports a small, flat,
 * engine-neutral C surface in terms of nothing but <stddef.h> types. If pcrec
 * changes `struct rx_info`, this file stops compiling; it cannot silently
 * disagree.
 *
 * The `pb_vm_*` getters are guarded by #ifdef because the VM stamps are
 * emitted on VM artifacts ONLY (record_schema.md 7: "an ABSENT pair is not an
 * error; an UNDECLARED one is"). A DFA artifact links a shim whose
 * `pb_has_vm_stamps()` returns 0, and the adapter forwards no VM pairs.
 */

#include <stddef.h>
#include <stdint.h>

#include PB_ARTIFACT

/* The adapter always emits with `-p rx`, but the prefix is a parameter here
 * rather than a literal, so a future adapter that needs two artifacts in one
 * process does not have to edit this file. */
#ifndef PB_SEARCH
#define PB_SEARCH      rx_search
#endif
#ifndef PB_MATCH_CAPS
#define PB_MATCH_CAPS  rx_match_caps
#endif
#ifndef PB_INFO
#define PB_INFO        rx_info
#endif

/* ------------------------------------------------- reflection (rx_info) */

int      pb_abi(void)             { return (int)PB_INFO.abi; }
int      pb_ncaps(void)           { return PB_INFO.ncaps; }
int      pb_ngroups(void)         { return PB_INFO.ngroups; }
int      pb_nnames(void)          { return PB_INFO.nnames; }
int      pb_engine(void)          { return (int)PB_INFO.engine; }
long long pb_step_budget(void)    { return (long long)PB_INFO.step_budget; }
long long pb_work_budget(void)    { return (long long)PB_INFO.work_budget; }
long long pb_frame_capacity(void) { return (long long)PB_INFO.frame_capacity; }
long long pb_subject_ceiling(void){ return (long long)PB_INFO.subject_ceiling; }
const char *pb_engine_why(void)   { return PB_INFO.engine_why; }

/* --------------------------------------------- the give-up code SPACE */

/* The artifact's OWN bounds on what a give-up is, so the harness classifies
 * by RANGE and never by a list it keeps in step by hand.
 *
 * pcrec's contract (D49, quoted from the emitted header): a typed give-up is
 * a return in `[PCREC_ERR_FLOOR, -2]` -- one per way the engine can give up
 * -- and the codes PROPAGATE rather than collapsing to -1. Values strictly
 * BELOW the floor are NOT give-ups: `PCREC_ERR_INTERNAL` says so in the
 * artifact itself, and anything further down is reserved for a future abort
 * semantic.
 *
 * Exporting the two numbers means a give-up code pcrec ADDS later is
 * classified correctly by an adapter nobody edited, and a reserved or
 * internal code can never be laundered into `gave-up` by an enumeration that
 * fell behind. `pb_err_name()` is for the row's `diagnostic`, which carries
 * the NAME rather than the bare integer. */

int pb_err_floor(void)    { return (int)PCREC_ERR_FLOOR; }
int pb_err_giveup_top(void) { return -2; }
int pb_err_internal(void) { return (int)PCREC_ERR_INTERNAL; }

const char *pb_err_name(int code) {
    switch (code) {
        case PCREC_ERR_STEPS:    return "PCREC_ERR_STEPS";
        case PCREC_ERR_FRAMES:   return "PCREC_ERR_FRAMES";
        case PCREC_ERR_WORK:     return "PCREC_ERR_WORK";
        case PCREC_ERR_RECURSE:  return "PCREC_ERR_RECURSE";
        case PCREC_ERR_INTERNAL: return "PCREC_ERR_INTERNAL";
        default:                 return (const char *)0;
    }
}

/* ----------------------------------- the D46 stamps (VM artifacts only) */

int pb_has_vm_stamps(void) {
#ifdef RX_VM_RUNGS
    return 1;
#else
    return 0;
#endif
}

const char *pb_vm_prefilter(void) {
#ifdef RX_VM_PREFILTER
    return RX_VM_PREFILTER;
#else
    return (const char *)0;
#endif
}

unsigned pb_vm_rungs(void) {
#ifdef RX_VM_RUNGS
    return (unsigned)RX_VM_RUNGS;
#else
    return 0u;
#endif
}

unsigned pb_vm_strats(void) {
#ifdef RX_VM_STRATS
    return (unsigned)RX_VM_STRATS;
#else
    return 0u;
#endif
}

unsigned pb_vm_prunes(void) {
#ifdef RX_VM_PRUNES
    return (unsigned)RX_VM_PRUNES;
#else
    return 0u;
#endif
}

const char *pb_engine_stamp(void) {
#ifdef RX_ENGINE
    return RX_ENGINE;
#else
    return (const char *)0;
#endif
}

/* ------------------------------------------------------------- matching */

/* Unanchored search from `pos`; `caps` is `pb_ncaps()` pairs.
 * Returns 1 = match, 0 = no match, negative = a typed give-up (D49: the
 * codes PROPAGATE and are NOT collapsed to -1, so the driver reports the
 * number it got). */
int pb_search(const unsigned char *s, size_t n, size_t pos,
              ptrdiff_t (*caps)[2]) {
    return PB_SEARCH(s, n, pos, caps);
}

/* Anchored at `pos`, capture-delivering. Returns the matched LENGTH (>= 0),
 * -1 on no match, or a typed give-up code.
 *
 * THE WHOLE-SUBJECT QUESTION IS THE CALLER'S. pcrec has no end-anchor
 * option, so "does the whole subject match" is answered by the driver as
 * `pb_match_caps(...) == n`. That is a SUFFICIENT test and not a necessary
 * one: a pattern whose leftmost-first anchored match is a strict prefix,
 * but which could reach the subject's end by backtracking, answers `no`
 * here where PCRE2_ANCHORED|PCRE2_ENDANCHORED answers `yes`. The asymmetry
 * is real, it is documented in testees/pcrec/CLAUDE.md, and on this
 * sub-bench it was MEASURED not to bite (85/85 agreement, both patterns). */
long long pb_match_caps(const unsigned char *s, size_t n, size_t pos,
                        ptrdiff_t (*caps)[2]) {
    rx_ctx ctx;
    ctx.subject = s;
    ctx.len = n;
    ctx.pos = pos;
    ctx.ncap = 0;
    ctx.caps = (const ptrdiff_t (*)[2])0;
    ctx.user = (void *)0;
    return (long long)PB_MATCH_CAPS(&ctx, caps);
}
