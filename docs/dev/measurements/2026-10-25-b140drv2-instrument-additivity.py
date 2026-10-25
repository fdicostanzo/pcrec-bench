#!/usr/bin/env python3
"""[B140] b140drv2: the rust and RE2 drivers' new `--mode subst` is ADDITIVE.

The same two claims, per engine, that 2026-10-25-b140drv-instrument-
additivity.py makes for pcre2 (BD16, docs/dev/decisions.md):

  1. THE INSTRUMENT. The existing timed unit is untouched (git diff BASE is
     empty for testees/re2/timed.cc, timed.h and testees/rust/timed/ -- the
     whole crate), the new timed function lives in its own unit
     (re2: timed_subst.cc; rust: the crate testees/rust/timed-subst/), and in
     the LINKED binaries the existing timed function (re2 `timed_run`; rust
     `rust_timed::run_subject`) has the same normalized instruction stream
     (sha256 of its disassembly with absolute addresses / rip-relative targets
     normalized, the 2026-10-09-b133-isolation-proof.py rule) and the same
     address mod 64 (== 0) in the OLD driver (BASE) and the NEW one.
     POSITIVE CONTROL: the normalized stream of `main` DIFFERS (it grew), so
     the comparison can see a change.
  2. THE MODES. For each of the existing-mode invocations below, the OLD and
     NEW drivers' stdout is identical on every column but SECONDS (the clock).

usage: 2026-10-25-b140drv2-instrument-additivity.py BASE_REV WORKDIR
(BASE_REV is the commit before the lane, e.g. 43b65a3c; writes nothing in the
repo). Needs g++/pkg-config re2, cargo (offline; the vendored registry), objdump, nm.
"""
import hashlib, os, re, shutil, subprocess, sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
BASE = sys.argv[1]
W = os.path.realpath(sys.argv[2]); os.makedirs(W, exist_ok=True)


def sh(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if p.returncode:
        raise SystemExit("FAILED: %s\n%s" % (cmd, p.stderr[-2000:]))
    return p.stdout


def norm(binary, symre):
    """-> (addr, sha, ninsn, symbol) of the one defined text symbol matching symre"""
    nm = sh(["nm", "-n", "--defined-only", binary])
    hits = [l.split(None, 2) for l in nm.splitlines()
            if len(l.split(None, 2)) == 3 and l.split(None, 2)[1] in "tT"
            and re.fullmatch(symre, l.split(None, 2)[2])]
    assert len(hits) == 1, (symre, hits)
    a, _t, sym = hits[0]
    d = sh(["objdump", "-d", "--no-show-raw-insn", "--disassemble=" + sym, binary])
    body = []
    for l in d.splitlines():
        m = re.match(r"\s*[0-9a-f]+:\t(.*)", l)
        if not m:
            continue
        ins = m.group(1)
        ins = re.sub(r"\s+#\s*[0-9a-f]+.*$", " # <rip>", ins)
        ins = re.sub(r"-?0x[0-9a-f]+\(%rip\)", "<disp>(%rip)", ins)
        ins = re.sub(r"\b[0-9a-f]+ <([^>+]+)>$", r"<\1>", ins)
        ins = re.sub(r"\b[0-9a-f]+ <(%s\+0x[0-9a-f]+)>$" % re.escape(sym), r"<\1>", ins)
        ins = re.sub(r"\b[0-9a-f]+ <%s>$" % re.escape(sym), "<%s>" % sym, ins)
        body.append(ins.strip())
    return int(a, 16), hashlib.sha256("\n".join(body).encode()).hexdigest()[:16], len(body), sym


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


def diff_empty(paths):
    d = sh(["git", "-C", ROOT, "diff", BASE, "--"] + paths)
    print("diff vs %s of %s: %s" % (BASE, " ".join(paths), "EMPTY (untouched)" if not d else "NOT EMPTY"))
    assert not d


# ---- the shared subjects and patterns
subj = os.path.join(W, "subjects.tsv")
with open(os.path.join(W, "s1.txt"), "wb") as f:
    f.write(b"GET /a.php?x=1 HTTP/1.1 foo@bar.com 10.0.0.1 aaa bbb 12345\n" * 40 + "café über\n".encode())
with open(os.path.join(W, "s2.txt"), "wb") as f:
    f.write(b"nothing here\n")
with open(subj, "w") as f:
    f.write("s1\t%s\ns2\t%s\n" % (os.path.join(W, "s1.txt"), os.path.join(W, "s2.txt")))
pats = {"lit": b"HTTP/1\\.1", "cls": b"[0-9]+", "grp": b"(a+)(b+)?", "email": b"[a-z]+@[a-z.]+",
        "whole": b"\\A(?:[a-z ]+)\\z"}
for k, v in pats.items():
    with open(os.path.join(W, "p-" + k), "wb") as f:
        f.write(v)


def compare_modes(old, new, runs, label):
    ok = 0
    for pk, args in runs:
        argv = ["--pattern", os.path.join(W, "p-" + pk), "--list", subj] + args
        o = strip_secs(sh([old] + argv))
        n = strip_secs(sh([new] + argv))
        same = o == n
        print("%s mode %-62s %s" % (label, " ".join(args), "IDENTICAL (%d lines, secs masked)" % len(o.splitlines()) if same else "DIFFERS"))
        assert same, (o, n)
        ok += 1
    return ok


# ============================================================ RE2
print("=== RE2 (testees/re2) ===")
diff_empty(["testees/re2/timed.cc", "testees/re2/timed.h"])
old = os.path.join(W, "re2-old"); os.makedirs(old, exist_ok=True)
for f in ("driver.cc", "timed.cc", "timed.h"):
    with open(os.path.join(old, f), "w") as fh:
        fh.write(sh(["git", "-C", ROOT, "show", "%s:testees/re2/%s" % (BASE, f)]))
SRC = os.path.join(ROOT, "testees", "re2")
cflags = sh(["pkg-config", "--cflags", "re2"]).split()
libs = sh(["pkg-config", "--libs", "re2"]).split()
cxx = ["g++", "-O2", "-std=c++17"] + cflags
sh(cxx + ["-o", os.path.join(W, "re2_old"), os.path.join(old, "driver.cc"), os.path.join(old, "timed.cc")] + libs)
sh(cxx + ["-o", os.path.join(W, "re2_new"), os.path.join(SRC, "driver.cc"), os.path.join(SRC, "timed.cc"),
          os.path.join(SRC, "timed_subst.cc")] + libs)
a_o, h_o, n_o, _ = norm(os.path.join(W, "re2_old"), r"_Z9timed_runPK8timed_inP9timed_out")
a_n, h_n, n_n, _ = norm(os.path.join(W, "re2_new"), r"_Z9timed_runPK8timed_inP9timed_out")
print("timed_run  OLD addr %#x (mod 64 = %d) %d insns sha %s" % (a_o, a_o % 64, n_o, h_o))
print("timed_run  NEW addr %#x (mod 64 = %d) %d insns sha %s" % (a_n, a_n % 64, n_n, h_n))
assert a_o % 64 == 0 and a_n % 64 == 0 and h_o == h_n and n_o == n_n
m_o = norm(os.path.join(W, "re2_old"), "main"); m_n = norm(os.path.join(W, "re2_new"), "main")
print("CONTROL main: OLD %d insns sha %s ; NEW %d insns sha %s -> %s" % (
    m_o[2], m_o[1], m_n[2], m_n[1], "differs (the comparison can see a change)" if m_o[1] != m_n[1] else "IDENTICAL?!"))
assert m_o[1] != m_n[1]
a_s, h_s, n_s, _ = norm(os.path.join(W, "re2_new"), r"_Z11timed_substPK9tsubst_inP10tsubst_out")
print("timed_subst NEW addr %#x (mod 64 = %d) %d insns sha %s" % (a_s, a_s % 64, n_s, h_s))
assert a_s % 64 == 0
runs = [
    ("lit", ["--mode", "search", "--iters", "3"]),
    ("cls", ["--mode", "search", "--iters", "2", "--find-all"]),
    ("whole", ["--mode", "match", "--iters", "2"]),
    ("email", ["--mode", "search", "--iters", "2", "--find-all", "--prime"]),
    ("email", ["--mode", "search", "--iters", "2", "--longest"]),
    ("cls", ["--mode", "search", "--iters", "1", "--find-all", "--utf8", "--encoding", "utf8"]),
]
k1 = compare_modes(os.path.join(W, "re2_old"), os.path.join(W, "re2_new"), runs, "re2 ")
print("RE2: ALL %d existing-mode invocations identical; timed_run unchanged" % k1)

# ============================================================ RUST
print("=== RUST (testees/rust) ===")
diff_empty(["testees/rust/timed"])
old = os.path.join(W, "rust-old")
shutil.rmtree(old, ignore_errors=True)
files = sh(["git", "-C", ROOT, "ls-tree", "-r", "--name-only", BASE, "testees/rust"]).split()
for rel in files:
    if rel.endswith((".md", ".py", ".toml")) and rel.count("/") == 2 and not rel.endswith("Cargo.toml") and not rel.endswith("Cargo.lock"):
        continue
    dst = os.path.join(old, os.path.relpath(rel, "testees/rust"))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w") as fh:
        fh.write(sh(["git", "-C", ROOT, "show", "%s:%s" % (BASE, rel)]))
cargo = shutil.which("cargo") or os.path.expanduser("~/.cargo/bin/cargo")
sh([cargo, "build", "--release", "--locked", "--offline", "--manifest-path", os.path.join(old, "Cargo.toml"),
    "--target-dir", os.path.join(W, "rust-old-target")])
sh([cargo, "build", "--release", "--locked", "--offline", "--manifest-path", os.path.join(ROOT, "testees/rust/Cargo.toml"),
    "--target-dir", os.path.join(W, "rust-new-target")])
r_old = os.path.join(W, "rust-old-target", "release", "rust_regex_driver")
r_new = os.path.join(W, "rust-new-target", "release", "rust_regex_driver")
sym = r"_RNvC[A-Za-z0-9]+_10rust_timed11run_subject"
a_o, h_o, n_o, s_o = norm(r_old, sym)
a_n, h_n, n_n, s_n = norm(r_new, sym)
print("run_subject OLD addr %#x (mod 64 = %d) %d insns sha %s (%s)" % (a_o, a_o % 64, n_o, h_o, s_o))
print("run_subject NEW addr %#x (mod 64 = %d) %d insns sha %s (%s)" % (a_n, a_n % 64, n_n, h_n, s_n))
assert a_o % 64 == 0 and a_n % 64 == 0 and h_o == h_n and n_o == n_n
m_o = norm(r_old, r"_RNvC[A-Za-z0-9]+_17rust_regex_driver4main")
m_n = norm(r_new, r"_RNvC[A-Za-z0-9]+_17rust_regex_driver4main")
print("CONTROL driver main: OLD %d insns sha %s ; NEW %d insns sha %s -> %s" % (
    m_o[2], m_o[1], m_n[2], m_n[1], "differs (the comparison can see a change)" if m_o[1] != m_n[1] else "IDENTICAL?!"))
assert m_o[1] != m_n[1]
a_s, h_s, n_s, _ = norm(r_new, r"_RNvC[A-Za-z0-9]+_16rust_timed_subst11timed_subst")
print("timed_subst NEW addr %#x (mod 64 = %d) %d insns sha %s" % (a_s, a_s % 64, n_s, h_s))
assert a_s % 64 == 0
rruns = [
    ("lit", ["--mode", "search", "--iters", "3"]),
    ("cls", ["--mode", "search", "--iters", "2", "--find-all"]),
    ("whole", ["--mode", "match", "--form", "whole-subject", "--iters", "2"]),
    ("email", ["--mode", "search", "--iters", "2", "--find-all", "--prime"]),
    ("cls", ["--mode", "search", "--iters", "1", "--find-all", "--utf8"]),
    ("grp", ["--mode", "search", "--iters", "2", "--subject-timeout", "30"]),
]
k2 = compare_modes(r_old, r_new, rruns, "rust")
print("RUST: ALL %d existing-mode invocations identical; run_subject unchanged" % k2)
print("DONE")
