/* ASSIST TEMPLATE -- RE2 (C++). Families: recursion, callouts, netstr, vars.
 *
 * Start with `python3 -m pcrecbench assist-init --member M --engine re2`:
 * it writes assists/M/re2/assist.cc holding only M's family. Fill the
 * function(s) marked ASSIST (and your setup); leave every BOILERPLATE fence
 * exactly as it is (the self-test compares them with this template). Read
 * bench/unusual/assists/AUTHORS.md and your problem statement first.
 *
 * Built with: g++ -O2 -std=c++17, `pkg-config --cflags --libs re2`, linked
 * with the assist runner (testees/assist/), which owns main's work, the
 * protocol, the clock and the answer tokens. Your state lives in globals,
 * built by setup outside the clock. Return UB_M (fill *m), UB_N, UB_R (vars:
 * the call is refused) or, on an engine give-up, a NEGATIVE code. */

/* BOILERPLATE includes */
#include <re2/re2.h>
#include <memory>
#include <optional>
#include <string>
#include <string_view>
#include <unordered_map>
#include "ub_assist.h"
/* END BOILERPLATE */


/* BOILERPLATE wrappers */
static bool pred(std::string_view s, size_t b, size_t c) { return ub_pred((const unsigned char *)s.data(), s.size(), b, c) != 0; }
/* END BOILERPLATE */

/* Your state (globals), built by setup outside the clock. */
static std::unique_ptr<RE2> re;

/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
    RE2::Options o;
    o.set_encoding(RE2::Options::EncodingLatin1);
    re = std::make_unique<RE2>("\\buser=(\\w+)", o);
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first PASSING candidate at or after `start` in the whole
 * subject `s` (bytes before `start` stay visible). pred(s, b, c) is the
 * member's shared predicate on group 1 = [b, c). Fill m->s, m->e and group 1
 * in m->g1s, m->g1e. */
/* BOILERPLATE shim */
static int find(std::string_view s, size_t start, ub_span *m) {
/* END BOILERPLATE */
    std::string_view g[2];
    while (start <= s.size() && re->Match(s, start, s.size(), RE2::UNANCHORED, g, 2)) {
        size_t b = g[1].data() - s.data(), c = b + g[1].size();
        if (pred(s, b, c)) {
            m->s = g[0].data() - s.data(), m->e = m->s + g[0].size(), m->g1s = b, m->g1e = c;
            return UB_M;
        }
        start = g[0].data() - s.data() + 1;
    }
    return UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */



/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
