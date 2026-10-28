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




/* BOILERPLATE shim */
struct Binding {                /* one call's binding */
    const ub_var *v;
    size_t n;
    /* the value of `name`, or nullopt when it is UNSET (an EMPTY value is "") */
    std::optional<std::string_view> get(const char *name) const {
        const ub_var *x = ub_lookup(v, n, name);
        return x ? std::optional<std::string_view>(std::string_view((const char *)x->p, x->len)) : std::nullopt;
    }
};
static std::unordered_map<std::string, std::unique_ptr<RE2>> cache;   /* the compiled-pattern cache */
/* END BOILERPLATE */

/* Your state (globals), built by setup outside the clock. */

/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

static int run(const std::string &q, std::string_view line, ub_span *m) {
    auto &re = cache[q];
    if (!re) {
        RE2::Options o;
        o.set_encoding(RE2::Options::EncodingLatin1);
        o.set_log_errors(false);
        re = std::make_unique<RE2>(q, o);
    }
    std::string_view g;
    if (!re->ok() || !re->Match(line, 0, line.size(), RE2::UNANCHORED, &g, 1)) return UB_N;
    m->s = g.data() - line.data();
    m->e = m->s + g.size();
    return UB_M;
}

/* ASSIST: one call. `line` is matched alone (offsets line-relative);
 * b.get("name") is the variable's value or nullopt when UNSET. Keep compiled
 * patterns in `cache`. */
/* BOILERPLATE shim */
static int vars(std::string_view line, const Binding &b, ub_span *m) {
/* END BOILERPLATE */
    auto t = b.get("tenant");
    if (!t) return UB_R;
    return run("^" + RE2::QuoteMeta(*t) + "-[0-9]{4} (?:ERROR|WARN) ", line, m);
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_vars(const unsigned char *l, size_t n, const ub_var *v, size_t nv, ub_span *m) { return vars(std::string_view((const char *)l, n), Binding{v, nv}, m); }
extern "C" void ub_reset(void) { cache.clear(); }
/* END BOILERPLATE */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
