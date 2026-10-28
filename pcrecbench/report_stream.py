"""pcrecbench/report_stream.py -- the STREAM view of the reporter ([B148] lane
b148rep; `docs/design/unusual_set_v1.md` 7.5 "Readers"; REPORTER_VERSION v29).
Selected by `pcrecbench report --grain stream` and by nothing else; built on
the [B143] substitution model (`report_subst.py`: the same record dedup, tier,
status and one-host rules; md and tsv renderings only).

What it reads. Records whose sub-bench declares the regime `call-stream`
(schema v1.11). Every `call-stream` match row is one trial of one (testee,
stream, pattern): `stream` = {calls, segment_bytes, matched, nomatch,
refused, gave_up, results_sha256[, first_limit]}, timed at `iterations >= 1`
replays. The row's denominators are the stream's OWN (`calls`,
`segment_bytes`) -- never the subject's size (7.1) -- which is why the set and
subject grains refuse/drop these rows and this view exists.

What it prints (7.5), per (stream, pattern) and testee:

* STREAMS: ns per stream (median over trials of `elapsed_ns / iterations`,
  min-max), calls/s, segment MB/s (10^6 bytes), and the matched / nomatch /
  refused / gave_up counts; a vars stream also its MISS count -- the memo
  compiles per replay: the row's `engine_metadata.assist_compiles` where the
  driver produced it (tagged `measured`), else the stream's declared
  `distinct_resolved` from `bench/<set>/values/streams.tsv` (tagged
  `declared`; read-only, absent file = no declared column).
* BREAK-EVEN (3.3), vars streams: pcrec's compile ns / (assisted ns per call
  - pcrec ns per call), per assisted testee; "none" where the assisted engine
  is not slower per call. The time of an assisted engine measures THAT assist
  (its keying, container, escaping), not the engine in the abstract (3.3).
* CALLOUT COST SPLIT (3.2): per (testee, member, subject), the `twin` /
  `pass` / `pass-nofn` / `real` arms (the pattern's `arm-*` and `twin_of-*`
  tags): `pass - twin` (the wrapper), `real - pass` (the callee, reported ONLY
  where the two arms' `callout_fires` are equal, 3.2 item 5), fires, and the
  SHARE `fires x callee_ns_per_fire / real_ns` where a calibration TSV
  (`tools/callout_calib.py`'s stdout, `--callee-calib FILE`) gives that
  engine's ns/fire; flagged >20 % on libpcre2 jit / >40 % anywhere. No
  cross-arm subtraction is computed on a member whose arms' fire counts
  differ by mechanism (co-netstr, M-10).
* DEPTH-OF-FAILURE (6.5): rung x engine -> `match` or the limit's NAME
  (`stream.first_limit`, else `reduce.giveup_code`'s reading of the
  diagnostic), over every `nest-*` subject row of any regime and every
  non-matched `call-stream` row; a wrong answer is `WRONG (excluded)`. Not
  MB/s.

Every number is under its record's status / tier / trial-agreement / load
verdict (the legend lists them per testee); a non-measured or scratch record
is "not ranked" unless `--include-unmeasured` / `--include-scratch`. Nothing
here is a ratio across testees except the break-even line.
"""

from __future__ import annotations

import csv
import os
import re
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field

from pcrecbench import reduce as _reduce
from pcrecbench import report as _rp
from pcrecbench import report_subst as _rs

STREAM_REGIME = "call-stream"

#: 3.2 item 4: flag a callee share over 20 % on libpcre2 jit, 40 % anywhere.
SHARE_FLAG_JIT = 0.20
SHARE_FLAG_ANY = 0.40

ARMS = ("twin", "pass", "pass-nofn", "real")
_NEST = re.compile(r"^nest-([a-z]+)-(\d+)(k?)$")


def is_stream_record(rec) -> bool:
    s = rec.setup or {}
    return STREAM_REGIME in (s.get("subbench", {}).get("regimes") or [])


@dataclass
class StreamCell:
    """One (testee, stream, pattern) cell."""
    state: str = "absent"      # measured | gave-up | <other outcome>
    n_trials: int = 0
    median_ns: float | None = None
    min_ns: float | None = None
    max_ns: float | None = None
    calls: int | None = None
    segment_bytes: int | None = None
    matched: int | None = None
    nomatch: int | None = None
    refused: int | None = None
    gave_up: int | None = None
    first_limit: str = ""
    misses: int | None = None
    misses_src: str = ""       # measured | declared
    note: str = ""
    compile_ns: float | None = None
    hw_bytes: int | None = None
    hw_method: str = ""

    @property
    def ranked(self) -> bool:
        return self.state == "measured" and self.median_ns is not None

    @property
    def calls_per_s(self):
        if self.ranked and self.calls and self.median_ns:
            return self.calls / (self.median_ns / 1e9)
        return None

    @property
    def mb_per_s(self):
        if self.ranked and self.segment_bytes and self.median_ns:
            return self.segment_bytes / 1e6 / (self.median_ns / 1e9)
        return None

    @property
    def ns_per_call(self):
        if self.ranked and self.calls:
            return self.median_ns / self.calls
        return None


@dataclass
class ArmCell:
    """One (testee, member, subject, regime) callout-arm row."""
    ns: dict = field(default_factory=dict)       # arm -> median ns
    fires: dict = field(default_factory=dict)    # arm -> callout_fires


@dataclass
class StreamData:
    query_desc: list
    source_desc: str
    included: list             # (record_id, path)
    excluded_invalid: list
    superseded: list
    newer_not_measured: list
    machines: set
    subbench_versions: set
    schema_versions: set
    skipped_non_stream: int
    include_unmeasured: bool
    include_scratch: bool
    store_parent: str
    subbench_alias_note: str | None
    testees: dict              # tid -> info
    ranked_testees: list
    not_ranked: list
    cells: dict                # (tid, stream, pattern) -> StreamCell
    patterns: dict             # pattern_id -> dict(tags=set, member=str)
    declared: dict             # stream -> dict (values/streams.tsv row)
    arms: dict                 # (tid, member, subject, regime) -> ArmCell
    depth: dict                # (pattern, subject) -> {tid: text}
    calib: dict                # (tid, member) -> ns_per_fire
    calib_src: str


# ---------------------------------------------------------------- reduction

def _limit_name(row) -> str:
    st = row.get("stream") or {}
    if st.get("first_limit"):
        return str(st["first_limit"])
    # the shared extractor (`giveup:-46:JIT stack limit reached` ->
    # `-46:JIT stack limit reached`), so `quick` / the set grain read alike
    return _reduce.giveup_code(row) or row.get("match_outcome", "?")


def _timed(rows):
    out = []
    for r in rows:
        t = r.get("timing") or {}
        it = t.get("iterations")
        if r.get("match_outcome") == "matched-as-expected" and it:
            out.append(t["elapsed_ns"] / it)
    return out


def _reduce_stream_cell(rows, compile_rows):
    c = StreamCell()
    st0 = next((r.get("stream") for r in rows if r.get("stream")), None) or {}
    c.calls = st0.get("calls")
    c.segment_bytes = st0.get("segment_bytes")
    for k in ("matched", "nomatch", "refused", "gave_up"):
        setattr(c, k, st0.get(k))
    ns = _timed(rows)
    outs = Counter(r.get("match_outcome") for r in rows)
    if ns:
        c.state = "measured"
        c.n_trials = len(ns)
        c.median_ns = statistics.median(ns)
        c.min_ns, c.max_ns = min(ns), max(ns)
    elif outs:
        c.state = outs.most_common(1)[0][0]
        bad = next((r for r in rows if r.get("match_outcome") == c.state), rows[0])
        c.first_limit = _limit_name(bad) if c.state == "gave-up" else ""
        c.note = _rs._first_diff(bad.get("diagnostic"))
    comp = [r for r in rows if (r.get("engine_metadata") or {}).get("assist_compiles") is not None]
    if comp:
        c.misses = int(statistics.median(
            r["engine_metadata"]["assist_compiles"] for r in comp))
        c.misses_src = "measured"
    hw = next((r["engine_metadata"] for r in rows
               if (r.get("engine_metadata") or {}).get("deep_mem_bytes") is not None), None)
    if hw:
        c.hw_bytes, c.hw_method = hw["deep_mem_bytes"], hw.get("deep_mem_method", "")
    tot = [(r.get("cost") or {}).get("total_ns") for r in compile_rows
           if r.get("compile_outcome") == "compiled"]
    tot = [t for t in tot if isinstance(t, (int, float))]
    if tot:
        c.compile_ns = statistics.median(tot)
    return c


def _depth_text(rows):
    outs = Counter(r.get("match_outcome") for r in rows)
    top = outs.most_common(1)[0][0]
    if top == "matched-as-expected":
        return "match"
    if top == "gave-up":
        return _limit_name(next(r for r in rows if r.get("match_outcome") == "gave-up"))
    if top == "did-not-match-as-expected":
        return "WRONG (excluded)"
    return str(top)


def _depth_key(subject):
    m = _NEST.match(subject)
    if m:
        return (0, m.group(1), int(m.group(2)) * (1024 if m.group(3) else 1))
    return (1, subject, 0)


def load_declared(subbench_id, repo_root):
    """values/streams.tsv of the sub-bench -> {stream: row}; {} when absent."""
    p = os.path.join(repo_root, "bench", subbench_id, "values", "streams.tsv")
    if not os.path.isfile(p):
        return {}
    with open(p, newline="") as f:
        return {r["stream"]: r for r in csv.DictReader(f, delimiter="\t")}


def load_calib(path):
    """callout_calib.py stdout -> {(testee, member): ns_per_fire}."""
    out = {}
    with open(path) as f:
        head = None
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            cols = line.rstrip("\n").split("\t")
            if head is None:
                head = cols
                continue
            row = dict(zip(head, cols))
            try:
                out[(row["testee"], row["member"])] = float(row["ns_per_fire"])
            except (KeyError, ValueError):
                pass
    return out


def build_stream_report(loaded, args, known_testee_ids=None):
    """-> (StreamData | None, error). Same refusals as the standard builder
    that apply (unknown --testee, mixed major, two machines)."""
    if getattr(args, "testee", None):
        known = known_testee_ids if known_testee_ids is not None else {
            r.setup["testee"]["testee_id"] for r in loaded
            if r.setup and "testee" in r.setup}
        unknown = [t for t in args.testee if t not in known]
        if unknown:
            return None, ("--testee names an id with no matching record in "
                          "the store: " + ", ".join(repr(t) for t in unknown))
    selected = [r for r in loaded if _rp.matches_filters(r, args)]
    stream_sel = [r for r in selected if is_stream_record(r)]
    skipped = len(selected) - len(stream_sel)
    if not stream_sel:
        return None, ("--grain stream: no record in the selection declares "
                      "the regime `call-stream` (%d record(s) selected, none "
                      "of it)" % len(selected))
    majors = {r.schema_major for r in stream_sel if r.schema_major is not None}
    if len(majors) > 1:
        return None, ("refusing to report: the selected records mix MAJOR "
                      "schema versions with no declared migration")
    excluded_invalid, valid = [], []
    for r in stream_sel:
        if r.problems:
            excluded_invalid.append((r.path, [str(p) for p in r.problems]))
        else:
            valid.append(r)
    valid, superseded, newer_nm, eff = _rs.select_latest(valid, args)
    hosts = sorted({r.setup["environment"]["machine_id"] for r in valid})
    if len(hosts) > 1:
        return None, ("the selected records span %d machines (%s); a report "
                      "is PER HOST and never pools machine_ids into one cell "
                      "-- add --machine <id> (O-90, [B137])"
                      % (len(hosts), ", ".join(hosts)))

    inc_unmeasured = bool(getattr(args, "include_unmeasured", False))
    inc_scratch = bool(getattr(args, "include_scratch", False))
    included, machines, svers, sbvers, sbids = [], set(), set(), set(), set()
    testees, not_ranked = {}, []
    patterns = {}
    cells_in, arms_in, depth_in = {}, defaultdict(lambda: defaultdict(list)), defaultdict(lambda: defaultdict(list))
    for r in sorted(valid, key=lambda r: eff[r.path]):
        s = r.setup
        tid, rid = eff[r.path], s["record_id"]
        included.append((rid, r.path))
        machines.add(s["environment"]["machine_id"])
        svers.add(s["schema_version"])
        sbvers.add(s["subbench"]["id"] + "@" + str(s["subbench"]["version"]))
        sbids.add(s["subbench"]["id"])
        t = s["testee"]
        status = s.get("status", "measured")
        rtier = s.get("tier", "pinned")
        env = s.get("environment") or {}
        occ = env.get("occupancy") or {}
        env_txt = "load %s; occupancy before %s / after %s" % (
            (env.get("load") or {}).get("verdict", "?"),
            (occ.get("before") or {}).get("verdict", "?"),
            (occ.get("after") or {}).get("verdict", "?"))
        testees[tid] = dict(
            status=status, status_detail=s.get("status_detail"), record_id=rid,
            rec_tier=rtier, engine_name=t.get("engine_name"),
            engine_mode=t.get("engine_mode"), env=env_txt,
            assisted=bool(t.get("assist")), schema_version=str(s.get("schema_version", "")),
            agreement=_rp._agreement_display(
                s.get("trial_agreement"), str(s.get("schema_version", ""))))
        for p in s.get("patterns", []):
            tags = set(p.get("tags") or [])
            member = next((x[len("twin_of-"):] for x in sorted(tags) if x.startswith("twin_of-")), "")
            arm = next((x[len("arm-"):] for x in sorted(tags) if x.startswith("arm-")), "")
            spell = next((x[len("spelling-"):] for x in sorted(tags) if x.startswith("spelling-")), "")
            patterns.setdefault(p["pattern_id"], dict(tags=tags, member=member, arm=arm,
                                                       spelling=spell))
        if status != "measured" and not inc_unmeasured:
            not_ranked.append((tid, "status %s" % status))
            continue
        if rtier == "scratch" and not inc_scratch:
            not_ranked.append((tid, "tier scratch"))
            continue
        m_by, c_by = defaultdict(list), defaultdict(list)
        for row in r.rows:
            if row.get("kind") == "compile":
                c_by[row.get("pattern_id")].append(row)
                continue
            if row.get("kind") != "match":
                continue
            pid, subj, reg = row.get("pattern_id"), row.get("subject_id"), row.get("regime")
            if reg == STREAM_REGIME:
                m_by[(subj, pid)].append(row)
            pm = patterns.get(pid) or {}
            if pm.get("arm") and pm.get("member") and reg != STREAM_REGIME:
                arms_in[(tid, pm["member"], subj, reg)][
                    pm["arm"] + (":" + pm["spelling"] if pm.get("spelling") else "")].append(row)
            if _NEST.match(subj or "") or reg == STREAM_REGIME:
                depth_in[(pid, subj)][tid].append(row)
        for (subj, pid), rows_ in m_by.items():
            cells_in[(tid, subj, pid)] = (rows_, c_by.get(pid, []))

    declared = {}
    for sb in sorted(sbids):
        declared.update(load_declared(sb, _rp.REPO_ROOT))
    cells = {}
    for k, (m, c) in cells_in.items():
        cell = _reduce_stream_cell(m, c)
        is_vars = "family-vars" in (patterns.get(k[2]) or {}).get("tags", ())
        if (is_vars and cell.misses is None and k[1] in declared
                and testees[k[0]]["assisted"]):
            try:
                cell.misses, cell.misses_src = int(declared[k[1]]["distinct_resolved"]), "declared"
            except (KeyError, ValueError):
                pass
        cells[k] = cell
    arms = {}
    for k, by_arm in arms_in.items():
        base = {a: r_ for a, r_ in by_arm.items() if ":" not in a}
        variants = {a: r_ for a, r_ in by_arm.items() if ":" in a}
        groups = [(k, base)] if not variants else [
            ((k[0], "%s[%s]" % (k[1], a.split(":", 1)[1]), k[2], k[3]),
             dict(base, **{"real": r_})) for a, r_ in sorted(variants.items())]
        for gk, garms in groups:
            ac = ArmCell()
            for arm, rows_ in garms.items():
                ns = _timed(rows_)
                if ns:
                    ac.ns[arm] = statistics.median(ns)
                fires = [(r.get("engine_metadata") or {}).get("callout_fires") for r in rows_]
                fires = [f for f in fires if f is not None]
                if fires:
                    ac.fires[arm] = int(statistics.median(fires))
            arms[gk] = ac
    # a stream rung is a depth row only where SOME testee did not match
    # (a nest-* rung always is one); every testee's reading then fills it.
    depth = {}
    for k, by_t in depth_in.items():
        texts = {tid: _depth_text(rows_) for tid, rows_ in by_t.items()}
        if _NEST.match(k[1] or "") or any(v != "match" for v in texts.values()):
            depth[k] = texts
    calib, calib_src = {}, ""
    cp = getattr(args, "callee_calib", None)
    if cp:
        calib, calib_src = load_calib(cp), os.path.basename(cp)
    return StreamData(
        query_desc=_rs._query_desc(args),
        source_desc="%s (%d record(s) matching this query)" % (
            getattr(args, "_source_desc", ""), len(selected)),
        included=included, excluded_invalid=excluded_invalid,
        superseded=superseded, newer_not_measured=newer_nm,
        machines=machines, subbench_versions=sbvers, schema_versions=svers,
        skipped_non_stream=skipped, include_unmeasured=inc_unmeasured,
        include_scratch=inc_scratch,
        store_parent=os.path.dirname(os.path.abspath(args.store)),
        subbench_alias_note=getattr(args, "_subbench_alias_note", None),
        testees=testees, ranked_testees=sorted({k[0] for k in cells} | {k[0] for k in arms}),
        not_ranked=not_ranked, cells=cells, patterns=patterns, declared=declared,
        arms=arms, depth=depth, calib=calib, calib_src=calib_src), None


# ------------------------------------------------------- derived quantities

def break_even(sd, stream, pattern):
    """-> list of (assisted_tid, text, value|None) for one vars stream, or []
    when no pcrec cell with a compile row and a measured per-call time."""
    pc = [(t, c) for (t, s, p), c in sorted(sd.cells.items())
          if s == stream and p == pattern and sd.testees[t]["engine_name"] == "pcrec"
          and c.ranked and c.compile_ns]
    if not pc:
        return []
    ptid, pcell = pc[0]
    out = []
    for (t, s, p), c in sorted(sd.cells.items()):
        if s != stream or p != pattern or not c.ranked or t == ptid:
            continue
        if sd.testees[t]["engine_name"] == "pcrec":
            continue
        d = c.ns_per_call - pcell.ns_per_call
        if d <= 0:
            out.append((t, "none: `%s` is not slower per call than `%s` "
                           "(%.0f vs %.0f ns/call)" % (t, ptid, c.ns_per_call,
                                                        pcell.ns_per_call), None))
        else:
            be = pcell.compile_ns / d
            out.append((t, "%s calls: `%s` compile %s / (assisted `%s` %.0f - "
                           "pcrec %.0f ns/call)" % (format(round(be), ","), ptid,
                                                    _rs._fmt_t(pcell.compile_ns), t,
                                                    c.ns_per_call, pcell.ns_per_call), be))
    return out


def callout_split(sd, key):
    """-> dict of the cost split of one ArmCell (None entries = not computed)."""
    tid, member, _subj, _reg = key
    ac = sd.arms[key]
    real = "real" if "real" in ac.ns else None
    member = member.split("[", 1)[0]       # calibration is per member
    ns = ac.ns
    out = dict(twin=ns.get("twin"), pas=ns.get("pass"), nofn=ns.get("pass-nofn"),
               real=ns.get("real"), fires_pass=ac.fires.get("pass"),
               fires_real=ac.fires.get("real"), wrapper=None, callee=None,
               per_fire=None, share=None, flag="", why="")
    if out["pas"] is not None and out["twin"] is not None:
        out["wrapper"] = out["pas"] - out["twin"]
    fp, fr = out["fires_pass"], out["fires_real"]
    if real and out["pas"] is not None:
        if fp is not None and fr is not None and fp == fr:
            out["callee"] = out["real"] - out["pas"]
            out["per_fire"] = out["callee"] / fr if fr else None
        else:
            out["why"] = "fires differ or absent (pass %s / real %s): real - pass not reported" % (fp, fr)
    nsf = sd.calib.get((tid, member))
    if nsf is not None and fr and out["real"]:
        out["share"] = fr * nsf / out["real"]
        eng = sd.testees[tid]
        if out["share"] > SHARE_FLAG_ANY:
            out["flag"] = "FLAG>40%"
        elif (eng["engine_name"] == "libpcre2" and eng["engine_mode"] == "jit"
              and out["share"] > SHARE_FLAG_JIT):
            out["flag"] = "over-budget>20%"
    return out


# ---------------------------------------------------------------- rendering

def _fmt_n(v):
    return "-" if v is None else format(int(v), ",")


def _fmt_rate(v):
    return "-" if v is None else format(round(v), ",")


def _streams_sorted(sd):
    return sorted({(k[1], k[2]) for k in sd.cells})


def _tl(sd, pred=None):
    return [t for t in sd.ranked_testees if pred is None or pred(t)]


def render_stream_markdown(sd):
    out = ["# pcrec-bench report\n", "reporter: %s\n" % _rp.REPORTER_VERSION,
           "## Query\n"]
    out.append("- filters: %s" % (", ".join(sd.query_desc) or "(none)"))
    out.append("- record source: %s" % sd.source_desc)
    out.append("- records included: %d" % len(sd.included))
    for rid, path in sd.included:
        t = next((tid for tid, i in sd.testees.items() if i["record_id"] == rid), None)
        i = sd.testees[t] if t else None
        out.append("    - `%s` (%s) -- status %s, record tier %s, agreement: %s; %s" % (
            rid, os.path.relpath(path, sd.store_parent),
            i["status"] if i else "?", i["rec_tier"] if i else "?",
            i["agreement"] if i else "n/a", i["env"] if i else "n/a"))
    if sd.skipped_non_stream:
        out.append("- records not of the `call-stream` regime, left to the "
                   "other grains: %d" % sd.skipped_non_stream)
    if sd.excluded_invalid:
        out.append("- records excluded (failed validation): %d" % len(sd.excluded_invalid))
        for path, probs in sd.excluded_invalid:
            out.append("    - `%s`: %s" % (os.path.relpath(path, sd.store_parent), probs[0]))
    if sd.superseded:
        out.append("- superseded: %d record(s) (OD-B15; --all-records lists them)"
                   % sum(len(v) for _k, v in sd.superseded))
    for kept, newer, status in sd.newer_not_measured:
        out.append("    - newer, not measured: `%s` (%s) -- kept `%s`" % (newer, status, kept))
    out.append("- sub-bench version(s): %s" % (", ".join(sorted(sd.subbench_versions)) or "(none)"))
    out.append("- machine(s): %s" % (", ".join(sorted(sd.machines)) or "(none)"))
    out.append("- schema version(s): %s" % (", ".join(sorted(sd.schema_versions)) or "(none)"))
    if sd.subbench_alias_note:
        out.append("- %s" % sd.subbench_alias_note)
    out.append("- grain: stream (per stream x pattern; ns per stream = median "
               "over trials of `elapsed_ns / iterations`; calls/s = "
               "`stream.calls` / seconds; segment MB/s = "
               "`stream.segment_bytes` / 10^6 / seconds -- the stream's own "
               "denominators, never the subject's size)")
    out.append("- callee calibration: %s" % (
        sd.calib_src or "none given (--callee-calib FILE): callee shares print `-`"))
    out.append("")

    out.append("## Streams\n")
    sp = _streams_sorted(sd)
    if not sp:
        out.append("_no ranked call-stream cell in this report._\n")
    for stream, pat in sp:
        decl = sd.declared.get(stream)
        out.append("### stream `%s` pattern `%s`%s\n" % (
            stream, pat, (" (declared: %s calls, %s distinct resolved, reuse %s)" % (
                decl.get("calls"), decl.get("distinct_resolved"), decl.get("reuse"))) if decl else ""))
        out.append("| testee | state | ns/stream (min-max) | calls/s | segment MB/s | "
                   "matched | nomatch | refused | gave_up | misses |")
        out.append("|---|---|---|---|---|---|---|---|---|---|")
        for t in _tl(sd):
            c = sd.cells.get((t, stream, pat))
            if c is None:
                continue
            if c.ranked:
                tt = "%s (%s-%s)" % (_rs._fmt_t(c.median_ns), _rs._fmt_t(c.min_ns),
                                     _rs._fmt_t(c.max_ns))
            else:
                tt = "-"
            st = c.state if c.state != "gave-up" else "**gave-up** (%s)" % (c.first_limit or "?")
            if c.state != "measured" and c.note and c.state != "gave-up":
                st += " (%s)" % c.note
            miss = "-" if c.misses is None else "%s (%s)" % (format(c.misses, ","), c.misses_src)
            out.append("| `%s` | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                t, st, tt, _fmt_rate(c.calls_per_s), _rs._fmt_mbs(c.mb_per_s),
                _fmt_n(c.matched), _fmt_n(c.nomatch), _fmt_n(c.refused),
                _fmt_n(c.gave_up), miss))
        be = break_even(sd, stream, pat)
        if be:
            out.append("")
            out.append("break-even (3.3), pcrec's compile paid back against each "
                       "assisted engine:")
            for _t, txt, _v in be:
                out.append("- %s" % txt)
            out.append("")
            out.append("_an assisted engine's time measures THAT assist (keying, "
                       "container, escaping), not the engine in the abstract._")
        out.append("")

    out.append("## Callout cost split (3.2)\n")
    keys = sorted(sd.arms)
    if not keys:
        out.append("_no callout-arm row (patterns tagged `arm-*` / `twin_of-*`) in this report._\n")
    else:
        out.append("| testee | member | subject (regime) | twin | pass | pass-nofn | real | "
                   "pass - twin | fires pass/real | real - pass (per fire) | callee share |")
        out.append("|---|---|---|---|---|---|---|---|---|---|---|")
        notes = []
        for k in keys:
            if not any(a.split(":")[0] == "real" for a in sd.arms[k].ns) and not sd.arms[k].ns:
                continue
            x = callout_split(sd, k)
            tid, member, subj, reg = k
            fr = "%s / %s" % ("-" if x["fires_pass"] is None else format(x["fires_pass"], ","),
                              "-" if x["fires_real"] is None else format(x["fires_real"], ","))
            rmp = "-" if x["callee"] is None else "%s (%.1f ns)" % (
                _rs._fmt_t(x["callee"]), x["per_fire"] if x["per_fire"] is not None else 0)
            sh = "-" if x["share"] is None else "%.1f %%%s" % (
                100 * x["share"], (" **%s**" % x["flag"]) if x["flag"] else "")
            out.append("| `%s` | %s | %s (%s) | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                tid, member, subj, reg, _rs._fmt_t(x["twin"]), _rs._fmt_t(x["pas"]),
                _rs._fmt_t(x["nofn"]), _rs._fmt_t(x["real"]), _rs._fmt_t(x["wrapper"]),
                fr, rmp, sh))
            if x["why"]:
                notes.append("`%s` %s on %s: %s" % (tid, member, subj, x["why"]))
        out.append("")
        for n in notes:
            out.append("- %s" % n)
        out.append("")

    out.append("## Depth of failure (6.5)\n")
    if not sd.depth:
        out.append("_no `nest-*` rung and no non-matched call-stream row in this report._\n")
    else:
        by_pat = defaultdict(list)
        for (pid, subj) in sd.depth:
            by_pat[pid].append(subj)
        for pid in sorted(by_pat):
            if all(v == "match" for s in by_pat[pid] for v in sd.depth[(pid, s)].values()):
                out.append("### pattern `%s`\n" % pid)
                out.append("every rung matches on every testee (%d rung(s))\n" % len(by_pat[pid]))
                continue
            tl = sorted({t for s in by_pat[pid] for t in sd.depth[(pid, s)]})
            out.append("### pattern `%s`\n" % pid)
            out.append("| rung | " + " | ".join("`%s`" % t for t in tl) + " |")
            out.append("|---|" + "---|" * len(tl))
            for subj in sorted(by_pat[pid], key=_depth_key):
                out.append("| `%s` | " % subj + " | ".join(
                    sd.depth[(pid, subj)].get(t, "-") for t in tl) + " |")
            out.append("")

    if sd.not_ranked:
        out.append("## Not ranked\n")
        for tid, why in sorted(sd.not_ranked):
            out.append("- `%s`: %s (use --include-unmeasured / --include-scratch to rank)" % (tid, why))
        out.append("")

    out.append("## Legend\n")
    out.append("- **ns/stream** = median wall time of one full replay of the declared "
               "call list; **calls/s** and **segment MB/s** use the stream's own "
               "`calls` / `segment_bytes` (7.1), not the subject's size.")
    out.append("- **misses** = memo compiles per replay of a vars stream: "
               "`measured` from the row's `assist_compiles`, `declared` from "
               "`values/streams.tsv` `distinct_resolved`; a native-vars testee (pcrec) compiles once and "
               "prints `-`.")
    out.append("- **refused** = host-refused calls (vars.md 5), engine-neutral; "
               "**gave_up** names the limit that stopped the stream.")
    out.append("- **real - pass** is printed only where the two arms' "
               "`callout_fires` are equal (3.2 item 5); **callee share** = "
               "fires x callee ns/fire / real ns, from the calibration TSV, "
               "an UPPER bound (warm replay); flagged over 20 % on libpcre2 jit "
               "or 40 % anywhere.")
    out.append("- **Depth of failure**: `match` or the limit's name; `WRONG "
               "(excluded)` = a silently wrong answer, never ranked.")
    for t in _tl(sd):
        i = sd.testees[t]
        out.append("- `%s` (%s%s): status %s, record tier %s, agreement %s; %s"
                   % (t, i["engine_name"], ", assisted" if i["assisted"] else "",
                      i["status"], i["rec_tier"], i["agreement"], i["env"]))
    return "\n".join(out) + "\n"


TSV_HEADER = ["section", "stream", "pattern", "testee", "state", "n_trials",
              "median_ns", "min_ns", "max_ns", "calls", "segment_bytes",
              "calls_per_s", "mb_per_s", "matched", "nomatch", "refused",
              "gave_up", "first_limit", "misses", "misses_src", "compile_ns",
              "break_even_calls", "note"]


def _f(v):
    return "" if v is None else ("%.6g" % v if isinstance(v, float) else str(v))


def render_stream_tsv(sd):
    lines = ["# " + "; ".join([
        "reporter: %s" % _rp.REPORTER_VERSION,
        "filters: %s" % (", ".join(sd.query_desc) or "(none)"),
        "source: %s" % sd.source_desc,
        "records: %d" % len(sd.included),
        "excluded_invalid: %d" % len(sd.excluded_invalid),
        "superseded: %d" % sum(len(v) for _k, v in sd.superseded),
        "newer_not_measured: %d" % len(sd.newer_not_measured),
        "subbench_versions: %s" % ",".join(sorted(sd.subbench_versions)),
        "machines: %s" % ",".join(sorted(sd.machines)),
        "schema_versions: %s" % ",".join(sorted(sd.schema_versions)),
        "grain: stream",
        "include_unmeasured: %s" % sd.include_unmeasured,
        "include_scratch: %s" % sd.include_scratch,
        "callee_calibration: %s" % (sd.calib_src or "none")]),
        "\t".join(TSV_HEADER)]

    def row(**kw):
        lines.append("\t".join(str(kw.get(h, "")) for h in TSV_HEADER))

    for tid, i in sorted(sd.testees.items()):
        row(section="record", testee=tid, state=i["status"],
            note=("tier %s; agreement %s; %s" % (i["rec_tier"], i["agreement"], i["env"])).replace("\t", " "))
    for (t, stream, pat), c in sorted(sd.cells.items()):
        row(section="cell", stream=stream, pattern=pat, testee=t, state=c.state,
            n_trials=c.n_trials or "", median_ns=_f(c.median_ns), min_ns=_f(c.min_ns),
            max_ns=_f(c.max_ns), calls=_f(c.calls), segment_bytes=_f(c.segment_bytes),
            calls_per_s=_f(c.calls_per_s), mb_per_s=_f(c.mb_per_s),
            matched=_f(c.matched), nomatch=_f(c.nomatch), refused=_f(c.refused),
            gave_up=_f(c.gave_up), first_limit=c.first_limit, misses=_f(c.misses),
            misses_src=c.misses_src, compile_ns=_f(c.compile_ns),
            note=c.note.replace("\t", " "))
    for stream, pat in _streams_sorted(sd):
        for t, txt, v in break_even(sd, stream, pat):
            row(section="break_even", stream=stream, pattern=pat, testee=t,
                break_even_calls=_f(v), note=txt.replace("\t", " "))
    for k in sorted(sd.arms):
        x = callout_split(sd, k)
        tid, member, subj, reg = k
        note = "member=%s regime=%s twin=%s pass=%s pass-nofn=%s real=%s " \
               "wrapper=%s callee=%s per_fire=%s fires_pass=%s fires_real=%s " \
               "share=%s %s %s" % (member, reg, _f(x["twin"]), _f(x["pas"]), _f(x["nofn"]),
                                   _f(x["real"]), _f(x["wrapper"]), _f(x["callee"]),
                                   _f(x["per_fire"]), _f(x["fires_pass"]),
                                   _f(x["fires_real"]), _f(x["share"]), x["flag"], x["why"])
        row(section="callout", stream=subj, pattern=member, testee=tid, note=note.strip())
    for (pid, subj), by_t in sorted(sd.depth.items(), key=lambda kv: (kv[0][0], _depth_key(kv[0][1]))):
        for t, txt in sorted(by_t.items()):
            row(section="depth", stream=subj, pattern=pid, testee=t, state=txt)
    for tid, why in sorted(sd.not_ranked):
        row(section="not_ranked", testee=tid, note=why)
    return "\n".join(lines) + "\n"
