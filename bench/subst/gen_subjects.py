#!/usr/bin/env python3
"""gen_subjects.py -- the substitution set's subjects: one Apache-combined
access log, in two sizes that are byte PREFIXES of each other.

    acc-small   17,500 lines  (~4 MB)   `make check`'s subject, always cheap
    acc-main 1,600,000 lines  (~350 MB) the timed subject ("a few hundred MB")

Both come from ONE stream (`logsim.stream`), so `acc-small` is the first
17,500 lines of `acc-main` byte for byte and every planted count at the
smaller size is the count of the same stream's prefix. The files are
GENERATED and GITIGNORED (`bench/*/subjects/`); the committed record of what
they must be is `manifest.tsv` (id, len, sha256, description, periodic --
the harness's five-column shape) and `planted.tsv` (the oracle-independent
counts of what the generator planted, per subject).

    gen_subjects.py                   write both subjects + manifest + planted
    gen_subjects.py --which small     only acc-small (and its manifest rows)
    gen_subjects.py --check           regenerate acc-small in memory and
                                      require manifest.tsv + planted.tsv to
                                      match; verify any subject file already
                                      on disk against its manifest row; when
                                      the real-log reference is present
                                      (build/subst-ref/apache_logs) run the
                                      calibration on the first window and
                                      require it to PASS -- skipped BY NAME
                                      when the reference is absent
    gen_subjects.py --check --full    also regenerate acc-main (hashing, not
                                      storing), prove acc-small is its
                                      prefix, and calibrate the mid window

Large subjects belong under /var/tmp/pcrecbench/<lane>/ (BOILERPLATE): set
`PCRECBENCH_SUBST_SUBJECTS` (or pass `--out`) to move `subjects/` there;
`gen_expectations.py` honours the same variable.

`periodic` is `no` for both: the smallest-period test (pcrecbench/periodic.py)
runs on the first 256 KiB, which refutes periodicity of the whole file (a
subject periodic with p <= 4096 is periodic in every prefix longer than p).

Engine-neutral (R-BENCH-4): nothing here names an engine or a case's pattern.
The planted densities (NOTES.md "Densities") are stated BEFORE any run.
"""
import argparse
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)

import logsim  # noqa: E402
from pcrecbench import periodic  # noqa: E402

SUBJECTS = (("acc-small", 17_500), ("acc-main", 1_600_000))
OUT_DEFAULT = os.environ.get("PCRECBENCH_SUBST_SUBJECTS",
                             os.path.join(HERE, "subjects"))
MANIFEST = os.path.join(HERE, "manifest.tsv")
PLANTED = os.path.join(HERE, "planted.tsv")
REF_DEFAULT = os.path.join(ROOT, "build", "subst-ref", "apache_logs")
PERIODIC_PREFIX = 256 * 1024

MANIFEST_HEADER = "id\tlen\tsha256\tdescription\tperiodic\n"
PLANTED_COLS = ("lines", "n_date", "n_rare", "n_email", "n_url7_correct",
                "n_url7_wrong", "n_url7_missing_noq", "n_url7_missing_q")
DESCRIPTIONS = {
    "acc-small": "Apache combined access log, the first 17,500 lines of acc-main (make check's subject)",
    "acc-main": "Apache combined access log, 1,600,000 lines (the timed subject)",
}


def generate(upto_lines, boundaries, sink=None):
    """Run the stream. -> {boundary lines: (sha256 hex, bytes, planted dict,
    first-256KiB bytes)} for each boundary, one pass. `sink(boundary_index,
    chunk)` receives every line's bytes (for writing files)."""
    planted = logsim.Planted()
    hs = {b: hashlib.sha256() for b in boundaries}
    nbytes = dict.fromkeys(boundaries, 0)
    snap = {}
    head = bytearray()
    live = list(boundaries)
    n = 0
    for line in logsim.stream(upto_lines, planted):
        n += 1
        if len(head) < PERIODIC_PREFIX:
            head += line
        for b in live:
            hs[b].update(line)
            nbytes[b] += len(line)
        if sink is not None:
            sink(n, line)
        if n in hs:
            snap[n] = (hs[n].hexdigest(), nbytes[n], dict(planted.n),
                       bytes(head[:PERIODIC_PREFIX]))
            live.remove(n)
    return snap


def rows_for(snap):
    man, pl = [], []
    for sid, lines in SUBJECTS:
        if lines not in snap:
            continue
        sha, nb, cnt, head = snap[lines]
        per = periodic.periodic_field(head)
        man.append("%s\t%d\t%s\t%s\t%s\n" % (sid, nb, sha, DESCRIPTIONS[sid], per))
        pl.append("%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d\n" % (
            sid, lines, lines, cnt["rare"], cnt["email"], cnt["url7_correct"],
            cnt["url7_wrong"], cnt["url7_missing_noq"], cnt["url7_missing_q"]))
    return man, pl


def read_rows(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines(keepends=True)[1:]


def cmd_write(args):
    which = [s for s in SUBJECTS if args.which in ("all", s[0].split("-")[1])]
    os.makedirs(args.out, exist_ok=True)
    handles = {}
    bounds = sorted(l for _s, l in which)
    last = max(bounds)

    # acc-small is a prefix of acc-main: write it from the same pass
    files = {}
    for sid, lines in which:
        files[lines] = open(os.path.join(args.out, sid + ".log"), "wb")

    def sink(n, line):
        for lines, fh in files.items():
            if n <= lines:
                fh.write(line)

    snap = generate(last, bounds, sink)
    for fh in files.values():
        fh.close()
    man, pl = rows_for(snap)
    mpath = args.manifest or MANIFEST
    ppath = args.planted or PLANTED
    old_m = {r.split("\t")[0]: r for r in read_rows(mpath)} if os.path.exists(mpath) and args.which != "all" else {}
    old_p = {r.split("\t")[0]: r for r in read_rows(ppath)} if os.path.exists(ppath) and args.which != "all" else {}
    for r in man:
        old_m[r.split("\t")[0]] = r
    for r in pl:
        old_p[r.split("\t")[0]] = r
    with open(mpath, "w", encoding="utf-8", newline="\n") as f:
        f.write(MANIFEST_HEADER)
        f.writelines(old_m[s] for s, _ in SUBJECTS if s in old_m)
    with open(ppath, "w", encoding="utf-8", newline="\n") as f:
        f.write("id\t" + "\t".join(PLANTED_COLS) + "\n")
        f.writelines(old_p[s] for s, _ in SUBJECTS if s in old_p)
    for sid, lines in which:
        sha, nb, cnt, _h = snap[lines]
        print("gen_subjects: %s %d lines, %d B, sha256 %s" % (sid, lines, nb, sha[:16]))
    return 0


def sha_file(path, limit=None):
    h = hashlib.sha256()
    left = limit
    with open(path, "rb") as f:
        while True:
            chunk = f.read(1 << 22 if left is None else min(1 << 22, left))
            if not chunk:
                break
            h.update(chunk)
            if left is not None:
                left -= len(chunk)
                if left <= 0:
                    break
    return h.hexdigest()


def cmd_check(args):
    ok = True
    bounds = [SUBJECTS[0][1]] + ([SUBJECTS[1][1]] if args.full else [])
    lines_small = []
    # regenerate; keep the small subject's lines in memory for calibration
    keep = {}

    def sink(n, line):
        if n <= SUBJECTS[0][1]:
            lines_small.append(line.rstrip(b"\n"))

    snap = generate(max(bounds), bounds, sink)
    man, pl = rows_for(snap)
    committed_m = {r.split("\t")[0]: r for r in read_rows(MANIFEST)}
    committed_p = {r.split("\t")[0]: r for r in read_rows(PLANTED)}
    for r in man:
        sid = r.split("\t")[0]
        if committed_m.get(sid) != r:
            print("FAIL manifest.tsv row for %s differs from the regeneration:\n"
                  "  committed:   %s  regenerated: %s" % (sid, committed_m.get(sid), r),
                  end="")
            ok = False
    for r in pl:
        sid = r.split("\t")[0]
        if committed_p.get(sid) != r:
            print("FAIL planted.tsv row for %s differs from the regeneration:\n"
                  "  committed:   %s  regenerated: %s" % (sid, committed_p.get(sid), r),
                  end="")
            ok = False
    print("gen_subjects: regenerated %s -- manifest + planted %s" % (
        ", ".join(s for s, l in SUBJECTS if l in snap), "MATCH" if ok else "DIFFER"))

    # any subject on disk must match its manifest row
    for sid, lines in SUBJECTS:
        path = os.path.join(args.out, sid + ".log")
        if not os.path.exists(path):
            continue
        row = committed_m[sid].rstrip("\n").split("\t")
        if os.path.getsize(path) != int(row[1]) or sha_file(path) != row[2]:
            print("FAIL %s on disk does not match manifest.tsv" % path)
            ok = False
        else:
            print("gen_subjects: %s on disk matches manifest.tsv" % path)
    sp = os.path.join(args.out, "acc-small.log")
    mp = os.path.join(args.out, "acc-main.log")
    if os.path.exists(sp) and os.path.exists(mp):
        if sha_file(mp, os.path.getsize(sp)) != sha_file(sp):
            print("FAIL acc-small is not a byte prefix of acc-main")
            ok = False
        else:
            print("gen_subjects: acc-small is a byte prefix of acc-main")
    if args.full and SUBJECTS[0][1] in snap and SUBJECTS[1][1] in snap:
        print("gen_subjects: acc-small prefix of acc-main holds by construction (one stream)")

    # calibration, when the reference is present
    ref = os.environ.get("PCRECBENCH_SUBST_REF", REF_DEFAULT)
    if not os.path.exists(ref):
        print("gen_subjects: calibration SKIPPED -- reference %s absent "
              "(bench/subst/fetch_reference.sh fetches it; make check never does)" % ref)
    else:
        import calibrate
        rows, cal_ok, _tsv = calibrate.run(ref, first_lines=lines_small,
                                           need_mid=args.full)
        nfail = sum(r[4] == "FAIL" for r in rows)
        print("gen_subjects: calibration %s (%d rows, %d FAIL, window(s): %s)" % (
            "PASS" if cal_ok else "FAIL", len(rows), nfail,
            "first10k" + (" + mid10k" if args.full else "")))
        if not cal_ok:
            for r in rows:
                if r[4] == "FAIL":
                    print("  FAIL", r[0], "ref", r[1], "gen", r[2])
            ok = False
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=OUT_DEFAULT,
                    help="directory for the .log subjects (default subjects/)")
    ap.add_argument("--which", choices=("all", "small", "main"), default="all")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--full", action="store_true",
                    help="with --check: also regenerate acc-main and calibrate the mid window")
    ap.add_argument("--manifest", help="write the manifest here instead")
    ap.add_argument("--planted", help="write planted.tsv here instead")
    args = ap.parse_args()
    return cmd_check(args) if args.check else cmd_write(args)


if __name__ == "__main__":
    sys.exit(main())
