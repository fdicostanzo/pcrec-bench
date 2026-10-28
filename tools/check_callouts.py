"""check_callouts.py -- `make check-harness`'s slice for the unusual set's
CALLOUT ARMS ([B148] L5, docs/design/unusual_set_v1.md 3.2, r9 C5/C9).

Called from tools/selfcheck.py's main() as `check_callouts.run(ok, bad)`,
shaped after tools/check_calls.py. A SMOKE: one trial, iters 1, scratch
records under build/, nothing printed is a number.

What it checks, each with its control:
  1. callees.o is built ONCE with the FIXED flags (two `ensure()` calls, one
     path, one sha256, the `.cmd` beside it); the timed object and every
     timed callout binary carry NO fire log (`UB_FIRE_LOG` absent from the
     bytes) while the counting object and the counting binaries do -- the
     counter is never in a timed build.
  2. THE RETURN-CODE MAPPING with the FIRST-CANDIDATE-FAILS control, on every
     native config (pcre2-interp, pcre2-jit, pcrec-auto, pcrec-vm,
     onig-default): `co-luhn` over a subject whose FIRST card fails Luhn and
     whose second passes answers the SECOND card's span under the real
     callee (FAIL = backtrack to the next candidate on every engine) and the
     FIRST's under the stub (CONTINUE). NEGATIVE CONTROL on the oracle: a
     libpcre2 callout returning the callee's own -1 unmapped ABANDONS the
     match (no match at all), +1 moves to the second card -- the mapping is
     load-bearing. pcrec's consume callee: an overlong netstring length FAILS
     its candidate and the next netstring matches (the host reference's
     answer).
  3. THE pass == twin GATE (and pass-nofn == twin on libpcre2): every short
     subject of the set, raw driver answers (span + captures) of each
     member's -pass arm equal its -twin's on every native config; the -real
     arm DIFFERS from the twin on at least one subject (the control: the
     callee is reached).
  4. the COUNTING build answers what the timed build answers on the real
     arms (same subjects), and the fire pass yields `callout_fires` > 0 on a
     subject with a candidate; the cross-engine fire digests are printed.
  5. the ONIGURUMA WITNESSES (testees/onig/callout_witness.c): the `(?{N})`
     contents spelling under the global progress callout, `(*name)`
     registration before onig_new, `[\\x80-\\xff]` under ASCII, `\\G`.
  6. pcrec's binding SHAPE: numbered and named sites bound to the wrapper
     with their slots, an unbound site refused BY NAME, and a callout pattern
     compiled WITHOUT the callout option keeps [B147]'s `separate-tu-pass`.
  7. `run_cell` (scratch, validator-accepted) over the luhn family on
     pcre2-jit, pcrec-vm and onig-default (+ pcre2-interp's nofn arm): every
     match row matched-as-expected, the real arm's rows carry
     `callout_fires`, the compile rows `callout_arm` / `callees_sha256`.
"""
import hashlib
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "bench", "unusual"))

WORK = os.path.join(ROOT, "build", "check-callouts")
NATIVE = ["pcre2-interp", "pcre2-jit", "pcrec-auto", "pcrec-vm", "onig-default"]
FF_SUBJECT = b"card 4111111111111112 then 4111111111111111 end"
FF_FIRST, FF_SECOND = (5, 21), (27, 43)
NS_SUBJECT = b"9:ab,2:cd,"


def _subject(d, sid, data):
    from pcrecbench import subbench as _sbm
    path = os.path.join(d, sid)
    with open(path, "wb") as f:
        f.write(data)
    return _sbm.Subject(sid, len(data), hashlib.sha256(data).hexdigest(),
                        "check_callouts", "no", path, "short")


def _compile(ad, testee, pid, text, co, work):
    ad.prepare(testee, work)
    cp = ad.compile(testee, pid, text, {"callouts": co}, 1, work)
    res = cp.forms["plain"]
    if res.outcome != "compiled":
        raise RuntimeError("%s did not compile %s: %s" % (testee, pid, res.diagnostic))
    return res


def _answers(ad, handle, subjects):
    by_trial, _i, _n = ad.measure(handle, "search_short", subjects, 1, 1, timeout=300)
    return {r.subject_id: (r.answer, r.start, r.end, r.caps) for r in by_trial[0]}


def _co(sb, pid, arm=None):
    from pcrecbench import callees
    p = [x for x in sb.patterns if x.name == pid][0]
    co = callees.options_for(sb, p)
    if arm:
        co = dict(co, arm=arm)
    return co


def _strings_has(path, needle):
    with open(path, "rb") as f:
        return needle in f.read()


def run(ok, bad):
    print("-- [B148] L5 the callout arms --")
    from pcrecbench import adapters as _ad, callees, harness as _h, subbench as _sbm
    import unusual_lib as U
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK)
    sb = _sbm.load(os.path.join(ROOT, "bench", "unusual"))

    # 1. built once, fixed flags, no counter in a timed build ----------------
    try:
        a1, a2 = callees.ensure(), callees.ensure()
        c1 = callees.ensure(count=True)
        with open(a1[0] + ".cmd") as f:
            cmd = f.read().split()
        if (a1 == a2 and cmd[1:1 + len(callees.FLAGS)] == callees.FLAGS
                and a1[1] != c1[1]):
            ok("callees.o built once with the fixed flags", "sha %s, %s"
               % (a1[1][:12], " ".join(callees.FLAGS)))
        else:
            bad("callees.o built once", repr((a1, a2, cmd)))
        if (not _strings_has(a1[0], b"UB_FIRE_LOG")
                and _strings_has(c1[0], b"UB_FIRE_LOG")):
            ok("the timed callees.o has no fire log; the counting object has",
               "UB_FIRE_LOG in the bytes")
        else:
            bad("timed vs counting callee object", "UB_FIRE_LOG placement")
    except Exception as e:                          # noqa: BLE001
        bad("callees.o build", str(e)[:400])

    # 2. the return-code mapping, first candidate fails ----------------------
    d = os.path.join(WORK, "subj")
    os.makedirs(d)
    ff = _subject(d, "ff", FF_SUBJECT)
    luhn = sb.pattern_bytes("co-luhn")
    handles = {}
    for t in NATIVE:
        try:
            ad, _cfg = _ad.resolve(t)
            w = os.path.join(WORK, t)
            real = _compile(ad, t, "co-luhn", luhn, _co(sb, "co-luhn"), w)
            stub = _compile(ad, t, "co-luhn-pass", luhn, _co(sb, "co-luhn-pass"), w)
            handles[t] = (ad, real)
            ra = _answers(ad, real.handle, [ff])["ff"]
            sa = _answers(ad, stub.handle, [ff])["ff"]
            if ra[:3] == ("match",) + FF_SECOND and sa[:3] == ("match",) + FF_FIRST:
                ok("mapping: %s -- a FAILing first candidate moves to the second" % t,
                   "real %s, stub %s" % (ra[1:3], sa[1:3]))
            else:
                bad("mapping: %s first-candidate-fails" % t, repr((ra, sa)))
        except Exception as e:                      # noqa: BLE001
            bad("mapping: %s" % t, str(e)[:400])
    # pcrec's driver is the plain one (the callees live in the .so)
    timed_bins = [r.handle.get("lib") if t.startswith("pcrec") else r.handle.get("driver")
                  for t, (_a, r) in handles.items()]
    count_bins = [b for _t, (_a, r) in handles.items()
                  for b in (r.handle.get("count_driver"), r.handle.get("count_lib")) if b]
    if (timed_bins and count_bins
            and not any(_strings_has(b, b"UB_FIRE_LOG") for b in timed_bins)
            and all(_strings_has(b, b"UB_FIRE_LOG") for b in count_bins)):
        ok("no counter in any timed callout binary", "%d timed, %d counting"
           % (len(timed_bins), len(count_bins)))
    else:
        bad("no counter in any timed callout binary", repr((timed_bins, count_bins)))
    # the oracle's negative control: the callee's -1 passed through abandons
    try:
        m_raw = U.Rx(luhn, callout=lambda f: -1 if not U.luhn_ok(
            f.subject[f.caps[1][0]:f.caps[1][1]]) else 0).search(FF_SUBJECT)
        m_map = U.Rx(luhn, callout=lambda f: 1 if not U.luhn_ok(
            f.subject[f.caps[1][0]:f.caps[1][1]]) else 0).search(FF_SUBJECT)
        if m_raw is None and m_map and m_map[0] == FF_SECOND:
            ok("negative control: libpcre2 ABANDONS on an unmapped -1, backtracks on +1",
               "-1 -> no match; +1 -> %s" % (m_map[0],))
        else:
            bad("negative control (oracle)", repr((m_raw, m_map)))
    except Exception as e:                          # noqa: BLE001
        bad("negative control (oracle)", str(e)[:300])
    # pcrec's consume callee: an overlong length FAILs its candidate
    try:
        ns = _subject(d, "ns", NS_SUBJECT)
        want = U.host_first("netstr", NS_SUBJECT, 0)
        for t in ("pcrec-auto", "pcrec-vm"):
            ad, _cfg = _ad.resolve(t)
            r = _compile(ad, t, "co-netstr", sb.pattern_bytes("co-netstr"),
                         _co(sb, "co-netstr"), os.path.join(WORK, t))
            got = _answers(ad, r.handle, [ns])["ns"]
            if want and got[:3] == ("match",) + tuple(want):
                ok("mapping: %s consume -- an overlong length FAILs, the next "
                   "netstring matches" % t, "%s = the host reference" % (got[1:3],))
            else:
                bad("mapping: %s consume" % t, repr((got, want)))
    except Exception as e:                          # noqa: BLE001
        bad("mapping: pcrec consume", str(e)[:400])

    # 3. pass == twin (and nofn == twin) over every short subject ------------
    shorts = sb.subjects_for("search_short")
    fam = ["co-luhn", "co-isbn", "co-member"]
    for t in NATIVE:
        try:
            ad, _cfg = _ad.resolve(t)
            w = os.path.join(WORK, t)
            arms = ["", "-pass", "-twin"] + (["-nofn"] if t.startswith("pcre2") else [])
            diff_real = 0
            failed = []
            for m in fam:
                ans = {}
                for arm in arms:
                    pid = m + arm
                    r = _compile(ad, t, pid, sb.pattern_bytes(pid), _co(sb, pid), w)
                    ans[arm] = _answers(ad, r.handle, shorts)
                for arm in [a for a in arms if a in ("-pass", "-nofn")]:
                    if ans[arm] != ans["-twin"]:
                        failed.append(m + arm)
                diff_real += sum(1 for s in ans[""] if ans[""][s] != ans["-twin"].get(s))
            if not failed and diff_real > 0:
                ok("gate: %s pass%s == twin on %d short subjects x 3 members"
                   % (t, "/nofn" if t.startswith("pcre2") else "", len(shorts)),
                   "control: real != twin on %d subject(s)" % diff_real)
            else:
                bad("gate: %s pass == twin" % t, "differ: %s; real-vs-twin %d"
                    % (failed, diff_real))
        except Exception as e:                      # noqa: BLE001
            bad("gate: %s pass == twin" % t, str(e)[:400])

    # 4. the counting build answers as the timed one; fires --------------------
    digests = {}
    probe = [s for s in shorts if s.subject_id.startswith(("lu-", "first-fails"))][:12] or shorts[:12]
    for t, (ad, real) in handles.items():
        try:
            fh = ad.fire_handle(real.handle)
            timed = _answers(ad, real.handle, probe)
            counted = _answers(ad, fh, probe)
            fires = _h.fire_pass(ad, real.handle, "search_short", probe, 300,
                                 os.path.join(WORK, "fires", t))
            tot = sum(v["callout_fires"] for v in fires.values())
            digests[t] = tuple(sorted((k, v["callout_fires"], v["callout_views_sha256"])
                                      for k, v in fires.items()))
            if timed == counted and len(fires) == len(probe) and tot > 0:
                ok("count build: %s answers = the timed build's; fires recorded" % t,
                   "%d fires over %d subjects" % (tot, len(probe)))
            else:
                bad("count build: %s" % t, repr((timed == counted, len(fires), tot)))
        except Exception as e:                      # noqa: BLE001
            bad("count build: %s" % t, str(e)[:400])
    groups = {}
    for t, dg in digests.items():
        groups.setdefault(dg, []).append(t)
    print("   fire digests over %d subjects: %s" % (len(probe), " | ".join(
        "+".join(v) for v in groups.values())))

    # 5. the Onig witnesses -------------------------------------------------------
    try:
        exe = os.path.join(WORK, "onig_callout_witness")
        src = os.path.join(ROOT, "testees", "onig", "callout_witness.c")
        subprocess.run(["gcc", "-O2", "-std=gnu11", "-o", exe, src, "-lonig"],
                       check=True, capture_output=True, timeout=120)
        out = subprocess.run([exe], capture_output=True, text=True, timeout=60)
        rows = [l.split("\t") for l in out.stdout.splitlines() if l.startswith("witness")]
        for r in rows:
            (ok if r[2] == "ok" else bad)("onig witness: %s" % r[1], r[3])
        if len(rows) != 4 or out.returncode != 0:
            bad("onig witnesses", "rc %d, %d rows" % (out.returncode, len(rows)))
    except Exception as e:                          # noqa: BLE001
        bad("onig witnesses", str(e)[:300])

    # 6. pcrec's binding shape ------------------------------------------------------
    try:
        pa, _cfg = _ad.resolve("pcrec-vm")
        # the adapter module is loaded by path, never put in sys.modules
        binding_source = type(pa).compile.__globals__["callee_binding_source"]
        src = binding_source("rx_callout_1,rx_callout_netstr", "artifact.h",
                                        "1=luhn,netstr=netstr")
        good = ("const rx_callout_ref rx_callout_1 = { pb_callee, (void *)&ub_slots[1] };" in src
                and "const rx_callout_ref rx_callout_netstr = { pb_callee, (void *)&ub_named[0].slot };" in src)
        try:
            binding_source("rx_callout_7", "artifact.h", "1=luhn")
            refused = False
        except _ad.AdapterError as e:
            refused = "callout site 7 is not bound" in str(e)
        (ok if good and refused else bad)(
            "pcrec binding: numbered + named sites to the wrapper; an unbound site refused BY NAME",
            "slots &ub_slots[1], &ub_named[0].slot")
        w = os.path.join(WORK, "pcrec-b147")
        pa.prepare("pcrec-vm", w)
        cp = pa.compile("pcrec-vm", "co-luhn", luhn, {}, 1, w)
        meta = cp.forms["plain"].engine_metadata or {}
        if meta.get("callout_binding") == "separate-tu-pass" and "callout_arm" not in meta:
            ok("pcrec: a callout pattern WITHOUT the callout option keeps [B147]'s "
               "separate-tu-pass", "no arm metadata")
        else:
            bad("pcrec [B147] pass-through unchanged", repr(meta.get("callout_binding")))
    except Exception as e:                          # noqa: BLE001
        bad("pcrec binding shape", str(e)[:400])

    # 7. run_cell over the luhn family ---------------------------------------------
    store_root = os.path.join(WORK, "scratch-store")
    for t, pats in (("pcre2-jit", ["co-luhn", "co-luhn-pass", "co-luhn-twin"]),
                    ("pcre2-interp", ["co-luhn-nofn", "co-luhn-twin"]),
                    ("pcrec-vm", ["co-luhn", "co-luhn-pass", "co-luhn-twin"]),
                    ("onig-default", ["co-luhn", "co-luhn-pass", "co-luhn-twin"])):
        try:
            res = _h.run_cell("unusual", t, regimes=["search_short"], trials=1, iters=1,
                              force_unquiet=True, tier="scratch", store_root=store_root,
                              patterns=pats + ["floor"], synthetic=True,
                              workdir=os.path.join(WORK, "cell-" + t), mem=False)
            mrows = [r for r in res.rows if r["kind"] == "match"]
            outs = sorted({r["match_outcome"] for r in mrows})
            crow = {r["pattern_id"]: (r.get("engine_metadata") or {})
                    for r in res.rows if r["kind"] == "compile"}
            fired = [r for r in mrows if r["pattern_id"] == "co-luhn"
                     and "callout_fires" in (r.get("engine_metadata") or {})]
            want_fired = "co-luhn" in pats
            arms_ok = all(crow.get(p, {}).get("callout_arm") for p in pats)
            if (outs == ["matched-as-expected"] and arms_ok
                    and (bool(fired) == want_fired)):
                ok("run_cell: %s x %s matched-as-expected" % (t, "/".join(pats)),
                   "validator-accepted scratch record; %d fire-counted rows" % len(fired))
            else:
                bad("run_cell: %s" % t, repr((outs, arms_ok, len(fired))))
        except Exception as e:                      # noqa: BLE001
            bad("run_cell: %s" % t, str(e)[:400])
