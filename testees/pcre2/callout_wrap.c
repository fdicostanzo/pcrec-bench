/* [B148] L5 THE libpcre2 CALLOUT WRAPPER (docs/design/unusual_set_v1.md 3.2;
 * linked only into the callout driver, `pcre2_driver_co`, built with
 * -DPB_CALLOUTS). The FULL per-engine wrapper of the `pass` arm (M-2): the
 * view is built from the callout block -- subject, position, the attempt
 * start, every capture pair copied into ptrdiff_t form (PCRE2_UNSET -> -1) --
 * and the slot's callee is called through its pointer. Its own translation
 * unit, noinline + aligned(64) like every function on the timed path.
 *
 * THE RETURN-CODE MAPPING (pcre2callout(3) "RETURN VALUES FROM CALLOUTS"):
 * UB_CONTINUE -> 0; UB_FAIL -> +1 (backtrack: the next candidate). A NEGATIVE
 * value would ABANDON the whole match (-1 = PCRE2_ERROR_NOMATCH), so passing
 * the callee's -1 through would turn a first-candidate failure into a
 * no-match; tools/check_callouts.py's first-candidate-fails control is what
 * catches that. A CONSUME return has no libpcre2 meaning: such a site is
 * never bound here (the binding is pcrec's), and a stray one fails. */
#include <stddef.h>
#include <stdint.h>

#include "../common/ub_bind.h"

/* pcre2.h 10.46's pcre2_callout_block (verified against /usr/include/pcre2.h;
 * this driver dlopens the runtime and carries no header, testees/pcre2/
 * CLAUDE.md "Why dlopen"). Only version >= 0 fields are read. */
struct pb_callout_block {
    uint32_t version, callout_number, capture_top, capture_last;
    size_t *offset_vector;
    const unsigned char *mark, *subject;
    size_t subject_length, start_match, current_position,
           pattern_position, next_item_length;
};

#define PB_UNSET (~(size_t)0)

size_t pb_co_ncap = 1;       /* the pattern's group count + 1, set once */

__attribute__((noinline, aligned(64)))
int pb_pcre2_callout(struct pb_callout_block *cb, void *data) {
    (void)data;
    const struct ub_slot *s = &ub_slots[cb->callout_number & (UB_NSLOT - 1)];
    if (!s->fn) return 1;
    ptrdiff_t caps[UB_MAXCAP][2];
    size_t ncap = pb_co_ncap < UB_MAXCAP ? pb_co_ncap : UB_MAXCAP;
    caps[0][0] = (ptrdiff_t)cb->start_match;
    caps[0][1] = -1;
    for (size_t k = 1; k < ncap; k++) {
        size_t a = k < cb->capture_top ? cb->offset_vector[2 * k] : PB_UNSET;
        size_t b = k < cb->capture_top ? cb->offset_vector[2 * k + 1] : PB_UNSET;
        caps[k][0] = a == PB_UNSET ? -1 : (ptrdiff_t)a;
        caps[k][1] = b == PB_UNSET ? -1 : (ptrdiff_t)b;
    }
    struct ub_view v = { cb->subject, cb->subject_length, cb->current_position,
                         ncap, (const ptrdiff_t (*)[2])caps, s->user };
    long r = s->fn(&v);
    return r == UB_CONTINUE ? 0 : 1;
}
