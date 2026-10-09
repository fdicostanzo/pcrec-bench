#!/usr/bin/env python3
"""tools/tests/test_trend.py -- self-tests for tools/trend.py, trend_html.py and
trend_cite_check.py ([B130]). A synthetic store in a tempdir (never the real
store), hand-computed expectations:

 set demo@1 holds pcrec pin A (abi 10); demo@2 holds pins B (abi 12) and C
 (abi 30); a pcre2-jit control record sits in each set version.
 cells (2 subjects, 5 trials; ns/call per subject, so the set sum is 2x):
   p1  A 100  B  50  programs differ        -> faster, ratio 0.5
   p2  A 100  B 101  ranges overlap          -> within-noise
   p3  A 100  B 130  program identical       -> slower (beyond the 0.0846 fallback band)
   p4  A 100  B 105  identical, disjoint     -> within-identical-band
   p5  B only                                -> new
   p6  pattern sha changes                   -> not-comparable
   p7  A gave up, B judged                   -> transition gave-up->judged
 control: 100 -> 100 everywhere except p2 (100 -> 150, a drift-suspect cell).
 instrument differs A vs B (override), same B vs C; abi span A->B 2, B->C 18.
Run: python3 tools/tests/test_trend.py
"""
import argparse
import builtins
import gzip
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import trend as T  # noqa: E402
import trend_snapshot as TS  # noqa: E402
import trend_cite_check as CC  # noqa: E402

PINS = ["aaaa111", "bbbb222", "cccc333"]
CFG = """machine = "m1"
control_globs = ["libpcre2_*_jit-caps-simdna"]
competitor_globs = ["re2_*_default-caps-simdna"]
headline_configs = ["auto-caps-simdna"]
wide_gap_abi = 8
fallback_band = 0.0846
band_min_cells = 10
"""


def trials(ns, spread=0.5):
    return [ns - spread, ns - spread / 2, ns, ns + spread / 2, ns + spread]


def write_record(store, setname, ver, tid, engine, ts, commit, abi, cells, patsha,
                 comp=None, status="measured"):
    """cells: {pid: {"ns": float | None (gave-up)}} for 2 subjects s1, s2."""
    d = os.path.join(store, "records", f"{setname}@{ver}", tid)
    os.makedirs(d, exist_ok=True)
    rel = f"records/{setname}@{ver}/{tid}/{setname}@{ver}__{tid}__m1__{ts}.jsonl"
    setup = {"kind": "setup", "schema_version": "1.7", "status": status,
             "testee": {"testee_id": tid, "engine_name": engine},
             "run": {"harness_commit": commit, "timestamp": ts},
             "patterns": [{"pattern_id": p, "canonical_sha256": patsha[p]} for p in cells],
             "subjects": [{"subject_id": s, "sha256": "sub" + s} for s in ("s1", "s2")]}
    lines = [json.dumps(setup)]
    for pid, c in cells.items():
        for s in ("s1", "s2"):
            for t, ns in enumerate(trials(c["ns"] or 1.0), 1):
                if c["ns"] is None:
                    lines.append(json.dumps({"kind": "match", "pattern_id": pid,
                        "regime": "short", "subject_id": s, "trial": t,
                        "match_outcome": "gave-up",
                        "diagnostic": "giveup:-3:PCREC_ERR_FRAMES",
                        "timing": {"elapsed_ns": 0, "iterations": 0}}))
                else:
                    lines.append(json.dumps({"kind": "match", "pattern_id": pid,
                        "regime": "short", "subject_id": s, "trial": t,
                        "match_outcome": "matched-as-expected",
                        "timing": {"elapsed_ns": ns * 1000, "iterations": 1000}}))
        if comp:
            lines.append(json.dumps({"kind": "compile", "pattern_id": pid,
                "compile_outcome": "compiled", "cost": {"total_ns": 1000},
                "engine_metadata": {"abi": abi, "program_sha256": comp[pid],
                                    "emit_bytes": 1000, "emit_code_bytes": 800,
                                    "engine": "dfa"}}))
    with open(os.path.join(store, rel), "w") as f:
        f.write("\n".join(lines) + "\n")
    return rel, (setname, ver, tid, ts, status)


def make_store(tmp, with_c=True):
    store = os.path.join(tmp, "store")
    os.makedirs(store)
    sha = {p: "psha-" + p for p in ("p1", "p2", "p3", "p4", "p5", "p6", "p7")}
    idx = []

    def put(*a, **k):
        rel, (sn, ver, tid, ts, st) = write_record(store, *a, **k)
        idx.append((rel, sn, ver, tid, "m1", ts, st, 10))
    A = {"p1": {"ns": 100}, "p2": {"ns": 100}, "p3": {"ns": 100}, "p4": {"ns": 100},
         "p6": {"ns": 100}, "p7": {"ns": None}}
    B = {"p1": {"ns": 50}, "p2": {"ns": 101}, "p3": {"ns": 130}, "p4": {"ns": 105},
         "p5": {"ns": 10}, "p6": {"ns": 100}, "p7": {"ns": 100}}
    ca = {p: "prog-" + p for p in A}
    cb = dict(ca)
    cb["p1"] = "prog-p1-NEW"
    cb["p5"] = "prog-p5"
    shaB = dict(sha)
    shaB["p6"] = "psha-p6-CHANGED"
    put("demo", "1", "pcrec_aaaa111_auto-caps-simdna", "pcrec", "2026-01-01T00:00:00Z",
        "commitA", 10, A, sha, ca)
    put("demo", "2", "pcrec_bbbb222_auto-caps-simdna", "pcrec", "2026-01-02T00:00:00Z",
        "commitB", 12, B, shaB, cb)
    # a superseded (older) measured record and an inconclusive one at the same pin
    put("demo", "2", "pcrec_bbbb222_auto-caps-simdna", "pcrec", "2026-01-01T12:00:00Z",
        "commitB", 12, B, shaB, cb)
    put("demo", "2", "pcrec_bbbb222_auto-caps-simdna", "pcrec", "2026-01-03T00:00:00Z",
        "commitB", 12, B, shaB, cb, status="inconclusive-spread")
    if with_c:
        put("demo", "2", "pcrec_cccc333_auto-caps-simdna", "pcrec", "2026-01-05T00:00:00Z",
            "commitB", 30, B, shaB, cb)
    # deny twin at pin B
    put("demo", "2", "pcrec_bbbb222_auto-caps-simdna_nolitrun", "pcrec",
        "2026-01-02T01:00:00Z", "commitB", 12,
        {p: {"ns": c["ns"] * 2 if c["ns"] else c["ns"]} for p, c in B.items()}, shaB, cb)
    CA = {p: {"ns": 100} for p in ("p1", "p2", "p3", "p4", "p6")}
    CB = {p: {"ns": 100} for p in ("p1", "p2", "p3", "p4", "p6", "p5", "p7")}
    CB["p2"] = {"ns": 150}
    put("demo", "1", "libpcre2_10.46_jit-caps-simdna", "libpcre2", "2026-01-01T00:30:00Z",
        "commitA", None, CA, sha)
    put("demo", "2", "libpcre2_10.46_jit-caps-simdna", "libpcre2", "2026-01-02T00:30:00Z",
        "commitA", None, CB, shaB)
    with open(os.path.join(store, "index.tsv"), "w") as f:
        f.write("path\tsubbench\tversion\ttestee_id\tmachine_id\ttimestamp\tstatus\trows\n")
        for r in idx:
            f.write("\t".join(str(x) for x in r) + "\n")
    rules = os.path.join(tmp, "rules.toml")
    with open(rules, "w") as f:
        f.write('[[pin_order]]\nengine = "pcrec"\npins = ["%s"]\n' % '", "'.join(PINS))
    cfgp = os.path.join(tmp, "config.toml")
    with open(cfgp, "w") as f:
        f.write(CFG)
    return store, rules, cfgp


LINKS = ("kind\tfrom\tto\tsource\treason\n"
         "set-version\tdemo@1\tdemo@2\tconfirmed\ttest: byte-identical subjects\n")


def snapshot_all(tmp, store, rules, cfgp, snap_dir, pins=PINS, force=False):
    """The store-reading half: one snapshot per pin, in pin order."""
    cfg = T.load_config(cfgp)
    pin_order = T.load_pin_order(rules)
    import csv
    with open(os.path.join(store, "index.tsv"), newline="") as f:
        idx = list(csv.DictReader(f, delimiter="\t"))
    instr = T.Instrument(tmp, override=lambda commit, eng: "instr:" + str(commit))
    out = []
    for pin in pins:
        out.append(T.write_pin_snapshot(pin, store, cfg, pin_order, idx, snap_dir,
                                        instr, None, force, cfgp))
    return out


def args_for(tmp, snap_dir, rules, cfgp, links=None):
    """The comparison's args: NO store (it must not need one)."""
    lp = os.path.join(tmp, "links.tsv")
    if links is not None or not os.path.exists(lp):
        with open(lp, "w") as f:
            f.write(LINKS if links is None else links)
    return argparse.Namespace(
        out=os.path.join(tmp, "out"), snapshots=snap_dir, links=lp, config=cfgp,
        rules=rules, interest=os.path.join(tmp, "interest.tsv"), sets=None,
        check=False, no_html=True)


def rows_of(files, name):
    out = []
    cols = None
    for ln in files[name].split("\n"):
        if not ln or ln.startswith("#"):
            continue
        c = ln.split("\t")
        if cols is None:
            cols = c
        else:
            out.append(dict(zip(cols, c)))
    return out


def main():
    fails = []

    def ok(name, cond, detail=""):
        print(("PASS " if cond else "FAIL ") + name + (" " + str(detail) if not cond else ""))
        if not cond:
            fails.append(name)

    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "interest.tsv"), "w") as f:
            f.write("# t\nmechanism\trole\tset\tpattern\tregime\tform\tnote\n"
                    "mech-x\ttarget\tdemo\tp1\t\t\tn\n")
        store, rules, cfgp = make_store(tmp)
        snaps = os.path.join(tmp, "snaps")
        snapshot_all(tmp, store, rules, cfgp, snaps)
        # THE STORE IS GONE from here on: the comparison must not need it
        shutil.rmtree(store)
        a = args_for(tmp, snaps, rules, cfgp)
        cfg, meta, files, out = T.render_files(a)
        dl = {(r["pattern"], r["pin"]): r for r in rows_of(files, "deltas.tsv")
              if r["config"] == "auto-caps-simdna"}
        g = lambda p, pin="bbbb222": dl[(p, pin)]
        ok("p1 faster x0.5 (hand: 100->50)", g("p1")["verdict"] == "faster"
           and g("p1")["ratio"] == "0.5000", g("p1"))
        ok("p1 absolute ns both sides (set sum over 2 subjects)",
           g("p1")["ns_prev"] == "200.0" and g("p1")["ns_new"] == "100.0")
        ok("p2 within-noise (ranges overlap)", g("p2")["verdict"] == "within-noise", g("p2"))
        ok("p3 identical program, beyond fallback band -> slower",
           g("p3")["verdict"] == "slower" and g("p3")["identical"] == "yes", g("p3"))
        ok("p4 identical, disjoint, inside band -> within-identical-band",
           g("p4")["verdict"] == "within-identical-band", g("p4"))
        ok("p5 new", g("p5")["verdict"] == "new")
        ok("p6 not-comparable (pattern sha moved)", g("p6")["verdict"] == "not-comparable"
           and g("p6")["ratio"] == "")
        ok("p7 gave-up -> judged transition, no ratio",
           g("p7")["transition"] == "gave-up->judged" and g("p7")["ratio"] == "", g("p7"))
        ok("p1 program differs", g("p1")["identical"] == "no")
        ok("instrument-changed flagged on A->B, not B->C",
           g("p1")["instrument_changed"] == "1" and g("p1", "cccc333")["instrument_changed"] == "0")
        ok("abi span 2 (A->B) not wide; 18 (B->C) wide",
           g("p1")["wide_gap"] == "0" and g("p1")["abi_span"] == "2"
           and g("p1", "cccc333")["wide_gap"] == "1")
        ok("control ratio 1.0 on p1, 1.5 on p2 (cell drift flagged)",
           g("p1")["control_ratio"] == "1.0000" and g("p2")["control_ratio"] == "1.5000"
           and g("p2")["cell_drift_suspect"] == "1" and g("p1")["cell_drift_suspect"] == "0", g("p2"))
        ok("R2: no delta pairs a pin with itself", all(r["pin"] != r["prev_pin"] for r in dl.values()))
        ok("previous = newest earlier pin (C's prev is B)", g("p1", "cccc333")["prev_pin"] == "bbbb222")
        sm = [r for r in rows_of(files, "summary.tsv")
              if r["pin"] == "bbbb222" and r["config"] == "auto-caps-simdna"]
        ok("one summary row, regime kept separate", len(sm) == 1 and sm[0]["regime"] == "short", sm)
        s = sm[0]
        ok("summary counts: 1 faster, 1 slower, 1 noise, 1 in-band",
           (s["n_faster"], s["n_slower"], s["n_within_noise"], s["n_within_identical_band"])
           == ("1", "1", "1", "1"), s)
        ok("identical-and-moved = 2 (p3, p4; p2 overlaps)", s["n_identical"] == "3"
           and s["n_identical_moved"] == "2", s)
        ok("drift-suspect cell count 1, pair not drift-suspect (median control 1.0)",
           s["n_drift_suspect_cells"] == "1" and s["drift_suspect"] == "0", s)
        ok("band_src fallback with < band_min_cells identical cells", s["band_src"] == "fallback")
        recs = rows_of(files, "records.tsv")
        disp = sorted(r["disposition"] for r in recs if r["testee_id"].startswith("pcrec_bbbb222_auto-caps-simdna")
                      and "nolitrun" not in r["testee_id"])
        ok("R11: superseded + inconclusive named, one used",
           disp == ["excluded-status:inconclusive-spread", "superseded", "used"], disp)
        tw = rows_of(files, "deny_twins.tsv")
        ok("deny twin rows: ratio 2.0 deny/base on p1", any(
            r["pattern"] == "p1" and r["ratio_deny_over_base"] == "2.0000" for r in tw), tw[:1])
        it = rows_of(files, "interest.tsv")
        ok("cells-of-interest join", any(r["mechanism"] == "mech-x" and r["pattern"] == "p1" for r in it))
        hist = [k for k in files if k.startswith("history/")]
        ok("history file per (set, config)", "history/demo/auto-caps-simdna.tsv" in hist, hist)
        mv = rows_of(files, "movers_by_stamp.tsv")
        ok("movers grouped by stamp value", any(m["stamp"] == "engine" for m in mv))
        # determinism
        cfg2, meta2, files2, _ = T.render_files(args_for(tmp, snaps, rules, cfgp))
        ok("regenerate twice: byte-identical", files == files2)
        # history append-only: drop pin C, regenerate, the shorter must be a prefix
        store2 = os.path.join(tmp, "s2")
        os.makedirs(store2)
        tmp2 = os.path.join(tmp, "t2")
        os.makedirs(tmp2)
        st2, ru2, cf2 = make_store(tmp2, with_c=False)
        sn2 = os.path.join(tmp2, "snaps")
        snapshot_all(tmp2, st2, ru2, cf2, sn2, pins=PINS[:2])
        _, _, f_no_c, _ = T.render_files(args_for(tmp2, sn2, ru2, cf2))
        h_old = f_no_c["history/demo/auto-caps-simdna.tsv"].split("\n")
        h_new = files["history/demo/auto-caps-simdna.tsv"].split("\n")
        body_old = [l for l in h_old if not l.startswith("#")][:-1]
        body_new = [l for l in h_new if not l.startswith("#")]
        ok("R14 history: older body is a prefix of the newer (pin appended)",
           body_new[:len(body_old)] == body_old and len(body_new) > len(body_old))
        # check mode
        outd = os.path.join(tmp, "out")
        T.write_files(outd, files)
        ok("--check clean right after write", T.check_files(outd, files) == [])
        with open(os.path.join(outd, "deltas.tsv"), "a") as f:
            f.write("x\n")
        ok("--check detects drift", any(r == "deltas.tsv" for r, _ in T.check_files(outd, files)))
        # R19 era-aware instrument + changed files (a tiny real git repo)
        import subprocess
        gr = os.path.join(tmp, "gitrepo")
        os.makedirs(os.path.join(gr, "testees", "pcrec"))
        run = lambda *c: subprocess.run(("git", "-C", gr) + c, check=True,
                                        capture_output=True, text=True).stdout.strip()
        run("init", "-q")
        run("config", "user.email", "t@t")
        run("config", "user.name", "t")
        wf = lambda n, t: open(os.path.join(gr, "testees", "pcrec", n), "w").write(t)
        wf("driver.c", "d1")
        wf("shim.c", "s1")
        run("add", "-A")
        run("commit", "-qm", "c1")
        c1 = run("rev-parse", "HEAD")
        wf("shim.c", "s2")
        run("commit", "-qam", "c2")
        c2 = run("rev-parse", "HEAD")
        wf("timed.c", "t1")
        wf("driver.c", "d2")
        run("add", "-A")
        run("commit", "-qm", "c3")
        c3 = run("rev-parse", "HEAD")
        ins = T.Instrument(gr)
        i1, i2, i3 = (ins.of(c, "pcrec") for c in (c1, c2, c3))
        ok("era 1 instrument = driver.c + shim.c", i1.startswith("era=1|") and "driver.c:" in i1
           and "timed.c" not in i1, i1)
        ok("era 2 instrument = timed.c + shim.c (driver.c no longer hashed)",
           i3.startswith("era=2|") and "timed.c:" in i3 and "driver.c" not in i3, i3)
        ok("changed files: shim only within era 1", T.instr_diff(i1, i2) == ["shim.c"], T.instr_diff(i1, i2))
        ok("a pair straddling the eras is changed by definition, era named",
           "era" in T.instr_diff(i2, i3))
        ok("identical instrument -> no changed file", T.instr_diff(i3, i3) == [])
        ok("delta rows carry instrument_changed_files", g("p1")["instrument_changed_files"] != "")
        ok("cells.tsv is exempt from --check (untracked)", "cells.tsv" in T.UNTRACKED)
        # unknown pin is excluded, named
        # ---- [B130.2] snapshots, links, store-free compare
        sdir = os.path.join(tmp, "snaps")
        sfiles = sorted(os.listdir(sdir))
        ok("one snapshot file per pin", sfiles == [p + ".tsv.gz" for p in PINS], sfiles)
        raw = open(os.path.join(sdir, "aaaa111.tsv.gz"), "rb").read()
        ok("deterministic gzip: mtime field 0, no filename", raw[4:8] == b"\0\0\0\0"
           and not (raw[3] & 8), raw[:10])
        hdr, recs = TS.read_header_recs(os.path.join(sdir, "bbbb222.tsv.gz"))
        ok("header carries the schema version and pin",
           hdr["schema"] == TS.SNAPSHOT_SCHEMA and hdr["pin"] == "bbbb222", hdr)
        ok("snapshot lists superseded + excluded records too (R11)",
           {"superseded", "used"} <= {r["disposition"] for r in recs}
           and any(r["disposition"].startswith("excluded-status") for r in recs))
        ok("a control stored once: pin C's copy is a ref to the first snapshot",
           any(r["role"] == "control" and r["data"].startswith("ref:")
               for r in TS.read_header_recs(os.path.join(sdir, "cccc333.tsv.gz"))[1]))
        ok("every CEL row recomputes from its SUBJ rows (verify)",
           all(TS.verify_snapshot(os.path.join(sdir, f)) == [] for f in sfiles))
        # round trip: the stored digest equals a fresh digest of the same record
        _h, rs = TS.read_snapshot(os.path.join(sdir, "bbbb222.tsv.gz"))
        used = [r for r in rs if r["disposition"] == "used" and r["role"] == "pcrec"
                and "nolitrun" not in r["testee_id"]][0]
        ok("per-subject trial rows are in the snapshot (common-subject rule)",
           set(used["dg"]["cells"]["p1\tshort\tplain"]) == {"s1", "s2"}
           and len(used["dg"]["cells"]["p1\tshort\tplain"]["s1"]) == 5)
        ok("per-subject median derivable from the stored trials (hand: p1 at B = 50.0)",
           TS.subject_median(used["dg"]["cells"]["p1\tshort\tplain"]["s1"]) == 50.0)
        # lossless trial codec: diag with every separator, float repr, int, None
        oc = {"matched-as-expected": 0, "gave-up": 1}
        tr = [[1, "matched-as-expected", 34529916.5, ""], [2, "gave-up", None,
              "giveup:-3,a%b\tc\nd"], [3, "matched-as-expected", 7, ""],
              [4, "matched-as-expected", 0.1 + 0.2, ""]]
        raws = [[69059833, 2], None, None, [3000, 7]]   # 1 exact; 4 exact (3000/7 != .3), so f-path
        raws[3] = None
        tr.append([5, "matched-as-expected", 1234567890123 / 1000, ""])
        raws.append([1234567890123, 1000])
        tr.append([6, "matched-as-expected", 1234567890124 / 1000, ""])
        raws.append([1234567890124, 1000])
        enc = TS.enc_trials(tr, oc, raws, 1000)
        back = TS.dec_trials(enc, ["matched-as-expected", "gave-up"], 1000)
        ok("trial codec round-trips exactly (exact elapsed/iters, f-path, None, escaped diag)",
           back == tr and [type(t[2]) for t in back] == [type(t[2]) for t in tr]
           and "/2" in enc and "f0.30000000000000004" in enc and ":1234567890123," in enc, enc)
        ok("snapshot text carries no JSON trial lists and no per-row path",
           not any(ln.startswith("SUBJ\t") and ("[[" in ln or "records/" in ln)
                   for ln in TS.read_lines(os.path.join(sdir, "bbbb222.tsv.gz"))))
        # immutability + determinism of the writer
        refused = False
        try:
            snapshot_all(tmp, os.path.join(tmp, "nostore"), rules, cfgp, sdir,
                         pins=["aaaa111"])
        except (SystemExit, OSError):
            refused = True
        ok("an existing snapshot is NOT overwritten without --force", refused)
        before = open(os.path.join(sdir, "aaaa111.tsv.gz"), "rb").read()
        ok("the refused write left the file byte-identical",
           before == open(os.path.join(sdir, "aaaa111.tsv.gz"), "rb").read())
        # store-free proof: trace every open() during a compare
        opened = []
        real_open, real_gz = builtins.open, gzip.open

        def traced(path, *a, **k):
            opened.append(str(path))
            return real_open(path, *a, **k)

        def traced_gz(path, *a, **k):
            opened.append(str(path))
            return real_gz(path, *a, **k)
        builtins.open, gzip.open = traced, traced_gz
        try:
            T.render_files(args_for(tmp, snaps, rules, cfgp))
        finally:
            builtins.open, gzip.open = real_open, real_gz
        ok("compare opened no path under store/ (store dir does not even exist)",
           opened and not any("/store" in o for o in opened)
           and not os.path.exists(os.path.join(tmp, "store")), [o for o in opened if "store" in o])
        # links-only: without the set-version link the pair is reported, not guessed
        _c, _m, f_nl, _o = T.render_files(args_for(
            tmp, snaps, rules, cfgp,
            links="kind\tfrom\tto\tsource\treason\n"))
        dnl = {(r["pattern"], r["pin"]): r for r in rows_of(f_nl, "deltas.tsv")
               if r["config"] == "auto-caps-simdna"}
        ok("unlinked set-version pair reported as `unlinked`, no ratio",
           dnl[("p1", "bbbb222")]["verdict"] == "unlinked"
           and dnl[("p1", "bbbb222")]["ratio"] == ""
           and "demo@1 ~ demo@2" in dnl[("p1", "bbbb222")]["why"], dnl[("p1", "bbbb222")])
        ok("same-version pairs need no link (C vs B unaffected)",
           dnl[("p1", "cccc333")]["verdict"] != "unlinked"
           and dnl[("p1", "cccc333")]["ratio"] != "")
        ok("deltas header counts the unlinked cells",
           "# unlinked_cells: 0" in files["deltas.tsv"]
           and "# unlinked_cells: 0" not in f_nl["deltas.tsv"])
        ok("the linked run equals the no-guess run everywhere a link is not needed",
           dl[("p1", "cccc333")]["ratio"] == dnl[("p1", "cccc333")]["ratio"])
        # config-rename link: records of the old name are read as the new
        _c, _m, f_rn, _o = T.render_files(args_for(
            tmp, snaps, rules, cfgp,
            links=LINKS + "config-rename\tauto-caps-simdna_nolitrun\tauto-caps-x\t"
                          "confirmed\ttest rename\n"))
        ok("config-rename link applies (new config name in deltas)",
           any(r["config"] == "auto-caps-x" for r in rows_of(f_rn, "deltas.tsv")))
        # proposals: the walk's pair is proposed when links.tsv lacks it
        import io
        import contextlib
        lp0 = os.path.join(tmp, "links_empty.tsv")
        real_open(lp0, "w").write("kind\tfrom\tto\tsource\treason\n")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            T.cmd_links(["--snapshots", snaps, "--links", lp0, "--config", cfgp,
                         "--rules", rules, "--interest", os.path.join(tmp, "interest.tsv")])
        ok("`links` proposes the demo@1~demo@2 pair as inferred",
           "set-version\tdemo@1\tdemo@2\tinferred" in buf.getvalue(), buf.getvalue())
        ok("headers carry the snapshot/links identity, not an index sha",
           "# snapshots_sha256:" in files["deltas.tsv"]
           and "# links:" in files["deltas.tsv"] and "index_sha256" not in files["deltas.tsv"])
        # citation check (independent module)
        ids = CC.ids_from_texts(files)
        good = "- p1 got faster [#%s].\n\nNOT KNOWN: why.\n" % g("p1")["row_id"]
        ok("cite check accepts real ids", CC.check_text(good, ids) == [])
        ok("cite check rejects an invented id",
           any("unknown id" in e for e in CC.check_text("- x [#D:nope].\n", ids)))
        ok("cite check rejects an uncited claim",
           any("uncited" in e for e in CC.check_text("- p1 got faster.\n", ids)))
        ok("cite ids come from the TSV, not the generator (a row_id appended to the text is seen)",
           "S:ZZZ" in CC.ids_from_texts({"summary.tsv": "row_id\nS:ZZZ\n"}))
        # html renders and carries the placeholder; a bad sidecar is rejected
        import trend_html as H
        os.makedirs(os.path.join(outd, "interpretation"))
        h = H.render_all(cfg, meta, out, outd, dict(files))
        ok("html: pages per pin + index + md", "index.html" in h and "pins/bbbb222.html" in h
           and "index.md" in h)
        ok("html: placeholder says interpretation is owed",
           "not yet written" in h["pins/bbbb222.html"])
        ok("html: instrument-changed banner present", "instrument-changed" in h["pins/bbbb222.html"])
        ok("html: no external fetch", "http://" not in h["index.html"] and "<script" not in h["index.html"])
        with open(os.path.join(outd, "interpretation", "bbbb222.md"), "w") as f:
            f.write("- bogus [#D:not-a-row].\n")
        h = H.render_all(cfg, meta, out, outd, dict(files))
        ok("html: sidecar with an unknown id REJECTED", "Interpretation REJECTED" in h["pins/bbbb222.html"])
        with open(os.path.join(outd, "interpretation", "bbbb222.md"), "w") as f:
            f.write("- p1 faster [#%s].\n" % g("p1")["row_id"])
        h = H.render_all(cfg, meta, out, outd, dict(files))
        ok("html: valid sidecar rendered", "AI-written, grounded" in h["pins/bbbb222.html"])
    print("\n%s" % ("ALL PASS" if not fails else "FAILED: " + ", ".join(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
