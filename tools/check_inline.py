#!/usr/bin/env python3
"""check_inline.py -- `make check-unusual`'s slice for the INLINE pcrec callout
arm's sources ([B148] lane b148inline; bench/unusual/gen_inline.py).

Called from tools/check_unusual.py as `check_inline.run(ok, bad)`; standalone:
`python3 -I tools/check_inline.py`. It needs NO pcrec build (and no pcrec
binary): everything is the committed files, hashlib, and -- for the last
section -- the box's own C compiler on a hand-written stand-in for pcrec's
`rx_ctx` / segment wrapper. A SMOKE: no timing, scratch under TMP_ROOT.

Each section carries a control that shares no source with what it controls
(the decoder, the body extraction and the pin check below are written HERE and
import nothing from gen_inline.py except to run its own `--check`):

  1. gen_inline.py --check: the generator re-derives all 13 files byte for byte.
  2. BYTE IDENTITY: every fragment block's decoded segment contains the callee
     body of callees/callees.c (re-extracted here by a brace scanner, not the
     generator's line search) byte for byte, between the prelude and the
     `#undef` tail. CONTROL: one flipped byte in the segment, and one in the
     callees.c copy, are each reported as a mismatch.
  3. VERBATIM PRELUDE: every prelude line that is not a declared shim is a line
     of callees.h / callees.c. Only the three helper shims (g1, fnv, g1_len)
     are written by the generator; section 6 proves them equivalent.
  4. PINS: every `include` line of every entry carries `sha256 <hex64>`, the
     digest recomputed from the file's bytes equals it, and a fragment holds
     nothing but comments, blank lines and `pattern-esc` blocks (so the
     every-chain rule has a one-edge chain). CONTROLS: a stale pin (one byte of
     the fragment changed), a pin with one hex digit flipped and an unpinned
     include are each refused BY NAME.
  5. PATTERN FIDELITY: each block's pattern, with its segment folded back to the
     original callout token, is the committed patterns/<arm>.rx byte for byte
     (the PCRE2-spelled files are untouched); the tag is `c` / `c,consume`
     as the site's attributes say; no `#include` and no `code-header` anywhere
     (the segments need no header); blocks.tsv points at pattern-esc lines.
  6. BEHAVIOUR (cc, gcc and clang when present): each segment, wrapped as pcrec
     wraps it (`static ptrdiff_t f(const rx_ctx *ctx) { TEXT }`), is compiled
     -Wall -Wextra and run against the callees.c function on random views
     (valid, unset, inverted, out-of-range-of-pos spans), the returns compared.
     CONTROL: a segment with one operator flipped is caught as a divergence.
     Not a substitute for pcrec's own compile of the block (part 2).
"""
import hashlib
import os
import random
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

UNUSUAL = os.path.join(ROOT, "bench", "unusual")
CALLEES = os.path.join(UNUSUAL, "callees")
INLINE = os.path.join(UNUSUAL, "inline")
GEN = os.path.join(UNUSUAL, "gen_inline.py")

FN = {"luhn": "ub_luhn", "isbn13": "ub_isbn13", "member": "ub_member",
      "netstr": "ub_netstr", "stub": "ub_stub"}
SHIM_RE = re.compile(r"^#define (g1|fnv|g1_len)\(")
LIBC_RE = re.compile(r"^#define memcmp\(a, b, n\) __builtin_memcmp\(a, b, n\)$")
PRELUDE_END = "const struct ub_view *v = &ub_v_;"
TAIL = "\n#undef UB_CONTINUE"
SEG_RE = re.compile(r"\(\?C`(c(?:,[a-z]+)?):(.*)`\)", re.S)


def read(path, mode="r"):
    with open(path, mode, **({} if "b" in mode else {"encoding": "utf-8"})) as f:
        return f.read()


# ---- independent helpers -------------------------------------------------

def decode_esc(q):
    """Decode the body of a pattern-esc "..." operand (rxt_format 1.5 / 1.5.1)."""
    out, i = [], 0
    table = {"\\": "\\", '"': '"', "n": "\n", "t": "\t", "r": "\r", "f": "\f", "v": "\v"}
    while i < len(q):
        ch = q[i]
        if ch != "\\":
            out.append(ch)
            i += 1
            continue
        nx = q[i + 1]
        if nx == "x":
            out.append(chr(int(q[i + 2:i + 4], 16)))
            i += 4
        else:
            out.append(table[nx])
            i += 2
    return "".join(out)


def fragment_blocks(text):
    """-> [(line_no, decoded pattern)] of the `pattern-esc` lines; raises on any
    line that is not a comment, blank, or a pattern-esc line."""
    blocks = []
    for n, line in enumerate(text.split("\n"), 1):
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r'pattern-esc "(.*)"', line)
        if not m:
            raise ValueError("fragment line %d is not a comment or a pattern-esc block: %.60r" % (n, line))
        blocks.append((n, decode_esc(m.group(1))))
    return blocks


def extract_body(c_text, fn):
    """The text between the braces of `long fn(const struct ub_view *v) {`,
    without the newline after `{` and the newline before `}` (a brace scanner
    that skips string / char literals and both comment kinds)."""
    head = "long %s(const struct ub_view *v) {" % fn
    i = c_text.index(head) + len(head)
    depth, j, n = 1, i, len(c_text)
    while depth:
        ch = c_text[j]
        if ch in "\"'":
            q = ch
            j += 1
            while c_text[j] != q:
                j += 2 if c_text[j] == "\\" else 1
        elif c_text.startswith("/*", j):
            j = c_text.index("*/", j) + 1
        elif c_text.startswith("//", j):
            j = c_text.index("\n", j)
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        j += 1
        assert j <= n
    return c_text[i + 1:j - 2]       # drop "\n" after '{' and "\n}" at the end


def body_identical(segment, body):
    """The decoded segment holds BODY immediately after the prelude marker and
    immediately before the #undef tail, byte for byte."""
    k = segment.find(PRELUDE_END + "\n")
    if k < 0:
        return False
    rest = segment[k + len(PRELUDE_END) + 1:]
    return rest.startswith(body + TAIL)


def flip(s, k):
    return s[:k] + chr(ord(s[k]) ^ 1) + s[k + 1:]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def verify_entry(entry_text, entry_dir, read_bytes):
    """-> list of problems (strings) of an entry file's include lines."""
    probs = []
    seen = 0
    for n, line in enumerate(entry_text.split("\n"), 1):
        if not line or line.startswith("#"):
            continue
        m = re.fullmatch(r'include "([^"]+)"(?: sha256 ([0-9a-fA-F]{64}))?', line)
        if not m:
            probs.append("line %d: not an include line: %.50r" % (n, line))
            continue
        seen += 1
        path, pin = m.groups()
        if pin is None:
            probs.append("line %d: include \"%s\" carries no sha256 pin" % (n, path))
            continue
        have = sha(read_bytes(os.path.normpath(os.path.join(entry_dir, path))))
        if have.lower() != pin.lower():
            probs.append("line %d: include \"%s\" sha256 pin mismatch (file hashes to %s)" % (n, path, have))
    if not seen:
        probs.append("no include line")
    return probs


# ---- the sections --------------------------------------------------------

def _arms():
    rows = [l.rstrip("\n").split("\t") for l in read(os.path.join(INLINE, "blocks.tsv")).splitlines()]
    hdr = rows[0]
    return [dict(zip(hdr, r)) for r in rows[1:]]


def section_generator(ok, bad):
    p = subprocess.run(["/usr/bin/gnutimeout", "120", sys.executable, "-I", GEN, "--check"],
                       capture_output=True, text=True)
    last = (p.stdout.strip().splitlines() or ["(no output)"])[-1]
    if p.returncode == 0:
        ok("gen_inline.py --check re-derives every file", last)
    else:
        bad("gen_inline.py --check", "rc=%d %s %s" % (p.returncode, last, p.stderr[-200:]))


def _segments():
    """-> [(arm row, pattern text, tag, segment text)] for every manifest row."""
    out = []
    frag_cache = {}
    for r in _arms():
        if r["fragment"] not in frag_cache:
            frag_cache[r["fragment"]] = dict(fragment_blocks(read(os.path.join(UNUSUAL, r["fragment"]))))
        pat = frag_cache[r["fragment"]][int(r["line"])]
        m = SEG_RE.search(pat)
        out.append((r, pat, m.group(1), m.group(2)))
    return out


def section_identity(ok, bad):
    c_text = read(os.path.join(CALLEES, "callees.c"))
    segs = _segments()
    n_ok = 0
    for r, pat, tag, seg in segs:
        body = extract_body(c_text, FN[r["callee"]])
        if body_identical(seg, body):
            n_ok += 1
        else:
            bad("byte identity: %s body of %s" % (r["arm"], FN[r["callee"]]), "differs from callees/callees.c")
    if n_ok == len(segs):
        ok("byte identity: every inlined body == its callees.c body", "%d blocks" % len(segs))
    # CONTROLS: one byte flipped in the segment / in the callees.c copy
    r, pat, tag, seg = next(x for x in segs if x[0]["callee"] == "luhn")
    body = extract_body(c_text, FN[r["callee"]])
    k = seg.find(PRELUDE_END) + len(PRELUDE_END) + 1 + body.index("t % 10")
    if not body_identical(flip(seg, k), body):
        ok("control: one flipped byte in the inlined body is a mismatch")
    else:
        bad("control: one flipped byte in the inlined body is a mismatch", "not detected")
    c2 = flip(c_text, c_text.index("t % 10 == 0 ? UB_CONTINUE"))
    if not body_identical(seg, extract_body(c2, FN[r["callee"]])):
        ok("control: one flipped byte in callees.c is a mismatch")
    else:
        bad("control: one flipped byte in callees.c is a mismatch", "not detected")
    if body_identical(seg, body):
        ok("control: the unmutated pair is identical (the predicate passes)")


def section_prelude(ok, bad):
    lines = set(read(os.path.join(CALLEES, "callees.h")).split("\n")) | \
        set(read(os.path.join(CALLEES, "callees.c")).split("\n"))
    odd, shims = [], set()
    for r, pat, tag, seg in _segments():
        pre = seg[:seg.index("const struct ub_view ub_v_ = {")].split("\n")
        for l in pre:
            if not l or l.startswith("/* bench/unusual/gen_inline.py"):
                continue
            if LIBC_RE.match(l):
                shims.add("memcmp->builtin")
            elif SHIM_RE.match(l):
                shims.add(SHIM_RE.match(l).group(1))
            elif l not in lines and l != "extern void *ub_inline_user;":
                odd.append((r["arm"], l[:50]))
    if not odd:
        ok("prelude: every non-shim line is verbatim from callees.h / callees.c",
           "shims: %s" % ", ".join(sorted(shims)))
    else:
        bad("prelude: every non-shim line is verbatim", repr(odd[:3]))


def section_pins(ok, bad):
    entries = sorted(f for f in os.listdir(INLINE) if f.endswith(".rxt"))
    allprobs = []
    for f in entries:
        text = read(os.path.join(INLINE, f))
        allprobs += ["%s: %s" % (f, p) for p in verify_entry(text, INLINE, lambda p: read(p, "rb"))]
    if not allprobs and entries:
        ok("pins: every include is sha256-pinned and the digest recomputes", "%d entries" % len(entries))
    else:
        bad("pins: every include is sha256-pinned and recomputes", "; ".join(allprobs)[:300])
    # every fragment holds only comments + pattern-esc blocks (no include/lib: a
    # one-edge chain; a head line in a fragment is a parse error in pcrec)
    frags = sorted(f for f in os.listdir(CALLEES) if f.endswith(".rxt"))
    try:
        for f in frags:
            fragment_blocks(read(os.path.join(CALLEES, f)))
        ok("pins: fragments hold only comments and pattern-esc blocks", "%d fragments" % len(frags))
    except ValueError as e:
        bad("pins: fragments hold only comments and pattern-esc blocks", str(e))
    # CONTROLS
    f0 = entries[0]
    text = read(os.path.join(INLINE, f0))
    fragpath = os.path.normpath(os.path.join(INLINE, re.search(r'include "([^"]+)"', text).group(1)))
    real = read(fragpath, "rb")
    stale = verify_entry(text, INLINE, lambda p: flip(real.decode("latin-1"), 40).encode("latin-1"))
    if any("pin mismatch" in p for p in stale):
        ok("control: a stale pin (one byte of the fragment changed) is refused BY NAME", stale[0][:70])
    else:
        bad("control: a stale pin is refused BY NAME", repr(stale))
    pin = re.search(r"sha256 ([0-9a-f]{64})", text).group(1)
    badpin = text.replace(pin, ("0" if pin[0] != "0" else "1") + pin[1:])
    flipped = verify_entry(badpin, INLINE, lambda p: real)
    if any("pin mismatch" in p for p in flipped):
        ok("control: a pin with one hex digit changed is refused BY NAME")
    else:
        bad("control: a pin with one hex digit changed is refused", repr(flipped))
    unpinned = verify_entry(text.replace(" sha256 " + pin, ""), INLINE, lambda p: real)
    if any("no sha256 pin" in p for p in unpinned):
        ok("control: an unpinned include is refused BY NAME", unpinned[0][:70])
    else:
        bad("control: an unpinned include is refused", repr(unpinned))
    if not verify_entry(text, INLINE, lambda p: real):
        ok("control: the unmutated entry raises no problem")


def section_fidelity(ok, bad):
    import tomllib
    bad_arms = []
    for r, pat, tag, seg in _segments():
        rx = read(os.path.join(UNUSUAL, "patterns", r["arm"] + ".rx"))
        site = re.search(r'\(\?C(?:(\d+)|"([^"]*)")\)', rx)
        want_attr = (site.group(2) or "").partition(",")[2]
        want_tag = "c" + ("," + want_attr if want_attr else "")
        m = SEG_RE.search(pat)
        folded = pat[:m.start()] + site.group(0) + pat[m.end():]
        if folded != rx or tag != want_tag or pat.count("(?C`") != 1:
            bad_arms.append(r["arm"])
    if not bad_arms:
        ok("fidelity: each block == patterns/<arm>.rx with the segment folded back",
           "tags c / c,consume as the sites say")
    else:
        bad("fidelity: block vs patterns/<arm>.rx", repr(bad_arms))
    hdr = [(r["arm"], seg[:40]) for r, pat, tag, seg in _segments() if "#include" in seg]
    heads = [f for f in os.listdir(INLINE) + os.listdir(CALLEES)
             if f.endswith(".rxt") and "code-header" in read(os.path.join(INLINE if f in os.listdir(INLINE) else CALLEES, f))]
    if not hdr and not heads:
        ok("no header: no segment `#include`s and no file names a `code-header`")
    else:
        bad("no header", repr((hdr, heads)))
    # blocks.tsv points at pattern-esc lines whose entry pins the same digest
    wrong = []
    for r in _arms():
        lines = read(os.path.join(UNUSUAL, r["fragment"])).split("\n")
        ent = read(os.path.join(UNUSUAL, r["entry"]))
        digest = sha(read(os.path.join(UNUSUAL, r["fragment"]), "rb"))
        if not lines[int(r["line"]) - 1].startswith('pattern-esc "') or digest != r["fragment_sha256"] \
                or ("sha256 " + digest) not in ent:
            wrong.append(r["arm"])
    if not wrong:
        ok("blocks.tsv: line, fragment digest and entry pin agree", "%d arms" % len(_arms()))
    else:
        bad("blocks.tsv agrees with the files", repr(wrong))
    longest = max(len(pat.encode()) for _r, pat, _t, _s in _segments())
    ok("size: longest decoded pattern", "%d bytes" % longest)
    # the sidecar's real/pass specs still bind the callees this set inlines
    with open(os.path.join(UNUSUAL, "subbench.toml"), "rb") as f:
        sc = tomllib.load(f)
    named = {i.split("=", 1)[1].partition(":")[0] for k in ("real", "pass") for i in sc["callouts"][k].split(",")}
    missing = {r["callee"] for r in _arms()} - named
    if not missing:
        ok("sidecar [callouts] binds every inlined callee", ", ".join(sorted({r["callee"] for r in _arms()})))
    else:
        bad("sidecar [callouts] binds every inlined callee", repr(missing))


STUB_H = r"""
#include <stddef.h>
#include <stdint.h>
typedef struct rx_var { const char *name; const unsigned char *p; size_t len; } rx_var;
typedef struct rx_ctx {
    const unsigned char *subject; size_t len; size_t pos; size_t ncap;
    const ptrdiff_t (*caps)[2]; void *user; const rx_var *vars; size_t nvars;
} rx_ctx;
"""

DRIVER_C = r"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "callees.h"
#include "seg_decls.h"
void *ub_inline_user;
static unsigned long long st;
static unsigned long long rnd(void) { st += 0x9E3779B97F4A7C15ULL; unsigned long long z = st;
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31); }
static const char *ALPHA[] = { "0123456789", "0123456789:,", "abcdefghij=_ 0123456789" };
int main(int argc, char **argv) {
    const char *users = argv[1];
    (void)argc;
    void *set = ub_member_new(users);
    if (!set) { fprintf(stderr, "no member set\n"); return 2; }
    ub_inline_user = set;
    long bad = 0, total = 0, nonzero = 0;
    for (int fi = 0; fi < NFN; fi++) {
        for (int it = 0; it < 60000; it++) {
            unsigned char sub[64];
            size_t len = rnd() % 40;
            const char *al = ALPHA[(fi == 3 || fi == 4) ? 1 : (fi == 2 ? 2 : 0)];
            size_t nal = strlen(al);
            for (size_t k = 0; k < len; k++) sub[k] = (unsigned char)al[rnd() % nal];
            if (fi == 2 && (rnd() & 1) && len >= 4) {          /* a known member name */
                static const char *names[] = { "alice", "bob", "carol", "dave", "root" };
                const char *nm = names[rnd() % 5]; size_t l = strlen(nm); if (l > len) l = len; memcpy(sub, nm, l);
            }
            if (fi == 0 && len >= 14 && (rnd() % 3 == 0)) {     /* a Luhn-valid number */
                for (size_t k = 0; k < len; k++) sub[k] = (unsigned char)('0' + rnd() % 10);
                unsigned t = 0; for (size_t k = 0; k + 1 < len; k++) { unsigned d = sub[len-1-(k+1)] - '0'; if (!(k & 1)) { d *= 2; if (d > 9) d -= 9; } t += d; }
                sub[len-1] = (unsigned char)('0' + (10 - t % 10) % 10);
            }
            ptrdiff_t caps[3][2];
            size_t pos = len ? rnd() % (len + 1) : 0;
            caps[0][0] = (ptrdiff_t)(rnd() % (len + 1)); caps[0][1] = -1;
            for (int g = 1; g < 3; g++) {
                switch (rnd() % 5) {
                case 0: caps[g][0] = caps[g][1] = -1; break;
                case 1: { ptrdiff_t a = rnd() % (len + 1), b = rnd() % (len + 1); caps[g][0] = a; caps[g][1] = b; break; } /* maybe inverted */
                default: { ptrdiff_t a = rnd() % (len + 1); ptrdiff_t b = a + (ptrdiff_t)(rnd() % (len - a + 1)); caps[g][0] = a; caps[g][1] = b; }
                }
            }
            size_t ncap = rnd() % 4;
            struct ub_view v = { sub, len, pos, ncap, (const ptrdiff_t (*)[2])caps, set };
            rx_ctx c = { sub, len, pos, ncap, (const ptrdiff_t (*)[2])caps, NULL, NULL, 0 };
            long a = FNS[fi](&v);
            long b = (long)SEGS[fi](&c);
            total++; if (a != 0) nonzero++;
            if (a != b) { if (bad < 3) fprintf(stderr, "DIVERGE %s len=%zu pos=%zu ncap=%zu: callee %ld segment %ld\n", NAMES[fi], len, pos, ncap, a, b); bad++; }
        }
    }
    printf("views=%ld diverged=%ld nonzero_returns=%ld\n", total, bad, nonzero);
    return bad ? 1 : 0;
}
"""


def _build_c(cc, work, segs, extra=()):
    """Write the segment TU + driver into WORK and build with CC. -> (rc, log)."""
    os.makedirs(work, exist_ok=True)
    order = ["luhn", "isbn13", "member", "netstr", "stub"]
    seg_by_callee = {}
    for r, pat, tag, seg in segs:
        seg_by_callee.setdefault(r["callee"], seg)
    with open(os.path.join(work, "seg.c"), "w") as f:
        f.write(STUB_H)
        for c in order:
            f.write("ptrdiff_t seg_%s(const rx_ctx *ctx) {%s__builtin_trap(); }\n" % (c, seg_by_callee[c]))
    with open(os.path.join(work, "seg_decls.h"), "w") as f:
        f.write(STUB_H + "".join("ptrdiff_t seg_%s(const rx_ctx *);\n" % c for c in order))
        f.write("#define NFN %d\n" % len(order))
        f.write("static long (*FNS[])(const struct ub_view *) = { %s };\n" % ", ".join(FN[c] for c in order))
        f.write("static ptrdiff_t (*SEGS[])(const rx_ctx *) = { %s };\n" % ", ".join("seg_" + c for c in order))
        f.write("static const char *NAMES[] = { %s };\n" % ", ".join('"%s"' % c for c in order))
    with open(os.path.join(work, "driver.c"), "w") as f:
        f.write(DRIVER_C)
    cmd = [cc, "-std=gnu11", "-O2", "-Wall", "-Wextra", "-I", CALLEES, *extra,
           os.path.join(work, "seg.c"), os.path.join(work, "driver.c"),
           os.path.join(CALLEES, "callees.c"), "-o", os.path.join(work, "t")]
    p = subprocess.run(["/usr/bin/gnutimeout", "120"] + cmd, capture_output=True, text=True)
    return p.returncode, p.stderr


def section_behaviour(ok, bad):
    from pcrecbench import TMP_ROOT
    import tempfile
    segs = _segments()
    users = os.path.join(UNUSUAL, "values", "users.tsv")
    ccs = [c for c in ("gcc", "clang") if shutil.which(c)]
    if not ccs:
        ok("behaviour: SKIPPED by name, no C compiler on PATH")
        return
    os.makedirs(TMP_ROOT, exist_ok=True)
    for cc in ccs:
        work = tempfile.mkdtemp(prefix="check_inline_", dir=TMP_ROOT)
        try:
            rc, log = _build_c(cc, work, segs)
            warn = [l for l in log.splitlines() if "warning:" in l]
            if rc != 0:
                bad("behaviour [%s]: the wrapped segments compile" % cc, log[-400:])
                continue
            ok("behaviour [%s]: the wrapped segments compile -Wall -Wextra" % cc,
               "%d warning(s)%s" % (len(warn), ("; first: " + warn[0][-90:]) if warn else ""))
            p = subprocess.run(["/usr/bin/gnutimeout", "120", os.path.join(work, "t"), users],
                               capture_output=True, text=True)
            line = (p.stdout.strip().splitlines() or ["(no output)"])[-1]
            m = re.search(r"views=(\d+) diverged=(\d+) nonzero_returns=(\d+)", line)
            if p.returncode == 0 and m and int(m.group(1)) >= 300000 and int(m.group(3)) > 1000:
                ok("behaviour [%s]: segment == callee on every random view" % cc, line)
            else:
                bad("behaviour [%s]: segment == callee on every random view" % cc,
                    (line + " " + p.stderr[-200:]))
            # CONTROL: one operator flipped in the luhn segment must diverge
            mut = [(r, pat, tag, seg.replace("t % 10 == 0 ? UB_CONTINUE : UB_FAIL",
                                              "t % 10 != 0 ? UB_CONTINUE : UB_FAIL", 1)
                    if r["callee"] == "luhn" else seg) for r, pat, tag, seg in segs]
            rc2, _ = _build_c(cc, work + "_m", mut)
            p2 = subprocess.run(["/usr/bin/gnutimeout", "120", os.path.join(work + "_m", "t"), users],
                                capture_output=True, text=True)
            if rc2 == 0 and p2.returncode == 1 and "DIVERGE luhn" in p2.stderr:
                ok("control [%s]: a flipped operator in the luhn segment is caught" % cc,
                   p2.stderr.strip().splitlines()[0][:70])
            else:
                bad("control [%s]: a flipped operator is caught" % cc, repr((rc2, p2.returncode, p2.stderr[-120:])))
        finally:
            shutil.rmtree(work, ignore_errors=True)
            shutil.rmtree(work + "_m", ignore_errors=True)


SECTIONS = [("generator", section_generator), ("identity", section_identity),
            ("prelude", section_prelude), ("pins", section_pins),
            ("fidelity", section_fidelity), ("behaviour", section_behaviour)]


def run(ok, bad):
    for name, fn in SECTIONS:
        try:
            fn(ok, bad)
        except Exception as e:                      # noqa: BLE001
            bad("inline %s crashed" % name, "%s: %s" % (type(e).__name__, e))


if __name__ == "__main__":
    fails = []

    def _ok(what, detail=""):
        print("   PASS  %-62s %s" % (what, detail))

    def _bad(what, detail=""):
        fails.append(what)
        print("   FAIL  %-62s %s" % (what, detail))
    run(_ok, _bad)
    print("check_inline: %d FAILED" % len(fails) if fails else "check_inline: all passed")
    sys.exit(1 if fails else 0)
