/* ASSIST TEMPLATE -- libpcre2 (C). Families: vars, netstr.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine pcre2`:
 * it writes assists/M/pcre2/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, -DPCRE2_CODE_UNIT_WIDTH=8, -lpcre2-8, linked with the
 * assist runner (testees/assist/), which owns main's work, the protocol, the
 * clock and the answer tokens. Return UB_M (fill *m), UB_N, UB_R (vars: the
 * call is refused) or, on an engine give-up, the engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <pcre2.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */


/* Your state (globals), built by ub_setup outside the clock. */
static pcre2_code *re;
static pcre2_match_data *md;
static pcre2_match_context *mc;

/* Pass only when the lazy run is exactly LEN bytes; 1 rejects this position. */
static int pred(pcre2_callout_block *cb, void *unused) {
    PCRE2_SIZE *ov = cb->offset_vector;
    long len = 0;
    for (PCRE2_SIZE i = ov[2]; i < ov[3]; i++) len = len * 10 + cb->subject[i] - '0';
    return cb->current_position - (ov[3] + 1) != len;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    int err;
    PCRE2_SIZE off;
    re = pcre2_compile((PCRE2_SPTR)"(\\d{1,9}):(?>(?s:.)*?(?C4)),", PCRE2_ZERO_TERMINATED, 0, &err, &off, NULL);
    md = pcre2_match_data_create_from_pattern(re, NULL);
    mc = pcre2_match_context_create(NULL);
    pcre2_set_callout(mc, pred, NULL);
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` in subj[0, n) (bytes before
 * `start` stay visible). Fill m->s, m->e and group 1 in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    int rc = pcre2_match(re, subj, n, start, 0, md, mc);
    if (rc < 0) return rc == PCRE2_ERROR_NOMATCH ? UB_N : rc;
    PCRE2_SIZE *ov = pcre2_get_ovector_pointer(md);
    m->s = ov[0]; m->e = ov[1]; m->g1s = ov[2]; m->g1e = ov[3];
    return UB_M;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
