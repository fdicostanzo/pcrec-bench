/* testees/common/ub_bind.c -- the binding-spec parser (ub_bind.h). Binding
 * glue, compiled with each callout driver (and into pcrec's callout .so);
 * runs before any timed call. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "ub_bind.h"

struct ub_slot ub_slots[UB_NSLOT];
struct ub_named_slot ub_named[UB_NNAMED];
int ub_nnamed;

static int callee_of(const char *name, size_t n, struct ub_slot *out,
                     char *err, size_t errn) {
    static const struct { const char *name; ub_fn *fn; } tab[] = {
        {"luhn", ub_luhn}, {"isbn13", ub_isbn13}, {"netstr", ub_netstr},
        {"netstr-end", ub_netstr_end}, {"stub", ub_stub},
    };
    for (size_t i = 0; i < sizeof tab / sizeof tab[0]; i++)
        if (strlen(tab[i].name) == n && !memcmp(tab[i].name, name, n)) {
            out->fn = tab[i].fn;
            out->user = NULL;
            out->callee = tab[i].name;
            return 0;
        }
    if (n > 7 && !memcmp(name, "member:", 7)) {
        char path[4096];
        if (n - 7 >= sizeof path) { snprintf(err, errn, "member path too long"); return -1; }
        memcpy(path, name + 7, n - 7);
        path[n - 7] = 0;
        out->fn = ub_member;
        out->user = ub_member_new(path);
        out->callee = "member";
        if (!out->user) { snprintf(err, errn, "cannot read the member set %s", path); return -1; }
        return 0;
    }
    snprintf(err, errn, "unknown callee %.*s (luhn isbn13 member:<file> netstr netstr-end stub)",
             (int)n, name);
    return -1;
}

int ub_bind_parse(const char *spec, char *err, size_t errn) {
    const char *p = spec;
    while (*p) {
        const char *end = strchr(p, ',');
        if (!end) end = p + strlen(p);
        const char *eq = memchr(p, '=', (size_t)(end - p));
        if (!eq || eq == p) { snprintf(err, errn, "binding %.*s has no KEY=CALLEE", (int)(end - p), p); return -1; }
        struct ub_slot s;
        if (callee_of(eq + 1, (size_t)(end - eq - 1), &s, err, errn)) return -1;
        size_t kn = (size_t)(eq - p);
        if (p[0] >= '0' && p[0] <= '9') {
            char *q;
            long k = strtol(p, &q, 10);
            if (q != eq || k < 0 || k >= UB_NSLOT) { snprintf(err, errn, "bad site number %.*s", (int)kn, p); return -1; }
            ub_slots[k] = s;
        } else {
            if (ub_nnamed == UB_NNAMED || kn >= sizeof ub_named[0].name) { snprintf(err, errn, "too many / too long names"); return -1; }
            memcpy(ub_named[ub_nnamed].name, p, kn);
            ub_named[ub_nnamed].name[kn] = 0;
            ub_named[ub_nnamed++].slot = s;
        }
        p = *end ? end + 1 : end;
    }
    return 0;
}

const struct ub_slot *ub_slot_named(const char *name, size_t n) {
    for (int i = 0; i < ub_nnamed; i++)
        if (strlen(ub_named[i].name) == n && !memcmp(ub_named[i].name, name, n))
            return &ub_named[i].slot;
    return NULL;
}
