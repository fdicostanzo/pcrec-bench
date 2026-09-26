"""docs/dev/measurements/probe_b101_twin_stamps.py -- [B101] (lane
b101repin, 2026-09-26): the PRE-WINDOW FACTS for the [OPT-REQBYTE] twin
(inbox I-111): I-111's twelve landing-bar patterns (+ router-prefix-order),
capability@0.1, the plain form both regimes compile (search_short and
throughput), under `pcrec-auto`'s flags (`--features all`) at the pin
02902356, DEFAULT vs `-fno-req-byte` (the `pcrec-auto-noreqbyte` arm), and
the ce658cb7 default for context. Per arm: RX_REQ_WHY / _REQ_BYTE /
_REQ_RUN / _DFA_PREFILTER / _DFA_PREFILTER_OFFSETS / _ENGINE / _ENGINE_SEL
by value, the v2 program_sha256, and whether the two 02902356 arms are
program-identical. Compile-only, no gcc, no timing. From the repo root:

    python3 docs/dev/measurements/probe_b101_twin_stamps.py

Archived output: docs/dev/measurements/2026-09-26-b101-twin-stamps.txt.
"""
import os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI                          # noqa: E402
from pcrecbench import subbench as _sb                 # noqa: E402

B = "/home/duxevents/pcrec-bench/build/pcrec-%s/build/pcrec"
CELLS = [  # (pattern, regimes, I-111 class)
    ("wild-secrets-username-password-pair", "thr", "IMPROVE"),
    ("wild-logparse-winpath-grok", "thr", "IMPROVE"),
    ("tag-depth3-bound", "thr", "IMPROVE"),
    ("dup-param-detect", "thr", "IMPROVE"),
    ("tag-pair-match", "thr", "IMPROVE"),
    ("floor-byte", "thr+srch", "DO-NOT-REGRESS"),
    ("float-literal-bound", "thr", "DO-NOT-REGRESS"),
    ("nested-comment-rec", "thr", "DO-NOT-REGRESS"),
    ("wild-secrets-github-pat", "thr", "DO-NOT-REGRESS"),
    ("wild-validator-uuid-grok", "thr", "DO-NOT-REGRESS"),
    ("router-prefix-order", "thr", "TIMED (not a control)"),
]
KEYS = ("ENGINE", "ENGINE_SEL", "REQ_WHY", "REQ_BYTE", "REQ_RUN",
        "DFA_PREFILTER", "DFA_PREFILTER_OFFSETS")
STAMP = re.compile(r'^#define RX_(%s) "([^"]*)"$' % "|".join(KEYS), re.M)
BASE = ["--features", "all"]
ARMS = [("ce658cb7", "default", BASE), ("02902356", "default", BASE),
        ("02902356", "noreqbyte", BASE + ["-fno-req-byte"])]

sb = _sb.find("capability")
print("pattern\tcells\tclass\tpin\tarm\t" + "\t".join(k.lower() for k in KEYS)
      + "\tv2_sha")
with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR", "/var/tmp")) as tmp:
    for name, regimes, cls in CELLS:
        pat = sb.pattern_bytes(name)
        shas = {}
        for pin, arm, flags in ARMS:
            t = PI.emit(B % pin, "--pattern", flags, pat, os.path.join(tmp, pin + arm))
            st = dict(STAMP.findall(t or ""))
            sha = PI.program_sha256_of_text(t) if t else "REFUSED"
            shas[(pin, arm)] = sha
            print("\t".join([name, regimes, cls, pin, arm]
                            + [st.get(k, "-") for k in KEYS] + [sha[:16]]))
        same = shas[("02902356", "default")] == shas[("02902356", "noreqbyte")]
        print("# %s: 02902356 default vs -fno-req-byte program-%s"
              % (name, "IDENTICAL" if same else "DIFFERENT"))
