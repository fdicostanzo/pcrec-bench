#!/usr/bin/env python3
"""check_unusual.py -- THE ONE ENTRY POINT for bench/unusual's checks
([B148] L8, docs/design/unusual_set_v1.md 10). `make check-unusual` runs it;
`make check` includes it.

    python3 tools/check_unusual.py [--only SECTION ...] [--list]

Sections (each timed; one summary line at the end; exit 1 on any failure):

  assist-tree   NEW (this file). The assist ledger against the file tree and
                the design: the 43 (member, engine) pairs the 3.0 verdict
                table derives (every NON-native pair, nothing else) are in
                assists.tsv exactly once each; the files under
                assists/<member>/<engine>/ are exactly the ledger's pairs
                (no assist deleted, none orphaned); every row has its author,
                reviewer lane and a reviewer_verdict that is not `pending`;
                the verdict counts equal the r10a/r10b review records'
                `Counts` lines. (The counter / sha256 / token / lines /
                duplicate / one-file agreement is `make check-tokcount`'s
                ledger-check and is NOT repeated here.)
  set           bench/unusual/check_set.py -- the set's own derivations
                (generators reproduce byte for byte, the reference scanner,
                the callout oracle table, host references, F2 pins).
  calls         tools/check_calls.py   (L4)
  vars          tools/check_vars.py    (L7)
  callouts      tools/check_callouts.py (L5)
  assist        tools/check_assist.py  (b148aw)
  w1fix         tools/check_w1fix.py   (b148w1fix: conditional-define + deep-arm storage prime)

The four tools/check_*.py modules were moved here from `make check-harness`
(tools/selfcheck.py main()): no check runs twice in `make check`.
`UNUSUAL_GATE_SKIPS` and its self-test stay in selfcheck.py -- they are about
the GENERIC gates over every set, which only selfcheck owns.

A SMOKE, not a measurement: no timing, no download, scratch under build/.
The callee-share calibration (tools/callout_calib.py) IS a timing read and is
deliberately not here. `expectations_stream.tsv`'s fast re-derive is
check_vars' section 2 (`gen_expectations.py --streams-only --check`); the
full expectations re-derivation is `bench/unusual/check_set.py --full`
(minutes; not in make check).
"""
import argparse
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)

UNUSUAL = os.path.join(ROOT, "bench", "unusual")
ASSISTS = os.path.join(UNUSUAL, "assists")
REVIEWS = os.path.join(ROOT, "docs", "dev", "reviews")

PASS, FAIL = [], []


def ok(what, detail=""):
    PASS.append(what)
    print("   PASS  %-52s %s" % (what, detail))


def bad(what, detail=""):
    FAIL.append(what)
    print("   FAIL  %-52s %s" % (what, detail))


# ---- the 3.0 verdict table, as data -------------------------------------
# Assist engines (the ledger's `engine` column) and, per family, the engines
# whose verdict is NOT native (3.0: libpcre2 ASSISTED on netstr and vars, Onig
# likewise; RE2 / rust / vectorscan assisted on everything). pcrec is native
# on all four, libpcre2 / Onig on recursion and callouts.
ALL = ("pcre2", "onig", "re2", "rust", "vectorscan")
FAMILIES = {
    # family column -> (members, non-native engines)
    "recursion": (("cscan", "wild-sexp-balanced", "wild-json-validate"),
                  ("re2", "rust", "vectorscan")),
    "callouts": (("co-luhn", "co-isbn", "co-member"),
                 ("re2", "rust", "vectorscan")),
    "netstr": (("co-netstr",), ALL),
    "vars": (("va-tenant", "va-route", "va-term", "va-term-bang"), ALL),
}
EXPECTED_PAIRS = 43


def expected_pairs():
    return {(m, e): fam for fam, (ms, es) in FAMILIES.items()
            for m in ms for e in es}


def _ledger():
    with open(os.path.join(ASSISTS, "assists.tsv"), encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if l.strip()]
    hdr = rows[0]
    return [dict(zip(hdr, r)) for r in rows[1:]], hdr


def _review_counts():
    """-> {verdict: n} summed over the r10* review records' Counts lines."""
    tot = {"accepted": 0, "golfed": 0, "not-idiomatic": 0, "padded": 0}
    files = sorted(f for f in os.listdir(REVIEWS)
                   if re.match(r"2026-10-28-r10[ab]-", f))
    for f in files:
        text = open(os.path.join(REVIEWS, f), encoding="utf-8").read()
        i = text.find("**Counts")
        if i < 0:
            continue
        seg = text[i:i + 400]
        for k in tot:
            m = re.search(r"(\d+) " + k, seg)
            if m:
                tot[k] += int(m.group(1))
    return tot, files


def section_assist_tree():
    rows, hdr = _ledger()
    want = expected_pairs()
    if len(want) == EXPECTED_PAIRS:
        ok("3.0 table derives %d non-native (member, engine) pairs" % len(want))
    else:
        bad("3.0 table derives %d pairs" % EXPECTED_PAIRS, str(len(want)))
    got = {}
    for r in rows:
        got.setdefault((r["member"], r["engine"]), []).append(r)
    dup = sorted(k for k, v in got.items() if len(v) > 1)
    missing = sorted(set(want) - set(got))
    extra = sorted(set(got) - set(want))
    if len(rows) == EXPECTED_PAIRS and not dup and not missing and not extra:
        ok("ledger: every non-native pair exactly once", "%d rows" % len(rows))
    else:
        bad("ledger: every non-native pair exactly once",
            "rows %d dup %s missing %s extra %s" % (len(rows), dup, missing, extra))
    fam_bad = [(k, v[0]["feature"]) for k, v in got.items()
               if k in want and v[0]["feature"] != want[k]]
    if not fam_bad:
        ok("ledger: each row's feature is its member's family")
    else:
        bad("ledger: each row's feature is its member's family", repr(fam_bad))
    # the file tree == the ledger's pairs (an assist deleted or orphaned)
    tree = set()
    for m in sorted(os.listdir(ASSISTS)):
        d = os.path.join(ASSISTS, m)
        if not os.path.isdir(d) or m in ("templates", "problems"):
            continue
        for e in sorted(os.listdir(d)):
            fs = [x for x in os.listdir(os.path.join(d, e)) if x.startswith("assist.")]
            if fs:
                tree.add((m, e))
            else:
                bad("tree: %s/%s holds an assist.* file" % (m, e), "empty dir")
    gone = sorted(set(got) - tree)
    orphan = sorted(tree - set(got))
    if not gone and not orphan:
        ok("tree: assists/<member>/<engine>/ equals the ledger's pairs",
           "%d dirs" % len(tree))
    else:
        bad("tree: assists/<member>/<engine>/ equals the ledger's pairs",
            "ledger row without a file %s; file without a row %s" % (gone, orphan))
    # every row owned, reviewed, and not pending
    unowned = [k for k, v in got.items()
               if not v[0]["author_lane"] or not v[0]["reviewer_lane"]]
    pend = [k for k, v in got.items() if v[0]["reviewer_verdict"] in ("", "pending")]
    if not unowned:
        ok("ledger: every row names an author lane and a reviewer lane")
    else:
        bad("ledger: every row names an author lane and a reviewer lane", repr(sorted(unowned)))
    if not pend:
        ok("ledger: no reviewer_verdict is empty or `pending`")
    else:
        bad("ledger: no reviewer_verdict is empty or `pending`", repr(sorted(pend)))
    # one author lane per (family, engine) (the L6 ruling) and authors != reviewers
    lanes = {}
    for r in rows:
        # a declared re-authoring lane `<lane>-vN` (Frank 2026-10-28, cscan x re2) counts as its base lane
        lanes.setdefault((r["feature"], r["engine"]), set()).add(re.sub(r"-v\d+$", "", r["author_lane"]))
    multi = {k: sorted(v) for k, v in lanes.items() if len(v) != 1}
    if not multi:
        ok("ledger: one author lane per (family, engine)", "%d groups" % len(lanes))
    else:
        bad("ledger: one author lane per (family, engine)", repr(multi))
    same = [k for k, v in got.items() if v[0]["author_lane"] == v[0]["reviewer_lane"]]
    if not same:
        ok("ledger: no author reviewed its own assist")
    else:
        bad("ledger: no author reviewed its own assist", repr(same))
    # verdict counts == the review records' Counts lines
    rc, files = _review_counts()
    have = {}
    for r in rows:
        have[r["reviewer_verdict"]] = have.get(r["reviewer_verdict"], 0) + 1
    cmp = {k: (have.get(k, 0), rc[k]) for k in rc}
    if len(files) == 2 and all(a == b for a, b in cmp.values()):
        ok("ledger reviewer_verdict counts == the r10a/r10b `Counts` lines",
           ", ".join("%d %s" % (a, k) for k, (a, _b) in cmp.items() if a))
    else:
        bad("ledger reviewer_verdict counts == the r10a/r10b `Counts` lines",
            "%d review files; (ledger, review) %r" % (len(files), cmp))


def _ledger_problems(rows, tree):
    """-> problems of a ledger (list of row dicts) against a file-tree pair set."""
    want = expected_pairs()
    got = {}
    for r in rows:
        got.setdefault((r["member"], r["engine"]), []).append(r)
    probs = []
    probs += ["duplicate %s" % (k,) for k, v in got.items() if len(v) > 1]
    probs += ["missing %s" % (k,) for k in set(want) - set(got)]
    probs += ["unexpected %s" % (k,) for k in set(got) - set(want)]
    probs += ["no file %s" % (k,) for k in set(got) - tree]
    probs += ["orphan file %s" % (k,) for k in tree - set(got)]
    probs += ["pending %s" % (k,) for k, v in got.items()
              if v[0]["reviewer_verdict"] in ("", "pending")]
    return probs


def section_assist_tree_controls():
    """CONTROLS: the same predicate refuses each sabotage BY NAME and passes
    the unsabotaged ledger (so it does not dislike everything)."""
    rows, _ = _ledger()
    tree = {(r["member"], r["engine"]) for r in rows}
    if not _ledger_problems(rows, tree):
        ok("control: the real ledger and tree raise no problem")
    else:
        bad("control: the real ledger and tree raise no problem", repr(_ledger_problems(rows, tree)))
    pend = [dict(r) for r in rows]
    pend[0]["reviewer_verdict"] = "pending"
    cases = [
        ("a `pending` verdict", pend, tree, "pending"),
        ("a deleted assist file (another lane removed one)", rows, tree - {(rows[3]["member"], rows[3]["engine"])}, "no file"),
        ("an orphan assist file", rows, tree | {("va-term", "tre")}, "orphan file"),
        ("a dropped ledger row", rows[1:], tree, "missing"),
        ("a duplicated ledger row", rows + [rows[0]], tree, "duplicate"),
        ("a native-engine row (cscan x pcre2)", rows + [dict(rows[0], engine="pcre2")], tree, "unexpected"),
    ]
    for what, r, t, needle in cases:
        probs = _ledger_problems(r, t)
        if any(needle in p for p in probs):
            ok("control: %s is refused BY NAME" % what, "; ".join(probs)[:60])
        else:
            bad("control: %s is refused BY NAME" % what, repr(probs))


def section_set():
    p = subprocess.run([sys.executable, "-I", os.path.join(UNUSUAL, "check_set.py")],
                       capture_output=True, text=True)
    out = (p.stdout + p.stderr).splitlines()
    nfail = 0
    for l in out:
        if l.startswith("FAIL"):
            nfail += 1
            bad("check_set: " + l[4:].strip()[:80])
    last = out[-1] if out else "(no output)"
    if p.returncode == 0 and nfail == 0:
        ok("bench/unusual/check_set.py", last)
    else:
        bad("bench/unusual/check_set.py", "rc=%d; %s" % (p.returncode, last))


def _module(name):
    def run():
        mod = __import__(name)
        mod.run(ok, bad)
    return run


SECTIONS = [
    ("assist-tree", lambda: (section_assist_tree(), section_assist_tree_controls())),
    ("set", section_set),
    ("calls", _module("check_calls")),
    ("vars", _module("check_vars")),
    ("callouts", _module("check_callouts")),
    ("assist", _module("check_assist")),
    ("w1fix", _module("check_w1fix")),
]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--only", nargs="+", metavar="SECTION")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args(argv)
    names = [n for n, _ in SECTIONS]
    if a.list:
        print("\n".join(names))
        return 0
    if a.only:
        unknown = [n for n in a.only if n not in names]
        if unknown:
            print("unknown section(s): %s (have %s)" % (unknown, names))
            return 2
    print("== check-unusual ==")
    summary = []
    t_all = time.time()
    for name, fn in SECTIONS:
        if a.only and name not in a.only:
            continue
        print("-- [B148] unusual: %s --" % name)
        p0, f0, t0 = len(PASS), len(FAIL), time.time()
        try:
            fn()
        except Exception as e:  # a crashed section is a failure, by name
            bad("section %s crashed" % name, "%s: %s" % (type(e).__name__, e))
        summary.append((name, len(PASS) - p0, len(FAIL) - f0, time.time() - t0))
    print()
    for name, p, f, t in summary:
        print("   %-12s %4d passed %3d failed %7.1f s" % (name, p, f, t))
    print("check-unusual: %d check(s) passed, %d FAILED  (%.1f s)"
          % (len(PASS), len(FAIL), time.time() - t_all))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
