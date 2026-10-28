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
    o.set_dot_nl(true);
    // '~' stands for any run of line splices (backslash, LF) between two bytes;
    // GlobalReplace's rewrite turns each pair of backslashes into one
    std::string p = R"re([A-Za-z_$\x80-\xff]~(?:[A-Za-z0-9_$\x80-\xff]~)*|(?:[0-9]|\.~[0-9])~(?:(?:[eEpP]~[+-]|'~[A-Za-z0-9_]|[A-Za-z0-9_.$\x80-\xff])~)*|"~(?:[^"\\\n]~|\\~[^\n]~)*"|'~(?:[^'\\\n]~|\\~[^\n]~)*'|/~\*~.*?\*~/|/~/(?:[^\\\n]|\\+\n|\\+[^\\\n])*\n|\{|<~%|(?:\}|%~>)~\)?|["']|/~\*~.*|/~/.*)re";
    RE2::GlobalReplace(&p, "~", "(?:\\\\\\\\\n)*");
    tok = std::make_unique<RE2>(p, o);
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
    if (s.substr(start, 3) != "(?{") return UB_N;
    size_t base = start + 3, pos = base;
    int depth = 1;
    std::string_view t;
    // unanchored: the engine skips the bytes that are not tokens
    while (tok->Match(s, pos, s.size(), RE2::UNANCHORED, &t, 1)) {
        size_t b = t.data() - s.data(), e = b + t.size();
        pos = e;
        switch (s[b]) {
        case '{': case '<': ++depth; break;
        case '}': case '%':
            if (depth > 1) { --depth; break; }
            if (s[e - 1] != ')') return UB_N;
            m->s = start, m->e = e;
            m->g1s = base, m->g1e = b;
            return UB_M;
        case '"': case '\'':
            if (e == b + 1) return UB_N;  // a quote that starts no literal
        }
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
