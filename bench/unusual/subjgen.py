"""subjgen.py -- the one write/--check routine of bench/unusual's three subject
generators (short, throughput, streams): each hands over (id, bytes,
description) rows; this writes the files into a gitignored directory and the
manifest (id, len, sha256, description, periodic) beside the generator, or
under --check regenerates in memory and diffs the committed manifest
(and, where the files exist on disk, their bytes).
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
from pcrecbench.periodic import periodic_field  # noqa: E402

HEADER = "id\tlen\tsha256\tdescription\tperiodic\n"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def manifest_text(rows):
    out = [HEADER]
    for sid, data, desc in rows:
        assert "\t" not in desc and "\n" not in desc, sid
        out.append("%s\t%d\t%s\t%s\t%s\n" % (sid, len(data), sha(data), desc, periodic_field(data)))
    return "".join(out)


def run(rows, outdir, manifest, check, ext=".bin"):
    """rows: iterable of (id, bytes, desc), consumed ONCE (a generator is fine
    for the multi-megabyte sets: the bytes of a row are dropped after it is
    written and hashed)."""
    os.makedirs(outdir, exist_ok=True)
    lines = [HEADER]
    bad = 0
    for sid, data, desc in rows:
        assert "\t" not in desc and "\n" not in desc, sid
        lines.append("%s\t%d\t%s\t%s\t%s\n" % (sid, len(data), sha(data), desc, periodic_field(data)))
        path = os.path.join(outdir, sid + ext)
        if check:
            if os.path.exists(path) and open(path, "rb").read() != data:
                sys.stderr.write("DIFF subject file %s\n" % path)
                bad += 1
        else:
            with open(path, "wb") as f:
                f.write(data)
    text = "".join(lines)
    if check:
        have = open(manifest, "r", encoding="utf-8").read() if os.path.exists(manifest) else None
        if have != text:
            sys.stderr.write("DIFF manifest %s\n" % manifest)
            bad += 1
        print("%s: %d subject(s), %d difference(s)" % (os.path.basename(manifest), len(lines) - 1, bad))
        return 1 if bad else 0
    with open(manifest, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d subjects, %s" % (len(lines) - 1, manifest))
    return 0
