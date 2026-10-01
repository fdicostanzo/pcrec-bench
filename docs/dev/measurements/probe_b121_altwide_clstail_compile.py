"""docs/dev/measurements/probe_b121_altwide_clstail_compile.py -- [B121]
altwide@0.3 prep: a COMPILE-ONLY (no timing) check of the six new
class-tail patterns against the real pinned pcrec at fc719ca4, under
auto and forced-vm, grounding NOTES.md's P19-P22 predictions in real
facts rather than a blind guess (the same discipline P9-P18 cite real
pattern_facts/oracle numbers for). Prints engine selection, dfa_prefilter,
emit_bytes/emit_code_bytes, and refusal diagnostics where refused."""
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.getcwd())
from pcrecbench import subbench as _sb

B = "/home/duxevents/pcrec-bench/build/pcrec-fc719ca4/build/pcrec"
C_ENV = dict(os.environ, LC_ALL="C", LANG="C")
STAMP_RE = re.compile(r'#define (RX_\w+) "?([^"\n]*)"?')


def compile_one(flags, text, workdir):
    out = os.path.join(workdir, "a.c")
    for p in (out, out[:-2] + ".h"):
        if os.path.exists(p):
            os.unlink(p)
    argv = [B, "-p", "rx"] + flags + ["-o", out, "--pattern", bytes(text)]
    r = subprocess.run(argv, capture_output=True, env=C_ENV, timeout=600)
    if r.returncode != 0:
        return None, r.stderr.decode("utf-8", "replace").strip()
    with open(out, encoding="utf-8") as fh:
        return fh.read(), None


def main():
    sb = _sb.find("altwide")
    names = ["clsa-64", "clsa-256", "clsa-1024",
             "clsd-64", "clsd-256", "clsd-1024"]
    configs = {
        "auto": ["--features", "all"],
        "vm":   ["--features", "all", "--engine=vm"],
    }
    with tempfile.TemporaryDirectory(dir="/var/tmp") as tmp:
        for name in names:
            text = sb.pattern_bytes(name)
            for cname, flags in configs.items():
                c, err = compile_one(flags, text, tmp)
                if c is None:
                    print("%s/%s: REFUSED (%s)" % (name, cname, err))
                    continue
                stamps = dict(STAMP_RE.findall(c))
                interesting = {k: v for k, v in stamps.items()
                               if k in ("RX_ENGINE", "RX_ENGINE_SEL",
                                        "RX_DFA_PREFILTER", "RX_DFA_TABLE",
                                        "RX_VM_ALT_ISLANDS",
                                        "RX_VM_ENTRY_SHAPE")}
                print("%s/%s: OK %s" % (name, cname, interesting))


if __name__ == "__main__":
    main()
