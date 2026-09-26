"""docs/dev/measurements/probe_b101_twin_refusals.py -- [B101]: capability@0.1 x 64 x both forms under pcrec-auto's flags at 02902356, default vs -fno-req-byte: the refusal set and program identity (v2). Archived result in 2026-09-26-b101-twin-stamps.txt (tail)."""
import os, sys, tempfile
sys.path.insert(0, os.getcwd()); sys.path.insert(0, "tools")
import program_identity as PI
from pcrecbench import subbench as _sb, record as _rec, capability as _cap
B = "/home/duxevents/pcrec-bench/build/pcrec-02902356/build/pcrec"
sb = _sb.find("capability"); diff = []; n = 0; ident = 0; ref = 0
with tempfile.TemporaryDirectory(dir="/var/tmp/b101scratch") as tmp:
    for p in sb.patterns:
        text = sb.pattern_bytes(p.name); fs = "free-spacing" in _cap.pattern_requires(p)
        for form in PI.FORMS:
            t = text if form == "plain" else _rec.whole_subject_text(text, fs)
            a = PI.emit(B, "--pattern", ["--features", "all"], t, tmp + "/a")
            b = PI.emit(B, "--pattern", ["--features", "all", "-fno-req-byte"], t, tmp + "/b")
            n += 1
            if (a is None) != (b is None): diff.append((p.name, form, a is None, b is None))
            elif a is None: ref += 1
            elif PI.program_sha256_of_text(a) == PI.program_sha256_of_text(b): ident += 1
print("rows", n, "refused-both", ref, "program-identical", ident, "refusal movers", diff)
