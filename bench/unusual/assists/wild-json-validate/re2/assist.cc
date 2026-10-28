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

static std::unique_ptr<RE2> tok;


/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
    RE2::Options o;
    o.set_encoding(RE2::Options::EncodingLatin1);
    tok = std::make_unique<RE2>(R"([ \t\n\r]*(?:[\[\]{}:,]|"(?:[^\\"\x00-\x1f]|\\["\\bfnrt/]|\\u[0-9a-fA-F]{4})*")"
        R"(|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null))", o);
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
    if (start) return UB_N;
    // x is what comes next: v value, e value or ], k key, o key or }, : colon, a comma or closer
    std::string open;
    std::string_view g;
    char x = 'v';
    size_t p = 0;
    while (tok->Match(s, p, s.size(), RE2::ANCHOR_START, &g, 1)) {
        p = g.data() - s.data() + g.size();
        char c = s[p - 1], top = open.empty() ? 0 : open.back();
        bool value = x == 'v' || x == 'e', key = x == 'k' || x == 'o';
        if (c == '[' || c == '{') {
            if (!value) return UB_N;
            open += c;
            x = c == '[' ? 'e' : 'o';
        } else if (c == ']' || c == '}') {
            if (top != (c == ']' ? '[' : '{') || (x != 'a' && x != (c == ']' ? 'e' : 'o'))) return UB_N;
            open.pop_back();
            x = 'a';
        } else if (c == ':' || c == ',') {
            if (x != (c == ':' ? ':' : 'a') || (c == ',' && !top)) return UB_N;
            x = c == ':' || top == '[' ? 'v' : 'k';
        } else if (c == '"' && key) {
            x = ':';
        } else {
            if (!value) return UB_N;
            x = 'a';
        }
    }
    if (x != 'a' || !open.empty() || s.find_first_not_of(" \t\n\r", p) != s.npos) return UB_N;
    m->s = 0, m->e = s.size();
    return UB_M;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */




/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
