// [B140] The SUBSTITUTION timed call's interface (see timed_subst.cc).
#ifndef RE2_TIMED_SUBST_H
#define RE2_TIMED_SUBST_H

#include <re2/re2.h>

#include <string>

struct tsubst_in {
    std::string *text;            // a FRESH COPY of the subject, made untimed;
                                  // GlobalReplace edits it in place
    const RE2 *re;
    absl::string_view rewrite;    // the template, RE2's dialect (`\1`)
};

struct tsubst_out {
    volatile int nsubst;          // GlobalReplace's return: replacements made
};

// Runs the timed substitution for one subject; returns the elapsed seconds.
double timed_subst(const struct tsubst_in *in, struct tsubst_out *out);

#endif
