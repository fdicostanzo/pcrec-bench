"""2026-10-27-b148l4-oseg-preflight.py -- [B148] L4, the O(segment) PRE-FLIGHT
(docs/design/unusual_set_v1.md 7.1; r9 C4).

Question: does a NO-MATCH call of the call-stream regime cost O(segment) on
every engine that runs a stream, or does it grow with the REST of the subject
(the engine is handed the subject from the call's offset to its end)? `\\G`
at a start offset may not bound an engine's scan: an engine that does not
treat `\\G` as an anchor retries at every later start position.

Method: one call, at offset 0, over a REAL local-refusal segment of
bench/unusual's seg-s stream (call 54, 60 B, and call 14, 333 B -- both `n`
under the oracle), followed by a filler tail of T bytes dense in `(` (a C call line, never
`(?{`) -- every `(` a start an unanchored engine must try -- at
T = 64 KiB and T = 640 KiB (the 10x the note asks for). Each engine through
its REAL adapter (`--mode calls`, the stream's own pattern: `cscan` for
libpcre2, `cscan-onig` for pcrec and Oniguruma), ITERS replays per trial,
TRIALS trials, the per-call median. PASS = the 640 KiB tail costs < 2x the
64 KiB one (an O(tail) scan reads ~10x). Every answer is checked `n`.

CONTROL (the measurement can see an O(tail) scan): the same probe on
pcre2-interp with `\\G` deleted from cscan -- an unanchored search that must
try every later start -- must read >= 5x.

Engines with no stream pattern that compiles at v0.1 (re2, rust,
vectorscan-block-som: no `\\G`, no recursion, no DEFINE) have nothing to
pre-flight; their `--mode calls` is exercised on a synthetic stream by
tools/check_calls.py, and their explicit-anchor paths are stated there.

Scratch only: no store write. Run pinned to one core:
    PYTHONPATH=. taskset -c 11 python3 docs/dev/measurements/2026-10-27-b148l4-oseg-preflight.py OUTDIR
"""
import hashlib
import os
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad, subbench as _sbm  # noqa: E402

CALLS = (54, 14)
TAILS = (64 * 1024, 640 * 1024)
ITERS = 2000
TRIALS = 5
FILLER = b"f(x); g(y) + (z) * h(w);\n"
ENGINES = (("pcre2-interp", "cscan"), ("pcre2-jit", "cscan"),
           ("pcrec-auto", "cscan-onig"), ("pcrec-vm", "cscan-onig"),
           ("onig-default", "cscan-onig"))


def segment(sb, call_id):
    buf = sb.subject_bytes("seg-s")
    for line in open(os.path.join(sb.root, "calls", "seg-s.tsv")).read().splitlines()[1:]:
        c = line.split("\t")
        if int(c[0]) == call_id:
            off, ln = int(c[1]), int(c[2])
            return buf[off:off + ln]
    raise SystemExit("no call %d" % call_id)


def stream(out, name, seg, tail):
    body = seg + (FILLER * (tail // len(FILLER) + 1))[:tail]
    p = os.path.join(out, name + ".bin")
    with open(p, "wb") as f:
        f.write(body)
    c = os.path.join(out, name + ".tsv")
    with open(c, "w") as f:
        f.write("call_id\toffset\tlength\tsegment_bytes\tbinding_id\n0\t0\t%d\t%d\t-\n"
                % (len(seg), len(seg)))
    s = _sbm.Subject(name, len(body), hashlib.sha256(body).hexdigest(), "preflight",
                     "no", p, "stream")
    s.calls_path, s.calls, s.segment_bytes = c, 1, len(seg)
    return s


def per_call(ad, h, s):
    by_trial, _i, _n = ad.measure(h, "call-stream", [s], ITERS, TRIALS, timeout=600)
    secs, toks = [], set()
    for rows in by_trial:
        r = rows[0]
        if r.stream is None or r.stream["nomatch"] != 1:
            raise SystemExit("%s: not one no-match call: %r %r" % (s.subject_id, r.answer, r.stream))
        secs.append(r.seconds / r.iters)
    return statistics.median(secs)


def main(out):
    os.makedirs(out, exist_ok=True)
    sb = _sbm.find("unusual")
    print("# O(segment) pre-flight, per-call median ns, %d replays x %d trials; load %s"
          % (ITERS, TRIALS, open("/proc/loadavg").read().split()[:3]))
    print("engine\tpattern\tcall\tseg_B\tt64k_ns\tt640k_ns\tratio\tverdict")
    rows = list(ENGINES) + [("pcre2-interp", "cscan-noG")]
    for t, pid in rows:
        ad, _ = _ad.resolve(t)
        work = os.path.join(out, "w-" + t)
        ad.prepare(t, work)
        pat = sb.pattern_bytes("cscan") if pid == "cscan-noG" else sb.pattern_bytes(pid)
        if pid == "cscan-noG":
            pat = pat.replace(b"\\G ", b"", 1)
            assert b"\\G" not in pat
        cp = ad.compile(t, pid, pat, {}, 1, work)
        h = cp.forms["plain"].handle
        for cid in CALLS:
            seg = segment(sb, cid)
            ns = []
            for tail in TAILS:
                s = stream(out, "pf-%s-%d-%d" % (t, cid, tail), seg, tail)
                ns.append(per_call(ad, h, s) * 1e9)
            ratio = ns[1] / ns[0]
            if pid == "cscan-noG":
                verdict = "CONTROL-SEES-O(tail)" if ratio >= 5 else "CONTROL-BLIND"
            else:
                verdict = "O(segment)" if ratio < 2 else "GROWS-WITH-TAIL"
            print("%s\t%s\t%d\t%d\t%.0f\t%.0f\t%.2f\t%s"
                  % (t, pid, cid, len(seg), ns[0], ns[1], ratio, verdict))
            sys.stdout.flush()


if __name__ == "__main__":
    main(sys.argv[1])
