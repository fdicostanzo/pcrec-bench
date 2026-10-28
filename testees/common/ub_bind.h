/* testees/common/ub_bind.h -- the callout BINDING table every native-callout
 * driver shares ([B148] L5, docs/design/unusual_set_v1.md 3.2 + 7.3).
 *
 * A binding SPEC binds a callout site to one shared callee
 * (bench/unusual/callees/callees.h) and its user data:
 *
 *     1=luhn,2=isbn13,3=member:/abs/path/users.tsv,4=netstr-end,netstr=netstr
 *
 * keys are a site NUMBER (0-255: `(?CN)`, Onig's `(?{N})`) or a NAME (pcrec's
 * `(?C"name,...")`); callees `luhn`, `isbn13`, `member:<file>`, `netstr`
 * (pcrec consume), `netstr-end` (the assisted check-at-end) and `stub` (the
 * `pass` arm). Parsed ONCE, before any timed call; the member set is built
 * then too. A wrapper reads a slot and calls `slot->fn(&view)`: the same
 * indirect call on every engine. */
#ifndef UB_BIND_H
#define UB_BIND_H

#include "../../bench/unusual/callees/callees.h"

struct ub_slot {
    ub_fn *fn;          /* NULL = unbound */
    void *user;
    const char *callee; /* the spec's callee name, for messages */
};

#define UB_NSLOT 256
#define UB_NNAMED 8

extern struct ub_slot ub_slots[UB_NSLOT];
struct ub_named_slot { char name[32]; struct ub_slot slot; };
extern struct ub_named_slot ub_named[UB_NNAMED];
extern int ub_nnamed;

/* -> 0, or -1 with a message in err (an unknown callee, an unreadable member
 * file, a bad key). */
int ub_bind_parse(const char *spec, char *err, size_t errn);

/* the slot bound to a name, or NULL */
const struct ub_slot *ub_slot_named(const char *name, size_t n);

#endif
