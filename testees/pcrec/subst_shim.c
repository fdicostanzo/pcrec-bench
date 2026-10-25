/* testees/pcrec/subst_shim.c -- the SUBSTITUTION artifact's flat surface
 * ([B140], docs/design/subst_bench_v1.md 3.1; contract docs/spec/subst_api.md).
 *
 * A second translation unit of the SAME .so shim.c builds, only for a
 * substitution cell: shim.c (unchanged) still #includes the rx artifact and
 * exports the `pb_*` matching surface the driver reads its `info` lines from;
 * this file adds ONE exported function, `pb_subst_all`, plus two provenance
 * getters. It includes
 *
 *   PB_SUPPORT          the support unit (`pcrec --emit-support`), PRIVATE to
 *                       this translation unit (PCREC_SUPPORT_STATIC, contract
 *                       10 para 3a): no external names, no link clash with
 *                       anything else in the .so;
 *   PB_RX_HEADER        the rx artifact's header, for `extern rx_info` (the
 *                       definition is shim.c's TU, via the artifact .c);
 *   PB_SUBST_ARTIFACT   the subst artifact's .c (`pcrec -p sub --subst-file`).
 *
 * `pb_subst_all` is the contract's own sub_all() (subst_api.md 6.9) verbatim
 * in shape: the code a user writes ONCE to substitute with any rx and any
 * template. It is what testees/pcrec/timed_subst.c times, so the iterator
 * init, the context setup (and its check) and the replace-all call are all
 * inside the clock, exactly as for a user.
 *
 * SCRATCH. A case-forcing template (`\U$1\E`) writes its case region into a
 * caller-supplied scratch (4 para 22). The scratch here is a static 64 KiB:
 * a batch is at most 64 matches and a region is the template's constant
 * bytes plus ONE group, so this bench's longest region (case 6: "/downloads/")
 * is ~11 bytes x 64. Should a region ever outgrow it the call returns
 * PCREC_SUBST_NOSPACE with o.sneed > o.scap (10 para 8) -- the driver reports
 * it by name as a failure, never silently. The static buffer makes this
 * function non-reentrant, which the single-threaded driver does not need.
 */
#include <stddef.h>
#include <stdint.h>
#include <limits.h>

#define PCREC_SUPPORT_STATIC
#include PB_SUPPORT
#include PB_RX_HEADER
#include PB_SUBST_ARTIFACT

#define PB_SUBST_BATCH 64
#define PB_SUBST_SCRATCH (64u * 1024u)

static unsigned char pb_subst_scratch[PB_SUBST_SCRATCH];

/* -> the number of matches substituted (>= 0) with *len the output length, or
 * a negative code; out == NULL && cap == 0 only sizes (10 para 7). */
int pb_subst_all(const unsigned char *s, size_t n, unsigned char *out,
                 size_t cap, size_t *len)
{
    const struct pcrec_subst_info *t = &sub_subst_info;
    rx_iter it = RX_ITER_INIT(s, n);
    rx_var vres[SUB_NVREFS];
    pcrec_subst_piece pc[PB_SUBST_BATCH * SUB_PIECES];
    pcrec_subst_out o = { .pc = pc, .cap = PB_SUBST_BATCH * SUB_PIECES,
                          .scratch = pb_subst_scratch,
                          .scap = sizeof pb_subst_scratch };
    rx_ctx ctx;
    int bad, rc = pcrec_subst_ctx_init(&ctx, &it, &rx_info, t, NULL, vres, 0, &bad);
    if (rc < 0) return rc;
    return pcrec_subst_replace_all(rx_info.next_n, &it, t, &ctx, NULL, 0, &o,
                                   out, cap, len);
}

/* provenance for the driver's `info` lines */
const char *pb_subst_modules(void)
{
#ifdef SUB_SUBST_MODULES
    return SUB_SUBST_MODULES;
#else
    return "";
#endif
}
int pb_subst_uses_scratch(void)
{
    return (sub_subst_info.uses & PCREC_SUBST_USES_SCRATCH) != 0;
}
