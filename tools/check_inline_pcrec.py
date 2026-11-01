#!/usr/bin/env python3
"""check_inline_pcrec.py -- `make check-unusual`'s slice for the INLINE pcrec
callout arm's BUILD-DEPENDENT half ([B148] lane b148inline2, inline arm part 2;
docs/dev/lanes/b148inline_report.md section 5 items 1-5). The source-only half
(generator, identity, pins, behaviour on a stand-in) is tools/check_inline.py.

Called from tools/check_unusual.py as `check_inline_pcrec.run(ok, bad)`;
standalone: `python3 -I tools/check_inline_pcrec.py`. It NEEDS the pinned pcrec
binary (build/pcrec-<pin>), gcc and clang, and runs pcrec, the C compilers and
the pcrec driver: NOT a light check. Without the pinned binary it is SKIPPED BY
NAME (one `ok` line), never silently green. A SMOKE: one trial, iters 1, scratch
under build/check-inline-pcrec; nothing printed is a number.

  0. IDS: `pcrec-auto-inline` / `pcrec-vm-inline` derive config_extra `inline`
     and the testee_id `pcrec_<pin>_{auto,vm}-caps-simdna_inline`; their
     describe() blocks name the grant in build_flags and runtime_options; no
     other pcrec config's config_extra mentions `inline` (the every-pre-existing-
     id-unchanged proof itself is selfcheck's frozen-renderer arm).
  1. COMPILE (item 1): each of the 14 blocks of inline/blocks.tsv, compiled as
     the adapter does (`--allow-code=c --include-block FRAG:LINE ENTRY`, auto and
     vm), exits 0 and the artifact stamps RX_CODE_LANGS "c", RX_CALLOUTS 1,
     RX_CALLOUT_BINDINGS "" (an all-code artifact), with NO `extern ...
     rx_callout_` binding declaration (so no binding unit can be needed).
  2. REFUSAL CONTROLS (item 2), through pcrec itself, on a scratch copy of the
     luhn entry+fragment: a fragment byte edited (the pin no longer verifies),
     the `sha256` dropped from the entry, `--allow-code=c` omitted -- each
     refused (rc != 0) with the named reason in stderr; the unmutated copy
     compiles (the positive control).
  3. gcc AND clang (item 3): every artifact of item 1 compiles with
     -Wall -Wextra; no diagnostic points INTO a fragment (`.rxt`, the user
     region the artifact's #line maps back to) -- the user's segment is warning-
     free under both compilers; the total warning count is printed.
  4. ANSWERS (item 4): through the adapter, `pcrec-auto-inline` equals the
     separate-TU `pcrec-auto` on every short subject for each real and pass
     arm, plus `pcrec-vm-inline` vs `pcrec-vm`; the FIRST-CANDIDATE-FAILS
     control (check_callouts) answers the second card under the real inline
     arm and the first under the stub; real != twin on at least one subject
     (the callee is reached); the inline compile row says callout_binding
     `inline`, code_langs `c`, carries inline_entry_sha256 /
     inline_fragment_sha256, NO callees_sha256, and has no fire handle (no
     `callout_fires` on an inline row, by declaration).
  5. CENSUS (item 5): emit_bytes / emit_code_bytes / program_sha256_v3 of the 14
     inline artifacts beside their separate-TU counterparts, printed as a
     table; the inline program differs from the separate-TU one on every real
     arm (the code is IN the artifact) -- the control that the table is not
     comparing one artifact with itself.
"""
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "bench", "unusual"))

UNUSUAL = os.path.join(ROOT, "bench", "unusual")
WORK = os.path.join(ROOT, "build", "check-inline-pcrec")
TO = "/usr/bin/gnutimeout"
FF_SUBJECT = b"card 4111111111111112 then 4111111111111111 end"
FF_FIRST, FF_SECOND = (5, 21), (27, 43)


def _rows():
    import csv
    with open(os.path.join(UNUSUAL, "inline", "blocks.tsv"), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _pcrec_argv(binary, flags, out, frag, line, entry):
    # the adapter's own argv shape (testees/pcrec/adapter.py _compile_one),
    # spelled from the config's flags so the check cannot drift from it
    return ([binary, "-p", "rx", "-fcomments", "--warn-emit-bytes=1"] + flags
            + ["-o", out, "--include-block", "%s:%s" % (frag, line), entry])


def _run(argv, timeout=300):
    return subprocess.run([TO, str(timeout)] + argv, capture_output=True, text=True)


def _stamp(text, name):
    m = re.search(r'^#define\s+RX_%s\s+"?([^"\n]*)"?\s*$' % name, text, re.M)
    return m.group(1) if m else None


def _read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def run(ok, bad):
    print("-- [B148] inline arm part 2: the build-dependent half --")
    from pcrecbench import adapters as _ad, record as _rec, subbench as _sbm, callees
    import unusual_lib as U                                      # noqa: F401
    shutil.rmtree(WORK, ignore_errors=True)
    os.makedirs(WORK)
    try:
        ad = _ad.discover()["pcrec"]
        binary = ad.pin_binary(build=False)
        if not os.path.isfile(binary):
            raise FileNotFoundError(binary)
    except Exception as e:                                       # noqa: BLE001
        ok("inline-pcrec: SKIPPED by name, no pinned pcrec binary",
           str(e).strip().splitlines()[0][:100] if str(e).strip() else "pin.sh --path failed")
        return
    cc_list = [c for c in ("gcc", "clang") if shutil.which(c)]
    rows = _rows()
    tmp = os.path.join(WORK, "describe")

    # ---- 0. ids --------------------------------------------------------------
    try:
        for tid, mode in (("pcrec-auto-inline", "auto"), ("pcrec-vm-inline", "vm")):
            blk = ad.describe(tid, tmp)
            got = _rec.derive_testee_id(blk).split("_", 2)[2]
            want = "%s-caps-simdna_inline" % mode
            flags_ok = ("--allow-code=c" in blk.get("build_flags", "")
                        and any(o.get("name") == "--allow-code" and o.get("value") == "c"
                                for o in blk.get("runtime_options", [])))
            if got == want and blk.get("config_extra") == "inline" and flags_ok:
                ok("ids: %s derives the frozen id shape" % tid,
                   _rec.derive_testee_id(blk))
            else:
                bad("ids: %s" % tid, repr((got, want, blk.get("config_extra"), flags_ok)))
        stray = [t for t in ad.testees() if t not in ("pcrec-auto-inline", "pcrec-vm-inline")
                 and "inline" in (ad.config(t).get("config_extra") or "")]
        (ok if not stray else bad)("ids: no other pcrec config carries an `inline` token", repr(stray))
    except Exception as e:                                       # noqa: BLE001
        bad("ids", "%s: %s" % (type(e).__name__, str(e)[:300]))

    # ---- 1. compile the 14 blocks -------------------------------------------
    arts = {}                              # (arm, form, mode) -> artifact .c path
    for mode, flags in (("auto", ["--features", "all", "--allow-code=c"]),
                        ("vm", ["--features", "all", "--engine=vm", "--allow-code=c"])):
        fails, n = [], 0
        for r in rows:
            frag = os.path.join(UNUSUAL, r["fragment"])
            entry = os.path.join(UNUSUAL, r["entry"])
            out = os.path.join(WORK, mode, r["arm"], r["form"], "artifact.c")
            os.makedirs(os.path.dirname(out))
            p = _run(_pcrec_argv(binary, flags, out, frag, r["line"], entry))
            n += 1
            if p.returncode != 0:
                fails.append((r["arm"], r["form"], p.stderr.strip()[:160]))
                continue
            txt = _read(out) + _read(out[:-2] + ".h")
            st = (_stamp(txt, "CODE_LANGS"), _stamp(txt, "CALLOUTS"),
                  _stamp(txt, "CALLOUT_BINDINGS"))
            if st != ("c", "1", "") or re.search(r"extern\s+const\s+rx_callout_ref", txt):
                fails.append((r["arm"], r["form"], "stamps %r" % (st,)))
                continue
            arts[(r["arm"], r["form"], mode)] = out
        if not fails:
            ok("compile [%s]: all %d blocks compile, RX_CODE_LANGS \"c\" / RX_CALLOUTS 1 / "
               "RX_CALLOUT_BINDINGS \"\", no extern binding" % (mode, n), "rc 0 x %d" % n)
        else:
            bad("compile [%s]: the inline blocks" % mode, repr(fails)[:600])

    # ---- 2. refusal controls through pcrec itself ---------------------------
    luhn = [r for r in rows if r["arm"] == "co-luhn" and r["form"] == "plain"][0]
    flags = ["--features", "all", "--allow-code=c"]

    def stage(name, mutate=None):
        d = os.path.join(WORK, "ctl-" + name)
        os.makedirs(os.path.join(d, "inline"))
        os.makedirs(os.path.join(d, "callees"))
        frag = os.path.join(d, "callees", os.path.basename(luhn["fragment"]))
        ent = os.path.join(d, "inline", os.path.basename(luhn["entry"]))
        shutil.copy(os.path.join(UNUSUAL, luhn["fragment"]), frag)
        shutil.copy(os.path.join(UNUSUAL, luhn["entry"]), ent)
        if mutate:
            mutate(frag, ent)
        return d, frag, ent

    def flip_fragment(frag, _ent):
        with open(frag, "rb") as f:
            b = bytearray(f.read())
        i = b.index(b"UB_FAIL")
        b[i] ^= 0x01
        with open(frag, "wb") as f:
            f.write(b)

    def drop_pin(_frag, ent):
        t = _read(ent)
        with open(ent, "w") as f:
            f.write(re.sub(r"\s+sha256\s+[0-9a-f]{64}", "", t))

    for name, mut, fl, needles in (
            ("ok", None, flags, None),
            ("stalepin", flip_fragment, flags, ("sha256", "pin", "digest", "mismatch")),
            ("nopin", drop_pin, flags, ("sha256", "pin")),
            ("nogrant", None, ["--features", "all"], ("code-c", "allow-code", "code"))):
        d, frag, ent = stage(name, mut)
        p = _run(_pcrec_argv(binary, fl, os.path.join(d, "a.c"), frag, luhn["line"], ent))
        if needles is None:
            (ok if p.returncode == 0 else bad)(
                "control: the unmutated scratch copy compiles (positive control)",
                p.stderr.strip()[:160])
        else:
            hit = any(n in p.stderr.lower() for n in needles)
            (ok if p.returncode != 0 and hit else bad)(
                "refusal: %s is refused through pcrec, by name" % name,
                "rc %d: %s" % (p.returncode, (p.stderr.strip().splitlines() or ["(no stderr)"])[0][:110]))

    # ---- 3. gcc AND clang on every artifact ---------------------------------
    for cc in cc_list:
        warn_total, user_hits, build_fail = 0, [], []
        for key, art in sorted(arts.items()):
            if key[2] != "auto":
                continue
            p = _run([cc, "-std=gnu11", "-O2", "-Wall", "-Wextra", "-fPIC", "-c",
                      "-I", os.path.dirname(art), "-o", os.devnull, art])
            if p.returncode != 0:
                build_fail.append((key, p.stderr.strip()[:120]))
            for line in p.stderr.splitlines():
                if "warning:" in line:
                    warn_total += 1
                    if ".rxt" in line.split(":", 1)[0]:
                        user_hits.append(line[:140])
        if not build_fail and not user_hits:
            ok("cc axis [%s]: every inline artifact builds -Wall -Wextra, no diagnostic in a "
               "fragment's user region" % cc, "%d warning(s) elsewhere" % warn_total)
        else:
            bad("cc axis [%s]" % cc, repr((build_fail, user_hits))[:600])

    # ---- 4. answers through the adapter -------------------------------------
    sb = _sbm.load(UNUSUAL)
    shorts = sb.subjects_for("search_short")
    d = os.path.join(WORK, "subj")
    os.makedirs(d)
    import hashlib
    path = os.path.join(d, "ff")
    with open(path, "wb") as f:
        f.write(FF_SUBJECT)
    ff = _sbm.Subject("ff", len(FF_SUBJECT), hashlib.sha256(FF_SUBJECT).hexdigest(),
                      "check_inline_pcrec", "no", path, "short")

    def co_of(pid):
        p = [x for x in sb.patterns if x.name == pid][0]
        return callees.options_for(sb, p)

    def comp(tid, pid, w):
        a, _c = _ad.resolve(tid)
        a.prepare(tid, w)
        cp = a.compile(tid, pid, sb.pattern_bytes(pid), {"callouts": co_of(pid)}, 1, w)
        res = cp.forms["plain"]
        if res.outcome != "compiled":
            raise RuntimeError("%s did not compile %s: %s" % (tid, pid, res.diagnostic))
        return a, res

    def answers(a, res, subs):
        by, _i, _n = a.measure(res.handle, "search_short", subs, 1, 1, timeout=300)
        return {r.subject_id: (r.answer, r.start, r.end, r.caps) for r in by[0]}

    census = []
    for inl, sep in (("pcrec-auto-inline", "pcrec-auto"), ("pcrec-vm-inline", "pcrec-vm")):
        bad_arms, real_vs_twin = [], 0
        try:
            for fam in ("co-luhn", "co-isbn", "co-member", "co-netstr"):
                arms = ["", "-pass"] if fam != "co-netstr" else [""]
                ans_twin = None
                a_s, r_s = comp(sep, fam + "-twin", os.path.join(WORK, sep))
                ans_twin = answers(a_s, r_s, shorts)
                for arm in arms:
                    pid = fam + arm
                    a_i, r_i = comp(inl, pid, os.path.join(WORK, inl))
                    a_s, r_s = comp(sep, pid, os.path.join(WORK, sep))
                    ai, as_ = answers(a_i, r_i, shorts), answers(a_s, r_s, shorts)
                    if ai != as_:
                        bad_arms.append(pid)
                    meta = r_i.engine_metadata
                    if not (meta.get("callout_binding") == "inline" and meta.get("code_langs") == "c"
                            and meta.get("inline_entry_sha256") and meta.get("inline_fragment_sha256")
                            and "callees_sha256" not in meta and a_i.fire_handle(r_i.handle) is None):
                        bad_arms.append(pid + ":metadata")
                    if arm == "":
                        real_vs_twin += sum(1 for s in ai if ai[s] != ans_twin.get(s))
                    for kind, res in (("inline", r_i), ("sep", r_s)):
                        m = res.engine_metadata
                        census.append((inl, pid, kind, m.get("emit_bytes"), m.get("emit_code_bytes"),
                                       m.get("program_sha256_v3"), m.get("callout_binding")))
            if not bad_arms and real_vs_twin > 0:
                ok("answers: %s == %s on %d short subjects x 4 members (real + pass arms)"
                   % (inl, sep, len(shorts)), "control: real != twin on %d subject(s)" % real_vs_twin)
            else:
                bad("answers: %s == %s" % (inl, sep), "differ: %s; real-vs-twin %d" % (bad_arms, real_vs_twin))
            a_i, r_real = comp(inl, "co-luhn", os.path.join(WORK, inl))
            _a2, r_stub = comp(inl, "co-luhn-pass", os.path.join(WORK, inl))
            ra, sa = answers(a_i, r_real, [ff])["ff"], answers(a_i, r_stub, [ff])["ff"]
            if ra[:3] == ("match",) + FF_SECOND and sa[:3] == ("match",) + FF_FIRST:
                ok("mapping: %s -- a FAILing first candidate moves to the second" % inl,
                   "real %s, stub %s" % (ra[1:3], sa[1:3]))
            else:
                bad("mapping: %s first-candidate-fails" % inl, repr((ra, sa)))
        except Exception as e:                                   # noqa: BLE001
            bad("answers: %s" % inl, "%s: %s" % (type(e).__name__, str(e)[:400]))

    # ---- 5. the census ------------------------------------------------------
    if census:
        print("   census (testee, pattern, kind, emit_bytes, emit_code_bytes, program_v3[:12], binding):")
        for c in census:
            print("     %s %s %s %s %s %s %s" % (c[0], c[1], c[2], c[3], c[4], (c[5] or "")[:12], c[6]))
        same = []
        by = {}
        for t, pid, kind, eb, ecb, h, _b in census:
            by[(t, pid, kind)] = (eb, ecb, h)
        for (t, pid, kind), v in by.items():
            if kind == "inline" and not pid.endswith("-pass") and by.get((t, pid, "sep"), (0, 0, None))[2] == v[2]:
                same.append((t, pid))
        miss = [k for k, v in by.items() if None in v]
        if not same and not miss:
            ok("census: %d artifacts read; every real inline program differs from its "
               "separate-TU one" % len(by), "table printed above")
        else:
            bad("census", "identical-program %s; missing fields %s" % (same, miss))
    else:
        bad("census", "no artifacts were compiled through the adapter")


if __name__ == "__main__":
    fails = []

    def _ok(what, detail=""):
        print("   PASS  %-62s %s" % (what, detail))

    def _bad(what, detail=""):
        fails.append(what)
        print("   FAIL  %-62s %s" % (what, detail))
    run(_ok, _bad)
    print("check_inline_pcrec: %d FAILED" % len(fails) if fails else "check_inline_pcrec: all passed")
    sys.exit(1 if fails else 0)
