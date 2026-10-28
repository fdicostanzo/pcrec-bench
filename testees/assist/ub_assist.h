/* testees/assist/ub_assist.h -- the C ABI between an ASSIST file and the
 * assist RUNNER ([B148] lane b148aw, docs/design/unusual_set_v1.md 5, 7.1-7.3).
 *
 * An assist (bench/unusual/assists/<member>/<engine>/assist.<ext>, authored
 * from bench/unusual/assists/templates/<engine>.<ext>) is ONE translation unit
 * in the engine's binding language (C, C++, Rust) that DEFINES the functions
 * below for its family; the runner (ub_runner.c + the timed loops in
 * ub_timed.c) is linked beside it and speaks the driver protocol
 * (pcrecbench/adapters.py) -- search / find-all / `--mode calls` incl. the vars
 * streams -- so an author writes only the assist logic. C++ and Rust export
 * the same symbols `extern "C"`; the template's fenced `shim` region does it.
 *
 * An assist defines only its family's functions: ub_setup always, then
 * ub_find (recursion / callouts / netstr) or ub_vars + ub_reset (vars); the
 * others come from ub_defaults.c (an archive linked after the assist).
 */
#ifndef UB_ASSIST_H
#define UB_ASSIST_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/* One answer's spans: group 0 = [s, e); group 1 = [g1s, g1e) where the
 * member's token carries one (cscan, the callout members, co-netstr), else
 * -1, -1. Absolute subject offsets (vars: line-relative). */
typedef struct { long s, e, g1s, g1e; } ub_span;

/* The return value of ub_find / ub_vars. A NEGATIVE value is an engine
 * GIVE-UP: the value is the engine's own return code (the token `g`, the
 * answer `giveup:<code>`), named by the adapter from its table. */
enum { UB_N = 0, UB_M = 1, UB_R = 2 };

/* One variable of a vars call's binding: the layout of
 * testees/common/vars_io.h's struct vvar. p == NULL is UNSET; p != NULL with
 * len == 0 is EMPTY. A name the binding does not list is UNSET. */
typedef struct { const char *name; const unsigned char *p; size_t len; } ub_var;

/* ---- defined by the ASSIST ------------------------------------------ */

/* Setup, OUTSIDE the clock: compile the assist's fixed patterns, build its
 * state. `pattern` is the member's canonical pattern bytes (the set's
 * patterns/<member>.rx), `member` its id. -> 0, or nonzero = the setup failed
 * (the adapter records `did-not-compile`; say why with ub_fail first). Called
 * once per compile trial; the last trial's state serves every subject. */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member);

/* recursion / callouts / netstr: the FIRST match at or after `start` (cscan:
 * exactly at `start`) in subj[0, n); bytes before `start` stay visible. */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m);

/* vars: one call -- `line` matched ALONE (^ is its first byte, offsets
 * line-relative) under the call's binding. UB_R = refused by the variable
 * rule (the engine not called). */
int ub_vars(const unsigned char *line, size_t n, const ub_var *v, size_t nv,
            ub_span *m);

/* vars: empty the compiled-pattern cache. Called by the runner BETWEEN
 * replays, OUTSIDE the clock (the cache is empty at the start of every
 * replay, unbounded within it). */
void ub_reset(void);

/* ---- provided by the RUNNER ----------------------------------------- */

/* callouts: the SHARED predicate (bench/unusual/callees/, the ONE callees.o)
 * bound to this member's site by `--callees`, evaluated on group 1 =
 * subj[g1s, g1e). -> 1 pass, 0 fail. Pure; the same compiled body every
 * engine calls (unusual_set_v1.md C5; problems/callouts.md 7a). */
int ub_pred(const unsigned char *subj, size_t n, size_t g1s, size_t g1e);

/* vars: the variable `name` of a call's binding, or NULL when it is UNSET
 * (listed as UNSET or not listed). A non-NULL result has p != NULL; len 0
 * is EMPTY. */
const ub_var *ub_lookup(const ub_var *v, size_t nv, const char *name);

/* setup: record why ub_setup failed (printed as the `error` line). */
void ub_fail(const char *msg);

/* the runner's entry point: the template's fenced `main` calls it (the
 * runner has no main of its own, so the same link works for C, C++ and a
 * Rust staticlib). */
int ub_main(int argc, char **argv);

#ifdef __cplusplus
}
#endif

#endif
