"""check_calls.py -- `make check-harness`'s slice for the CALL-STREAM regime
and the `deep` limits arms ([B148] L4, docs/design/unusual_set_v1.md 6.2-6.5,
7.1-7.3).

Called from tools/selfcheck.py's main() as `check_calls.run(ok, bad)` (the
two reporting callbacks selfcheck owns), shaped after tools/check_subst.py:
the slice's checks live beside nothing else. A SMOKE: `--iters 1`, one
trial, scratch records under build/, nothing printed is a number.

What it checks, each with its control:
  1. `--mode calls` through the REAL adapter path (prepare / compile /
     measure) on a SYNTHETIC stream -- a pattern with a group 1 every engine
     on the roster compiles, call offsets inside words, before the first
     match and past the last -- for every calls-capable testee: the token
     file's sha256 equals the libpcre2 oracle's (`search` at each offset;
     group 0 only for vectorscan, which has no groups). `--anchor-explicit`
     on the engines that have an anchored call equals the oracle under
     PCRE2_ANCHORED. CONTROL: the same rows against a one-token-wrong
     expectation are `wrong-span-or-captures` (harness.stream_outcome).
  2. refusals BY NAME: a vars binding row (calls_io.h and the rust reader),
     `--anchor-explicit` outside calls mode, vectorscan calls without
     `--som`, rust `--anchor-explicit`; a `call-stream` regime NAMED for a
     testee without `--mode calls`; an `unusual_only` testee on a set that is
     not an unusual set. CONTROL: `CALL_STREAM_PENDING` is False and
     vectorscan-block-som says it supports the mode while -nosom does not.
  3. bench/unusual's REAL streams through `run_cell` (scratch store,
     validator-accepted): cscan x {seg-s, seg-l} on pcre2-jit and
     cscan-onig on onig-default-deep and pcrec-vm-deep, every row
     `matched-as-expected` against expectations_stream.tsv; pcrec-auto on
     the same stream GIVES UP and names `PCREC_ERR_FRAMES` (X49) -- the
     deep arm's 1 GiB buffer is what completes it (the control).
  4. every engine's limits READ BACK by value, both arms (6.2): libpcre2's
     config defaults and the deep context's values, Oniguruma's six getters
     before and after the setters, pcrec's step/work budgets and storage.
  5. the 6.4 high-water pass: pcrec's canary and libpcre2's counting
     allocator on two nesting depths grow with depth (the known-depth
     control) and the floor pattern on a flat subject holds far less (the
     no-recursion control); every method's row carries `deep_mem_method` by
     name. (The counting allocator once missed the frames entirely -- 136 B
     on a 2,048-deep nest -- because the frames are the MATCH DATA's
     allocation; this control is what found it.)
"""
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import oracle_pcre2 as oracle  # noqa: E402

WORK = os.path.join(ROOT, "build", "check-calls")
SYN_PATTERN = rb"([a-z]+)=([0-9]+)"
SYN_SUBJECT = b"aa=1 bb=22 c=333 nope zz=4444 q=5 tail"
#: call offsets: a match start, mid-word, between matches, inside a non-match
#: word, the last match, past every match, the very end
SYN_OFFSETS = [0, 1, 5, 11, 18, 22, 30, 34, len(SYN_SUBJECT)]
CALLS_TESTEES = ["pcre2-interp", "pcre2-jit", "pcre2-interp-deep",
                 "pcre2-jit-deep", "pcrec-auto", "pcrec-vm", "pcrec-vm-in",
                 "pcrec-vm-deep", "onig-default", "onig-default-deep",
                 "re2-default", "rust-default", "vectorscan-block-som"]
ANCHORED_TESTEES = ["pcre2-jit", "pcrec-vm", "onig-default", "re2-default"]
PCRE2_ANCHORED = 0x80000000


def _sha(tokens):
    return hashlib.sha256(b"".join(t.encode() + b"\n" for t in tokens)).hexdigest()


def _oracle_tokens(g1, anchored):
    rx = oracle.compile(SYN_PATTERN)
    toks = []
    for off in SYN_OFFSETS:
        if anchored:
            m = _anchored_search(rx, off)
        else:
            m = rx.search(SYN_SUBJECT, off)
        if m is None:
            toks.append("n")
            continue
        (s, e), groups = m
        if g1:
            gs, ge = groups[0] if groups and groups[0] else (-1, -1)
            toks.append("m:%d,%d;%d,%d" % (s, e, gs, ge))
        else:
            toks.append("m:%d,%d" % (s, e))
    return toks


def _anchored_search(rx, off):
    """PCRE2_ANCHORED at `off` through the oracle's raw call."""
    return oracle._search_raw(rx, SYN_SUBJECT, off, PCRE2_ANCHORED)


def _write_stream(d, name, offsets, binding="-"):
    from pcrecbench import subbench as _sbm
    subj = os.path.join(d, name + ".bin")
    with open(subj, "wb") as f:
        f.write(SYN_SUBJECT)
    calls = os.path.join(d, name + ".tsv")
    with open(calls, "w", encoding="utf-8", newline="\n") as f:
        f.write("call_id\toffset\tlength\tsegment_bytes\tbinding_id\n")
        for i, off in enumerate(offsets):
            ln = min(5, len(SYN_SUBJECT) - off)
            f.write("%d\t%d\t%d\t%d\t%s\n" % (i, off, ln, ln, binding))
    s = _sbm.Subject(name, len(SYN_SUBJECT), hashlib.sha256(SYN_SUBJECT).hexdigest(),
                     "synthetic stream", "no", subj, "stream")
    s.calls_path = calls
    s.calls = len(offsets)
    s.segment_bytes = sum(min(5, len(SYN_SUBJECT) - o) for o in offsets)
    return s


def _compile(ad, testee, work, pattern=SYN_PATTERN, pid="syn"):
    ad.prepare(testee, work)
    cp = ad.compile(testee, pid, pattern, {}, 1, work)
    res = cp.forms["plain"]
    if res.outcome != "compiled":
        raise RuntimeError("%s did not compile %r: %s" % (testee, pattern, res.diagnostic))
    return res.handle


def _tokens_of(row):
    return (row.stream or {}).get("results_sha256")


def run(ok, bad):
    print("-- [B148] L4 the call-stream regime and the deep limits arms --")
    from pcrecbench import adapters as _ad, harness as _h
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK)
    d = tempfile.mkdtemp(prefix="syn-", dir=WORK)
    stream = _write_stream(d, "syn", SYN_OFFSETS)

    # 1. the synthetic stream on every calls-capable testee ---------------
    want_g1 = _sha(_oracle_tokens(True, False))
    want_g0 = _sha(_oracle_tokens(False, False))
    want_anch = _sha(_oracle_tokens(True, True))
    rows_seen = None
    for t in CALLS_TESTEES:
        try:
            ad, _cfg = _ad.resolve(t)
            work = os.path.join(WORK, t)
            h = _compile(ad, t, work)
            by_trial, _i, _n = ad.measure(h, "call-stream", [stream], 1, 1, timeout=300)
            r = by_trial[0][0]
            want = want_g0 if t.startswith("vectorscan") else want_g1
            if _tokens_of(r) == want and r.stream["calls"] == len(SYN_OFFSETS):
                ok("calls: %s's synthetic stream = the oracle's tokens" % t,
                   "%d calls, %d matched" % (r.stream["calls"], r.stream["matched"]))
                rows_seen = rows_seen or (r, h, ad)
            else:
                bad("calls: %s's synthetic stream" % t,
                    "%s vs %s (%r)" % (_tokens_of(r), want, r.stream))
        except Exception as e:                      # noqa: BLE001
            bad("calls: %s on the synthetic stream" % t, str(e)[:400])
    for t in ANCHORED_TESTEES:
        try:
            ad, _cfg = _ad.resolve(t)
            h = dict(_compile(ad, t, os.path.join(WORK, t)), stream_anchor="explicit")
            by_trial, _i, _n = ad.measure(h, "call-stream", [stream], 1, 1, timeout=300)
            r = by_trial[0][0]
            if _tokens_of(r) == want_anch:
                ok("calls: %s --anchor-explicit = the oracle under PCRE2_ANCHORED" % t,
                   "%d matched of %d" % (r.stream["matched"], r.stream["calls"]))
            else:
                bad("calls: %s --anchor-explicit" % t, repr(r.stream))
        except Exception as e:                      # noqa: BLE001
            bad("calls: %s --anchor-explicit" % t, str(e)[:400])
    if rows_seen:
        r, h, ad = rows_seen

        class _Sexp:
            calls, matched, nomatch, refused = (r.stream["calls"], r.stream["matched"],
                                                r.stream["nomatch"], 0)
            results_sha256 = "0" * 64
        out = _h.stream_outcome(r, _Sexp, stream, h, ad)
        if out[0] == "wrong-span-or-captures":
            ok("calls: CONTROL -- the same row against a wrong hash is wrong-span-or-captures")
        else:
            bad("calls: control outcome", repr(out[:3]))

    # 2. refusals by name ------------------------------------------------
    vars_stream = _write_stream(d, "vars", [0, 5], binding="b1")
    for t, needle in (("pcre2-jit", "lane L7"), ("onig-default", "lane L7"),
                      ("rust-default", "lane L7")):
        try:
            ad, _cfg = _ad.resolve(t)
            h = _compile(ad, t, os.path.join(WORK, t))
            by_trial, _i, notes = ad.measure(h, "call-stream", [vars_stream], 1, 1, timeout=120)
            text = " ".join(notes) + " ".join(str(x) for x in (by_trial[0] if by_trial else []))
            if not (by_trial and by_trial[0] and by_trial[0][0].stream):
                ok("refuse: %s refuses a vars binding row by name" % t, "no stream answered")
            else:
                bad("refuse: %s answered a vars stream" % t, text[:200])
        except Exception as e:                      # noqa: BLE001
            if needle in str(e) or "binding" in str(e):
                ok("refuse: %s refuses a vars binding row by name" % t)
            else:
                bad("refuse: %s vars row" % t, str(e)[:300])
    vs, _ = _ad.resolve("vectorscan-block-som")
    if vs.supports_calls("vectorscan-block-som") and \
            not vs.supports_calls("vectorscan-block-nosom"):
        ok("refuse: vectorscan supports_calls on -som only")
    else:
        bad("refuse: vectorscan supports_calls")
    if _h.CALL_STREAM_PENDING is False:
        ok("refuse: harness.CALL_STREAM_PENDING is False (L4 landed)")
    else:
        bad("refuse: CALL_STREAM_PENDING still set")
    for args, needle, what in (
            (dict(subbench_name="unusual", testee_id="tre-default",
                  regimes=["call-stream"]), "does not speak `--mode calls`",
             "a named call-stream regime for a testee without --mode calls"),
            (dict(subbench_name="email", testee_id="pcre2-jit-deep",
                  regimes=["search_short"]), "unusual-set-only",
             "an unusual_only testee on a set that is not an unusual set")):
        try:
            _h.run_cell(trials=1, iters=1, force_unquiet=True, tier="scratch",
                        store_root=os.path.join(WORK, "refusal-store"), **args)
            bad("refuse: %s was measured" % what)
        except _h.HarnessError as e:
            if needle in str(e):
                ok("refuse: %s is refused BY NAME" % what)
            else:
                bad("refuse: %s" % what, str(e)[:300])
    _driver_refusals(ok, bad)

    # 3. the real streams through run_cell -----------------------------------
    store_root = os.path.join(WORK, "scratch-store")
    recs = {}
    # one match row per stream subject: counted from the manifest, never a literal
    # (b148f2 added the two sqlite streams to F1's two)
    with open(os.path.join(ROOT, "bench", "unusual", "manifest_streams.tsv")) as f:
        n_streams = sum(1 for l in f) - 1
    for t, pat in (("pcre2-jit", "cscan"), ("onig-default-deep", "cscan-onig"),
                   ("pcrec-vm-deep", "cscan-onig"), ("pcrec-auto", "cscan-onig")):
        try:
            res = _h.run_cell("unusual", t, regimes=["call-stream"], trials=1, iters=1,
                              force_unquiet=True, tier="scratch", store_root=store_root,
                              patterns=[pat, "floor"], synthetic=True,
                              workdir=os.path.join(WORK, "cell-" + t), mem=True)
            recs[t] = res
            mrows = [r for r in res.rows if r["kind"] == "match" and r["pattern_id"] == pat]
            outs = sorted({r["match_outcome"] for r in mrows})
            if t == "pcrec-auto":
                lim = {(r.get("stream") or {}).get("first_limit") for r in mrows}
                if outs == ["gave-up"] and lim == {"PCREC_ERR_FRAMES"} and all(
                        "PCREC_ERR_FRAMES" in (r.get("diagnostic") or "") for r in mrows):
                    ok("streams: pcrec-auto gives up on cscan-onig and NAMES PCREC_ERR_FRAMES",
                       "the default arm's stack-resident frames; X49")
                else:
                    bad("streams: pcrec-auto give-up naming", repr((outs, lim)))
            elif outs == ["matched-as-expected"] and len(mrows) == n_streams:
                ok("streams: %s x %s x %d streams matched-as-expected" % (t, pat, n_streams),
                   "validator-accepted scratch record")
            else:
                bad("streams: %s x %s" % (t, pat), repr(outs))
        except Exception as e:                      # noqa: BLE001
            bad("streams: %s x %s" % (t, pat), str(e)[:400])

    # 4. limits read back by value --------------------------------------
    def crow(t, pat):
        res = recs.get(t)
        if not res:
            return {}
        for r in res.rows:
            if r["kind"] == "compile" and r["pattern_id"] == pat:
                return r.get("engine_metadata") or {}
        return {}
    em = crow("onig-default-deep", "cscan-onig")
    if em.get("lim_match_stack_elems") == 33554432 and em.get("lim_subexp_call_nest") == 1000000 \
            and em.get("lim_retry_in_match") == 0 and em.get("lim_stack_elem_bytes") == 32:
        ok("limits: onig-default-deep reads back stack 33,554,432 x 32 B, nest 1,000,000, retry 0")
    else:
        bad("limits: onig-default-deep", repr(em))
    em = crow("pcrec-vm-deep", "cscan-onig")
    if em.get("step_budget") == 9223372036854775807 and em.get("work_budget") == 9223372036854775807 \
            and 0 < em.get("lim_storage_bytes", 0) <= 1 << 30:
        ok("limits: pcrec-vm-deep step/work budgets INT64_MAX, storage <= 1 GiB",
           "%d B" % em["lim_storage_bytes"])
    else:
        bad("limits: pcrec-vm-deep", repr(em))
    em = crow("pcrec-auto", "cscan-onig")
    if em.get("step_budget") == 500000000 and em.get("lim_storage_bytes", 0) > 0:
        ok("limits: CONTROL pcrec-auto reads its default budgets and stamped storage",
           "%d B" % em["lim_storage_bytes"])
    else:
        bad("limits: pcrec-auto default arm", repr(em))
    em = crow("pcre2-jit", "cscan")
    if em.get("lim_match") == 10000000 and em.get("lim_jit_stack_bytes") == 32768 \
            and em.get("lim_config_heap_kib") == 20000000:
        ok("limits: CONTROL pcre2-jit default arm reads match 10,000,000, JIT stack 32 KiB")
    else:
        bad("limits: pcre2-jit default arm", repr(em))
    _driver_limits(ok, bad)

    # 5. the high-water pass ----------------------------------------------
    _mem_controls(ok, bad, _ad, _h)


def _drv(ad, t, work):
    ad.prepare(t, work)
    return ad.prepare_driver(work)


def _driver_refusals(ok, bad):
    from pcrecbench import adapters as _ad
    work = os.path.join(WORK, "drv")
    pat = os.path.join(WORK, "syn.rx")
    with open(pat, "wb") as f:
        f.write(SYN_PATTERN)
    cases = []
    ad, _ = _ad.resolve("pcre2-jit")
    cases.append(("pcre2", [_drv(ad, "pcre2-jit", work), "--pattern", pat, "--mode", "search",
                            "--anchor-explicit", "--list", "/dev/null"], "--mode calls flag"))
    ad, _ = _ad.resolve("onig-default")
    cases.append(("onig", [_drv(ad, "onig-default", work), "--pattern", pat, "--mode", "search",
                           "--anchor-explicit", "--list", "/dev/null"], "--mode calls flag"))
    ad, _ = _ad.resolve("vectorscan-block-som")
    cases.append(("vectorscan", [_drv(ad, "vectorscan-block-som", work), "--pattern", pat,
                                 "--mode", "calls", "--list", "/dev/null"], "needs --som"))
    ad, _ = _ad.resolve("rust-default")
    cases.append(("rust", [_drv(ad, "rust-default", work), "--pattern", pat, "--mode", "calls",
                           "--anchor-explicit", "--list", "/dev/null"], "anchored-at-offset"))
    for name, argv, needle in cases:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=60)
        if p.returncode != 0 and needle in (p.stdout + p.stderr):
            ok("refuse: the %s driver refuses by name: %s" % (name, needle))
        else:
            bad("refuse: %s driver" % name, (p.stdout + p.stderr)[-300:])


def _info(argv):
    p = subprocess.run(argv, capture_output=True, text=True, timeout=60)
    out = {}
    for line in p.stdout.splitlines():
        c = line.split("\t")
        if c[0] == "info" and len(c) >= 3:
            out[c[1]] = c[2]
    return out


def _driver_limits(ok, bad):
    from pcrecbench import adapters as _ad
    work = os.path.join(WORK, "drv")
    pat = os.path.join(WORK, "syn.rx")
    ad, _ = _ad.resolve("pcre2-interp")
    drv = _drv(ad, "pcre2-interp", work)
    dflt = _info([drv, "--pattern", pat, "--limits"])
    deep = _info([drv, "--pattern", pat, "--limits", "--deep"])
    jdeep = _info([drv, "--pattern", pat, "--limits", "--deep", "--jit"])
    if (dflt.get("lim_match") == "10000000" and dflt.get("lim_heap_kib") == "20000000"
            and deep.get("lim_match") == "4294967295" and deep.get("lim_depth") == "4294967295"
            and deep.get("lim_heap_kib") == "1048576"
            and jdeep.get("lim_jit_stack_bytes") == str(1 << 30)):
        ok("limits: libpcre2 default 10,000,000 / 20,000,000 KiB; deep UINT32_MAX / "
           "1,048,576 KiB, JIT stack 1 GiB", "the deep arm is TIGHTER on heap (6.1)")
    else:
        bad("limits: libpcre2 read-back", repr((dflt, deep, jdeep)))
    ad, _ = _ad.resolve("onig-default")
    drv = _drv(ad, "onig-default", work)
    d0 = _info([drv, "--pattern", pat, "--limits"])
    if d0.get("lim_match_stack_elems") == "0" and d0.get("lim_retry_in_match") == "10000000" \
            and d0.get("lim_subexp_call_nest") == "20" and d0.get("lim_parse_depth") == "4096":
        ok("limits: CONTROL Oniguruma defaults read back: stack 0 (unlimited), retry "
           "10,000,000, nest 20, parse depth 4,096")
    else:
        bad("limits: Oniguruma defaults", repr(d0))


def _mem_controls(ok, bad, _ad, _h):
    from pcrecbench import subbench as _sbm
    sb = _sbm.find("unusual")
    for t, pid, method in (("pcrec-vm-deep", "cscan-onig", "canary"),
                           ("pcre2-interp-deep", "cscan", "counting-alloc")):
        try:
            ad, _ = _ad.resolve(t)
            work = os.path.join(WORK, "mem-grow-" + t)
            h = _compile(ad, t, work, pattern=sb.pattern_bytes(pid), pid=pid)
            subs = [sb.subject("nest-brace-512"), sb.subject("nest-brace-2k")]
            m = _h.mem_pass(ad, h, "throughput", subs, 300, 60)
            a, b = m["nest-brace-512"]["deep_mem_bytes"], m["nest-brace-2k"]["deep_mem_bytes"]
            hf = _compile(ad, t, work, pattern=sb.pattern_bytes("floor"), pid="floor")
            f = _h.mem_pass(ad, hf, "throughput", [sb.subject("literal-100k")], 300, 60)
            fl = f["literal-100k"]["deep_mem_bytes"]
            if b > 2 * a > 0 and fl < a and m["nest-brace-2k"]["deep_mem_method"] == method:
                ok("mem: %s %s grows with nesting (512 -> 2k braces), the floor holds less"
                   % (t, method), "%d -> %d B; floor %d B" % (a, b, fl))
            else:
                bad("mem: %s known-depth controls" % t, repr((a, b, fl)))
        except Exception as e:                      # noqa: BLE001
            bad("mem: %s known-depth controls" % t, str(e)[:400])
    for t, method in (("pcre2-jit-deep", "mincore"),
                      ("onig-default-deep", "rss-delta")):
        try:
            ad, _ = _ad.resolve(t)
            pat = sb.pattern_bytes("cscan-onig" if t.startswith("onig") else "cscan")
            h = _compile(ad, t, os.path.join(WORK, "mem-" + t), pattern=pat, pid="m")
            m = _h.mem_pass(ad, h, "throughput", [sb.subject("nest-brace-2k")], 300, 60)
            row = m.get("nest-brace-2k") or {}
            if row.get("deep_mem_method") == method and row.get("deep_maxrss_kb", 0) > 0:
                ok("mem: %s reports method %s by name" % (t, method),
                   "%d B, maxrss %d KiB" % (row["deep_mem_bytes"], row["deep_maxrss_kb"]))
            else:
                bad("mem: %s" % t, repr(row))
        except Exception as e:                      # noqa: BLE001
            bad("mem: %s" % t, str(e)[:400])


if __name__ == "__main__":
    fails = []
    run(lambda *a: print("ok  ", *a), lambda *a: (fails.append(a), print("FAIL", *a)))
    sys.exit(1 if fails else 0)
