#!/usr/bin/env python3
"""calibrate.py -- measure the generated access log against a REAL one.

The reference is the elastic/examples Apache-combined sample (10,000 lines;
commit bc53b584c0f9f574d4373193334bf03541a54936, git blob 94bf224f..., sha256
f15c31e9... -- `fetch_reference.sh` downloads and verifies it, nothing here
does). It is DATA: this module only ever reads it as bytes and splits it on
newlines; it never executes, imports or evals any of it. Run it with
`python3 -I`.

WHAT IS COMPARED (docs/design/subst_bench_v1.md 8a item 2), the reference's
10,000 lines against TWO same-size windows of the generated stream: the
FIRST 10,000 lines and a 10,000-line window from the MIDDLE of the 1.6 M-line
`acc-main` (lines 800,000..809,999):

  * byte entropy (bits/byte, Shannon over the window's byte histogram);
  * compression ratios: gzip -6 (zlib), xz -6 (lzma), zstd -3 (the `zstd`
    binary, skipped by name when absent) -- compressed/original, so they also
    catch CROSS-LINE repetition;
  * the line-length distribution (mean and p10/p50/p90/p99);
  * field variety per 10 k lines (distinct client addresses, request paths,
    user agents, referrers) and the mean run of consecutive same-address
    lines (the interleaving of sessions);
  * the status mix (200/304/404/301 fractions);
  * each case's MATCHES PER LINE, from `cases/*/PATTERN.rx` run with python's
    `re` (every pattern here is a leftmost-first pattern whose python-re and
    PCRE2 counts agree; the oracle's counts are what the expectations carry).

TOLERANCES (stated in NOTES.md before any run; Frank's proposal, ruling 8a):
  compression ratios         +-5 % (relative)
  entropy                    +-5 %
  line-length mean/percentiles, field variety, run length, natural case
  densities                  +-10 % (relative)
  a FRACTION below 5 % (status 304/404/301, case densities below 0.05 per
  line) passes on EITHER +-10 % relative OR +-0.3 percentage points
  absolute: the reference is ONE 10 k-line sample and a 2 % event has a
  binomial standard deviation of ~7 % of itself.
PLANTED densities are marked "by design" and exempt: case 2 (blocked paths),
case 4 (one date per line), case 5b (e-mails), case 7 (the URL mix).

Exit status 0 iff every non-exempt row passes on both windows.
"""
import argparse
import collections
import itertools
import lzma
import math
import os
import re
import shutil
import subprocess
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import logsim  # noqa: E402

REF_PATH_DEFAULT = os.path.join(ROOT, "build", "subst-ref", "apache_logs")
REF_SHA256 = "f15c31e905f86c7b4b6ab44aee74d0a2086dce89f010187d983edea7ef0364ef"
MID_START = 800_000
WINDOW = 10_000

LINE_RX = re.compile(
    rb'^(\S+) \S+ \S+ \[[^\]]+\] "(?:(\S+) (\S+) [^"]*|[^"]*)" (\d+) \S+ '
    rb'"([^"]*)" "([^"]*)"$')

#: cases whose density is PLANTED on purpose ("by design", exempt); the others
#: are natural and held to the tolerance.
BY_DESIGN = {"2-rare", "4-reorder", "5b-mask-email", "7-url-tld-fix",
             "7a-url-tld-value", "7b-url-tld-insert-qmark",
             "7c-url-tld-insert-amp"}


PLANTED_URL = re.compile(rb"https://www\.(acme|globex|initech|umbrella|hooli)\.")


def read_lines(path):
    with open(path, "rb") as f:
        data = f.read()
    return [l for l in data.split(b"\n") if l]


def case_patterns():
    out = {}
    cdir = os.path.join(HERE, "cases")
    for c in sorted(os.listdir(cdir)):
        with open(os.path.join(cdir, c, "PATTERN.rx"), "rb") as f:
            out[c] = re.compile(f.read().rstrip(b"\n"))
    return out


def zstd_ratio(data):
    z = shutil.which("zstd")
    if not z:
        return None
    r = subprocess.run([z, "-3", "-c", "-q"], input=data, capture_output=True,
                       check=True)
    return len(r.stdout) / len(data)


def metrics(lines, pats):
    """-> ordered dict metric -> float|None for one window of lines."""
    data = b"\n".join(lines) + b"\n"
    n = len(data)
    m = collections.OrderedDict()
    hist = collections.Counter(data)
    m["entropy_bits_per_byte"] = -sum(v / n * math.log2(v / n)
                                      for v in hist.values())
    m["gzip6_ratio"] = len(zlib.compress(data, 6)) / n
    m["xz6_ratio"] = len(lzma.compress(data, preset=6)) / n
    m["zstd3_ratio"] = zstd_ratio(data)
    ll = sorted(len(l) + 1 for l in lines)
    nl = len(ll)
    m["linelen_mean"] = sum(ll) / nl
    for p in (10, 50, 90, 99):
        m["linelen_p%d" % p] = ll[min(nl - 1, nl * p // 100)]
    rows = [LINE_RX.match(l) for l in lines]
    m["unparsed_lines"] = sum(r is None for r in rows)
    rows = [r.groups() for r in rows if r]
    # Variety is a property of the NATURAL traffic: the planted e-mail and
    # case-7 URL values are all distinct by design, so a path or referrer
    # that carries one is left out of its distinct count (the lines stay in
    # the window).
    m["unique_ips_per_10k"] = len({r[0] for r in rows})
    m["unique_paths_per_10k"] = len({r[2] for r in rows if b"@" not in r[2]})
    m["unique_agents_per_10k"] = len({r[5] for r in rows})
    m["unique_referrers_per_10k"] = len({r[4] for r in rows
                                         if b"@" not in r[4]
                                         and not PLANTED_URL.match(r[4])})
    runs = [len(list(g)) for _k, g in itertools.groupby(r[0] for r in rows)]
    m["ip_run_mean"] = sum(runs) / len(runs)
    st = collections.Counter(r[3] for r in rows)
    for code in (b"200", b"304", b"404", b"301"):
        m["status_%s_frac" % code.decode()] = st[code] / len(rows)
    for c, rx in pats.items():
        m["case_%s_per_line" % c] = sum(len(rx.findall(l)) for l in lines) / nl
    return m


def tolerance(name, ref_value):
    """-> (relative tol, absolute tol or None, exempt-reason or None)."""
    if name.startswith("case_"):
        c = name[len("case_"):-len("_per_line")]
        if c in BY_DESIGN:
            return 0.10, None, "by design"
        return 0.10, (0.3 / 100 if ref_value < 0.05 else None), None
    if name in ("gzip6_ratio", "xz6_ratio", "zstd3_ratio",
                "entropy_bits_per_byte"):
        return 0.05, None, None
    if name.startswith("status_") and ref_value < 0.05:
        return 0.10, 0.3 / 100, None
    if name == "unparsed_lines":
        return None, None, "info"
    return 0.10, None, None


def compare(ref, windows):
    """-> list of rows (metric, ref, {win: value}, tol_text, verdict)."""
    rows = []
    for name, rv in ref.items():
        rel, ab, exempt = tolerance(name, rv)
        vals = {w: m[name] for w, m in windows.items()}
        if rv is None or any(v is None for v in vals.values()):
            rows.append((name, rv, vals, "n/a (tool absent)", "SKIP"))
            continue
        tol_text = ("+-%d%%" % round(rel * 100)) if rel else "-"
        if ab:
            tol_text += " or +-%.1fpp" % (ab * 100)
        if exempt:
            rows.append((name, rv, vals, exempt, "BY-DESIGN" if exempt == "by design" else "INFO"))
            continue
        ok = True
        for v in vals.values():
            dev = abs(v - rv) / rv if rv else (0 if v == 0 else 1)
            good = dev <= rel or (ab is not None and abs(v - rv) <= ab)
            ok = ok and good
        rows.append((name, rv, vals, tol_text, "PASS" if ok else "FAIL"))
    return rows


def render_tsv(rows, wins):
    out = ["metric\treference\t%s\t%s\ttolerance\tverdict" % (
        "\t".join(wins), "\t".join("dev_" + w for w in wins))]
    for name, rv, vals, tol, verdict in rows:
        def f(x):
            return "n/a" if x is None else ("%.6g" % x)

        def dev(w):
            v = vals[w]
            if rv is None or v is None or not rv:
                return "n/a"
            return "%+.1f%%" % (100 * (v - rv) / rv)

        out.append("\t".join([name, f(rv)] + [f(vals[w]) for w in wins]
                             + [dev(w) for w in wins] + [tol, verdict]))
    return "\n".join(out) + "\n"


def load_reference(path):
    import hashlib
    with open(path, "rb") as f:
        data = f.read()
    got = hashlib.sha256(data).hexdigest()
    if got != REF_SHA256:
        raise SystemExit("calibrate: reference %s has sha256 %s, expected %s "
                         "-- refusing" % (path, got, REF_SHA256))
    return [l for l in data.split(b"\n") if l]


def generated_windows(first_lines=None, need_mid=True):
    """-> {window name: lines}. `first_lines`, if given, supplies the first
    window (a prefix already in memory); the mid window runs the stream to
    MID_START + WINDOW and keeps the tail."""
    wins = {}
    if first_lines is not None:
        wins["gen_first10k"] = first_lines[:WINDOW]
    if need_mid or first_lines is None:
        got = []
        for i, line in enumerate(logsim.stream(MID_START + WINDOW)):
            if i < WINDOW and first_lines is None:
                wins.setdefault("gen_first10k", []).append(line.rstrip(b"\n"))
            if i >= MID_START:
                got.append(line.rstrip(b"\n"))
        wins["gen_mid10k"] = got
    return wins


def run(ref_path=REF_PATH_DEFAULT, first_lines=None, need_mid=True,
        quiet=False):
    """The programmatic entry (gen_subjects --check calls it): -> (rows,
    ok, tsv). Raises SystemExit by name if the reference is wrong."""
    pats = case_patterns()
    ref = metrics(load_reference(ref_path), pats)
    wl = generated_windows(first_lines, need_mid)
    wm = collections.OrderedDict(
        (w, metrics(lines, pats)) for w, lines in sorted(wl.items()))
    rows = compare(ref, wm)
    ok = all(r[4] != "FAIL" for r in rows)
    return rows, ok, render_tsv(rows, list(wm))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--reference",
                    default=os.environ.get("PCRECBENCH_SUBST_REF",
                                           REF_PATH_DEFAULT))
    ap.add_argument("--out", help="write the comparison table TSV here")
    args = ap.parse_args()
    if not os.path.exists(args.reference):
        print("calibrate: SKIPPED -- reference %s absent (run "
              "bench/subst/fetch_reference.sh; make check never fetches)"
              % args.reference)
        return 0
    rows, ok, tsv = run(args.reference)
    sys.stdout.write(tsv)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(tsv)
    print("calibrate: %s (%d rows, %d FAIL)" % (
        "PASS" if ok else "FAIL", len(rows), sum(r[4] == "FAIL" for r in rows)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
