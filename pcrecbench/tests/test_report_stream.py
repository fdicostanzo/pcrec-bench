"""Tests for the STREAM view (`report --grain stream`, pcrecbench/report_stream.py,
[B148] lane b148rep, docs/design/unusual_set_v1.md 7.5).

Hand-built LoadedRecords (the [B9]/[B143] bypass technique) so every printed
number is checked against arithmetic done by hand here, never by the code
under test. No engine, no store: `bench/unusual/values/streams.tsv` is read
(read-only) for the declared miss counts, exactly as the view does.

Plain runnable module, like test_report.py:

    python3 -m pcrecbench.tests.test_report_stream
"""

from __future__ import annotations

import glob
import os
import sys
import tempfile
import traceback

from pcrecbench import report, report_stream
from pcrecbench.tests import test_report as T

_check = T._check
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOAD_OK = {"verdict": "quiet"}
OCC_OK = {"before": {"verdict": "pass"}, "after": {"verdict": "pass"}}


def _srow(pid, subj, trial, seq, ns, calls, seg, *, outcome="matched-as-expected",
          matched=None, nomatch=0, refused=0, gave_up=0, first_limit=None,
          meta=None, regime="call-stream", iterations=1):
    st = {"calls": calls, "segment_bytes": seg,
          "matched": calls - nomatch - refused - gave_up if matched is None else matched,
          "nomatch": nomatch, "refused": refused, "gave_up": gave_up,
          "results_sha256": "0" * 64}
    if first_limit:
        st["first_limit"] = first_limit
    r = {"kind": "match", "pattern_id": pid, "subject_id": subj, "regime": regime,
         "trial": trial, "seq": seq, "match_outcome": outcome}
    if regime == "call-stream":
        r["stream"] = st
    if outcome == "gave-up":
        r["diagnostic"] = "call 1 of 1: gave up on " + (first_limit or "x")
    else:
        r["timing"] = {"elapsed_ns": ns, "iterations": iterations,
                       "bytes_processed": seg}
    if meta:
        r["engine_metadata"] = meta
    return r


def _crow(pid, total_ns):
    return {"kind": "compile", "pattern_id": pid, "trial": 1, "seq": 0,
            "compile_outcome": "compiled", "cost": {"total_ns": total_ns}}


def _rec(tid, engine, rows, *, assisted=False, status="measured", tier="scratch",
         patterns=None, machine="m1", ts="2026-10-28T10:00:00Z", mode="calls"):
    s = T._mini_setup(tid, sb_id="unusual", sb_version="0.1", machine=machine,
                      timestamp=ts, status=status, tier=tier, patterns=patterns)
    s["schema_version"] = "1.11"
    s["subbench"]["regimes"] = ["call-stream", "large-subject-throughput"]
    s["testee"].update({"engine_name": engine, "engine_mode": mode})
    if assisted:
        s["testee"]["assist"] = {"assist_version": "v01", "members": []}
    s["environment"] = {"machine_id": machine, "load": LOAD_OK, "occupancy": OCC_OK}
    return report.LoadedRecord(path="/x/%s.jsonl" % tid, setup=s, rows=rows,
                               problems=[], schema_major=1, schema_minor=11)


def _build(recs, **kw):
    kw.setdefault("include_scratch", True)
    args = T._args(grain="stream", store="/x/store", **kw)
    return report_stream.build_stream_report(recs, args)


def _vars_population():
    """tenant-d64 (declared distinct_resolved 64 in values/streams.tsv):
    pcrec 1 ms / replay, compile 5 ms; an assisted engine 11 ms / replay."""
    pats = [{"pattern_id": "va-tenant", "tags": ["family-vars"]}]
    pc = _rec("pcrec_auto", "pcrec", [
        _crow("va-tenant", 5_000_000),
        _srow("va-tenant", "tenant-d64", 1, 1, 1_000_000, 16384, 524288, nomatch=4000),
        _srow("va-tenant", "tenant-d64", 2, 2, 3_000_000, 16384, 524288, nomatch=4000),
        _srow("va-tenant", "tenant-d64", 3, 3, 2_000_000, 16384, 524288, nomatch=4000)],
        patterns=pats)
    asst = _rec("re2_assist", "re2", [
        _srow("va-tenant", "tenant-d64", t, t, 11_000_000, 16384, 524288, nomatch=4000,
              refused=3) for t in (1, 2, 3)], assisted=True, patterns=pats)
    return [pc, asst]


def test_stream_cell_reduction_by_hand_b148rep():
    sd, err = _build(_vars_population())
    _check(err is None, "builds: %s" % err)
    c = sd.cells[("pcrec_auto", "tenant-d64", "va-tenant")]
    # median of 1,3,2 ms = 2 ms; calls/s = 16384 / 0.002; MB/s = 524288/1e6/0.002
    _check(c.median_ns == 2_000_000 and (c.min_ns, c.max_ns) == (1_000_000, 3_000_000),
           "median/min/max %r %r %r" % (c.median_ns, c.min_ns, c.max_ns))
    _check(abs(c.calls_per_s - 8_192_000) < 1e-6, "calls/s %r" % c.calls_per_s)
    _check(abs(c.mb_per_s - 262.144) < 1e-9, "MB/s %r" % c.mb_per_s)
    _check((c.nomatch, c.refused, c.gave_up) == (4000, 0, 0), "counts")
    a = sd.cells[("re2_assist", "tenant-d64", "va-tenant")]
    _check(a.refused == 3 and a.matched == 16384 - 4000 - 3, "assisted refused/matched")
    # the miss count: declared (values/streams.tsv, 64) for the ASSISTED testee
    # only; the native-vars one compiles once and prints no miss column
    _check((a.misses, a.misses_src) == (64, "declared"), "assisted misses %r" % ((a.misses, a.misses_src),))
    _check(c.misses is None, "native vars testee: no miss count")
    md = report_stream.render_stream_markdown(sd)
    _check("| `pcrec_auto` | measured | 2.000 ms (1.000 ms-3.000 ms) | 8,192,000 | "
           "262 MB/s |" in md, "pcrec row:\n" + md)
    _check("64 (declared)" in md and "status inconclusive" not in md, "misses column")
    _check("status measured, record tier scratch" in md and "load quiet; occupancy before pass / after pass" in md,
           "every record carries its status/tier/environment")


def test_break_even_by_hand_b148rep():
    sd, _ = _build(_vars_population())
    be = report_stream.break_even(sd, "tenant-d64", "va-tenant")
    # pcrec 2e6/16384 = 122.07 ns/call; assisted 11e6/16384 = 671.35; d = 549.28
    # break-even = 5e6 / 549.28 = 9102.9 calls
    _check(len(be) == 1 and be[0][0] == "re2_assist", "one assisted engine: %r" % (be,))
    exp = 5_000_000 / ((11_000_000 - 2_000_000) / 16384)
    _check(abs(be[0][2] - exp) < 1e-6, "value %r vs %r" % (be[0][2], exp))
    # an assisted engine that is NOT slower per call has no break-even
    pop = _vars_population()
    for r in pop[1].rows:
        r["timing"]["elapsed_ns"] = 1_000_000
    sd2, _ = _build(pop)
    be2 = report_stream.break_even(sd2, "tenant-d64", "va-tenant")
    _check(be2[0][2] is None and be2[0][1].startswith("none"), "CONTROL: %r" % (be2,))


def _callout_population():
    tags = lambda arm, extra=(): ["family-callouts", "arm-" + arm, "twin_of-co-luhn", *extra]  # noqa: E731
    pats = [{"pattern_id": "co-luhn", "tags": tags("real")},
            {"pattern_id": "co-luhn-pass", "tags": tags("pass")},
            {"pattern_id": "co-luhn-twin", "tags": tags("twin")},
            {"pattern_id": "co-luhn-nofn", "tags": tags("pass-nofn")}]

    def thr(pid, ns, fires=None):
        return _srow(pid, "co-luhn-1m", 1, 1, ns, 1, 1_000_000, regime="large-subject-throughput",
                     meta={"callout_fires": fires} if fires is not None else None)
    jit = _rec("libpcre2_jit", "libpcre2", [
        thr("co-luhn-twin", 1_000_000), thr("co-luhn-pass", 1_300_000, 10_000),
        thr("co-luhn-nofn", 1_100_000), thr("co-luhn", 2_000_000, 10_000),
        _srow("cscan", "seg-s", 1, 9, 1_000_000, 4, 400)], patterns=pats, mode="jit")
    # fires differ between pass and real on this engine: real - pass NOT reported
    pcr = _rec("pcrec_auto", "pcrec", [
        thr("co-luhn-twin", 900_000), thr("co-luhn-pass", 1_000_000, 10_000),
        thr("co-luhn", 1_500_000, 12_000),
        _srow("cscan", "seg-s", 1, 9, 1_000_000, 4, 400)], patterns=pats, mode="auto")
    return [jit, pcr]


def test_callout_split_and_share_b148rep():
    with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False) as f:
        f.write("# callout_calib: synthetic\ntestee\tmember\tns_per_fire\n"
                "libpcre2_jit\tco-luhn\t50.0\npcrec_auto\tco-luhn\t20.0\n")
        calib = f.name
    try:
        sd, err = _build(_callout_population(), callee_calib=calib)
        _check(err is None, err)
        j = report_stream.callout_split(sd, ("libpcre2_jit", "co-luhn", "co-luhn-1m", "large-subject-throughput"))
        _check(j["wrapper"] == 300_000 and j["callee"] == 700_000, "pass-twin / real-pass: %r" % j)
        _check(abs(j["per_fire"] - 70.0) < 1e-9, "per fire %r" % j["per_fire"])
        # share = 10,000 fires x 50 ns / 2,000,000 ns = 0.25 -> over the 20 % jit budget
        _check(abs(j["share"] - 0.25) < 1e-12 and j["flag"] == "over-budget>20%", "share/flag %r" % j)
        p = report_stream.callout_split(sd, ("pcrec_auto", "co-luhn", "co-luhn-1m", "large-subject-throughput"))
        _check(p["callee"] is None and "fires differ" in p["why"], "fires differ: %r" % p)
        # 12,000 x 20 / 1,500,000 = 0.16: under every bar, no flag
        _check(abs(p["share"] - 0.16) < 1e-12 and p["flag"] == "", "pcrec share %r" % p)
        md = report_stream.render_stream_markdown(sd)
        _check("25.0 % **over-budget>20%**" in md and "16.0 %" in md, "rendered shares:\n" + md)
        sd0, _ = _build(_callout_population())
        _check(report_stream.callout_split(sd0, ("libpcre2_jit", "co-luhn", "co-luhn-1m",
                                                 "large-subject-throughput"))["share"] is None,
               "CONTROL: no calibration, no share")
    finally:
        os.unlink(calib)


def test_depth_of_failure_table_b148rep():
    pats = [{"pattern_id": "cscan", "tags": []}]

    def rung(subj, outcome, limit=""):
        r = _srow("cscan", subj, 1, 1, 1000, 1, 100, regime="large-subject-throughput")
        r["match_outcome"] = outcome
        if outcome != "matched-as-expected":
            r.pop("timing")
            r["diagnostic"] = ("the engine gave up rather than answering: giveup:" + limit
                               if outcome == "gave-up" else "answer differs")
        return r
    a = _rec("jit", "libpcre2", [rung("nest-brace-128", "matched-as-expected"),
                                 rung("nest-brace-1k", "gave-up", "-46:JIT stack limit reached"),
                                 rung("nest-brace-100k", "gave-up", "-46:JIT stack limit reached")],
             patterns=pats)
    b = _rec("pcrec", "pcrec", [rung("nest-brace-128", "matched-as-expected"),
                                rung("nest-brace-1k", "matched-as-expected"),
                                rung("nest-brace-100k", "did-not-match-as-expected")], patterns=pats)
    # a stream record anchors the grain (the view selects call-stream records)
    a.rows.append(_srow("cscan", "seg-s", 1, 9, 1000, 4, 400))
    sd, err = _build([a, b])
    _check(err is None, err)
    d = sd.depth
    _check(d[("cscan", "nest-brace-128")] == {"jit": "match", "pcrec": "match"}, "128: %r" % d)
    _check(d[("cscan", "nest-brace-1k")]["jit"] == "-46:JIT" or d[("cscan", "nest-brace-1k")]["jit"].startswith("-46:"),
           "limit named: %r" % d[("cscan", "nest-brace-1k")])
    _check(d[("cscan", "nest-brace-100k")]["pcrec"] == "WRONG (excluded)", "wrong answer named")
    md = report_stream.render_stream_markdown(sd)
    order = [md.index("`nest-brace-%s`" % k) for k in ("128", "1k", "100k")]
    _check(order == sorted(order), "rungs sorted by depth, not by name")
    # CONTROL: a stream rung that every testee matches is not a depth row
    _check(("cscan", "seg-s") not in d, "all-match stream rung is not a depth row")


def test_gave_up_stream_cell_names_the_limit_b148rep():
    rec = _rec("jit", "libpcre2", [
        _srow("cscan", "s-deep", t, t, 0, 1, 4096, outcome="gave-up", gave_up=1,
              first_limit="PCRE2_ERROR_HEAPLIMIT") for t in (1, 2, 3)])
    sd, err = _build([rec])
    _check(err is None, err)
    c = sd.cells[("jit", "s-deep", "cscan")]
    _check(c.state == "gave-up" and c.first_limit == "PCRE2_ERROR_HEAPLIMIT" and not c.ranked, "cell %r" % c)
    md = report_stream.render_stream_markdown(sd)
    _check("**gave-up** (PCRE2_ERROR_HEAPLIMIT)" in md, md)
    tsv = report_stream.render_stream_tsv(sd)
    _check("\tgave-up\t" in tsv and "PCRE2_ERROR_HEAPLIMIT" in tsv and tsv.startswith("# reporter:"), "tsv")


def test_status_and_tier_gates_and_refusals_b148rep():
    pop = _vars_population()
    # a non-measured / pinned-gate record is NOT ranked unless asked
    pop[1].setup["status"] = "inconclusive-load"
    sd, err = _build(pop)
    _check(err is None and ("re2_assist", "status inconclusive-load") in sd.not_ranked
           and ("re2_assist", "tenant-d64", "va-tenant") not in sd.cells, "unmeasured not ranked")
    args = T._args(grain="stream", include_scratch=True, include_unmeasured=True, store="/x/store")
    sd2, _ = report_stream.build_stream_report(pop, args)
    _check(("re2_assist", "tenant-d64", "va-tenant") in sd2.cells, "--include-unmeasured ranks it")
    sd3, _ = _build(_vars_population(), include_scratch=False)
    _check(sd3.not_ranked and not sd3.cells, "scratch tier not ranked by default")
    # a selection with no call-stream record is refused BY NAME
    plain = T._mini_setup("t", sb_id="email", sb_version="0.1")
    plain["subbench"]["regimes"] = ["short-subject-search"]
    sd4, err = _build([T._mk_loaded("/x/p.jsonl", plain, [])])
    _check(sd4 is None and "`call-stream`" in err and "--grain stream" in err, "refusal: %s" % err)
    # two hosts: refused (one host per report)
    two = [_vars_population()[0], _vars_population()[1]]
    two[1].setup["environment"]["machine_id"] = "m2"
    sd5, err = _build(two)
    _check(sd5 is None and "span 2 machines" in err, "two hosts: %s" % err)


def test_set_and_subject_grains_refuse_call_stream_by_name_b148rep():
    """§7.5: set grain REFUSES a `call-stream` input BY NAME -- both the set
    and the subject grain (one code path), pointing at `--grain stream`.
    CONTROL: the stream view itself accepts the same records."""
    only = [_rec("pcrec_auto", "pcrec", [_srow("cscan", "seg-s", 1, 1, 1000, 4, 400)])]
    only[0].setup["subbench"]["regimes"] = ["call-stream"]
    for grain in ("set", "subject"):
        rd, err = report.build_report(only, T._args(store="/x/store", grain=grain,
                                                    include_scratch=True))
        _check(rd is None and "`call-stream`" in err and "--grain stream" in err,
               "%s grain refusal: %s" % (grain, err))
    sd, err = _build(only)
    _check(err is None and sd.cells, "CONTROL: the stream view reads it")


def test_cli_stream_grain_flags_b148rep():
    """CLI: --grain stream takes no matrix format; --callee-calib needs it."""
    import io
    import contextlib
    for argv, needle in ((["--grain", "stream", "--format", "matrix"], "--grain set"),
                         (["--callee-calib", "/x"], "requires --grain stream")):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            rc = report.main(["--store", "/nonexistent"] + argv)
        _check(rc == 2 and needle in err.getvalue(), "%s -> %r" % (argv, err.getvalue()))


def test_skip_tables_exporters_by_name_b148rep():
    """§7.5 P12, the three reader controls: the viewer exporter, the trend
    digest and the front page each skip a `call-stream` record's rows BY
    NAME (the declared skip table `reduce.SET_GRAIN_SKIP_REGIMES`), run for
    real over schema/examples' v1.11 call-stream record. CONTROL: the same
    functions yield cells for an ordinary search record."""
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import trend
    import viewer_export as V
    import frontpage as F
    ex = glob.glob(os.path.join(ROOT, "schema", "examples", "unusual-example*.jsonl"))
    _check(len(ex) == 1, "the v1.11 example record exists")
    ex = ex[0]
    fixture = sorted(glob.glob(os.path.join(ROOT, "pcrecbench", "tests", "fixtures",
                                            "store", "records", "*", "*", "*.jsonl")))[0]
    # 1. trend digest
    _check(trend.build_digest(ex)["cells"] == {}, "trend: no call-stream cell")
    _check(trend.build_digest(fixture)["cells"], "CONTROL trend: a search record has cells")
    # 2. viewer exporter
    rv = V._get_record_validator()
    rows, _meta, _forms = V.export_rows_for_record(ex, rv)
    _check(not [r for r in rows if r["regime"] == "call-stream"],
           "viewer: no call-stream row exported")
    crows, _m, _f = V.export_rows_for_record(fixture, rv)
    _check([r for r in crows if r["median_ns"] is not None], "CONTROL viewer: a search record exports cells")
    # 3. front page
    s = F.Summary(os.path.dirname(ex), {"path": os.path.basename(ex)})
    _check(s.cells == {} and "call-stream" not in s.regimes, "front page: no call-stream case")
    f = F.Summary(os.path.dirname(fixture), {"path": os.path.basename(fixture)})
    _check(f.cells, "CONTROL front page: a search record has cases")


TESTS = [
    test_stream_cell_reduction_by_hand_b148rep,
    test_break_even_by_hand_b148rep,
    test_callout_split_and_share_b148rep,
    test_depth_of_failure_table_b148rep,
    test_gave_up_stream_cell_names_the_limit_b148rep,
    test_status_and_tier_gates_and_refusals_b148rep,
    test_set_and_subject_grains_refuse_call_stream_by_name_b148rep,
    test_cli_stream_grain_flags_b148rep,
    test_skip_tables_exporters_by_name_b148rep,
]


def main():
    os.environ.setdefault("LC_ALL", "C")
    passed = failed = 0
    for t in TESTS:
        try:
            t()
        except Exception:  # noqa: BLE001
            failed += 1
            print(f"FAIL {t.__name__}")
            traceback.print_exc()
        else:
            passed += 1
            print(f"ok   {t.__name__}")
    print(f"\n{passed} passed, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
