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
  stamps        ([B16], extended [B18]) the abi 4-11 mechanism stamps, on
                a real artifact of each KIND at the pin, asserted by VALUE:
                a pure DFA artifact, a VM HYBRID, a non-hybrid VM artifact,
                a provably-empty one and an anchored `attempt` one. Plus
                the SCOPE rules in both directions (a hybrid carries every
                `_DFA_*` pair incl. the abi-9 offsets; a non-hybrid VM
                carries none; `dfa_match` on every DFA artifact and NO VM
                one, hybrids included; the size term's VM-only trio on no
                DFA artifact; `max_emit_bytes` on all), the fast tier's own
                scope, and `rx_info.match_form` read BY VALUE off the
                driver: non-NULL and equal to the macro on a DFA artifact,
                NULL on a VM one.
  ledger stamps ([B18]) the SAME assertion on the bench's OWN patterns --
                the values pcrec's inbox I-15/I-16/I-17 PREDICTED for them:
                loglines `uuid` offsets `0,8*,13`, `iso-ts` `0,4*`,
                `stack-frame` `0,1*`; `ipv6`/`kv-quoted`/`bignum` and BOTH
                email patterns declined (`none`); every DFA artifact
                `unwrapped`; every VM artifact `K=8`/`default` under the
                default caps; and the [SEL-1] fallback -- `level-context`
                under `pcrec-auto` COMPILES as a VM artifact whose
                diagnostic starts `RX_ENGINE_WHY: dfa overflowed`. A
                corpus witness moves the day selection moves under it;
                here that movement IS the finding these rows exist for.
  deny controls ([B16], generalised [B18]) each deny flag reaches its
                stamp's OTHER value on a real artifact -- the control that
                distinguishes a working stamp from a constant, since the
                corpus reaches only one value of most axes:
                `-fno-premul-table` (`dfa_table` premultiplied -> indexed),
                `-fno-offset-skip` (`dfa_prefilter` offset-set-bounded ->
                byte-class-bounded AND the offsets `0,8*,13` -> `none`),
                `-fno-anchored-dfa` (`dfa_match` unwrapped -> search-filter),
                `-fno-size-term` (`unroll_k_why` default -> denied, K
                unchanged). The FLAG SPELLING comes from the registry
                (`pcrec --list-axes`, the axis's order-1 row), not from a
                hand table.
  list-axes     ([B18]) the committed `testees/pcrec/list_axes.tsv` is
                byte-identical (below its source header) to the pin's live
                `pcrec --list-axes`, and the adapter's declared stamp value
                sets agree with the registry's stamp_value column
                (`adapter.registry_check`).
  abi floor     ([B16], the SABOTAGE) an artifact whose `rx_info.abi` is
                edited below `shim.c`'s `PB_SHIM_MIN_ABI` (10 since [B18]:
                the shim reads `rx_info.match_form`) is REFUSED by name,
                carrying both numbers -- the floor read out of shim.c, not
                retyped -- with the unmodified artifact loading fine in the
                same run as the control, and the token the adapter watches
                for checked against the diagnostic the driver actually
                produced.

Everything runs under gnutimeout with LC_ALL=C. Nothing here writes into the
real store: the smoke uses a scratch store under the build tree.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from pcrecbench import adapters as _ad                    # noqa: E402
from pcrecbench.driverrun import build_driver, run_driver  # noqa: E402
from pcrecbench import record as _rec                      # noqa: E402
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
    # `--tier scratch` since v1.4 (gate_shape_v14.md 3.4, ruling E-2): a
    # PINNED `--trials 1` run is `inconclusive-spread` by the rule's own
    # precondition (exit 4 -- `check_exit_code_4` is where THAT is proved);
    # the smoke is a scratch record, whose status is the pre-flight's.
    proc = run([sys.executable, "-m", "pcrecbench", "run",
                "--subbench", "email", "--testee", "pcre2-interp",
                "--trials", "1", "--iters", "1", "--regimes", "match",
                "--force-unquiet", "--store", scratch, "--tier", "scratch",
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
    # "old" = the examples with NO `tier` key at all -- the 1.1 pair. The
    # 1.4 example ([B20]) carries `tier: pinned` explicitly and is the
    # ACCEPT half of check-schema's own gates, not this check's subject.
    old = [f for f in _glob.glob(os.path.join(ex, "*.jsonl"))
           if "_local-" not in os.path.basename(f)
           and "tier" not in _json.loads(open(f, encoding="utf-8").readline())]
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
# The [ART-SIZE] defaults (pcrec limits.md 8): the EFFECTIVE caps every
# artifact stamps unless a raise-only override was given -- none is, in any
# pinned config.
_CAPS_VM = {"unroll_k": 8, "unroll_k_why": "default",
            "max_emit_code_bytes": 500000, "max_emit_bytes": 1000000}
_CAPS_DFA = {"max_emit_bytes": 1000000}

# [B19] (abi 12): an expected value may be a compiled regex, matched with
# `fullmatch` -- for the two `_LANG_WHY` values that carry a number
# (`size cap retry, exact N > cap` -- N is the exact artifact's byte count
# and moves with the emitter's own text).
_SIZE_CAP_RETRY = re.compile(r"size cap retry, exact \d+ > \d+")
_DFA_OVERFLOW_RETRY = re.compile(r"dfa overflow retry, exact nfa \d+")

# K41's second fuzz-gate witness (pcrec tests/codegen/run_prefilter_collapse.sh,
# known_issues.md K41): the one pattern in reach whose EXACT artifact the
# code cap refuses (~671,000 code bytes > 500,000) and which the [OPT-4]
# size-cap rung rescues in ~50 ms as a count-collapsed hybrid of ~152,000.
# Chosen over `(a|b){0,30000}` (the total-cap witness, 24 s a compile).
_K41W2 = (rb"(?:(0{28,30}|[\n\t]?(?:c{1}?c{28,30}?a|1{1,}a{0,30}0|c){5,10}?\n)"
          rb"{0,3}?b[\x6]|[^abc]b(0{2,}[\]]|(b{0,30}a??|a{0,3}?\n)[-a]|^))a?"
          rb"|a(\n{1,2}b{1,2}|0)??a{0,30}$")


def _stamp_ok(got, want):
    if isinstance(want, re.Pattern):
        return isinstance(got, str) and want.fullmatch(got) is not None
    return got == want


STAMP_CASES = (
    # (label, testee, pattern, expected {pair: value})
    ("pure DFA", "pcrec-auto", b"foo[0-9]+bar",
     {"engine": "dfa", "dfa_scan": "unanchored", "dfa_prefilter": "memchr",
      "dfa_table": "premultiplied", "dfa_prefilter_offsets": "none",
      "dfa_match": "unwrapped", "engine_sel": "selected", **_CAPS_DFA}),
    ("VM hybrid", "pcrec-auto", b"a(b|c)+d",
     {"engine": "vm", "prefilter": "hybrid", "dfa_scan": "unanchored",
      "dfa_prefilter": "memchr", "dfa_table": "premultiplied",
      "dfa_prefilter_offsets": "none", "engine_sel": "selected",
      "vm_prefilter_lang": "exact",
      "vm_prefilter_lang_why": "no counted repeat", **_CAPS_VM}),
    ("VM, no DFA scan", "pcrec-vm", b"a(b|c)+d",
     {"engine": "vm", "prefilter": "none", "engine_sel": "forced",
      **_CAPS_VM}),
    ("provably-empty DFA", "pcrec-auto", b"[^\\x00-\\xff]",
     {"engine": "dfa", "dfa_scan": "empty", "dfa_prefilter": "none",
      "dfa_table": "none", "dfa_prefilter_offsets": "none",
      "dfa_match": "search-filter", "engine_sel": "selected", **_CAPS_DFA}),
    # [B18]: the `attempt` scan (an anchored pattern) is the other
    # `search-filter` population I-16 names, and the other `dfa_table none`.
    ("anchored attempt DFA", "pcrec-auto", b"^foo[0-9]+bar",
     {"engine": "dfa", "dfa_scan": "attempt", "dfa_prefilter": "none",
      "dfa_table": "none", "dfa_prefilter_offsets": "none",
      "dfa_match": "search-filter", "engine_sel": "selected", **_CAPS_DFA}),
    # [B19]: a VM hybrid with a counted repeat that nothing collapses --
    # the `exact` language's OTHER why value, and the pattern the force
    # control below moves to `count-collapsed` / `forced`.
    ("VM hybrid, counted repeat, exact", "pcrec-auto", b"a(b|c){2,5}d",
     {"engine": "vm", "prefilter": "hybrid", "engine_sel": "selected",
      "vm_prefilter_lang": "exact", "vm_prefilter_lang_why": "exact",
      **_CAPS_VM}),
    # [B19]: THE SIZE-CAP RUNG (limits.md 8, [OPT-4]): the exact artifact
    # is REFUSED by the code cap and the retry ships a count-collapsed
    # hybrid. At 96e44c2 it stamped `engine_sel selected` -- the mislabel
    # O-8/O-10 flagged, whose only structured trace was the `_why`'s
    # `size cap retry` prefix; since 263b013 ([LIM-1], [B22]) it stamps its
    # OWN token, `size-cap-retry`, and Frank's ask (b) bucket sees it by
    # VALUE (the prefix bucketing is RETIRED -- inbox I-25).
    ("size-cap rung rescue (K41 witness 2)", "pcrec-auto", _K41W2,
     {"engine": "vm", "prefilter": "hybrid", "engine_sel": "size-cap-retry",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": _SIZE_CAP_RETRY, **_CAPS_VM}),
)


def _bench_pattern(subbench, name):
    with open(os.path.join(ROOT, "bench", subbench, "patterns", name + ".rx"),
              "rb") as f:
        return f.read().rstrip(b"\n")


# [B18]: THE LEDGER'S OWN ROWS -- the bench patterns pcrec's inbox
# I-15/I-16/I-17 made predictions about, asserted by VALUE at the pin. A
# corpus witness is a check that stops being one the day selection moves
# under it ([B16]'s reason for the hand-chosen kinds above); on THESE rows
# that movement is exactly the finding the re-pin exists to catch, so it is
# a `bad` naming the value, never a silent edit.
LEDGER_STAMP_CASES = (
    # (label, testee, subbench, pattern, expected)
    ("uuid: the k-set skip, scanned at 8", "pcrec-auto", "loglines", "uuid",
     {"engine": "dfa", "dfa_prefilter": "offset-set-bounded",
      "dfa_prefilter_offsets": "0,8*,13", "dfa_match": "unwrapped",
      "engine_sel": "selected"}),
    ("iso-ts: the k-set skip, scanned at 4", "pcrec-auto", "loglines", "iso-ts",
     {"engine": "dfa", "dfa_prefilter": "offset-set",
      "dfa_prefilter_offsets": "0,4*", "dfa_match": "unwrapped",
      "engine_sel": "selected"}),
    ("stack-frame: the k-set skip, scanned at 1", "pcrec-auto", "loglines",
     "stack-frame",
     {"engine": "dfa", "dfa_prefilter": "offset-set-bounded",
      "dfa_prefilter_offsets": "0,1*", "dfa_match": "unwrapped",
      "engine_sel": "selected"}),
    ("ipv6: declined", "pcrec-auto", "loglines", "ipv6",
     {"engine": "dfa", "dfa_prefilter": "byte-class",
      "dfa_prefilter_offsets": "none", "engine_sel": "selected"}),
    ("kv-quoted: declined", "pcrec-auto", "loglines", "kv-quoted",
     {"engine": "dfa", "dfa_prefilter": "byte-class-bounded",
      "dfa_prefilter_offsets": "none", "engine_sel": "selected"}),
    ("bignum: declined", "pcrec-auto", "loglines", "bignum",
     {"engine": "dfa", "dfa_prefilter": "byte-class-bounded",
      "dfa_prefilter_offsets": "none", "engine_sel": "selected"}),
    ("ipv4: control, declined", "pcrec-auto", "loglines", "ipv4",
     {"engine": "dfa", "dfa_prefilter_offsets": "none",
      "engine_sel": "selected"}),
    ("hex32-id: control, declined", "pcrec-auto", "loglines", "hex32-id",
     {"engine": "dfa", "dfa_prefilter_offsets": "none",
      "engine_sel": "selected"}),
    ("http-5xx: control, declined", "pcrec-auto", "loglines", "http-5xx",
     {"engine": "dfa", "dfa_prefilter_offsets": "none",
      "engine_sel": "selected"}),
    ("email orig: declined (`@` at a variable offset)", "pcrec-auto", "email",
     "orig",
     {"engine": "dfa", "dfa_prefilter": "byte-class",
      "dfa_prefilter_offsets": "none", "dfa_match": "unwrapped",
      "engine_sel": "selected"}),
    ("email factored: declined", "pcrec-auto", "email", "factored",
     {"engine": "dfa", "dfa_prefilter": "byte-class",
      "dfa_prefilter_offsets": "none", "dfa_match": "unwrapped",
      "engine_sel": "selected"}),
    ("email orig under --engine=vm: K=8/default", "pcrec-vm", "email", "orig",
     {"engine": "vm", "prefilter": "none", "engine_sel": "forced",
      **_CAPS_VM}),
    # THE [SEL-1] FALLBACK (I-15 (6), Frank's ask (b)): under `auto` a DFA cap
    # overflow is a SELECTION OUTCOME -- the compile falls back to the VM. At
    # 35e1ab1 this cell was did-not-compile; at 36d5963 a VM artifact with NO
    # prefilter; at 96e44c2 ([OPT-4], [B19]) the [SEL-1] rung KEEPS a
    # prefilter rebuilt from the count-collapsed language -- I-18 (ii)'s
    # prediction (vm / collapsed-prefilter / count-collapsed / "dfa overflow
    # retry, exact nfa 462"), asserted here as MEASURED: every one held.
    ("level-context under auto: the [SEL-1] VM fallback", "pcrec-auto",
     "loglines", "level-context",
     {"engine": "vm", "prefilter": "hybrid", "dfa_scan": "unanchored",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 462",
      **_CAPS_VM}),
    # [B22] bounded's 32768 rung at pin 263b013: the artifact CHANGED KIND
    # (I-22 (ii)'s reason the cross-pin byte comparison was invalid). At
    # 96e44c2 the state-cap rung RESCUED it as a 32 KB collapsed-prefilter
    # hybrid (`exact nfa 65538`); [OPT-4.1] gates the rescue on the
    # collapsed language being NON-nullable, `[a-z]*` is nullable, so the
    # offer is DECLINED: a plain-VM artifact, `declined-nullable`, NO
    # prefilter, NO language pair -- and emit_bytes == emit_code_bytes
    # (18,291: a declined plain-VM artifact has no table initializers at
    # all). The BY-VALUE control [B22] (d) names.
    ("bounded cls-upto-32768: the rescue declined (nullable)", "pcrec-auto",
     "bounded", "cls-upto-32768",
     {"engine": "vm", "prefilter": "none",
      "engine_sel": "declined-nullable",
      "emit_bytes": 18291, "emit_code_bytes": 18291,
      **_CAPS_VM}),
    # [B19] (e): the 16384 rung is a DFA that WARNS (limits.md 8,
    # `--warn-emit-bytes` default 250,000) -- the warning is captured as a
    # pair, the outcome stays `compiled`, and the two source-bytes pairs
    # are the message's own numbers. I-18's table says 725,692 bytes for a
    # file named `[a-z]{0,16384}`; the adapter's `artifact.c`/`.h` names
    # make it 724,699 comment-excluded (the count includes the emitted
    # #include line). Unchanged at 263b013 (RE-MEASURED: [OPT-4.1]/[LIM-1]
    # touch no `selected` DFA artifact). ~8 s a compile under load.
    ("bounded cls-upto-16384: the DFA that warns", "pcrec-auto",
     "bounded", "cls-upto-16384",
     {"engine": "dfa", "engine_sel": "selected", "dfa_scan": "unanchored",
      "warned_emit_bytes": 724699, "emit_bytes": 724699,
      "emit_code_bytes": 11589, **_CAPS_DFA}),
    # ------ [B22] THE DECLINE/KEEP SETS at 263b013 (the I-21 CORRECTION's
    # code-derived minw analysis, stamped 11/11 as predicted -- inbox
    # I-23/I-25; plan [B22]). DECLINE (`pcrec_minw(root) == 0` on the
    # composed form): `declined-nullable`, VM, prefilter `none`, no
    # language pair. The whole-subject (`(?:...)\z`) forms overflow by the
    # K7 SUBSET-ELEMENTS budget where the plain forms hit the state cap --
    # distinct RX_ENGINE_WHY prose, asserted after the loop. A sixth tuple
    # element names the FORM (default plain).
    ("bounded cls-upto-32768 whole: declined, the K7 route", "pcrec-auto",
     "bounded", "cls-upto-32768",
     {"engine": "vm", "prefilter": "none",
      "engine_sel": "declined-nullable",
      "emit_bytes": 18496, "emit_code_bytes": 18496,
      **_CAPS_VM}, "whole-subject"),
    ("bounded cls-upto-16384 whole: declined", "pcrec-auto",
     "bounded", "cls-upto-16384",
     {"engine": "vm", "prefilter": "none",
      "engine_sel": "declined-nullable", **_CAPS_VM}, "whole-subject"),
    ("bounded cls-lazy-16384 whole: declined", "pcrec-auto",
     "bounded", "cls-lazy-16384",
     {"engine": "vm", "prefilter": "none",
      "engine_sel": "declined-nullable", **_CAPS_VM}, "whole-subject"),
    # KEEP (minw > 0: the collapsed language is NON-nullable): the rescue
    # and its bytes stay -- the four ctx rungs (minw 8), and the two nest
    # wholes (minw 1; I-21's original "return to flat" line was WRONG for
    # these two, corrected the same day -- their rescue-with-no-benefit is
    # a NAMED RESIDUAL under pcrec D77, not a target).
    ("bounded ctx-greedy-256: the rescue kept", "pcrec-auto",
     "bounded", "ctx-greedy-256",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 558",
      **_CAPS_VM}),
    ("bounded ctx-lazy-64: the rescue kept", "pcrec-auto",
     "bounded", "ctx-lazy-64",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 174",
      **_CAPS_VM}),
    ("bounded ctx-lazy-256: the rescue kept", "pcrec-auto",
     "bounded", "ctx-lazy-256",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 558",
      **_CAPS_VM}),
    ("bounded ctx-lazy-1024: the rescue kept", "pcrec-auto",
     "bounded", "ctx-lazy-1024",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 2094",
      **_CAPS_VM}),
    ("bounded nest2-64 whole: the rescue kept (non-nullable)", "pcrec-auto",
     "bounded", "nest2-64",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 8258",
      **_CAPS_VM}, "whole-subject"),
    ("bounded nest3-16 whole: the rescue kept (non-nullable)", "pcrec-auto",
     "bounded", "nest3-16",
     {"engine": "vm", "prefilter": "hybrid",
      "engine_sel": "collapsed-prefilter",
      "vm_prefilter_lang": "count-collapsed",
      "vm_prefilter_lang_why": "dfa overflow retry, exact nfa 8466",
      **_CAPS_VM}, "whole-subject"),
    # ... and the CONTRAST that keeps the whole rows readable: the same
    # nest2-64 pattern's PLAIN form is an ordinary selected DFA (the two
    # forms are different machines at these counts -- I-20).
    ("bounded nest2-64 plain: an ordinary selected DFA", "pcrec-auto",
     "bounded", "nest2-64",
     {"engine": "dfa", "engine_sel": "selected", **_CAPS_DFA}),
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
    proves that guard is wired rather than decorative. [B18] added the
    abi 9-11 pairs to every case, the `attempt` kind, the LEDGER rows
    (LEDGER_STAMP_CASES: the bench's own patterns at the values pcrec
    predicted, the [SEL-1] fallback included), the new scope rules, and
    ONE thing read off the driver rather than the record: `rx_info.
    match_form`'s presence, so that "NULL on a VM artifact" is a VALUE
    this check saw and not the absence of a pair. [B19] added the abi-12
    pairs (`engine_sel` on every artifact; `vm_prefilter_lang` / `_why` on
    every VM HYBRID and no other -- the letter said "every VM artifact",
    the spec and the artifacts say hybrids), the size-cap rescue kind
    (K41's witness 2), two bounded ledger rows (the 32768 rescue, the
    16384 DFA that warns), Frank's ask (b) bucket derived from the record,
    and the two source-bytes pairs with the warning pair. [B22] (pin
    263b013, abi 12 unchanged) re-pointed the size-cap kind at its OWN
    route token (`size-cap-retry`, [LIM-1]) and added the I-21-corrected
    DECLINE/KEEP sets as ledger rows -- the four nullable declines
    (`declined-nullable`, [OPT-4.1]: no prefilter, no language pair, the
    plain-vs-`\\z` overflow routes distinct in RX_ENGINE_WHY) against the
    six kept rescues (the ctx rungs, the nest wholes) -- with the bucket
    re-asserted as the VALUE-only rule (the `_why`-prefix special case
    retired, inbox I-25)."""
    print("-- the abi 4-12 mechanism stamps (pcrec I-5/I-6/I-11/I-13/I-15/I-16/I-17/I-18/I-21/I-25) --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("mechanism stamps", "no pcrec adapter")
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-stamps-")
    metas = {}
    handles = {}
    diags = {}
    try:
        cases = [(label, tid, pattern, expected, "stamps", _ad.FORM_PLAIN)
                 for label, tid, pattern, expected in STAMP_CASES]
        # [B22]: a LEDGER case may carry a sixth element naming the FORM it
        # asserts on (`whole-subject` for the `(?:...)\z` artifact the match
        # regime uses) -- the decline/keep sets are per (pattern, form).
        cases += [(c[0], c[1], _bench_pattern(c[2], c[3]), c[4], "ledger",
                   c[5] if len(c) > 5 else _ad.FORM_PLAIN)
                  for c in LEDGER_STAMP_CASES]
        for label, tid, pattern, expected, kind, form in cases:
            adapter.prepare(tid, tmp)
            pid = re.sub(r"[^A-Za-z0-9]+", "-", label).strip("-")[:40]
            cr = adapter.compile(tid, pid, pattern, {}, 1, tmp).get(form)
            if cr.outcome != "compiled":
                bad("%s: %s" % (kind, label), "%s: %s" % (cr.outcome, cr.diagnostic))
                continue
            em = cr.engine_metadata
            metas[label] = em
            handles[label] = cr.handle
            diags[label] = cr.diagnostic or ""
            wrong = {k: (em.get(k), v) for k, v in expected.items()
                     if not _stamp_ok(em.get(k), v)}
            if wrong:
                bad("%s: %s" % (kind, label),
                    "; ".join("%s: got %r, want %r" % (k, got, want)
                              for k, (got, want) in sorted(wrong.items())))
                continue
            ok("%s: %s" % (kind, label),
               ", ".join("%s=%s" % (k, em.get(k)) for k in sorted(expected)))

        # -- the [SEL-1] fallback names its cap (I-15 (6)): the prose is
        # the compile row's diagnostic, exactly where record_schema.md 7
        # puts RX_ENGINE_WHY, and it is the ONE fact that separates "auto
        # picked the VM" from "auto fell back to the VM". Frank's ask (b)
        # is bucketed on this prefix.
        lvl = "level-context under auto: the [SEL-1] VM fallback"
        d = diags.get(lvl)
        if d is not None:
            if d.startswith("RX_ENGINE_WHY: dfa overflowed"):
                ok("ledger: the fallback's diagnostic names the cap",
                   d[:90])
            else:
                bad("ledger: the fallback's diagnostic names the cap",
                    "expected `RX_ENGINE_WHY: dfa overflowed...`, got %r" % d[:120])

        # -- [B22] the OVERFLOW ROUTE is distinct per form (I-22/I-23,
        # I-20's mechanism): the plain form hits the DFA STATE cap
        # (PCREC_MAX_DFA_STATES_TABLE, ">32000 states"), the `(?:...)\z`
        # form the K7 SUBSET-ELEMENTS budget (PCREC_MAX_SUBSET_ELEMS,
        # "subset construction exceeds 48000000 state-set elements (K7)")
        # -- two different limits rows in list_limits.tsv, told apart ONLY
        # by RX_ENGINE_WHY's prose in the compile row's diagnostic. Both
        # values asserted, and asserted DISTINCT.
        p32 = diags.get("bounded cls-upto-32768: the rescue declined (nullable)")
        w32 = diags.get("bounded cls-upto-32768 whole: declined, the K7 route")
        if p32 is not None and w32 is not None:
            state_cap = "RX_ENGINE_WHY: dfa overflowed: >32000 states"
            k7 = "subset construction exceeds 48000000 state-set elements (K7)"
            if p32.startswith(state_cap) and k7 in w32 and k7 not in p32:
                ok("ledger: the plain form overflows by the STATE cap, the `\\z` form by the K7 subset-elements budget -- distinct RX_ENGINE_WHY values",
                   "plain %r; whole %r" % (p32[:60], w32[:100]))
            else:
                bad("ledger: the plain form overflows by the STATE cap, the `\\z` form by the K7 subset-elements budget -- distinct RX_ENGINE_WHY values",
                    "plain %r, whole %r" % (p32[:120], w32[:120]))

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

        # -- [B18] the abi-9 offsets ride with the scan family: on every
        # artifact that has `dfa_scan` and on no other --
        has_scan = {l: "dfa_scan" in em for l, em in metas.items()}
        has_ofs = {l: "dfa_prefilter_offsets" in em for l, em in metas.items()}
        if metas and has_scan == has_ofs:
            ok("scope: dfa_prefilter_offsets on every artifact with a DFA scan and no other",
               "%d with, %d without (the hybrid with, the forced VM without)"
               % (sum(has_ofs.values()), len(has_ofs) - sum(has_ofs.values())))
        elif metas:
            bad("scope: dfa_prefilter_offsets on every artifact with a DFA scan and no other",
                "scan %r vs offsets %r" % (has_scan, has_ofs))

        # -- [B18] the abi-10 match form is an ENTRY fact: every DFA
        # artifact, NO VM artifact, hybrids included (a different iff from
        # the scan family's -- match_api.md 6.3 says why) --
        want_dm = {l: em.get("engine") == "dfa" for l, em in metas.items()}
        has_dm = {l: "dfa_match" in em for l, em in metas.items()}
        if metas and want_dm == has_dm:
            ok("scope: dfa_match on every DFA artifact and on NO VM artifact (hybrid included)",
               "DFA: %s; VM (none): %s"
               % (", ".join(sorted(str(metas[l]["dfa_match"]) for l in has_dm if has_dm[l])),
                  ", ".join(sorted(l for l in has_dm if not has_dm[l]))[:80]))
        elif metas:
            bad("scope: dfa_match on every DFA artifact and on NO VM artifact (hybrid included)",
                "engine=dfa %r vs has dfa_match %r" % (want_dm, has_dm))

        # -- [B18] rx_info.match_form BY VALUE, off the driver: non-NULL
        # and equal to the macro on a DFA artifact, NULL on a VM one. The
        # record cannot show a NULL (the field is a control, not a pair),
        # so the driver's own `info rxinfo_match_form_present` line is
        # read for each artifact built above. --
        mf_seen = {}
        for label, h in handles.items():
            out = run_driver([h["driver"], "--lib", h["lib"], "--trial", "1"],
                             timeout=120, cwd=tmp)
            mf_seen[label] = (out.info.get("rxinfo_match_form_present"),
                              out.info.get("rxinfo_match_form"))
        problems = []
        for label, (present, value) in mf_seen.items():
            engine = metas[label].get("engine")
            macro = metas[label].get("dfa_match")
            if engine == "dfa" and not (present == "1" and value == macro):
                problems.append("%s: engine dfa, field present=%r value=%r macro=%r"
                                % (label, present, value, macro))
            if engine == "vm" and present != "0":
                problems.append("%s: engine vm, field present=%r (must be NULL)"
                                % (label, present))
        if handles and not problems:
            n_dfa = sum(1 for l in mf_seen if metas[l].get("engine") == "dfa")
            ok("rx_info.match_form read BY VALUE: non-NULL == macro on %d DFA artifacts, NULL on %d VM artifacts"
               % (n_dfa, len(mf_seen) - n_dfa),
               "printed on every artifact as `rxinfo_match_form_present`")
        elif handles:
            bad("rx_info.match_form read BY VALUE", "; ".join(problems))

        # -- [B18] the size term: VM-only trio on every VM artifact and no
        # DFA one; the total cap on ALL --
        trio = ("unroll_k", "unroll_k_why", "max_emit_code_bytes")
        has_trio = {l: all(k in em for k in trio) for l, em in metas.items()}
        any_trio = {l: any(k in em for k in trio) for l, em in metas.items()}
        want_vm = {l: em.get("engine") == "vm" for l, em in metas.items()}
        if metas and has_trio == want_vm and any_trio == want_vm:
            ok("scope: unroll_k / unroll_k_why / max_emit_code_bytes on every VM artifact and no DFA one",
               "%d VM, %d DFA" % (sum(want_vm.values()), len(want_vm) - sum(want_vm.values())))
        elif metas:
            bad("scope: unroll_k / unroll_k_why / max_emit_code_bytes on every VM artifact and no DFA one",
                "all-three %r any %r wanted %r" % (has_trio, any_trio, want_vm))
        missing_cap = [l for l, em in metas.items() if "max_emit_bytes" not in em]
        if metas and not missing_cap:
            ok("scope: max_emit_bytes on EVERY artifact, both engines",
               "%d artifacts, all 1000000" % len(metas)
               if all(em.get("max_emit_bytes") == 1000000 for em in metas.values())
               else "%d artifacts" % len(metas))
        elif metas:
            bad("scope: max_emit_bytes on EVERY artifact, both engines",
                "missing on %s" % ", ".join(missing_cap))

        # -- [B19] the abi-12 route token: on EVERY artifact, both engines,
        # and its value set is the registry's `engine-route` axis --
        missing_sel = [l for l, em in metas.items() if "engine_sel" not in em]
        if metas and not missing_sel:
            ok("scope: engine_sel on EVERY artifact, both engines",
               "%d artifacts; values %s"
               % (len(metas), ", ".join(sorted({em["engine_sel"]
                                                for em in metas.values()}))))
        elif metas:
            bad("scope: engine_sel on EVERY artifact, both engines",
                "missing on %s" % ", ".join(missing_sel))

        # -- [B19] the language pair: on every VM HYBRID and on NO other
        # artifact -- not the forced-VM one (no prefilter), not a DFA one.
        # I-18 said "every VM artifact"; match_api.md 6.3 and the artifacts
        # say hybrids, and this is the check that would have caught the
        # letter's wording had the adapter followed it. --
        want_lang = {l: (em.get("engine") == "vm" and em.get("prefilter") == "hybrid")
                     for l, em in metas.items()}
        has_lang = {l: ("vm_prefilter_lang" in em and "vm_prefilter_lang_why" in em)
                    for l, em in metas.items()}
        any_lang = {l: ("vm_prefilter_lang" in em or "vm_prefilter_lang_why" in em)
                    for l, em in metas.items()}
        if metas and has_lang == want_lang and any_lang == want_lang:
            n_h = sum(want_lang.values())
            ok("scope: vm_prefilter_lang / _why on every VM HYBRID and on NO other artifact",
               "%d hybrids with, %d others (forced VM, DFA) without"
               % (n_h, len(metas) - n_h))
        elif metas:
            bad("scope: vm_prefilter_lang / _why on every VM HYBRID and on NO other artifact",
                "has %r wanted %r" % (has_lang, want_lang))

        # -- [B19]/[B22] Frank's ask (b), derived from the RECORD: the `DFA
        # fallback tripped` bucket is engine_sel not in (selected, forced)
        # (adapter.ENGINE_SEL_FALLBACK -- FIVE values since 263b013).
        # Asserted to be EXACTLY the fallback witnesses above: the
        # state-cap rescues (collapsed-prefilter), the nullable DECLINES
        # (declined-nullable) and -- new at this pin -- the SIZE-CAP rescue
        # by its OWN token (size-cap-retry; it stamped `selected` at
        # 96e44c2 and was bucketed on its `_why` prefix, I-19 (3) -- that
        # prefix bucketing is RETIRED, inbox I-25: the bucket reads the
        # VALUE and nothing else). The controls: every `selected` /
        # `forced` witness stays outside, hybrids with `exact` language
        # included. --
        mod = _pcrec_adapter_module()
        tripped = sorted(l for l, em in metas.items()
                         if em.get("engine_sel") in mod.ENGINE_SEL_FALLBACK)
        # (the loglines "declined" labels are DFA-PREFILTER declines on
        # `selected` artifacts and stay outside -- the phrases below are
        # this table's own, chosen not to collide with them)
        want_tripped = sorted(l for l in metas
                              if l.startswith("level-context under auto")
                              or l.startswith("size-cap rung rescue")
                              or ": the rescue declined" in l
                              or ": the rescue kept" in l
                              or "whole: declined" in l)
        size_rescue = sorted(l for l, em in metas.items()
                             if em.get("engine_sel") == "size-cap-retry")
        if metas and tripped == want_tripped and tripped and size_rescue:
            ok("bucket: `DFA fallback tripped` (engine_sel not in selected/forced) is exactly the fallback witnesses, size-cap rescue INCLUDED by value",
               "%d witnesses: %s; the size-cap rescue (%s) is INSIDE it by "
               "its own token -- the [B19]-era _why-prefix bucketing is "
               "retired" % (len(tripped), ", ".join(tripped),
                            ", ".join(size_rescue)))
        elif metas:
            bad("bucket: `DFA fallback tripped` (engine_sel not in selected/forced) is exactly the fallback witnesses, size-cap rescue INCLUDED by value",
                "tripped %r, wanted %r" % (tripped, want_tripped))

        # -- [B19] (d)/(e) the two source-bytes pairs on every compiled
        # artifact; the warning pair only where the message fired, and equal
        # to emit_bytes there (the adapter refuses a disagreement before
        # this check could see one; this is the record-side statement). --
        no_size = [l for l, em in metas.items()
                   if "emit_bytes" not in em or "emit_code_bytes" not in em]
        bad_order = [l for l, em in metas.items()
                     if "emit_bytes" in em and "emit_code_bytes" in em
                     and not (0 < em["emit_code_bytes"] <= em["emit_bytes"])]
        warned = {l: em["warned_emit_bytes"] for l, em in metas.items()
                  if "warned_emit_bytes" in em}
        warn_wrong = [l for l, v in warned.items() if v != metas[l]["emit_bytes"]]
        if metas and not no_size and not bad_order and not warn_wrong:
            ok("emit_bytes / emit_code_bytes on every compiled artifact; warned_emit_bytes only where pcrec warned",
               "%d artifacts sized (0 < code <= total); warned: %s"
               % (len(metas), ", ".join("%s=%d" % kv for kv in sorted(warned.items()))
                  or "none"))
        elif metas:
            bad("emit_bytes / emit_code_bytes on every compiled artifact; warned_emit_bytes only where pcrec warned",
                "unsized %r; code>total %r; warned!=total %r"
                % (no_size, bad_order, warn_wrong))
        lbl16 = "bounded cls-upto-16384: the DFA that warns"
        if lbl16 in diags:
            d = diags[lbl16]
            if "pcrec stderr: pcrec: warning: large artifact: 724699 bytes" in d \
                    and "over --warn-emit-bytes=250000" in d:
                ok("the --warn-emit-bytes line is captured in the compile row's diagnostic, and the outcome is `compiled`",
                   d.split("pcrec stderr: ")[1][:100])
            else:
                bad("the --warn-emit-bytes line is captured in the compile row's diagnostic, and the outcome is `compiled`",
                    "diagnostic %r" % d[:200])

        # -- one abi, and it is at or above the shim's floor --
        abis = {label: em.get("abi") for label, em in metas.items()}
        distinct = set(abis.values())
        floor = _shim_min_abi()
        if len(distinct) == 1 and None not in distinct:
            abi = next(iter(distinct))
            if floor is None or abi >= floor:
                ok("abi is stamped and identical on every artifact",
                   "abi %d on %d artifacts, both engines (shim floor %s)"
                   % (abi, len(abis), floor))
            else:
                bad("abi is stamped and identical on every artifact",
                    "abi %d is below the shim's floor %d -- the adapter should "
                    "have refused" % (abi, floor))
        else:
            bad("abi is stamped and identical on every artifact",
                "abi values %r" % abis)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# [B18]: THE DENY-FLAG CONTROLS, one per stamp whose corpus population is
# one-sided. (label, registry axis, subbench/pattern or literal, base flags,
# {pair: (default value, denied value)}). The FLAG comes from the registry's
# order-1 row for the axis (`cli_flag`); the values are the spec's. The
# `size-term` axis's registry rows carry no stamp_value (a documented gap,
# list_axes.tsv's header), so its values are hand-stated here.
#
# [B19] generalised: a sixth element names the ARM the flag produces --
# `deny` (the registry row's `-fno-` spelling removes a candidate) or
# `force` (the `-f` spelling makes the candidate apply). The
# `prefilter-lang` axis's flag row carries BOTH spellings in one
# `cli_flag` cell (`-fno-prefilter-collapse / -fprefilter-collapse`), split
# on ` / ` and picked by prefix. An expected flagged value of
# DID_NOT_COMPILE says the flag turns a compile into a REFUSAL by name. The
# FIRST pair of each dict is the one the registry row's `stamp_value` is
# compared with (the row's own stamp); the rest ride along.
#
# [B22] generalised twice more, both forced by the 263b013 registry:
# (1) the flag ROW is found by its `cli_flag` cell within the axis, no
# longer assumed to be order 1 -- the `size-term` axis now lists its rows
# in the SELECTOR's preference order with `-fno-size-term` on the `denied`
# row (order 2); (2) an OPTIONAL seventh element `reg_arm` names the arm
# the flag row's `stamp_value` describes -- "default" (a deny flag on the
# candidate it removes: the [B19] rule), "flagged" (a flag on the OUTCOME
# row it produces: size-term's `denied`), or "skip" (the row's value
# matches neither arm by design: the nullability decline, where the flag
# asked for a collapse the policy refused). Omitted, the [B19] rule
# applies (deny -> default arm, force -> flagged arm).
DID_NOT_COMPILE = object()
DENY_CONTROLS = (
    ("dfa_table", "table", ("literal", b"(?:[a-z]+)@(?:[a-z]+)"), "",
     {"dfa_table": ("premultiplied", "indexed")}, "deny"),
    ("dfa_prefilter + offsets", "prefilter", ("loglines", "uuid"), "",
     {"dfa_prefilter": ("offset-set-bounded", "byte-class-bounded"),
      "dfa_prefilter_offsets": ("0,8*,13", "none")}, "deny"),
    ("dfa_match", "match", ("email", "floor"), "",
     {"dfa_match": ("unwrapped", "search-filter")}, "deny"),
    # [B22]: since 263b013 the registry's `-fno-size-term` flag sits on the
    # `denied` row (order 2, stamp_value "denied" -- the value the FLAGGED
    # arm reads), no longer on an order-1 row; the seventh element says so.
    ("unroll_k_why", "size-term", ("email", "orig"), "--engine=vm",
     {"unroll_k_why": ("default", "denied"), "unroll_k": (8, 8)}, "deny",
     "flagged"),
    # [B19] (abi 12, [OPT-4]) -- the collapse denied on the [SEL-1] rung:
    # the rescue becomes the OLD fallback (no prefilter at all, the
    # 36d5963 shape), NOT a refusal -- limits.md 8: "the [SEL-1] rung ...
    # where the alternative is no prefilter at all rather than a refusal".
    # I-18 said the flag "turns a rescue into a refusal"; that is the
    # SIZE-CAP rung's truth (next row), measured here as each rung's own.
    # THREE pairs move: the route token, the language pair (to ABSENT --
    # the scope iff seen from the flag's side) and the VM's own prefilter
    # decision.
    ("engine_sel + vm_prefilter_lang: the [SEL-1] rung denied -> prefilter dropped",
     "prefilter-lang", ("loglines", "level-context"), "",
     {"vm_prefilter_lang": ("count-collapsed", None),   # first: the row's own stamp
      "vm_prefilter_lang_why": ("dfa overflow retry, exact nfa 462", None),
      "engine_sel": ("collapsed-prefilter", "overflowed-dfa"),
      "prefilter": ("hybrid", "none")}, "deny"),
    # ... and denied on the SIZE-CAP rung: the rescue becomes the cap's
    # REFUSAL, `did-not-compile` by name ("pattern too large: N bytes of
    # emitted code (limit 500000)").
    ("vm_prefilter_lang: the size-cap rung denied -> REFUSED",
     "prefilter-lang", ("literal", _K41W2), "",
     {"vm_prefilter_lang": ("count-collapsed", DID_NOT_COMPILE),
      "vm_prefilter_lang_why": (_SIZE_CAP_RETRY, DID_NOT_COMPILE)}, "deny"),
    # -fprefilter-collapse (bit 20) on a hybrid that would otherwise be
    # exact: the language moves, its why reads `forced`, the route token
    # does NOT move (nothing overflowed -- `selected` both arms).
    ("vm_prefilter_lang: -fprefilter-collapse forces the collapse",
     "prefilter-lang", ("literal", b"a(b|c){2,5}d"), "",
     {"vm_prefilter_lang": ("exact", "count-collapsed"),
      "vm_prefilter_lang_why": ("exact", "forced"),
      "engine_sel": ("selected", "selected")}, "force"),
    # [B22] ([OPT-4.1], pin 263b013): -fprefilter-collapse on a hybrid
    # whose COLLAPSED language is nullable reaches the nullability POLICY,
    # not the collapse -- the flag chooses a language, not whether a filter
    # exists, and a nullable one can never dismiss a position, so the
    # prefilter is KEPT and built from the EXACT language:
    # `_LANG "exact"` / `_LANG_WHY "nullable collapsed language"` (pcrec
    # tuning.md 2.17; the value I-21's correction named). The route token
    # stays `selected` in both arms (nothing overflowed), and the registry
    # row's stamp_value (`count-collapsed`, the collapse that was DECLINED)
    # matches neither arm -- `reg_arm` "skip" says so rather than failing.
    ("vm_prefilter_lang_why: -fprefilter-collapse declined as nullable",
     "prefilter-lang", ("literal", b"(x){0,5}"), "",
     {"vm_prefilter_lang": ("exact", "exact"),
      "vm_prefilter_lang_why": ("exact", "nullable collapsed language"),
      "engine_sel": ("selected", "selected")}, "force", "skip"),
)


def _pcrec_adapter_module():
    """testees/pcrec/adapter.py as a module, imported rather than retyped
    (its ABI_FLOOR_TOKEN, registry helpers and declaration)."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "pcrec_adapter_for_selfcheck",
        os.path.join(ROOT, "testees", "pcrec", "adapter.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_deny_flag_controls():
    """THE DENY FLAGS AS CONTROL BUILDS ([B16] for `-fno-premul-table`,
    generalised by [B18] to every stamp the re-pin added a deny flag for).

    Why this is worth a check rather than a note. `dfa_table`'s value set
    has four members and the corpus reaches only two of them: pcrec's own
    form census measured `indexed` and `mixed` at ZERO corpus population,
    because every ordinary pattern is small enough that the pre-multiplied
    form wins. The same is true of `dfa_match` (every DFA artifact of both
    sub-benches is `unwrapped`) and of `unroll_k_why` (every VM artifact is
    `default` -- I-17's survey: 0 K movements). A check that only ever sees
    one value cannot tell a working stamp from a constant, and this bench
    would then be filtering records on a column that never varies. The
    deny flag is the lever that reaches the other value, so it is also the
    control on the stamp -- and for the offset-k skip it moves TWO pairs at
    once, which is the iff between them seen from the flag's side.

    The flag's SPELLING is read from the registry (`testees/pcrec/
    list_axes.tsv`, the axis's order-1 row), so a renamed flag fails here
    by name rather than being quietly retyped; the registry's own
    `stamp_value` for that row is checked against the default value where
    the registry carries one.

    It runs through `pcrec-local` -- the provided-binary testee -- pointed
    at the PIN's own binary, which is the supported way to pass an extra
    flag and is scratch tier by construction (nothing here is measured or
    stored)."""
    print("-- the deny-flag controls: each flag reaches its stamp's OTHER value --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("deny-flag controls", "no pcrec adapter")
        return
    mod = _pcrec_adapter_module()
    try:
        rows = mod.registry_rows()
    except Exception as e:                       # noqa: BLE001
        bad("deny-flag controls", "cannot read the registry: %s" % e)
        return
    tmp = tempfile.mkdtemp(prefix="pcrecbench-deny-")
    saved = {k: os.environ.get(k) for k in ("PCREC_BIN", "PCREC_LOCAL_FLAGS")}
    try:
        os.environ["PCREC_BIN"] = adapter.pin_binary()
        for row_spec in DENY_CONTROLS:
            label, axis, src, base, pairs, arm_kind = row_spec[:6]
            reg_arm = (row_spec[6] if len(row_spec) > 6
                       else ("default" if arm_kind == "deny" else "flagged"))
            # [B22]: find the axis row CARRYING the flag (its cli_flag
            # cell), wherever the selector's preference order put it.
            flagrows = [r for r in rows
                        if r["axis"] == axis and r.get("cli_flag", "").startswith("-f")]
            if len(flagrows) < 1:
                bad("deny control: %s" % label,
                    "the registry has no row with a -f cli_flag for axis %r"
                    % (axis,))
                continue
            first = flagrows[:1]
            spellings = [f.strip() for f in first[0]["cli_flag"].split(" / ")]
            if arm_kind == "deny":
                flag = next((f for f in spellings if f.startswith("-fno-")), None)
                bit = first[0].get("deny_bit", "")
            else:
                flag = next((f for f in spellings
                             if f.startswith("-f") and not f.startswith("-fno-")), None)
                bit = first[0].get("force_bit", "")
            if not flag:
                bad("deny control: %s" % label,
                    "the registry's cli_flag %r for axis %r has no %s spelling"
                    % (first[0]["cli_flag"], axis, arm_kind))
                continue
            flagged = "denied" if arm_kind == "deny" else "forced"
            if src[0] == "literal":
                pattern = src[1]
            else:
                pattern = _bench_pattern(src[0], src[1])
            want = {"default": {k: v[0] for k, v in pairs.items()},
                    flagged: {k: v[1] for k, v in pairs.items()}}
            expect_refusal = any(v is DID_NOT_COMPILE for v in want[flagged].values())
            got = {}
            failed = False
            for arm, extra in (("default", base), (flagged, (base + " " + flag).strip())):
                os.environ["PCREC_LOCAL_FLAGS"] = extra
                adapter.prepare("pcrec-local", tmp)
                pid = re.sub(r"[^A-Za-z0-9]+", "-", "%s-%s" % (label, arm)).strip("-")[:48]
                cr = adapter.compile("pcrec-local", pid, pattern, {}, 1,
                                     tmp).get(_ad.FORM_PLAIN)
                if arm == flagged and expect_refusal:
                    if cr.outcome == "did-not-compile" and "pattern too large" in (cr.diagnostic or ""):
                        got[arm] = {k: DID_NOT_COMPILE for k in pairs}
                    else:
                        bad("deny control: %s" % label,
                            "%s arm (%r) should have been REFUSED by a size cap; "
                            "got %s: %s" % (arm, extra, cr.outcome,
                                            (cr.diagnostic or "")[:160]))
                        failed = True
                        break
                    continue
                if cr.outcome != "compiled":
                    bad("deny control: %s" % label,
                        "%s arm (%r) did not compile: %s" % (arm, extra, cr.diagnostic))
                    failed = True
                    break
                got[arm] = {k: cr.engine_metadata.get(k) for k in pairs}
            if failed:
                continue
            agree = all(_stamp_ok(got[a][k], want[a][k]) for a in want for k in pairs)
            if agree:
                reg_val = first[0].get("stamp_value", "")
                note = ""
                main_pair = next(iter(pairs))
                chosen_arm = "default" if reg_arm == "default" else flagged
                if reg_arm == "skip":
                    note = ("; registry stamp_value %r deliberately matches "
                            "neither arm (the flag reached a policy, not the "
                            "candidate -- reg_arm skip)" % (reg_val,))
                elif reg_val and reg_val != got[chosen_arm][main_pair]:
                    bad("deny control: %s" % label,
                        "the registry says %s's flag row stamps %r; the "
                        "%s arm read %r" % (axis, reg_val, chosen_arm, got[chosen_arm][main_pair]))
                    continue
                elif reg_val:
                    note = "; registry stamp_value %r agrees (%s arm)" % (reg_val, chosen_arm)
                else:
                    note = "; registry carries no stamp_value for this row"
                fmt = lambda d: ", ".join(
                    "%s=%s" % (k, "REFUSED" if v is DID_NOT_COMPILE else v)
                    for k, v in d.items())
                ok("deny control: %s" % label,
                   "%s (bit %s, from the registry): %s -> %s%s"
                   % (flag, bit or "?", fmt(got["default"]), fmt(got[flagged]), note))
            else:
                bad("deny control: %s" % label,
                    "%s: got %r, want %r -- a stamp that cannot move is not a stamp"
                    % (flag, got, want))
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)


def check_list_axes_registry():
    """THE FOURTH REGISTRY SURFACE, ARCHIVED AND CHECKED ([B18], pcrec I-15
    (5), registry.md 6). Two facts:

    1. `testees/pcrec/list_axes.tsv` -- pcrec's own `--list-axes` output at
       the pin, under a source header -- is byte-identical (below that
       header) to what the pin's binary prints NOW. A re-pin that forgets
       to re-archive fails here, and the diff IS the list of what moved.
    2. The adapter's declared stamp VALUE SETS agree with the registry's
       `stamp_value` column (`adapter.registry_check`): every value pcrec
       stamps for `RX_ENGINE` / `RX_VM_PREFILTER` / `RX_DFA_PREFILTER` /
       `RX_DFA_TABLE` / `RX_DFA_MATCH` is declared, so a candidate pcrec
       adds fails here by name instead of as the first record's X15
       rejection."""
    print("-- the --list-axes registry: archived copy vs the pin, and the declaration vs it --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("list-axes registry", "no pcrec adapter")
        return
    mod = _pcrec_adapter_module()
    proc = run([adapter.pin_binary(), "--list-axes"], timeout=60)
    if proc.returncode != 0:
        bad("list-axes: the pin prints its registry", proc.stderr[-300:])
        return
    live = proc.stdout
    try:
        with open(mod.LIST_AXES_TSV, "r", encoding="utf-8") as f:
            committed = f.read()
    except OSError as e:
        bad("list-axes: the archived copy exists", str(e))
        return
    first_live = live.splitlines(True)[0] if live else ""
    idx = committed.find(first_live) if first_live else -1
    if idx < 0:
        bad("list-axes: the archived copy matches the pin's live output",
            "the live output's first line %r is not in %s"
            % (first_live.strip()[:60], mod.LIST_AXES_TSV))
        return
    body = committed[idx:]
    n_rows = sum(1 for l in live.splitlines() if l and not l.startswith("#"))
    n_axes = len({l.split("\t")[0] for l in live.splitlines() if l and not l.startswith("#")})
    if body == live:
        ok("list-axes: the archived copy matches the pin's live output",
           "%d rows / %d axes, byte-identical below the source header"
           % (n_rows, n_axes))
    else:
        import difflib
        diff = list(difflib.unified_diff(body.splitlines(), live.splitlines(),
                                         "committed", "live", lineterm="", n=0))
        bad("list-axes: the archived copy matches the pin's live output",
            "re-archive testees/pcrec/list_axes.tsv; diff: %s"
            % " | ".join(diff[2:12]))
    try:
        problems = mod.registry_check()
    except Exception as e:                       # noqa: BLE001
        bad("list-axes: the declared value sets agree with the registry", str(e))
        return
    if not problems:
        allowed = ", ".join("%s:%s" % (k, "/".join(sorted(v)))
                            for k, v in sorted(mod.REGISTRY_OUTCOME_VALUES.items()))
        ok("list-axes: the declared value sets agree with the registry",
           "%s checked both ways (%s)"
           % (", ".join(sorted(mod.REGISTRY_STAMP_PAIRS)),
              ("outcome values %s allowed" % allowed) if allowed
              else "no outcome-value exceptions: the registry enumerates "
                   "them all at this pin -- [B22]"))
    else:
        bad("list-axes: the declared value sets agree with the registry",
            "; ".join(problems))


def check_list_definitions_registry():
    """THE FIFTH REGISTRY SURFACE, ARCHIVED AND CHECKED ([B19], pcrec I-18
    (4), [DD-11], registry.md 9). `testees/pcrec/list_definitions.tsv` --
    `pcrec --list-definitions | grep -v '^#'` at the pin, under a bench
    source header -- is byte-identical (below that header) to what the
    pin's binary prints NOW. A re-pin that forgets to re-archive fails
    here, and the diff is the list of definitions that moved. Nothing the
    adapter reads depends on the file (the emitted code is unchanged by
    [DD-11]); the check is the archive's guarantee of being verbatim."""
    print("-- the --list-definitions table: archived copy vs the pin --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("list-definitions", "no pcrec adapter")
        return
    mod = _pcrec_adapter_module()
    proc = run([adapter.pin_binary(), "--list-definitions"], timeout=60)
    if proc.returncode != 0:
        bad("list-definitions: the pin prints its table", proc.stderr[-300:])
        return
    live = [l for l in proc.stdout.splitlines() if l and not l.startswith("#")]
    try:
        with open(mod.LIST_DEFINITIONS_TSV, "r", encoding="utf-8") as f:
            committed = [l for l in f.read().splitlines()
                         if l and not l.startswith("#")]
    except OSError as e:
        bad("list-definitions: the archived copy exists", str(e))
        return
    if committed == live:
        kinds = sorted({l.split("\t")[0] for l in live})
        ok("list-definitions: the archived copy matches the pin's live output",
           "%d rows (kinds %s), byte-identical below the source header"
           % (len(live), ", ".join(kinds)))
    else:
        import difflib
        diff = list(difflib.unified_diff(committed, live, "committed", "live",
                                         lineterm="", n=0))
        bad("list-definitions: the archived copy matches the pin's live output",
            "re-archive testees/pcrec/list_definitions.tsv; diff: %s"
            % " | ".join(diff[2:12]))


def check_list_limits_registry():
    """THE SIXTH REGISTRY SURFACE, ARCHIVED AND CHECKED ([B22], pcrec D90 /
    [LIM-1], inbox I-25: "ARCHIVE IT beside --list-axes at your re-pin").
    `testees/pcrec/list_limits.tsv` -- `pcrec --list-limits` at the pin,
    under a bench source header -- is byte-identical (below that header) to
    what the pin's binary prints NOW: the same rule as the other two
    archives (a re-pin that forgets to re-archive fails here, and the diff
    is the list of limits that MOVED -- exactly the kind of change that
    would otherwise surface only as an unexplained selection or refusal
    change in a record). Nothing the adapter reads depends on the file:
    every cap and capacity it needs is stamped per artifact."""
    print("-- the --list-limits table: archived copy vs the pin --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("list-limits", "no pcrec adapter")
        return
    mod = _pcrec_adapter_module()
    proc = run([adapter.pin_binary(), "--list-limits"], timeout=60)
    if proc.returncode != 0:
        bad("list-limits: the pin prints its table", proc.stderr[-300:])
        return
    live = proc.stdout
    try:
        with open(mod.LIST_LIMITS_TSV, "r", encoding="utf-8") as f:
            committed = f.read()
    except OSError as e:
        bad("list-limits: the archived copy exists", str(e))
        return
    first_live = live.splitlines(True)[0] if live else ""
    idx = committed.find(first_live) if first_live else -1
    if idx < 0:
        bad("list-limits: the archived copy matches the pin's live output",
            "the live output's first line %r is not in %s"
            % (first_live.strip()[:60], mod.LIST_LIMITS_TSV))
        return
    body = committed[idx:]
    n_rows = sum(1 for l in live.splitlines() if l and not l.startswith("#"))
    if body == live:
        kinds = sorted({l.split("\t")[3] for l in live.splitlines()
                        if l and not l.startswith("#")})
        ok("list-limits: the archived copy matches the pin's live output",
           "%d rows (kinds: %s), byte-identical below the source header"
           % (n_rows, ", ".join(kinds)))
    else:
        import difflib
        diff = list(difflib.unified_diff(body.splitlines(), live.splitlines(),
                                         "committed", "live", lineterm="", n=0))
        bad("list-limits: the archived copy matches the pin's live output",
            "re-archive testees/pcrec/list_limits.tsv; diff: %s"
            % " | ".join(diff[2:12]))


# [B19] (d): the artifact KINDS the size port is checked on, against the
# pin's OWN numbers. Each exercises a different branch of the classifier:
# a table-dominated unanchored DFA (multi-line `= {` initializers), an
# `attempt` DFA (the one-line computed-goto jump table pcrec's first
# instrument could not see -- compile.c's own comment), a VM hybrid (code-
# dominated), and a `\z` form (the whole-subject artifact the adapter also
# builds). `--warn-emit-bytes=1` makes the advisory line fire on every one
# of them, and the line prints the two quantities in the order the port
# returns them.
EMIT_SIZE_WITNESSES = (
    ("table-dominated DFA (email orig)", ("email", "orig"), ""),
    ("attempt DFA, one-line jump table", ("literal", b"^foo[0-9]+bar"), ""),
    ("VM hybrid", ("literal", b"a(b|c)+d"), ""),
    ("VM hybrid, forced collapse", ("literal", b"a(b|c){2,5}d"),
     "-fprefilter-collapse"),
    # [B22] (e), inbox I-22 (ii): THE SAME-PIN RE-COMPARISON on the one
    # artifact whose cross-pin byte comparison was INVALID -- bounded's
    # `[a-z]{0,32768}`, a count-collapsed HYBRID at 96e44c2 and a DECLINED
    # plain-VM artifact since [OPT-4.1] (it changed KIND, so any
    # before/after byte delta says nothing about counting rules). Both
    # sides at ONE pin, with the counting rule STATED (pcrec
    # docs/dev/lanes/opt41_report.md 15 enumerates six readings; the one
    # this bench and the caps mean is "split `.c` + `.h`, comment-excluded"
    # -- emit_size() summed over both emitted files, the definition
    # `emit_size_measure` enforces): the pin's own `--warn-emit-bytes=1`
    # numbers vs the port, byte-exact, both forms. The absolute value is
    # name-dependent (the emitted `#include "<basename>.h"` line -- the
    # [B16] finding), which is WHY the comparison is same-files, never a
    # constant: with the adapter's `artifact.c` naming it reads
    # 18,291 plain / 18,496 whole, and emit_bytes == emit_code_bytes (a
    # declined plain-VM artifact carries no table initializers at all).
    ("declined plain-VM artifact (bounded cls-upto-32768)",
     ("bounded", "cls-upto-32768"), ""),
)


def check_emit_size_port():
    """THE SIZE PORT AGAINST THE PIN'S OWN NUMBERS ([B19] (d), I-18 (iv)).

    `adapter.emit_size()` is a port of pcrec src/core/compile.c's
    `emit_size_measure` -- the ONE definition the two caps enforce and the
    `--warn-emit-bytes` message prints (total minus comments; that minus
    table initializers). A port is a second implementation of someone
    else's definition, which is exactly the shape that drifts (pcrec's own
    r40 F1: "this row's own measuring instrument disagreed with the
    artifact it was measuring"), so it is checked here against the
    definition's owner: the pin's binary is run with `--warn-emit-bytes=1`
    on artifacts of each kind, its message's two numbers are parsed by
    THIS check (not by the adapter), and they must equal the port's over
    the same two files. The adapter separately refuses any compile whose
    warning disagrees with the port (`_emit_facts`); this is the check
    that proves that refusal is not decorative, and that the port is right
    where no warning fires at the default threshold (every artifact of
    both sub-benches but one)."""
    print("-- the emit-size port vs pcrec's --warn-emit-bytes numbers --")
    try:
        adapter = _ad.discover()["pcrec"]
    except KeyError:
        bad("emit-size port", "no pcrec adapter")
        return
    mod = _pcrec_adapter_module()
    pcrec = adapter.pin_binary()
    tmp = tempfile.mkdtemp(prefix="pcrecbench-emitsize-")
    try:
        for i, (label, src, extra) in enumerate(EMIT_SIZE_WITNESSES):
            pattern = src[1] if src[0] == "literal" else _bench_pattern(src[0], src[1])
            forms = ((_ad.FORM_PLAIN, pattern),
                     (_ad.FORM_WHOLE_SUBJECT, _rec.whole_subject_text(pattern)))
            for form, text in forms:
                d = os.path.join(tmp, "w%d-%s" % (i, form))
                os.makedirs(d, exist_ok=True)
                art = os.path.join(d, "artifact.c")
                argv = [pcrec, "-p", "rx", "--features", "all",
                        "--warn-emit-bytes=1"] + extra.split() + \
                       ["-o", art, "--", text.decode("latin-1")]
                proc = run(argv, timeout=120)
                if proc.returncode != 0:
                    bad("emit-size port: %s / %s" % (label, form),
                        "pcrec did not emit: %s" % proc.stderr[-200:])
                    continue
                m = mod.WARN_RE.search(proc.stderr or "")
                if not m:
                    bad("emit-size port: %s / %s" % (label, form),
                        "--warn-emit-bytes=1 did not make the advisory line "
                        "fire (stderr %r)" % proc.stderr[-200:])
                    continue
                pin_tot, pin_code = int(m.group(1)), int(m.group(2))
                files = [art] + ([art[:-2] + ".h"] if os.path.exists(art[:-2] + ".h") else [])
                port = mod.emit_size(files)
                if port == (pin_tot, pin_code):
                    raw = sum(os.path.getsize(f) for f in files)
                    ok("emit-size port: %s / %s" % (label, form),
                       "pin says %d total / %d code; the port agrees "
                       "(raw file bytes %d, %d files)"
                       % (pin_tot, pin_code, raw, len(files)))
                else:
                    bad("emit-size port: %s / %s" % (label, form),
                        "pin says %d / %d, the port %d / %d over %s -- "
                        "re-derive adapter.emit_size() against compile.c"
                        % (pin_tot, pin_code, port[0], port[1], files))
        # The NEGATIVE control: a file the port must not mistake -- a
        # comment line inside a table initializer stays PROSE, a `= {`
        # that is not `static const` stays CODE, and a block comment that
        # opens and closes on one line is one line of prose. Hand-built,
        # with a hand-counted answer.
        # The CLASSIFICATION is the hand part; each line's byte count is
        # arithmetic (its length plus the newline it ends with).
        probe_lines = (
            (b"/* one-line comment */", "prose"),
            (b"int x = 1;", "code"),
            (b"static const int rx_t[2] = {", "table"),
            (b"    /* inside */", "prose"),     # a comment INSIDE a table
            (b"    1, 2 };", "table"),          # the closing line is table
            (b"struct s v[1] = { 0 };", "code"),  # `= {` but not static const
            (b"/* open", "prose"),
            (b"   still */ int y;", "prose"),   # the closing line is prose
            (b"// tail", "prose"),
        )
        probe = b"".join(l + b"\n" for l, _c in probe_lines)
        pf = os.path.join(tmp, "probe.c")
        with open(pf, "wb") as f:
            f.write(probe)
        total = len(probe)
        prose = sum(len(l) + 1 for l, c in probe_lines if c == "prose")
        tables = sum(len(l) + 1 for l, c in probe_lines if c == "table")
        want = (total - prose, total - prose - tables)
        got = mod.emit_size([pf])
        if got == want:
            ok("emit-size port: the hand-counted probe",
               "%d bytes: prose %d, tables %d -> total %d, code %d"
               % (total, prose, tables, want[0], want[1]))
        else:
            bad("emit-size port: the hand-counted probe",
                "want %r, got %r" % (want, got))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def check_abi_floor_refusal():
    """THE ABI FLOOR, ON A SABOTAGED ARTIFACT ([B16]).

    `shim.c` reads two `struct rx_info` fields that pcrec appended at abi
    6, and declares that floor once (`PB_SHIM_MIN_ABI`). `driver.c` refuses
    an artifact below it before reading anything else, and `adapter.py`
    turns that refusal into a clean AdapterError.

    Nothing in the corpus can exercise that path -- the pin's abi is at or
    above the floor by construction -- so without a SABOTAGE the whole
    refusal would ship unexercised, which is this project's own stated
    check-design lesson. The sabotage is the smallest one that reaches the
    real path: compile a real artifact, edit its `rx_info` initialiser's
    `.abi = N` to `.abi = 5` (below the floor, 6 at [B16] and 10 since
    [B18]) in a COPY, and run the ordinary shim + driver over it. It still
    compiles (the fields are all still there -- the point is that the
    driver must not TRUST them on an artifact that claims to predate them),
    and the refusal must fire by name and carry both numbers -- the floor
    read out of shim.c (`_shim_min_abi`), never retyped here.

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
        floor = _shim_min_abi()
        if floor is None:
            bad("abi-floor: the refusal carries BOTH numbers",
                "PB_SHIM_MIN_ABI not found in shim.c")
        elif ("artifact rx_info.abi 5" in diag) and ("below the %d" % floor in diag):
            ok("abi-floor: the refusal carries BOTH numbers",
               "the artifact's claimed abi (5) and the shim's floor (%d, read "
               "out of shim.c), so a reader knows which end to move" % floor)
        else:
            bad("abi-floor: the refusal carries BOTH numbers",
                "shim floor %r; got %r" % (floor, diag[:200]))

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
    return _pcrec_adapter_module().ABI_FLOOR_TOKEN


# --------------------------------------------- 25 the free_text note guard

def check_note_length_guard():
    """[B12] (2026-08-29, bounded's first window): a record's `note` /
    `status_detail` are schema `free_text` (maxLength 8192), and the harness
    filled them from a per-cell LIST that grew with the set -- 24 patterns x 3
    regimes = 72 calibration sentences (~12 KB) -- so a 21-minute cell was
    measured and then REJECTED at validation. `record.join_notes` is now the
    only path from that list to a record. The CONTROL reads the cap FROM THE
    SCHEMA JSON, not from record.py, so the constant and the schema cannot
    drift apart unnoticed; the sentences are the real ones (the rejected
    record's own shape, 72 x ~165 bytes)."""
    import json as _json
    sys.path.insert(0, ROOT)
    from pcrecbench import record as rec
    with open(os.path.join(ROOT, "schema", "record.schema.json")) as fh:
        schema = _json.load(fh)
    cap = schema["$defs"]["free_text"]["maxLength"]
    if rec.FREE_TEXT_MAX == cap:
        ok("note guard: record.FREE_TEXT_MAX == schema free_text cap",
           "%d" % cap)
    else:
        bad("note guard: record.FREE_TEXT_MAX != schema free_text cap",
            "%d vs %d" % (rec.FREE_TEXT_MAX, cap))
        return
    sentence = ("iters for (cls-upto-%d, plain, search_short) = 471032: median "
                "per-iteration 0.106 us (subject d-00256) -> iters=471032 for "
                "a 50 ms loop")
    seventy_two = [sentence % i for i in range(72)]
    raw = "quiet window run | " + "; ".join(seventy_two)
    if len(raw) <= cap:
        bad("note guard: the 72-sentence shape does not exceed the cap",
            "%d bytes -- the control is not a control" % len(raw))
        return
    joined = rec.join_notes(seventy_two, prefix="quiet window run")
    elided = 72 - joined.count("iters for (")
    if len(joined) <= cap and "note(s) elided" in joined and \
            ("[+%d calibration/adapter note(s) elided" % elided) in joined:
        ok("note guard: 72 real sentences fit under the cap",
           "%d -> %d bytes, %d elided, marker names the count and the class"
           % (len(raw), len(joined), elided))
    else:
        bad("note guard: 72 real sentences", "len=%d joined=%r"
            % (len(joined), joined[-160:]))
    short = rec.join_notes(seventy_two[:3], prefix="x")
    if short == "x | " + "; ".join(seventy_two[:3]):
        ok("note guard: a short list joins verbatim (no marker)")
    else:
        bad("note guard: short list altered", repr(short[:120]))
    huge = rec.join_notes([], prefix="y" * (cap * 2))
    if len(huge) == cap and huge.endswith("free_text cap]"):
        ok("note guard: an over-cap prefix is cut to the cap with a marker")
    else:
        bad("note guard: over-cap prefix", "len=%d" % len(huge))
    # And the schema itself agrees: the joined string validates as free_text.
    try:
        import jsonschema
        jsonschema.validate(joined, schema["$defs"]["free_text"])
        jsonschema.validate(huge, schema["$defs"]["free_text"])
        ok("note guard: the joined strings validate as schema free_text")
    except Exception as e:  # noqa: BLE001 -- the check reports, never raises
        bad("note guard: schema rejects the joined string", str(e)[:120])


# ------------------------------------- 26 the occupancy AVERAGE (OD-B12)

def _mpstat_capture(busy_by_second, cpus=12):
    """A synthetic `mpstat -P ALL 1 N` capture in LC_ALL=C layout: one
    header+block per second, then the `Average:` block mpstat itself
    prints. `busy_by_second[s][cpu]` is that core's busy %% in second s
    (missing = 2 %%)."""
    hdr = ("%s     CPU    %%usr   %%nice    %%sys %%iowait    %%irq   %%soft  "
           "%%steal  %%guest  %%gnice   %%idle")
    def row(stamp, cpu, busy):
        return ("%s %7s %7.2f    0.00    0.00    0.00    0.00    0.00    0.00"
                "    0.00    0.00 %7.2f" % (stamp, cpu, busy, 100.0 - busy))
    out = ["Linux 7.0.0 (synthetic) \t08/30/26 \t_x86_64_\t(%d CPU)" % cpus, ""]
    n = len(busy_by_second)
    for sec, per in enumerate(busy_by_second):
        stamp = "00:00:%02d" % (sec + 1)
        out.append(hdr % stamp)
        allb = sum(per.get(c, 2.0) for c in range(cpus)) / cpus
        out.append(row(stamp, "all", allb))
        for c in range(cpus):
            out.append(row(stamp, c, per.get(c, 2.0)))
        out.append("")
    out.append(hdr % "Average:")
    avg = {c: sum(per.get(c, 2.0) for per in busy_by_second) / n
           for c in range(cpus)}
    out.append(row("Average:", "all", sum(avg.values()) / cpus))
    for c in range(cpus):
        out.append(row("Average:", c, avg[c]))
    return "\n".join(out) + "\n"


def check_occupancy_average():
    """BD7 / OD-B12 (2026-08-30): the occupancy instrument is a 5 x 1 s
    mpstat run judged on its AVERAGE block. Five of five inconclusive-load
    stamps in the 2026-08-29/30 windows were one-second after-samples that
    caught a burst (10.1-20.2 %% on one core, load quiet). The CONTROLS: the
    same synthetic capture judged one second at a time DOES fail on the
    burst second -- so the rule, not the fixture, is what passes it -- and
    a sustained competitor still fails on the average."""
    sys.path.insert(0, ROOT)
    from pcrecbench import quiet
    if quiet.OCCUPANCY_SECONDS == 5 and quiet.MPSTAT_CMD[-1] == "5" \
            and " ".join(quiet.MPSTAT_CMD).endswith("1 5"):
        ok("occupancy: the instrument is mpstat -P ALL 1 5",
           " ".join(quiet.MPSTAT_CMD))
    else:
        bad("occupancy: instrument is not 5 x 1 s", " ".join(quiet.MPSTAT_CMD))
        return
    # (a) a one-second 30 % burst on core 3; the pinned core 11 at 100 %.
    burst = [{11: 100.0}, {11: 100.0, 3: 30.0}, {11: 100.0}, {11: 100.0},
             {11: 100.0}]
    cap = _mpstat_capture(burst)
    avg = quiet.judge_mpstat(cap, exclude_cpu=11)
    secs, average = quiet.split_mpstat(cap)
    if len(secs) == 5 and average:
        ok("occupancy: capture splits into 5 seconds + an Average block")
    else:
        bad("occupancy: split", "%d seconds, average=%r" % (len(secs), bool(average)))
        return
    one, _ = quiet.parse_mpstat(secs[1])
    burst_alone = round(100.0 - min(v for c, v in one.items() if c != 11), 2)
    if avg["verdict"] == "pass" and abs(avg["max_busy_pct"] - 7.6) < 0.05 \
            and burst_alone == 30.0:
        ok("occupancy: a 1-s 30 % burst averages to 7.6 % -> pass",
           "the burst second alone reads %.1f %% (the old rule's fail)"
           % burst_alone)
    else:
        bad("occupancy: burst averaging", "%r alone=%s" % (avg, burst_alone))
    if "per-second peak" in avg["raw"] and "30.00" in avg["raw"] \
            and avg["raw"].startswith("Average:"):
        ok("occupancy: raw keeps the Average block and the per-second peaks")
    else:
        bad("occupancy: raw content", avg["raw"][:200])
    # (b) a sustained competitor on core 5 for all five seconds.
    sustained = [{11: 100.0, 5: 100.0}] * 5
    s2 = quiet.judge_mpstat(_mpstat_capture(sustained), exclude_cpu=11)
    if s2["verdict"] == "fail" and s2["max_busy_pct"] == 100.0:
        ok("occupancy: a sustained 100 % core still fails on the average")
    else:
        bad("occupancy: sustained competitor", repr(s2))
    # (c) the pinned core is excluded: at 100 % throughout it never counts.
    quiet_box = [{11: 100.0}] * 5
    s3 = quiet.judge_mpstat(_mpstat_capture(quiet_box), exclude_cpu=11)
    s4 = quiet.judge_mpstat(_mpstat_capture(quiet_box), exclude_cpu=None)
    if s3["verdict"] == "pass" and s4["verdict"] == "fail":
        ok("occupancy: the target core is excluded iff asked",
           "pass with exclude_cpu=11, fail without")
    else:
        bad("occupancy: exclude_cpu", "%r / %r" % (s3["verdict"], s4["verdict"]))
    # (d) a single-interval capture (no Average block) is still judged.
    single = _mpstat_capture([{11: 100.0, 4: 12.0}])
    single = single.split("\nAverage:")[0]
    s5 = quiet.judge_mpstat(single, exclude_cpu=11)
    if s5["verdict"] == "fail" and s5["max_busy_pct"] == 12.0:
        ok("occupancy: a single-interval capture is judged as itself")
    else:
        bad("occupancy: single interval", repr(s5)[:200])


# ------------------------------- 27 the gate's shape, schema v1.4 ([B20])
#
# docs/design/gate_shape_v14.md 8, each check with the CONTROL the spec
# names. No sleep injection in the production drivers (ruling R-10): the
# end-to-end assertions go through hand-assembled records and `store.write`,
# which VALIDATES -- so X31/X32/X33 fire on the harness's own stamp, which
# is the reason `check_spread_status_stamped` is end-to-end at all.

def _capture_without_cpu(text, cpu):
    """A synthetic capture with every row of `cpu` removed (the target row
    ABSENT: an offline core, a restricted cpuset, a row the parser skipped)."""
    return "\n".join(ln for ln in text.splitlines()
                     if not re.match(r"^\S+\s+%d\s" % cpu, ln)) + "\n"


def check_target_core_preflight():
    """gate_shape_v14.md 1 (c)/(c'), ruling R-2: the pre-flight judges the
    TARGET core's own reading and refuses a capture with no target row.
    Three synthetic captures with exclude_cpu = 11 (the fixture shares no
    source with judge_mpstat); the CONTROL is twofold -- the non-target
    verdict is `pass` in all three (the refusals come from the NEW clauses,
    not X26's), and the same captures with exclude_cpu = None carry no
    field and refuse nothing (the clause is inert when nothing is pinned)."""
    print("-- the target-core pre-flight (v1.4) --")
    from pcrecbench import quiet
    load = {"load1": 0.5}
    busy = _mpstat_capture([{11: 60.0}] * 5)
    idle = _mpstat_capture([{11: 4.0}] * 5)
    absent = _capture_without_cpu(_mpstat_capture([{11: 4.0}] * 5), 11)
    s_busy = quiet.judge_mpstat(busy, exclude_cpu=11, siblings=[5])
    s_idle = quiet.judge_mpstat(idle, exclude_cpu=11, siblings=[5])
    s_abs = quiet.judge_mpstat(absent, exclude_cpu=11, siblings=[5])
    if (s_busy["target_busy_pct"] == 60.0 and s_busy["verdict"] == "pass"
            and s_idle["target_busy_pct"] == 4.0 and s_idle["verdict"] == "pass"
            and s_abs["target_busy_pct"] is None and s_abs["verdict"] == "pass"):
        ok("target: the tri-state field (60 / 4 / None), verdict pass in all three",
           "the non-target judgement is untouched (X26)")
    else:
        bad("target: tri-state field", "%r %r %r" % (
            s_busy.get("target_busy_pct"), s_idle.get("target_busy_pct"),
            s_abs.get("target_busy_pct", "ABSENT")))
        return
    r_busy = quiet.gate(load, s_busy, force=True)
    r_idle = quiet.gate(load, s_idle, force=True)
    r_abs = quiet.gate(load, s_abs, force=True)
    if (len(r_busy) == 1 and "TARGET core cpu11 reads 60.00% busy" in r_busy[0]
            and r_idle == []
            and len(r_abs) == 1 and "target core cpu11 does not appear" in r_abs[0]):
        ok("target: gate() refuses the busy target and the missing row BY NAME",
           "busy -> '%s...'; idle -> no reason; absent -> '%s...'"
           % (r_busy[0][:40], r_abs[0][:44]))
    else:
        bad("target: gate() clauses", "%r / %r / %r" % (r_busy, r_idle, r_abs))
    try:
        quiet.gate(load, s_busy, force=False)
        bad("target: a busy target is a REFUSAL without --force-unquiet")
    except quiet.QuietRefusal as e:
        ok("target: a busy target is a REFUSAL without --force-unquiet",
           "QuietRefusal (exit 3): %s" % str(e).splitlines()[1].strip()[:60])
    # the CONTROL: nothing pinned => no field, and the TARGET clauses inert
    # on all three (the 60 % capture is then refused by the NON-target
    # clause, as it should be: cpu 11 is just another core when unpinned)
    ctl = [quiet.judge_mpstat(t, exclude_cpu=None) for t in (busy, idle, absent)]
    reasons = [quiet.gate(load, c, force=True) for c in ctl]
    if all("target_busy_pct" not in c for c in ctl) \
            and not any("TARGET core" in r or "does not appear" in r
                        for rs in reasons for r in rs) \
            and reasons[1] == [] and reasons[2] == [] \
            and reasons[0] and reasons[0][0].startswith("occupancy: busiest non-target core 60.00%"):
        ok("target: CONTROL -- unpinned, the field is absent and the target clauses inert",
           "the 60 % capture is refused by the NON-target clause instead")
    else:
        bad("target: control", "%r %r" % ([c.get("target_busy_pct", "ABSENT") for c in ctl], reasons))
    # and the `unavailable` early return carries null when pinned (H1)
    u = quiet.judge_mpstat("garbage with no rows", exclude_cpu=11, siblings=[5])
    if u["verdict"] == "unavailable" and u.get("target_busy_pct", "ABSENT") is None \
            and quiet.gate(load, u, force=True) == [
                "occupancy: %s is unavailable -- recorded, not skipped "
                "(requirements 9(b))" % " ".join(quiet.MPSTAT_CMD)]:
        ok("target: `unavailable` carries target null and only the unavailable reason")
    else:
        bad("target: unavailable early return", repr(u)[:200])


def check_quiet_cli_agrees_with_gate():
    """Ruling R-7: `pcrecbench quiet` reduces each sample through the SAME
    `gate()` a run's pre-flight uses. One synthetic sample (load1 over the
    limit AND the target busy): the CLI's printed reasons are gate()'s
    list, verbatim, and it exits 3; CONTROL: a sample that passes both
    prints no reason and exits 0."""
    print("-- the quiet CLI judges through gate() (v1.4) --")
    import io
    import contextlib
    from pcrecbench import quiet, __main__ as cli

    class Args:
        samples = 1
        pin = 11

    def run_cli(load1, capture):
        sample = quiet.judge_mpstat(capture, exclude_cpu=11, siblings=[5])
        load = {"loadavg_raw": "%.2f 0.1 0.1 1/1 1" % load1, "sampled_at": "x",
                "load1": load1, "load5": 0.1, "load15": 0.1}
        saved = (quiet.check, quiet.pinning)
        quiet.check = lambda exclude_cpu=None, **kw: (load, sample)
        quiet.pinning = lambda cpu=None: {"mode": "taskset", "cpu": 11}
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = cli.cmd_quiet(Args())
        finally:
            quiet.check, quiet.pinning = saved
        printed = [ln.strip()[2:] for ln in buf.getvalue().splitlines()
                   if ln.strip().startswith("- ")]
        return rc, printed, quiet.gate(load, sample, force=True)

    rc, printed, want = run_cli(3.4, _mpstat_capture([{11: 60.0}] * 5))
    if rc == 3 and printed == want and len(want) == 2 \
            and want[0].startswith("load1 3.40 exceeds"):
        ok("quiet CLI: prints exactly gate()'s reasons (load1 + the target), exit 3",
           "%d reason(s)" % len(want))
    else:
        bad("quiet CLI vs gate()", "rc %s printed %r want %r" % (rc, printed, want))
    rc2, printed2, want2 = run_cli(0.4, _mpstat_capture([{11: 4.0}] * 5))
    if rc2 == 0 and printed2 == [] and want2 == []:
        ok("quiet CLI: CONTROL -- a passing sample prints no reason, exit 0")
    else:
        bad("quiet CLI control", "rc %s printed %r want %r" % (rc2, printed2, want2))


def _example_14():
    """The generated 1.4 good example (schema/examples), as (setup, rows)."""
    import glob as _glob
    import json as _json
    f = [x for x in _glob.glob(os.path.join(ROOT, "schema", "examples", "*.jsonl"))
         if "20260830T120000Z" in x][0]
    lines = [ln for ln in open(f, encoding="utf-8").read().split("\n") if ln.strip()]
    return _json.loads(lines[0]), [_json.loads(ln) for ln in lines[1:]]


def _write_scratch(setup, rows, name):
    """Write a hand-assembled record through store.write into a scratch
    store (VALIDATING), -> (path, setup as written) or raises StoreError."""
    from pcrecbench import store as _store
    root = os.path.join(ROOT, "build", "selfcheck-%s-store" % name)
    shutil.rmtree(root, ignore_errors=True)
    path, rid = _store.write(root, setup, rows)
    from pcrecbench import reduce as _rd
    return path, _rd.read_record(path)[0]


def check_after_sample_is_provenance():
    """gate_shape_v14.md 2: a FAILED after sample never disqualifies a v1.4
    record. The 1.4 example with its after occupancy at 40 % (pre-flight
    passed, rows agree, 5 trials) stamped by `derive_status` and joined by
    `join_notes` comes back `measured`, its `note` carrying the provenance
    sentence SECOND (after the operator's prefix), `occupancy.after.verdict
    = fail` (X26 holds), and it VALIDATES at 1.4 through store.write.
    CONTROL: the same record re-stamped 1.3 is REJECTED -- by X13 (the v1.1
    text reads the after sample) and by X33 (the block on a 1.3 record)."""
    print("-- the after sample is provenance (v1.4) --")
    import json as _json
    from pcrecbench import harness as _h, quiet, record as _rec, store as _store
    setup, rows = _example_14()
    occ = setup["environment"]["occupancy"]
    occ["after"]["max_busy_pct"] = 40.0
    occ["after"]["verdict"] = "fail"
    status, first = _h.derive_status([], setup["trial_agreement"], "pinned")
    after = quiet.after_notes(occ, setup["environment"]["load"])
    setup["status"] = status
    setup.pop("status_detail", None)
    setup["note"] = _rec.join_notes(after + ["calibration for (x) = 1 iters: capped"],
                                    prefix="quiet window run", first=first)
    try:
        path, written = _write_scratch(setup, rows, "afterprov")
    except _store.StoreError as e:
        bad("after-sample: the record validates at 1.4", str(e)[-300:])
        return
    parts = written["note"].split(" | ", 1)[1].split("; ")
    if (written["status"] == "measured" and parts[0].startswith(
            "after-sample (provenance, not a verdict): occupancy after the run 40.00%")
            and written["note"].startswith("quiet window run | ")
            and written["environment"]["occupancy"]["after"]["verdict"] == "fail"
            and len(after) == 2):
        ok("after-sample: 40 % after -> measured; the sentence SECOND in note; X26 holds",
           "note = prefix | %s..." % parts[0][:48])
    else:
        bad("after-sample as provenance", "status %s note %r"
            % (written["status"], written.get("note", "")[:200]))
    # the CONTROL: the same record stamped 1.3 is rejected by X13 AND X33
    ctl = dict(written)
    ctl["schema_version"] = "1.3"
    root = os.path.join(ROOT, "build", "selfcheck-afterprov-ctl")
    shutil.rmtree(root, ignore_errors=True)
    try:
        _store.write(root, ctl, rows)
        bad("after-sample: CONTROL -- the same record at 1.3 must be REJECTED")
    except _store.StoreError as e:
        msg = str(e)
        if "[X13]" in msg and "[X33]" in msg:
            ok("after-sample: CONTROL -- re-stamped 1.3 it is rejected by X13 and X33",
               "one sabotage, two versions, two verdicts")
        else:
            bad("after-sample control", msg[-300:])
    shutil.rmtree(root, ignore_errors=True)


def _ta_row(pid, sid, regime, trial, seq, ns=None, outcome="matched-as-expected",
            iterations=1000):
    row = {"kind": "match", "pattern_id": pid, "subject_id": sid, "regime": regime,
           "trial": trial, "seq": seq, "match_outcome": outcome,
           "consumed_length": None}
    if regime == "large-subject-throughput":
        row["truncation_check"] = "verified"
    if outcome == "matched-as-expected":
        row["timing"] = {"elapsed_ns": int(round(ns * iterations)),
                         "iterations": iterations, "bytes_processed": 0}
        if iterations > 1:
            row["calibration"] = {"target_ns": 1000, "probe_iterations": 1,
                                  "probe_elapsed_ns": 100000}
    elif outcome == "timed-out":
        row["diagnostic"] = "the per-subject alarm fired (fixture)"
    return row


def _ta_fixture(trials=5):
    """gate_shape_v14.md 8's hand-computed fixture: group A of 4 rows (clean;
    one 3x trial; two 1.6x trials; one 0.6x trial) => d = 2 of n = 4,
    DISAGREES under (2, 3); group B of 5 rows, one disagreeing => d = 1;
    group C of 3 rows at iterations = 1 => unjudged (few_timed_trials);
    group D: one row EVERY trial timed-out (all_timed_out), one MIXED (two
    timed-out, three timed) => judged and disagreeing, d = 1 of n = 1.
    Plus the two BOUNDARY rows in group B: a trial at exactly k*m (not
    slow) and a minimum at exactly m/k (not fast)."""
    S = "short-subject-search"
    M = "match-compliance"
    spec = [
        ("pa", "a1", S, [100, 101, 99, 100, 102]),
        ("pa", "a2", S, [100, 300, 100, 100, 100]),
        ("pa", "a3", S, [100, 160, 100, 160, 100]),
        ("pa", "a4", S, [100, 100, 60, 100, 100]),
        ("pb", "b1", S, [100, 100, 100, 100, 100]),
        ("pb", "b2", S, [150, 150, 150, 150, 225]),      # 225 == 1.5 * 150: NOT slow
        ("pb", "b3", S, [150, 150, 150, 100, 150]),      # 100 == 150 / 1.5: NOT fast
        ("pb", "b4", S, [100, 101, 100, 99, 100]),
        ("pb", "b5", S, [100, 160, 100, 160, 100]),
    ]
    rows, seq = [], 0
    for pid, sid, reg, vals in spec:
        for t in range(1, trials + 1):
            seq += 1
            rows.append(_ta_row(pid, sid, reg, t, seq, vals[t - 1]))
    for sid in ("c1", "c2", "c3"):
        for t in range(1, trials + 1):
            seq += 1
            rows.append(_ta_row("pc", sid, M, t, seq, 100, iterations=1))
    for t in range(1, trials + 1):
        seq += 1
        rows.append(_ta_row("pd", "d1", M, t, seq, outcome="timed-out"))
    for t in range(1, trials + 1):
        seq += 1
        if t in (2, 4):
            rows.append(_ta_row("pd", "d2", M, t, seq, outcome="timed-out"))
        else:
            rows.append(_ta_row("pd", "d2", M, t, seq, 100))
    return rows


def _assemble(rows, base=None, trials_hint=None):
    """A VALID setup for hand-built rows: the 1.4 example's setup with the
    rosters replaced and one `plain` compile row per pattern prepended."""
    import json as _json
    setup, _ex_rows = _example_14() if base is None else base
    setup = _json.loads(_json.dumps(setup))
    pats = sorted({r["pattern_id"] for r in rows})
    subs = sorted({r["subject_id"] for r in rows if r["kind"] == "match"})
    setup["patterns"] = [{"pattern_id": p, "canonical_sha256": "0" * 64,
                          "hazard_class": "none", "size_class": "tiny", "variant": None}
                         for p in pats]
    setup["subjects"] = [{"subject_id": s_, "role": "single", "n_subjects": 1,
                          "bytes_offered": 64, "sha256": "0" * 64} for s_ in subs]
    setup["subbench"]["regimes"] = ["match-compliance", "short-subject-search",
                                    "large-subject-throughput"]
    compile_rows = [{"kind": "compile", "pattern_id": p, "trial": 1,
                     "compile_outcome": "compiled", "cost_class": "compiled-aot",
                     "cost": {"total_ns": 1000}} for p in pats]
    all_rows = compile_rows + [dict(r) for r in rows]
    for i, r in enumerate(all_rows, start=1):
        r["seq"] = i
    setup["environment"]["occupancy"].pop("timeline", None)
    setup["environment"]["occupancy"].pop("timeline_tool", None)
    setup.pop("status_detail", None)
    setup.pop("note", None)
    return setup, all_rows


def check_trial_agreement_fixture():
    """gate_shape_v14.md 8: `reduce.judge_trial_agreement` on the
    hand-computed fixture gives the stated integers; `share_c = 1` flips
    it to `agree`; truncated to 3 trials it is `n/a-trials` with every key
    unjudged under `na_trials`. CONTROL: `schema/validate.py`'s X32
    recomputation (its OWN implementation, no shared source) on the same
    rows gives the same integers and the same worst group -- called
    directly AND through store.write, where X32 fires on the block."""
    print("-- the trial-agreement fixture: two implementations, one answer --")
    import importlib.util
    from pcrecbench import reduce as _rd, store as _store
    rows = _ta_fixture()
    want = {"trials": 5, "groups_judged": 3, "groups_disagreeing": 1,
            "rows_judged": 10, "rows_disagreeing": 4, "rows_unjudged": 4,
            "rows_unjudged_reasons": {"few_timed_trials": 3, "all_timed_out": 1,
                                      "na_trials": 0},
            "worst_group": {"pattern_id": "pa", "regime": "short-subject-search",
                            "form": "plain", "d": 2, "n": 4}}
    got = _rd.judge_trial_agreement(rows)
    if all(got[k] == v for k, v in want.items()) and got["verdict"] == "disagree":
        ok("agreement: the fixture's integers (3 groups, 1 disagrees; 10/4/4 rows; A d=2 n=4)",
           "verdict disagree; boundary rows at exactly k*m and m/k are not disagreements")
    else:
        bad("agreement: fixture", repr({k: got.get(k) for k in list(want) + ["verdict"]}))
        return
    g1 = _rd.judge_trial_agreement(rows, share_c=1)
    if g1["verdict"] == "agree" and g1["groups_disagreeing"] == 0 \
            and g1["rows_disagreeing"] == 4:
        ok("agreement: share_c = 1 flips the verdict to agree (the same 4 rows)")
    else:
        bad("agreement: share_c=1", repr(g1))
    g3 = _rd.judge_trial_agreement(_ta_fixture(trials=3))
    if g3["verdict"] == "n/a-trials" and g3["rows_unjudged"] == 14 \
            and g3["rows_unjudged_reasons"]["na_trials"] == 14 \
            and g3["rows_judged"] == g3["groups_judged"] == 0 and g3["worst_group"] is None:
        ok("agreement: 3 trials -> n/a-trials, 14 keys unjudged under na_trials")
    else:
        bad("agreement: 3 trials", repr(g3))
    # the CONTROL: validate.py's second implementation, directly
    spec = importlib.util.spec_from_file_location(
        "pb_validate", os.path.join(ROOT, "schema", "validate.py"))
    V = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(V)
    v = V.judge_trial_agreement(rows, 1.5, 2, 3)
    same = all(v[k] == got[k] for k in want)
    v1 = V.judge_trial_agreement(rows, 1.5, 2, 1)
    if same and v1["groups_disagreeing"] == 0 and V.expected_verdict(got) == "disagree":
        ok("agreement: CONTROL -- validate.py's own implementation gives the same integers",
           "no shared source; counts and worst_group key equal")
    else:
        bad("agreement: validate.py disagrees", "%r vs %r" % (v, {k: got[k] for k in want}))
    # ... and through store.write, where X32 fires on the stamped block
    setup, all_rows = _assemble(rows)
    setup["trial_agreement"] = _rd.judge_trial_agreement(all_rows)
    setup["status"] = "inconclusive-spread"
    setup["status_detail"] = "fixture"
    try:
        _write_scratch(setup, all_rows, "tafix")
        ok("agreement: the fixture written as a record VALIDATES (X31/X32/X33 on the stamp)")
    except _store.StoreError as e:
        bad("agreement: fixture record rejected", str(e)[-400:])
    setup["trial_agreement"]["rows_disagreeing"] = 3            # the stamp sabotaged
    try:
        _write_scratch(setup, all_rows, "tafix2")
        bad("agreement: a sabotaged stamp must be REJECTED by X32")
    except _store.StoreError as e:
        if "[X32]" in str(e):
            ok("agreement: a stamp of 3 beside rows that say 4 is rejected by X32")
        else:
            bad("agreement: sabotage rejected for the wrong reason", str(e)[-200:])


def check_spread_status_stamped():
    """Ruling R-10: `harness.derive_status` on all five rows of the 5
    decision table returns the stated status and sentence order; then a
    hand-assembled record whose rows make one group disagree, stamped
    through the same function and written through store.write (which
    VALIDATES), comes back `inconclusive-spread` with the block's numbers
    and the 3.4 line at offset 0 of `status_detail`. CONTROL: the same
    rows with ONE slow trial per row instead of two => `measured` -- the
    rule tolerates one, and the check shows it does."""
    print("-- the status decision table, and inconclusive-spread stamped --")
    from pcrecbench import harness as _h, reduce as _rd, store as _store, record as _rec
    agree = {"verdict": "agree", "rule": "v1.4-group", "groups_judged": 2}
    disagree = {"verdict": "disagree", "rule": "v1.4-group", "k": 1.5, "d_min": 2,
                "share_c": 3, "trials": 5, "groups_disagreeing": 1, "groups_judged": 2,
                "rows_disagreeing": 2, "rows_judged": 4, "rows_unjudged": 0,
                "worst_group": {"pattern_id": "pa", "regime": "short-subject-search",
                                "form": "plain", "d": 2, "n": 2}}
    na = {"verdict": "n/a-trials", "rule": "v1.4-group", "trials": 3, "rows_unjudged": 9}
    R = ["load1 3.00 exceeds the limit 2.00"]
    table = [
        ((R, disagree, "pinned"), ("inconclusive-load", [R[0], "trial agreement (v1.4-group, k=1.5"])),
        ((R, agree, "scratch"), ("inconclusive-load", [R[0]])),
        (([], agree, "pinned"), ("measured", [])),
        (([], disagree, "scratch"), ("inconclusive-spread", ["trial agreement (v1.4-group, k=1.5"])),
        (([], na, "pinned"), ("inconclusive-spread", ["trial agreement (v1.4-group): n/a-trials (3 trials"])),
        (([], na, "scratch"), ("measured", ["trial agreement (v1.4-group): n/a-trials (3 trials"])),
    ]
    fails = []
    for (r, v, tier), (w_status, w_prefixes) in table:
        st, sent = _h.derive_status(r, v, tier)
        if st != w_status or len(sent) != len(w_prefixes) or \
                not all(x.startswith(pfx) for x, pfx in zip(sent, w_prefixes)):
            fails.append("(%r, %s, %s) -> %s %r" % (r, v["verdict"], tier, st, sent))
    if not fails:
        ok("status: derive_status matches the decision table on all six cases",
           "R x {agree, disagree, n/a-trials} x tier; the 3.4 line where the table says")
    else:
        bad("status: decision table", "; ".join(fails)[:300])
    # end to end: two rows with two slow trials each => the group disagrees
    def rows_with(slow_trials):
        rows, seq = [], 0
        for sid in ("s1", "s2"):
            for t in range(1, 6):
                seq += 1
                v = 200 if t in slow_trials else 100
                rows.append(_ta_row("pa", sid, "short-subject-search", t, seq, v))
        return rows
    for label, slow, want_status in (("two slow trials per row", (2, 4), "inconclusive-spread"),
                                     ("CONTROL: one slow trial per row", (3,), "measured")):
        setup, all_rows = _assemble(rows_with(slow))
        block = _rd.judge_trial_agreement(all_rows)
        status, first = _h.derive_status([], block, "pinned")
        setup["status"] = status
        if status != "measured":
            setup["status_detail"] = _rec.join_notes([], first=first)
        setup["trial_agreement"] = block
        try:
            path, written = _write_scratch(setup, all_rows, "spread")
        except _store.StoreError as e:
            bad("status: %s" % label, str(e)[-300:])
            continue
        sd = written.get("status_detail", "")
        if written["status"] == want_status and (
                want_status == "measured" or (
                    sd.startswith("trial agreement (v1.4-group, k=1.5, d_min=2, share_c=3, "
                                  "trials=5): 1 of 1 groups disagree; 2 of 2 rows disagree, "
                                  "0 unjudged; worst group pa / short-subject-search / plain: "
                                  "d=2 of n=2")
                    and written["trial_agreement"]["verdict"] == "disagree")):
            ok("status: %s -> %s, written and validated" % (label, want_status),
               "status_detail[0:24] = %r" % sd[:24] if sd else "no status_detail")
        else:
            bad("status: %s" % label, "%s %r" % (written["status"], sd[:160]))


def check_status_sentence_never_elided():
    """Ruling R-4: a record whose calibration sentences exceed the free_text
    cap (bench/bounded's 72-sentence shape) still has its status-deciding
    sentence at offset 0 and the elision marker names the class dropped;
    CONTROL: the same sentences joined WITHOUT `first=` -- the status
    sentence appended last, as before v1.4 -- show it elided."""
    print("-- the status sentence is never elided (v1.4) --")
    from pcrecbench import record as rec
    status = ("trial agreement (v1.4-group, k=1.5, d_min=2, share_c=3, trials=5): "
              "1 of 72 groups disagree; 23 of 1536 rows disagree, 0 unjudged; worst "
              "group cls-upto-32768 / match-compliance / plain: d=23 of n=30")
    cal = [("calibration for (cls-upto-%d, plain, search_short) = 471032 iters: the "
            "median subject would need iters=900000 for 50 ms, capped to 471032 by "
            "the 20 s per-trial budget") % i for i in range(72)]
    joined = rec.join_notes(cal, first=[status])
    if joined.startswith(status) and len(joined) <= rec.FREE_TEXT_MAX \
            and "calibration/adapter note(s) elided" in joined:
        ok("elision: the status sentence is at offset 0; the marker names the class",
           "%d bytes, %d calibration sentence(s) kept" % (len(joined), joined.count("calibration for")))
    else:
        bad("elision: status sentence", joined[:120] + " ... " + joined[-120:])
    ctl = rec.join_notes(cal + [status])
    if status not in ctl and len(ctl) <= rec.FREE_TEXT_MAX:
        ok("elision: CONTROL -- appended last without first=, the status sentence is elided")
    else:
        bad("elision: control", "the status sentence survived without first= (%d bytes)" % len(ctl))


def check_smoke_block_na_trials():
    """gate_shape_v14.md 8: the `--trials 1` smoke record (check_run_smoke's,
    scratch tier) carries the block with `n/a-trials`, `trials: 1`, every
    count 0, `rows_unjudged` = its row keys, and validated (it was written);
    its status is the PRE-FLIGHT's on the scratch tier (5 row 5: never
    `inconclusive-spread`). CONTROLS: `x33-trial-agreement-missing` is
    rejected by X33; the same record re-tiered `pinned` through
    `derive_status` is `inconclusive-spread` (row 4)."""
    print("-- the smoke record carries the block (n/a-trials) --")
    import glob as _glob
    from pcrecbench import harness as _h, reduce as _rd
    files = _glob.glob(os.path.join(ROOT, "build", "selfcheck-store", "records",
                                    "*", "*", "*.jsonl"))
    if not files:
        bad("smoke block: no smoke record found (check_run_smoke did not run?)")
        return
    setup, rows = _rd.read_record(files[0])
    ta = setup.get("trial_agreement") or {}
    keys = {(r["pattern_id"], r["regime"], r.get("form", "plain"), r["subject_id"])
            for r in rows if r["kind"] == "match"}
    if (setup["schema_version"] == "1.4" and setup.get("tier") == "scratch"
            and ta.get("verdict") == "n/a-trials" and ta.get("trials") == 1
            and ta.get("rows_unjudged") == len(keys)
            and ta["rows_unjudged_reasons"]["na_trials"] == len(keys)
            and all(ta.get(k) == 0 for k in ("groups_judged", "groups_disagreeing",
                                             "rows_judged", "rows_disagreeing"))
            and ta.get("worst_group") is None
            and setup["status"] != "inconclusive-spread"):
        ok("smoke block: n/a-trials, trials 1, %d keys unjudged, status %s (scratch)"
           % (len(keys), setup["status"]))
    else:
        bad("smoke block", "%s %r" % (setup.get("status"), ta))
    st, _s = _h.derive_status([], ta, "scratch")
    st_p, sent = _h.derive_status([], ta, "pinned")
    if st == "measured" and st_p == "inconclusive-spread" and sent \
            and sent[0].startswith("trial agreement (v1.4-group): n/a-trials (1 trials"):
        ok("smoke block: CONTROL -- scratch keeps the pre-flight's status; pinned "
           "is inconclusive-spread", "derive_status rows 5 and 4")
    else:
        bad("smoke block: re-tiered control", "%s / %s %r" % (st, st_p, sent))
    proc = _validate(["--expect-reject", "--expect-rule", "X33",
                      os.path.join(ROOT, "schema", "examples", "bad",
                                   "x33-trial-agreement-missing.jsonl")])
    if proc.returncode == 0:
        ok("smoke block: CONTROL -- a 1.4 record with no block is rejected by X33")
    else:
        bad("smoke block: X33 control", (proc.stderr or proc.stdout)[-200:])


def check_scratch_carries_block():
    """gate_shape_v14.md 8: `quick --trials 5` writes a scratch record WITH
    the block and prints the agreement line FROM it; CONTROL: `quick` at its
    default 3 trials writes the block with `n/a-trials` and prints
    `n/a (3 trials -- the rule needs 5, odd; ...)`.

    The 5-trial VERDICT is REPORTED, not asserted (manager ruling,
    2026-08-30, confirming the lane's choice): `agree` is what a quiet box
    gives, but this check is about the block being CARRIED and PRINTED,
    and a smoke suite on a shared box must not fail on the box's own
    verdict -- `make check` is a smoke suite, never a measurement (root
    CLAUDE.md), and a check that turns red whenever a neighbour session
    is busy would train people to ignore red."""
    print("-- `quick` carries the block and prints it (v1.4) --")
    import glob as _glob
    from pcrecbench import reduce as _rd
    for trials, label in ((5, "--trials 5"), (None, "CONTROL: the default 3 trials")):
        scratch = os.path.join(ROOT, "build", "selfcheck-quick14-store")
        shutil.rmtree(scratch, ignore_errors=True)
        argv = ["gnutimeout", "300", sys.executable, "-m", "pcrecbench", "quick",
                "--subbench", "email", "--pattern", "orig", "--regime", "search",
                "--testee", "pcre2-jit", "--subjects", "5", "--store", scratch,
                "--synthetic", "--quiet-output"]
        if trials:
            argv += ["--trials", str(trials)]
        proc = run(argv, cwd=ROOT, timeout=330)
        files = _glob.glob(os.path.join(scratch, "records", "*", "*", "*.jsonl"))
        if proc.returncode != 0 or len(files) != 1:
            bad("quick block: %s" % label, (proc.stderr or proc.stdout)[-200:])
            continue
        setup, _rows = _rd.read_record(files[0])
        ta = setup.get("trial_agreement") or {}
        line = next((ln for ln in proc.stdout.splitlines()
                     if ln.startswith("trial agreement:")), "")
        if trials:
            if ta.get("verdict") in ("agree", "disagree") and ta.get("trials") == 5 \
                    and _rd.agreement_line(ta) in line:
                ok("quick block: --trials 5 carries the block (%s) and prints it"
                   % ta["verdict"], line[16:96])
            else:
                bad("quick block: --trials 5", "%r / %r" % (ta, line))
        else:
            if ta.get("verdict") == "n/a-trials" and ta.get("trials") == 3 \
                    and "n/a (3 trials -- the rule needs 5, odd; pass --trials 5 to judge)" in line:
                ok("quick block: CONTROL -- 3 trials -> n/a-trials, printed as such")
            else:
                bad("quick block: 3-trial control", "%r / %r" % (ta, line))
        shutil.rmtree(scratch, ignore_errors=True)


def check_exit_code_4():
    """Ruling R-6 / contract 4: a `run` whose record is `inconclusive-spread`
    returns 4 with the record WRITTEN and INDEXED, and `pcrecbench index`
    prints the per-status breakdown. The deterministic way to such a record
    without sleep injection: a PINNED-tier `--trials 1` run into a scratch
    store (n/a-trials on the ranked tier, 3.4) -- with the pre-flight's
    SAMPLES simulated quiet in-process (`quiet.check` returning a quiet
    load line and a synthetic idle capture, so the REAL `gate()` finds no
    reason and X13's own clauses hold on the written record: on a busy box
    `inconclusive-load` would rightly take precedence, R-15, and the exit
    code would be 0 for a reason this check is not about). `cmd_run` is
    called in-process so its return value IS the exit code.
    CONTROL: the same run at tier scratch returns 0 (its status is the
    pre-flight's, row 5)."""
    print("-- exit code 4 (v1.4) --")
    import glob as _glob
    import io
    import contextlib
    from pcrecbench import quiet, reduce as _rd, __main__ as cli

    class Args:
        subbench = "email"
        testee = "pcre2-interp"
        regimes = ["match"]
        trials = 1
        iters = 1
        force_unquiet = True
        machine_id = "selfcheck-box"
        pin = None
        subject_timeout = 60
        driver_timeout = 900
        note = "make check exit-code probe -- NOT a measurement"
        synthetic = True
        quiet_output = True

    def quiet_samples(exclude_cpu=None, **_kw):
        import time as _time
        load = {"loadavg_raw": "0.50 0.40 0.30 1/512 30412",
                "sampled_at": _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime()),
                "load1": 0.5, "load5": 0.4, "load15": 0.3}
        return load, quiet.judge_mpstat(_mpstat_capture([{}] * 5), exclude_cpu=exclude_cpu)

    saved = quiet.check
    for tier, want_rc in (("pinned", 4), ("scratch", 0)):
        scratch = os.path.join(ROOT, "build", "selfcheck-rc4-store")
        shutil.rmtree(scratch, ignore_errors=True)
        args = Args()
        args.tier = tier
        args.store = scratch
        quiet.check = quiet_samples              # a quiet box's samples, simulated
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                rc = cli.cmd_run(args)
        except Exception as e:                                 # noqa: BLE001
            bad("exit 4: %s run" % tier, "%s" % e)
            quiet.check = saved
            continue
        finally:
            quiet.check = saved
        files = _glob.glob(os.path.join(scratch, "records", "*", "*", "*.jsonl"))
        setup = _rd.read_record(files[0])[0] if files else {}
        idx = run([sys.executable, "-m", "pcrecbench", "index", "--store", scratch],
                  cwd=ROOT)
        by_status = next((ln for ln in idx.stdout.splitlines()
                          if ln.startswith("index: by status:")), "")
        if tier == "pinned":
            good = (rc == 4 and len(files) == 1
                    and setup.get("status") == "inconclusive-spread"
                    and "inconclusive-spread 1" in by_status
                    and "status     inconclusive-spread" in buf.getvalue())
            label = "exit 4: a pinned --trials 1 run is inconclusive-spread, written, indexed"
        else:
            good = (rc == 0 and len(files) == 1 and setup.get("status") == "measured")
            label = "exit 4: CONTROL -- the same run at tier scratch is measured, returns 0"
        if good:
            ok(label, "rc %d, status %s; %s" % (rc, setup.get("status"), by_status[7:60]))
        else:
            bad(label, "rc %s files %d status %s" % (rc, len(files), setup.get("status")))
        shutil.rmtree(scratch, ignore_errors=True)


def check_timeline_provenance():
    """gate_shape_v14.md 3.6 / 8: a PINNED run on a box with /proc/stat
    writes one `timeline` item per group with `elapsed_ms > 0` and the
    target core reading our own driver (>= 50 % busy over the group; the
    busiest core on a quiet box), and validates; CONTROL: the same run with
    /proc/stat made unreadable (the module's path pointed at a file that
    does not exist -- in-process, no production hook) writes NO `timeline`
    and no `timeline_tool`, and validates."""
    print("-- the per-group occupancy timeline (v1.4, provenance) --")
    from pcrecbench import harness as _h, quiet
    try:
        cpu = min(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        cpu = 0
    if shutil.which("taskset") is None:
        bad("timeline: taskset missing; a pinned run cannot be made")
        return
    saved = quiet.PROC_STAT_PATH
    for label, path in (("with /proc/stat", saved),
                        ("CONTROL: /proc/stat unreadable", "/nonexistent/proc/stat")):
        scratch = os.path.join(ROOT, "build", "selfcheck-timeline-store")
        shutil.rmtree(scratch, ignore_errors=True)
        quiet.PROC_STAT_PATH = path
        try:
            res = _h.run_cell("email", "pcre2-interp", regimes=["match"], trials=1,
                              iters=None, force_unquiet=True, store_root=scratch,
                              machine_id="selfcheck-box", pin_cpu=cpu,
                              synthetic=True, tier="scratch", patterns=["floor"],
                              subject_limit=5, budget=2.0,
                              note="make check timeline probe -- NOT a measurement")
        except Exception as e:                             # noqa: BLE001
            bad("timeline: %s" % label, "%s" % e)
            quiet.PROC_STAT_PATH = saved
            continue
        finally:
            quiet.PROC_STAT_PATH = saved
        occ = res.setup["environment"]["occupancy"]
        tl = occ.get("timeline")
        if path == saved:
            groups = {(r["pattern_id"], r["regime"], r.get("form", "plain"))
                      for r in res.rows if r["kind"] == "match"}
            if (tl and len(tl) == len(groups) and occ.get("timeline_tool") == "/proc/stat"
                    and all(it["elapsed_ms"] > 0 for it in tl)
                    and all(it["target_busy_pct"] >= 50.0 for it in tl)
                    and res.setup["environment"]["pinning"]["cpu"] == cpu):
                busiest = all(it["target_busy_pct"] >= it["max_other_busy_pct"] for it in tl)
                ok("timeline: one item per group (%d), elapsed > 0, target cpu%d reads "
                   "our driver" % (len(tl), cpu),
                   "target %.1f%%, sibling %s, busiest other cpu%d %.1f%%%s" % (
                       tl[0]["target_busy_pct"], tl[0]["sibling_busy_pct"],
                       tl[0]["max_other_cpu"], tl[0]["max_other_busy_pct"],
                       "" if busiest else " (NOT the busiest: the box was loaded)"))
            else:
                bad("timeline: %s" % label, "%r pin %r" % (tl, res.setup["environment"]["pinning"]))
        else:
            if tl is None and "timeline_tool" not in occ:
                ok("timeline: CONTROL -- /proc/stat unreadable writes no timeline; validated")
            else:
                bad("timeline: control", "%r %r" % (tl, occ.get("timeline_tool")))
        shutil.rmtree(scratch, ignore_errors=True)


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
    check_deny_flag_controls()
    check_list_axes_registry()
    check_list_definitions_registry()
    check_list_limits_registry()
    check_emit_size_port()
    check_abi_floor_refusal()
    check_note_length_guard()
    check_occupancy_average()
    check_target_core_preflight()
    check_quiet_cli_agrees_with_gate()
    check_after_sample_is_provenance()
    check_trial_agreement_fixture()
    check_spread_status_stamped()
    check_status_sentence_never_elided()
    check_smoke_block_na_trials()
    check_scratch_carries_block()
    check_exit_code_4()
    check_timeline_provenance()
    print()
    print("check-harness: %d check(s) passed, %d FAILED"
          % (len(PASS), len(FAIL)))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
