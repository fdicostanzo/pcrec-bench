"""docs/dev/measurements/probe_b121_dfa_nocaps_identity.py -- [B121],
I-125 Q3 follow-up: confirms the reverse-population census's "0 hits"
finding means pcrec-nocaps (auto, no-captures) and a forced-DFA
pcrec-dfa-nocaps emit the SAME PROGRAM wherever both compile on
bench/capability@0.1 + bench/syntax@0.1 (plain + whole-subject), using
tools/program_identity.py's own v2 normalization (never a re-typed
rule). Compile-only, no timing. Run at `nice -n 19`."""
import os, sys, tempfile

sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI
from pcrecbench import subbench as _sb, record as _rec, capability as _cap

B = "/home/duxevents/pcrec-bench/build/pcrec-fc719ca4/build/pcrec"


def census(sb_name, forms):
    sb = _sb.find(sb_name)
    ident = changed = refused_either = 0
    diffs = []
    with tempfile.TemporaryDirectory(dir="/var/tmp") as tmp:
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            try:
                fs = "free-spacing" in _cap.pattern_requires(p)
            except Exception:
                fs = False
            for form in forms:
                t = text if form == "plain" else _rec.whole_subject_text(text, fs)
                a = PI.emit(B, "--pattern", ["--features", "all", "--no-captures"],
                            t, tmp + "/a")
                b = PI.emit(B, "--pattern",
                            ["--features", "all", "--engine=dfa", "--no-captures"],
                            t, tmp + "/b")
                if a is None or b is None:
                    refused_either += 1
                    continue
                if PI.program_sha256_of_text(a) == PI.program_sha256_of_text(b):
                    ident += 1
                else:
                    changed += 1
                    diffs.append((p.name, form))
    print("-- %s: identical=%d changed=%d refused-either=%d --"
          % (sb_name, ident, changed, refused_either))
    if diffs:
        print("   DIFFER:", diffs)


if __name__ == "__main__":
    census("capability", ("plain", "whole-subject"))
    census("syntax", ("plain",))
