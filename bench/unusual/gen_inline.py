#!/usr/bin/env python3
"""gen_inline.py -- writes (or --check re-derives) the INLINE pcrec callout arm's
sources ([B148] lane b148inline; Frank 2026-10-29, plan.md [B148] "INLINE"):

    callees/ub_<callee>.rxt   one .rxt FRAGMENT per callee: a `pattern-esc` block
                              per pcrec-spelled callout arm that binds it, the
                              callee's C body inside the pattern as pcrec
                              [INLINE-C] stage 2's  (?C`c: ... `)  segment
    inline/<arm>.rxt          the ENTRY file of one arm: `include "<fragment>"
                              sha256 <hex64>` and nothing else (stage 3's pin)
    inline/blocks.tsv         which fragment line is which arm's pattern

    python3 -I bench/unusual/gen_inline.py            # write
    python3 -I bench/unusual/gen_inline.py --check    # re-derive + byte-diff

WHAT IS INLINED. The callee body is the text between the braces of
`long ub_<callee>(const struct ub_view *v) { ... }` in callees/callees.c,
BYTE FOR BYTE (tools/check_inline.py re-extracts it independently and compares).
A segment is a function BODY, so what a function definition would have outside
it is written as a PRELUDE inside the segment (no header, no `code-header` line:
pcrec's `--code-header` CLI path has an uninitialised field at cb32eda28, and
`--include-block` does not read the entry's `code-header` lines at all):

  * the macros / struct the body names: `UB_CONTINUE`, `UB_FAIL` (callees.h,
    verbatim lines), `UB_RETURN` (callees.c's non-counting definition, verbatim),
    `struct ub_view` (callees.h, verbatim), `struct ub_set` (callees.c, verbatim,
    member only);
  * the view the body reads, built from the segment's `ctx` (match_api 11.3);
  * a libc call a body makes (`memcmp`) is respelled to the compiler builtin
    by a one-line macro (no `<string.h>` needed);
  * the file-scope STATIC helpers of callees.c (`g1`, `fnv`, `g1_len`), which a
    function body cannot contain: SHIMS below, function-like macros over GNU
    statement expressions. These are the ONLY non-verbatim lines; the equivalence
    of shim and helper is what check_inline's differential run proves (gcc and
    clang, random views, every callee).

Pattern text comes from patterns/<arm>.rx and the sidecar's [callouts] tables:
the callout token `(?C<n>)` / `(?C"<name>,<attrs>")` is replaced by the segment
`(?C`c[,<attrs>]: <prelude><body>`)`. Only the pcrec arm is spelled inline; the
PCRE2-spelled pattern files are untouched. The member callee's runtime set
(ctx->user is NULL at a code site) arrives through `extern void *ub_inline_user`,
a data symbol the driver defines (part 2).
"""
import hashlib
import os
import re
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
CALLEES_C = os.path.join(HERE, "callees", "callees.c")
CALLEES_H = os.path.join(HERE, "callees", "callees.h")
FRAG_DIR = os.path.join(HERE, "callees")
ENTRY_DIR = os.path.join(HERE, "inline")
MANIFEST = os.path.join(ENTRY_DIR, "blocks.tsv")
SIDECAR = os.path.join(HERE, "subbench.toml")

TOOL = "bench/unusual/gen_inline.py"
DELIM = "`"

# sidecar callee name -> C function (callees.h). netstr-end is the ASSISTED
# check-at-end callee of co-netstr-assist, an engine-spelled pattern: not here.
CALLEE_FN = {"luhn": "ub_luhn", "isbn13": "ub_isbn13", "member": "ub_member",
             "netstr": "ub_netstr", "stub": "ub_stub"}

# file-scope static helpers of callees.c -> function-like-macro shims (the one
# non-verbatim part). Each shim is the same function as its helper, line by line.
SHIMS = {
    "g1": ("#define g1(v, pp, nn) ({ int ub_ok_ = 0; "
           "if (!((v)->ncap < 2 || (v)->caps[1][0] < 0 || (v)->caps[1][1] < (v)->caps[1][0])) "
           "{ *(pp) = (v)->subject + (v)->caps[1][0]; "
           "*(nn) = (size_t)((v)->caps[1][1] - (v)->caps[1][0]); ub_ok_ = 1; } ub_ok_; })"),
    "fnv": ("#define fnv(p, n) ({ size_t ub_h_ = (size_t)1469598103934665603ULL; "
            "for (size_t ub_i_ = 0; ub_i_ < (n); ub_i_++) "
            "{ ub_h_ ^= (p)[ub_i_]; ub_h_ *= (size_t)1099511628211ULL; } ub_h_; })"),
    "g1_len": ("#define g1_len(v) ({ const unsigned char *ub_gp_; size_t ub_gn_; long ub_gl_ = -1; "
               "if (g1(v, &ub_gp_, &ub_gn_) && ub_gn_ != 0 && ub_gn_ <= 9) "
               "{ ub_gl_ = 0; for (size_t ub_gk_ = 0; ub_gk_ < ub_gn_; ub_gk_++) "
               "ub_gl_ = ub_gl_ * 10 + (ub_gp_[ub_gk_] - '0'); } ub_gl_; })"),
}
# libc calls a body makes and a segment cannot declare (no header): the compiler's
# own builtin, same semantics, no declaration needed (gcc and clang both).
LIBC_BUILTINS = {"memcmp": "#define memcmp(a, b, n) __builtin_memcmp(a, b, n)"}
SHIM_DEPS = {"g1_len": ["g1"]}
SHIM_ORDER = ["g1", "g1_len", "fnv"]


def _lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def func_body(lines, fn):
    """The lines between `long <fn>(const struct ub_view *v) {` and the next
    line that is exactly `}`."""
    head = "long %s(const struct ub_view *v) {" % fn
    i = lines.index(head)
    j = lines.index("}", i)
    return lines[i + 1:j]


def block(lines, first, last):
    i = lines.index(first)
    j = lines.index(last, i)
    return lines[i:j + 1]


def define_line(lines, prefix):
    hits = [l for l in lines if l.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def non_counting_ub_return(c_lines):
    """callees.c's `#else` branch definition of UB_RETURN (the timed object's)."""
    i = c_lines.index("#else")
    return define_line(c_lines[i:], "#define UB_RETURN(")


def segment_text(callee):
    """-> the decoded C text that follows `c[,attrs]:` for CALLEE."""
    fn = CALLEE_FN[callee]
    c, h = _lines(CALLEES_C), _lines(CALLEES_H)
    body = func_body(c, fn)
    text_body = "\n".join(body)
    out = [""]
    out.append("/* %s: ub_inline prelude, then the body of %s from callees/callees.c, "
               "byte for byte */" % (TOOL, fn))
    out.append(define_line(h, "#define UB_CONTINUE"))
    out.append(define_line(h, "#define UB_FAIL"))
    out.append(non_counting_ub_return(c))
    out += block(h, "struct ub_view {", "};")
    if "ub_set" in text_body:
        out += block(c, "struct ub_set {", "};")
    used = [s for s in SHIM_ORDER
            if re.search(r"\b%s\(" % s, text_body)
            or any(s in SHIM_DEPS.get(u, []) for u in SHIM_ORDER if re.search(r"\b%s\(" % u, text_body))]
    for s in used:
        out.append(SHIMS[s])
    libc = [n for n in LIBC_BUILTINS if re.search(r"\b%s\(" % n, text_body)]
    for n in libc:
        out.append(LIBC_BUILTINS[n])
    user = "ub_inline_user" if "->user" in text_body else "ctx->user"
    if user == "ub_inline_user":
        out.append("extern void *ub_inline_user;")
    out.append("const struct ub_view ub_v_ = { ctx->subject, ctx->len, ctx->pos, "
               "ctx->ncap, ctx->caps, %s };" % user)
    out.append("const struct ub_view *v = &ub_v_;")
    out += body
    out.append("#undef UB_CONTINUE")
    out.append("#undef UB_FAIL")
    out.append("#undef UB_RETURN")
    for s in reversed(used):
        out.append("#undef %s" % s)
    for n in libc:
        out.append("#undef %s" % n)
    out.append("")
    text = "\n".join(out)
    assert DELIM not in text, "callee text contains the segment delimiter"
    return text


def esc(s):
    """pattern-esc's vocabulary (rxt_format 1.5 / 1.5.1): \\\" \\\\ \\n \\t \\r."""
    r = []
    for ch in s:
        if ch == "\\":
            r.append("\\\\")
        elif ch == '"':
            r.append('\\"')
        elif ch == "\n":
            r.append("\\n")
        elif ch == "\t":
            r.append("\\t")
        elif ch == "\r":
            r.append("\\r")
        elif ord(ch) < 0x20 or ord(ch) >= 0x7f:
            r.append("\\x%02x" % ord(ch) if ord(ch) < 0x100 else "?")
        else:
            r.append(ch)
    return "".join(r)


SITE = re.compile(r'\(\?C(?:(\d+)|"([^"]*)")\)')


def arms():
    """-> [(pattern, kind, callee, member_arg, attrs, pattern_text)], sorted by
    pattern id: every pcrec-spelled arm-real / arm-pass pattern with a site."""
    with open(SIDECAR, "rb") as f:
        sc = tomllib.load(f)
    spec = {}
    for kind in ("real", "pass"):
        for item in sc["callouts"][kind].split(","):
            key, val = item.split("=", 1)
            callee, _, arg = val.partition(":")
            spec[(kind, key)] = (callee, arg)
    out = []
    for p in sc["patterns"]:
        tags = set(p.get("tags", []))
        kind = ("real" if "arm-real" in tags else "pass" if "arm-pass" in tags else None)
        if kind is None or "spelling-assisted" in tags:
            continue
        with open(os.path.join(HERE, p["file"]), encoding="utf-8") as f:
            text = f.read()
        sites = SITE.findall(text)
        if len(sites) != 1:
            continue
        num, name = sites[0]
        key, _, attrs = (num or name).partition(",")
        callee, arg = spec[(kind, key)]
        out.append((p["name"], kind, callee, arg, attrs, text))
    return sorted(out)


def inline_pattern(text, callee, attrs):
    seg = "c%s:%s" % ("," + attrs if attrs else "", segment_text(callee))
    return SITE.sub(lambda m: "(?C%s%s%s)" % (DELIM, seg, DELIM), text, count=1)


def sha256_text(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def build():
    """-> {relative path: text} of everything this generator owns."""
    files = {}
    by_callee = {}
    for name, kind, callee, arg, attrs, text in arms():
        by_callee.setdefault(callee, []).append((name, kind, arg, attrs, text))
    manifest = []
    entries = {}
    for callee in sorted(by_callee):
        rel = "callees/ub_%s.rxt" % callee
        out = ["# %s -- the %s callee, INLINE (pcrec [INLINE-C] stage 2 segments)." % (rel, CALLEE_FN[callee]),
               "# GENERATED by %s from callees/callees.c; DO NOT EDIT (--check re-derives it)." % TOOL,
               "# A fragment: pattern blocks only. An entry file (inline/<arm>.rxt) includes it",
               "# with a sha256 pin and the harness compiles a block with --include-block."]
        for name, kind, arg, attrs, text in by_callee[callee]:
            out.append("# %s: the %s arm of %s; pattern text from patterns/%s.rx"
                       % ("block", kind, name, name))
            out.append('pattern-esc "%s"' % esc(inline_pattern(text, callee, attrs)))
            manifest.append((name, kind, callee, arg, rel, len(out)))
        frag_text = "\n".join(out) + "\n"
        files[rel] = frag_text
        frag_sha = sha256_text(frag_text)
        for name, kind, arg, attrs, text in by_callee[callee]:
            entries[name] = (rel, frag_sha)
    for name, (rel, frag_sha) in sorted(entries.items()):
        files["inline/%s.rxt" % name] = (
            "# inline/%s.rxt -- ENTRY file of the inline arm of %s (GENERATED by %s).\n"
            "# It builds nothing itself: the harness compiles the fragment's block with\n"
            "#   pcrec --allow-code=c --include-block %s:<line> inline/%s.rxt ...\n"
            "# The include is sha256-pinned (rxt_format 1.1.1): reached code compiles only\n"
            "# when every include line on the chain carries a pin.\n"
            'include "../%s" sha256 %s\n' % (name, name, TOOL, os.path.basename(rel), name, rel, frag_sha))
    rows = ["\t".join(("arm", "kind", "callee", "member_arg", "fragment", "line",
                       "entry", "fragment_sha256"))]
    for name, kind, callee, arg, rel, line in sorted(manifest):
        rows.append("\t".join((name, kind, callee, arg or "-", rel, str(line),
                               "inline/%s.rxt" % name, entries[name][1])))
    files["inline/blocks.tsv"] = "\n".join(rows) + "\n"
    return files


def main(argv):
    check = "--check" in argv
    files = build()
    diffs = 0
    os.makedirs(ENTRY_DIR, exist_ok=True)
    for rel, text in sorted(files.items()):
        path = os.path.join(HERE, rel)
        if check:
            have = open(path, encoding="utf-8").read() if os.path.exists(path) else None
            if have != text:
                diffs += 1
                print("DIFF  %s" % rel)
        else:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
    if check:
        print("gen_inline --check: %d file(s), %d difference(s)" % (len(files), diffs))
        return 1 if diffs else 0
    print("gen_inline: wrote %d file(s)" % len(files))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
