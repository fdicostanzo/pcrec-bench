/* ASSIST TEMPLATE -- Vectorscan (C). Families: recursion, callouts, netstr, vars.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine vectorscan`:
 * it writes assists/M/vectorscan/assist.c holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: gcc -O2, `pkg-config --cflags --libs libhs`, linked with the
 * assist runner (testees/assist/), which owns main's work, the protocol, the
 * clock and the answer tokens. Scratch space is yours (allocate it in
 * ub_setup). Return UB_M (fill *m), UB_N, UB_R (vars: the call is refused)
 * or, on an engine give-up, the engine's own NEGATIVE code. */

/* BOILERPLATE includes */
#include <hs.h>
#include "ub_assist.h"
#include "ub_map.h"
/* END BOILERPLATE */

/* Your state (globals), built by ub_setup outside the clock. */
static hs_database_t *db;
static hs_scratch_t *scratch;
static char *stack;
static size_t cap, len;
static unsigned kind;

/* the engine lexes one token at the scan's start: ws, string, scalar, punct */
static int on_token(unsigned id, unsigned long long from, unsigned long long to,
                    unsigned flags, void *ctx) {
    kind = id; len = to;
    return 0;
}

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    static const char *pat[] = {
        "^[\\t\\n\\r ]+",
        "^\"([^\\\\\"\\x00-\\x1f]|\\\\[\"\\\\bfnrt/]|\\\\u[0-9a-fA-F]{4})*\"",
        "^(-?(0|[1-9][0-9]*)(\\.[0-9]+)?([eE][+-]?[0-9]+)?|true|false|null)",
        "^[][{},:]"};
    static const unsigned flags[] = {0, 0, 0, 0}, ids[] = {1, 2, 3, 4};
    hs_compile_error_t *err;
    return hs_compile_multi(pat, flags, ids, 4, HS_MODE_BLOCK, NULL, &db, &err) ||
           hs_alloc_scratch(db, &scratch);
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * subj[0, n) (bytes before `start` stay visible). Fill m->s, m->e and, for
 * cscan, the body in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    size_t pos = 0, d = 0;
    int s = 0;  /* 0 value, 1 value or ], 2 key or }, 3 key, 4 colon, 5 after value */
    if (start) return UB_N;
    if (cap < n) stack = realloc(stack, cap = n);
    while (pos < n) {
        kind = 0;
        int r = hs_scan(db, (const char *)subj + pos, n - pos, 0, scratch, on_token, 0);
        if (r) return r;
        int c = subj[pos];
        pos += len;
        if (kind == 1) continue;
        if (!kind) return UB_N;
        if (kind < 4) {
            if (s <= 1) s = 5;
            else if (kind == 2 && (s == 2 || s == 3)) s = 4;
            else return UB_N;
        } else if (c == '[' || c == '{') {
            if (s > 1) return UB_N;
            stack[d++] = c;
            s = c == '[' ? 1 : 2;
        } else if (c == ',') {
            if (s != 5 || !d) return UB_N;
            s = stack[d - 1] == '[' ? 0 : 3;
        } else if (c == ':') {
            if (s != 4) return UB_N;
            s = 0;
        } else {
            if (!d || stack[--d] != c - 2 || (s != 5 && s != (c == ']' ? 1 : 2))) return UB_N;
            s = 5;
        }
    }
    if (s != 5 || d) return UB_N;
    m->s = 0; m->e = n;
    return UB_M;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */




/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
