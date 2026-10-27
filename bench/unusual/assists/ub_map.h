/* ub_map.h -- the ONE declared C hash-map helper of the assist budget
 * ([B148] unusual_set_v1.md 5.1/5.2): byte-string key -> void* value, open
 * addressing, FNV-1a, keys copied. Outside the token count (RULES.md); an
 * assist may include it and may not carry a hash map of its own.
 * Not thread-safe; values are owned by the caller. */
#ifndef UB_MAP_H
#define UB_MAP_H
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct { char *key; size_t len; uint64_t h; void *val; } ub_slot;
typedef struct { ub_slot *s; size_t cap, n; } ub_map;

static inline uint64_t ub_hash(const void *k, size_t len) {
    const unsigned char *p = (const unsigned char *)k;
    uint64_t h = 1469598103934665603ULL;
    for (size_t i = 0; i < len; i++) { h ^= p[i]; h *= 1099511628211ULL; }
    return h | 1; /* never 0: 0 marks an empty slot */
}
static inline void ub_map_init(ub_map *m) { m->s = NULL; m->cap = m->n = 0; }
static inline void *ub_map_get(const ub_map *m, const void *k, size_t len) {
    if (!m->cap) return NULL;
    uint64_t h = ub_hash(k, len);
    for (size_t i = h & (m->cap - 1); m->s[i].h; i = (i + 1) & (m->cap - 1))
        if (m->s[i].h == h && m->s[i].len == len && !memcmp(m->s[i].key, k, len))
            return m->s[i].val;
    return NULL;
}
static inline int ub_map_put(ub_map *m, const void *k, size_t len, void *val) {
    if ((m->n + 1) * 2 > m->cap) { /* grow at load 1/2 */
        size_t nc = m->cap ? m->cap * 2 : 16;
        ub_slot *ns = (ub_slot *)calloc(nc, sizeof *ns);
        if (!ns) return -1;
        for (size_t j = 0; j < m->cap; j++) if (m->s[j].h) {
            size_t i = m->s[j].h & (nc - 1);
            while (ns[i].h) i = (i + 1) & (nc - 1);
            ns[i] = m->s[j];
        }
        free(m->s); m->s = ns; m->cap = nc;
    }
    uint64_t h = ub_hash(k, len);
    size_t i = h & (m->cap - 1);
    for (; m->s[i].h; i = (i + 1) & (m->cap - 1))
        if (m->s[i].h == h && m->s[i].len == len && !memcmp(m->s[i].key, k, len)) {
            m->s[i].val = val; return 0;
        }
    char *kc = (char *)malloc(len ? len : 1);
    if (!kc) return -1;
    memcpy(kc, k, len);
    m->s[i].key = kc; m->s[i].len = len; m->s[i].h = h; m->s[i].val = val;
    m->n++;
    return 0;
}
/* visit every value (e.g. to free compiled regexes), then ub_map_free */
static inline void ub_map_each(const ub_map *m, void (*f)(void *val)) {
    for (size_t i = 0; i < m->cap; i++) if (m->s[i].h) f(m->s[i].val);
}
static inline void ub_map_free(ub_map *m) {
    for (size_t i = 0; i < m->cap; i++) if (m->s[i].h) free(m->s[i].key);
    free(m->s); ub_map_init(m);
}
#endif
