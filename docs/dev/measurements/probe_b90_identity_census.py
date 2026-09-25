"""docs/dev/measurements/probe_b90_identity_census.py -- [B90]/[B88] (lane
b90repin, 2026-09-25): the COMPILE-ONLY program-identity census over
bench/capability@0.1 at five pcrec pins (25b1984f 8d716693 b1885a83
6ef76820 ce658cb7), 3 configs (auto-caps, auto-nocaps, vm-caps; vm-in-caps
is compile-identical to vm-caps) x 64 patterns x 2 forms, every consecutive
pair judged under BOTH normalizations of tools/program_identity.py (v1
`normalize_pair`, v2 `program_sha256_of_text`), plus the RX_REQ_WHY /
RX_VM_FRAMELESS / RX_ENGINE / RX_REQ_BYTE stamps. Emits WITHOUT -fcomments
(program_identity.emit, the census's own path). Run from the repo root:

    python3 docs/dev/measurements/probe_b90_identity_census.py OUT.tsv

No timing, no gcc: pcrec emits only (~1,900 emits, one core, ~6 min).
Archived output: docs/dev/measurements/2026-09-25-b90-identity-census.txt.
"""
import hashlib, os, re, sys, tempfile
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import program_identity as PI
from pcrecbench import subbench as _sb
from pcrecbench import record as _rec
from pcrecbench import capability as _cap

OUT = sys.argv[1]
PINS = ["25b1984f", "8d716693", "b1885a83", "6ef76820", "ce658cb7"]
PAIRS = list(zip(PINS, PINS[1:]))
CFGS = {"auto-caps-simdna": ["--features", "all"],
        "auto-nocaps-simdna": ["--features", "all", "--no-captures"],
        "vm-caps-simdna": ["--features", "all", "--engine=vm"]}
bins = {p: "/home/duxevents/pcrec-bench/build/pcrec-%s/build/pcrec" % p for p in PINS}
sb = _sb.find("capability")
texts = {}
cache = {}
stamp = re.compile(r'^#define RX_(REQ_WHY|VM_FRAMELESS|ENGINE|REQ_BYTE) (.*)$', re.M)
with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as tmp:
    shapes = {p: PI._cli_shape(b, tmp) for p, b in bins.items()}
    rows = []
    for cfg, flags in CFGS.items():
        for p in sb.patterns:
            text = sb.pattern_bytes(p.name)
            fs = "free-spacing" in _cap.pattern_requires(p)
            for form in PI.FORMS:
                ptext = text if form == "plain" else _rec.whole_subject_text(text, fs)
                got = {}
                for pin in PINS:
                    got[pin] = PI.emit(bins[pin], shapes[pin], flags, ptext,
                                       os.path.join(tmp, pin))
                for old, new in PAIRS:
                    a, b = got[old], got[new]
                    if a is None or b is None:
                        v1 = v2 = ("refused-both" if a is None and b is None
                                   else "refused-old" if a is None else "refused-new")
                    else:
                        na, nb, _ = PI.normalize_pair(a, b)
                        v1 = "identical" if na == nb else "changed"
                        v2 = ("identical" if PI.program_sha256_of_text(a)
                              == PI.program_sha256_of_text(b) else "changed")
                    st = {}
                    for side, t in (("o", a), ("n", b)):
                        d = dict(stamp.findall(t or ""))
                        st[side] = d
                    rows.append([old, new, cfg, p.name, form, v1, v2,
                                 st["o"].get("REQ_WHY", "-"), st["n"].get("REQ_WHY", "-"),
                                 st["n"].get("VM_FRAMELESS", "-"),
                                 st["n"].get("ENGINE", "-"),
                                 PI.program_sha256_of_text(b) if b else "-"])
                print(cfg, p.name, form, file=sys.stderr, flush=True)
with open(OUT, "w") as fh:
    fh.write("old\tnew\tconfig\tpattern_id\tform\tv1\tv2\treq_why_old\treq_why_new\tframeless_new\tengine_new\tv2_sha_new\n")
    for r in rows:
        fh.write("\t".join(r) + "\n")
print("DONE rows=%d" % len(rows))
