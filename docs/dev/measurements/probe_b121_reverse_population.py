"""docs/dev/measurements/probe_b121_reverse_population.py -- [B121],
inbox I-125 Q3: THE REVERSE POPULATION. For every bench/capability@0.1 and
bench/syntax@0.1 pattern (plain form), compiles under `pcrec-nocaps`'s own
flags (--features all --no-captures, engine=auto) and reads the emitted
RX_ENGINE stamp; separately compiles under forced `--engine=dfa
--no-captures`. Reports every pattern where AUTO (nocaps) selected the VM
AND the forced-DFA form still compiles -- the population Q3 asks whether
a pinned `pcrec-dfa-nocaps` testee could ever beat `pcrec-nocaps` on.
Compile-only, no timing. Run at `nice -n 19`. Archived result appended to
2026-10-01-b121-dfa-nocaps-census.txt."""
import os, sys, subprocess, tempfile, re

sys.path.insert(0, os.getcwd())
from pcrecbench import subbench as _sb, record as _rec, capability as _cap

B = "/home/duxevents/pcrec-bench/build/pcrec-fc719ca4/build/pcrec"
C_ENV = dict(os.environ, LC_ALL="C", LANG="C")


def try_compile(flags, pattern_bytes, workdir):
    out = os.path.join(workdir, "a.c")
    for p in (out, out[:-2] + ".h"):
        if os.path.exists(p):
            os.unlink(p)
    argv = [B, "-p", "rx"] + list(flags) + ["-o", out, "--pattern",
                                              bytes(pattern_bytes)]
    r = subprocess.run(argv, capture_output=True, env=C_ENV, timeout=600)
    if r.returncode != 0:
        return None, r.stderr.decode("utf-8", "replace").strip()
    with open(out, encoding="utf-8") as fh:
        return fh.read(), None


ENGINE_RE = re.compile(r'#define RX_ENGINE "(\w+)"')


def census(sb_name, forms):
    sb = _sb.find(sb_name)
    hits = []
    with tempfile.TemporaryDirectory(dir="/var/tmp") as tmp:
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            try:
                fs = "free-spacing" in _cap.pattern_requires(p)
            except Exception:
                fs = False
            for form in forms:
                t = text if form == "plain" else _rec.whole_subject_text(text, fs)
                auto_c, auto_err = try_compile(
                    ["--features", "all", "--no-captures"], t, tmp)
                dfa_c, dfa_err = try_compile(
                    ["--features", "all", "--engine=dfa", "--no-captures"],
                    t, tmp)
                if auto_c is None:
                    continue
                m = ENGINE_RE.search(auto_c)
                engine = m.group(1) if m else "?"
                if engine == "vm" and dfa_c is not None:
                    hits.append((p.name, form))
                    print("  HIT %s %s: auto(nocaps)=vm, forced-dfa(nocaps)=OK"
                          % (p.name, form))
    print("-- %s: %d (pattern,form) pair(s) in the reverse population: %s --"
          % (sb_name, len(hits), hits))


if __name__ == "__main__":
    census("capability", ("plain", "whole-subject"))
    census("syntax", ("plain",))
