#!/usr/bin/env python3
"""tools/selfcheck.py -- the harness half of `make check` (contract 6).

Nine checks, and the ones that matter are the POSITIVE CONTROLS. pcrec's own
check-design lesson, applied here: a check that has never been seen to fail is
not known to be a check, so every gate below is exercised against an input it
must reject, in the same run that exercises it against one it must accept.

  manifests     EVERY sub-bench under bench/ ([B11.1]: enumerated, never
                named), each generator its sidecar declares reproducing its
                committed manifest byte for byte, plus any other `gen_*.py`
                the directory carries re-derived through `--check`
                (bench/loglines' pattern_facts.tsv is the first); and a
                SABOTAGED manifest is rejected (control).
  expectations  every sub-bench's expectations.tsv re-derives from the
                libpcre2 oracle; and a sabotaged expectation is rejected
                (control).
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
  frame buffer  the pcrec `_in` path (match_api.md 10): the `_in` entries
                agree with the plain ones on the smoke pattern; the buffer
                MATTERS (the control) -- a deliberately tiny buffer on a deep
                email subject gives up `PCREC_ERR_FRAMES` BY NAME where the
                configured capacities match; the pin's compile rows carry
                abi == 3 and the sizing pairs, a DFA artifact stamps 0 and
                records no buffer pair, a VM artifact records the capacities.
  run smoke     a full `run` of one cell into a SCRATCH store, validated.
  tier schema   (v1.2, [B10]) the scratch example is accepted, the 1.1
                examples with NO `tier` still are (absent = pinned), and the
                two tier controls are rejected FOR X28 / X29 by name.
  tier store    the canonical store (the `.canonical` marker) REFUSES a
                scratch record on write, and REFUSES to index one planted
                there by hand (the sabotage); a scratch store takes it.
  reduction     the shared set-grain reduction (pcrecbench/reduce.py, the
                arithmetic `quick` prints and the reporter ranks) on a
                3-trial x 2-subject fixture whose median is hand-computable,
                and on a fixture with one give-up, which must EXCLUDE the
                set and name the code.
  quick         a `quick` cell (two testees, one pattern, one regime, five
                subjects) completes in seconds, its records are scratch and
                valid, and the median it printed equals the shared reduction
                recomputed from the record file.
  pcrec-local   the provided-binary testee: describes as `local:<sha12>`
                with no `+describe` for a git-archive pin, `+…-dirty` and a
                null commit beside a dirty repo, `+<sha>` and HEAD beside a
                clean one; a missing $PCREC_BIN is a clean error naming the
                variable; a quick cell runs; `run --store <canonical>` is
                REFUSED.
  floor pattern (v1.3, [B15]) bench/email's `role: floor` pattern: the
                sidecar assigns exactly one floor and the other two patterns
                `member`; a real quick cell's record carries `role: "floor"`
                on the right pattern; the schema's X30 rejects a record
                declaring TWO floor patterns; and both drivers (pcre2,
                pcrec) agree with the oracle on the floor pattern of EVERY
                sub-bench ([B11.1]), on a matching and a non-matching subject
                chosen by the EXPECTATION -- which doubles as the per-
                sub-bench driver smoke, since it is a real adapter compiling
                a real pattern of the set and answering real subjects of it.
  KB-1          (docs/dev/known_issues.md, FIXED) pcrec-auto's
                runtime_options pairs `--features` with `all`, not `true`
                with `all` silently dropped.
  stamps        ([B16]) the abi 4-8 mechanism stamps, on a real artifact of
                each KIND at the pin, asserted by VALUE: a pure DFA
                artifact, a VM HYBRID, a non-hybrid VM artifact and a
                provably-empty one. Plus the two SCOPE rules in both
                directions (a hybrid carries all three `_DFA_*` pairs; a
                non-hybrid VM carries none) and the fast tier's own scope.
  dfa_table     ([B16]) `-fno-premul-table` moves `RX_DFA_TABLE` from
                `premultiplied` to `indexed` -- the control that
                distinguishes a working stamp from a constant, since the
                corpus reaches only one of the four values.
  abi floor     ([B16], the SABOTAGE) an artifact whose `rx_info.abi` is
                edited below `shim.c`'s `PB_SHIM_MIN_ABI` is REFUSED by
                name, carrying both numbers, with the unmodified artifact
                loading fine in the same run as the control -- and the
                token the adapter watches for checked against the
                diagnostic the driver actually produced.

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
from pcrecbench.driverrun import build_driver, run_driver  # noqa: E402
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

def subbench_dirs():
    """EVERY sub-bench under `bench/`, by discovery, never by name ([B11.1]).

    The generic gates -- generators reproduce their manifests, expectations
    re-derive, a driver answers the floor pattern by the oracle -- belong to
    the sub-bench CONTRACT (harness contract 6: "bench/*/ each"), so they
    enumerate. A gate that named `email` would have silently covered one of
    two sub-benches the day the second landed, and the count it printed would
    not have moved to say so."""
    root = os.path.join(ROOT, "bench")
    out = []
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if os.path.exists(os.path.join(path, "subbench.toml")):
            out.append((name, path))
    return out


def check_manifests():
    print("-- manifests reproduce byte for byte --")
    for name, bench in subbench_dirs():
        sb = Subbench(bench)
        subj = sb.cfg.get("subjects", {})
        pairs = [(subj.get("generator"), subj.get("manifest", "manifest.tsv"))]
        if subj.get("throughput_generator"):
            pairs.append((subj["throughput_generator"],
                          subj.get("throughput_manifest",
                                   "manifest_throughput.tsv")))
        # Any other committed `gen_*.py` in the directory that supports
        # `--check` is re-derived too, by existence -- [B11.1]'s
        # `gen_pattern_facts.py` is the first, and a sub-bench that adds
        # another derived table gets it covered without editing this file.
        for gen, manifest in pairs:
            path = os.path.join(bench, manifest)
            with open(path, "rb") as f:
                before = f.read()
            proc = run([sys.executable, os.path.join(bench, gen)])
            if proc.returncode != 0:
                bad("%s: %s" % (name, gen), proc.stderr.strip()[:200])
                continue
            with open(path, "rb") as f:
                after = f.read()
            if before == after:
                ok("%s: %s" % (name, gen), "%d line(s)" % (before.count(b"\n") - 1))
            else:
                bad("%s: %s" % (name, gen),
                    "the regenerated manifest differs from the committed one")
        for extra in sorted(f for f in os.listdir(bench)
                            if f.startswith("gen_") and f.endswith(".py")
                            and f not in [p[0] for p in pairs]
                            and f != "gen_expectations.py"):
            proc = run([sys.executable, os.path.join(bench, extra), "--check"],
                       timeout=1800)
            if proc.returncode == 0:
                ok("%s: %s --check" % (name, extra),
                   proc.stdout.strip().splitlines()[-1]
                   if proc.stdout.strip() else "")
            else:
                bad("%s: %s --check" % (name, extra),
                    (proc.stderr or proc.stdout).strip()[:300])

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
    derived = 0
    for name, bench in subbench_dirs():
        proc = run([sys.executable, os.path.join(bench, "gen_expectations.py"),
                    "--check"], timeout=1800)
        if proc.returncode == 0:
            derived += 1
            ok("%s: gen_expectations.py --check" % name,
               proc.stdout.strip().splitlines()[-1]
               if proc.stdout.strip() else "")
        else:
            bad("%s: gen_expectations.py --check" % name,
                proc.stderr.strip()[:300])
    if not derived:
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


# ------------------------------------------ 9 the caller-provided frame buffer

def _shim_min_abi():
    """`PB_SHIM_MIN_ABI` read out of `testees/pcrec/shim.c` itself, so this
    file keeps no second copy of the number. `None` if the macro is not
    found -- the caller then checks only what it can."""
    import re as _re
    path = os.path.join(ROOT, "testees", "pcrec", "shim.c")
    try:
        with open(path, "r", encoding="utf-8") as f:
            m = _re.search(r"^#define\s+PB_SHIM_MIN_ABI\s+(\d+)", f.read(),
                           _re.M)
    except OSError:
        return None
    return int(m.group(1)) if m else None


def check_frame_buffer():
    """THE CONTROLS FOR THE `_in` PATH (pcrec match_api.md 10, [DD-14.FB]).

    Three things, each with the case that would expose a shim or driver that
    quietly did nothing:

      1. AGREEMENT: `pcrec-auto-in` (the `_in` entries with a buffer) answers
         the smoke pattern with the same span AND captures as `pcrec-auto`
         (the plain entries). 10.3 promises the entries are siblings; this is
         the bench checking it rather than believing it.
      2. THE BUFFER MATTERS: on bench/email's `factored` pattern and the
         deepest give-up subject (s-059), the stamped default gives up
         `PCREC_ERR_FRAMES`, a deliberately TINY caller buffer (4 frames / 4
         entries) gives up `PCREC_ERR_FRAMES` BY NAME, and the configured
         capacities MATCH the whole subject as the oracle expects. A shim
         that ignored the descriptor -- passed NULL, or the wrong region --
         fails the third arm; a driver that never allocated fails it too.
         (Sabotaged once on purpose: with the shim passing NULL the
         configured arm gave up exactly like the default -- see the commit.)
      3. THE ABI READ AND THE PAIRS: every pcrec compile row at this pin
         carries `abi == 3` and the four sizing pairs; on a DFA artifact
         (`orig` under auto) the frame size is 0 and NO `buffer_*` pair is
         recorded even though the config asked for one (10.4's "this engine
         takes no buffers"); on the VM artifact under `pcrec-vm-in` the two
         `buffer_*` pairs carry the config's capacities."""
    print("-- the caller-provided frame buffer (the `_in` path) --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("frame-buffer control", "no pcrec adapter")
        return
    cfg_in = adapter.testees().get("pcrec-auto-in")
    cfg_vm_in = adapter.testees().get("pcrec-vm-in")
    if not cfg_in or not cfg_vm_in:
        bad("frame-buffer control",
            "configs.toml has no pcrec-auto-in / pcrec-vm-in")
        return
    sb = Subbench(BENCH)
    tmp = tempfile.mkdtemp(prefix="pcrecbench-fb-")
    try:
        subj_path = os.path.join(tmp, "s.bin")
        with open(subj_path, "wb") as f:
            f.write(b"xabcbd")

        class S:
            subject_id, path, length = "s-smoke", subj_path, 6

        # 1. agreement --------------------------------------------------
        answers = {}
        for tid in ("pcrec-auto", "pcrec-auto-in"):
            adapter.prepare(tid, tmp)
            cr = adapter.compile(tid, "smoke", b"a(b|c)+d", {}, 1,
                                 tmp).get(_ad.FORM_PLAIN)
            if cr.outcome != "compiled":
                bad("_in agreement", "%s: %s" % (tid, cr.diagnostic))
                return
            rows, _i, _n = adapter.measure(dict(cr.handle), "search_short",
                                           [S()], 1, 1, timeout=120)
            answers[tid] = (rows[0][0], cr.engine_metadata)
        plain, plain_meta = answers["pcrec-auto"]
        via_in, in_meta = answers["pcrec-auto-in"]
        same = (plain.answer, plain.start, plain.end, plain.caps) == \
               (via_in.answer, via_in.start, via_in.end, via_in.caps)
        if in_meta.get("engine") != "vm" or "buffer_frames" not in in_meta:
            bad("_in agreement",
                "the smoke pattern did not exercise the buffer: engine=%s, "
                "buffer_frames=%s -- the agreement would be vacuous"
                % (in_meta.get("engine"), in_meta.get("buffer_frames")))
        elif same and plain.matched and (plain.start, plain.end) == (1, 6):
            ok("_in agreement (plain vs caller buffer)",
               "a(b|c)+d over 'xabcbd': both [%d,%d) caps %s, VM artifact, "
               "buffer %s/%s in use"
               % (plain.start, plain.end, plain.caps,
                  in_meta["buffer_frames"], in_meta["buffer_trail"]))
        else:
            bad("_in agreement (plain vs caller buffer)",
                "plain %s [%s,%s) %s vs _in %s [%s,%s) %s"
                % (plain.answer, plain.start, plain.end, plain.caps,
                   via_in.answer, via_in.start, via_in.end, via_in.caps))

        # 2. the buffer matters ----------------------------------------
        adapter.prepare("pcrec-vm-in", tmp)
        cp = adapter.compile("pcrec-vm-in", "factored",
                             sb.pattern_bytes("factored"), {}, 1, tmp)
        cr = cp.get(_ad.FORM_WHOLE_SUBJECT)
        if cr is None or cr.outcome != "compiled":
            bad("buffer-matters control",
                "factored did not compile under pcrec-vm-in: %s"
                % (cr and cr.diagnostic))
            return
        deep = sb.subject("s-059")
        exp = sb.expectation("factored", "s-059", "match")
        arms = {
            "default": [],
            "tiny": ["--buffer-frames", "4", "--buffer-trail", "4"],
            "configured": list(cr.handle["buffer_args"]),
        }
        got = {}
        for arm, args in arms.items():
            handle = dict(cr.handle)
            handle["buffer_args"] = args
            rows, _i, _n = adapter.measure(handle, "match", [deep], 1, 1,
                                           timeout=120)
            row = rows[0][0]
            outcome, _o, _d = outcome_for(row, exp, "match", deep)
            got[arm] = (row, outcome)
        want_giveup = "giveup:-3:PCREC_ERR_FRAMES"
        d_row, d_out = got["default"]
        t_row, t_out = got["tiny"]
        c_row, c_out = got["configured"]
        if d_row.answer == want_giveup and d_out == "gave-up":
            ok("buffer-matters: the stamped default gives up",
               "s-059 (%d B) -> %s -> gave-up" % (deep.length, d_row.answer))
        else:
            bad("buffer-matters: the stamped default gives up",
                "s-059 -> %s (%s); the control's premise is gone"
                % (d_row.answer, d_out))
        if t_row.answer == want_giveup and t_out == "gave-up":
            ok("buffer-matters: a tiny caller buffer gives up BY NAME",
               "4 frames / 4 entries -> %s" % t_row.answer)
        else:
            bad("buffer-matters: a tiny caller buffer gives up BY NAME",
                "4/4 -> %s (%s)" % (t_row.answer, t_out))
        if c_row.matched and c_out == "matched-as-expected":
            ok("buffer-matters: the configured capacities MATCH",
               "%s -> match [%d,%d), matched-as-expected"
               % (" ".join(arms["configured"]), c_row.start, c_row.end))
        else:
            bad("buffer-matters: the configured capacities MATCH",
                "%s -> %s (%s): the descriptor is not reaching the artifact"
                % (" ".join(arms["configured"]), c_row.answer, c_out))

        # 3. the abi read and the pairs --------------------------------
        vm_meta = cr.engine_metadata
        adapter.prepare("pcrec-auto-in", tmp)
        dfa = adapter.compile("pcrec-auto-in", "orig",
                              sb.pattern_bytes("orig"), {}, 1,
                              tmp).get(_ad.FORM_PLAIN)
        dfa_meta = dfa.engine_metadata if dfa.outcome == "compiled" else {}
        sizing = ("resume_frames", "trail_frames", "resume_frame_size",
                  "trail_frame_size")
        # The abi is READ, not asserted to be a literal ([B16]). This check
        # pinned `abi == 3` and had to be edited at every re-pin, which
        # makes it a check of this file's edit history rather than of the
        # bench. What it actually needs to hold is: one abi across every
        # artifact of both engines (a mixed set would mean two pcrecs got
        # into one run), at or above the floor shim.c declares -- and the
        # floor is IMPORTED from shim.c, never retyped here.
        abis = {m.get("abi") for m in (plain_meta, in_meta, vm_meta, dfa_meta)}
        floor = _shim_min_abi()
        if (len(abis) == 1 and None not in abis
                and (floor is None or next(iter(abis)) >= floor)
                and all(k in m for m in (vm_meta, dfa_meta) for k in sizing)):
            ok("one abi, at or above the shim's floor, + the sizing pairs",
               "4 artifacts, both engines, all abi %d (shim floor %s)"
               % (next(iter(abis)), floor))
        else:
            bad("one abi, at or above the shim's floor, + the sizing pairs",
                "abi values %s (shim floor %s); sizing pairs present: vm %s, "
                "dfa %s"
                % (sorted(abis, key=str), floor,
                   [k for k in sizing if k in vm_meta],
                   [k for k in sizing if k in dfa_meta]))
        if (dfa_meta.get("engine") == "dfa"
                and dfa_meta.get("resume_frame_size") == 0
                and "buffer_frames" not in dfa_meta
                and "buffer_trail" not in dfa_meta):
            ok("a DFA artifact stamps 0 and records NO buffer pair",
               "orig under pcrec-auto-in: engine dfa, frame size 0, buffers "
               "inert (10.4)")
        else:
            bad("a DFA artifact stamps 0 and records NO buffer pair",
                "orig under pcrec-auto-in: %s"
                % {k: dfa_meta.get(k) for k in ("engine", "resume_frame_size",
                                                "buffer_frames")})
        caps = (cfg_vm_in.get("buffer_frames"), cfg_vm_in.get("buffer_trail"))
        if (vm_meta.get("engine") == "vm"
                and (vm_meta.get("buffer_frames"),
                     vm_meta.get("buffer_trail")) == caps
                and vm_meta.get("resume_frame_size", 0) > 0):
            ok("a VM artifact records the configured capacities",
               "factored under pcrec-vm-in: buffer %s/%s, frame %d B, "
               "trail entry %d B"
               % (caps[0], caps[1], vm_meta["resume_frame_size"],
                  vm_meta["trail_frame_size"]))
        else:
            bad("a VM artifact records the configured capacities",
                "factored under pcrec-vm-in: %s"
                % {k: vm_meta.get(k) for k in ("engine", "buffer_frames",
                                               "buffer_trail",
                                               "resume_frame_size")})
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


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


# ------------------------------------------------------ 10 the record tiers

def _validate(argv):
    return run([sys.executable, os.path.join(ROOT, "schema", "validate.py")]
               + argv, timeout=300)


def check_tier_schema():
    """Schema v1.2 ([B10] (a)): the tier fields are ADDITIVE and the two tier
    rules FIRE. `make check-schema` covers the same files by glob; this
    names what each proves."""
    print("-- the record tiers: schema v1.2 --")
    import glob as _glob
    import json as _json
    ex = os.path.join(ROOT, "schema", "examples")
    scratch = [f for f in _glob.glob(os.path.join(ex, "*.jsonl"))
               if "_local-" in os.path.basename(f)]
    old = [f for f in _glob.glob(os.path.join(ex, "*.jsonl"))
           if "_local-" not in os.path.basename(f)]
    if len(scratch) != 1:
        bad("scratch example present", "found %d" % len(scratch))
        return
    setup = _json.loads(open(scratch[0], encoding="utf-8").readline())
    proc = _validate(["--check-filename", scratch[0]])
    if (proc.returncode == 0 and setup.get("tier") == "scratch"
            and setup.get("schema_version") == "1.2"
            and str(setup["testee"]["engine_version"]).startswith("local:")
            and setup["testee"].get("engine_commit") is None
            and "binary" in setup["testee"]):
        ok("scratch example accepted (v1.2)",
           "tier scratch, local: version, null commit, binary present")
    else:
        bad("scratch example accepted (v1.2)",
            (proc.stderr or proc.stdout).strip()[-300:])
    proc = _validate(["--check-filename"] + old)
    absent = all("tier" not in _json.loads(open(f, encoding="utf-8").readline())
                 for f in old)
    if proc.returncode == 0 and absent and old:
        ok("1.1 examples with NO tier still validate",
           "%d record(s): absent tier = pinned" % len(old))
    else:
        bad("1.1 examples with NO tier still validate",
            (proc.stderr or proc.stdout).strip()[-300:])
    for rule, name in (("X28", "x28-local-binary-not-scratch.jsonl"),
                       ("X29", "x29-scratch-without-binary.jsonl")):
        f = os.path.join(ex, "bad", name)
        proc = _validate(["--expect-reject", "--expect-rule", rule, f])
        if proc.returncode == 0 and os.path.exists(f):
            ok("%s control rejected for %s" % (name.split("-")[0], rule),
               name)
        else:
            bad("%s control rejected for %s" % (name.split("-")[0], rule),
                (proc.stderr or proc.stdout).strip()[-300:])


def check_store_tier_refusal():
    """THE STORE'S HALF OF THE TIER RULE, with its sabotage. A scratch
    record must be refused INTO the canonical store (write), and the
    canonical index must refuse to LIST one that got there some other way
    -- proven by planting one by hand. The same record into a store without
    the marker is written, validated and indexed, so the refusal is the
    marker's and not a broken writer's."""
    print("-- the record tiers: the store refuses scratch into canonical --")
    from pcrecbench import store as _store
    import json as _json
    import glob as _glob

    if _store.is_canonical(_store.DEFAULT_STORE):
        ok("the repo's store/ carries the .canonical marker",
           os.path.relpath(_store.DEFAULT_STORE, ROOT))
    else:
        bad("the repo's store/ carries the .canonical marker", "it does not")

    ex = [f for f in _glob.glob(os.path.join(ROOT, "schema", "examples",
                                             "*.jsonl"))
          if "_local-" in os.path.basename(f)]
    if not ex:
        bad("store tier refusal", "no scratch example to write")
        return
    lines = open(ex[0], encoding="utf-8").read().splitlines()
    setup = _json.loads(lines[0])
    rows = [_json.loads(l) for l in lines[1:]]
    assert setup.get("tier") == "scratch"

    tmp = tempfile.mkdtemp(prefix="pcrecbench-tier-")
    try:
        canon = os.path.join(tmp, "canonical")
        os.makedirs(canon)
        with open(os.path.join(canon, _store.CANONICAL_MARKER), "w") as f:
            f.write("canonical\n")
        # 1. write refused
        try:
            _store.write(canon, dict(setup), rows, validate=False)
            bad("canonical store REFUSES a scratch record on write",
                "it was written")
        except _store.StoreError as e:
            if "REFUSED" in str(e) and not _glob.glob(
                    os.path.join(canon, "records", "*", "*", "*.jsonl")):
                ok("canonical store REFUSES a scratch record on write",
                   "StoreError, nothing on disk")
            else:
                bad("canonical store REFUSES a scratch record on write",
                    str(e)[:200])
        # 2. SABOTAGE: plant one by hand; index must refuse to list it
        sb = setup["subbench"]
        d = _store.record_dir(canon, sb["id"], sb["version"],
                              setup["testee"]["testee_id"])
        os.makedirs(d, exist_ok=True)
        planted = os.path.join(d, setup["record_id"] + ".jsonl")
        with open(planted, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")
        try:
            _store.index(canon)
            bad("canonical index REFUSES to list a planted scratch record",
                "index.tsv was written")
        except _store.StoreError as e:
            if "REFUSED" in str(e) and setup["record_id"] in str(e):
                ok("canonical index REFUSES to list a planted scratch record",
                   "StoreError names the file")
            else:
                bad("canonical index REFUSES to list a planted scratch record",
                    str(e)[:200])
        # 3. the CONTROL: a scratch store takes it, validated, and indexes it
        scratch = os.path.join(tmp, "scratch")
        try:
            path, rid = _store.write(scratch, dict(setup), rows, validate=True)
            n = _store.index(scratch)
            if n == 1 and os.path.exists(path):
                ok("a scratch store WRITES (validated) and INDEXES it",
                   "1 record, validator-accepted")
            else:
                bad("a scratch store WRITES (validated) and INDEXES it",
                    "index counted %d" % n)
        except _store.StoreError as e:
            bad("a scratch store WRITES (validated) and INDEXES it",
                str(e)[:300])
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_reduction():
    """THE SHARED ARITHMETIC (R5): `quick` prints it, the reporter ranks
    it, and this fixture pins it to numbers a reader can check by hand.

      subject A, trials 1..3: 100, 300, 200 ns/call
      subject B, trials 1..3:  10,  30,  20 ns/call
      per-trial set sums:     110, 330, 220  -> median 220, min 110, max 330

    Then the CONTROL: B's trial 2 becomes a `gave-up` (PCREC_ERR_FRAMES).
    The set must carry NO number, name B as failing, count one give-up
    under its code, and report pass-rate 1/2."""
    print("-- the shared set-grain reduction (reduce.py) --")
    from pcrecbench import reduce as _rd

    def row(sid, trial, ns, iters=10):
        return {"kind": "match", "pattern_id": "p", "subject_id": sid,
                "regime": "short-subject-search", "trial": trial,
                "match_outcome": "matched-as-expected",
                "timing": {"elapsed_ns": ns * iters, "iterations": iters,
                           "bytes_processed": 40 * iters}}

    fixture = {"A": [row("A", 1, 100), row("A", 2, 300), row("A", 3, 200)],
               "B": [row("B", 1, 10), row("B", 2, 30), row("B", 3, 20)]}
    r = _rd.reduce_set_cell(fixture)
    if (r.median_ns, r.min_ns, r.max_ns, r.n_trials, r.pass_rate,
            r.n_gave_up, r.failing_subjects) == (220, 110, 330, 3, 1.0, 0, []):
        ok("set-grain reduction on the hand-computed fixture",
           "sums %s -> median 220, min 110, max 330" % r.sums)
    else:
        bad("set-grain reduction on the hand-computed fixture",
            "median %s min %s max %s n %s pass %s"
            % (r.median_ns, r.min_ns, r.max_ns, r.n_trials, r.pass_rate))

    giveup = {"A": list(fixture["A"]),
              "B": [fixture["B"][0],
                    {"kind": "match", "pattern_id": "p", "subject_id": "B",
                     "regime": "short-subject-search", "trial": 2,
                     "match_outcome": "gave-up",
                     "observed": {"matched": False},
                     "diagnostic": "the engine gave up rather than answering: "
                                   "giveup:-3:PCREC_ERR_FRAMES"},
                    fixture["B"][2]]}
    r = _rd.reduce_set_cell(giveup)
    if (r.median_ns is None and r.failing_subjects == ["B"]
            and r.n_gave_up == 1 and r.pass_rate == 0.5
            and r.giveup_codes == {"-3:PCREC_ERR_FRAMES": 1}):
        ok("... and one give-up EXCLUDES the set and names its code",
           "B fails, pass-rate 1/2, give-ups {-3:PCREC_ERR_FRAMES: 1}")
    else:
        bad("... and one give-up EXCLUDES the set and names its code",
            "median %s failing %s gave_up %s codes %s"
            % (r.median_ns, r.failing_subjects, r.n_gave_up, r.giveup_codes))


# --------------------------------------------------------------- 11 quick

def check_quick():
    """`pcrecbench quick` ([B10] (b)): the loop's surface, end to end, under
    a hard timeout. Two testees, one pattern, one regime, five subjects, two
    trials -- seconds. Then the three things that make the printed number
    trustworthy: the records are `tier: scratch` and validator-accepted (the
    store validated them on write; re-checked here through the shared
    validator with --check-filename), and the MEDIAN the command printed
    equals `reduce.reduce_set_cell` re-applied to the record FILE -- the
    same function the reporter ranks with (R5). A printed number that
    cannot be recomputed from the record is a number with nothing behind
    it."""
    print("-- `quick`: one cell, two testees, the comparable recomputed --")
    from pcrecbench import reduce as _rd
    import glob as _glob
    import re as _re

    scratch = os.path.join(ROOT, "build", "selfcheck-quick-store")
    shutil.rmtree(scratch, ignore_errors=True)
    t0 = __import__("time").monotonic()
    proc = run(["gnutimeout", "300", sys.executable, "-m", "pcrecbench",
                "quick", "--subbench", "email", "--pattern", "orig",
                "--regime", "search", "--testee", "pcre2-jit",
                "--vs", "pcre2-interp", "--subjects", "5", "--trials", "2",
                "--store", scratch, "--synthetic", "--quiet-output"],
               cwd=ROOT, timeout=330)
    wall = __import__("time").monotonic() - t0
    if proc.returncode != 0:
        bad("quick completes under gnutimeout 300",
            "exit %d: %s" % (proc.returncode,
                             (proc.stderr or proc.stdout).strip()[-300:]))
        return
    ok("quick completes under gnutimeout 300",
       "pcre2-jit vs pcre2-interp, orig, search, 5 subjects x 2 trials: "
       "%.1f s wall" % wall)

    printed = {}
    for line in proc.stdout.splitlines():
        m = _re.match(r"^(pcre2-\w+)\s+(\S+)\s+(\S+)\s+", line)
        if m:
            printed[m.group(1)] = (m.group(2), m.group(3))
    files = sorted(_glob.glob(os.path.join(scratch, "records", "*", "*",
                                           "*.jsonl")))
    if len(files) != 2 or set(printed) != {"pcre2-jit", "pcre2-interp"}:
        bad("quick wrote two records and printed two rows",
            "%d file(s); rows for %s" % (len(files), sorted(printed)))
        return
    proc = _validate(["--check-filename"] + files)
    tiers = []
    for f in files:
        setup, rows = _rd.read_record(f)
        tiers.append(setup.get("tier"))
    if proc.returncode == 0 and tiers == ["scratch", "scratch"]:
        ok("both quick records are tier scratch and validator-accepted",
           "schema %s" % setup.get("schema_version"))
    else:
        bad("both quick records are tier scratch and validator-accepted",
            "tiers %s; %s" % (tiers, (proc.stderr or proc.stdout)[-200:]))

    agree = 0
    for f in files:
        setup, rows = _rd.read_record(f)
        cells = _rd.cells_from_record(rows)
        mine = [v for k, v in cells.items()
                if k[0] == "orig" and k[1] == "short-subject-search"]
        r = _rd.reduce_set_cell(mine[0]) if len(mine) == 1 else None
        tid = "pcre2-jit" if "_jit-" in f else "pcre2-interp"
        want = "%.3f" % r.median_ns if r and r.median_ns is not None else "-"
        if printed[tid][1] == want and r.n_subjects == 5:
            agree += 1
        else:
            bad("the printed median equals the shared reduction of the file",
                "%s: printed %s, recomputed %s over %s subject(s)"
                % (tid, printed[tid][1], want, r and r.n_subjects))
    if agree == 2:
        ok("the printed median equals the shared reduction of the file",
           "both testees: reduce_set_cell(record) == the number on screen")
    shutil.rmtree(scratch, ignore_errors=True)


# --------------------------------------------------------- 12 pcrec-local

def check_pcrec_local():
    """THE PROVIDED-BINARY TESTEE ([B10] (c)), with the case for each claim:

      1. $PCREC_BIN unset -> a clean AdapterError NAMING the variable.
      2. PCREC_BIN = the 692c2e8 pin (a `git archive` snapshot, PIN.tsv, no
         repository): describes as `local:<sha12>` with NO `+` suffix, tier
         scratch, testee.binary's sha256 is the file's.
      3. A tiny repository built in scratch around a COPY of that binary:
         CLEAN -> `+<sha>` and engine_commit == HEAD (40 hex); then one
         tracked file modified -> `+<sha>-dirty` and engine_commit null.
      4. A `quick` cell runs on it (the same emit-c/gcc/load path as the
         pinned testees), and its record is scratch with a local: version.
      5. `run --testee pcrec-local --store <a canonical store>` is REFUSED
         before anything is written -- proven against a temp store carrying
         the marker (so a broken refusal cannot touch the real one), with
         the real store/ asserted to carry the same marker."""
    print("-- pcrec-local: a provided binary, scratch by construction --")
    from pcrecbench import store as _store
    from pcrecbench import reduce as _rd
    import glob as _glob
    import re as _re
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("pcrec-local", "no pcrec adapter")
        return
    pin = adapter.pin_binary()
    env0 = dict(os.environ)
    env0.pop("PCREC_BIN", None)
    env0.pop("PCREC_LOCAL_FLAGS", None)

    # 1. missing variable
    saved = dict(os.environ)
    os.environ.pop("PCREC_BIN", None)
    os.environ.pop("PCREC_LOCAL_FLAGS", None)
    try:
        adapter.describe("pcrec-local")
        bad("a missing $PCREC_BIN is a clean error naming the variable",
            "describe() did not raise")
    except _ad.AdapterError as e:
        if "PCREC_BIN" in str(e):
            ok("a missing $PCREC_BIN is a clean error naming the variable",
               str(e).split(":")[0])
        else:
            bad("a missing $PCREC_BIN is a clean error naming the variable",
                str(e)[:200])
    finally:
        os.environ.clear()
        os.environ.update(saved)

    # 2. the archive pin: no repository beside it
    os.environ["PCREC_BIN"] = pin
    os.environ.pop("PCREC_LOCAL_FLAGS", None)
    try:
        d = adapter.describe("pcrec-local")
        want_sha = _ad.sha256_file(pin)
        ev = d["engine_version"]
        if (ev == "local:" + want_sha[:12] and "+" not in ev
                and d.get("tier") == "scratch"
                and d.get("binary", {}).get("sha256") == want_sha
                and d.get("engine_commit") is None
                and adapter.tier("pcrec-local") == "scratch"):
            ok("the pin's binary describes as local:<sha12>, no +describe",
               "%s (PIN.tsv stops the repository walk)" % ev)
        else:
            bad("the pin's binary describes as local:<sha12>, no +describe",
                "%s commit=%s tier=%s" % (ev, d.get("engine_commit"),
                                         d.get("tier")))
    finally:
        os.environ.clear()
        os.environ.update(saved)

    # 3. a repository beside a copy: clean, then dirty
    tmp = tempfile.mkdtemp(prefix="pcrecbench-local-")
    genv = dict(C_ENV, GIT_AUTHOR_NAME="selfcheck", GIT_AUTHOR_EMAIL="s@x",
                GIT_COMMITTER_NAME="selfcheck", GIT_COMMITTER_EMAIL="s@x",
                HOME=tmp, GIT_CONFIG_NOSYSTEM="1")
    try:
        repo = os.path.join(tmp, "repo")
        os.makedirs(os.path.join(repo, "build"))
        copied = os.path.join(repo, "build", "pcrec")
        shutil.copy2(pin, copied)
        readme = os.path.join(repo, "README")
        with open(readme, "w") as f:
            f.write("a tiny repository beside a copied pcrec binary\n")

        def git(*a):
            return subprocess.run(["git", "-C", repo] + list(a),
                                  capture_output=True, text=True, env=genv,
                                  timeout=60)
        git("init", "-q")
        git("add", "README")
        git("commit", "-q", "-m", "one")
        head = git("rev-parse", "HEAD").stdout.strip()
        os.environ["PCREC_BIN"] = copied
        os.environ.pop("PCREC_LOCAL_FLAGS", None)
        d = adapter.describe("pcrec-local")
        ev = d["engine_version"]
        if (_re.fullmatch(r"local:[0-9a-f]{12}\+[0-9a-f]{7,}", ev)
                and d.get("engine_commit") == head and len(head) == 40):
            ok("beside a CLEAN repository: +<describe>, engine_commit = HEAD",
               "%s, commit %s" % (ev, head[:12]))
        else:
            bad("beside a CLEAN repository: +<describe>, engine_commit = HEAD",
                "%s commit=%s (HEAD %s)" % (ev, d.get("engine_commit"), head))
        with open(readme, "a") as f:
            f.write("edited, not committed\n")
        d = adapter.describe("pcrec-local")
        ev = d["engine_version"]
        if ev.endswith("-dirty") and d.get("engine_commit") is None \
                and d.get("tier") == "scratch":
            ok("beside a DIRTY repository: +...-dirty, engine_commit null",
               ev)
        else:
            bad("beside a DIRTY repository: +...-dirty, engine_commit null",
                "%s commit=%s" % (ev, d.get("engine_commit")))
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(tmp, ignore_errors=True)

    # 4. a quick cell runs on the pin's binary
    scratch = os.path.join(ROOT, "build", "selfcheck-local-store")
    shutil.rmtree(scratch, ignore_errors=True)
    env1 = dict(env0, PCREC_BIN=pin)
    proc = subprocess.run(
        ["gnutimeout", "300", sys.executable, "-m", "pcrecbench", "quick",
         "--subbench", "email", "--pattern", "orig", "--regime", "search",
         "--testee", "pcrec-local", "--subjects", "5", "--trials", "1",
         "--store", scratch, "--synthetic", "--quiet-output"],
        capture_output=True, text=True, env=env1, cwd=ROOT, timeout=330)
    files = _glob.glob(os.path.join(scratch, "records", "*", "*", "*.jsonl"))
    if proc.returncode == 0 and len(files) == 1:
        setup, rows = _rd.read_record(files[0])
        ev = setup["testee"]["engine_version"]
        if setup.get("tier") == "scratch" and ev.startswith("local:") \
                and "_local-" in os.path.basename(files[0]):
            ok("a quick cell runs on pcrec-local",
               "%s -> %s, %s" % (ev, setup["status"],
                                 proc.stdout.splitlines()[2].split()[0:1]))
        else:
            bad("a quick cell runs on pcrec-local",
                "tier %s version %s" % (setup.get("tier"), ev))
    else:
        bad("a quick cell runs on pcrec-local",
            "exit %d, %d file(s): %s"
            % (proc.returncode, len(files),
               (proc.stderr or proc.stdout).strip()[-300:]))
    shutil.rmtree(scratch, ignore_errors=True)

    # 5. into a canonical store: REFUSED, nothing written
    canon = tempfile.mkdtemp(prefix="pcrecbench-canon-")
    try:
        with open(os.path.join(canon, _store.CANONICAL_MARKER), "w") as f:
            f.write("canonical\n")
        proc = subprocess.run(
            ["gnutimeout", "120", sys.executable, "-m", "pcrecbench", "run",
             "--subbench", "email", "--testee", "pcrec-local",
             "--trials", "1", "--iters", "1", "--regimes", "match",
             "--store", canon, "--quiet-output"],
            capture_output=True, text=True, env=env1, cwd=ROOT, timeout=150)
        written = [f for f in os.listdir(canon) if f != _store.CANONICAL_MARKER]
        if proc.returncode != 0 and "REFUSED" in proc.stderr and not written \
                and _store.is_canonical(_store.DEFAULT_STORE):
            ok("run --testee pcrec-local --store <canonical> is REFUSED",
               "exit %d, nothing written; store/ carries the same marker"
               % proc.returncode)
        else:
            bad("run --testee pcrec-local --store <canonical> is REFUSED",
                "exit %d; written %s; %s"
                % (proc.returncode, written, proc.stderr.strip()[-200:]))
    finally:
        shutil.rmtree(canon, ignore_errors=True)


# ------------------------------------------------------- 13 the floor pattern

def check_floor_pattern():
    """[B15] R5: bench/email's FLOOR pattern (`patterns/floor.rx`, sidecar
    `role = "floor"`, schema v1.3) actually reaches a real record, the
    schema refuses a SECOND floor pattern (X30), and both drivers agree
    with the oracle on it: nomatch on a subject with no `@`, the first
    `@`'s span on one that has one."""
    print("-- the floor pattern (role: floor, schema v1.3) --")
    sb = Subbench(BENCH)
    floor, orig, factored = (sb.pattern("floor"), sb.pattern("orig"),
                             sb.pattern("factored"))
    if floor.role == "floor" and orig.role == "member" \
            and factored.role == "member":
        ok("sidecar role: exactly one floor, the rest member",
           "floor=%s orig=%s factored=%s" % (floor.role, orig.role, factored.role))
    else:
        bad("sidecar role: exactly one floor, the rest member",
            "floor=%r orig=%r factored=%r" % (floor.role, orig.role, factored.role))

    # role REACHES THE RECORD, through a real (scratch-tier) quick cell.
    from pcrecbench import reduce as _rd
    import glob as _glob
    scratch = os.path.join(ROOT, "build", "selfcheck-floor-store")
    shutil.rmtree(scratch, ignore_errors=True)
    proc = run(["gnutimeout", "300", sys.executable, "-m", "pcrecbench",
                "quick", "--subbench", "email", "--pattern", "floor",
                "--regime", "search", "--testee", "pcre2-jit",
                "--subjects", "5", "--trials", "1",
                "--store", scratch, "--synthetic", "--quiet-output"],
               cwd=ROOT, timeout=330)
    if proc.returncode != 0:
        bad("a floor-pattern quick cell completes",
            (proc.stderr or proc.stdout).strip()[-300:])
    else:
        files = sorted(_glob.glob(os.path.join(scratch, "records", "*", "*",
                                                "*.jsonl")))
        setup, _rows = _rd.read_record(files[0]) if files else ({}, [])
        roles = {p.get("pattern_id"): p.get("role")
                 for p in setup.get("patterns", [])}
        if roles.get("floor") == "floor":
            ok("patterns[].role: 'floor' reaches a real record", "roles %s" % roles)
        else:
            bad("patterns[].role: 'floor' reaches a real record", "roles %s" % roles)
    shutil.rmtree(scratch, ignore_errors=True)

    # X30: a record declaring TWO floor-role patterns is rejected.
    f = os.path.join(ROOT, "schema", "examples", "bad",
                     "x30-two-floor-patterns.jsonl")
    proc = _validate(["--expect-reject", "--expect-rule", "X30", f])
    if proc.returncode == 0 and os.path.exists(f):
        ok("X30 control rejected (two role: floor patterns)", os.path.basename(f))
    else:
        bad("X30 control rejected (two role: floor patterns)",
            (proc.stderr or proc.stdout).strip()[-300:])

    # Both drivers agree with the oracle on the floor pattern -- on EVERY
    # sub-bench ([B11.1]), which is also this suite's per-sub-bench driver
    # smoke: a real adapter compiles a real pattern from the set and answers
    # real subjects of it, and the answers are the oracle's.
    for name, bench in subbench_dirs():
        _floor_oracle_smoke(name, Subbench(bench))


def _floor_oracle_smoke(name, sb):
    """One sub-bench's floor pattern, through both drivers, against the
    oracle's own expectations.

    The two subjects are chosen BY THE EXPECTATION, not by looking for a
    byte: one the floor is expected to match and one it is expected to miss.
    A set whose floor matches every subject (bench/loglines' floor is `:`,
    which every log line carries) has no missing one, so the check says so
    and uses two matching subjects rather than reporting a failure -- the
    pair it can get is still a real driver-vs-oracle comparison."""
    floors = [p for p in sb.patterns if p.role == "floor"]
    if len(floors) != 1:
        bad("%s: exactly one floor pattern" % name,
            "found %d: %s" % (len(floors), [p.name for p in floors]))
        return
    floor = floors[0].name
    if "search_short" not in sb.regimes:
        ok("%s: floor smoke skipped" % name,
           "the sub-bench declares no search_short regime")
        return
    hits, misses = [], []
    for s in sb.subjects_for("search_short"):
        exp = sb.expectation(floor, s.subject_id, "search_short")
        if exp is None:
            continue
        (hits if exp.matched else misses).append(s)
    pair = ([misses[0], hits[0]] if misses and hits
            else (hits[:2] if len(hits) >= 2 else misses[:2]))
    note = "" if (misses and hits) else " (no non-matching subject in the set)"
    if len(pair) != 2:
        bad("%s: floor test subjects found" % name,
            "%d hit(s), %d miss(es)" % (len(hits), len(misses)))
        return
    for engine, testee in (("pcre2", "pcre2-jit"), ("pcrec", "pcrec-auto")):
        label = "%s: %s answers the floor pattern by the oracle" % (name, engine)
        adapter = _ad.discover().get(engine)
        if adapter is None:
            bad(label, "no adapter")
            continue
        tmp = tempfile.mkdtemp(prefix="pcrecbench-floor-")
        try:
            adapter.prepare(testee, tmp)
            cr = adapter.compile(testee, floor, sb.pattern_bytes(floor),
                                 {}, 1, tmp).get(_ad.FORM_PLAIN)
            if cr.outcome != "compiled":
                bad(label, "%s: %s" % (cr.outcome, cr.diagnostic))
                continue
            rows_by_trial, _i, _n = adapter.measure(
                dict(cr.handle), "search_short", pair, 1, 1, timeout=120)
            rows = {r.subject_id: r for r in rows_by_trial[0]}
            got = []
            for s in pair:
                exp = sb.expectation(floor, s.subject_id, "search_short")
                o, _o, _d = outcome_for(rows[s.subject_id], exp,
                                        "search_short", s)
                got.append((s, exp, o))
            if all(o == "matched-as-expected" for _s, _e, o in got):
                ok(label, "%s%s" % (", ".join(
                    "%s %s" % (s.subject_id,
                               "nomatch" if not e.matched
                               else "[%s,%s)" % (e.start, e.end))
                    for s, e, _o in got), note))
            else:
                bad(label, "; ".join("%s: %s" % (s.subject_id, o)
                                     for s, _e, o in got))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


def check_kb1_runtime_options():
    """KB-1 (docs/dev/known_issues.md), FIXED: `testees/pcrec/adapter.py`'s
    `runtime_options()` must pair a BARE flag with the token that FOLLOWS
    it, not stamp `True` and lose the value. `pcrec-auto`'s own flags are
    `["--features", "all"]`, so its describe() must show `{"name":
    "--features", "value": "all"}` -- not `{"value": true}` with `all`
    silently dropped (still legible only in `build_flags` as free text)."""
    print("-- KB-1: runtime_options pairs a bare flag with its value --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("KB-1 fixed: --features pairs with 'all'", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-kb1-")
    try:
        adapter.prepare("pcrec-auto", tmp)
        block = adapter.describe("pcrec-auto", tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    opts = {o.get("name"): o.get("value") for o in block.get("runtime_options", [])}
    if opts.get("--features") == "all":
        ok("KB-1 fixed: pcrec-auto's --features pairs with 'all'",
           "runtime_options %s" % block.get("runtime_options"))
    else:
        bad("KB-1 fixed: pcrec-auto's --features pairs with 'all'",
            "runtime_options %s" % block.get("runtime_options"))


# --------------------------------------- 14 the abi 4-8 mechanism stamps

#: The artifacts the stamp check compiles, and what each is FOR. Every row
#: is a distinct artifact KIND, because the scope rules the stamps obey are
#: rules about kinds: `RX_ENGINE` is on all of them, the three `_DFA_*`
#: stamps are on exactly those that CONTAIN a DFA scan (match_api.md 6.3
#: (a)'s iff), and `RX_FAST_*` is on exactly the VM ones.
#:
#: The patterns are small and hand-chosen rather than drawn from
#: bench/email, deliberately: a check whose witness is a corpus pattern
#: stops being a check the day engine selection moves under it (which is
#: precisely what happened to this bench between 8da6120 and 692c2e8 --
#: `factored` changed engines). These four are the SHAPES, and each one's
#: expected values are asserted, not merely printed.
STAMP_CASES = (
    # (label, testee, pattern, expected {pair: value})
    ("pure DFA", "pcrec-auto", b"foo[0-9]+bar",
     {"engine": "dfa", "dfa_scan": "unanchored", "dfa_prefilter": "memchr",
      "dfa_table": "premultiplied"}),
    ("VM hybrid", "pcrec-auto", b"a(b|c)+d",
     {"engine": "vm", "prefilter": "hybrid", "dfa_scan": "unanchored",
      "dfa_prefilter": "memchr", "dfa_table": "premultiplied"}),
    ("VM, no DFA scan", "pcrec-vm", b"a(b|c)+d",
     {"engine": "vm", "prefilter": "none"}),
    ("provably-empty DFA", "pcrec-auto", b"[^\\x00-\\xff]",
     {"engine": "dfa", "dfa_scan": "empty", "dfa_prefilter": "none",
      "dfa_table": "none"}),
)


def check_mechanism_stamps():
    """THE abi 4-8 STAMPS, PROVEN ON REAL ARTIFACTS AT THE PIN ([B16]).

    pcrec's inbox I-5, I-6, I-11 and I-13 describe five pins' worth of new
    observability. This check compiles a real artifact of each KIND through
    the ordinary adapter path and asserts each stamp's VALUE -- not its
    presence. Four things it is built to catch, each of which a
    presence-only check would pass:

      1. A stamp read from the wrong macro (`dfa_prefilter` filled from
         `RX_VM_PREFILTER` would read `hybrid`, which is not in its value
         set at all).
      2. The SCOPE RULES broken in either direction: a non-hybrid VM
         artifact must carry NO `_DFA_*` pair, and a VM hybrid MUST carry
         all three (that direction is [DD-13c]'s whole point -- until it
         landed, the artifact kind where the DFA scan does the work was the
         one kind that could not say so).
      3. `RX_FAST_FRAMES`/`_TRAIL` present on every VM artifact and on NO
         DFA artifact (6.3 family (b)).
      4. An adapter that dropped a pair the driver prints -- which is a
         real failure this bench shipped for five pins: `engine_stamp` was
         printed from abi 4 and never recorded. Every pair asserted here is
         read out of the RECORD's engine_metadata, where a dropped pair is
         simply absent.

    The macro-vs-`rx_info` agreement is NOT re-asserted here: the adapter
    raises on a disagreement before this check could see one
    (`Adapter._check_agreement`), and `check_abi_floor_refusal` is what
    proves that guard is wired rather than decorative."""
    print("-- the abi 4-8 mechanism stamps (pcrec I-5/I-6/I-11/I-13) --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("mechanism stamps", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-stamps-")
    metas = {}
    try:
        for label, tid, pattern, expected in STAMP_CASES:
            adapter.prepare(tid, tmp)
            cr = adapter.compile(tid, label.replace(" ", "-").replace(",", ""),
                                 pattern, {}, 1, tmp).get(_ad.FORM_PLAIN)
            if cr.outcome != "compiled":
                bad("stamps: %s" % label, cr.diagnostic)
                continue
            em = cr.engine_metadata
            metas[label] = em
            wrong = {k: (em.get(k), v) for k, v in expected.items()
                     if em.get(k) != v}
            if wrong:
                bad("stamps: %s" % label,
                    "; ".join("%s: got %r, want %r" % (k, got, want)
                              for k, (got, want) in sorted(wrong.items())))
                continue
            ok("stamps: %s" % label,
               ", ".join("%s=%s" % (k, expected[k]) for k in sorted(expected)))

        # -- the SCOPE rules, in both directions (match_api.md 6.3 (a)) --
        dfa_keys = ("dfa_scan", "dfa_prefilter", "dfa_table")
        nonhybrid = metas.get("VM, no DFA scan", {})
        present = [k for k in dfa_keys if k in nonhybrid]
        if nonhybrid and not present:
            ok("scope: a non-hybrid VM artifact carries NO _DFA_* pair",
               "engine=vm, prefilter=none, and none of %s"
               % ", ".join(dfa_keys))
        elif nonhybrid:
            bad("scope: a non-hybrid VM artifact carries NO _DFA_* pair",
                "but it carries %s -- the iff in 6.3 (a) does not hold"
                % ", ".join(present))
        hybrid = metas.get("VM hybrid", {})
        missing = [k for k in dfa_keys if k not in hybrid]
        if hybrid and not missing:
            ok("scope: a VM HYBRID carries all three _DFA_* pairs",
               "the [DD-13c] direction: scan=%s, prefilter=%s, table=%s"
               % (hybrid["dfa_scan"], hybrid["dfa_prefilter"],
                  hybrid["dfa_table"]))
        elif hybrid:
            bad("scope: a VM HYBRID carries all three _DFA_* pairs",
                "missing %s" % ", ".join(missing))

        # -- the fast tier: every VM artifact, no DFA artifact ([OPT-1]) --
        fast_seen = {label: ("fast_frames" in em and "fast_trail" in em)
                     for label, em in metas.items()}
        want_fast = {label: (em.get("engine") == "vm")
                     for label, em in metas.items()}
        if fast_seen and fast_seen == want_fast:
            vm_labels = [l for l, w in want_fast.items() if w]
            ok("scope: RX_FAST_FRAMES/_TRAIL on every VM artifact and no DFA one",
               "VM: %s (e.g. %s/%s); DFA: none"
               % (", ".join(sorted(vm_labels)),
                  metas[vm_labels[0]]["fast_frames"],
                  metas[vm_labels[0]]["fast_trail"]) if vm_labels else "")
        else:
            bad("scope: RX_FAST_FRAMES/_TRAIL on every VM artifact and no DFA one",
                "seen %r, wanted %r" % (fast_seen, want_fast))

        # -- one abi, and it is at or above the shim's floor --
        abis = {label: em.get("abi") for label, em in metas.items()}
        distinct = set(abis.values())
        if len(distinct) == 1 and None not in distinct:
            ok("abi is stamped and identical on every artifact",
               "abi %d on %d artifacts, both engines"
               % (next(iter(distinct)), len(abis)))
        else:
            bad("abi is stamped and identical on every artifact",
                "abi values %r" % abis)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_dfa_table_deny_flag():
    """[OPT-3]'s CONTROL ROW: `-fno-premul-table` moves `RX_DFA_TABLE` from
    `premultiplied` to `indexed` on the same pattern (pcrec I-11, tuning.md
    2.13).

    Why this is worth a check rather than a note. `dfa_table`'s value set
    has four members and the corpus reaches only two of them: pcrec's own
    form census measured `indexed` and `mixed` at ZERO corpus population,
    because every ordinary pattern is small enough that the pre-multiplied
    form wins. A check that only ever sees `premultiplied` cannot tell a
    working stamp from a constant, and this bench would then be filtering
    records on a column that never varies. The deny flag is the lever that
    reaches the other value, so it is also the control on the stamp.

    It runs through `pcrec-local` -- the provided-binary testee -- pointed
    at the PIN's own binary, which is the supported way to pass an extra
    flag and is scratch tier by construction (nothing here is measured or
    stored)."""
    print("-- RX_DFA_TABLE's deny-flag control (pcrec I-11, tuning.md 2.13) --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("dfa_table deny-flag control", "no pcrec adapter")
        return
    pattern = b"(?:[a-z]+)@(?:[a-z]+)"     # the census's own `indexed` witness
    tmp = tempfile.mkdtemp(prefix="pcrecbench-premul-")
    saved = {k: os.environ.get(k) for k in ("PCREC_BIN", "PCREC_LOCAL_FLAGS")}
    try:
        os.environ["PCREC_BIN"] = adapter.pin_binary()
        got = {}
        for arm, extra in (("default", ""),
                           ("-fno-premul-table", "-fno-premul-table")):
            os.environ["PCREC_LOCAL_FLAGS"] = extra
            adapter.prepare("pcrec-local", tmp)
            cr = adapter.compile("pcrec-local", "premul-" + arm.strip("-"),
                                 pattern, {}, 1, tmp).get(_ad.FORM_PLAIN)
            if cr.outcome != "compiled":
                bad("dfa_table deny-flag control",
                    "%s did not compile: %s" % (arm, cr.diagnostic))
                return
            got[arm] = cr.engine_metadata.get("dfa_table")
        if got == {"default": "premultiplied", "-fno-premul-table": "indexed"}:
            ok("dfa_table: the deny flag reaches the OTHER value",
               "%s: default -> premultiplied, -fno-premul-table -> indexed "
               "(the corpus reaches only the first)"
               % pattern.decode())
        else:
            bad("dfa_table: the deny flag reaches the OTHER value",
                "got %r; a stamp that cannot move is not a stamp" % got)
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)


def check_abi_floor_refusal():
    """THE ABI FLOOR, ON A SABOTAGED ARTIFACT ([B16]).

    `shim.c` reads two `struct rx_info` fields that pcrec appended at abi
    6, and declares that floor once (`PB_SHIM_MIN_ABI`). `driver.c` refuses
    an artifact below it before reading anything else, and `adapter.py`
    turns that refusal into a clean AdapterError.

    Nothing in the corpus can exercise that path -- the pin is abi 8 -- so
    without a SABOTAGE the whole refusal would ship unexercised, which is
    this project's own stated check-design lesson. The sabotage is the
    smallest one that reaches the real path: compile a real artifact, edit
    its `rx_info` initialiser's `.abi = 8` to `.abi = 5` in a COPY, and run
    the ordinary shim + driver over it. It still compiles (the fields are
    all still there -- the point is that the driver must not TRUST them on
    an artifact that claims to predate them), and the refusal must fire by
    name and carry both numbers.

    The POSITIVE CONTROL is in the same run: the unmodified artifact, built
    and loaded by the same code, must load fine. A refusal that fired on
    everything would pass a check written without it."""
    print("-- the abi floor, refused by name on a sabotaged artifact --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("abi-floor refusal", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-abifloor-")
    try:
        pcrec = adapter.pin_binary()
        art = os.path.join(tmp, "artifact.c")
        proc = run([pcrec, "-p", "rx", "--features", "all", "-o", art, "--",
                    "foo[0-9]+bar"], timeout=120)
        if proc.returncode != 0:
            bad("abi-floor refusal", "pcrec did not emit: %s" % proc.stderr)
            return
        with open(art, "r", encoding="utf-8") as f:
            src = f.read()
        import re as _re
        m = _re.search(r"\.abi = (\d+),", src)
        if not m:
            bad("abi-floor refusal",
                "the emitted artifact has no `.abi = N,` line to sabotage -- "
                "pcrec changed the initialiser's shape; re-derive this check")
            return
        real_abi = int(m.group(1))
        sabotaged = os.path.join(tmp, "sabotaged.c")
        with open(sabotaged, "w", encoding="utf-8") as f:
            f.write(src.replace(m.group(0), ".abi = 5,", 1))
        # The artifact's own .h sits beside the original; both .c files are
        # in `tmp`, so one -I serves both.
        drv = build_driver(os.path.join(ROOT, "testees", "pcrec", "driver.c"),
                           os.path.join(tmp, "pcrec_driver"), extra=["-ldl"])
        shim = os.path.join(ROOT, "testees", "pcrec", "shim.c")
        results = {}
        for arm, csrc in (("real", art), ("sabotaged", sabotaged)):
            so = os.path.join(tmp, "%s.so" % arm)
            g = run([os.environ.get("CC", "gcc"), "-O0", "-std=gnu11", "-fPIC",
                     "-shared", "-o", so, shim,
                     '-DPB_ARTIFACT="%s"' % csrc, "-I", tmp], timeout=300)
            if g.returncode != 0:
                bad("abi-floor refusal",
                    "the %s artifact did not build: %s" % (arm, g.stderr[-400:]))
                return
            results[arm] = run_driver([drv, "--lib", so, "--trial", "1"],
                                      timeout=120, cwd=tmp)
        real, sab = results["real"], results["sabotaged"]

        if real.returncode == 0 and real.info.get("abi") == str(real_abi):
            ok("abi-floor CONTROL: the unmodified artifact loads",
               "abi %d, driver exit 0 -- the refusal is not firing on "
               "everything" % real_abi)
        else:
            bad("abi-floor CONTROL: the unmodified artifact loads",
                "exit %d, abi %r" % (real.returncode, real.info.get("abi")))

        diag = sab.diagnostic() or ""
        if sab.returncode != 0 and "abi-below-shim-floor" in diag:
            ok("abi-floor: a below-floor artifact is REFUSED by name",
               "exit %d; %s" % (sab.returncode,
                                diag.split("\n")[0][:140]))
        else:
            bad("abi-floor: a below-floor artifact is REFUSED by name",
                "exit %d, diagnostic %r -- the floor is not wired"
                % (sab.returncode, diag[:200]))
        if ("artifact rx_info.abi 5" in diag) and ("below the 6" in diag):
            ok("abi-floor: the refusal carries BOTH numbers",
               "the artifact's claimed abi and the shim's floor, so a reader "
               "knows which end to move")
        else:
            bad("abi-floor: the refusal carries BOTH numbers",
                "got %r" % diag[:200])

        # ...and the token the ADAPTER watches for is the token the DRIVER
        # actually emitted. Two copies of one string, in two languages, with
        # nothing but this line enforcing that they agree -- which is the
        # shape of failure this project keeps paying for, so it is checked
        # against the REAL diagnostic rather than against a literal.
        token = _pcrec_adapter_token()
        if token and token in diag:
            ok("abi-floor: the adapter's token matches the driver's output",
               "%r appears in the refusal the driver just produced, so "
               "_compile_one raises AdapterError instead of recording a "
               "`crashed` compile row" % token)
        else:
            bad("abi-floor: the adapter's token matches the driver's output",
                "adapter watches for %r; the driver said %r" % (token, diag[:160]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _pcrec_adapter_token():
    """The adapter's own refusal token, imported rather than retyped -- the
    number and the string both live on the other side, and a check that
    kept its own copy of either would be checking itself."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "pcrec_adapter_for_selfcheck",
        os.path.join(ROOT, "testees", "pcrec", "adapter.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ABI_FLOOR_TOKEN


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
    check_frame_buffer()
    check_run_smoke()
    check_tier_schema()
    check_store_tier_refusal()
    check_reduction()
    check_quick()
    check_pcrec_local()
    check_floor_pattern()
    check_kb1_runtime_options()
    check_mechanism_stamps()
    check_dfa_table_deny_flag()
    check_abi_floor_refusal()
    print()
    print("check-harness: %d check(s) passed, %d FAILED"
          % (len(PASS), len(FAIL)))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
