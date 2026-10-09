#!/usr/bin/env python3
"""tools/trend.py -- THE pcrec TREND REPORT's generator ([B130],
docs/design/pcrec_trend_report_v0.md R1-R19, implementation note at its end).

    python3 tools/trend.py [--sets a,b] [--out reports/trend] [--check]   # COMPARE
    python3 tools/trend.py snapshot --pin <pin> [--force]   # reads store/, once per pin
    python3 tools/trend.py links [--write]                  # propose links.tsv rows

THE COMPARISON NEVER OPENS store/ ([B130.2], design note section 8): it reads
`reports/trend/snapshots/<pin>.tsv.gz` (one immutable file per pinned pcrec
version, tools/trend_snapshot.py), `links.tsv` (the explicit cross-version
links) and `config.toml`, and writes `reports/trend/`: the A-form TSVs (cells,
deltas, summary, movers_by_stamp, compile_deltas, deny_twins, interest,
records, history/<set>/<config>.tsv) and the B-form (index.html,
pins/<pin>.html, index.md; tools/trend_html.py). `snapshot` is the only
command that reads the store. Every number is computed here from the snapshots
through `pcrecbench.reduce` (the reporter's own set-grain arithmetic: per-trial
sum over subjects, median and [min, max] over trials). Nothing is typed by hand.

THE ARITHMETIC IN ONE PLACE
  * A record is a DIGEST (per cell, per subject, per trial: outcome and
    ns/call; per compile row: outcome and stamps): built once from the store
    by `snapshot` (cached under build/trend-cache/, a speed cache only) and
    stored in the snapshot; the comparison rebuilds it from the snapshot. A
    cell is rebuilt from a digest as synthetic match rows and handed to
    `reduce.reduce_set_cell`, so the number IS the reporter's.
  * ratio = NEW / OLD of the set-grain median (> 1: slower), as in O-92.
  * Like for like (R3): a delta needs equal pattern sha and is computed over
    the subjects present in BOTH records with equal sha. Otherwise `new` /
    `not-comparable`. A pair spanning two versions of a set needs a
    `set-version` row in links.tsv, else `unlinked` (never guessed).
  * Within-window noise (R4): trial [min, max] ranges overlap -> `within-noise`.
    Cross-window (R4+): disjoint ranges must also clear the identical-program
    band of that pair+regime (q95 of |ratio-1| over program-identical cells,
    fallback config `fallback_band`), else `within-identical-band`.
  * Identity (R6+): program_sha256 of the compile rows (program_identity v2).
    Equal -> yes. Unequal across abi 67 -> `unknown-abi67` (v2 is blind to
    abi 67's text normalization). Unequal otherwise -> no.
  * Drift (R5/R5+): per-cell same-cell ratio of the control engine's records
    nearest in time to each side, over subjects common to all four.
  * Instrument (R19): sha256 of testees/<engine>/{shim.c,driver.c,driver.cc,
    src/main.rs} at each record's run.harness_commit (git show).

Row ids (cited by the AI interpretation, R9): D:<set@ver>:<config>:<pin>:
<pattern>:<regime>:<form> (deltas.tsv), S:<set@ver>:<config>:<pin>:<prev>:
<regime> (summary.tsv), C:... (cells.tsv), K:... (compile_deltas.tsv).

DETERMINISM: no clock, no random; "as_of" is the newest record timestamp
used (the design note's "generation time" would break byte identity).
"""

import argparse
import csv
import fnmatch
import gzip
import hashlib
import json
import math
import os
import statistics
import subprocess
import sys
import tomllib
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from pcrecbench import reduce as R  # noqa: E402
import trend_snapshot as TS  # noqa: E402

GEN_VERSION = "trend-v1"
DIGEST_VERSION = "d2"   # cache key part: bump when build_digest changes
TSV_SCHEMA = "trend-tsv-1"
IDENTITY_CRITERION = ("program_sha256 (compile row engine_metadata, "
                      "tools/program_identity.py normalization v2); equal = "
                      "identical; unequal across abi 67 = unknown-abi67 "
                      "(v2 is blind to abi 67's text normalization)")
STAMP_KEYS = ("engine", "dfa_prefilter", "dfa_start", "req_why", "vm_start_scan")
ENGINE_DIR = {"libpcre2": "pcre2", "oniguruma": "onig"}
INSTR_FILES = ("shim.c", "driver.c", "driver.cc", "src/main.rs")
ABI_BLIND = 67
DEFAULT_CONFIG = os.path.join(ROOT, "reports", "trend", "config.toml")
DEFAULT_OUT = os.path.join(ROOT, "reports", "trend")
LINK_KINDS = ("set-version", "config-rename")
LINK_COLS = ["kind", "from", "to", "source", "reason"]


# ------------------------------------------------------------------ helpers

def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def fnum(x, nd=1):
    return "" if x is None else f"{x:.{nd}f}"


def frat(x):
    return "" if x is None else f"{x:.4f}"


def clean(v):
    if v is None:
        return ""
    return str(v).replace("\t", " ").replace("\n", " ").replace("\r", " ")


def read_tsv(path):
    """Rows of a trend TSV as dicts; '#' lines skipped."""
    with open(path, newline="", encoding="utf-8") as f:
        lines = [ln for ln in f if not ln.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t"))


def load_pin_order(rules_path):
    with open(rules_path, "rb") as f:
        d = tomllib.load(f)
    for blk in d.get("pin_order", []):
        if blk.get("engine") == "pcrec":
            return list(blk["pins"])
    raise SystemExit("trend: no [[pin_order]] engine=pcrec in " + rules_path)


def split_pcrec_id(tid):
    """pcrec_<pin>_<config> -> (pin, config), else None."""
    if not tid.startswith("pcrec_"):
        return None
    rest = tid[len("pcrec_"):]
    pin, _, cfg = rest.partition("_")
    return (pin, cfg) if cfg else None


def twin_base(cfg):
    """('auto-caps-simdna_noisland') -> 'auto-caps-simdna' for a deny twin
    (suffix token after '_' starting with 'no'); else None. A trailing
    '-utf8' on the suffix belongs to the base ('..._utf8')."""
    base, _, suf = cfg.partition("_")
    if not suf or not suf.startswith("no"):
        return None
    if suf.endswith("-utf8"):
        base += "_utf8"
    return base


# --------------------------------------------------------------- digests

def build_digest(path):
    setup, rows = R.read_record(path)
    t = setup.get("testee", {})
    run = setup.get("run", {})
    cells, rawt = {}, {}
    for r in rows:
        if r.get("kind") != "match":
            continue
        key = "\t".join((r.get("pattern_id"), r.get("regime"),
                         r.get("form") or "plain"))
        o = r.get("match_outcome")
        diag = "" if o == R.MATCHED else str(r.get("diagnostic") or "")[:200]
        cells.setdefault(key, {}).setdefault(r.get("subject_id"), []).append(
            [r.get("trial"), o, R.ns_per_call(r), diag])
        tm = r.get("timing") or {}
        rawt.setdefault(key, {}).setdefault(r.get("subject_id"), []).append(
            [tm.get("elapsed_ns"), tm.get("iterations")])
    comp = {}
    for r in rows:
        if r.get("kind") != "compile":
            continue
        k = r.get("pattern_id") + "\t" + (r.get("form") or "plain")
        e = comp.setdefault(k, {"outcome": r.get("compile_outcome"),
                                "ns": [], "meta": None, "diag": ""})
        if e["meta"] is None and r.get("engine_metadata"):
            e["meta"] = r["engine_metadata"]
        c = (r.get("cost") or {}).get("total_ns")
        if c is not None:
            e["ns"].append(c)
        if r.get("diagnostic") and not e["diag"]:
            e["diag"] = str(r["diagnostic"])[:200]
    abis = [e["meta"].get("abi") for e in comp.values()
            if e["meta"] and isinstance(e["meta"].get("abi"), int)]
    return {
        "path": path,
        "testee_id": t.get("testee_id"), "engine_name": t.get("engine_name"),
        "harness_commit": run.get("harness_commit"),
        "timestamp": run.get("timestamp"),
        "schema_version": setup.get("schema_version"),
        "abi": max(abis) if abis else None,
        "patterns": {p["pattern_id"]: p.get("canonical_sha256")
                     for p in setup.get("patterns", [])},
        "subjects": {s["subject_id"]: s.get("sha256")
                     for s in setup.get("subjects", [])},
        "cells": cells, "compile": comp, "rawt": rawt,
    }


def get_digest(path, cache_dir):
    st = os.stat(path)
    key = hashlib.sha1(f"{GEN_VERSION}|{DIGEST_VERSION}|{os.path.abspath(path)}|{st.st_size}|"
                       f"{st.st_mtime_ns}".encode()).hexdigest()
    cp = os.path.join(cache_dir, key + ".json.gz") if cache_dir else None
    if cp and os.path.exists(cp):
        try:
            with gzip.open(cp, "rt", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    d = build_digest(path)
    if cp:
        os.makedirs(cache_dir, exist_ok=True)
        tmp = cp + f".{os.getpid()}.tmp"
        with gzip.open(tmp, "wt", encoding="utf-8") as f:
            json.dump(d, f)
        os.replace(tmp, cp)
    return d


# ---------------------------------------------------------------- instrument

ERA1_FILES = ("driver.c", "driver.cc", "src/main.rs", "shim.c")
ERA2_FILES = ("timed.c", "timed.cc", "timed.h", "timed/Cargo.toml",
              "timed/src/lib.rs", "shim.c")
ERA2_MARK = ("timed.c", "timed.cc", "timed/src/lib.rs")


def instr_parse(s):
    """'era=2|shim.c:ab,timed.c:cd' -> (era, {file: sha}); an unstructured
    string (tests, 'unavailable') -> (None, {'': s})."""
    if not s.startswith("era="):
        return None, {"": s}
    era, _, rest = s.partition("|")
    return era[4:], dict(x.split(":", 1) for x in rest.split(",") if x)


def instr_diff(a, b):
    """Names of the hashed files that differ between two instrument strings
    ('era' when the eras differ: a pair straddling the [B133] boundary is
    instrument-changed by definition)."""
    ea, fa = instr_parse(a)
    eb, fb = instr_parse(b)
    out = []
    if ea != eb:
        out.append("era")
    for k in sorted(set(fa) | set(fb)):
        if fa.get(k) != fb.get(k):
            out.append(k or "instrument")
    return out


class Instrument:
    """R19, ERA-AWARE: sha256 of the bench sources entering the timed loop,
    at a commit. Era 2 (testees/<engine>/timed.* exists at the commit, lane
    b133loop / [B133]): {timed.*, shim.c where present}; era 1 (every earlier
    commit): {driver.c / driver.cc / src/main.rs, shim.c}."""

    def __init__(self, repo, enabled=True, override=None):
        self.repo, self.enabled, self.override = repo, enabled, override
        self._c = {}

    def _show(self, commit, d, fn):
        p = subprocess.run(["git", "-C", self.repo, "show",
                            f"{commit}:testees/{d}/{fn}"], capture_output=True)
        return (hashlib.sha256(p.stdout).hexdigest()[:12]
                if p.returncode == 0 else None)

    def of(self, commit, engine_name):
        if self.override is not None:
            return self.override(commit, engine_name)
        if not self.enabled or not commit:
            return "unavailable"
        d = ENGINE_DIR.get(engine_name, engine_name)
        k = (commit, d)
        if k not in self._c:
            era2 = any(self._show(commit, d, fn) for fn in ERA2_MARK)
            files = ERA2_FILES if era2 else ERA1_FILES
            parts = []
            for fn in files:
                h = self._show(commit, d, fn)
                if h:
                    parts.append(f"{fn}:{h}")
            self._c[k] = f"era={2 if era2 else 1}|" + ",".join(parts)
        return self._c[k]


# ------------------------------------------------------------------ cells

class Rec:
    """One chosen record: digest + identity fields."""

    def __init__(self, role, set_ver, tid, pin, config, path, dg, instr):
        self.role, self.set_ver, self.tid = role, set_ver, tid
        self.pin, self.config, self.path, self.dg = pin, config, path, dg
        self.ts = dg["timestamp"] or ""
        self.instr = instr
        self.memo = {}

    def rel(self):
        return self.path

    def common(self, other, pid, subs=None):
        """Subject ids present in both records with equal sha (for a cell key
        both have), sorted."""
        return None


def _lookup_subjects(rec, key):
    return rec.dg["cells"].get(key, {})


def reduce_cell(rec, key, subs):
    """SetCell summary of rec's cell `key` over subject ids `subs`
    (tuple), memoised. Uses reduce.reduce_set_cell on synthetic rows."""
    mk = (key, subs)
    if mk in rec.memo:
        return rec.memo[mk]
    cell = rec.dg["cells"].get(key, {})
    by = {}
    for sid in subs:
        rows = []
        for trial, o, ns, diag in cell.get(sid, []):
            rows.append({"kind": "match", "match_outcome": o, "trial": trial,
                         "timing": ({"elapsed_ns": ns, "iterations": 1}
                                    if ns is not None
                                    else {"elapsed_ns": 0, "iterations": 0}),
                         "diagnostic": diag})
        by[sid] = rows
    sc = R.reduce_set_cell(by)
    if sc.median_ns is not None:
        state = "judged"
    elif sc.n_wrong > 0:
        state = "wrong"
    elif sc.n_gave_up > 0:
        state = "gave-up"
    elif sc.n_no_expectation > 0:
        state = "no-expectation"
    else:
        state = "failing"
    out = {"state": state, "median": sc.median_ns, "min": sc.min_ns,
           "max": sc.max_ns, "n_subjects": sc.n_subjects,
           "n_trials": sc.n_trials, "n_wrong": sc.n_wrong,
           "n_gave_up": sc.n_gave_up}
    rec.memo[mk] = out
    return out


def compile_state(rec, pid, form):
    e = rec.dg["compile"].get(pid + "\t" + form)
    if e is None:
        return "absent"
    o = e["outcome"]
    if o == "compiled":
        return "compiled"
    if o == "did-not-compile":
        return "refused"
    if o and o.startswith("unsupported"):
        return "unsupported"
    return o or "absent"


def common_subjects(ra, rb, key):
    """Subjects of cell `key` present in both records with equal subject sha."""
    ca, cb = ra.dg["cells"].get(key), rb.dg["cells"].get(key)
    if not ca or not cb:
        return ()
    sa, sb = ra.dg["subjects"], rb.dg["subjects"]
    out = []
    for sid in ca:
        if sid in cb and sa.get(sid) is not None and sa.get(sid) == sb.get(sid):
            out.append(sid)
    return tuple(sorted(out))


def full_subjects(rec, key):
    return tuple(sorted(rec.dg["cells"].get(key, {})))


def cell_state(rec, key, subs=None):
    """(state, reduction-or-None) of a cell in rec, falling back to the
    compile row for a pattern with no match rows."""
    if key in rec.dg["cells"]:
        subs = subs if subs is not None else full_subjects(rec, key)
        red = reduce_cell(rec, key, subs)
        return red["state"], red
    pid, _rg, form = key.split("\t")
    cs = compile_state(rec, pid, form)
    return (cs if cs in ("refused", "unsupported") else "absent"), None


def abi_of(rec):
    return rec.dg.get("abi")


def comp_meta(rec, pid, form):
    e = rec.dg["compile"].get(pid + "\t" + form)
    return (e or {}).get("meta") or {}


def stamp_vals(rec, pid, form):
    m = comp_meta(rec, pid, form)
    return {k: clean(m.get(k)) for k in STAMP_KEYS}


def per_call(med, n):
    return None if med is None or not n else med / n


def disjoint(a, b):
    return b["max"] < a["min"] or b["min"] > a["max"]


# ------------------------------------------------------------ record choice

def select_records(index_rows, cfg, pin_order):
    """-> (records meta list for records.tsv, chosen {(set_ver, tid): meta}).
    R11: per (set_ver, testee_id) the newest `measured` record is used; every
    other record is listed with its disposition, never silently mixed."""
    machine = cfg["machine"]
    by = defaultdict(list)
    for r in index_rows:
        by[(f"{r['subbench']}@{r['version']}", r["testee_id"])].append(r)
    metas, chosen = [], {}
    for (sv, tid), rs in sorted(by.items()):
        rs = sorted(rs, key=lambda r: (r["timestamp"], r["path"]))
        role = classify(tid, cfg)
        if role is None:
            continue
        pc = split_pcrec_id(tid)
        pin, config = pc if pc else ("", "")
        usable = [r for r in rs if r["status"] == "measured"
                  and r["machine_id"] == machine]
        top = usable[-1] if usable else None
        for r in rs:
            if r["machine_id"] != machine:
                disp = "excluded-machine"
            elif r["status"] != "measured":
                disp = "excluded-status:" + r["status"]
            elif r is top:
                disp = "used"
            else:
                disp = "superseded"
            m = {"role": role, "set_ver": sv, "testee_id": tid, "config": config,
                 "pin": pin, "machine": r["machine_id"],
                 "timestamp": r["timestamp"], "status": r["status"],
                 "disposition": disp, "path": r["path"],
                 "superseded_by": top["path"] if disp == "superseded" and top else ""}
            if pin and pin not in pin_order:
                m["disposition"] = "excluded-unknown-pin"
            metas.append(m)
            if r is top and m["disposition"] == "used":
                chosen[(sv, tid)] = m
    return metas, chosen


def classify(tid, cfg):
    if split_pcrec_id(tid):
        return "pcrec"
    for g in cfg["control_globs"]:
        if fnmatch.fnmatch(tid, g):
            return "control"
    for g in cfg["competitor_globs"]:
        if fnmatch.fnmatch(tid, g):
            return "competitor"
    return None


# ------------------------------------------------------------- main compute

def nearest(recs, ts):
    """Record of `recs` nearest in time (ISO strings compare lexically; use
    the sorted position)."""
    if not recs:
        return None
    return min(recs, key=lambda r: (abs(iso_s(r.ts) - iso_s(ts)), r.ts, r.tid))


def iso_s(ts):
    import calendar
    import time
    try:
        return calendar.timegm(time.strptime(ts, "%Y-%m-%dT%H:%M:%SZ"))
    except Exception:
        return 0


def quantile(xs, q):
    xs = sorted(xs)
    if not xs:
        return None
    i = (len(xs) - 1) * q
    lo, hi = int(math.floor(i)), int(math.ceil(i))
    return xs[lo] + (xs[hi] - xs[lo]) * (i - lo)


def geomean(xs):
    xs = [x for x in xs if x and x > 0]
    return statistics.geometric_mean(xs) if xs else None


class Out:
    def __init__(self):
        self.cells, self.deltas, self.summary = [], [], []
        self.movers, self.compile, self.twins, self.history = [], [], [], []
        self.interest = []


def process_set(setname, pc, ctrl, comp, links, cfg, pin_order, out,
                interest_spec):
    """pc: the pcrec Recs of this set name; ctrl / comp: {(pin, set_ver):
    [Rec]} -- the control and competitor records stored in that pin's
    SNAPSHOT (the same window's), never looked up anywhere else."""
    pidx = {p: i for i, p in enumerate(pin_order)}
    if not pc:
        return

    # ---- cells.tsv rows (R7, R12, R16)
    for r in sorted(pc, key=lambda r: (pidx[r.pin], r.set_ver, r.config)):
        keys = sorted(r.dg["cells"])
        for key in keys:
            pid, rg, form = key.split("\t")
            subs = full_subjects(r, key)
            st, red = cell_state(r, key, subs)
            row = cell_row(r, key, st, red, subs)
            if red and red["median"] is not None:
                fill_competitors(row, r, key, subs, red,
                                 ctrl.get((r.pin, r.set_ver), []),
                                 comp.get((r.pin, r.set_ver), []), cfg)
            out.cells.append(row)
        for ck in sorted(r.dg["compile"]):
            pid, form = ck.split("\t")
            if compile_state(r, pid, form) in ("refused", "unsupported"):
                key = f"{pid}\t-\t{form}"
                if not any(k.startswith(pid + "\t") and k.endswith("\t" + form)
                           for k in r.dg["cells"]):
                    out.cells.append(cell_row(r, key, compile_state(r, pid, form),
                                              None, ()))

    # ---- deltas, per config along pin order (R2, R3)
    byconf = defaultdict(list)
    for r in pc:
        byconf[r.config].append(r)
    raw = []
    for config, rs in sorted(byconf.items()):
        rs.sort(key=lambda r: (pidx[r.pin], r.ts, r.set_ver))
        for j, new in enumerate(rs):
            keys = set(new.dg["cells"])
            for p in [x for x in rs[:j] if pidx[x.pin] < pidx[new.pin]]:
                keys |= set(p.dg["cells"])
            for key in sorted(keys):
                d = make_delta(new, [x for x in rs[:j] if pidx[x.pin] < pidx[new.pin]],
                               key, ctrl, cfg, pidx, links)
                if d:
                    raw.append(d)
    finish_deltas(raw, cfg, pin_order, out, ctrl)
    # compile/size deltas (Q2)
    compile_deltas(byconf, pidx, cfg, out, links)
    # deny twins (R17)
    deny_twins(pc, cfg, out)
    # cells of interest (R17)
    for sp in interest_spec:
        if sp["set"].split("@")[0] != setname:
            continue
        out.interest_pending = getattr(out, "interest_pending", [])
        out.interest_pending.append(sp)


def cell_row(r, key, st, red, subs):
    pid, rg, form = key.split("\t")
    meta = comp_meta(r, pid, form)
    cs = r.dg["compile"].get(pid + "\t" + form) or {}
    cns = statistics.median(cs["ns"]) if cs.get("ns") else None
    row = {
        "row_id": f"C:{r.set_ver}:{r.config}:{r.pin}:{pid}:{rg}:{form}",
        "set_ver": r.set_ver, "config": r.config, "pin": r.pin,
        "pattern": pid, "regime": rg, "form": form, "state": st,
        "median_ns": fnum(red["median"]) if red else "",
        "min_ns": fnum(red["min"]) if red else "",
        "max_ns": fnum(red["max"]) if red else "",
        "n_subjects": red["n_subjects"] if red else "",
        "n_trials": red["n_trials"] if red else "",
        "percall_ns": fnum(per_call(red["median"], red["n_subjects"]), 2) if red else "",
        "n_wrong": red["n_wrong"] if red else "",
        "n_gave_up": red["n_gave_up"] if red else "",
        "compile_outcome": cs.get("outcome") or "",
        "compile_median_ns": fnum(cns, 0),
        "emit_bytes": clean(meta.get("emit_bytes")),
        "emit_code_bytes": clean(meta.get("emit_code_bytes")),
        "program_sha256": clean(meta.get("program_sha256"))[:16],
        "engine_sel": clean(meta.get("engine_sel")),
        "jit_ns": "", "jit_ratio": "", "auto_best_engine": "",
        "auto_best_ratio": "",
        "instrument": r.instr, "record": r.path,
    }
    for k in STAMP_KEYS:
        row[k] = clean(meta.get(k))
    return row


def fill_competitors(row, r, key, subs, red, ctrls, comps, cfg):
    """R12: pcrec/competitor on the subjects both have (equal sha)."""
    pat = r.dg["patterns"].get(key.split("\t")[0])

    def ratio(other):
        if other is None or other.dg["patterns"].get(key.split("\t")[0]) != pat \
                or pat is None:
            return None, None
        cs = common_subjects(r, other, key)
        if not cs:
            return None, None
        a, b = reduce_cell(r, key, cs), reduce_cell(other, key, cs)
        if a["median"] is None or b["median"] is None or b["median"] == 0:
            return None, None
        return a["median"] / b["median"], b["median"]

    jit = nearest(ctrls, r.ts)
    rt, ns = ratio(jit)
    if rt is not None:
        row["jit_ns"], row["jit_ratio"] = fnum(ns), frat(rt)
    best = None
    for c in sorted(comps, key=lambda c: c.tid):
        rt, _ = ratio(c)
        if rt is not None and (best is None or rt > best[0]):
            best = (rt, c.tid)
    if best:
        row["auto_best_engine"], row["auto_best_ratio"] = best[1], frat(best[0])


def make_delta(new, earlier, key, ctrls, cfg, pidx, links):
    pid, rg, form = key.split("\t")
    # newest earlier record with this cell comparable (R2)
    prev = None
    newer_has = key in new.dg["cells"] or compile_state(new, pid, form) in (
        "refused", "unsupported")
    for p in reversed(earlier):
        if key in p.dg["cells"] or compile_state(p, pid, form) in (
                "refused", "unsupported"):
            prev = p
            break
    if not newer_has and prev is None:
        return None
    base = {"set_ver": new.set_ver, "config": new.config, "pin": new.pin,
            "pattern": pid, "regime": rg, "form": form, "record_new": new.path}
    if prev is None:
        if key not in new.dg["cells"]:
            return None
        st, red = cell_state(new, key)
        base.update(prev_pin="", prev_set_ver="", verdict="new", state_new=st,
                    ns_new=red and red["median"], rec_new=new, rec_prev=None)
        return base
    base.update(prev_pin=prev.pin, prev_set_ver=prev.set_ver,
                record_prev=prev.path, rec_new=new, rec_prev=prev,
                verdict="pending")
    if not links.set_ok(prev.set_ver, new.set_ver):
        base.update(verdict="unlinked",
                    why=f"no set-version link {prev.set_ver} ~ {new.set_ver} "
                        f"in links.tsv")
        return base
    pn, pp = new.dg["patterns"].get(pid), prev.dg["patterns"].get(pid)
    if pn is None or pp is None or pn != pp:
        base.update(verdict="not-comparable",
                    why="pattern bytes changed" if pn and pp else "no pattern sha")
        return base
    if key in new.dg["cells"] and key in prev.dg["cells"]:
        cs = common_subjects(prev, new, key)
        if not cs:
            base.update(verdict="not-comparable", why="no common subjects")
            return base
        a = reduce_cell(prev, key, cs)
        b = reduce_cell(new, key, cs)
        base.update(cs=cs, a=a, b=b, state_prev=a["state"], state_new=b["state"],
                    n_prev=len(prev.dg["cells"][key]), n_new=len(new.dg["cells"][key]))
    else:
        sa, ra = cell_state(prev, key)
        sb, rb = cell_state(new, key)
        base.update(cs=(), a=ra, b=rb, state_prev=sa, state_new=sb,
                    n_prev=0, n_new=0)
    return base


def finish_deltas(raw, cfg, pin_order, out, ctrls):
    # pass 1: ratios, disjointness, identity, control
    ctrl_cache = {}
    groups = defaultdict(list)
    for d in raw:
        d["row_id"] = (f"D:{d['set_ver']}:{d['config']}:{d['pin']}:"
                       f"{d['pattern']}:{d['regime']}:{d['form']}")
        if d["verdict"] == "new":
            continue
        new, prev = d["rec_new"], d["rec_prev"]
        d["abi_prev"], d["abi_new"] = abi_of(prev), abi_of(new)
        d["abi_span"] = (d["abi_new"] - d["abi_prev"]
                         if d["abi_new"] is not None and d["abi_prev"] is not None
                         else None)
        d["wide_gap"] = d["abi_span"] is not None and d["abi_span"] > cfg["wide_gap_abi"]
        d["instrument_changed"] = new.instr != prev.instr
        d["instrument_files"] = ";".join(instr_diff(prev.instr, new.instr))
        if d["verdict"] in ("not-comparable", "unlinked"):
            continue
        a, b = d["a"], d["b"]
        d["ratio"] = None
        d["transition"] = ""
        sp, sn = d["state_prev"], d["state_new"]
        if sp != sn:
            d["transition"] = f"{sp}->{sn}"
        pid, form = d["pattern"], d["form"]
        pm, nm = comp_meta(prev, pid, form), comp_meta(new, pid, form)
        sp_, sn_ = clean(pm.get("program_sha256")), clean(nm.get("program_sha256"))
        if sp_ and sp_ == sn_:
            d["identical"] = "yes"
        elif sp_ and sn_ and d["abi_prev"] is not None and d["abi_new"] is not None \
                and d["abi_prev"] < ABI_BLIND <= d["abi_new"]:
            d["identical"] = "unknown-abi67"
        elif sp_ and sn_:
            d["identical"] = "no"
        else:
            d["identical"] = "unknown"
        d["prog_prev"], d["prog_new"] = sp_[:12], sn_[:12]
        if a and b and a["median"] is not None and b["median"] is not None \
                and a["median"] > 0:
            d["ratio"] = b["median"] / a["median"]
            d["disjoint"] = disjoint(a, b)
            d["control_ratio"], d["control_info"] = control_ratio(
                d, ctrls, ctrl_cache)
        groups[(d["set_ver"], d["config"], d["pin"], d["prev_pin"],
                d["prev_set_ver"], d["regime"])].append(d)
    # pass 2: identical-program band per pair+regime, verdicts
    for gk, ds in sorted(groups.items()):
        ident = [abs(d["ratio"] - 1.0) for d in ds
                 if d.get("ratio") and d["identical"] == "yes"]
        if len(ident) >= cfg["band_min_cells"]:
            band, bsrc = quantile(ident, 0.95), "q95-identical"
        else:
            band, bsrc = cfg["fallback_band"], "fallback"
        for d in ds:
            d["band"], d["band_src"], d["n_ident_cells"] = band, bsrc, len(ident)
            if d.get("ratio") is None:
                d["verdict"] = "no-number" if d["transition"] else "same-state"
            elif not d["disjoint"]:
                d["verdict"] = "within-noise"
            elif abs(d["ratio"] - 1.0) <= band:
                d["verdict"] = "within-identical-band"
            else:
                d["verdict"] = "faster" if d["ratio"] < 1 else "slower"
    # emit delta rows + summary + movers
    for d in raw:
        out.deltas.append(delta_row(d))
    summarize(groups, cfg, out)
    out.raw_deltas = raw
    out.raw_deltas_all = getattr(out, "raw_deltas_all", []) + raw


def control_ratio(d, ctrls, cache):
    new, prev = d["rec_new"], d["rec_prev"]
    cn = nearest(ctrls.get((new.pin, new.set_ver), []), new.ts)
    cp = nearest(ctrls.get((prev.pin, prev.set_ver), []), prev.ts)
    if cn is None or cp is None:
        return None, "no-control"
    key = f"{d['pattern']}\t{d['regime']}\t{d['form']}"
    if cn is cp:
        return None, "control-same-record"
    if cp.dg["patterns"].get(d["pattern"]) != prev.dg["patterns"].get(d["pattern"]) \
            or cn.dg["patterns"].get(d["pattern"]) != cp.dg["patterns"].get(d["pattern"]):
        return None, "control-pattern-differs"
    cs = [s for s in d["cs"]
          if s in cp.dg["cells"].get(key, {}) and s in cn.dg["cells"].get(key, {})
          and cp.dg["subjects"].get(s) == prev.dg["subjects"].get(s)
          and cn.dg["subjects"].get(s) == prev.dg["subjects"].get(s)]
    if not cs:
        return None, "control-no-common"
    cs = tuple(sorted(cs))
    a, b = reduce_cell(cp, key, cs), reduce_cell(cn, key, cs)
    if a["median"] is None or b["median"] is None or a["median"] == 0:
        return None, "control-no-number"
    return b["median"] / a["median"], f"{cp.ts[:10]}>{cn.ts[:10]}"


def delta_row(d):
    new = d["rec_new"]
    base = {"row_id": d["row_id"], "set_ver": d["set_ver"],
            "prev_set_ver": d.get("prev_set_ver", ""), "config": d["config"],
            "pin": d["pin"], "prev_pin": d.get("prev_pin", ""),
            "pattern": d["pattern"], "regime": d["regime"], "form": d["form"],
            "verdict": d["verdict"], "why": d.get("why", "")}
    keys = ["ratio", "state_prev", "state_new", "transition", "ns_prev", "ns_new",
            "min_prev", "max_prev", "min_new", "max_new", "percall_prev",
            "percall_new", "n_common_subjects", "n_subjects_prev",
            "n_subjects_new", "identical", "prog_prev", "prog_new", "abi_prev",
            "abi_new", "abi_span", "band", "band_src", "control_ratio",
            "control_windows", "cell_drift_suspect", "instrument_changed",
            "wide_gap", "stamp_changes"] + [k + "_new" for k in STAMP_KEYS] + [
            "record_prev", "record_new"]
    row = dict(base)
    for k in keys:
        row[k] = ""
    row["record_new"] = new.path
    if d["verdict"] == "new":
        row["state_new"] = d.get("state_new", "")
        row["ns_new"] = fnum(d.get("ns_new"))
        return row
    prev = d["rec_prev"]
    row["record_prev"] = prev.path
    row["abi_prev"], row["abi_new"] = clean(d.get("abi_prev")), clean(d.get("abi_new"))
    row["abi_span"] = clean(d.get("abi_span"))
    row["wide_gap"] = int(d.get("wide_gap", False))
    row["instrument_changed"] = int(d.get("instrument_changed", False))
    row["instrument_changed_files"] = d.get("instrument_files", "")
    if d["verdict"] in ("not-comparable", "unlinked"):
        return row
    a, b = d["a"], d["b"]
    row["ratio"] = frat(d.get("ratio"))
    row["state_prev"], row["state_new"] = d["state_prev"], d["state_new"]
    row["transition"] = d["transition"]
    row["identical"] = d["identical"]
    row["prog_prev"], row["prog_new"] = d["prog_prev"], d["prog_new"]
    if a:
        row.update(ns_prev=fnum(a["median"]), min_prev=fnum(a["min"]),
                   max_prev=fnum(a["max"]),
                   percall_prev=fnum(per_call(a["median"], a["n_subjects"]), 2),
                   n_subjects_prev=a["n_subjects"])
    if b:
        row.update(ns_new=fnum(b["median"]), min_new=fnum(b["min"]),
                   max_new=fnum(b["max"]),
                   percall_new=fnum(per_call(b["median"], b["n_subjects"]), 2),
                   n_subjects_new=b["n_subjects"])
    row["n_common_subjects"] = len(d["cs"])
    row["band"] = frat(d.get("band"))
    row["band_src"] = d.get("band_src", "")
    cr = d.get("control_ratio")
    row["control_ratio"] = frat(cr)
    row["control_windows"] = (d.get("control_info") or "")
    row["_cr"] = cr
    ch = []
    pm = comp_meta(prev, d["pattern"], d["form"])
    nm = comp_meta(new, d["pattern"], d["form"])
    for k in STAMP_KEYS:
        o, n = clean(pm.get(k)), clean(nm.get(k))
        row[k + "_new"] = n
        if o != n:
            ch.append(f"{k}:{o or '-'}>{n or '-'}")
    row["stamp_changes"] = ";".join(ch)
    return row


def summarize(groups, cfg, out):
    lo, hi = cfg["drift_band"]
    clo, chi = cfg["cell_drift_band"]
    for gk, ds in sorted(groups.items()):
        sv, config, pin, ppin, psv, rg = gk
        num = [d for d in ds if d.get("ratio")]
        for d in num:
            cr = d.get("control_ratio")
            d["cell_drift"] = cr is not None and not (clo <= cr <= chi)
        # annotate emitted rows
        n = len(num)
        faster = [d for d in num if d["verdict"] == "faster"]
        slower = [d for d in num if d["verdict"] == "slower"]
        ident = [d for d in num if d["identical"] == "yes"]
        ident_moved = [d for d in ident if d["disjoint"]]
        crs = [d["control_ratio"] for d in num if d.get("control_ratio")]
        cmed = statistics.median(crs) if crs else None
        drift = cmed is not None and not (lo <= cmed <= hi)
        rs = [d["ratio"] for d in num]
        idr = sorted(abs(d["ratio"] - 1) for d in ident)
        trans = [d for d in ds if d.get("transition")]
        top = sorted([d for d in faster], key=lambda d: d["ratio"])[:3] + \
            sorted([d for d in slower], key=lambda d: -d["ratio"])[:3]
        first = ds[0]
        out.summary.append({
            "row_id": f"S:{sv}:{config}:{pin}:{ppin}:{rg}",
            "set_ver": sv, "prev_set_ver": psv, "config": config, "pin": pin,
            "prev_pin": ppin, "regime": rg, "n_cells": len(ds), "n_numeric": n,
            "n_faster": len(faster), "n_slower": len(slower),
            "n_within_noise": sum(1 for d in num if d["verdict"] == "within-noise"),
            "n_within_identical_band": sum(1 for d in num
                                           if d["verdict"] == "within-identical-band"),
            "median_ratio": frat(statistics.median(rs)) if rs else "",
            "geomean_ratio": frat(geomean(rs)),
            "n_identical": len(ident), "n_identical_moved": len(ident_moved),
            "identical_median_abs_dev": frat(statistics.median(idr)) if idr else "",
            "identical_max_abs_dev": frat(idr[-1]) if idr else "",
            "band": frat(first.get("band")), "band_src": first.get("band_src", ""),
            "control_median_ratio": frat(cmed),
            "n_control_cells": len(crs),
            "drift_suspect": int(drift),
            "n_drift_suspect_cells": sum(1 for d in num if d.get("cell_drift")),
            "abi_span": clean(first.get("abi_span")),
            "wide_gap": int(bool(first.get("wide_gap"))),
            "instrument_changed": int(bool(first.get("instrument_changed"))),
            "instrument_changed_files": first.get("instrument_files", ""),
            "n_correctness_changes": len(trans),
            "top_movers": ";".join(d["row_id"] for d in top),
            "identity_criterion": "program_sha256-v2",
        })
        for d in num:
            d["row_cell_drift"] = d["cell_drift"]
        # R13 movers grouped by stamp value
        movers = [d for d in faster + slower if d["identical"] != "yes"]
        g = defaultdict(list)
        for d in movers:
            pm = comp_meta(d["rec_prev"], d["pattern"], d["form"])
            nm = comp_meta(d["rec_new"], d["pattern"], d["form"])
            for k in STAMP_KEYS:
                g[(k, clean(pm.get(k)), clean(nm.get(k)))].append(d)
        for (k, o, nv), l in sorted(g.items()):
            rr = [x["ratio"] for x in l]
            out.movers.append({
                "set_ver": sv, "config": config, "pin": pin, "prev_pin": ppin,
                "regime": rg, "stamp": k, "prev_value": o, "new_value": nv,
                "changed": int(o != nv), "n_movers": len(l),
                "n_faster": sum(1 for x in l if x["verdict"] == "faster"),
                "n_slower": sum(1 for x in l if x["verdict"] == "slower"),
                "geomean_ratio": frat(geomean(rr)),
                "example_rows": ";".join(x["row_id"] for x in l[:3]),
            })


def compile_deltas(byconf, pidx, cfg, out, links):
    ts, tc = cfg["size_threshold"], cfg["compile_threshold"]
    for config, rs in sorted(byconf.items()):
        for j, new in enumerate(rs):
            for ck in sorted(new.dg["compile"]):
                pid, form = ck.split("\t")
                prev = None
                for p in reversed([x for x in rs[:j] if pidx[x.pin] < pidx[new.pin]]):
                    if ck in p.dg["compile"] and \
                            p.dg["patterns"].get(pid) == new.dg["patterns"].get(pid):
                        prev = p
                        break
                if prev is None or not links.set_ok(prev.set_ver, new.set_ver):
                    continue
                o, n = prev.dg["compile"][ck], new.dg["compile"][ck]
                om, nm = o.get("meta") or {}, n.get("meta") or {}

                def ratio(a, b):
                    try:
                        a, b = float(a), float(b)
                        return b / a if a else None
                    except (TypeError, ValueError):
                        return None
                eb = ratio(om.get("emit_bytes"), nm.get("emit_bytes"))
                ec = ratio(om.get("emit_code_bytes"), nm.get("emit_code_bytes"))
                co = statistics.median(o["ns"]) if o["ns"] else None
                cn = statistics.median(n["ns"]) if n["ns"] else None
                cr = cn / co if co and cn else None
                cdis = bool(o["ns"] and n["ns"] and
                            (min(n["ns"]) > max(o["ns"]) or max(n["ns"]) < min(o["ns"])))
                hl_size = ec is not None and abs(ec - 1) >= ts
                hl_comp = cr is not None and cdis and abs(cr - 1) >= tc
                outc_change = o["outcome"] != n["outcome"]
                if not (hl_size or hl_comp or outc_change) and not cfg.get("emit_all_compile"):
                    continue
                out.compile.append({
                    "row_id": f"K:{new.set_ver}:{config}:{new.pin}:{pid}:{form}",
                    "set_ver": new.set_ver, "config": config, "pin": new.pin,
                    "prev_pin": prev.pin, "pattern": pid, "form": form,
                    "outcome_prev": o["outcome"], "outcome_new": n["outcome"],
                    "emit_bytes_prev": clean(om.get("emit_bytes")),
                    "emit_bytes_new": clean(nm.get("emit_bytes")),
                    "emit_bytes_ratio": frat(eb),
                    "emit_code_bytes_prev": clean(om.get("emit_code_bytes")),
                    "emit_code_bytes_new": clean(nm.get("emit_code_bytes")),
                    "emit_code_bytes_ratio": frat(ec),
                    "compile_ns_prev": fnum(co, 0), "compile_ns_new": fnum(cn, 0),
                    "compile_ratio": frat(cr), "compile_ranges_disjoint": int(cdis),
                    "identical": ("yes" if om.get("program_sha256")
                                  and om.get("program_sha256") == nm.get("program_sha256")
                                  else "no-or-unknown"),
                    "highlight_size": int(hl_size), "highlight_compile": int(hl_comp),
                    "outcome_changed": int(outc_change),
                    "instrument_changed": int(new.instr != prev.instr),
                })


def deny_twins(pc, cfg, out):
    by = {(r.set_ver, r.pin, r.config): r for r in pc}
    for (sv, pin, config), tw in sorted(by.items()):
        b = twin_base(config)
        if not b or (sv, pin, b) not in by:
            continue
        base = by[(sv, pin, b)]
        gap_h = abs(iso_s(tw.ts) - iso_s(base.ts)) / 3600.0
        for key in sorted(set(base.dg["cells"]) & set(tw.dg["cells"])):
            pid, rg, form = key.split("\t")
            if base.dg["patterns"].get(pid) != tw.dg["patterns"].get(pid):
                continue
            cs = common_subjects(base, tw, key)
            if not cs:
                continue
            a, c = reduce_cell(base, key, cs), reduce_cell(tw, key, cs)
            if a["median"] is None or c["median"] is None:
                continue
            ratio = c["median"] / a["median"]
            pa = clean(comp_meta(base, pid, form).get("program_sha256"))
            pb = clean(comp_meta(tw, pid, form).get("program_sha256"))
            out.twins.append({
                "row_id": f"T:{sv}:{config}:{pin}:{pid}:{rg}:{form}",
                "set_ver": sv, "pin": pin, "base_config": b, "deny_config": config,
                "pattern": pid, "regime": rg, "form": form,
                "ratio_deny_over_base": frat(ratio),
                "ns_base": fnum(a["median"]), "ns_deny": fnum(c["median"]),
                "ranges_disjoint": int(disjoint(a, c)),
                "program_identical": "yes" if pa and pa == pb else "no",
                "window_gap_hours": fnum(gap_h, 1),
                "cross_window": int(gap_h > cfg["same_window_hours"]),
                "n_common_subjects": len(cs),
                "instrument_changed": int(base.instr != tw.instr),
            })


# ------------------------------------------------------------ interest file

def load_interest(path):
    if not path or not os.path.exists(path):
        return []
    out = []
    with open(path, newline="", encoding="utf-8") as f:
        lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    for r in csv.DictReader(lines, delimiter="\t"):
        r = {k: (v or "").strip() for k, v in r.items()}
        if r.get("mechanism") and r.get("pattern"):
            out.append(r)
    return out


def interest_rows(out, spec):
    """Join the interest spec onto deltas.tsv rows (any config, any pin)."""
    rows = []
    for sp in spec:
        for d in out.deltas:
            if d["set_ver"].split("@")[0] != sp["set"].split("@")[0]:
                continue
            if sp["set"] and "@" in sp["set"] and d["set_ver"] != sp["set"]:
                continue
            if d["pattern"] != sp["pattern"]:
                continue
            if sp.get("regime") and d["regime"] != sp["regime"]:
                continue
            if sp.get("form") and d["form"] != sp["form"]:
                continue
            if not d["ratio"]:
                continue
            rows.append({"mechanism": sp["mechanism"], "role": sp.get("role", ""),
                         "note": sp.get("note", ""), "delta_row_id": d["row_id"],
                         "set_ver": d["set_ver"], "config": d["config"],
                         "pin": d["pin"], "prev_pin": d["prev_pin"],
                         "pattern": d["pattern"], "regime": d["regime"],
                         "form": d["form"], "ratio": d["ratio"],
                         "verdict": d["verdict"], "identical": d["identical"],
                         "instrument_changed": d["instrument_changed"]})
    return rows


# ------------------------------------------------------------------ writing

def header_lines(name, meta, extra=()):
    h = [f"# trend_report: {name}", f"# schema: {TSV_SCHEMA}",
         f"# generator: {GEN_VERSION}"]
    for k in ("snapshots_sha256", "links_sha256", "links", "config_sha256",
              "pin_order_sha256", "as_of",
              "identity_criterion", "wide_gap_abi", "fallback_band",
              "direction"):
        h.append(f"# {k}: {meta[k]}")
    h.extend(extra)
    return h


def tsv_text(name, meta, cols, rows, extra=()):
    lines = header_lines(name, meta, extra)
    lines.append("\t".join(cols))
    for r in rows:
        lines.append("\t".join(clean(r.get(c, "")) for c in cols))
    return "\n".join(lines) + "\n"


CELL_COLS = ["row_id", "set_ver", "config", "pin", "pattern", "regime", "form",
             "state", "median_ns", "min_ns", "max_ns", "n_subjects", "n_trials",
             "percall_ns", "n_wrong", "n_gave_up", "compile_outcome",
             "compile_median_ns", "emit_bytes", "emit_code_bytes",
             "program_sha256", "engine_sel"] + list(STAMP_KEYS) + [
             "jit_ns", "jit_ratio", "auto_best_engine", "auto_best_ratio",
             "instrument", "record"]
DELTA_COLS = ["row_id", "set_ver", "prev_set_ver", "config", "pin", "prev_pin",
              "pattern", "regime", "form", "verdict", "why", "ratio", "state_prev",
              "state_new", "transition", "ns_prev", "ns_new", "min_prev", "max_prev",
              "min_new", "max_new", "percall_prev", "percall_new",
              "n_common_subjects", "n_subjects_prev", "n_subjects_new",
              "identical", "prog_prev", "prog_new", "abi_prev", "abi_new",
              "abi_span", "band", "band_src", "control_ratio", "control_windows",
              "cell_drift_suspect", "instrument_changed",
              "instrument_changed_files", "wide_gap", "stamp_changes"] + [k + "_new" for k in STAMP_KEYS] + [
              "record_prev", "record_new"]
SUMMARY_COLS = ["row_id", "set_ver", "prev_set_ver", "config", "pin", "prev_pin",
                "regime", "n_cells", "n_numeric", "n_faster", "n_slower",
                "n_within_noise", "n_within_identical_band", "median_ratio",
                "geomean_ratio", "n_identical", "n_identical_moved",
                "identical_median_abs_dev", "identical_max_abs_dev", "band",
                "band_src", "control_median_ratio", "n_control_cells",
                "drift_suspect", "n_drift_suspect_cells", "abi_span", "wide_gap",
                "instrument_changed", "instrument_changed_files",
                "n_correctness_changes", "top_movers",
                "identity_criterion"]
MOVER_COLS = ["set_ver", "config", "pin", "prev_pin", "regime", "stamp",
              "prev_value", "new_value", "changed", "n_movers", "n_faster",
              "n_slower", "geomean_ratio", "example_rows"]
COMPILE_COLS = ["row_id", "set_ver", "config", "pin", "prev_pin", "pattern",
                "form", "outcome_prev", "outcome_new", "emit_bytes_prev",
                "emit_bytes_new", "emit_bytes_ratio", "emit_code_bytes_prev",
                "emit_code_bytes_new", "emit_code_bytes_ratio", "compile_ns_prev",
                "compile_ns_new", "compile_ratio", "compile_ranges_disjoint",
                "identical", "highlight_size", "highlight_compile",
                "outcome_changed", "instrument_changed"]
TWIN_COLS = ["row_id", "set_ver", "pin", "base_config", "deny_config", "pattern",
             "regime", "form", "ratio_deny_over_base", "ns_base", "ns_deny",
             "ranges_disjoint", "program_identical", "window_gap_hours",
             "cross_window", "n_common_subjects", "instrument_changed"]
INTEREST_COLS = ["mechanism", "role", "note", "delta_row_id", "set_ver", "config",
                 "pin", "prev_pin", "pattern", "regime", "form", "ratio",
                 "verdict", "identical", "instrument_changed"]
RECORD_COLS = ["role", "set_ver", "testee_id", "config", "pin", "machine",
               "timestamp", "status", "disposition", "superseded_by", "path",
               "harness_commit", "instrument", "abi"]
HISTORY_COLS = ["pin_idx", "pin", "set_ver", "pattern", "regime", "form", "state",
                "median_ns", "min_ns", "max_ns", "percall_ns", "emit_code_bytes",
                "program_sha256", "delta_row_id", "prev_pin", "ratio_vs_prev",
                "verdict"]

INTEREST_TEMPLATE = """# cells_of_interest.tsv -- pcrec's INPUT to the trend report (R17).
# One row per cell of a mechanism under study; the report renders one section
# per mechanism and joins each row to deltas.tsv (every config, every pin pair).
# Columns (tab-separated): mechanism, role (target|carveout), set (name or
# name@version), pattern, regime (optional), form (optional), note.
# Lines starting with '#' are ignored. Fill below the header row.
mechanism\trole\tset\tpattern\tregime\tform\tnote
"""


# ------------------------------------------------------------------- links

class Links:
    """The explicit cross-version links the comparison may use
    (reports/trend/links.tsv). Kinds: `set-version` (an UNDIRECTED pair of
    versions of one set whose records a delta may span) and `config-rename`
    (from -> to: records of `from` are read as config `to`). A pair that would
    need an unlisted link is `unlinked`, never guessed. `allow_all` is the
    proposal mode only (`trend.py links`): it permits every pair and counts
    the ones it used in `seen`."""

    def __init__(self, rows=(), allow_all=False):
        self.rows = list(rows)
        self.allow_all = allow_all
        self.sv = {frozenset((r["from"], r["to"])) for r in self.rows
                   if r["kind"] == "set-version"}
        self.rename = {r["from"]: r["to"] for r in self.rows
                       if r["kind"] == "config-rename"}
        self.seen = defaultdict(int)

    def set_ok(self, a, b):
        if a == b:
            return True
        self.seen[tuple(sorted((a, b)))] += 1
        return self.allow_all or frozenset((a, b)) in self.sv

    def config(self, c):
        return self.rename.get(c, c)

    def counts(self):
        conf = sum(1 for r in self.rows if r["source"] == "confirmed")
        return f"{len(self.rows)} ({conf} confirmed, {len(self.rows) - conf} inferred)"


def load_links(path):
    """Rows of links.tsv (validated: closed kinds, closed sources, no
    duplicates); a missing file is an empty link set."""
    if not path or not os.path.exists(path):
        return Links()
    rows = read_tsv(path)
    seen = set()
    for r in rows:
        if r.get("kind") not in LINK_KINDS:
            raise SystemExit(f"trend: {path}: unknown link kind {r.get('kind')!r}")
        if r.get("source") not in ("inferred", "confirmed"):
            raise SystemExit(f"trend: {path}: source must be inferred|confirmed: {r}")
        k = (r["kind"], frozenset((r["from"], r["to"])) if r["kind"] == "set-version"
             else (r["from"], r["to"]))
        if k in seen:
            raise SystemExit(f"trend: {path}: duplicate link {r['kind']} {r['from']} {r['to']}")
        seen.add(k)
    return Links(rows)


# --------------------------------------------------------- snapshot loading

def load_snapshots(snap_dir, links, sets_filter=None):
    """Read every snapshot under snap_dir. -> (metas, pcrec Recs, ctrl pool,
    comp pool, pins_present). The ONLY inputs of the comparison; store/ is
    never touched. A record stored `ref:<pin>` is resolved to the snapshot
    holding it inline; control/competitor Recs are shared objects across the
    pins that reference them (so `control-same-record` is an identity test)."""
    files = sorted(fn for fn in os.listdir(snap_dir) if fn.endswith(".tsv.gz")) \
        if os.path.isdir(snap_dir) else []
    loaded = []
    for fn in files:
        header, recs = TS.read_snapshot(os.path.join(snap_dir, fn))
        loaded.append((fn[:-len(".tsv.gz")], header, recs))
    dg_of = {}
    for _pin, _h, recs in loaded:
        for r in recs:
            if r.get("dg") is not None:
                dg_of.setdefault(r["path"], r["dg"])
    rec_obj = {}
    metas_by_path = {}
    pcrec, ctrl, comp = [], defaultdict(list), defaultdict(list)
    for pin, _h, recs in loaded:
        for r in recs:
            role = r["role"]
            m = {"role": role, "set_ver": r["set_ver"], "testee_id": r["testee_id"],
                 "config": links.config(r["config"]) if role == "pcrec" else r["config"],
                 "pin": r["pin"], "machine": r["machine"],
                 "timestamp": r["timestamp"], "status": r["status"],
                 "disposition": r["disposition"],
                 "superseded_by": r["superseded_by"], "path": r["path"],
                 "harness_commit": r["harness_commit"], "instrument": r["instrument"],
                 "abi": r["abi"]}
            old = metas_by_path.get(r["path"])
            if old is None or (m["disposition"] == "used"
                               and old["disposition"] != "used"):
                metas_by_path[r["path"]] = m
            if r["data"] == "none":
                continue
            dg = dg_of.get(r["path"])
            if dg is None:
                raise SystemExit(f"trend: snapshot {pin}: {r['path']} is stored "
                                 f"{r['data']} but no snapshot holds it inline")
            if sets_filter and r["set_ver"].split("@")[0] not in sets_filter:
                continue
            rec = rec_obj.get(r["path"])
            if rec is None:
                rec = rec_obj[r["path"]] = Rec(role, r["set_ver"], r["testee_id"],
                                               r["pin"], m["config"], r["path"], dg,
                                               r["instrument"])
            if role == "pcrec":
                pcrec.append(rec)
            elif role == "control":
                ctrl[(pin, r["set_ver"])].append(rec)
            elif role == "competitor":
                comp[(pin, r["set_ver"])].append(rec)
    for pool in (ctrl, comp):
        for k in pool:
            pool[k].sort(key=lambda x: x.tid)
    metas = sorted(metas_by_path.values(), key=lambda m: m["path"])
    return metas, pcrec, ctrl, comp, sorted(p for p, _h, _r in loaded)


def build_outputs(args, links=None):
    """The comparison, from snapshot files + links + config ONLY."""
    cfg = load_config(args.config)
    pin_order = load_pin_order(args.rules)
    links = links if links is not None else load_links(args.links)
    sets_f = set(args.sets.split(",")) if args.sets else None
    metas, pcrec, ctrl, comp, snap_pins = load_snapshots(args.snapshots, links, sets_f)
    if sets_f:
        metas = [m for m in metas if m["set_ver"].split("@")[0] in sets_f]
    out = Out()
    interest_spec = load_interest(args.interest)
    names = sorted({r.set_ver.split("@")[0] for r in pcrec})
    for nm in names:
        process_set(nm, [r for r in pcrec if r.set_ver.split("@")[0] == nm],
                    ctrl, comp, links, cfg, pin_order, out, interest_spec)
        sys.stderr.write(f"trend: {nm} done ({len(out.cells)} cells, "
                         f"{len(out.deltas)} deltas)\n")
    used_ts = [m["timestamp"] for m in metas if m["disposition"] == "used"
               and m["role"] == "pcrec"]
    pins_used = {m["pin"] for m in metas if m["role"] == "pcrec"
                 and m["disposition"] == "used"}
    skipped = [p for p in pin_order if p not in pins_used]
    meta = {
        "snapshots_sha256": TS.snapshots_digest(args.snapshots),
        "links_sha256": sha_file(args.links) if os.path.exists(args.links) else "none",
        "links": links.counts(),
        "config_sha256": sha_file(args.config),
        "pin_order_sha256": hashlib.sha256("\n".join(pin_order).encode()).hexdigest(),
        "as_of": max(used_ts) if used_ts else "",
        "identity_criterion": IDENTITY_CRITERION,
        "wide_gap_abi": cfg["wide_gap_abi"],
        "fallback_band": cfg["fallback_band"],
        "direction": "ratio = new/old of the set-grain median (>1 slower)",
        "pins_without_records": ",".join(skipped),
        "pin_order": ",".join(pin_order),
    }
    return cfg, meta, metas, out, pin_order, interest_spec


def load_config(path):
    with open(path, "rb") as f:
        d = tomllib.load(f)
    d.setdefault("machine", "budu-ryzen1600")
    d.setdefault("control_globs", ["libpcre2_*_jit-caps-simdna"])
    d.setdefault("competitor_globs", [])
    d.setdefault("headline_configs", ["auto-caps-simdna", "auto-nocaps-simdna"])
    d.setdefault("wide_gap_abi", 8)
    d.setdefault("fallback_band", 0.0846)
    d.setdefault("band_min_cells", 10)
    d.setdefault("drift_band", [0.97, 1.03])
    d.setdefault("cell_drift_band", [0.90, 1.10])
    d.setdefault("size_threshold", 0.10)
    d.setdefault("compile_threshold", 0.25)
    d.setdefault("same_window_hours", 24)
    d.setdefault("highlight_top", 8)
    return d


def render_files(args):
    cfg, meta, metas, out, pin_order, interest_spec = build_outputs(args)
    # cell_drift_suspect on emitted delta rows
    clo, chi = cfg["cell_drift_band"]
    for row in out.deltas:
        cr = row.pop("_cr", None)
        row["cell_drift_suspect"] = ("" if cr is None
                                     else int(not (clo <= cr <= chi)))
    pidx = {p: i for i, p in enumerate(pin_order)}
    files = {}
    ordc = lambda r: (r["set_ver"], r.get("config", r.get("deny_config", "")), pidx.get(r["pin"], 999),
                      r.get("pattern", ""), r.get("regime", ""), r.get("form", ""))
    out.cells.sort(key=ordc)
    out.deltas.sort(key=ordc)
    out.summary.sort(key=lambda r: (r["set_ver"], r["config"],
                                    pidx.get(r["pin"], 999), r["prev_pin"], r["regime"]))
    out.movers.sort(key=lambda r: (r["set_ver"], r["config"], pidx.get(r["pin"], 999),
                                   r["regime"], r["stamp"], r["prev_value"], r["new_value"]))
    out.compile.sort(key=ordc)
    out.twins.sort(key=ordc)
    metas.sort(key=lambda m: (m["role"], m["set_ver"], m["testee_id"], m["timestamp"]))
    irows = interest_rows(out, interest_spec)
    out.interest_rows = irows
    ex = ["# pins_without_records: " + meta["pins_without_records"]]
    files["records.tsv"] = tsv_text("records", meta, RECORD_COLS, metas, ex)
    files["cells.tsv"] = tsv_text("cells", meta, CELL_COLS, out.cells)
    n_unl = sum(1 for d in out.deltas if d["verdict"] == "unlinked")
    files["deltas.tsv"] = tsv_text("deltas", meta, DELTA_COLS, out.deltas,
                                   [f"# unlinked_cells: {n_unl}"])
    files["summary.tsv"] = tsv_text("summary", meta, SUMMARY_COLS, out.summary)
    files["movers_by_stamp.tsv"] = tsv_text("movers_by_stamp", meta, MOVER_COLS,
                                            out.movers)
    files["compile_deltas.tsv"] = tsv_text(
        "compile_deltas", meta, COMPILE_COLS, out.compile,
        [f"# size_threshold: {cfg['size_threshold']}",
         f"# compile_threshold: {cfg['compile_threshold']}"])
    files["deny_twins.tsv"] = tsv_text("deny_twins", meta, TWIN_COLS, out.twins)
    files["interest.tsv"] = tsv_text("interest", meta, INTEREST_COLS, irows)
    # history (R14): pin-major so a new pin appends
    dmap = {(d["set_ver"], d["config"], d["pin"], d["pattern"], d["regime"],
             d["form"]): d for d in out.deltas}
    hist = defaultdict(list)
    for c in out.cells:
        if c["regime"] == "-":
            continue
        setname = c["set_ver"].split("@")[0]
        d = dmap.get((c["set_ver"], c["config"], c["pin"], c["pattern"],
                      c["regime"], c["form"]), {})
        hist[(setname, c["config"])].append({
            "pin_idx": pidx.get(c["pin"], 999), "pin": c["pin"],
            "set_ver": c["set_ver"], "pattern": c["pattern"], "regime": c["regime"],
            "form": c["form"], "state": c["state"], "median_ns": c["median_ns"],
            "min_ns": c["min_ns"], "max_ns": c["max_ns"],
            "percall_ns": c["percall_ns"], "emit_code_bytes": c["emit_code_bytes"],
            "program_sha256": c["program_sha256"],
            "delta_row_id": d.get("row_id", ""), "prev_pin": d.get("prev_pin", ""),
            "ratio_vs_prev": d.get("ratio", ""), "verdict": d.get("verdict", "")})
    for (sn, config), rows in sorted(hist.items()):
        rows.sort(key=lambda r: (r["pin_idx"], r["set_ver"], r["pattern"],
                                 r["regime"], r["form"]))
        files[f"history/{sn}/{config}.tsv"] = tsv_text(
            f"history {sn} {config}", meta, HISTORY_COLS, rows,
            ["# append-only: rows ordered pin-major (pin_order); a new pin appends"])
    return cfg, meta, files, out


def write_files(root, files, extra_stale_dirs=("history",)):
    for rel, text in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        tmp = p + f".{os.getpid()}.tmp"
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        os.replace(tmp, p)


UNTRACKED = ("cells.tsv",)   # gitignored, regenerated by `make trend`


def check_files(root, files):
    bad = []
    for rel, text in sorted(files.items()):
        if rel in UNTRACKED:
            continue
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            bad.append((rel, "missing"))
            continue
        with open(p, encoding="utf-8", newline="") as f:
            cur = f.read()
        if cur != text:
            if rel.startswith("history/") and text.startswith(
                    cur.rsplit("\n", 2)[0]):
                bad.append((rel, "grown (committed is a prefix)"))
            else:
                bad.append((rel, "differs" + (" (history REWRITTEN)"
                                              if rel.startswith("history/") else "")))
    return bad


# ------------------------------------------------------------- snapshot cmd

def write_pin_snapshot(pin, store, cfg, pin_order, index_rows, snap_dir, instr,
                       cache_dir, force=False, config_path=None):
    """Write <snap_dir>/<pin>.tsv.gz from the store (the only reader of
    store/ in this module). Returns (path, n_records, n_inline)."""
    if pin not in pin_order:
        raise SystemExit(f"trend snapshot: {pin} is not in [[pin_order]] "
                         f"(catalogue/rules.toml)")
    dest = TS.snapshot_path(snap_dir, pin)
    if os.path.exists(dest) and not force:
        raise SystemExit(f"trend snapshot: {dest} exists: snapshots are immutable "
                         f"(--force to overwrite)")
    metas, chosen = select_records(index_rows, cfg, pin_order)
    mine = [m for m in metas if m["role"] == "pcrec" and m["pin"] == pin]
    used = [m for m in mine if m["disposition"] == "used"]
    if not used:
        raise SystemExit(f"trend snapshot: no used (measured, machine "
                         f"{cfg['machine']}) pcrec record at pin {pin}")
    svs = {m["set_ver"] for m in used}
    owners = TS.inline_owners(snap_dir, skip_pin=pin)
    # control: the used record(s) nearest in time to each used pcrec record of
    # the set@version; competitors: every used one (R12)
    want_ctrl = set()
    for sv in svs:
        cs = [m for m in metas if m["role"] == "control" and m["set_ver"] == sv
              and m["disposition"] == "used"]
        for u in [x for x in used if x["set_ver"] == sv]:
            if cs:
                want_ctrl.add(min(cs, key=lambda c: (
                    abs(iso_s(c["timestamp"]) - iso_s(u["timestamp"])),
                    c["timestamp"], c["testee_id"]))["path"])
    entries = []
    n_inline = 0
    for m in metas:
        role = m["role"]
        if role == "pcrec":
            if m["pin"] != pin:
                continue
        elif m["set_ver"] not in svs:
            continue
        m = dict(m)
        m["harness_commit"], m["instrument"], m["abi"] = "", "", ""
        m["schema_version"], m["engine_name"] = "", ""
        dg, data = None, "none"
        if m["disposition"] in ("used", "superseded"):
            dg = get_digest(os.path.join(store, m["path"]), cache_dir)
            m["harness_commit"] = dg["harness_commit"] or ""
            m["instrument"] = instr.of(dg["harness_commit"], dg["engine_name"])
            m["abi"] = dg["abi"] if dg["abi"] is not None else ""
            m["schema_version"] = dg.get("schema_version") or ""
            m["engine_name"] = dg.get("engine_name") or ""
        if m["disposition"] == "used" and (
                role in ("pcrec", "competitor")
                or (role == "control" and m["path"] in want_ctrl)):
            if m["path"] in owners:
                data = "ref:" + owners[m["path"]]
            else:
                data = "inline"
                n_inline += 1
        entries.append((m, dg if data == "inline" else None, data))
    header = [("generator", GEN_VERSION),
              ("index_sha256", sha_file(os.path.join(store, "index.tsv"))),
              ("config_sha256", sha_file(config_path) if config_path else ""),
              ("machine", cfg["machine"]),
              ("n_records", len(entries)), ("n_inline", n_inline)]
    TS.write_snapshot(pin, entries, header, snap_dir, force=force)
    return dest, len(entries), n_inline


def cmd_snapshot(argv):
    ap = argparse.ArgumentParser(
        prog="trend.py snapshot",
        description="write the immutable per-pin snapshot (reads the store)")
    ap.add_argument("--pin", action="append", default=[],
                    help="pcrec pin (repeatable)")
    ap.add_argument("--all-pins", action="store_true",
                    help="every pin of [[pin_order]] with a used record in the store")
    ap.add_argument("--store", default=os.path.join(ROOT, "store"))
    ap.add_argument("--snapshots", default=os.path.join(DEFAULT_OUT, "snapshots"))
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--rules", default=os.path.join(ROOT, "catalogue", "rules.toml"))
    ap.add_argument("--repo", default=ROOT, help="git repo for instrument shas")
    ap.add_argument("--cache", default=os.path.join(ROOT, "build", "trend-cache"))
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--no-git", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing snapshot (snapshots are immutable)")
    args = ap.parse_args(argv)
    cfg = load_config(args.config)
    pin_order = load_pin_order(args.rules)
    with open(os.path.join(args.store, "index.tsv"), newline="", encoding="utf-8") as f:
        index_rows = list(csv.DictReader(f, delimiter="\t"))
    pins = list(args.pin)
    if args.all_pins:
        have = {split_pcrec_id(r["testee_id"])[0] for r in index_rows
                if split_pcrec_id(r["testee_id"])}
        pins += [p for p in pin_order if p in have and p not in pins]
    if not pins:
        ap.error("--pin or --all-pins required")
    instr = Instrument(args.repo, enabled=not args.no_git)
    cache = None if args.no_cache else args.cache
    rc = 0
    for pin in pins:
        try:
            dest, n, ni = write_pin_snapshot(pin, args.store, cfg, pin_order,
                                             index_rows, args.snapshots, instr,
                                             cache, args.force, args.config)
        except SystemExit as e:
            print(e)
            if args.all_pins and "exists" in str(e):
                continue        # backfill is resumable: existing = skipped
            rc = 1
            continue
        print(f"trend snapshot: {pin}: {n} records ({ni} inline) -> {dest} "
              f"({os.path.getsize(dest)} bytes)")
    return rc


# ----------------------------------------------------------------- links cmd

def cmd_links(argv):
    ap = argparse.ArgumentParser(
        prog="trend.py links",
        description="propose cross-version links the walk would use but "
                    "links.tsv lacks (as `inferred` rows); reads snapshots only")
    ap.add_argument("--snapshots", default=os.path.join(DEFAULT_OUT, "snapshots"))
    ap.add_argument("--links", default=os.path.join(DEFAULT_OUT, "links.tsv"))
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--rules", default=os.path.join(ROOT, "catalogue", "rules.toml"))
    ap.add_argument("--interest", default=None)
    ap.add_argument("--sets", default=None)
    ap.add_argument("--write", action="store_true",
                    help="append the proposals to links.tsv as source=inferred")
    args = ap.parse_args(argv)
    args.interest = args.interest or os.path.join(DEFAULT_OUT, "cells_of_interest.tsv")
    have = load_links(args.links)
    probe = Links(have.rows, allow_all=True)
    _cfg, _meta, _metas, out, _po, _spec = build_outputs(args, probe)
    comparable = defaultdict(int)
    for d in out.raw_deltas_all:
        if d.get("prev_set_ver") and d["prev_set_ver"] != d["set_ver"] \
                and d["verdict"] not in ("new", "not-comparable", "unlinked"):
            comparable[tuple(sorted((d["prev_set_ver"], d["set_ver"])))] += 1
    props = []
    for pair in sorted(probe.seen):
        if frozenset(pair) in have.sv:
            continue
        a, b = pair
        props.append({"kind": "set-version", "from": a, "to": b,
                      "source": "inferred",
                      "reason": f"delta walk pairs {a} with {b} "
                                f"({probe.seen[pair]} cell lookups, "
                                f"{comparable.get(pair, 0)} comparable cells); "
                                f"proposed by trend.py links, to be confirmed"})
    for r in props:
        print("\t".join(r[c] for c in LINK_COLS))
    print(f"trend links: {len(props)} proposed, {len(have.rows)} already listed")
    if args.write and props:
        new = not os.path.exists(args.links)
        with open(args.links, "a", encoding="utf-8", newline="") as f:
            if new:
                f.write(LINKS_HEADER)
                f.write("\t".join(LINK_COLS) + "\n")
            for r in props:
                f.write("\t".join(r[c] for c in LINK_COLS) + "\n")
    return 0


LINKS_HEADER = """# links.tsv -- the explicit cross-version links the trend comparison may use ([B130.2]).
# kind: set-version (an UNDIRECTED pair of versions of one set whose records a
# delta may span) | config-rename (from -> to). source: inferred (proposed by
# `trend.py links`, in force, awaiting confirmation) | confirmed (manager/Frank).
# A pair that would need a link not listed here is reported `unlinked`, never guessed.
"""


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "snapshot":
        return cmd_snapshot(argv[1:])
    if argv and argv[0] == "links":
        return cmd_links(argv[1:])
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--snapshots", default=None,
                    help="snapshot directory (default <out>/snapshots)")
    ap.add_argument("--links", default=None, help="default <out>/links.tsv")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--rules", default=os.path.join(ROOT, "catalogue", "rules.toml"))
    ap.add_argument("--interest", default=None,
                    help="cells-of-interest file (default <out>/cells_of_interest.tsv)")
    ap.add_argument("--sets", default=None, help="comma list of set names (dev slice)")
    ap.add_argument("--check", action="store_true",
                    help="regenerate in memory, exit 1 on drift from --out")
    ap.add_argument("--no-html", action="store_true")
    args = ap.parse_args(argv)
    args.snapshots = args.snapshots or os.path.join(args.out, "snapshots")
    args.links = args.links or os.path.join(args.out, "links.tsv")
    if args.interest is None:
        args.interest = os.path.join(args.out, "cells_of_interest.tsv")
    cfg, meta, files, out = render_files(args)
    if not args.no_html:
        import trend_html
        files.update(trend_html.render_all(cfg, meta, out, args.out, dict(files)))
    if not os.path.exists(args.interest) and not args.check:
        files[os.path.relpath(args.interest, args.out)] = INTEREST_TEMPLATE
    if args.check:
        bad = check_files(args.out, files)
        for rel, why in bad:
            print(f"trend --check: {rel}: {why}")
        print(f"trend --check: {len(files)} files, {len(bad)} drifted")
        return 1 if bad else 0
    write_files(args.out, files)
    print(f"trend: wrote {len(files)} files under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
