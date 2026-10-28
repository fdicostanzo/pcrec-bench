"""pcrecbench/report_subst.py -- the SUBSTITUTION view of the reporter
([B143], plan [B140] step 5; `docs/design/subst_bench_v1.md` section 6 with
section 8a's rulings; REPORTER_VERSION v27). Selected by `pcrecbench report
--grain subst` and by nothing else.

What it reports. Records whose sub-bench declares the regime `substitution`
(schema v1.9): every match row is one (case, subject, trial) of one testee
and carries `subst` = {case, gate, nsubst, out_bytes, out_sha256}; a
`process` testee (the TOOLS tier) also carries `process` (rusage, the
`| wc -c` sink) and has no separable compile row.

What it decides (the rulings, each by name):

* TWO TIERS, REPORTED SEPARATELY (8a item 8): a testee's
  `testee.invocation` (`library`, the default when absent, or `process`)
  puts it in the LIBRARY or the TOOLS section. NO cross-tier ratio is
  computed anywhere in this module, and the report says "the tiers are not
  comparable" in words.
* LIBRARY ratios are against the baseline `pcre2-jit` (engine `libpcre2`,
  mode `jit`); TOOLS ratios are against `sed`. A tier without its baseline
  prints `-` for the ratio and says why. Ratio = baseline median / cell
  median, so `x2.00 faster` means half the time.
* `unsupported` is a FIRST-CLASS CELL, never dropped (8a item 5, design
  1.1): a compile row `unsupported-by-declaration` with no match rows
  (X44) renders as the word `unsupported` and its declared token, so a
  reader sees the case was asked and could not be expressed. `wrong` and
  `divergent-declared` show the gate word and the diagnostic's first
  differing byte; a wrong cell is excluded from every number built from
  the others (the best-other summary).
* The per-case `n_subst` sits UNDER THE CASE NAME in the row label (design
  section 6: cases differ by ~5 orders of magnitude and the reader needs
  that to interpret anything).
* pcrec's COMPILE TIME is a SEPARATE table (8a item 9), never added into a
  run time. A TOOLS testee has no compile row (S7): the section says so.
* One SUMMARY row per case at the foot of each LIBRARY table: the best
  pcrec library testee against the best other library testee, `wrong` /
  `unsupported` cells excluded from "best other". Not computed for TOOLS.

Reduction. Per (testee, subject, case): the `matched-as-expected` rows with
a `timing` block, `elapsed_ns / iterations` per trial (iterations is 1 here
by the design), then median / min / max over trials; MB/s is
`bytes_processed / 1e6 / seconds` (10^6 bytes). The record dedup, tier,
status and one-host rules are the standard reporter's, applied the same
way (newest MEASURED record per (sub-bench@version, testee, machine);
scratch and non-measured records listed under "not ranked" unless
`--include-scratch` / `--include-unmeasured`; two machine ids are refused,
O-90). Nothing here reads `bench/`.

The module imports `report` lazily (inside `main`'s dispatch) and only
borrows its record loading and filter helpers; it renders nothing the
standard grains render.
"""

from __future__ import annotations

import os
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field

from pcrecbench import report as _rp

TIER_LIBRARY = "library"
TIER_TOOLS = "tools"
TIER_TITLE = {TIER_LIBRARY: "LIBRARY", TIER_TOOLS: "TOOLS"}

#: per-tier baseline: (engine_name, engine_mode or None for any)
BASELINE = {TIER_LIBRARY: ("libpcre2", "jit"), TIER_TOOLS: ("sed", None)}

#: the sentence both renderings carry (8a item 8).
TIERS_NOT_COMPARABLE = ("the tiers are not comparable: the LIBRARY tier times "
                        "only the transform in-process; the TOOLS tier times "
                        "a whole `tool ... | wc -c` launch (process start, "
                        "pattern parse, I/O). No cross-tier ratio is "
                        "computed.")

NOT_IN_SET = ("Oniguruma, TRE and Vectorscan are not in this set (no usable "
              "substitute API, subst_bench_v1.md 3.1); that is a roster fact, "
              "not an `unsupported` cell.")


def is_substitution_record(rec) -> bool:
    s = rec.setup or {}
    return "substitution" in (s.get("subbench", {}).get("regimes") or [])


def tier_of(setup) -> str:
    inv = (setup.get("testee") or {}).get("invocation", "library")
    return TIER_TOOLS if inv == "process" else TIER_LIBRARY


@dataclass
class Cell:
    """One (testee, subject, case) cell."""
    state: str = "absent"          # measured | unsupported | wrong |
    #                                divergent-declared | <other outcome>
    gate: str = ""
    pattern_id: str = ""
    n_trials: int = 0
    median_ns: float | None = None
    min_ns: float | None = None
    max_ns: float | None = None
    mb_per_s: float | None = None
    nsubst: int | None = None
    out_bytes: int | None = None
    bytes_processed: int | None = None
    maxrss_kb: float | None = None
    user_s: float | None = None
    sys_s: float | None = None
    note: str = ""                 # unsupported token / diagnostic excerpt
    declaration_ref: str = ""
    compile_median_ns: float | None = None
    compile_phases: dict = field(default_factory=dict)  # name -> median ns
    compile_outcome: str = ""

    @property
    def ranked(self) -> bool:
        return self.state in ("measured", "divergent-declared") and \
            self.median_ns is not None


@dataclass
class SubstData:
    query_desc: list
    source_desc: str
    included: list
    excluded_invalid: list
    superseded: list
    newer_not_measured: list
    machines: set
    subbench_versions: set
    schema_versions: set
    skipped_non_subst: int
    include_unmeasured: bool
    include_scratch: bool
    include_provenance: bool
    store_parent: str
    subbench_alias_note: str | None
    # testee_id -> dict(tier, status, status_detail, record_id, rec_tier,
    #                   engine_name, engine_mode, agreement, schema_version)
    testees: dict
    ranked_testees: list           # testee ids that are ranked, sorted
    not_ranked: list               # (testee_id, reason)
    # (testee_id, subject, case) -> Cell     (ranked testees only)
    cells: dict
    subjects: dict                 # subject_id -> bytes
    cases: dict                    # case id -> (pattern_id, {subject: nsubst})
    baseline: dict                 # tier -> testee_id | None


def _first_diff(diag):
    if not diag:
        return ""
    d = str(diag).replace("\n", " ")
    return d if len(d) <= 160 else d[:157] + "..."


def _unsupported_token(row):
    ref = str(row.get("declaration_ref") or "")
    diag = str(row.get("diagnostic") or "")
    for src in (ref, diag):
        i = src.rfind("unsupported:")
        if i >= 0:
            return src[i + len("unsupported:"):].strip(" )")
    j = diag.find("declared unsupported (")
    if j >= 0:
        return diag[j + len("declared unsupported ("):].split(")")[0]
    return "unsupported"


def _reduce_cell(match_rows, compile_rows):
    c = Cell()
    if match_rows:
        subst = [r.get("subst") or {} for r in match_rows]
        gates = Counter(s.get("gate") for s in subst)
        c.pattern_id = match_rows[0].get("pattern_id", "")
        timed = []
        for r in match_rows:
            t = r.get("timing") or {}
            it = t.get("iterations")
            if r.get("match_outcome") == "matched-as-expected" and it:
                timed.append((t["elapsed_ns"] / it, t.get("bytes_processed"), r))
        s0 = next((s for s in subst if s), {})
        c.nsubst = s0.get("nsubst")
        c.out_bytes = s0.get("out_bytes")
        if gates.get("wrong"):
            c.state = "wrong"
            c.gate = "wrong"
            bad = next(r for r in match_rows
                       if (r.get("subst") or {}).get("gate") == "wrong")
            c.note = _first_diff(bad.get("diagnostic"))
        elif timed:
            ns = [t for t, _b, _r in timed]
            c.n_trials = len(ns)
            c.median_ns = statistics.median(ns)
            c.min_ns, c.max_ns = min(ns), max(ns)
            c.bytes_processed = next((b for _t, b, _r in timed if b), None)
            if c.bytes_processed and c.median_ns:
                c.mb_per_s = c.bytes_processed / 1e6 / (c.median_ns / 1e9)
            if gates.get("divergent-declared") and \
                    gates.get("divergent-declared") == sum(gates.values()):
                c.state = c.gate = "divergent-declared"
                c.declaration_ref = next(
                    (s.get("declaration_ref") for s in subst
                     if s.get("declaration_ref")), "") or ""
            else:
                c.state, c.gate = "measured", "agrees"
            procs = [t[2].get("process") for t in timed if t[2].get("process")]
            if procs:
                c.maxrss_kb = statistics.median(p["maxrss_kb"] for p in procs)
                c.user_s = statistics.median(p["user_s"] for p in procs)
                c.sys_s = statistics.median(p["sys_s"] for p in procs)
        else:
            outs = Counter(r.get("match_outcome") for r in match_rows)
            c.state = outs.most_common(1)[0][0] if outs else "absent"
            c.note = _first_diff(match_rows[0].get("diagnostic"))
    elif compile_rows:
        outc = Counter(r.get("compile_outcome") for r in compile_rows)
        top = outc.most_common(1)[0][0]
        c.compile_outcome = top
        c.pattern_id = compile_rows[0].get("pattern_id", "")
        if top == "unsupported-by-declaration":
            c.state = "unsupported"
            c.note = _unsupported_token(compile_rows[0])
            c.declaration_ref = str(compile_rows[0].get("declaration_ref") or "")
        else:
            c.state = top
            c.note = _first_diff(compile_rows[0].get("diagnostic"))
    done = [r for r in compile_rows if r.get("compile_outcome") == "compiled"]
    tot = [(r.get("cost") or {}).get("total_ns") for r in done]
    tot = [t for t in tot if isinstance(t, (int, float))]
    if tot:
        c.compile_median_ns = statistics.median(tot)
        ph = defaultdict(list)
        for r in done:
            for p in (r.get("cost") or {}).get("phases") or []:
                ph[p["name"]].append(p["elapsed_ns"])
        c.compile_phases = {k: statistics.median(v) for k, v in ph.items()}
        c.compile_outcome = "compiled"
    return c


def select_latest(valid, args):
    """The standard reporter's record dedup (newest MEASURED record per
    (sub-bench@version, testee, machine); `--all-records` keeps all) --
    shared with the stream view ([B148] rep). -> (kept, superseded,
    newer_not_measured, eff) with eff = record path -> effective testee id."""
    all_records = bool(getattr(args, "all_records", False))
    groups = defaultdict(list)
    for r in valid:
        s = r.setup
        key = (s["subbench"]["id"] + "@" + str(s["subbench"]["version"]),
               s["testee"]["testee_id"], s["environment"]["machine_id"])
        groups[key].append((s["run"]["timestamp"], r))
    kept, superseded, newer_nm, eff = [], [], [], {}
    for (_sb, tid, _m), entries in groups.items():
        entries.sort(key=lambda te: _rp.ts_key(te[0]))
        if all_records:
            for ts, r in entries:
                kept.append(r)
                eff[r.path] = tid + "@" + _rp._date_suffix(ts) if len(entries) > 1 else tid
            continue
        meas = [(ts, r) for ts, r in entries
                if r.setup.get("status", "measured") == "measured"]
        kts, kr = meas[-1] if meas else entries[-1]
        kept.append(kr)
        eff[kr.path] = tid
        older = [r for ts, r in entries if _rp.ts_key(ts) < _rp.ts_key(kts)]
        if older:
            superseded.append((kr.setup["record_id"],
                               [r.setup["record_id"] for r in older]))
        for ts, r in entries:
            if _rp.ts_key(ts) > _rp.ts_key(kts):
                newer_nm.append((kr.setup["record_id"], r.setup["record_id"],
                                 r.setup.get("status", "measured")))
    return kept, superseded, newer_nm, eff


def build_subst_report(loaded, args, known_testee_ids=None):
    """-> (SubstData | None, error). Same refusals as the standard builder
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
    subst_sel = [r for r in selected if is_substitution_record(r)]
    skipped = len(selected) - len(subst_sel)
    if not subst_sel:
        return None, ("--grain subst: no record in the selection declares the "
                      "regime `substitution` (%d record(s) selected, all of "
                      "another regime)" % len(selected))
    majors = {r.schema_major for r in subst_sel if r.schema_major is not None}
    if len(majors) > 1:
        return None, ("refusing to report: the selected records mix MAJOR "
                      "schema versions with no declared migration")
    excluded_invalid, valid = [], []
    for r in subst_sel:
        if r.problems:
            excluded_invalid.append((r.path, [str(p) for p in r.problems]))
        else:
            valid.append(r)

    valid, superseded, newer_nm, eff = select_latest(valid, args)
    hosts = sorted({r.setup["environment"]["machine_id"] for r in valid})
    if len(hosts) > 1:
        return None, ("the selected records span %d machines (%s); a report "
                      "is PER HOST and never pools machine_ids into one cell "
                      "-- add --machine <id> (O-90, [B137])"
                      % (len(hosts), ", ".join(hosts)))

    included, machines, svers, sbvers = [], set(), set(), set()
    testees, not_ranked, cells_in = {}, [], {}
    subjects = {}
    inc_unmeasured = bool(getattr(args, "include_unmeasured", False))
    inc_scratch = bool(getattr(args, "include_scratch", False))
    for r in sorted(valid, key=lambda r: eff[r.path]):
        s = r.setup
        tid = eff[r.path]
        rid = s["record_id"]
        included.append((rid, r.path))
        machines.add(s["environment"]["machine_id"])
        svers.add(s["schema_version"])
        sbvers.add(s["subbench"]["id"] + "@" + str(s["subbench"]["version"]))
        t = s["testee"]
        status = s.get("status", "measured")
        rtier = s.get("tier", "pinned")
        info = dict(tier=tier_of(s), status=status,
                    status_detail=s.get("status_detail"), record_id=rid,
                    rec_tier=rtier, engine_name=t.get("engine_name"),
                    engine_mode=t.get("engine_mode"),
                    agreement=_rp._agreement_display(
                        s.get("trial_agreement"), str(s.get("schema_version", ""))),
                    schema_version=str(s.get("schema_version", "")),
                    compile_cost_definition=t.get("compile_cost_definition", ""))
        testees[tid] = info
        for sj in s.get("subjects", []):
            subjects[sj["subject_id"]] = sj.get("bytes_offered")
        if status != "measured" and not inc_unmeasured:
            not_ranked.append((tid, "status %s" % status))
            continue
        if rtier == "scratch" and not inc_scratch:
            not_ranked.append((tid, "tier scratch"))
            continue
        m_by, c_by = defaultdict(list), defaultdict(list)
        for row in r.rows:
            if row.get("kind") == "match":
                sub = row.get("subst") or {}
                m_by[(row.get("subject_id"), sub.get("case") or row.get("pattern_id"))].append(row)
            elif row.get("kind") == "compile":
                c_by[row.get("pattern_id")].append(row)
        pat_case = {}
        for (subj, case), rows_ in m_by.items():
            pat_case[rows_[0].get("pattern_id")] = case
        for (subj, case), rows_ in m_by.items():
            cells_in[(tid, subj, case)] = (rows_, c_by.get(rows_[0].get("pattern_id"), []))
        # unsupported / refused cases: compile rows with no match rows
        for pid, crows in c_by.items():
            if pid in pat_case:
                continue
            case = pid.split("-", 1)[0]
            for subj in (list(subjects) or [""]):
                cells_in[(tid, "*", case)] = ([], crows)
                break

    cells = {k: _reduce_cell(m, c) for k, (m, c) in cells_in.items()}
    ranked = sorted({k[0] for k in cells})
    # a "*" cell (compile-only: unsupported/refused) applies to every subject
    subj_ids = sorted({k[1] for k in cells if k[1] != "*"}) or sorted(subjects)
    for (tid, subj, case), c in list(cells.items()):
        if subj == "*":
            del cells[(tid, subj, case)]
            for sj in subj_ids:
                cells[(tid, sj, case)] = c
    cases = {}
    for (tid, subj, case), c in cells.items():
        pid, per = cases.setdefault(case, (c.pattern_id, {}))
        if c.pattern_id and not pid:
            cases[case] = (c.pattern_id, per)
        if c.state == "measured" and c.nsubst is not None:
            per.setdefault(subj, Counter())[c.nsubst] += 1
    cases = {k: (v[0], {s: cnt.most_common(1)[0][0] for s, cnt in v[1].items()})
             for k, v in cases.items()}

    baseline = {}
    for tier, (eng, mode) in BASELINE.items():
        baseline[tier] = next(
            (t for t in ranked if testees[t]["tier"] == tier
             and testees[t]["engine_name"] == eng
             and (mode is None or testees[t]["engine_mode"] == mode)), None)
    return SubstData(
        query_desc=_query_desc(args),
        source_desc="%s (%d record(s) matching this query)" % (
            getattr(args, "_source_desc", ""), len(selected)),
        included=included, excluded_invalid=excluded_invalid,
        superseded=superseded, newer_not_measured=newer_nm,
        machines=machines, subbench_versions=sbvers, schema_versions=svers,
        skipped_non_subst=skipped, include_unmeasured=inc_unmeasured,
        include_scratch=inc_scratch,
        include_provenance=bool(getattr(args, "include_provenance", False)),
        store_parent=os.path.dirname(os.path.abspath(args.store)),
        subbench_alias_note=getattr(args, "_subbench_alias_note", None),
        testees=testees, ranked_testees=ranked, not_ranked=not_ranked,
        cells=cells, subjects=subjects, cases=cases, baseline=baseline), None


def _query_desc(args):
    """The standard reporter's own order and spelling (build_report), so the
    TSV header round-trips through scripts/regen_reports.py's header_argv."""
    out = []
    for name in ("subbench", "version", "regime", "machine", "since", "until"):
        v = getattr(args, name, None)
        if v:
            out.append("%s=%s" % (name, v))
    for f, v in getattr(args, "where", None) or []:
        out.append("where %s=%s" % (f, v))
    for t in getattr(args, "testee", None) or []:
        out.append("testee=%s" % t)
    if getattr(args, "include_synthetic", False):
        out.append("include-synthetic")
    return out


# ------------------------------------------------------------- formatting

def _fmt_t(ns):
    if ns is None:
        return "-"
    s = ns / 1e9
    if s >= 1:
        return "%.3f s" % s
    if s >= 1e-3:
        return "%.3f ms" % (s * 1e3)
    return "%.1f us" % (s * 1e6)


def _fmt_mbs(v):
    return "-" if v is None else ("%.0f MB/s" % v if v >= 100 else "%.1f MB/s" % v)


def _fmt_rss(kb):
    if kb is None:
        return "-"
    return "%.1f MB" % (kb / 1024.0) if kb >= 1024 else "%d KB" % kb


def _ratio(base_ns, ns):
    """-> (float | None, text). >1 = faster than the baseline."""
    if base_ns is None or ns is None or not ns:
        return None, "-"
    r = base_ns / ns
    if abs(r - 1.0) < 0.005:
        return r, "x1.00 (same)"
    return r, ("x%.2f faster" % r) if r > 1 else ("x%.2f slower" % (1.0 / r))


def _short(tid):
    return tid


def _tier_testees(sd, tier):
    return [t for t in sd.ranked_testees if sd.testees[t]["tier"] == tier]


def _cases_sorted(sd):
    def key(c):
        digits = "".join(ch for ch in c if ch.isdigit())
        return (int(digits) if digits else 0, c)
    return sorted(sd.cases, key=key)


def _case_label(sd, case, subj):
    pid, per = sd.cases[case]
    n = per.get(subj)
    lab = "**%s** `%s`" % (case, pid or case)
    return lab + (" (n_subst %s)" % format(n, ",") if n is not None else
                  " (n_subst -)")


def _cell_text(sd, tier, tid, subj, case, base_ns):
    c = sd.cells.get((tid, subj, case))
    if c is None:
        return "-"
    if c.state == "unsupported":
        return "**unsupported** (%s)" % (c.note or "declared")
    if c.state == "wrong":
        return "**WRONG** (excluded; %s)" % (c.note or "no diagnostic")
    if not c.ranked:
        return "%s%s" % (c.state, (" (%s)" % c.note) if c.note else "")
    _r, rt = _ratio(base_ns, c.median_ns)
    out = "%s (%s)" % (_fmt_t(c.median_ns), _fmt_mbs(c.mb_per_s))
    if sd.baseline.get(tier) and tid != sd.baseline[tier]:
        out += " %s" % rt
    elif tid == sd.baseline.get(tier):
        out += " baseline"
    if c.state == "divergent-declared":
        out += " **divergent-declared** (%s)" % (c.declaration_ref or "declared")
    if tier == TIER_TOOLS and c.maxrss_kb is not None:
        out += "<br>maxrss %s" % _fmt_rss(c.maxrss_kb)
    return out


def _base_ns(sd, tier, subj, case):
    b = sd.baseline.get(tier)
    c = sd.cells.get((b, subj, case)) if b else None
    return c.median_ns if c is not None and c.ranked else None


def _summary_row(sd, subj, case):
    """pcrec LIBRARY / best-other-library for one case: text, plus the
    numbers for the TSV."""
    lib = _tier_testees(sd, TIER_LIBRARY)
    pc = [(sd.cells[(t, subj, case)].median_ns, t) for t in lib
          if sd.testees[t]["engine_name"] == "pcrec"
          and (t, subj, case) in sd.cells and sd.cells[(t, subj, case)].ranked]
    ot = [(sd.cells[(t, subj, case)].median_ns, t) for t in lib
          if sd.testees[t]["engine_name"] != "pcrec"
          and (t, subj, case) in sd.cells and sd.cells[(t, subj, case)].ranked]
    if not pc:
        return None, "no ranked pcrec library cell"
    if not ot:
        return None, "no ranked other-library cell"
    p, ot_ = min(pc), min(ot)
    r = ot_[0] / p[0]
    word = "faster" if r > 1 else "slower"
    val = r if r > 1 else 1.0 / r
    return (r, p[1], ot_[1]), "`%s` x%.2f %s than best-other `%s`" % (
        p[1], val, word, ot_[1])


# ---------------------------------------------------------------- markdown

def render_subst_markdown(sd):
    out = ["# pcrec-bench report\n", "reporter: %s\n" % _rp.REPORTER_VERSION,
           "## Query\n"]
    out.append("- filters: %s" % (", ".join(sd.query_desc) or "(none)"))
    out.append("- record source: %s" % sd.source_desc)
    out.append("- records included: %d" % len(sd.included))
    for rid, path in sd.included:
        t = next((tid for tid, i in sd.testees.items() if i["record_id"] == rid), None)
        ag = sd.testees[t]["agreement"] if t else "n/a"
        out.append("    - `%s` (%s) — agreement: %s" % (
            rid, os.path.relpath(path, sd.store_parent), ag))
    if sd.skipped_non_subst:
        out.append("- records not of the `substitution` regime, left to the "
                   "other grains: %d" % sd.skipped_non_subst)
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
    out.append("- grain: subst (per case x subject; median over trials of "
               "`elapsed_ns / iterations`; MB/s = subject bytes / 10^6 / "
               "seconds; ratio = baseline median / cell median)")
    out.append("- %s" % TIERS_NOT_COMPARABLE)
    out.append("- %s" % NOT_IN_SET)
    for tier in (TIER_LIBRARY, TIER_TOOLS):
        b = sd.baseline.get(tier)
        out.append("- %s baseline: %s" % (
            TIER_TITLE[tier],
            ("`%s`" % b) if b else "none in this report (ratios print `-`)"))
    out.append("")

    for tier in (TIER_LIBRARY, TIER_TOOLS):
        tl = _tier_testees(sd, tier)
        out.append("## %s tier\n" % TIER_TITLE[tier])
        if not tl:
            out.append("_no ranked %s testee in this report._\n" % TIER_TITLE[tier].lower())
            continue
        subs = sorted({k[1] for k in sd.cells if k[0] in tl})
        for subj in subs:
            nb = sd.subjects.get(subj)
            out.append("### %s subject `%s`%s\n" % (
                TIER_TITLE[tier], subj, (" (%s B)" % format(nb, ",")) if nb else ""))
            header = ["case"] + ["`%s`" % t for t in tl]
            out.append("| " + " | ".join(header) + " |")
            out.append("|" + "|".join(["---"] * len(header)) + "|")
            for case in _cases_sorted(sd):
                if not any((t, subj, case) in sd.cells for t in tl):
                    continue
                b = _base_ns(sd, tier, subj, case)
                row = [_case_label(sd, case, subj)] + [
                    _cell_text(sd, tier, t, subj, case, b) for t in tl]
                out.append("| " + " | ".join(row) + " |")
            if tier == TIER_LIBRARY:
                has_pc = any(sd.testees[t]["engine_name"] == "pcrec" for t in tl)
                if not has_pc:
                    out.append("")
                    out.append("pcrec LIBRARY / best-other-library: n/a (no "
                               "ranked pcrec library testee in this report)")
                else:
                    srow = []
                    for case in _cases_sorted(sd):
                        if not any((t, subj, case) in sd.cells for t in tl):
                            continue
                        _v, txt = _summary_row(sd, subj, case)
                        srow.append("**%s**: %s" % (case, txt if _v else "n/a (%s)" % txt))
                    out.append("")
                    out.append("pcrec LIBRARY / best-other-library, per case "
                               "(`wrong` / `unsupported` cells excluded from "
                               "best-other): " + "; ".join(srow))
            out.append("")
        # compile: separate, never added into a run time
        out.append("### %s compile (a SEPARATE column, never added into a run time)\n" % TIER_TITLE[tier])
        if tier == TIER_TOOLS:
            out.append("_none: a command-line tool re-parses its pattern on "
                       "every launch, so there is no separable compile (schema "
                       "v1.9 S7); the parse is inside the timed process wall "
                       "time and no compile row is recorded._\n")
            continue
        header = ["case"] + ["`%s`" % t for t in tl]
        out.append("| " + " | ".join(header) + " |")
        out.append("|" + "|".join(["---"] * len(header)) + "|")
        any_row = False
        subj0 = subs[0] if subs else None
        for case in _cases_sorted(sd):
            vals = []
            for t in tl:
                c = sd.cells.get((t, subj0, case))
                if c is None:
                    vals.append("-")
                elif c.state == "unsupported":
                    vals.append("unsupported")
                elif c.compile_median_ns is None:
                    vals.append("-" if not c.compile_outcome else c.compile_outcome)
                else:
                    txt = _fmt_t(c.compile_median_ns)
                    if len(c.compile_phases) > 1:
                        txt += " (" + ", ".join(
                            "%s %s" % (k, _fmt_t(v)) for k, v in sorted(c.compile_phases.items())) + ")"
                    vals.append(txt)
            if any(v != "-" for v in vals):
                any_row = True
                out.append("| " + " | ".join([_case_label(sd, case, subj0)] + vals) + " |")
        if not any_row:
            out.append("| _no compile rows_ |" + " |" * len(tl))
        out.append("")

    if sd.not_ranked:
        out.append("## Not ranked\n")
        for tid, why in sorted(sd.not_ranked):
            out.append("- `%s`: %s (use --include-unmeasured / --include-scratch to rank)" % (tid, why))
        out.append("")

    out.append("## Legend\n")
    out.append("- **cell** = median wall time over trials (MB/s of subject) "
               "and the ratio against the tier's baseline; `x2.00 faster` "
               "means half the baseline's time. TOOLS cells add the median "
               "maxrss under the time.")
    out.append("- **unsupported** = the (testee, case) cannot express the "
               "case; a result, never a wrong answer, and never dropped "
               "(its token is the declared reason). **WRONG** = the output "
               "sha256 differs from the oracle's and the divergence is not "
               "declared; shown with the first differing byte, excluded from "
               "every number built from the others. **divergent-declared** = "
               "differs by a declared, cited divergence.")
    out.append("- **n_subst** under a case name = the oracle's substitution "
               "count for that subject (from the agreeing cells).")
    out.append("- %s" % TIERS_NOT_COMPARABLE)
    for tier in (TIER_LIBRARY, TIER_TOOLS):
        for t in _tier_testees(sd, tier):
            i = sd.testees[t]
            out.append("- `%s` (%s, %s tier): status %s, record tier %s, agreement %s"
                       % (t, i["engine_name"], tier, i["status"], i["rec_tier"], i["agreement"]))
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------- tsv

TSV_HEADER = ["section", "tier", "subject", "case", "pattern_id", "testee",
              "state", "gate", "n_trials", "median_ns", "min_ns", "max_ns",
              "mb_per_s", "ratio_vs_baseline", "n_subst", "out_bytes",
              "maxrss_kb", "user_s", "sys_s", "compile_median_ns", "note"]


def _f(v, fmt="%.6g"):
    return "" if v is None else (fmt % v if isinstance(v, float) else str(v))


def render_subst_tsv(sd):
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
        "grain: subst",
        "include_unmeasured: %s" % sd.include_unmeasured,
        "include_scratch: %s" % sd.include_scratch,
        "baseline_library: %s" % (sd.baseline.get(TIER_LIBRARY) or "none"),
        "baseline_tools: %s" % (sd.baseline.get(TIER_TOOLS) or "none"),
        "cross_tier_ratio: none (the tiers are not comparable)"]),
        "\t".join(TSV_HEADER)]

    def row(**kw):
        lines.append("\t".join(str(kw.get(h, "")) for h in TSV_HEADER))

    for tid, i in sorted(sd.testees.items()):
        row(section="record", tier=i["tier"], testee=tid, state=i["status"],
            gate=i["rec_tier"], note=i["agreement"].replace("\t", " "))
    for tier in (TIER_LIBRARY, TIER_TOOLS):
        tl = _tier_testees(sd, tier)
        subs = sorted({k[1] for k in sd.cells if k[0] in tl})
        for subj in subs:
            for case in _cases_sorted(sd):
                b = _base_ns(sd, tier, subj, case)
                for t in tl:
                    c = sd.cells.get((t, subj, case))
                    if c is None:
                        continue
                    r, _txt = _ratio(b, c.median_ns) if c.ranked and t != sd.baseline.get(tier) else (None, "")
                    row(section="cell", tier=tier, subject=subj, case=case,
                        pattern_id=c.pattern_id, testee=t, state=c.state,
                        gate=c.gate, n_trials=c.n_trials or "",
                        median_ns=_f(c.median_ns), min_ns=_f(c.min_ns),
                        max_ns=_f(c.max_ns), mb_per_s=_f(c.mb_per_s),
                        ratio_vs_baseline=_f(r), n_subst=_f(c.nsubst),
                        out_bytes=_f(c.out_bytes), maxrss_kb=_f(c.maxrss_kb),
                        user_s=_f(c.user_s), sys_s=_f(c.sys_s),
                        compile_median_ns=_f(c.compile_median_ns),
                        note=(c.note or c.declaration_ref).replace("\t", " "))
                if tier == TIER_LIBRARY and any((t, subj, case) in sd.cells for t in tl):
                    v, txt = _summary_row(sd, subj, case)
                    row(section="summary", tier=tier, subject=subj, case=case,
                        pattern_id=sd.cases[case][0],
                        testee=v[1] if v else "", state="pcrec-vs-best-other" if v else "n/a",
                        ratio_vs_baseline=_f(v[0]) if v else "",
                        note=txt if not v else "best-other=" + v[2])
    for tid, why in sorted(sd.not_ranked):
        row(section="not_ranked", tier=sd.testees[tid]["tier"], testee=tid, note=why)
    return "\n".join(lines) + "\n"
