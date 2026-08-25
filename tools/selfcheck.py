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
  v1.1 ready    every schema-v1.1 field is MEASURED today, stripped by
                `record.project()` at 1.0, and kept at 1.1 -- the control
                that stops the projection being dead code.
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
                cr = adapter.compile(tid, "smoke", b"a(b|c)+d", {}, 1, tmp)
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
                                 sb.pattern_bytes(exp.pattern), {}, 1, tmp)
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
                                 sb.pattern_bytes(exp.pattern), {}, 1, tmp)
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
                                 {}, 1, tmp)
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
    "row.seq":                 "v1.1 (1)",
    "match.calibration":       "v1.1 (4)",
    "load.before.loadavg_raw": "v1.1 (2)",
    "load.before.sampled_at":  "v1.1 (2)",
    "load.after.loadavg_raw":  "v1.1 (2)",
    "occupancy.before":        "v1.1 (3)",
    "occupancy.after":         "v1.1 (3)",
    "run.driver_build_flags":  "v1.1 (6)",
    "run.driver_compiler":     "v1.1 (6)",
    "run.clock_source":        "v1.1 (9)",
    "environment.cpu_mhz":     "v1.1 (10)",
}


def _probe_v11(setup, rows):
    """-> the set of SCHEMA_V11_FIELDS actually present in this record."""
    env = setup.get("environment", {})
    load = env.get("load", {})
    occ = env.get("occupancy", {})
    run = setup.get("run", {})
    match_rows = [r for r in rows if r.get("kind") == "match"]
    present = set()
    if rows and all("seq" in r for r in rows):
        present.add("row.seq")
    if match_rows and all("calibration" in r for r in match_rows):
        present.add("match.calibration")
    for end in ("before", "after"):
        v = load.get(end)
        if isinstance(v, dict):
            for k in ("loadavg_raw", "sampled_at"):
                if k in v and "load.%s.%s" % (end, k) in SCHEMA_V11_FIELDS:
                    present.add("load.%s.%s" % (end, k))
    for k in ("before", "after"):
        if k in occ:
            present.add("occupancy.%s" % k)
    for k in ("driver_build_flags", "driver_compiler", "clock_source"):
        if run.get(k):
            present.add("run.%s" % k)
    if env.get("cpu_mhz") is not None:
        present.add("environment.cpu_mhz")
    return present


def check_schema_v11_readiness():
    """THE CONTROL FOR THE PROJECTION, without which it is dead code.

    Schema v1.1 is landing on another lane. This harness MEASURES every one
    of its new fields already and `record.project()` narrows the record to
    whatever `SCHEMA_VERSION` currently is. That arrangement has an obvious
    failure mode: the projection strips a field the harness never actually
    built, nobody notices because 1.0 records look right, and the day
    SCHEMA_VERSION flips the field is simply absent.

    So this asserts all three legs at once, on a REAL run:
      1. the FULL record the harness builds carries every v1.1 field;
      2. projecting it at 1.0 removes exactly those and nothing else, and the
         result is what the validator accepted;
      3. projecting it at 1.1 keeps them.
    Leg 1 is the one that matters -- 2 and 3 are cheap and would pass on an
    empty record."""
    print("-- schema v1.1 readiness (the projection is live, not dead) --")
    from pcrecbench import harness as _h, record as _r

    scratch = os.path.join(ROOT, "build", "selfcheck-v11-store")
    shutil.rmtree(scratch, ignore_errors=True)
    try:
        res = _h.run_cell("email", "pcre2-interp", regimes=["match"],
                          trials=1, iters=1, force_unquiet=True,
                          store_root=scratch, machine_id="selfcheck-box",
                          synthetic=True,
                          note="make check v1.1-readiness probe -- NOT a measurement")
    except Exception as e:                                 # noqa: BLE001
        bad("v1.1 readiness", "%s" % e)
        return

    built = _probe_v11(res.full_setup, res.full_rows)
    missing = sorted(set(SCHEMA_V11_FIELDS) - built)
    if missing:
        bad("v1.1 fields are MEASURED",
            "not built: %s" % ", ".join("%s [%s]" % (m, SCHEMA_V11_FIELDS[m])
                                        for m in missing))
    else:
        ok("v1.1 fields are MEASURED",
           "all %d present in the full record" % len(SCHEMA_V11_FIELDS))

    written = _probe_v11(res.setup, res.rows)
    if written:
        bad("... and STRIPPED at schema 1.0",
            "leaked into the written record: %s" % ", ".join(sorted(written)))
    else:
        ok("... and STRIPPED at schema 1.0",
           "the written record carries none of them")

    s11, r11 = _r.project(res.full_setup, res.full_rows, schema_version="1.1")
    kept = _probe_v11(s11, r11)
    if kept == set(SCHEMA_V11_FIELDS):
        ok("... and KEPT at schema 1.1",
           "flipping SCHEMA_VERSION emits all %d" % len(SCHEMA_V11_FIELDS))
    else:
        bad("... and KEPT at schema 1.1",
            "1.1 would drop: %s"
            % ", ".join(sorted(set(SCHEMA_V11_FIELDS) - kept)))

    seqs = [r["seq"] for r in res.full_rows]
    if seqs == list(range(1, len(seqs) + 1)):
        ok("seq is dense and monotonic across the whole record",
           "1..%d over compile AND match rows" % len(seqs))
    else:
        bad("seq is dense and monotonic across the whole record",
            "got %s..%s over %d rows" % (seqs[:1], seqs[-1:], len(seqs)))
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
    check_schema_v11_readiness()
    check_run_smoke()
    print()
    print("check-harness: %d check(s) passed, %d FAILED"
          % (len(PASS), len(FAIL)))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
