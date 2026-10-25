#!/usr/bin/env python3
"""[B140] b140drv: the pcre2 driver's new `--mode subst` is ADDITIVE.

Two claims, each with its evidence, for BD16 (docs/dev/decisions.md) and the
brief's "no existing mode may change by a byte":

  1. THE INSTRUMENT. timed.c is untouched (git diff BASE -- testees/pcre2/
     timed.c is empty, asserted), the new timed function lives in its own
     translation unit (timed_subst.c), and in the LINKED binaries `timed_run`
     has the same normalized instruction stream (sha256 of its disassembly
     with absolute addresses / rip-relative targets normalized, the
     2026-10-09-b133-isolation-proof.py rule) and the same address mod 64
     (== 0) in the OLD driver (BASE) and the NEW one. POSITIVE CONTROL: the
     normalized stream of `main` DIFFERS (it grew), so the comparison can see
     a change.
  2. THE MODES. For each of 8 invocations of the existing modes (search,
     match, find-all; interp, jit, dfa; one -utf), the OLD and NEW drivers'
     stdout is identical on every column but SECONDS (the clock).

usage: 2026-10-25-b140drv-instrument-additivity.py BASE_REV WORKDIR
(BASE_REV is the commit before the lane, e.g. 80569bf1; writes nothing in the
repo). Needs gcc, objdump, nm, libpcre2-8.so.0.
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = sys.argv[1]
W = os.path.realpath(sys.argv[2]); os.makedirs(W, exist_ok=True)
SRC = os.path.join(ROOT, "testees", "pcre2")


def sh(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if p.returncode:
        raise SystemExit("FAILED: %s\n%s" % (cmd, p.stderr[-2000:]))
    return p.stdout


def norm(binary, sym):
    nm = sh(["nm", "-n", "--defined-only", binary])
    addr = next(int(l.split()[0], 16) for l in nm.splitlines() if l.split()[2:] == [sym] or l.endswith(" " + sym))
    d = sh(["objdump", "-d", "--no-show-raw-insn", "--disassemble=" + sym, binary])
    body = []
    for l in d.splitlines():
        m = re.match(r"\s*[0-9a-f]+:\t(.*)", l)
        if not m:
            continue
        ins = m.group(1)
        ins = re.sub(r"\s+#\s*[0-9a-f]+.*$", " # <rip>", ins)
        ins = re.sub(r"-?0x[0-9a-f]+\(%rip\)", "<disp>(%rip)", ins)
        ins = re.sub(r"\b[0-9a-f]+ <([^>]+)>$", r"<\1>", ins)   # call/jmp: drop the absolute address, keep symbol+offset
        body.append(ins.strip())
    return addr, hashlib.sha256("\n".join(body).encode()).hexdigest()[:16], len(body)


# ---- build OLD (BASE_REV) and NEW
old = os.path.join(W, "old"); os.makedirs(old, exist_ok=True)
for f in ("driver.c", "timed.c", "timed.h"):
    with open(os.path.join(old, f), "w") as fh:
        fh.write(sh(["git", "-C", ROOT, "show", "%s:testees/pcre2/%s" % (BASE, f)]))
cc = ["gcc", "-O2", "-std=gnu11"]
sh(cc + ["-o", os.path.join(W, "drv_old"), os.path.join(old, "driver.c"), os.path.join(old, "timed.c"), "-ldl"])
sh(cc + ["-o", os.path.join(W, "drv_new"), os.path.join(SRC, "driver.c"), os.path.join(SRC, "timed.c"),
         os.path.join(SRC, "timed_subst.c"), "-ldl"])

diff = sh(["git", "-C", ROOT, "diff", BASE, "--", "testees/pcre2/timed.c", "testees/pcre2/timed.h"])
print("timed.c / timed.h diff vs %s: %s" % (BASE, "EMPTY (untouched)" if not diff else "NOT EMPTY"))
assert not diff

a_old, h_old, n_old = norm(os.path.join(W, "drv_old"), "timed_run")
a_new, h_new, n_new = norm(os.path.join(W, "drv_new"), "timed_run")
print("timed_run  OLD addr %#x (mod 64 = %d) %d insns sha %s" % (a_old, a_old % 64, n_old, h_old))
print("timed_run  NEW addr %#x (mod 64 = %d) %d insns sha %s" % (a_new, a_new % 64, n_new, h_new))
assert a_old % 64 == 0 and a_new % 64 == 0 and h_old == h_new and n_old == n_new
m_old = norm(os.path.join(W, "drv_old"), "main")
m_new = norm(os.path.join(W, "drv_new"), "main")
print("CONTROL main: OLD %d insns sha %s ; NEW %d insns sha %s -> %s"
      % (m_old[2], m_old[1], m_new[2], m_new[1], "differs (the comparison can see a change)" if m_old[1] != m_new[1] else "IDENTICAL?!"))
assert m_old[1] != m_new[1]
a_s, h_s, n_s = norm(os.path.join(W, "drv_new"), "timed_subst")
print("timed_subst NEW addr %#x (mod 64 = %d) %d insns sha %s" % (a_s, a_s % 64, n_s, h_s))
assert a_s % 64 == 0

# ---- the modes
subj = os.path.join(W, "subjects.tsv")
with open(os.path.join(W, "s1.txt"), "wb") as f:
    f.write(b"GET /a.php?x=1 HTTP/1.1 foo@bar.com 10.0.0.1 aaa bbb 12345\n" * 40 + "café über\n".encode())
with open(os.path.join(W, "s2.txt"), "wb") as f:
    f.write(b"nothing here\n")
with open(subj, "w") as f:
    f.write("s1\t%s\ns2\t%s\n" % (os.path.join(W, "s1.txt"), os.path.join(W, "s2.txt")))
pats = {"lit": b"HTTP/1\\.1", "cls": b"[0-9]+", "grp": b"(a+)(b+)?", "email": b"[a-z]+@[a-z.]+"}
for k, v in pats.items():
    with open(os.path.join(W, "p-" + k), "wb") as f:
        f.write(v)
runs = [
    ("lit", ["--mode", "search", "--iters", "3"]),
    ("lit", ["--mode", "search", "--iters", "3", "--jit"]),
    ("cls", ["--mode", "search", "--iters", "2", "--find-all"]),
    ("cls", ["--mode", "search", "--iters", "2", "--find-all", "--jit"]),
    ("grp", ["--mode", "match", "--iters", "2"]),
    ("email", ["--mode", "search", "--iters", "2", "--dfa"]),
    ("email", ["--mode", "search", "--iters", "2", "--find-all", "--dfa"]),
    ("cls", ["--mode", "search", "--iters", "1", "--find-all", "--utf", "--utf8"]),
]


def strip_secs(out):
    keep = []
    for l in out.splitlines():
        c = l.split("\t")
        if c[0] == "subject" and len(c) >= 11:
            c[8] = "<s>"
        elif c[0] == "compile":
            c[3] = "<s>"
        keep.append("\t".join(c))
    return "\n".join(keep)


ok = 0
for pk, args in runs:
    argv = ["--pattern", os.path.join(W, "p-" + pk), "--list", subj] + args
    o = strip_secs(sh([os.path.join(W, "drv_old")] + argv))
    n = strip_secs(sh([os.path.join(W, "drv_new")] + argv))
    same = o == n
    print("mode %-60s %s" % (" ".join(args), "IDENTICAL (%d lines, secs masked)" % len(o.splitlines()) if same else "DIFFERS"))
    assert same, (o, n)
    ok += 1
print("ALL %d existing-mode invocations identical; timed_run unchanged" % ok)
