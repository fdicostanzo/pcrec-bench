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

/* ==== FAMILY recursion ==== */
/* Your state (globals), built by setup outside the clock. */

/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
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
    return UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */
/* ==== END FAMILY recursion ==== */

/* ==== FAMILY callouts ==== */
/* BOILERPLATE wrappers */
static bool pred(std::string_view s, size_t b, size_t c) { return ub_pred((const unsigned char *)s.data(), s.size(), b, c) != 0; }
/* END BOILERPLATE */

/* Your state (globals), built by setup outside the clock. */

/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
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
    return UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */
/* ==== END FAMILY callouts ==== */

/* ==== FAMILY netstr ==== */
/* Your state (globals), built by setup outside the clock. */

/* BOILERPLATE shim */
static int setup(std::string_view pattern) {
/* END BOILERPLATE */
    return 0;
/* BOILERPLATE shim */
}
/* END BOILERPLATE */

/* ASSIST: the first match at or after `start` in the whole subject `s`
 * (bytes before `start` stay visible). Fill m->s, m->e and group 1 in
 * m->g1s, m->g1e. */
/* BOILERPLATE shim */
static int find(std::string_view s, size_t start, ub_span *m) {
/* END BOILERPLATE */
    return UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_find(const unsigned char *s, size_t n, size_t start, ub_span *m) { return find(std::string_view((const char *)s, n), start, m); }
/* END BOILERPLATE */
/* ==== END FAMILY netstr ==== */

/* ==== FAMILY vars ==== */
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

/* ASSIST: one call. `line` is matched alone (offsets line-relative);
 * b.get("name") is the variable's value or nullopt when UNSET. Keep compiled
 * patterns in `cache`. */
/* BOILERPLATE shim */
static int vars(std::string_view line, const Binding &b, ub_span *m) {
/* END BOILERPLATE */
    return UB_N;
/* BOILERPLATE shim */
}
extern "C" int ub_setup(const unsigned char *p, size_t n, const char *) { return setup(std::string_view((const char *)p, n)); }
extern "C" int ub_vars(const unsigned char *l, size_t n, const ub_var *v, size_t nv, ub_span *m) { return vars(std::string_view((const char *)l, n), Binding{v, nv}, m); }
extern "C" void ub_reset(void) { cache.clear(); }
/* END BOILERPLATE */
/* ==== END FAMILY vars ==== */

/* BOILERPLATE main */
int main(int argc, char **argv) { return ub_main(argc, argv); }
/* END BOILERPLATE */
