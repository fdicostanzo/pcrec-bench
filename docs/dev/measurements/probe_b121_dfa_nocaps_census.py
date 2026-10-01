"""docs/dev/measurements/probe_b121_dfa_nocaps_census.py -- [B121], inbox
I-125 Q2/Q3: a compile-only census (NO timing) at pin fc719ca4 deciding the
real REQUIRES-token population for three CANDIDATE new testees --
`pcrec-vm-nocaps` (--engine=vm --no-captures), `pcrec-dfa` (--engine=dfa,
captures on), `pcrec-dfa-nocaps` (--engine=dfa --no-captures) -- against
bench/capability@0.1 (64 patterns x 2 forms) and bench/syntax@0.1 (95
patterns, plain form only: the set has no whole-subject form), beside the
pcrec-auto baseline for contrast. Reuses tools/program_identity.py's own
`emit()` argv shape (never a re-typed escaping rule) but also captures
stderr, which that module discards, so a refusal's own diagnostic text is
in the archive. Run at `nice -n 19`, single process, no -j (lane rule: no
timing slot in this window). Archived result:
2026-10-01-b121-dfa-nocaps-census.txt."""
import os, sys, subprocess, tempfile

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI
from pcrecbench import subbench as _sb, record as _rec, capability as _cap

B = "/home/duxevents/pcrec-bench/build/pcrec-fc719ca4/build/pcrec"
C_ENV = dict(os.environ, LC_ALL="C", LANG="C")

CANDIDATES = {
    "pcrec-auto":        ["--features", "all"],
    "pcrec-vm-nocaps":   ["--features", "all", "--engine=vm", "--no-captures"],
    "pcrec-dfa":         ["--features", "all", "--engine=dfa"],
    "pcrec-dfa-nocaps":  ["--features", "all", "--engine=dfa", "--no-captures"],
}


def try_compile(flags, pattern_bytes, workdir):
    """Same argv shape as PI.emit (binary, -p rx, flags, -o OUT, --pattern,
    <raw bytes>), but returns (ok, stderr-text) instead of discarding
    stderr on a refusal."""
    out = os.path.join(workdir, "a.c")
    for p in (out, out[:-2] + ".h"):
        if os.path.exists(p):
            os.unlink(p)
    argv = [B, "-p", "rx"] + list(flags) + ["-o", out, "--pattern",
                                              bytes(pattern_bytes)]
    r = subprocess.run(argv, capture_output=True, env=C_ENV, timeout=600)
    err = r.stderr.decode("utf-8", "replace").strip()
    return (r.returncode == 0), err


def census(sb_name, forms):
    sb = _sb.find(sb_name)
    print("== %s: %d patterns x %d form(s) ==" % (sb_name, len(sb.patterns),
                                                     len(forms)))
    n_ok = {c: 0 for c in CANDIDATES}
    n_tot = 0
    with tempfile.TemporaryDirectory(dir="/var/tmp") as tmp:
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            try:
                fs = "free-spacing" in _cap.pattern_requires(p)
            except Exception:
                fs = False
            for form in forms:
                t = text if form == "plain" else _rec.whole_subject_text(text, fs)
                n_tot += 1
                row = []
                for cand, flags in CANDIDATES.items():
                    ok, err = try_compile(flags, t, tmp)
                    if ok:
                        n_ok[cand] += 1
                    row.append("%s=%s%s" % (cand, "OK" if ok else "REFUSED",
                                             "" if ok else (" (%s)" % err)))
                print("%s\t%s\t%s" % (p.name, form, " | ".join(row)))
    print("-- %s totals (of %d cells): %s --"
          % (sb_name, n_tot, ", ".join("%s=%d" % (c, n_ok[c])
                                        for c in CANDIDATES)))


if __name__ == "__main__":
    census("capability", ("plain", "whole-subject"))
    census("syntax", ("plain",))
