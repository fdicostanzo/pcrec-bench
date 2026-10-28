/* [B148] L4 THE DEEP ARM's match call for the EXISTING instrument (docs/
 * design/unusual_set_v1.md 6.1-6.2). timed.c (BD16, untouched) calls
 * `in->match(code, buf, len, pos, opts, md, NULL)` through a function
 * pointer and passes NULL as the match context -- the library's defaults,
 * which IS the `default` arm. The `deep` arm needs a match context (the
 * raised match/depth limits, the 1 GiB heap limit, the assigned 1 GiB JIT
 * stack), so its driver hands timed.c THIS function as `match` instead: it
 * forwards every argument unchanged and substitutes the deep arm's context
 * for the NULL. One extra direct call per match, on the deep arm only; the
 * default arm's code path and object bytes are exactly what they were. Its
 * own translation unit, noinline + aligned(64), like every timed function. */
#include <stddef.h>
#include <stdint.h>

void *timed_ctx_mctx;   /* set ONCE by driver.c before any timed call */
int (*timed_ctx_match)(void *, const unsigned char *, size_t, size_t,
                       uint32_t, void *, void *);

__attribute__((noinline, aligned(64)))
int timed_ctx_forward(void *code, const unsigned char *buf, size_t len,
                      size_t pos, uint32_t opts, void *md, void *mctx_ignored) {
    (void)mctx_ignored;
    return timed_ctx_match(code, buf, len, pos, opts, md, timed_ctx_mctx);
}
