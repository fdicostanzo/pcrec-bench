#!/usr/bin/env python3
"""[B133] isolation proof: the timed function's bytes and address mod 64 are
UNCHANGED when ~40 dummy getter lines are added to a driver (and, for pcrec,
to shim.c).

For each engine's driver: build BASE (the committed driver + timed unit) and
VARIANT (the same with 40 `printf("info\\tdummyN ...")` lines inserted before
the first `if (!list_path)` -- exactly the shape of the [B124]/[B126] getter
growth [B132] blamed), then compare, for the timed function:
  - its address mod 64 in the LINKED binary (both builds),
  - the sha256 of its disassembly with every absolute address / rip-relative
    target normalized away (a call's rel32 and a .rodata reference move with
    the link; the instruction stream does not),
and, as the POSITIVE CONTROL that the comparison can see a change at all, the
size of main() (which grows) and, for the pcrec shim, the PRE-[B133] shim.c
(git ec62878) with the same 40 getters: its pb_search address mod 64 MOVES.
usage: 2026-10-09-b133-isolation-proof.py WORKDIR   (writes nothing in the repo)
"""
import os, re, subprocess, sys, hashlib, shutil

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
W = os.path.realpath(sys.argv[1]); os.makedirs(W, exist_ok=True)
DUMMY_N = 40

def sh(cmd, **kw):
    p = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, **kw)
    if p.returncode: raise SystemExit("FAILED: %s\n%s" % (cmd, p.stderr[-2000:]))
    return p.stdout

def norm_disasm(binary, symre):
    """-> {symbol: (addr, sha of normalized stream, ninsn)} for symbols matching symre"""
    nm = sh(["nm", "-n", "--defined-only", binary])
    out = {}
    for line in nm.splitlines():
        a, t, s = line.split(None, 2)
        if t in "tT" and re.fullmatch(symre, s):
            d = sh(["objdump", "-d", "--no-show-raw-insn", "--disassemble=" + s, binary])
            body = []
            for l in d.splitlines():
                m = re.match(r"\s*[0-9a-f]+:\t(.*)", l)
                if not m: continue
                ins = m.group(1)
                ins = re.sub(r"\s+#\s*[0-9a-f]+.*$", " # <rip>", ins)       # rip-relative target
                ins = re.sub(r"-?0x[0-9a-f]+\(%rip\)", "<disp>(%rip)", ins)  # its displacement
                ins = re.sub(r"\b[0-9a-f]+ <([^>+]+)>$", r"<\1>", ins)     # call/jmp to another symbol
                ins = re.sub(r"\b[0-9a-f]+ <(%s\+0x[0-9a-f]+)>$" % re.escape(s), r"<\1>", ins)  # intra-function (kept)
                ins = re.sub(r"\b[0-9a-f]+ <%s>$" % re.escape(s), "<%s>" % s, ins)
                body.append(ins.strip())
            out[s] = (int(a, 16), hashlib.sha256("\n".join(body).encode()).hexdigest()[:16], len(body))
    return out

def add_dummies(src_text, anchor_re, line_fmt):
    lines = src_text.split("\n")
    idx = next(i for i, l in enumerate(lines) if re.search(anchor_re, l))
    ins = [line_fmt % (i, i, i) for i in range(DUMMY_N)]
    return "\n".join(lines[:idx] + ins + lines[idx:])

C_DUMMY = '    printf("info\\tdummy%d\\t%d\\n", %d, 0);'
CC_DUMMY = '    std::printf("info\\tdummy%d\\t%d\\n", %d, 0);'
engines = [
  # name, dir, driver file, compile argv builder, timed symbol re, anchor, dummy fmt
  ("pcrec", "pcrec", "driver.c", "cc", ["-ldl"], r"timed_run", r"if \(!list_path\)", C_DUMMY),
  ("pcre2", "pcre2", "driver.c", "cc", ["-ldl"], r"timed_run", r"if \(!list_path\)", C_DUMMY),
  ("onig", "onig", "driver.c", "cc", ["-lonig"], r"timed_run", r"if \(!list_path\)", C_DUMMY),
  ("tre", "tre", "driver.c", "cc", ["-ltre"], r"timed_run", r"if \(!list_path\)", C_DUMMY),
  ("vectorscan", "vectorscan", "driver.c", "cc", ["-lhs"], r"timed_run", r"if \(!list_path\)", C_DUMMY),
  ("re2", "re2", "driver.cc", "cxx", None, r"_Z9timed_run.*", r"if \(!load_list", CC_DUMMY),
]

def build_c(d, drv, timed, out, libs, cxx=False):
    if cxx:
        cf = sh("pkg-config --cflags re2").split(); lb = sh("pkg-config --libs re2").split()
        sh(["g++", "-O2", "-std=c++17"] + cf + ["-I", d, "-o", out, drv, timed] + lb)
    else:
        sh(["gcc", "-O2", "-std=gnu11", "-I", d, "-o", out, drv, timed] + libs)

report = []
ok = True
for name, sub, drvfile, kind, libs, symre, anchor, fmt in engines:
    src_dir = os.path.join(ROOT, "testees", sub)
    ed = os.path.join(W, name); shutil.rmtree(ed, ignore_errors=True)
    os.makedirs(ed + "/base"); os.makedirs(ed + "/var")
    for sd in ("base", "var"):
        for f in os.listdir(src_dir):
            if f.startswith("timed.") or f == drvfile:
                shutil.copy(os.path.join(src_dir, f), os.path.join(ed, sd, f))
    vp = os.path.join(ed, "var", drvfile)
    txt = add_dummies(open(vp).read(), anchor, fmt)
    open(vp, "w").write(txt)
    timed = "timed.cc" if kind == "cxx" else "timed.c"
    res = {}
    for sd in ("base", "var"):
        d = os.path.join(ed, sd)
        build_c(d, os.path.join(d, drvfile), os.path.join(d, timed), os.path.join(d, "drv"),
                libs, cxx=(kind == "cxx"))
        res[sd] = norm_disasm(os.path.join(d, "drv"), symre)
        res[sd + "_main"] = norm_disasm(os.path.join(d, "drv"), r"main")
    sb = list(res["base"].values())[0]
    sv = list(res["var"].values())[0]
    mb = res["base_main"]["main"]; mv = res["var_main"]["main"]
    same = (sb[1] == sv[1] and sb[2] == sv[2] and sb[0] % 64 == 0 and sv[0] % 64 == 0)
    ok &= same
    report.append("%-10s timed fn: base addr=0x%x mod64=%d ninsn=%d sha=%s | variant addr=0x%x mod64=%d ninsn=%d sha=%s | %s"
                  % (name, sb[0], sb[0] % 64, sb[2], sb[1], sv[0], sv[0] % 64, sv[2], sv[1],
                     "IDENTICAL" if same else "*** DIFFERS ***"))
    report.append("%-10s   control: main() insns base=%d variant=%d (main changed: %s)"
                  % ("", mb[2], mv[2], "yes" if mb[1] != mv[1] else "NO -- control is blind"))
    ok &= (mb[1] != mv[1])


# ---------------------------------------------------------------- rust
def rust_part():
    rd = os.path.join(W, "rust"); shutil.rmtree(rd, ignore_errors=True)
    env = dict(os.environ, PATH=os.path.expanduser("~/.cargo/bin") + ":" + os.environ["PATH"])
    res = {}
    for sd in ("base", "var"):
        d = os.path.join(rd, sd)
        shutil.copytree(os.path.join(ROOT, "testees", "rust"), d,
                        ignore=shutil.ignore_patterns("target", "*.py", "*.toml.bak", "CLAUDE.md", "configs.toml"))
        if sd == "var":
            mp = os.path.join(d, "src", "main.rs"); txt = open(mp).read().split("\n")
            idx = next(i for i, l in enumerate(txt) if "let list_path = match" in l)
            ins = ['    emit!("info\\tdummy%d\\t{}", %d);' % (i, i) for i in range(DUMMY_N)]
            open(mp, "w").write("\n".join(txt[:idx] + ins + txt[idx:]))
        subprocess.run(["cargo", "build", "--release", "--locked", "--offline", "--manifest-path",
                        d + "/Cargo.toml", "--target-dir", d + "/tgt"], check=True, capture_output=True, env=env)
        b = d + "/tgt/release/rust_regex_driver"
        res[sd] = norm_disasm(b, r"_RNvCs\w+_10rust_timed11run_subject")
        res[sd + "_main"] = norm_disasm(b, r"_RNvCs\w+_17rust_regex_driver4main")
    sb = list(res["base"].values())[0]; sv = list(res["var"].values())[0]
    mb = list(res["base_main"].values())[0]; mv = list(res["var_main"].values())[0]
    same = sb[1] == sv[1] and sb[2] == sv[2] and sb[0] % 64 == 0 and sv[0] % 64 == 0
    report.append("%-10s timed fn: base addr=0x%x mod64=%d ninsn=%d sha=%s | variant addr=0x%x mod64=%d ninsn=%d sha=%s | %s"
                  % ("rust", sb[0], sb[0] % 64, sb[2], sb[1], sv[0], sv[0] % 64, sv[2], sv[1],
                     "IDENTICAL" if same else "*** DIFFERS ***"))
    report.append("%-10s   control: main() insns base=%d variant=%d (main changed: %s)"
                  % ("", mb[2], mv[2], "yes" if mb[1] != mv[1] else "NO -- control is blind"))
    return same and mb[1] != mv[1]
ok &= rust_part()

# ---------------------------------------------------------------- pcrec shim
def shim_part():
    pcrec = sh([os.path.join(ROOT, "testees", "pcrec", "pin.sh"), "--path", "255bcdd8"]).strip()
    pat_dir = os.path.join(ROOT, "bench", "capability", "patterns")
    marker = "/* ------------------------------------------------------------- matching */"
    cur = open(os.path.join(ROOT, "testees", "pcrec", "shim.c")).read()
    pre = sh(["git", "-C", ROOT, "show", "ec62878:testees/pcrec/shim.c"])
    # varied sizes (a stamp getter is 16 B for a constant, more for a string/branch):
    # 40 identical 16-byte bodies would add 640 B = 0 mod 64 and move nothing.
    getters = "\n".join(
        "long long pb_dummy_getter%d(void) { return %d; }" % (i, i) if i % 3 else
        "const char *pb_dummy_getter%d(void) { static volatile int v; return v ? \"a%d\" : (v = %d, \"b\"); }" % (i, i, i)
        for i in range(DUMMY_N + 1)) + "\n"
    arms = {"post": cur, "post+40": cur.replace(marker, getters + marker, 1),
            "pre": pre, "pre+40": pre.replace(marker, getters + marker, 1)}
    fns = ["pb_search", "pb_match_caps", "pb_search_in", "pb_match_caps_in"]
    allok = True
    for pat in ("winpath-near-miss", "keyword-prefix-order"):
        for cfgname, fl in (("caps", []), ("nocaps", ["--no-captures"])):
            d = os.path.join(W, "shim-%s-%s" % (pat, cfgname)); os.makedirs(d, exist_ok=True)
            sh([pcrec, "-p", "rx", "-fcomments", "--features", "all"] + fl +
               ["-o", d + "/artifact.c", "--pattern", open(os.path.join(pat_dir, pat + ".rx")).read().rstrip("\n")])
            rows = {}
            for arm, txt in arms.items():
                sp = os.path.join(d, arm + ".c"); open(sp, "w").write(txt)
                so = os.path.join(d, arm + ".so")
                sh(["gcc", "-O2", "-std=gnu11", "-fPIC", "-shared", "-o", so, sp,
                    '-DPB_ARTIFACT="%s/artifact.c"' % d, "-I", d])
                rows[arm] = norm_disasm(so, "|".join(fns + ["rx_search"]))
                if "rx_search" not in rows[arm]:
                    rows[arm].update(norm_disasm(so, r"[a-z_0-9]*_search"))
            for arm in arms:
                report.append("shim %-20s %-7s %-8s " % (pat, cfgname, arm) + " ".join(
                    "%s:mod64=%d,sha=%s" % (f, rows[arm][f][0] % 64, rows[arm][f][1][:8]) for f in fns if f in rows[arm]))
            # the claim: post vs post+40 identical placement and bytes on the four wrappers
            same = all(rows["post"][f][0] % 64 == 0 and rows["post+40"][f][0] % 64 == 0
                       and rows["post"][f][1] == rows["post+40"][f][1] for f in fns if f in rows["post"])
            moved = any(rows["pre"][f][0] % 64 != rows["pre+40"][f][0] % 64 for f in fns if f in rows["pre"])
            report.append("shim %s %s: post vs post+40 wrappers identical & 64-aligned: %s ; positive control "
                          "(pre-B133 shim, +40 getters) moves a wrapper mod 64: %s" % (pat, cfgname, same, moved))
            allok &= same
    return allok
ok &= shim_part()

print("\n".join(report))
sys.exit(0 if ok else 1)
