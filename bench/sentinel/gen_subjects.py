#!/usr/bin/env python3
"""gen_subjects.py -- the SENTINEL set's short subjects: capability@0.2's own
75 typed subjects, regenerated through capability's builder (bench/capability/
gen_subjects.py `build()`), so the bytes, ids and manifest rows are IDENTICAL
by construction. `subjects/` is gitignored; `manifest.tsv` is committed and is
byte-identical to capability's.

    python3 bench/sentinel/gen_subjects.py            # write subjects/ + manifest.tsv
    python3 bench/sentinel/gen_subjects.py --check    # re-derive, diff the manifest
"""
import hashlib
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
CAP = os.path.join(os.path.dirname(HERE), "capability")
sys.path.insert(0, CAP)

spec = importlib.util.spec_from_file_location("cap_gen_subjects", os.path.join(CAP, "gen_subjects.py"))
cap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cap)

OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")


def main():
    check = "--check" in sys.argv
    subjects = cap.build()
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, body in subjects:
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            cap.ct.periodic_field(body)))
    text = "\n".join(rows) + "\n"
    if check:
        have = open(MANIFEST, encoding="utf-8").read()
        capm = open(os.path.join(CAP, "manifest.tsv"), encoding="utf-8").read()
        if have != text or have != capm:
            print("gen_subjects --check: manifest.tsv DRIFT (vs derived: %s, vs capability's: %s)"
                  % (have != text, have != capm))
            return 1
        print("gen_subjects --check: OK (%d subjects)" % len(subjects))
        return 0
    os.makedirs(OUT, exist_ok=True)
    for sid, _d, body in subjects:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write(text)
    print("gen_subjects: %d subjects -> %s" % (len(subjects), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
