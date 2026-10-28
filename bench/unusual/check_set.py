#!/usr/bin/env python3
"""check_set.py -- bench/unusual's own checks (L3). L8's tools/check_unusual.py
is the make-check entry; this is the set-local part it will call.

    python3 -I bench/unusual/check_set.py            # fast checks (~1 min incl. the 5 MB manifests)
    python3 -I bench/unusual/check_set.py --full     # + the full expectations re-derivation (MINUTES, see NOTES.md)

Every check has a NEGATIVE arm where one is cheap (a sabotaged input must be refused).
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import members as MB  # noqa: E402
import unusual_lib as U  # noqa: E402

FAILS = []
N = [0]


def check(name, ok, detail=""):
    N[0] += 1
    if not ok:
        FAILS.append(name)
    print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  -- " + detail) if detail else ""))


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, script), *args], capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def main(argv):
    full = "--full" in argv
    # 1. derived files reproduce
    rc, out = run("gen_patterns.py", "--check")
    check("gen_patterns --check", rc == 0, out)
    for script in ("gen_subjects.py", "gen_throughput_subjects.py", "gen_streams.py"):
        rc, out = run(script, "--check")
        check(script + " --check (manifest reproduces byte for byte)", rc == 0, out.splitlines()[-1] if out else "")

    # 2. the cscan reference scanner: 76 pcrec cases = hand rule = libpcre2 = reference scanner
    g = MB.check_cscan_source()
    ms = {m.id: m for m in MB.members()}
    rx = U.Rx(ms["cscan"].text)
    rxo = U.Rx(ms["cscan-onig"].text)
    bad = 0
    for lab, subj, exp in g.C:
        b = subj.encode("latin-1")
        r, o, oo = U.ref_scan(b, 0), rx.search(b, 0), rxo.search(b, 0)
        got = None if r is None else subj[r[2]:r[3]]
        og = None if o is None else subj[o[1][0][0]:o[1][0][1]]
        ogo = None if oo is None else subj[oo[1][0][0]:oo[1][0][1]]
        if not (got == exp == og == ogo):
            bad += 1
            print("   case", lab, repr(exp), repr(got), repr(og), repr(ogo))
    check("73 start-0 cscan cases: hand rule == libpcre2 == reference scanner == Onig-variant text", bad == 0, "%d of %d bad" % (bad, len(g.C)))
    starts = [(1, "a(?{ x; })", " x; "), (0, "a(?{ x; })", None), (10, "a(?{ x; })(?{ y; })", " y; ")]
    ok = True
    for st, s, exp in starts:
        b = s.encode()
        r = U.ref_scan(b, st)
        ok &= (None if r is None else s[r[2]:r[3]]) == exp
    check("3 start-offset (\\G) cases", ok)
    # negative: a sabotaged scanner rule must disagree with the table (digraph %> treated as plain)
    b = b"(?{ x; %>)"
    check("negative: the digraph case needs the digraph rule (`(?{ x; %>)` matches)", U.ref_scan(b, 0) is not None)

    # 3. callout oracle layout + return-code table
    check("callout block layout and the +1/-1 return codes", U.selfcheck())
    luhn = U.Rx(ms["co-luhn"].text, callout=U.callee_for("luhn"))
    twin = U.Rx(ms["co-luhn-twin"].text)
    s = b"a 4111111111111112 b 4111111111111111 c"
    r1, r2 = luhn.search(s), twin.search(s)
    check("first-candidate-fails control: real answers the SECOND candidate, twin the first",
          r1 is not None and r2 is not None and r1[0][0] > r2[0][0], "%r vs %r" % (r1 and r1[0], r2 and r2[0]))

    # 4. host references agree with the oracle on every short subject (cheap)
    man = [l.split("\t")[0] for l in open(os.path.join(HERE, "manifest.tsv"))][1:]
    ndis = 0
    for sid in man:
        data = open(os.path.join(HERE, "subjects", sid + ".bin"), "rb").read()
        for pid, kind in (("co-luhn", "luhn"), ("co-isbn", "isbn"), ("co-member", "member")):
            o = U.Rx(ms[pid].text, callout=U.callee_for(kind)).search(data)
            h = U.host_first(kind, data)
            if (None if o is None else o[0]) != h:
                ndis += 1
        o = U.Rx(ms["co-netstr-assist"].text, callout=U.callee_for("netstr")).search(data)
        if (None if o is None else o[0]) != U.netstr_first(data):
            ndis += 1
        o = U.Rx(ms["wild-sexp-balanced"].text).search(data)
        if (None if o is None else o[0]) != U.sexp_first(data):
            ndis += 1
    check("callout / netstring / S-expression oracles == host references on %d short subjects" % len(man), ndis == 0, "%d disagreements" % ndis)

    # 5. expectations coverage by applies.tsv (needs the files)
    exp_path = os.path.join(HERE, "expectations.tsv")
    if os.path.exists(exp_path):
        rows = [l.rstrip("\n").split("\t") for l in open(exp_path)][1:]
        keys = {(r[0], r[1], r[2]) for r in rows}
        check("expectations.tsv has no duplicate (pattern, subject, regime)", len(keys) == len(rows))
        check("expectations_stream.tsv has 4 rows (2 streams x cscan, cscan-onig)",
              len(open(os.path.join(HERE, "expectations_stream.tsv")).read().splitlines()) == 5)
        check("no vars pattern has an expectation row (L7 owns them)", not any(r[0].startswith("va-") for r in rows))
    # 6. the F2 fetch scripts refuse by name while their tables are empty
    for script in ("fetch_sqlite.py", "fetch_kernel.py"):
        rc, out = run(script)
        check(script + " refuses by name (table empty, nothing fetched)", rc == 2 and "REFUSED" in out)
    check("F2 subjects are skipped BY NAME (skipped_subjects.tsv has the 7 ids)",
          len(open(os.path.join(HERE, "skipped_subjects.tsv")).read().splitlines()) == 8)

    if full:
        rc, out = run("gen_expectations.py", "--check")
        check("gen_expectations --check (full re-derivation incl. every agreement control)", rc == 0, out.splitlines()[0] if out else "")
    print("\n%d checks, %d failed" % (N[0], len(FAILS)))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
