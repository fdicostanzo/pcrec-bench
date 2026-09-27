/* SCRATCH measurement only (KB-29's TRE reachability question,
 * docs/dev/known_issues.md, lane b98kb29). An LD_PRELOAD malloc/calloc/
 * realloc interposer: with TRE_FAILMALLOC_VERBOSE=1 it counts every
 * allocation the process makes (one stderr line per call, "alloc #N"),
 * letting a caller bracket exactly which phase of a program (compile vs
 * exec call 1 vs exec call 2 ...) makes how many allocations. With
 * TRE_FAILMALLOC_AT=N set, it also FAILS (returns NULL) the Nth and every
 * later allocation -- real fault injection: the resulting REG_ESPACE (or
 * whatever error libtre reports) is libtre's own genuine reaction to a
 * genuine malloc() returning NULL, not a fabricated code path.
 *
 * Used here only to COUNT allocations inside testees/tre/driver.c's
 * find-all loop's tre_regnexecb() calls (see probe_kb29_tre_giveup_
 * reachability.c and its own archive for what that counting found).
 * Not part of any adapter or build; not linked by anything in testees/. */
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

static void *(*real_malloc)(size_t) = NULL;
static void *(*real_calloc)(size_t, size_t) = NULL;
static void *(*real_realloc)(void *, size_t) = NULL;
static long fail_at = -1;   /* -1 = never fail */
static long counter = 0;
static int in_init = 0;

static void init(void) {
    if (real_malloc) return;
    in_init = 1;
    real_malloc = dlsym(RTLD_NEXT, "malloc");
    real_calloc = dlsym(RTLD_NEXT, "calloc");
    real_realloc = dlsym(RTLD_NEXT, "realloc");
    const char *e = getenv("TRE_FAILMALLOC_AT");
    if (e && *e) fail_at = atol(e);
    in_init = 0;
}

static int should_fail(void) {
    counter++;
    if (getenv("TRE_FAILMALLOC_VERBOSE"))
        fprintf(stderr, "[failmalloc] alloc #%ld\n", counter);
    if (fail_at < 0) return 0;
    return counter >= fail_at;
}

void *malloc(size_t n) {
    if (!real_malloc) {
        if (in_init) {
            /* dlsym() itself may malloc() while we are resolving the real
             * symbols -- a tiny static bump allocator breaks the
             * recursion without ever calling a NULL real_malloc. */
            static char buf[65536];
            static size_t off = 0;
            if (off + n > sizeof buf) return NULL;
            void *p = buf + off;
            off += (n + 15) & ~15UL;
            return p;
        }
        init();
    }
    if (should_fail()) return NULL;
    return real_malloc(n);
}

void *calloc(size_t nm, size_t sz) {
    if (!real_calloc) { init(); if (!real_calloc) return NULL; }
    if (should_fail()) return NULL;
    return real_calloc(nm, sz);
}

void *realloc(void *p, size_t n) {
    if (!real_realloc) init();
    if (should_fail()) return NULL;
    return real_realloc(p, n);
}
