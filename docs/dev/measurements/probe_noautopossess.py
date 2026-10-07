# Archived 2026-10-07 (forty-fifth session) from the session scratchpad; run from the repo root.
"""K93 / (?R) ruling probe: libpcre2 default vs PCRE2_NO_AUTO_POSSESS on the
bench's 12 subroutine-call patterns x every expectation row (pattern, subject,
regime). Same calls as the sets' gen_expectations.py (match/search/find_all).
Reports ANSWER flips (match/nomatch, span, nmatches) and CAPTURE-only diffs."""
import sys, time
sys.path.insert(0, ".")
from pcrecbench import subbench, oracle_pcre2 as o
NAP = 0x00004000  # PCRE2_NO_AUTO_POSSESS (pcre2.h; 0x2000 is NO_AUTO_CAPTURE)
PATS = {"capability": ["balanced-parens-rec", "nested-comment-rec", "bracket-array-define"],
        "syntax": ["rec-1", "rec-name", "rec-r-uc", "rec-back", "rec-fwd", "rec-define",
                   "rec-g-angle", "rec-py"],
        "email": ["factored"]}
print("libpcre2", o.version())
rows = flips = capd = errs = 0
for st, names in PATS.items():
    sb = subbench.find(st)
    for name in names:
        pb = sb.pattern_bytes(name)
        a, b = o.compile(pb, 0), o.compile(pb, NAP)
        assert o._info_u32(b, 1) & NAP and not o._info_u32(a, 1) & NAP, name  # ARGOPTIONS control
        for e in sb.expectations.values():
            if e.pattern != name:
                continue
            body = sb.subject_bytes(e.subject)
            res = []
            for rx in (a, b):
                try:
                    if e.regime == "match": r = rx.match(body, 0)
                    elif e.regime == "search_short": r = rx.search(body, 0)
                    else: r = rx.find_all(body)
                except o.Pcre2Error as x:
                    r = ("ERROR", str(x))
                res.append(r)
            rows += 1
            ra, rb = res
            def ans(r):
                if r is None or (isinstance(r, tuple) and r and r[0] == "ERROR"): return r
                if e.regime == "throughput": return r
                return r[0]
            if ra == rb: continue
            if isinstance(ra, tuple) and ra and ra[0] == "ERROR" or isinstance(rb, tuple) and rb and rb[0] == "ERROR":
                errs += 1; tag = "ERROR"
            elif ans(ra) != ans(rb): flips += 1; tag = "FLIP"
            else: capd += 1; tag = "CAPTURES-ONLY"
            print("%s\t%s\t%s\t%s\t%s\tdefault=%r\tno_auto_possess=%r\texpected=%s"
                  % (tag, st, name, e.subject, e.regime, ra, rb, e.expected))
print("rows %d  answer-flips %d  capture-only %d  errors %d" % (rows, flips, capd, errs))
