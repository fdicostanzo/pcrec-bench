#!/usr/bin/env python3
"""gen_streams.py -- the F1 segment streams (docs/design/unusual_set_v1.md 4.1).

    python3 -I bench/unusual/gen_streams.py          # write streams/ + calls/ + manifest_streams.tsv
    python3 -I bench/unusual/gen_streams.py --check

A stream is a subject (filler pattern text between `(?{ ... })` C segments,
segment sizes log-uniform 20 B - 5 KB) plus a CALL LIST: one call per segment
at the segment's start offset, the access pattern of the compiler's scanner.

  streams/<id>.bin           the subject
  calls/<id>.tsv             header + one row per call:
                             call_id  offset  length  segment_bytes  binding_id
                             offset/length are absolute, in the subject;
                             `length` = `segment_bytes` = the segment's declared
                             byte span (the throughput DENOMINATOR is the sum of
                             segment_bytes, never the subject size: the filler
                             is never scanned); binding_id is `-` (cscan has no
                             caller variables)
  manifest_streams.tsv       id len sha256 description periodic calls
                             segment_bytes calls_sha256 local_refusals

About 1 % of segments carry a LOCAL refusal (a raw newline inside a string or
character literal): the call answers `n` and its damage is confined to its own
segment, because every call is \\G-anchored at its own start.

seg-s 256 calls, seg-l 4096 calls. Seeds are constants below.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import subjgen  # noqa: E402
import unusual_text as T  # noqa: E402

STREAMS = [("seg-s", 20261027, 256), ("seg-l", 20261028, 4096)]
HEAD = "id\tlen\tsha256\tdescription\tperiodic\tcalls\tsegment_bytes\tcalls_sha256\tlocal_refusals\n"
CALLS_HEAD = "call_id\toffset\tlength\tsegment_bytes\tbinding_id\n"


def build(seed, n):
    data, calls = T.segment_stream(seed, n)
    text = CALLS_HEAD + "".join("%d\t%d\t%d\t%d\t-\n" % (i, off, ln, ln) for i, (off, ln, _r) in enumerate(calls))
    return data, calls, text.encode("ascii")


def main(argv):
    check = "--check" in argv
    os.makedirs(os.path.join(HERE, "streams"), exist_ok=True)
    os.makedirs(os.path.join(HERE, "calls"), exist_ok=True)
    out = [HEAD]
    bad = 0
    for sid, seed, n in STREAMS:
        data, calls, ctext = build(seed, n)
        segb = sum(ln for _o, ln, _r in calls)
        refused = sum(1 for _o, _l, r in calls if r)
        out.append("%s\t%d\t%s\tF1 segment stream: %d calls, filler between C (?{ }) segments of 20 B-5 KB, %d local refusals\t%s\t%d\t%d\t%s\t%d\n"
                   % (sid, len(data), subjgen.sha(data), n, refused, subjgen.sha(data) and __import__("pcrecbench.periodic", fromlist=["x"]).periodic_field(data),
                      n, segb, subjgen.sha(ctext), refused))
        for path, blob in ((os.path.join(HERE, "streams", sid + ".bin"), data), (os.path.join(HERE, "calls", sid + ".tsv"), ctext)):
            if check:
                if os.path.exists(path) and open(path, "rb").read() != blob:
                    sys.stderr.write("DIFF %s\n" % path)
                    bad += 1
            else:
                with open(path, "wb") as f:
                    f.write(blob)
    text = "".join(out)
    mpath = os.path.join(HERE, "manifest_streams.tsv")
    if check:
        have = open(mpath).read() if os.path.exists(mpath) else None
        if have != text:
            sys.stderr.write("DIFF manifest_streams.tsv\n")
            bad += 1
        print("manifest_streams.tsv: %d stream(s), %d difference(s)" % (len(STREAMS), bad))
        return 1 if bad else 0
    with open(mpath, "w") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
