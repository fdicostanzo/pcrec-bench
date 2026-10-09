#!/usr/bin/env python3
"""tools/trend_snapshot.py -- PER-VERSION SNAPSHOTS for the pcrec trend report
([B130.2], docs/design/pcrec_trend_report_v0.md section 8).

A snapshot is ONE immutable file per pinned pcrec version,
`reports/trend/snapshots/<pin>.tsv.gz`, holding everything the comparison
needs from that version's records, so the comparison (`tools/trend.py`) never
opens `store/`. The only code here that reads the store is `write_snapshot`.

FORMAT (trend-snapshot-2; deterministic gzip, mtime 0, level 9; UTF-8 text,
one row per line, first column = row tag, tab separated). v2 is the LOSSLESSLY
COMPACT encoding of v1 (same content, no rounding): records are keyed by a
short integer `rid`, cells by `cid`, subjects by `sbid`, outcomes by a code.

  # key: value            header lines (schema, pin, generator, provenance)
  OUT  code outcome       the file's closed outcome-code table
  REC  rid path role set_ver testee_id config pin machine timestamp status
       disposition superseded_by harness_commit instrument abi schema_version
       engine_name data
       -- one row per index record CONSIDERED (R11): used, superseded,
          excluded-*; `data` = `inline` (rows below follow in THIS file),
          `ref:<pin>` (the same record is stored inline in <pin>.tsv.gz: a
          control/competitor record shared by several windows is stored once,
          in the first snapshot that needed it) or `none` (listed only).
  SB   sbid subject_id sha256   the subject table: each (subject id, sha)
       stored ONCE per file, however many records and cells use it
  PAT  rid pattern_id canonical_sha256
  CMP  rid pattern_id form outcome compile_ns(json list) diag meta(json)
       -- the compile row: stamps (STAMP_KEYS), program_sha256, emit bytes,
          engine_sel, abi, compile ns per measurement
  CEL  cid rid pattern regime form state n_subjects n_trials median_ns min_ns
       max_ns n_wrong n_gave_up n_no_expectation pattern_sha subject_set_sha
       program_sha256
       -- the set-grain reduction over ALL the cell's subjects
          (`reduce.reduce_set_cell`): human-readable, and a self-check: a
          reader recomputes it from the SUBJ rows (`verify_snapshot`)
  SUBJ cid sbid iters trials
       -- per-subject: the full per-trial list as `trial:outcome-code:time`
          items joined by `,` (`:diag` appended only when the diagnostic is
          non-empty; `%`, `,`, `:` and control characters in a diag are
          %-escaped). `time` is the measured elapsed_ns as written, over the
          row's `iters` (or `elapsed/iters` when a trial differs): ns/call is
          RECOMPUTED as elapsed/iters, which equals the original float bit
          for bit (checked at write time; a trial that is not recomputable is
          stored `f<float>`; empty = no timing). The subject's own median ns/call
          (`subject_median`) is DERIVED from the trials, not stored: it lets a
          pair compare over COMMON subjects when a set version adds or drops
          subjects.

Row order is fixed (records by path, then PAT, CMP, CEL, SUBJ each sorted), so
the same inputs give the same bytes. No clock: the header carries provenance
shas (index, config), never a time.
"""

import csv
import gzip
import hashlib
import io
import json
import os
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from pcrecbench import reduce as R  # noqa: E402

SNAPSHOT_SCHEMA = "trend-snapshot-2"
META_KEYS = ("engine", "dfa_prefilter", "dfa_start", "req_why", "vm_start_scan",
             "emit_bytes", "emit_code_bytes", "program_sha256", "engine_sel",
             "abi")
REC_COLS = ["rid", "path", "role", "set_ver", "testee_id", "config", "pin", "machine",
            "timestamp", "status", "disposition", "superseded_by",
            "harness_commit", "instrument", "abi", "schema_version",
            "engine_name", "data"]


class SnapshotError(Exception):
    pass


def _cell(v):
    if v is None:
        return ""
    return str(v).replace("\t", " ").replace("\n", " ").replace("\r", " ")


def _row(*cols):
    return "\t".join(_cell(c) for c in cols)


def gzip_bytes(text):
    """Deterministic gzip: no filename, mtime 0, fixed level."""
    buf = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buf, mtime=0,
                       compresslevel=9) as g:
        g.write(text.encode("utf-8"))
    return buf.getvalue()


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def subject_median(trials):
    """Median ns/call of one subject over its matched trials (None if none)."""
    v = [ns for _t, o, ns, _d in trials if o == R.MATCHED and ns is not None]
    return statistics.median(v) if v else None


def reduce_all(cells_key, subs):
    """SetCell summary of one digest cell over all subjects (shared by writer
    and verifier, so the CEL row is exactly what a reader recomputes)."""
    by = {}
    for sid, trials in subs.items():
        rows = []
        for trial, o, ns, diag in trials:
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
    return {"state": state, "median": sc.median_ns, "min": sc.min_ns,
            "max": sc.max_ns, "n_subjects": sc.n_subjects,
            "n_trials": sc.n_trials, "n_wrong": sc.n_wrong,
            "n_gave_up": sc.n_gave_up, "n_no_expectation": sc.n_no_expectation}


def subject_set_sha(subs, shas):
    h = hashlib.sha256()
    for sid in sorted(subs):
        h.update(f"{sid}:{shas.get(sid) or ''}\n".encode())
    return h.hexdigest()


def _esc(t):
    return (str(t).replace("%", "%25").replace(",", "%2C").replace(":", "%3A")
            .replace("\t", "%09").replace("\n", "%0A").replace("\r", "%0D"))


def _unesc(t):
    return (t.replace("%0D", "\r").replace("%0A", "\n").replace("%09", "\t")
            .replace("%3A", ":").replace("%2C", ",").replace("%25", "%"))


def _num(x):
    return "" if x is None else repr(x)


def _parse_num(t):
    if t == "":
        return None
    try:
        return int(t)
    except ValueError:
        return float(t)


def _exact(ns, raw):
    """(elapsed, iters) when ns == elapsed/iters bit for bit, else None."""
    if raw is None or ns is None:
        return None
    e, i = raw
    if isinstance(e, (int, float)) and isinstance(i, int) and i and e / i == ns:
        return e, i
    return None


def row_iters(trials, raws):
    """The iteration count shared by most of a subject's exact trials."""
    c = {}
    for (_t, _o, ns, _d), raw in zip(trials, raws):
        x = _exact(ns, raw)
        if x:
            c[x[1]] = c.get(x[1], 0) + 1
    return max(sorted(c), key=lambda k: c[k]) if c else None


def enc_trials(trials, ocode, raws=None, iters=None):
    out = []
    raws = raws or [None] * len(trials)
    for (trial, o, ns, diag), raw in zip(trials, raws):
        x = _exact(ns, raw)
        if ns is None:
            v = ""
        elif x is None:
            v = "f" + repr(ns)        # not recomputable: the float itself
        else:
            v = repr(x[0]) + ("" if x[1] == iters else f"/{x[1]}")
        it = f"{'' if trial is None else trial}:{ocode[o]}:{v}"
        if diag:
            it += ":" + _esc(diag)
        out.append(it)
    return ",".join(out)


def dec_trials(text, outcomes, iters=None):
    out = []
    for it in text.split(","):
        f = it.split(":")
        trial = int(f[0]) if f[0] != "" else None
        v = f[2]
        if v == "":
            ns = None
        elif v[0] == "f":
            ns = _parse_num(v[1:])
        else:
            e, _, i = v.partition("/")
            ns = _parse_num(e) / (int(i) if i else iters)
        out.append([trial, outcomes[int(f[1])], ns,
                    _unesc(f[3]) if len(f) > 3 else ""])
    return out


def _f(x):
    return "" if x is None else repr(x)


def render_snapshot(pin, header, entries):
    """entries: list of (meta, dg_or_None, data) -> gz bytes."""
    entries = sorted(entries, key=lambda e: e[0]["path"])
    lines = [f"# trend_snapshot: {pin}", f"# schema: {SNAPSHOT_SCHEMA}",
             f"# pin: {pin}"]
    for k, v in header:
        lines.append(f"# {k}: {_cell(v)}")
    outcomes = sorted({t[1] for _m, dg, d in entries if d == "inline"
                       for subs in dg["cells"].values()
                       for tr in subs.values() for t in tr}, key=str)
    ocode = {o: i for i, o in enumerate(outcomes)}
    for o, i in ocode.items():
        lines.append(_row("OUT", i, o))
    lines.append(_row(*(["COLS"] + REC_COLS)))
    rid_of = {}
    for i, (m, _dg, data) in enumerate(entries):
        rid_of[m["path"]] = i
        lines.append(_row("REC", i, m["path"], m["role"], m["set_ver"],
                          m["testee_id"], m["config"], m["pin"], m["machine"],
                          m["timestamp"], m["status"], m["disposition"],
                          m.get("superseded_by", ""), m.get("harness_commit", ""),
                          m.get("instrument", ""), m.get("abi", ""),
                          m.get("schema_version", ""), m.get("engine_name", ""),
                          data))
    sb_id, sb_lines = {}, []

    def sb(sid, sha):
        k = (sid, sha or "")
        if k not in sb_id:
            sb_id[k] = len(sb_id)
            sb_lines.append(_row("SB", sb_id[k], sid, sha or ""))
        return sb_id[k]
    body, cid = [], 0
    for m, dg, data in entries:
        if data != "inline":
            continue
        rid = rid_of[m["path"]]
        for pid in sorted(dg["patterns"]):
            body.append(_row("PAT", rid, pid, dg["patterns"][pid]))
        for ck in sorted(dg["compile"]):
            pid, form = ck.split("\t")
            e = dg["compile"][ck]
            meta = {k: (e["meta"] or {}).get(k) for k in META_KEYS
                    if (e["meta"] or {}).get(k) is not None}
            body.append(_row("CMP", rid, pid, form, e["outcome"],
                             json.dumps(e["ns"]), e.get("diag") or "",
                             json.dumps(meta, sort_keys=True)))
        for key in sorted(dg["cells"]):
            pid, rg, form = key.split("\t")
            subs = dg["cells"][key]
            red = reduce_all(key, subs)
            cm = ((dg["compile"].get(pid + "\t" + form) or {}).get("meta")) or {}
            body.append(_row("CEL", cid, rid, pid, rg, form, red["state"],
                             red["n_subjects"], red["n_trials"],
                             _f(red["median"]), _f(red["min"]), _f(red["max"]),
                             red["n_wrong"], red["n_gave_up"],
                             red["n_no_expectation"],
                             dg["patterns"].get(pid) or "",
                             subject_set_sha(subs, dg["subjects"]),
                             cm.get("program_sha256") or ""))
            for sid in sorted(subs):
                raws = (dg.get("rawt") or {}).get(key, {}).get(sid)
                its = row_iters(subs[sid], raws) if raws else None
                body.append(_row("SUBJ", cid, sb(sid, dg["subjects"].get(sid)),
                                 "" if its is None else its,
                                 enc_trials(subs[sid], ocode, raws, its)))
            cid += 1
    lines.extend(sb_lines)
    lines.extend(body)
    return gzip_bytes("\n".join(lines) + "\n")


# ------------------------------------------------------------------ reading

def read_lines(path):
    with gzip.open(path, "rt", encoding="utf-8", newline="") as f:
        for ln in f:
            yield ln.rstrip("\n")


def read_header_recs(path):
    """(header dict, REC rows as dicts) -- stops at the first row after the REC
    block, so it is cheap on a large snapshot."""
    header, recs = {}, []
    for ln in read_lines(path):
        if ln.startswith("# "):
            k, _, v = ln[2:].partition(": ")
            header[k] = v
        elif ln.startswith("COLS\t") or ln.startswith("OUT\t"):
            continue
        elif ln.startswith("REC\t"):
            recs.append(dict(zip(REC_COLS, ln.split("\t")[1:])))
        else:
            break
    return header, recs


def read_snapshot(path):
    """-> (header, recs list of dicts; an inline record carries 'dg')."""
    header, recs, dgs = {}, [], {}
    outcomes, sb, cells = {}, {}, {}
    for ln in read_lines(path):
        if ln.startswith("# "):
            k, _, v = ln[2:].partition(": ")
            header[k] = v
            continue
        c = ln.split("\t")
        tag = c[0]
        if tag == "OUT":
            outcomes[int(c[1])] = c[2]
        elif tag == "REC":
            recs.append(dict(zip(REC_COLS, c[1:])))
        elif tag == "SB":
            sb[int(c[1])] = (c[2], c[3])
        elif tag in ("PAT", "CMP", "CEL"):
            rid = c[1] if tag != "CEL" else c[2]
            dg = dgs.get(rid)
            if dg is None:
                dg = dgs[rid] = {"patterns": {}, "subjects": {}, "cells": {},
                                 "compile": {}, "_cel": {}}
            if tag == "PAT":
                dg["patterns"][c[2]] = c[3] or None
            elif tag == "CMP":
                dg["compile"][c[2] + "\t" + c[3]] = {
                    "outcome": c[4], "ns": json.loads(c[5]), "diag": c[6],
                    "meta": json.loads(c[7])}
            else:
                key = c[3] + "\t" + c[4] + "\t" + c[5]
                dg["_cel"][key] = c[6:]
                cells[int(c[1])] = (dg, key)
        elif tag == "SUBJ":
            dg, key = cells[int(c[1])]
            sid, sha = sb[int(c[2])]
            dg["cells"].setdefault(key, {})[sid] = dec_trials(
                c[4], outcomes, int(c[3]) if c[3] != "" else None)
            if sha:
                dg["subjects"][sid] = sha
    by_rid = {r["rid"]: r for r in recs}
    for rid, dg in dgs.items():
        r = by_rid.get(rid)
        if r is None:
            raise SnapshotError(f"{path}: body rows for unlisted record {rid}")
        abi = r["abi"]
        dg.update(path=r["path"], testee_id=r["testee_id"],
                  engine_name=r["engine_name"],
                  harness_commit=r["harness_commit"] or None,
                  timestamp=r["timestamp"], schema_version=r["schema_version"],
                  abi=int(abi) if abi != "" else None)
        r["dg"] = dg
    return header, recs


def verify_snapshot(path):
    """Recompute every CEL row from its SUBJ rows; list of mismatch strings."""
    header, recs = read_snapshot(path)
    bad = []
    for r in recs:
        dg = r.get("dg")
        if dg is None:
            continue
        for key, stored in dg["_cel"].items():
            pid, rg, form = key.split("\t")
            red = reduce_all(key, dg["cells"].get(key, {}))
            want = [red["state"], str(red["n_subjects"]), str(red["n_trials"]),
                    _f(red["median"]), _f(red["min"]), _f(red["max"]),
                    str(red["n_wrong"]), str(red["n_gave_up"]),
                    str(red["n_no_expectation"])]
            if stored[:9] != want:
                bad.append(f"{r['path']} {key}: stored {stored[:9]} != {want}")
    return bad


def snapshot_path(snap_dir, pin):
    return os.path.join(snap_dir, f"{pin}.tsv.gz")


def inline_owners(snap_dir, skip_pin=None):
    """{record path: pin of the snapshot storing it inline} over the existing
    snapshots (REC rows only)."""
    out = {}
    if not os.path.isdir(snap_dir):
        return out
    for fn in sorted(os.listdir(snap_dir)):
        if not fn.endswith(".tsv.gz"):
            continue
        pin = fn[:-len(".tsv.gz")]
        if pin == skip_pin:
            continue
        _h, recs = read_header_recs(os.path.join(snap_dir, fn))
        for r in recs:
            if r["data"] == "inline":
                out.setdefault(r["path"], pin)
    return out


def write_snapshot(pin, entries, header, snap_dir, force=False):
    """Write <snap_dir>/<pin>.tsv.gz. Refuses to overwrite (immutability)
    unless force. entries: [(meta, dg|None, data)]. Returns the path."""
    os.makedirs(snap_dir, exist_ok=True)
    dest = snapshot_path(snap_dir, pin)
    if os.path.exists(dest) and not force:
        raise SnapshotError(f"{dest} exists: snapshots are immutable "
                            f"(--force to overwrite)")
    data = render_snapshot(pin, header, entries)
    tmp = dest + f".{os.getpid()}.tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dest)
    return dest


def snapshots_digest(snap_dir):
    """sha256 over the (name, file sha256) list of every snapshot -- the
    comparison's input identity (replaces the store index sha in headers)."""
    h = hashlib.sha256()
    if os.path.isdir(snap_dir):
        for fn in sorted(os.listdir(snap_dir)):
            if fn.endswith(".tsv.gz"):
                with open(os.path.join(snap_dir, fn), "rb") as f:
                    h.update(fn.encode() + b"\t" + sha_bytes(f.read()).encode() + b"\n")
    return h.hexdigest()
