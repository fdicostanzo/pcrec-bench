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

static std::unique_ptr<RE2> paren;


/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
    paren = std::make_unique<RE2>("[()]");
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` (cscan: exactly at `start`) in
 * the whole subject `s` (bytes before `start` stay visible). Fill m->s, m->e
 * and, for cscan, the body in m->g1s, m->g1e. */
/* BOILERPLATE shim */
static int find(std::string_view s, size_t start, ub_span *m) {
/* END BOILERPLATE */
    std::vector<long> open;
    std::string_view g;
    bool found = false;
    for (size_t p = start; paren->Match(s, p, s.size(), RE2::UNANCHORED, &g, 1);) {
        p = g.data() - s.data() + 1;
        if (g[0] == '(') open.push_back(p - 1);
        else if (!open.empty()) {
            // a pair closed; the leftmost open one wins, so keep reading until none is left
            if (!found || open.back() < m->s) m->s = open.back(), m->e = p;
            found = true;
            open.pop_back();
            if (open.empty()) break;
        }
    }
    return found ? UB_M : UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */




/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
