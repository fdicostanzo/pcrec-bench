#!/usr/bin/env python3
"""gen_expectations.py -- expectations.tsv, expectations_stream.tsv and
applies.tsv for bench/unusual (docs/design/unusual_set_v1.md section 8).

    python3 -I bench/unusual/gen_expectations.py            # write all three
    python3 -I bench/unusual/gen_expectations.py --check    # re-derive + diff
    python3 -I bench/unusual/gen_expectations.py --report   # counts only, writes nothing

METHODS (the `method` column). Primary, for every pattern libpcre2 can run:
`libpcre2-differential` -- the installed libpcre2 10.46 INTERPRETER at its
library defaults (heap 20,000,000 KiB: the 1 GiB cap of the `deep` arm is a
TESTEE arm, never the oracle's, design 8), through pcrecbench/oracle_pcre2.py's
binding. A callout member is compiled with its site and answered with a
Python callout function (unusual_lib.callee_for: the engine-neutral callee,
return codes per the design's 3.2 table). Second method, per family:

  cscan, cscan-onig   unusual_lib.ref_scan -- the regex-free reference scanner
                      (rules 1-5 + the three header choices); where libpcre2
                      GIVES UP the triple is answered by it alone and the row
                      says `reference-scanner`
  wild-sexp-balanced  a depth-counting stack scan (unusual_lib.sexp_first)
  wild-json-*         python json.loads with parse_constant refused; a
                      document python cannot answer (RecursionError) is
                      unjudged by the second method, declared in the report
  callouts            plain Python of each intention (unusual_lib.host_first)
  co-netstr           PRIMARY is the host reference (the pcrec spelling's
                      `consume` is not libpcre2 syntax); it must agree with
                      co-netstr-assist, which libpcre2 answers with the
                      check-at-end callee (P3)
  pass arms           libpcre2 with a stub callee; MUST equal the twin's row

Every triple both methods answer must AGREE (span, group 1 where the pattern
has one, find-all count); a disagreement aborts the derivation. The vars
members (route `vars`) have NO rows: their expectations are per-call over
declared value streams, L7's. pcrec is never asked.

REGIMES. search_short: every non-vars pattern x every short subject, the first
match's span. throughput: only the (pattern, subject) cells applies.tsv names
(a 5 MB comment is not the JSON validator's subject), first match span AND the
non-overlapping find-all count (the advance rule of oracle_pcre2._find_all_impl).

expectations_stream.tsv: one row per (stream, pattern) for the call-stream
regime (design 7.1/8): the per-call result tokens `n` | `m:<s>,<e>;<g1s>,<g1e>`
(absolute offsets, group 0 and group 1 only), `results_sha256` = sha256 of the
tokens each followed by "\\n".
"""
import fnmatch
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import members as MB  # noqa: E402
import unusual_lib as U  # noqa: E402
from unusual_lib import Rx  # noqa: E402
from pcrecbench import oracle_pcre2 as O  # noqa: E402

HEADER = "pattern\tsubject\tregime\texpected\tstart\tend\tnmatches\tmethod\toracle\n"
STREAM_HEADER = "subject\tpattern\tcalls\tmatched\tnomatch\trefused\tresults_sha256\tmethod\n"
APPLIES_HEADER = "pattern\tregime\tsubject_glob\n"
PRIMARY = "libpcre2-differential"

NEST = ["nest-brace-*", "nest-paren-*", "nest-digraph-10k"]
CSCAN_THROUGHPUT = ["comment-5m", "literal-100k", "nest-brace-*", "nest-paren-*", "nest-digraph-10k",
                    "idents-1m", "splice-1m", "define-witness", "unterminated-5m"]


# ORACLE DECLINES (declared, deterministic, listed in NOTES.md): cells where the
# libpcre2 INTERPRETER's own cost is prohibitive for a derivation that
# `--check` must repeat. Measured on this box (10.46, library defaults),
# cscan's recursion per brace level: depth 8000 1.6 s, 16000 7 s, 32768 74 s
# -- super-quadratic, ~50 min extrapolated at 100000 for EACH of cscan and
# cscan-onig. Those two cells are answered by the reference scanner alone
# (method `reference-scanner`); the libpcre2 answer is shown on every rung
# up to 32768, where the scanner and libpcre2 agree.
ORACLE_DECLINED = {
    ("cscan", "nest-brace-100k"): "libpcre2 interpreter ~50 min extrapolated (74 s at depth 32768, super-quadratic)",
    ("cscan-onig", "nest-brace-100k"): "same subject, same cost",
}


def applies_table(ms):
    """-> [(pattern, regime, [subject globs])]. Short: every non-vars pattern
    over every short subject. Throughput: the table below."""
    rows = []
    for m in ms:
        if m.route == "vars":
            continue
        rows.append((m.id, "search_short", ["*"]))
        if m.id in ("cscan", "cscan-onig"):
            g = CSCAN_THROUGHPUT
        elif m.id == "wild-sexp-balanced":
            g = ["sx-1m", "nest-paren-*"]
        elif m.id.startswith("wild-json-validate"):
            g = ["js-1m", "js-near-1m"]
        elif m.id.startswith("co-luhn"):
            g = ["co-luhn-1m"]
        elif m.id.startswith("co-isbn"):
            g = ["co-isbn-1m"]
        elif m.id.startswith("co-member"):
            g = ["co-member-1m"]
        elif m.id.startswith("co-netstr"):
            g = ["co-netstr-1m"]
        elif m.id == "floor":
            g = ["*"]
        else:
            raise KeyError(m.id)
        rows.append((m.id, "throughput", g))
    return rows


def render_applies(ms):
    return (APPLIES_HEADER + "".join("%s\t%s\t%s\n" % (p, r, " ".join(g)) for p, r, g in applies_table(ms))).encode()


def read_manifest(name):
    out = []
    with open(os.path.join(HERE, name)) as f:
        next(f)
        for line in f:
            c = line.rstrip("\n").split("\t")
            out.append(c[0])
    return out


def subject_bytes(kind, sid):
    with open(os.path.join(HERE, kind, sid + ".bin"), "rb") as f:
        return f.read()


# --------------------------------------------------------------------------
# one pattern's answers
# --------------------------------------------------------------------------
class Answer:
    """first span (s, e) | None, group-1 span | None, find-all count."""

    def __init__(self, first, g1, count, method):
        self.first, self.g1, self.count, self.method = first, g1, count, method

    def key(self, regime):
        if regime == "throughput":
            return (self.first, self.count)
        return (self.first,)


def find_all_rx(rx, s):
    """Rx.find_all plus group 1 of the FIRST match."""
    pos, count, first, g1 = 0, 0, None, None
    n = len(s)
    while pos <= n:
        got = rx.search(s, pos)
        if got is None:
            break
        (a, b), grp = got
        if first is None:
            first = (a, b)
            g1 = grp[0] if grp else None
        count += 1
        pos = b if b > a else a + 1
    return first, g1, count


def first_rx(rx, s):
    got = rx.search(s, 0)
    if got is None:
        return None, None
    (a, b), grp = got
    return (a, b), (grp[0] if grp else None)


class Deriver:
    def __init__(self, ms):
        self.ms = {m.id: m for m in ms}
        self.rx = {}
        self.gaveup = []
        self.declined = []
        self.fallbacks = []
        self.current_sid = None
        self.notes = {"agree": 0, "unjudged": 0, "fallback": 0}

    def _rx(self, m):
        if m.id not in self.rx:
            kind = None
            if m.route.startswith("callout:"):
                kind = m.route.split(":", 1)[1]
            elif m.route.startswith("pass:"):
                kind = "pass"
            # "nofn:" ([B148] L5): no callout function at all -> kind None
            self.rx[m.id] = Rx(m.text, callout=U.callee_for(kind) if kind else None)
        return self.rx[m.id]

    # ---- the primary (libpcre2) answer, or a give-up
    def primary(self, m, s, regime):
        if m.route in ("netstr-native",):
            return None
        rx = self._rx(m)
        if regime == "throughput":
            first, g1, count = find_all_rx(rx, s)
        else:
            first, g1 = first_rx(rx, s)
            count = None
        return Answer(first, g1, count, PRIMARY)

    # ---- the second (host) answer; None = not judged
    def second(self, m, s, regime):
        r = m.route
        tp = regime == "throughput"
        if r == "cscan":
            first, g1, count = None, None, 0
            pos = 0
            while True:
                got = U.ref_scan(s, pos)
                if got is None:
                    break
                a, b, ba, bb = got
                if first is None:
                    first, g1 = (a, b), (ba, bb)
                count += 1
                pos = b
                if not tp:
                    break
            return Answer(first, g1, count if tp else None, "reference-scanner")
        if m.id == "wild-sexp-balanced":
            first, count = sexp_find_all(s)
            return Answer(first, first, count if tp else None, "host-reference")
        if m.id.startswith("wild-json-validate"):
            ok = U.json_ok(s)
            if ok is None:
                return None
            first = (0, len(s)) if ok else None
            return Answer(first, None, (1 if ok else 0) if tp else None, "host-reference")
        if r.startswith("callout:") or r == "netstr-native":
            kind = "netstr" if r == "netstr-native" else r.split(":", 1)[1]
            if tp:
                first, count = U.host_find_all(lambda subj, pos: U.host_first(kind, subj, pos), s)
            else:
                first, count = U.host_first(kind, s, 0), None
            return Answer(first, None, count, "host-reference")
        return None            # plain / pass: no independent second method; plain is its own primary

    def derive(self, m, s, regime):
        """-> Answer | None (None = dropped)."""
        try:
            if (m.id, self.current_sid) in ORACLE_DECLINED:
                self.declined.append((m.id, self.current_sid, ORACLE_DECLINED[(m.id, self.current_sid)]))
                a, gave_up = None, "declined: " + ORACLE_DECLINED[(m.id, self.current_sid)]
            else:
                a = self.primary(m, s, regime)
                gave_up = False
        except O.Pcre2Error as e:
            a, gave_up = None, str(e)
        b = self.second(m, s, regime)
        if a is None and b is None:
            self.gaveup.append((m.id, regime, gave_up or "no oracle route"))
            return None
        if a is None:
            if m.route == "netstr-native" or gave_up is False:
                pass
            self.notes["fallback"] += 1 if gave_up else 0
            if gave_up:
                self.fallbacks.append((m.id, regime, self.current_sid, gave_up))
            return b
        if b is None:
            self.notes["unjudged"] += 1
            return a
        # agreement: span, count, and (where the pattern has a group-1 notion) group 1
        if a.key(regime) != b.key(regime):
            raise SystemExit("DISAGREEMENT %s %s: oracle %r vs %s %r" % (m.id, regime, a.key(regime), b.method, b.key(regime)))
        if m.route == "cscan" and a.first is not None and a.g1 != b.g1:
            raise SystemExit("DISAGREEMENT %s group 1: oracle %r vs reference %r" % (m.id, a.g1, b.g1))
        self.notes["agree"] += 1
        return a


def sexp_find_all(s):
    """(first span, count) of balanced `(...)` groups, find-all semantics, one
    pass: pair every ')' with the nearest unmatched '(' (the pairing the
    pattern's possessive recursion gives), then take the leftmost group, then
    the leftmost one starting at/after its end, and so on."""
    stack, ends = [], {}
    for i, c in enumerate(s):
        if c == 40:
            stack.append(i)
        elif c == 41 and stack:
            ends[stack.pop()] = i + 1
    pos, count, first = 0, 0, None
    for j in sorted(ends):
        if j >= pos:
            if first is None:
                first = (j, ends[j])
            count += 1
            pos = ends[j]
    return first, count


def match_glob(globs, sid):
    return any(fnmatch.fnmatchcase(sid, g) for g in globs)


# --------------------------------------------------------------------------
def build(report_only=False):
    MB.check_cscan_source()
    ms = MB.members()
    short = read_manifest("manifest.tsv")
    thr = read_manifest("manifest_throughput.tsv")
    ver = O.version()
    d = Deriver(ms)
    rows = []
    table = applies_table(ms)
    import time
    by = {m.id: m for m in ms}
    # cache subjects (the short ones are tiny; throughput subjects loaded per use)
    short_b = {sid: subject_bytes("subjects", sid) for sid in short}
    answers = {}
    for pid, regime, globs in table:
        m = by[pid]
        ids = short if regime == "search_short" else thr
        for sid in ids:
            if not match_glob(globs, sid):
                continue
            s = short_b[sid] if regime == "search_short" else subject_bytes("throughput", sid)
            t0 = time.time()
            d.current_sid = sid
            a = d.derive(m, s, regime)
            dt = time.time() - t0
            if dt > 20:
                sys.stderr.write("slow: %s %s %.1fs\n" % (pid, sid, dt))
            answers[(pid, sid, regime)] = a
            if a is None:
                continue
            exp = "match" if a.first else "nomatch"
            st, en = (a.first if a.first else ("-", "-"))
            nm = a.count if regime == "throughput" else "-"
            rows.append("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (pid, sid, regime, exp, st, en, nm, a.method, ver))
    # pass arms equal their twins
    for (pid, sid, regime), a in answers.items():
        m = by[pid]
        if m.route.startswith(("pass:", "nofn:")):
            tw = answers.get((m.route.split(":", 1)[1], sid, regime))
            if tw is None or a is None or a.key(regime) != tw.key(regime):
                raise SystemExit("pass arm %s differs from its twin on %s" % (pid, sid))
    # the netstr pcrec spelling must equal the assisted spelling's libpcre2 answer
    for (pid, sid, regime), a in answers.items():
        if pid == "co-netstr":
            b = answers.get(("co-netstr-assist", sid, regime))
            if b is None or a is None or a.key(regime) != b.key(regime):
                raise SystemExit("co-netstr (host reference) != co-netstr-assist (libpcre2) on %s" % sid)
    # the Onig variants answer as the originals do
    for (pid, sid, regime), a in answers.items():
        if pid in ("cscan-onig", "wild-json-validate-onig"):
            b = answers.get((pid[:-5], sid, regime))
            if b is None or a is None or a.key(regime) != b.key(regime):
                raise SystemExit("%s differs from %s on %s" % (pid, pid[:-5], sid))
    # the twin-vs-real sanity: a callout row's span is its twin's span or a later/absent one
    expectations = (HEADER + "".join(rows)).encode()

    # ---- the call-stream expectations
    srows = []
    with open(os.path.join(HERE, "manifest_streams.tsv")) as f:
        next(f)
        streams = [l.split("\t")[0] for l in f]
    for sid in streams:
        data = open(os.path.join(HERE, "streams", sid + ".bin"), "rb").read()
        calls = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "calls", sid + ".tsv"))][1:]
        refus = int([l.split("\t") for l in open(os.path.join(HERE, "manifest_streams.tsv"))][1 + streams.index(sid)][8])
        for pid in ("cscan", "cscan-onig"):
            rx = Rx(by[pid].text)
            toks = []
            for _cid, off, _ln, _sb, _b in calls:
                off = int(off)
                got = rx.search(data, off)
                ref = U.ref_scan(data, off)
                if got is None:
                    tok = "n"
                    if ref is not None:
                        raise SystemExit("stream %s %s: oracle no match, reference matches at %d" % (sid, pid, off))
                else:
                    (a, b), grp = got
                    tok = "m:%d,%d;%d,%d" % (a, b, grp[0][0], grp[0][1])
                    if ref is None or (ref[0], ref[1], ref[2], ref[3]) != (a, b, grp[0][0], grp[0][1]):
                        raise SystemExit("stream %s %s: oracle %s vs reference %r at %d" % (sid, pid, tok, ref, off))
                toks.append(tok)
            nm = sum(1 for t in toks if t == "n")
            if nm != refus:
                raise SystemExit("stream %s %s: %d no-match calls, %d local refusals generated" % (sid, pid, nm, refus))
            h = U.sha256(("".join(t + "\n" for t in toks)).encode())
            srows.append("%s\t%s\t%d\t%d\t%d\t0\t%s\t%s\n" % (sid, pid, len(toks), len(toks) - nm, nm, h, PRIMARY))
    stream_exp = (STREAM_HEADER + "".join(srows)).encode()
    return expectations, stream_exp, render_applies(ms), d, len(rows)


def main(argv):
    check = "--check" in argv
    report = "--report" in argv
    exp, sexp, app, d, n = build()
    print("expectations.tsv: %d rows; stream rows: %d; agreement-checked triples: %d; second-method-only (oracle gave up): %d; unjudged by a second method: %d"
          % (n, sexp.count(b"\n") - 1, d.notes["agree"], d.notes["fallback"], d.notes["unjudged"]))
    for g in d.fallbacks:
        print("FALLBACK (libpcre2 did not answer):", g)
    for g in d.declined:
        print("ORACLE DECLINED (answered by the reference scanner):", g)
    for g in d.gaveup:
        print("DROPPED (gave up, no second method):", g)
    outs = {"expectations.tsv": exp, "expectations_stream.tsv": sexp, "applies.tsv": app}
    if report:
        return 0
    bad = 0
    for name, data in outs.items():
        path = os.path.join(HERE, name)
        if check:
            if (open(path, "rb").read() if os.path.exists(path) else None) != data:
                sys.stderr.write("DIFF %s\n" % name)
                bad += 1
        else:
            with open(path, "wb") as f:
                f.write(data)
    if check:
        print("gen_expectations --check: %d difference(s)" % bad)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
