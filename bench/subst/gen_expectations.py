#!/usr/bin/env python3
"""gen_expectations.py -- the substitution set's expectations, from the
libpcre2 oracle (method `libpcre2-differential`, docs/design/subst_bench_v1.md
section 4).

For every (case, subject) one row: the number of substitutions, the output's
byte length and its SHA-256 -- the figures a competitor's output must equal
(`bench/subst/NOTES.md` "The correctness gate"). They come from
`pcrecbench.oracle_pcre2.Compiled.substitute` (pcre2_substitute,
SUBSTITUTE_GLOBAL, + SUBSTITUTE_EXTENDED where the template has a case
operator or a conditional), with the template RENDERED from the case's
engine-neutral `TEMPLATE.neutral` by `pcrecbench.subst_template`. The oracle
is the libpcre2 INTERPRETER (the code is never JIT-compiled): no JIT stack,
so the -46 of design question 11 cannot arise here.

NOTHING is taken on the oracle's word alone. Each row also carries an
INDEPENDENT count of the substitutions, taken without the oracle:
  1   bytes.count of the literal
  2   the generator's planted count (and the planted paths counted as bytes)
  3   digit-run transitions via bytes.translate (no regex at all)
  4   the newline count (one date per line by construction)
  5, 5b, 6   python's `re` (another implementation of the same patterns)
  7, 7a, 7b, 7c   the generator's planted populations (wrong TLD / missing
      with no query / missing after other fields)
A disagreement between the oracle and the independent count is a FAILURE of
the set (nothing is written). And case 7's one-pass output must equal the
sequential application of 7a, 7b, 7c (their populations are disjoint): the
`control` column.

    gen_expectations.py             write expectations.tsv (acc-small always;
                                    acc-main when subjects/acc-main.log exists)
    gen_expectations.py --check     re-derive acc-small and require the
                                    committed rows to match; --full adds acc-main
                                    (needs the file; ~minutes)
"""
import argparse
import csv
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402
from pcrecbench import subst_template as st  # noqa: E402

OUT = os.path.join(HERE, "expectations.tsv")
SUBJ_DIR = os.environ.get("PCRECBENCH_SUBST_SUBJECTS",
                          os.path.join(HERE, "subjects"))
HEADER = ("case", "subject", "nsubst", "out_bytes", "out_sha256",
          "independent_nsubst", "independent_basis", "control")
SMALL, MAIN = "acc-small", "acc-main"


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_cases():
    cases = []
    for row in read_tsv(os.path.join(HERE, "cases.tsv")):
        d = os.path.join(HERE, "cases", row["dir"])
        with open(os.path.join(d, "PATTERN.rx"), "rb") as f:
            pat = f.read()
        if not pat.endswith(b"\n") or pat.count(b"\n") != 1:
            raise SystemExit("%s: PATTERN.rx must be exactly one line" % d)
        with open(os.path.join(d, "TEMPLATE.neutral"), "rb") as f:
            ir = st.parse(f.read())
        cases.append((row["case"], pat[:-1], ir))
    return cases


def planted_row(subject):
    for r in read_tsv(os.path.join(HERE, "planted.tsv")):
        if r["id"] == subject:
            return {k: int(v) for k, v in r.items() if k != "id"}
    raise SystemExit("planted.tsv has no row for %s" % subject)


DIGITS = bytes.maketrans(bytes(range(256)),
                         bytes(ord("1") if 48 <= b <= 57 else ord("0")
                               for b in range(256)))


def independent(case, data, planted):
    """-> (count, basis)."""
    if case == "1":
        return data.count(b"HTTP/1.1"), "bytes.count"
    if case == "2":
        n = sum(data.count(p.encode()) for p in
                ("/phpmyadmin/index.php", "/phpmyadmin/setup.php",
                 "/wp-admin/admin.php", "/wp-admin/install.php",
                 "/phpmyadmin/scripts.php", "/wp-admin/upgrade.php"))
        if n != planted["n_rare"]:
            raise SystemExit("case 2: planted %d != literal count %d"
                             % (planted["n_rare"], n))
        return planted["n_rare"], "planted"
    if case == "3":
        t = data.translate(DIGITS)
        return t.count(b"01") + (1 if t[:1] == b"1" else 0), "digit-run transitions"
    if case == "4":
        return data.count(b"\n"), "newline count"
    if case in ("5", "5b", "6"):
        pat = {"5": rb"\b([0-9]{1,3}\.){3}[0-9]{1,3}\b",
               "5b": rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
               "6": rb"/(blog|images|downloads|static)/"}[case]
        return sum(1 for _ in re.finditer(pat, data)), "python re"
    if case == "7a":
        return planted["n_url7_wrong"], "planted"
    if case == "7b":
        return planted["n_url7_missing_noq"], "planted"
    if case == "7c":
        return planted["n_url7_missing_q"], "planted"
    if case == "7":
        return (planted["n_url7_wrong"] + planted["n_url7_missing_noq"]
                + planted["n_url7_missing_q"]), "planted"
    raise SystemExit("no independent count for case %s" % case)


def derive(subject, data, cases):
    planted = planted_row(subject)
    rows = []
    for case, pat, ir in cases:
        ext = st.needs_extended(ir)
        bad = st.unset_refs(ir)
        if bad:
            raise SystemExit("case %s: template references optional groups "
                             "outside their guard: %r" % (case, bad))
        tpl = st.render(ir, "pcre2", extended=ext)
        n, out = oracle.compile(pat).substitute(data, tpl, extended=ext)
        sha = hashlib.sha256(out).hexdigest()
        ind, basis = independent(case, data, planted)
        if ind != n:
            raise SystemExit("case %s on %s: oracle nsubst %d != independent "
                             "%d (%s) -- the set is broken, nothing written"
                             % (case, subject, n, ind, basis))
        rows.append([case, subject, str(n), str(len(out)), sha, str(ind), basis, ""])
        del out
    # case 7's one pass == 7a, then 7b, then 7c (disjoint populations)
    cur = data
    for case, pat, ir in cases:
        if case in ("7a", "7b", "7c"):
            tpl = st.render(ir, "pcre2", extended=False)
            _n, o = oracle.compile(pat).substitute(cur, tpl)
            cur = bytes(o)
    comp = hashlib.sha256(cur).hexdigest()
    for r in rows:
        if r[0] == "7":
            if comp != r[4]:
                raise SystemExit("case 7 control: 7a+7b+7c != the one-pass 7 "
                                 "on %s" % subject)
            r[7] = "composition(7a,7b,7c)==7:ok"
    return rows


def subject_bytes(subject):
    path = os.path.join(SUBJ_DIR, subject + ".log")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    if subject == SMALL:
        import logsim
        n = int(next(r["lines"] for r in read_tsv(os.path.join(HERE, "planted.tsv"))
                     if r["id"] == SMALL))
        return b"".join(logsim.stream(n))
    return None


def fmt(rows):
    return "\n".join("\t".join(r) for r in [HEADER] + rows) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--full", action="store_true",
                    help="with --check: also re-derive acc-main (needs the file)")
    args = ap.parse_args()
    cases = load_cases()
    subjects = [SMALL] + ([MAIN] if (os.path.exists(os.path.join(SUBJ_DIR, MAIN + ".log"))
                                     and (not args.check or args.full)) else [])
    rows = []
    for sid in subjects:
        data = subject_bytes(sid)
        rows += derive(sid, data, cases)
        print("gen_expectations: %s derived (%d cases, %d B)" % (sid, len(cases), len(data)))
        del data
    if args.check:
        committed = read_tsv(OUT)
        bad = 0
        for r in rows:
            want = dict(zip(HEADER, r))
            have = next((c for c in committed
                         if c["case"] == want["case"] and c["subject"] == want["subject"]), None)
            if have != want:
                print("FAIL expectation differs: %s %s\n  committed %r\n  derived   %r"
                      % (want["case"], want["subject"], have, want))
                bad += 1
        print("gen_expectations: %d/%d rows match the committed table" % (len(rows) - bad, len(rows)))
        return 1 if bad else 0
    # keep rows of subjects not re-derived this run
    keep = []
    if os.path.exists(OUT):
        keep = [[c[h] for h in HEADER] for c in read_tsv(OUT) if c["subject"] not in subjects]
    allrows = sorted(keep + rows, key=lambda r: (r[1] != SMALL, r[0]))
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(fmt(allrows))
    print("gen_expectations: wrote %s (%d rows)" % (OUT, len(allrows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
