/* [B148] L5 THE ONIGURUMA CALLOUT WRAPPER (docs/design/unusual_set_v1.md 3.2;
 * linked only into the callout driver, `onig_driver_co`, built with
 * -DPB_CALLOUTS). Oniguruma 6.9.10 has no per-call match context: the
 * callout function is GLOBAL (`onig_set_progress_callout`), set once before
 * any timed call, and a `(?{N})` contents callout fires through it under
 * plain onig_search/onig_match (measured: docs/dev/lanes/b148l5_report.md,
 * "Onig witnesses"), so timed.c is untouched (BD16).
 *
 * The site number is the callout's CONTENTS (`(?{1})` -> "1"; the adapter
 * respells the set's `(?C1)` to `(?{1})`, recorded as `callout_respell`).
 * Oniguruma numbers its callouts itself (onig_get_callout_num_by_callout_args,
 * 1-based, in pattern order), so the contents are parsed ONCE per callout
 * number and cached; every later fire is a table read. The view: subject,
 * current position, the attempt start, every capture pair read with
 * onig_get_capture_range_in_callout (ONIG_REGION_NOTPOS -> -1).
 *
 * THE RETURN-CODE MAPPING (oniguruma.h): UB_CONTINUE -> ONIG_CALLOUT_SUCCESS
 * (0); UB_FAIL -> ONIG_CALLOUT_FAIL (1, backtrack: the next candidate). A
 * CONSUME return has no Oniguruma meaning: never bound here; a stray one
 * fails. */
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>

#include <oniguruma.h>

#include "../common/ub_bind.h"

int pb_co_ncap = 1;                  /* group count + 1, set once */
static const struct ub_slot *pb_by_num[64];

static const struct ub_slot *slot_for(OnigCalloutArgs *a) {
    int num = onig_get_callout_num_by_callout_args(a);
    if (num > 0 && num < 64 && pb_by_num[num]) return pb_by_num[num];
    const UChar *c = onig_get_contents_by_callout_args(a);
    const UChar *ce = onig_get_contents_end_by_callout_args(a);
    long k = 0;
    if (!c || c == ce) return NULL;
    for (; c < ce; c++) {
        if (*c < '0' || *c > '9') return NULL;
        k = k * 10 + (*c - '0');
        if (k >= UB_NSLOT) return NULL;
    }
    const struct ub_slot *s = &ub_slots[k];
    if (num > 0 && num < 64) pb_by_num[num] = s;
    return s;
}

__attribute__((noinline, aligned(64)))
int pb_onig_callout(OnigCalloutArgs *a, void *user) {
    (void)user;
    const struct ub_slot *s = slot_for(a);
    if (!s || !s->fn) return ONIG_CALLOUT_FAIL;
    const UChar *str = onig_get_string_by_callout_args(a);
    ptrdiff_t caps[UB_MAXCAP][2];
    int ncap = pb_co_ncap < UB_MAXCAP ? pb_co_ncap : UB_MAXCAP;
    caps[0][0] = onig_get_start_by_callout_args(a) - str;
    caps[0][1] = -1;
    for (int k = 1; k < ncap; k++) {
        int b = ONIG_REGION_NOTPOS, e = ONIG_REGION_NOTPOS;
        onig_get_capture_range_in_callout(a, k, &b, &e);
        caps[k][0] = b == ONIG_REGION_NOTPOS ? -1 : b;
        caps[k][1] = e == ONIG_REGION_NOTPOS ? -1 : e;
    }
    struct ub_view v = { str, (size_t)(onig_get_string_end_by_callout_args(a) - str),
                         (size_t)(onig_get_current_by_callout_args(a) - str),
                         (size_t)ncap, (const ptrdiff_t (*)[2])caps, s->user };
    long r = s->fn(&v);
    return r == UB_CONTINUE ? ONIG_CALLOUT_SUCCESS : ONIG_CALLOUT_FAIL;
}
