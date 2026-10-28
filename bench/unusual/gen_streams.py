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

F2 (4.2): `sqlite-bodies` is the same shape over the REAL function bodies of the
vendored SQLite amalgamation (vendor/sqlite3.c.xz, decompressed IN MEMORY, its
sha256 checked against vendor/sqlite3.c.xz.sha256 -- nothing decompressed is ever
written outside the gitignored streams/ tree). A body is located by the set's own
regex-free reference scanner (unusual_lib.ref_scan): a function opens at a
column-0 line ending in `{` (not struct/union/enum/typedef/extern) or at a lone
`{` line, and closes at the next line that is exactly `}`; the candidate segment
`(?{ <body incl. its braces> })` is KEPT iff ref_scan accepts it whole (a body
the scanner refuses is excluded and counted, never a call). Filler between
segments is the F1 filler (unusual_text.filler). `sqlite-bodies-s` is the
deterministic 1-in-16 sample (every body whose 0-based index is 0 mod 16, P14)
with its own filler seed. Every call is answered by the scanner: no local refusals.

L7 (lane b148l7) appends the five caller-VARIABLES streams of gen_vars.py to the
same manifest: a vars stream's calls are LINES (offset/length = the line, binding
id per call), `local_refusals` = the calls the variables rule REFUSES (vars.md 5),
and each stream carries a bindings table `values/<id>.tsv` (`binding_id name
value`, value = hex | UNSET | EMPTY) plus one row per (stream, member) in
`values/streams.tsv` (stream length, distinct values, distinct RESOLVED patterns
= the miss count a memoizing engine pays, refused calls, reuse order).
"""
import hashlib
import lzma
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import subjgen  # noqa: E402
import unusual_text as T  # noqa: E402
import gen_vars as GV  # noqa: E402   (L7: the caller-variables streams)

STREAMS = [("seg-s", 20261027, 256), ("seg-l", 20261028, 4096), ("sqlite-bodies", "sqlite-bodies", 0), ("sqlite-bodies-s", "sqlite-bodies-s", 0)]
HEAD = "id\tlen\tsha256\tdescription\tperiodic\tcalls\tsegment_bytes\tcalls_sha256\tlocal_refusals\n"
VALUES_HEAD = "stream\tmember\tcalls\tbindings\tdistinct_values\tdistinct_resolved\trefused\treuse\tbindings_sha256\n"
CALLS_HEAD = "call_id\toffset\tlength\tsegment_bytes\tbinding_id\n"


SQLITE_SEEDS = {"sqlite-bodies": 20261029, "sqlite-bodies-s": 20261030}
SAMPLE_EVERY = 16
_BODIES = []


def sqlite_bodies():
    """-> [segment bytes] in source order, memoised; also sets sqlite_bodies.stats."""
    if _BODIES:
        return _BODIES[0]
    import unusual_lib as U
    vend = os.path.join(HERE, "vendor")
    src = lzma.open(os.path.join(vend, "sqlite3.c.xz")).read()
    want = dict(l.rstrip("\n").split("\t") for l in open(os.path.join(vend, "sqlite3.c.xz.sha256")))
    if hashlib.sha256(src).hexdigest() != want["sqlite3_c_sha256"]:
        raise SystemExit("vendor/sqlite3.c.xz does not decompress to the pinned sqlite3.c sha256")
    lines = src.split(b"\n")
    starts, off = [], 0
    for ln in lines:
        starts.append(off)
        off += len(ln) + 1
    segs, refused, notfunc = [], 0, 0
    kw = (b"struct", b"union", b"enum", b"typedef", b"extern")
    i = 0
    while i < len(lines):
        l = lines[i]
        if l == b"{" or (l.endswith(b"{") and l[:1] and l[:1] not in b" \t#/}*{" and not l.startswith(kw)):
            j = i + 1
            while j < len(lines) and not lines[j].startswith(b"}"):
                j += 1
            if j >= len(lines):
                break
            if lines[j] != b"}":            # `};` / `} name;`: an initializer or a type, not a function
                notfunc += 1
            else:
                seg = b"(?{ " + src[starts[i] + len(l) - 1:starts[j] + 1] + b" })"
                r = U.ref_scan(seg, 0)
                if r and r[1] == len(seg):
                    segs.append(seg)
                else:
                    refused += 1
            i = j + 1
        else:
            i += 1
    sqlite_bodies.version = want["version"]
    sqlite_bodies.stats = (len(segs), refused, notfunc)
    _BODIES.append(segs)
    return segs


def build_sqlite(sid):
    rng = T.Rng(SQLITE_SEEDS[sid])
    segs = sqlite_bodies()
    if sid.endswith("-s"):
        segs = segs[::SAMPLE_EVERY]
    out = bytearray()
    calls = []
    for seg in segs:
        out += T.filler(rng)
        calls.append((len(out), len(seg), False))
        out += seg
    out += T.filler(rng)
    return bytes(out), calls


def build(seed, n):
    if isinstance(seed, str):
        data, calls = build_sqlite(seed)
    else:
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
        if isinstance(seed, str):
            nb, nref, nfn = sqlite_bodies.stats
            desc = ("F2 SQLite %s function bodies: %d calls, one (?{ body }) per body located by the reference scanner "
                    "(%d refused by it and excluded, %d non-function brace blocks)%s, %d local refusals"
                    % (sqlite_bodies.version, len(calls), nref, nfn, ", 1-in-16 sample of %d" % nb if sid.endswith("-s") else "", refused))
        else:
            desc = "F1 segment stream: %d calls, filler between C (?{ }) segments of 20 B-5 KB, %d local refusals" % (n, refused)
        out.append("%s\t%d\t%s\t%s\t%s\t%d\t%d\t%s\t%d\n"
                   % (sid, len(data), subjgen.sha(data), desc, __import__("pcrecbench.periodic", fromlist=["x"]).periodic_field(data),
                      len(calls), segb, subjgen.sha(ctext), refused))
        for path, blob in ((os.path.join(HERE, "streams", sid + ".bin"), data), (os.path.join(HERE, "calls", sid + ".tsv"), ctext)):
            # --check MATERIALIZES a missing stream (the files are generated and
            # gitignored; the harness's generic gates run this --check before
            # gen_expectations.py reads them) and compares a present one.
            if check and os.path.exists(path):
                if open(path, "rb").read() != blob:
                    sys.stderr.write("DIFF %s\n" % path)
                    bad += 1
            else:
                with open(path, "wb") as f:
                    f.write(blob)
    vrows = [VALUES_HEAD]
    os.makedirs(os.path.join(HERE, "values"), exist_ok=True)
    for st in GV.build_all():
        data, ctext, btext = st.data, st.calls_text(), st.bindings_text()
        facts = {m: st.facts(m) for m in st.members}
        refused = {f["refused"] for f in facts.values()}
        assert len(refused) == 1, (st.sid, facts)           # members sharing a stream refuse the same calls
        refused = refused.pop()
        n = len(st.calls)
        out.append("%s\t%d\t%s\tvars stream (%s): %d calls, one log line per call, %d binding(s), reuse %s, %d refused by the variables rule\t%s\t%d\t%d\t%s\t%d\n"
                   % (st.sid, len(data), subjgen.sha(data), "+".join(st.members), n, len(st.bindings), st.reuse, refused,
                      __import__("pcrecbench.periodic", fromlist=["x"]).periodic_field(data),
                      n, st.segment_bytes, subjgen.sha(ctext), refused))
        for m in st.members:
            vrows.append("%s\t%s\t%d\t%d\t%d\t%d\t%d\t%s\t%s\n"
                         % (st.sid, m, n, len(st.bindings), len({tuple(sorted(d.items(), key=lambda kv: kv[0]))
                                                                for _b, d in st.bindings}),
                            facts[m]["distinct_resolved"], facts[m]["refused"], st.reuse, subjgen.sha(btext)))
        for path, blob in ((os.path.join(HERE, "streams", st.sid + ".bin"), data),
                           (os.path.join(HERE, "calls", st.sid + ".tsv"), ctext),
                           (os.path.join(HERE, "values", st.sid + ".tsv"), btext)):
            committed = os.sep + "values" + os.sep in path
            if check and (committed or os.path.exists(path)):
                if not os.path.exists(path) or open(path, "rb").read() != blob:
                    sys.stderr.write("DIFF %s\n" % path)
                    bad += 1
            else:
                with open(path, "wb") as f:
                    f.write(blob)
    vtext = "".join(vrows)
    vpath = os.path.join(HERE, "values", "streams.tsv")
    if check:
        if (open(vpath).read() if os.path.exists(vpath) else None) != vtext:
            sys.stderr.write("DIFF values/streams.tsv\n")
            bad += 1
    else:
        with open(vpath, "w") as f:
            f.write(vtext)
    nstreams = len(STREAMS) + len(GV.STREAMS)
    text = "".join(out)
    mpath = os.path.join(HERE, "manifest_streams.tsv")
    if check:
        have = open(mpath).read() if os.path.exists(mpath) else None
        if have != text:
            sys.stderr.write("DIFF manifest_streams.tsv\n")
            bad += 1
        print("manifest_streams.tsv: %d stream(s), %d difference(s)" % (nstreams, bad))
        return 1 if bad else 0
    with open(mpath, "w") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
