#!/usr/bin/env python3
"""[B148] L4 (lane b148l4): `--mode calls`, `--deep`, `--limits`, `--mem-pass`
and `--anchor-explicit` are ADDITIVE in all six drivers (BD16).

The b140drv / b140drv2 / b140pcrec proofs' two claims, for every driver the
lane touched, in one script:

  1. THE INSTRUMENT. Each driver's timed source (`timed.c`/`.h`, re2
     `timed.cc`, rust's `timed/` crate) is diff-empty against BASE (asserted),
     and in the LINKED binaries the timed function (`timed_run`; rust
     `rust_timed::run_subject`) has the same normalized instruction stream
     (the 2026-10-09-b133 rule: rip-relative and absolute targets masked) and
     the same address mod 64 in the OLD driver (built by BASE's own adapter)
     and the NEW one. POSITIVE CONTROL: `main` differs (it grew; rust's
     `rust_regex_driver::main`, its C `main` being the runtime's shim).
  2. THE MODES. Existing-mode invocations (search, match, find-all, plus a
     JIT / DFA / VM arm where the engine has one) give stdout identical on
     every column but SECONDS, OLD vs NEW.

usage: 2026-10-27-b148l4-instrument-additivity.py BASE_REV WORKDIR
(BASE_REV: the commit the lane branched from; writes nothing in the repo).
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = sys.argv[1]
W = os.path.realpath(sys.argv[2]); os.makedirs(W, exist_ok=True)
OLDROOT = os.path.join(W, "oldroot")

TIMED = {"pcre2": ["testees/pcre2/timed.c", "testees/pcre2/timed.h"],
         "pcrec": ["testees/pcrec/timed.c", "testees/pcrec/timed.h"],
         "onig": ["testees/onig/timed.c", "testees/onig/timed.h"],
         "re2": ["testees/re2/timed.cc", "testees/re2/timed.h"],
         "vectorscan": ["testees/vectorscan/timed.c", "testees/vectorscan/timed.h"],
         "rust": ["testees/rust/timed"]}
SYM = {"rust": "rust_timed::run_subject"}


def sh(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if p.returncode:
        raise SystemExit("FAILED: %s\n%s%s" % (cmd, p.stdout[-1500:], p.stderr[-2000:]))
    return p.stdout


def norm(binary, sym):
    nm = sh(["nm", "-n", "-C", "--defined-only", binary])
    cand = [l for l in nm.splitlines() if " ".join(l.split()[2:]).startswith(sym)]
    if sym == "main":
        cand = [l for l in nm.splitlines() if l.split()[2:] == ["main"]]
    line = cand[0]
    addr = int(line.split()[0], 16)
    raw = sh(["nm", "-n", "--defined-only", binary])
    mangled = next(l.split()[2] for l in raw.splitlines() if int(l.split()[0], 16) == addr
                   and l.split()[1].lower() == "t")
    d = sh(["objdump", "-d", "--no-show-raw-insn", "--disassemble=" + mangled, binary])
    body = []
    for l in d.splitlines():
        m = re.match(r"\s*[0-9a-f]+:\t(.*)", l)
        if not m:
            continue
        ins = m.group(1)
        ins = re.sub(r"\s+#\s*[0-9a-f]+.*$", " # <rip>", ins)
        ins = re.sub(r"-?0x[0-9a-f]+\(%rip\)", "<disp>(%rip)", ins)
        ins = re.sub(r"\b[0-9a-f]+ <([^>]+)>$", r"<\1>", ins)
        body.append(ins.strip())
    return addr, hashlib.sha256("\n".join(body).encode()).hexdigest()[:16], len(body)


def build(root, eng, wd):
    """The driver as `root`'s OWN adapter builds it (prepare + compile one
    pattern, so pcrec's artifact exists too). -> (driver, lib or None)."""
    code = r'''
import sys, os, json
sys.path.insert(0, %r)
from pcrecbench import adapters
a = adapters.discover()[%r]
t = %r
wd = %r
a.prepare(t, wd)
cp = a.compile(t, "p", b"(a+)(b+)?|[0-9]+", {}, 1, wd)
h = cp.forms["plain"].handle
print(json.dumps({"driver": h.get("driver"), "lib": h.get("lib")}))
''' % (root, eng, {"pcre2": "pcre2-interp", "pcrec": "pcrec-vm", "onig": "onig-default",
                   "re2": "re2-default", "rust": "rust-default",
                   "vectorscan": "vectorscan-block-som"}[eng], wd)
    out = sh([sys.executable, "-c", code], cwd=root,
             env=dict(os.environ, PYTHONPATH=root))
    import json
    return json.loads(out.strip().splitlines()[-1])


def strip_secs(out):
    keep = []
    for l in out.splitlines():
        c = l.split("\t")
        if c[0] == "subject" and len(c) >= 9:
            c[8] = "<s>"
        elif c[0] == "compile" and len(c) >= 4:
            c[3] = "<s>"
        elif c[0] == "info" and c[1:2] and ("seconds" in c[1] or c[1] in ("lib", "pattern")):
            c[2:] = ["<x>"]
        keep.append("\t".join(c))
    return "\n".join(keep)


def main():
    if not os.path.isdir(OLDROOT):
        os.makedirs(OLDROOT)
        tar = subprocess.run(["git", "-C", ROOT, "archive", BASE, "pcrecbench", "testees",
                              "schema", "tools"], capture_output=True, check=True).stdout
        subprocess.run(["tar", "-x", "-C", OLDROOT], input=tar, check=True)
    print("BASE %s; NEW = the working tree at %s" % (BASE, sh(["git", "-C", ROOT, "rev-parse",
                                                              "--short", "HEAD"]).strip()))
    subj = os.path.join(W, "subjects.tsv")
    with open(os.path.join(W, "s1.txt"), "wb") as f:
        f.write(b"GET /a.php?x=1 HTTP/1.1 aaab bbb 12345 aab\n" * 40)
    with open(os.path.join(W, "s2.txt"), "wb") as f:
        f.write(b"nothing here\n")
    with open(subj, "w") as f:
        f.write("s1\t%s\ns2\t%s\n" % (os.path.join(W, "s1.txt"), os.path.join(W, "s2.txt")))
    pat = os.path.join(W, "p.rx")
    with open(pat, "wb") as f:
        f.write(b"(a+)(b+)?|[0-9]+")
    total = 0
    for eng in ("pcre2", "pcrec", "onig", "re2", "rust", "vectorscan"):
        diff = sh(["git", "-C", ROOT, "diff", BASE, "--"] + TIMED[eng])
        assert not diff, eng
        old = build(OLDROOT, eng, os.path.join(W, "old-" + eng))
        new = build(ROOT, eng, os.path.join(W, "new-" + eng))
        sym = SYM.get(eng, "timed_run")
        a_o, h_o, n_o = norm(old["driver"], sym)
        a_n, h_n, n_n = norm(new["driver"], sym)
        # rust's C-level `main` is the runtime's shim; its own main is the control
        ctl = "rust_regex_driver::main" if eng == "rust" else "main"
        m_o, m_n = norm(old["driver"], ctl), norm(new["driver"], ctl)
        print("%-10s timed source diff EMPTY; %s OLD mod64=%d %d insns %s | NEW mod64=%d %d insns %s -> %s; "
              "CONTROL main %s"
              % (eng, sym, a_o % 64, n_o, h_o, a_n % 64, n_n, h_n,
                 "IDENTICAL" if (h_o, n_o, a_o % 64) == (h_n, n_n, a_n % 64) else "DIFFERS",
                 "differs" if m_o[1] != m_n[1] else "IDENTICAL?!"))
        assert (h_o, n_o, a_o % 64) == (h_n, n_n, a_n % 64) and m_o[1] != m_n[1], eng
        pre = ["--lib", new["lib"]] if eng == "pcrec" else []
        runs = [["--mode", "search", "--iters", "3"], ["--mode", "match", "--iters", "2"],
                ["--mode", "search", "--iters", "2", "--find-all"]]
        if eng == "pcre2":
            runs += [["--mode", "search", "--iters", "2", "--jit"],
                     ["--mode", "search", "--iters", "2", "--find-all", "--dfa"]]
        if eng in ("onig", "rust", "vectorscan"):
            # these drivers take the FORM explicitly: match = the whole-subject
            # artifact the adapter compiles (testees/<eng>/adapter.py)
            runs = [r + ["--form", "whole-subject" if r[1] == "match" else "plain"]
                    for r in runs]
        if eng == "vectorscan":
            runs = [r + ["--som"] for r in runs]
        for args in runs:
            argv = pre + ["--pattern", pat, "--list", subj] + args
            if eng == "pcrec":
                argv = pre + ["--list", subj] + args
            o = strip_secs(sh([old["driver"]] + argv))
            n = strip_secs(sh([new["driver"]] + argv))
            same = o == n
            print("    mode %-48s %s" % (" ".join(args), "IDENTICAL (%d lines, secs masked)"
                                          % len(o.splitlines()) if same else "DIFFERS"))
            if not same:
                print(o, "\n----\n", n)
            assert same, eng
            total += 1
    print("ALL six drivers: the timed function unchanged; %d existing-mode invocations identical"
          % total)


if __name__ == "__main__":
    main()
