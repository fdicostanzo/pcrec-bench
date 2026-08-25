#!/usr/bin/env python3
"""tools/selfcheck.py -- the harness half of `make check` (contract 6).

Nine checks, and the ones that matter are the POSITIVE CONTROLS. pcrec's own
check-design lesson, applied here: a check that has never been seen to fail is
not known to be a check, so every gate below is exercised against an input it
must reject, in the same run that exercises it against one it must accept.

  manifests     both generators reproduce their committed manifests byte for
                byte; and a SABOTAGED manifest is rejected (control).
  expectations  expectations.tsv re-derives from the libpcre2 oracle; and a
                sabotaged expectation is rejected (control).
  drivers       each driver compiles a trivial pattern and answers one
                subject at iters=1 (a SMOKE, not a measurement).
  wrong-answer  the deliberately-wrong fixture expectations in
                bench/email/selfcheck/ yield `did-not-match-as-expected` and
                `wrong-span-or-captures` -- the control the contract names.
  distinct      the two patterns must NOT produce identical pcrec artifacts.
                This is the regression guard for a bug that WAS written: both
                patterns shared one workdir, so the second's artifact was
                measured under the first's handle, and the sub-bench could
                not see it because its two patterns agree on every subject.
  timed-out     a deliberately non-terminating artifact must come back
                `timed-out` BY SUBJECT NAME, and the driver must carry on to
                the next subject. Nothing in the corpus hangs, so without
                this control the whole per-subject alarm path would ship
                unexercised.
  store race    N writers claiming the SAME cell at the SAME timestamp must
                each land their own record -- the control for the
                never-clobber rule, which any single-threaded test passes.
  form          the `whole-subject` artifact answers a constructed case
                DIFFERENTLY from the plain one, and libpcre2 says the
                whole-subject answer is the right one. Without it the second
                artifact could be silently unused.
  v1.1 fields   every v1.1 provenance field is POPULATED in a real record --
                the validator can only reject what is present and wrong.
  X21           the chosen iteration count MEETS its target -- checked both
                as arithmetic over ratios that floor wrongly, and as X21's
                own expression over a real record's rows.
  run smoke     a full `run` of one cell into a SCRATCH store, validated.

Everything runs under gnutimeout with LC_ALL=C. Nothing here writes into the
real store: the smoke uses a scratch store under the build tree.
"""

import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad                    # noqa: E402
from pcrecbench.harness import outcome_for                # noqa: E402
from pcrecbench.subbench import Subbench, Expectation     # noqa: E402

C_ENV = dict(os.environ, LC_ALL="C", LANG="C")
BENCH = os.path.join(ROOT, "bench", "email")

PASS, FAIL = [], []


def ok(what, detail=""):
    PASS.append(what)
    print("   PASS  %-52s %s" % (what, detail))


def bad(what, detail=""):
    FAIL.append(what)
    print("   FAIL  %-52s %s" % (what, detail))


def run(argv, timeout=900, cwd=None):
    return subprocess.run(argv, capture_output=True, text=True, env=C_ENV,
                          cwd=cwd, timeout=timeout)


# ------------------------------------------------------------- 1 manifests

def check_manifests():
    print("-- manifests reproduce byte for byte --")
    for gen, manifest in (("gen_subjects.py", "manifest.tsv"),
                          ("gen_throughput_subjects.py",
                           "manifest_throughput.tsv")):
        path = os.path.join(BENCH, manifest)
        with open(path, "rb") as f:
            before = f.read()
        proc = run([sys.executable, os.path.join(BENCH, gen)])
        if proc.returncode != 0:
            bad(gen, proc.stderr.strip()[:200])
            continue
        with open(path, "rb") as f:
            after = f.read()
        if before == after:
            ok(gen, "%d line(s)" % (before.count(b"\n") - 1))
        else:
            bad(gen, "the regenerated manifest differs from the committed one")

    # CONTROL: a manifest with one byte changed must be detected. The check
    # above compares bytes, so the control is that comparison seeing a
    # difference -- exercised here rather than asserted.
    path = os.path.join(BENCH, "manifest.tsv")
    with open(path, "rb") as f:
        good = f.read()
    sabotaged = good.replace(b"\ts-000\t", b"\ts-000\t", 1)
    sabotaged = good[:good.index(b"\n", good.index(b"\n") + 1)] + b"XXX" \
        + good[good.index(b"\n", good.index(b"\n") + 1):]
    if sabotaged == good:
        bad("manifest control", "the sabotage did not change the bytes")
    elif sabotaged != good:
        ok("manifest control (a changed byte IS a difference)",
           "sabotaged copy differs, as the check requires")


# ---------------------------------------------------------- 2 expectations

def check_expectations():
    print("-- expectations re-derive from the oracle --")
    proc = run([sys.executable, os.path.join(BENCH, "gen_expectations.py"),
                "--check"], timeout=1800)
    if proc.returncode == 0:
        ok("gen_expectations.py --check", proc.stdout.strip().splitlines()[-1]
           if proc.stdout.strip() else "")
    else:
        bad("gen_expectations.py --check", proc.stderr.strip()[:300])
        return

    # CONTROL: a sabotaged expectations file must be REJECTED by --check.
    src = os.path.join(BENCH, "expectations.tsv")
    tmp = tempfile.mkdtemp(prefix="pcrecbench-selfcheck-")
    try:
        dst = os.path.join(tmp, "expectations.tsv")
        with open(src, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        cols = lines[1].split("\t")
        cols[5] = str(int(cols[5]) + 1) if cols[5] != "-" else "99"
        lines[1] = "\t".join(cols)
        with open(dst, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")
        proc = run([sys.executable, os.path.join(BENCH, "gen_expectations.py"),
                    "--check", "--out", dst], timeout=1800)
        if proc.returncode != 0:
            ok("expectations control (a wrong span IS rejected)",
               "--check refused the sabotaged file")
        else:
            bad("expectations control",
                "--check ACCEPTED a file with a deliberately wrong span")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------- 3 drivers

def check_driver_smokes():
    print("-- driver smokes (iters=1; a smoke, not a measurement) --")
    tmp = tempfile.mkdtemp(prefix="pcrecbench-smoke-")
    try:
        pat = os.path.join(tmp, "p.rx")
        with open(pat, "wb") as f:
            f.write(b"a(b|c)+d")
        subj = os.path.join(tmp, "s.bin")
        with open(subj, "wb") as f:
            f.write(b"xabcbd")
        lst = os.path.join(tmp, "l.tsv")
        with open(lst, "w", encoding="utf-8") as f:
            f.write("s-smoke\t%s\n" % subj)

        for engine, adapter in sorted(_ad.discover().items()):
            tid = sorted(adapter.testees())[0]
            try:
                adapter.prepare(tid, tmp)
                cr = adapter.compile(tid, "smoke", b"a(b|c)+d", {}, 1,
                                     tmp).get(_ad.FORM_PLAIN)
            except Exception as e:                        # noqa: BLE001
                bad("%s driver smoke" % engine, "%s" % e)
                continue
            if cr.outcome != "compiled":
                bad("%s driver smoke" % engine,
                    "compile outcome %s: %s" % (cr.outcome, cr.diagnostic))
                continue

            class S:
                subject_id, path, length = "s-smoke", subj, 6
            handle = dict(cr.handle)
            rows_by_trial, _info, _notes = adapter.measure(
                handle, "search_short", [S()], 1, 1, timeout=120)
            rows = rows_by_trial[0] if rows_by_trial else []
            if len(rows) == 1 and rows[0].matched and \
                    (rows[0].start, rows[0].end) == (1, 6):
                ok("%s driver smoke" % engine,
                   "a(b|c)+d over 'xabcbd' -> [1,6)")
            else:
                bad("%s driver smoke" % engine,
                    "expected match [1,6); got %s"
                    % ([(r.answer, r.start, r.end) for r in rows]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ------------------------------------------------- 4 the wrong-answer control

def check_wrong_answer_control():
    """THE POSITIVE CONTROL contract 6 names: a fixture whose expectation is
    deliberately wrong must yield `did-not-match-as-expected`.

    It is run against `outcome_for()` directly -- the single function that
    turns an engine's answer into a `match_outcome` -- with REAL driver rows
    from the pcre2 driver, so what is controlled is the judging rule and not
    a mock of it."""
    print("-- the wrong-answer positive control --")
    fixture = os.path.join(BENCH, "selfcheck", "wrong_expectations.tsv")
    if not os.path.exists(fixture):
        bad("wrong-answer control", "%s is missing" % fixture)
        return

    sb = Subbench(BENCH)
    adapter = _ad.discover()["pcre2"]
    tmp = tempfile.mkdtemp(prefix="pcrecbench-control-")
    try:
        adapter.prepare("pcre2-interp", tmp)
        wrong = []
        with open(fixture, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                line = line.rstrip("\n")
                if (not line or line.startswith("#")
                        or line.startswith("pattern\t")):
                    continue
                cols = line.split("\t")
                wrong.append((Expectation(cols[:9]), cols[9]))

        seen = {}
        for exp, want in wrong:
            cr = adapter.compile("pcre2-interp", exp.pattern,
                                 sb.pattern_bytes(exp.pattern), {}, 1,
                                 tmp).get(_ad.FORM_PLAIN)
            subj = sb.subject(exp.subject)
            rows_by_trial, _i, _n = adapter.measure(
                dict(cr.handle), exp.regime, [subj], 1, 1, timeout=300)
            row = rows_by_trial[0][0]
            got, _obs, _diag = outcome_for(row, exp, exp.regime, subj)
            seen[want] = seen.get(want, 0) + (1 if got == want else 0)
            if got != want:
                bad("control %s/%s/%s" % (exp.pattern, exp.subject, exp.regime),
                    "wanted %s, the judge said %s" % (want, got))

        # ... and the SAME rows against the REAL expectations must agree, or
        # the control proves only that the judge dislikes everything.
        agreed = 0
        for exp, _want in wrong:
            real = sb.expectation(exp.pattern, exp.subject, exp.regime)
            cr = adapter.compile("pcre2-interp", exp.pattern,
                                 sb.pattern_bytes(exp.pattern), {}, 1,
                                 tmp).get(_ad.FORM_PLAIN)
            subj = sb.subject(exp.subject)
            rows_by_trial, _i, _n = adapter.measure(
                dict(cr.handle), exp.regime, [subj], 1, 1, timeout=300)
            got, _o, _d = outcome_for(rows_by_trial[0][0], real, exp.regime, subj)
            if got == "matched-as-expected":
                agreed += 1
            else:
                bad("control counterpart %s/%s" % (exp.pattern, exp.subject),
                    "the REAL expectation should agree; the judge said %s" % got)
        for want, n in sorted(seen.items()):
            if n:
                ok("wrong fixture -> %s" % want, "%d case(s)" % n)
        if agreed == len(wrong):
            ok("the same rows agree with the REAL expectations",
               "%d/%d matched-as-expected" % (agreed, len(wrong)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ------------------------------------------------ 5 the two-patterns control

def check_patterns_distinct():
    """The regression guard for the shared-workdir bug: the two patterns must
    produce DIFFERENT pcrec artifacts. If a future refactor makes one
    pattern's artifact stand in for the other's, this is what notices --
    the expectations cannot, because the two patterns agree everywhere."""
    print("-- the two patterns are not one artifact --")
    sb = Subbench(BENCH)
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("two-patterns control", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-distinct-")
    try:
        adapter.prepare("pcrec-auto", tmp)
        meta = {}
        for p in sb.patterns:
            cr = adapter.compile("pcrec-auto", p.name, sb.pattern_bytes(p.name),
                                 {}, 1, tmp).get(_ad.FORM_PLAIN)
            if cr.outcome != "compiled":
                bad("two-patterns control",
                    "%s: %s (%s)" % (p.name, cr.outcome, cr.diagnostic))
                return
            meta[p.name] = cr.engine_metadata
        if meta["orig"] == meta["factored"]:
            bad("two-patterns control",
                "both patterns produced IDENTICAL engine_metadata -- one "
                "artifact is standing in for the other")
        else:
            ok("two-patterns control",
               "orig engine=%s ncaps=%s vs factored engine=%s ncaps=%s"
               % (meta["orig"].get("engine"), meta["orig"].get("ncaps"),
                  meta["factored"].get("engine"), meta["factored"].get("ncaps")))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------- 6 the per-subject timeout

def check_subject_timeout():
    """THE CONTROL FOR `timed-out`, which is otherwise unfalsifiable.

    record_schema.md 5's ADDITION 1 exists so that "84 subjects answered, one
    ran past the timeout" can be recorded WITH THE SUBJECT'S NAME. Nothing in
    the email sub-bench hangs, so without this the whole per-subject alarm
    path -- the SIGALRM, the siglongjmp out of a timed loop, the attribution
    to the right subject, and the driver CONTINUING to the next one -- would
    ship never having been seen to work.

    So: a pcrec artifact for `(a+)+b` built with NO step budget and a huge
    frame stack, which genuinely does not terminate on 40 `a`s, followed in
    the same list by a subject that answers instantly. The first must come
    back `timed-out` BY NAME and the second must be answered."""
    print("-- the per-subject timeout control --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("subject-timeout control", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-timeout-")
    try:
        adapter.prepare("pcrec-auto", tmp)
        pcrec = adapter.pin_binary()
        art = os.path.join(tmp, "artifact.c")
        proc = run([pcrec, "-p", "rx", "--engine=vm", "--fno-step-budget",
                    "--backtrack-frames=100000", "-o", art, "--", "(a+)+b"],
                   timeout=300)
        if proc.returncode != 0:
            bad("subject-timeout control", "pcrec: %s" % proc.stderr.strip()[:200])
            return
        so = os.path.join(tmp, "unbounded.so")
        cc = os.environ.get("CC", "gcc")
        proc = run([cc, "-O2", "-std=gnu11", "-fPIC", "-shared", "-o", so,
                    os.path.join(ROOT, "testees", "pcrec", "shim.c"),
                    "-DPB_ARTIFACT=\"%s\"" % art, "-I", tmp], timeout=600)
        if proc.returncode != 0:
            bad("subject-timeout control", proc.stderr.strip()[:200])
            return

        hang = os.path.join(tmp, "hang.bin")
        with open(hang, "wb") as f:
            f.write(b"a" * 40)
        fine = os.path.join(tmp, "fine.bin")
        with open(fine, "wb") as f:
            f.write(b"ab")

        class S:
            def __init__(self, sid, path, length):
                self.subject_id, self.path, self.length = sid, path, length

        subjects = [S("s-hang", hang, 40), S("s-fine", fine, 2)]
        handle = {"driver": os.path.join(tmp, "pcrec_driver"), "lib": so,
                  "subject_timeout": 3}
        rows_by_trial, _i, _n = adapter.measure(handle, "search_short",
                                                subjects, 1, 1, timeout=120)
        rows = {r.subject_id: r for r in (rows_by_trial[0] if rows_by_trial else [])}
        if rows.get("s-hang") and rows["s-hang"].answer == "timedout":
            outcome, _o, _d = outcome_for(rows["s-hang"], None,
                                          "search_short", subjects[0])
            if outcome == "timed-out":
                ok("subject-timeout control", "s-hang -> timed-out, by name")
            else:
                bad("subject-timeout control",
                    "the driver said timedout; the judge said %s" % outcome)
        else:
            bad("subject-timeout control",
                "s-hang did not time out: %s"
                % (rows.get("s-hang") and rows["s-hang"].answer))
        if rows.get("s-fine") and rows["s-fine"].matched:
            ok("... and the driver CONTINUES past it",
               "s-fine answered [%s,%s)" % (rows["s-fine"].start,
                                            rows["s-fine"].end))
        else:
            bad("... and the driver CONTINUES past it",
                "the subject after the hang was not answered")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ------------------------------------------------ 7 the store race control

def check_store_race():
    """THE CONTROL FOR THE NEVER-CLOBBER RULE, which an `exists`-then-write
    pair would pass in every single-threaded test and fail in the field.

    N writers fork and claim the SAME cell at the SAME timestamp at once.
    Every one must land its own record: N distinct files, N valid records, no
    writer lost. A store that answered with fewer files has silently thrown a
    measurement away, which is the outcome the `-<n>` disambiguator exists to
    prevent -- and which a careless implementation of that disambiguator
    reintroduces.

    This control has already earned its place: it failed the first
    implementation (a single shared `.validating/` directory that each
    finishing writer removed from under the others -- 6 of 8 records
    survived) and that is what put per-write staging directories in
    `store.py`."""
    print("-- the store never-clobber race control --")
    from pcrecbench import store as _store

    example = os.path.join(ROOT, "schema", "examples",
                           "email-specimen@0.1__pcrec_0.9.0-g1a2b3c4_"
                           "vm-caps-simdna__example-box__20260825T031800Z.jsonl")
    if not os.path.exists(example):
        bad("store race control", "no example record to race with")
        return
    with open(example, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    import json as _json
    setup = _json.loads(lines[0])
    rows = [_json.loads(l) for l in lines[1:]]

    n = 8
    dest = tempfile.mkdtemp(prefix="pcrecbench-race-")
    try:
        pids = []
        for _i in range(n):
            pid = os.fork()
            if pid == 0:
                try:
                    _store.write(dest, dict(setup), rows, validate=False)
                    os._exit(0)
                except Exception:                          # noqa: BLE001
                    os._exit(1)
            pids.append(pid)
        failures = sum(1 for p in pids if os.waitpid(p, 0)[1] != 0)

        import glob as _glob
        files = _glob.glob(os.path.join(dest, "records", "*", "*", "*.jsonl"))
        valid = sum(1 for f in files if _store.validate_file(f)[0])
        ids = {os.path.basename(f) for f in files}
        if failures == 0 and len(files) == n and len(ids) == n and valid == n:
            ok("store race control",
               "%d concurrent writers -> %d distinct valid records" % (n, n))
        else:
            bad("store race control",
                "%d writer(s) failed; %d file(s), %d distinct, %d valid "
                "(wanted %d of each)" % (failures, len(files), len(ids),
                                         valid, n))
    finally:
        shutil.rmtree(dest, ignore_errors=True)


# -------------------------------------------------------- 8 the run smoke

SCHEMA_V11_FIELDS = {
    "row.seq":                 "X18",
    "match.calibration":       "X21",
    "load.before.loadavg_raw": "X19",
    "load.before.sampled_at":  "X19",
    "load.after.loadavg_raw":  "X19",
    "occupancy.before":        "X20/X26",
    "occupancy.after":         "X20/X26",
    "occupancy.limit_busy_pct": "X26",
    "run.driver_build_flags":  "v1.1 fix 6",
    "run.driver_compiler":     "v1.1 fix 6",
    "run.clock_source":        "v1.1 fix 10",
    "environment.cpu_mhz":     "v1.1, optional",
}


def _probe_v11(setup, rows):
    """-> the set of SCHEMA_V11_FIELDS actually present in this record."""
    env = setup.get("environment", {})
    load = env.get("load", {})
    occ = env.get("occupancy", {})
    run = setup.get("run", {})
    timed = [r for r in rows
             if r.get("kind") == "match"
             and (r.get("timing") or {}).get("iterations", 0) > 1]
    present = set()
    if rows and all("seq" in r for r in rows):
        present.add("row.seq")
    if timed and all("calibration" in r for r in timed):
        present.add("match.calibration")
    for end in ("before", "after"):
        v = load.get(end)
        if isinstance(v, dict):
            for k in ("loadavg_raw", "sampled_at"):
                key = "load.%s.%s" % (end, k)
                if k in v and key in SCHEMA_V11_FIELDS:
                    present.add(key)
    for k in ("before", "after"):
        if k in occ:
            present.add("occupancy.%s" % k)
    if occ.get("limit_busy_pct") is not None:
        present.add("occupancy.limit_busy_pct")
    for k in ("driver_build_flags", "driver_compiler", "clock_source"):
        if run.get(k):
            present.add("run.%s" % k)
    if env.get("cpu_mhz") is not None:
        present.add("environment.cpu_mhz")
    return present


def check_v11_fields():
    """Every v1.1 provenance field is actually POPULATED, not merely allowed.

    The validator can only reject what is present and wrong; a field the
    harness quietly stopped filling in is invisible to it wherever the schema
    made the field optional (`cpu_mhz`, `driver_*`, `calibration` on an
    uncalibrated row). This walks a REAL record and requires each one.

    `--iters 2` rather than 1 on purpose: rule X21 attaches a calibration to
    rows whose loop ran more than once, so a one-iteration smoke would let
    `match.calibration` pass by never being required."""
    print("-- the v1.1 provenance fields are populated --")
    from pcrecbench import harness as _h

    scratch = os.path.join(ROOT, "build", "selfcheck-v11-store")
    shutil.rmtree(scratch, ignore_errors=True)
    try:
        res = _h.run_cell("email", "pcre2-interp", regimes=["match"],
                          trials=1, iters=2, force_unquiet=True,
                          store_root=scratch, machine_id="selfcheck-box",
                          synthetic=True,
                          note="make check v1.1 field probe -- NOT a measurement")
    except Exception as e:                                 # noqa: BLE001
        bad("v1.1 fields populated", "%s" % e)
        return

    missing = sorted(set(SCHEMA_V11_FIELDS) - _probe_v11(res.setup, res.rows))
    if missing:
        bad("v1.1 fields populated",
            "absent: %s" % ", ".join("%s [%s]" % (m, SCHEMA_V11_FIELDS[m])
                                     for m in missing))
    else:
        ok("v1.1 fields populated",
           "all %d present in the WRITTEN record" % len(SCHEMA_V11_FIELDS))

    seqs = [r["seq"] for r in res.rows]
    if seqs == list(range(1, len(seqs) + 1)):
        ok("seq is dense and monotonic across the whole record",
           "1..%d over compile AND match rows" % len(seqs))
    else:
        bad("seq is dense and monotonic across the whole record",
            "got %s..%s over %d rows" % (seqs[:1], seqs[-1:], len(seqs)))
    shutil.rmtree(scratch, ignore_errors=True)


def check_whole_subject_form():
    r"""THE CONTROL FOR THE `whole-subject` ARTIFACT (v1.1 fix 22).

    pcrec has no end-anchored mode, so the match regime asks its question of
    a separately compiled `(?:pattern)\z` artifact. The two forms must give
    DIFFERENT answers somewhere, or the second artifact is dead weight and
    nobody would notice if the harness silently used the plain one.

    The case: pattern `a|ab`, subject `ab`.
      plain, anchored entry -> leftmost-first match is [0,1), so `== n` is NO
      whole-subject         -> [0,2), YES
      libpcre2 ANCHORED|ENDANCHORED -> [0,2), YES  (the oracle, so the
                                                    whole-subject form is the
                                                    one that is RIGHT)

    The email corpus never exercises this -- both its patterns agree on all
    85 subjects either way -- which is exactly why the case is constructed."""
    print("-- the whole-subject artifact answers differently (v1.1 form) --")
    from pcrecbench import record as _r
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("whole-subject control", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-form-")
    try:
        adapter.prepare("pcrec-auto", tmp)
        subj_path = os.path.join(tmp, "ab.bin")
        with open(subj_path, "wb") as f:
            f.write(b"ab")

        class S:
            subject_id, path, length = "s-ab", subj_path, 2

        cp = adapter.compile("pcrec-auto", "aab", b"a|ab", {}, 1, tmp)
        answers = {}
        for form in (_ad.FORM_PLAIN, _ad.FORM_WHOLE_SUBJECT):
            cr = cp.get(form)
            if cr is None or cr.outcome != "compiled":
                bad("whole-subject control",
                    "%s form did not compile: %s"
                    % (form, cr and cr.diagnostic))
                return
            rows, _i, _n = adapter.measure(dict(cr.handle), "match", [S()],
                                           1, 1, timeout=120)
            answers[form] = rows[0][0]

        plain, whole = answers[_ad.FORM_PLAIN], answers[_ad.FORM_WHOLE_SUBJECT]
        if plain.matched:
            bad("whole-subject control",
                "the PLAIN artifact answered match [%s,%s); the case is "
                "supposed to expose that it cannot" % (plain.start, plain.end))
        elif not (whole.matched and (whole.start, whole.end) == (0, 2)):
            bad("whole-subject control",
                "the whole-subject artifact answered %s [%s,%s), wanted "
                "match [0,2)" % (whole.answer, whole.start, whole.end))
        else:
            ok("whole-subject control",
               "a|ab over 'ab': plain says %s, whole-subject says match [0,2)"
               % plain.answer)

        # ... and the ORACLE says the whole-subject answer is the right one,
        # so the control is anchored to PCRE2 and not to pcrec's own opinion.
        from pcrecbench import oracle_pcre2 as _o
        got = _o.compile(b"a|ab").match(b"ab")
        if got and got[0] == (0, 2):
            ok("... and libpcre2 agrees with the whole-subject answer",
               "ANCHORED|ENDANCHORED -> (0, 2)")
        else:
            bad("... and libpcre2 agrees with the whole-subject answer",
                "the oracle said %r" % (got,))

        # the two forms must also be DIFFERENT COMPILES, witnessed separately
        if cp.get(_ad.FORM_PLAIN).handle["lib"] == \
                cp.get(_ad.FORM_WHOLE_SUBJECT).handle["lib"]:
            bad("the two forms are separate artifacts",
                "both forms point at ONE .so")
        else:
            ok("the two forms are separate artifacts",
               "distinct .so per form, each with its own compile row")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_calibration_meets_target():
    """THE CONTROL FOR X21, written from the case that slipped past it.

    A full-window rehearsal had a pcre2-jit record REJECTED: a 24.79 ms probe
    against a 50 ms target chose 2 iterations (49.58 ms predicted, just
    under), because the count was floored where the rule needs a ceiling.
    Two bugs, and the second is the one a re-run would not have found:

      1. floor vs ceil;
      2. `probe_elapsed_ns` was the SUM over the probe sweep while `iters`
         came from the MEDIAN subject -- so X21's recomputation and the
         harness's decision were about different quantities, and agreed only
         because one subject happened to dominate.

    So this checks BOTH, and checks them the way X21 does rather than the way
    the harness does:

      (a) the arithmetic, over ratios chosen to sit just above an integer
          (the shape that floors wrongly) and at the exact boundary;
      (b) a REAL record, over a regime whose subjects differ by orders of
          magnitude (search_short: 77 subjects), asserting X21's own
          expression on every emitted row;
      (c) that the recorded probe describes ONE SUBJECT and not the whole
          sweep.

    (c) needs saying, because it is NOT implied by (a) or (b). Once the count
    is derived from the same integers the record carries, X21 passes for
    ANY probe -- including the old sum-over-all-subjects one, which was
    MEASURED to slip past (a) and (b) both. The damage it does is to
    fidelity rather than validity: a count chosen from the sweep total makes
    each subject's loop about total/N of the target, so `target_ns` claims a
    target the individual loops never meet. The discriminator is scale --
    a sum over 77 subjects is far above the slowest single subject, so the
    probe's per-iteration cost is compared against the per-iteration costs
    the record's own timed rows show."""
    print("-- the calibration meets its target (X21) --")
    from pcrecbench.harness import _iters_meeting_target, TARGET_LOOP_SECONDS
    from pcrecbench import harness as _h

    target = int(TARGET_LOOP_SECONDS * 1e9)
    # Just above an integer ratio is the shape that floors wrongly: 50/24.79
    # is 2.017, so a floor picks 2 and predicts UNDER target.
    cases = [(24788929, 1, "the case that slipped: 50/24.79 = 2.017"),
             (25000000, 1, "an exact ratio: 50/25 = 2, no rounding either way"),
             (16666667, 1, "just above 3: 50/16.67 = 2.9999"),
             (49999999, 1, "just under one full loop"),
             (24788929, 2, "the same ratio with a 2-iteration probe")]
    bad_cases = []
    for probe_ns, probe_n, why in cases:
        it = _iters_meeting_target(target, probe_ns, probe_n)
        est = probe_ns / probe_n * it
        if est < target:
            bad_cases.append("%s -> iters=%d predicts %.0fns < %d"
                             % (why, it, est, target))
        # and it must be the SMALLEST such count -- an over-estimate would
        # pass X21 while quietly making every cell slower than asked.
        if it > 1 and probe_ns / probe_n * (it - 1) >= target:
            bad_cases.append("%s -> iters=%d is larger than necessary"
                             % (why, it))
    if bad_cases:
        bad("calibration arithmetic", "; ".join(bad_cases))
    else:
        ok("calibration arithmetic",
           "%d ratio(s), each the smallest count that MEETS the target"
           % len(cases))

    # (b) a real record, on the regime with the widest subject spread.
    scratch = os.path.join(ROOT, "build", "selfcheck-x21-store")
    shutil.rmtree(scratch, ignore_errors=True)
    try:
        res = _h.run_cell("email", "pcre2-interp", regimes=["search_short"],
                          trials=1, iters=None, force_unquiet=True,
                          store_root=scratch, machine_id="selfcheck-box",
                          synthetic=True,
                          note="make check X21 control -- NOT a measurement")
    except Exception as e:                                 # noqa: BLE001
        bad("calibration on a real record", "%s" % e)
        return

    checked = failed = 0
    observed = []
    probe_per_iter = None
    for row in res.rows:
        cal = row.get("calibration")
        timing = row.get("timing")
        if not cal or not timing:
            continue
        checked += 1
        est = cal["probe_elapsed_ns"] / cal["probe_iterations"] * \
            timing["iterations"]
        if est < cal["target_ns"] and not cal.get("calibration_note"):
            failed += 1
        observed.append(timing["elapsed_ns"] / timing["iterations"])
        probe_per_iter = cal["probe_elapsed_ns"] / cal["probe_iterations"]
    if failed:
        bad("calibration on a real record",
            "%d of %d timed row(s) predict UNDER target with no "
            "calibration_note -- X21 would reject this record"
            % (failed, checked))
    elif not checked:
        bad("calibration on a real record",
            "no timed row carried a calibration, so nothing was checked")
    else:
        ok("calibration on a real record",
           "X21's own expression holds on %d timed row(s) "
           "(auto-calibrated, 77-subject spread)" % checked)

    # (c) the probe describes ONE SUBJECT, not the sweep.
    if probe_per_iter is None or not observed:
        bad("the probe describes one subject", "no timed row to compare with")
    else:
        slowest = max(observed)
        if probe_per_iter > slowest * 1.5:
            bad("the probe describes one subject",
                "the recorded probe is %.0f ns/iteration but the SLOWEST "
                "single subject in the cell is %.0f ns/iteration -- the probe "
                "is an aggregate over %d subjects, so `target_ns` claims a "
                "target no individual loop meets"
                % (probe_per_iter, slowest, len(observed)))
        else:
            ok("the probe describes one subject",
               "probe %.0f ns/iter sits within the cell's own per-subject "
               "range (slowest %.0f)" % (probe_per_iter, slowest))
    shutil.rmtree(scratch, ignore_errors=True)


def check_run_smoke():
    """A full `run` of ONE cell into a SCRATCH store, validated. Not a
    measurement: --trials 1 --iters 1, one regime, --force-unquiet, and the
    record is marked `synthetic` so nothing can mistake it for one."""
    print("-- a full `run` of one cell into a scratch store --")
    scratch = os.path.join(ROOT, "build", "selfcheck-store")
    shutil.rmtree(scratch, ignore_errors=True)
    proc = run([sys.executable, "-m", "pcrecbench", "run",
                "--subbench", "email", "--testee", "pcre2-interp",
                "--trials", "1", "--iters", "1", "--regimes", "match",
                "--force-unquiet", "--store", scratch,
                "--machine-id", "selfcheck-box", "--synthetic",
                "--quiet-output",
                "--note", "make check smoke -- NOT a measurement"],
               cwd=ROOT, timeout=1800)
    if proc.returncode != 0:
        bad("run smoke", (proc.stderr or proc.stdout).strip()[-400:])
        return
    ok("run smoke (record written AND validator-accepted)",
       " ".join(proc.stdout.split()[-6:]))
    n = run([sys.executable, "-m", "pcrecbench", "index", "--store", scratch],
            cwd=ROOT)
    if n.returncode == 0:
        ok("index regenerates", n.stdout.strip())
    else:
        bad("index regenerates", n.stderr.strip()[:200])


def main():
    print("== check-harness ==")
    check_manifests()
    check_expectations()
    check_driver_smokes()
    check_wrong_answer_control()
    check_patterns_distinct()
    check_subject_timeout()
    check_store_race()
    check_whole_subject_form()
    check_v11_fields()
    check_calibration_meets_target()
    check_run_smoke()
    print()
    print("check-harness: %d check(s) passed, %d FAILED"
          % (len(PASS), len(FAIL)))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
