/* ASSIST TEMPLATE -- Oniguruma (C). Families: vars, netstr.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine onig`:
 * it writes assists/M/onig/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, -lonig, linked with the assist runner
 * (testees/assist/), which owns main's work, the protocol, the clock and the
 * answer tokens. onig_initialize is yours (in ub_setup). Return UB_M (fill
 * *m), UB_N, UB_R (vars: the call is refused) or, on an engine give-up, the
 * engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <oniguruma.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */


/* Your state (globals), built by ub_setup outside the clock. */
static regex_t *re;
static OnigRegion *reg;

/* The callout after each step of the lazy run: pass only when the run is
 * exactly as long as the number in group 1. */
static int exact_len(OnigCalloutArgs *a, void *u) {
    int b, e;
    onig_get_capture_range_in_callout(a, 1, &b, &e);
    const OnigUChar *s = onig_get_string_by_callout_args(a);
    long len = 0;
    for (int i = b; i < e; i++) len = len * 10 + s[i] - '0';
    return onig_get_current_by_callout_args(a) - s - e - 1 == len ? ONIG_CALLOUT_SUCCESS : ONIG_CALLOUT_FAIL;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    static const char pat[] = "(\\d{1,9}):(?>(?m:.)*?(?{4})),";
    OnigEncoding enc = ONIG_ENCODING_ASCII;
    onig_initialize(&enc, 1);
    onig_set_progress_callout(exact_len);
    reg = onig_region_new();
    return onig_new(&re, (const OnigUChar *)pat, (const OnigUChar *)pat + sizeof pat - 1,
                    ONIG_OPTION_NONE, ONIG_ENCODING_ASCII, ONIG_SYNTAX_ONIGURUMA, 0);
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` in subj[0, n) (bytes before
 * `start` stay visible). Fill m->s, m->e and group 1 in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    int r = onig_search(re, subj, subj + n, subj + start, subj + n, reg, ONIG_OPTION_NONE);
    if (r == ONIG_MISMATCH) return UB_N;
    if (r < 0) return r;
    *m = (ub_span){reg->beg[0], reg->end[0], reg->beg[1], reg->end[1]};
    return UB_M;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
