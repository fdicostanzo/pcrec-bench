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
static const unsigned char *buf;
static size_t len;

/* the offset of the next byte at or after i that is not a splice */
static size_t sk(size_t i) {
    while (i + 1 < len && buf[i] == '\\' && buf[i + 1] == '\n') i += 2;
    return i;
}
static int ch(size_t i) { return i < len ? buf[i] : -1; }
static size_t nx(size_t i) { return sk(i + 1); }
static int alpha(int c) { return c >= 'a' && c <= 'z' || c >= 'A' && c <= 'Z' || c == '_' || c == '$' || c >= 128; }
static int digit(int c) { return c >= '0' && c <= '9'; }

/* BOILERPLATE shim */
int ub_setup(const unsigned char *pattern, size_t plen, const char *member) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * subj[0, n) (bytes before `start` stay visible). Fill m->s, m->e and, for
 * cscan, the body in m->g1s, m->g1e. */
/* BOILERPLATE shim */
int ub_find(const unsigned char *subj, size_t n, size_t start, ub_span *m) {
/* END BOILERPLATE */
    buf = subj; len = n;
    if (n - start < 3 || memcmp(subj + start, "(?{", 3)) return UB_N;
    size_t i = sk(start + 3), d = 1;
    for (int c; (c = ch(i)) >= 0; i = nx(i)) {
        int c1 = ch(nx(i));
        if (alpha(c)) {
            while (alpha(ch(nx(i))) || digit(ch(nx(i)))) i = nx(i);
        } else if (digit(c) || c == '.' && digit(c1)) {
            for (int e; e = ch(nx(i)), alpha(e) || digit(e) || e == '.' || e == '\'' && (alpha(ch(nx(nx(i)))) || digit(ch(nx(nx(i)))));) {
                if (e == '\'' || (e | 32) == 'e' && (ch(nx(nx(i))) == '+' || ch(nx(nx(i))) == '-')
                    || (e | 32) == 'p' && (ch(nx(nx(i))) == '+' || ch(nx(nx(i))) == '-')) i = nx(i);
                i = nx(i);
            }
        } else if (c == '"' || c == '\'') {
            for (i = nx(i); ch(i) != c; i = nx(i)) {
                if (ch(i) < 0 || ch(i) == '\n') return UB_N;
                if (ch(i) == '\\') i = nx(i);
            }
        } else if (c == '/' && c1 == '*') {
            for (i = nx(nx(i)); ch(i) != '*' || ch(nx(i)) != '/'; i = nx(i))
                if (ch(i) < 0) return UB_N;
            i = nx(i);
        } else if (c == '/' && c1 == '/') {
            while (ch(i) != '\n') if (ch(i = nx(i)) < 0) return UB_N;
        } else if (c == '{' || c == '<' && c1 == '%') {
            d++;
            if (c == '<') i = nx(i);
        } else if (c == '}' || c == '%' && c1 == '>') {
            size_t e = c == '%' ? nx(i) : i;
            if (--d) { i = e; continue; }
            if (ch(nx(e)) != ')') return UB_N;
            m->s = start; m->e = nx(e) + 1;
            m->g1s = start + 3; m->g1e = i;
            return UB_M;
        }
    }
    return UB_N;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */




/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
