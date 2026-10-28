"""check_vars.py -- `make check-unusual`'s slice for the caller-VARIABLES
members of bench/unusual ([B148] L7, docs/design/unusual_set_v1.md 3.3, 7.1,
8; review r9 C6).

Called from tools/check_unusual.py as `check_vars.run(ok, bad)` ([B148] L8: moved out of selfcheck.py's main()) (the two
reporting callbacks selfcheck owns), shaped after tools/check_calls.py. A
SMOKE: `--iters 1`, one trial, scratch records under build/, nothing printed
is a number.

What it checks, each with its control:
  1. the Python resolver (gen_vars.resolve = vars.md 2/5) against a HAND table:
     every operator on UNSET / EMPTY / a value, `${!n}` = `${n}`, a word's
     backslash, metacharacters and 0x00 escaped, the refusals. CONTROL: the
     nested chain `${a:-${b}}` (dropped from v0.1) is refused AT PARSE.
  2. the streams: stream length FIXED on the d4/d64/d4096 ladder (16,384), the
     miss count (distinct resolved patterns) = d, exactly, recomputed from the
     committed calls + bindings files and equal to values/streams.tsv; the
     refused counts equal the manifest's; the generators reproduce
     (`gen_streams.py --check`, `gen_expectations.py --streams-only --check`).
  3. ESCAPING IS EXERCISED: re-resolving WITHOUT escaping changes the tokens
     of the tenant-d64 and term-zipf streams (or fails to compile) -- the
     as-itself rule is what the expectations decide, not a no-op.
  4. the public sample (assists/problems/vars-samples.tsv): 20 cases per
     member, all three token kinds per member, reproduces from the oracle,
     disjoint from the held-out calls, and the problem statement names it.
  5. pcrec's NATIVE vars path through run_cell (scratch store, validator-
     accepted): all four members on pcrec-auto, pcrec-vm-in (the caller-buffer
     entry) and pcrec-vm-deep, every stream row `matched-as-expected` against
     expectations_stream.tsv, refused counts equal, no give-up. CONTROLS: the
     same row against a wrong hash is `wrong-span-or-captures`; PCREC_ERR_UNSET_VAR
     is a REFUSED call (token `r`), not a give-up; a vars list given to a
     var-FREE artifact is refused by name; the shim's old `pb_search` on a
     var-bearing artifact answers UNSET_VAR (it passes no variables).
  6. the capability declaration fails CLOSED: libpcre2, Oniguruma, RE2, Rust,
     Vectorscan and the -utf8 / forced-DFA pcrec siblings are
     `unsupported-by-declaration` for a vars member; the six native pcrec
     configs are not.
"""
import hashlib
import os
import re
import shutil
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "bench", "unusual"))

WORK = os.path.join(ROOT, "build", "check-vars")
NATIVE = ["pcrec-auto", "pcrec-vm-in", "pcrec-vm-deep"]
MEMBERS = ["va-tenant", "va-route", "va-term", "va-term-bang"]

# (template, binding, resolved pattern or None)  -- computed BY HAND
U, E = None, b""
HAND = [
    (b"^${n}-", {"n": b"ab"}, b"^ab-"),
    (b"^${n}-", {"n": E}, b"^-"),                              # EMPTY is a value at a bare ${n}
    (b"^${n}-", {"n": U}, None),                               # UNSET refuses
    (b"^${n}-", {}, None),                                     # a name not mentioned is UNSET
    (b"${!n}", {"n": b"ab"}, b"ab"),                           # ${!n} = ${n}
    (b"${!n}", {"n": U}, None),
    (b"${n:-w}", {"n": U}, b"w"),
    (b"${n:-w}", {"n": E}, b"w"),                              # the colon folds EMPTY in
    (b"${n:-w}", {"n": b"v"}, b"v"),
    (b"${n+w}", {"n": U}, b""),
    (b"${n+w}", {"n": E}, b"w"),                               # SET includes EMPTY
    (b"${n+w}", {"n": b"v"}, b"w"),
    (b"${n:?}", {"n": U}, None),
    (b"${n:?}", {"n": E}, None),
    (b"${n:?}", {"n": b"v"}, b"v"),
    (b"${n:-a.b}", {"n": U}, b"a\\.b"),                        # a default word is LITERAL and escaped
    (b"${n+\\.json}", {"n": b"x"}, b"\\.json"),                # a word's backslash makes the next byte literal
    (b"${n}", {"n": b"a.c"}, b"a\\.c"),
    (b"${n}", {"n": b"x|y"}, b"x\\|y"),
    (b"${n}", {"n": b"(f)"}, b"\\(f\\)"),
    (b"${n}", {"n": b"a\x00b"}, b"a\\x00b"),                   # NUL, as an escape
    (b"${n}", {"n": b"\xc3\xa9"}, b"\\xc3\\xa9"),              # a high byte, as an escape
    (b"${n}", {"n": b"a b"}, b"a\\x20b"),
    (b"${n}", {"n": b"a_9"}, b"a_9"),                          # word bytes stay themselves
    (b"x${a}y${b:-z}", {"a": b"1"}, b"x1yz"),
]


def run(ok, bad):
    print("-- [B148] L7 caller-variables members: streams, expectations, pcrec's native path --")
    import gen_vars as GV
    import gen_vars_samples as GS
    import members as MB

    # 1. the resolver -------------------------------------------------------
    wrong = [(t, b, w, GV.resolve(t, b)) for t, b, w in HAND if GV.resolve(t, b) != w]
    if not wrong:
        ok("vars: the resolver equals %d hand-computed (template, binding) cases" % len(HAND),
           "every operator x UNSET/EMPTY/value, ${!n}, word escapes, NUL, a high byte")
    else:
        bad("vars: resolver", repr(wrong[:3]))
    try:
        GV.parse(b"${a:-${b}}")
        bad("vars: CONTROL -- the nested chain must be refused at parse")
    except GV.VarsSyntax as e:
        ok("vars: CONTROL -- the nested chain `${a:-${b}}` is refused at parse (Q-C, dropped from v0.1)", str(e))
    texts = {m.id: m.text for m in MB.members() if m.route == "vars"}
    if sorted(texts) == sorted(MEMBERS) and all(GV.names(t) for t in texts.values()):
        ok("vars: the four members parse, each naming its variables",
           "; ".join("%s: %s" % (k, ",".join(GV.names(texts[k]))) for k in MEMBERS))
    else:
        bad("vars: members", repr(sorted(texts)))

    # 2. the streams --------------------------------------------------------
    built = {s.sid: s for s in GV.build_all()}
    rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(ROOT, "bench", "unusual", "values", "streams.tsv"))][1:]
    vals = {(r[0], r[1]): r for r in rows}
    ladder = [built["tenant-d4"], built["tenant-d64"], built["tenant-d4096"]]
    fixed = {len(s.calls) for s in ladder}
    miss = [s.facts("va-tenant")["distinct_resolved"] for s in ladder]
    if fixed == {16384} and miss == [4, 64, 4096]:
        ok("vars: the d4/d64/d4096 ladder holds the stream length FIXED at 16,384 calls; miss counts 4 / 64 / 4096",
           "recomputed from the resolver over the committed bindings")
    else:
        bad("vars: ladder", "lengths %r misses %r" % (sorted(fixed), miss))
    agree = True
    for (sid, m), r in vals.items():
        f = built[sid].facts(m)
        agree &= (int(r[2]) == len(built[sid].calls) and int(r[5]) == f["distinct_resolved"] and int(r[6]) == f["refused"])
    if agree and len(vals) == 6:
        ok("vars: values/streams.tsv (6 stream x member rows) equals the recomputed calls / miss count / refused")
    else:
        bad("vars: values/streams.tsv")
    man = {l.split("\t")[0]: l.rstrip("\n").split("\t") for l in open(os.path.join(ROOT, "bench", "unusual", "manifest_streams.tsv"))}
    if all(int(man[s.sid][8]) == s.facts(s.members[0])["refused"] and int(man[s.sid][5]) == len(s.calls)
           and int(man[s.sid][6]) == s.segment_bytes for s in built.values()):
        ok("vars: manifest_streams.tsv calls / segment_bytes / local_refusals equal the stream (5 streams)")
    else:
        bad("vars: manifest rows")
    route = built["route-zipf"]
    rb = route.facts("va-route")
    if rb["distinct_resolved"] < len(route.bindings):
        ok("vars: route-zipf -- the memo key is the RESOLVED pattern, not the binding",
           "%d bindings, %d distinct resolved patterns (prefix UNSET/EMPTY/api resolve alike)"
           % (len(route.bindings), rb["distinct_resolved"]))
    else:
        bad("vars: route-zipf collapse")
    import subprocess
    for script, args, what in (("gen_streams.py", ["--check"], "gen_streams.py --check (streams, calls, bindings, manifest)"),
                               ("gen_expectations.py", ["--streams-only", "--check"], "gen_expectations.py --streams-only --check (per-call expectations, libpcre2 vs python re)"),
                               ("gen_vars_samples.py", ["--check"], "gen_vars_samples.py --check")):
        p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "bench", "unusual", script)] + args,
                           capture_output=True, text=True, timeout=1200)
        if p.returncode == 0:
            ok("vars: " + what)
        else:
            bad("vars: " + what, (p.stdout + p.stderr)[-300:])

    # 3. escaping is exercised ----------------------------------------------
    from unusual_lib import Rx
    for sid, member in (("tenant-d64", "va-tenant"), ("term-zipf", "va-term")):
        st = built[sid]
        diff = 0
        for (off, ln, _b, k) in st.calls:
            line = st.data[off:off + ln]
            esc = GV.resolve(texts[member], st.bindings[k][1])
            raw = GV.resolve(texts[member], st.bindings[k][1], esc=lambda v: v)
            if esc is None:
                continue
            try:
                a = Rx(esc).search(line, 0)
                b = Rx(raw).search(line, 0)
            except Exception:                   # noqa: BLE001 -- the unescaped text may not even compile
                diff += 1
                continue
            diff += (a is None) != (b is None) or (a is not None and a[0] != b[0])
        if diff > 0:
            ok("vars: CONTROL -- %s: interpolating WITHOUT escaping changes %d of %d calls' answers" % (sid, diff, len(st.calls)),
               "so the as-itself rule is decided by the expectations")
        else:
            bad("vars: escaping not exercised on %s" % sid)

    # 4. the public sample --------------------------------------------------
    rows = [l.rstrip("\n").split("\t") for l in open(GS.OUT)][1:]
    per = {}
    for r in rows:
        per.setdefault(r[1], []).append(r[5].split(":")[0])
    if (sorted(per) == sorted(MEMBERS) and all(len(v) == 20 for v in per.values())
            and all({"m", "n", "r"} <= set(v) for v in per.values())):
        ok("vars: the public sample has 20 cases per member and every token kind (m / n / r) per member",
           "assists/problems/vars-samples.tsv")
    else:
        bad("vars: sample shape", repr({k: len(v) for k, v in per.items()}))
    if not GS.heldout_clash():
        ok("vars: no sample (binding, line) is a call of a held-out stream")
    else:
        bad("vars: sample leaks into the held-out corpus", repr(GS.heldout_clash()[:2]))
    prob = open(os.path.join(ROOT, "bench", "unusual", "assists", "problems", "vars.md"), encoding="utf-8").read()
    if "vars-samples.tsv" in prob and "pcrec" not in prob.lower() and "rx_var" not in prob:
        ok("vars: the problem statement names the sample and carries no pcrec internals")
    else:
        bad("vars: problem statement")

    # 5. pcrec's native path -------------------------------------------------
    _native(ok, bad, built, texts)

    # 6. capability fails closed ---------------------------------------------
    _capability(ok, bad)


def _native(ok, bad, built, texts):
    from pcrecbench import adapters as _ad, harness as _h
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK, exist_ok=True)
    store_root = os.path.join(WORK, "scratch-store")
    last = None
    for t in NATIVE:
        try:
            res = _h.run_cell("unusual", t, regimes=["call-stream"], trials=1, iters=1, force_unquiet=True,
                              tier="scratch", store_root=store_root, patterns=MEMBERS, synthetic=True,
                              workdir=os.path.join(WORK, "cell-" + t), mem=False)
        except Exception as e:                   # noqa: BLE001
            bad("vars: %s through run_cell" % t, str(e)[:400])
            continue
        mrows = [r for r in res.rows if r["kind"] == "match"]
        outs = sorted({r["match_outcome"] for r in mrows})
        want = sum(len(built[s].picks) > 0 for s in built)
        refused = sum((r.get("stream") or {}).get("refused", 0) for r in mrows)
        gave = sum((r.get("stream") or {}).get("gave_up", 0) for r in mrows)
        exp_refused = sum(int(r[6]) for r in (l.rstrip("\n").split("\t") for l in open(
            os.path.join(ROOT, "bench", "unusual", "values", "streams.tsv")).readlines()[1:]))
        if len(mrows) == 6 and outs == ["matched-as-expected"] and refused == exp_refused and gave == 0:
            ok("vars: %s runs all four members NATIVELY -- 6 stream rows matched-as-expected" % t,
               "%d calls REFUSED by the variables rule (token r), 0 gave up" % refused)
            last = (t, res)
        else:
            bad("vars: %s native path" % t, "rows %d outcomes %r refused %d gave_up %d" % (len(mrows), outs, refused, gave))
    # control: a wrong hash is wrong-span-or-captures
    if last:
        t, res = last
        r = [x for x in res.rows if x["kind"] == "match" and x["pattern_id"] == "va-route"][0]
        st = r["stream"]
        ad, _ = _ad.resolve(t)
        row = types.SimpleNamespace(answer="stream", detail=None, stream=dict(st, tokens=st["calls"], first_code=None, first_limit=None),
                                    consumed=None)

        class _Sexp:
            calls, matched, nomatch, refused = st["calls"], st["matched"], st["nomatch"], st["refused"]
            results_sha256 = "0" * 64
        from pcrecbench import subbench as _sbm
        subj = _sbm.find("unusual").subject(r["subject_id"])
        out = _h.stream_outcome(row, _Sexp, subj, {}, ad)
        if out[0] == "wrong-span-or-captures":
            ok("vars: CONTROL -- the same va-route row against a wrong hash is wrong-span-or-captures")
        else:
            bad("vars: control outcome", repr(out[:3]))
    _driver_controls(ok, bad)


def _driver_controls(ok, bad):
    """The three driver-level controls on a tiny hand stream: a refusal is `r`
    (not a give-up), a vars list on a var-free artifact is refused by name, and
    the OLD pb_search on a var-bearing artifact answers UNSET_VAR."""
    from pcrecbench import adapters as _ad, subbench as _sbm
    ad, _ = _ad.resolve("pcrec-auto")
    work = os.path.join(WORK, "drv")
    ad.prepare("pcrec-auto", work)

    def handle(pattern, pid):
        cp = ad.compile("pcrec-auto", pid, pattern, {}, 1, work)
        res = cp.forms["plain"]
        if res.outcome != "compiled":
            raise RuntimeError("did not compile %r: %s" % (pattern, res.diagnostic))
        return res.handle

    line = b"acme-0001 ERROR x\n"
    subj = os.path.join(WORK, "tiny.bin")
    with open(subj, "wb") as f:
        f.write(line * 3)
    calls = os.path.join(WORK, "tiny.calls.tsv")
    with open(calls, "w", newline="\n") as f:
        f.write("call_id\toffset\tlength\tsegment_bytes\tbinding_id\n")
        for i in range(3):
            f.write("%d\t%d\t%d\t%d\tb%d\n" % (i, i * len(line), len(line) - 1, len(line) - 1, i))
    binds = os.path.join(WORK, "tiny.bindings.tsv")
    with open(binds, "w", newline="\n") as f:
        f.write("binding_id\tname\tvalue\nb0\ttenant\t%s\nb1\ttenant\tUNSET\nb2\ttenant\tEMPTY\n" % b"acme".hex())

    calls_nb = os.path.join(WORK, "tiny.calls-nobind.tsv")
    with open(calls_nb, "w", newline="\n") as f:
        f.write("call_id\toffset\tlength\tsegment_bytes\tbinding_id\n")
        for i in range(3):
            f.write("%d\t%d\t%d\t%d\t-\n" % (i, i * len(line), len(line) - 1, len(line) - 1))

    def mk(with_bindings):
        s = _sbm.Subject("tiny", len(line) * 3, hashlib.sha256(line * 3).hexdigest(), "tiny", "no", subj, "stream")
        s.calls_path, s.calls, s.segment_bytes = (calls if with_bindings else calls_nb), 3, 3 * (len(line) - 1)
        s.bindings_path = binds if with_bindings else None
        return s
    try:
        h = handle(rb"^${tenant}-[0-9]{4} (?:ERROR|WARN) ", "tiny-vars")
        by_trial, _i, _n = ad.measure(h, "call-stream", [mk(True)], 1, 1, timeout=120)
        st = by_trial[0][0].stream
        if (st["matched"], st["nomatch"], st["refused"], st["gave_up"]) == (1, 1, 1, 0):
            ok("vars: PCREC_ERR_UNSET_VAR is a REFUSED call -- one match, one no-match (EMPTY), one refusal (UNSET), 0 give-ups",
               "tokens m / n / r")
        else:
            bad("vars: tiny stream counts", repr(st))
        # the old three-column path on the SAME var-bearing artifact: no variables
        # are passed, so every call is refused by the artifact (-8 -> a give-up
        # token here, NAMED PCREC_ERR_UNSET_VAR) -- the artifact links and says so
        by_trial, _i, _n = ad.measure(h, "call-stream", [mk(False)], 1, 1, timeout=120)
        st = by_trial[0][0].stream
        if st["gave_up"] == 3 and st["refused"] == 0 and st.get("first_code") == -8:
            ok("vars: CONTROL -- the pre-existing pb_search on a var-bearing artifact passes no variables and answers UNSET_VAR",
               "gave_up=%d refused=%d first code %s (-8)" % (st["gave_up"], st["refused"], st.get("first_code")))
        else:
            bad("vars: pb_search on a var-bearing artifact", repr(st))
    except Exception as e:                       # noqa: BLE001
        bad("vars: tiny-stream driver controls", str(e)[:400])
    try:
        h = handle(rb"^acme", "tiny-free")
        by_trial, _i, notes = ad.measure(h, "call-stream", [mk(True)], 1, 1, timeout=120)
        text = " ".join(notes) + " ".join("%s %s" % (x.answer, x.detail) for x in (by_trial[0] if by_trial else []))
        if by_trial and by_trial[0] and by_trial[0][0].stream:
            bad("vars: a vars list on a var-free artifact was ANSWERED", text[:200])
        elif "no caller variables" in text:
            ok("vars: a vars stream given to a var-FREE artifact is refused BY NAME", "no caller variables (RX_NVARS undefined)")
        else:
            bad("vars: var-free refusal text", text[:300])
    except Exception as e:                       # noqa: BLE001
        if "no caller variables" in str(e):
            ok("vars: a vars stream given to a var-FREE artifact is refused BY NAME", "no caller variables (RX_NVARS undefined)")
        else:
            bad("vars: var-free refusal text", str(e)[:300])


def _capability(ok, bad):
    from pcrecbench import capability as C, subbench as _sbm
    sb = _sbm.find("unusual")
    pats = {p.name: p for p in sb.patterns}
    closed = ["pcre2-interp", "pcre2-jit", "onig-default", "re2-default", "rust-default", "vectorscan-block-som",
              "pcrec-auto-utf8", "pcrec-dfa"]
    native = ["pcrec-auto", "pcrec-nocaps", "pcrec-vm", "pcrec-vm-in", "pcrec-auto-deep", "pcrec-vm-deep"]

    def miss(t, m):
        return C.missing_capabilities(sb, t, pats[m])
    if (all(miss(t, m) for t in closed for m in MEMBERS)
            and not any(miss(t, m) for t in native for m in MEMBERS)):
        ok("vars: capability fails CLOSED -- %d non-native configs are unsupported-by-declaration for all four members; "
           "the %d native pcrec configs are not" % (len(closed), len(native)))
    else:
        bad("vars: capability declaration", repr({t: sorted(miss(t, "va-term")) for t in closed + native}))
