"""python3 -m pcrecbench -- the harness CLI (harness contract 4).

    run      measure one cell and write one record
    quick    ONE pattern x ONE regime for one or two testees, tier scratch,
             the comparable printed inline (the edit-test loop, I-4 (b))
    index    regenerate <store>/index.tsv
    quiet    sample the box and print the quiet-box verdict (OD-B8)
    testees  list the testees the adapters provide
    report   the query -> report reducer (pcrecbench/report.py, [B5])
"""

import argparse
import os
import sys
import time

from . import HARNESS_VERSION


def cmd_run(args):
    from . import harness, quiet, store, adapters, env, subbench
    try:
        path, rid, setup, rows = harness.run_cell(
            args.subbench, args.testee,
            regimes=args.regimes, trials=args.trials, iters=args.iters,
            force_unquiet=args.force_unquiet, store_root=args.store,
            machine_id=args.machine_id, pin_cpu=args.pin,
            subject_timeout=args.subject_timeout,
            driver_timeout=args.driver_timeout,
            command_line=["python3", "-m", "pcrecbench"] + sys.argv[1:],
            note=args.note, synthetic=args.synthetic,
            tier=args.tier,
            progress=(lambda *a: print(*a, file=sys.stderr)) if not args.quiet_output else None)
    except quiet.QuietRefusal as e:
        print("pcrecbench run: %s" % e, file=sys.stderr)
        return 3
    except (harness.HarnessError, store.StoreError,
            adapters.AdapterError, env.MachineRegistryError,
            subbench.SubbenchError) as e:
        print("pcrecbench run: %s" % e, file=sys.stderr)
        return 1
    ncomp = sum(1 for r in rows if r["kind"] == "compile")
    nmatch = len(rows) - ncomp
    print("%s" % path)
    print("record_id  %s" % rid)
    print("tier       %s" % setup.get("tier", "pinned"))
    print("status     %s" % setup["status"])
    print("rows       %d (%d compile, %d match)" % (len(rows), ncomp, nmatch))
    return 0


# `quick` speaks the loop's spellings and the sub-bench's; both map to the
# contract's short regime names (subbench.REGIME_TO_ENUM's keys).
QUICK_REGIMES = {"search": "search_short", "search_short": "search_short",
                 "match": "match", "throughput": "throughput"}


def cmd_quick(args):
    """I-4 (b): one cell, one or two testees, seconds not minutes. Every
    record is `tier: scratch` (the store refuses the canonical tree); the
    comparable printed is `reduce.reduce_set_cell` applied to the record
    just written -- the SAME function the reporter ranks with (R5) -- so
    the number on the screen is the number a report would show."""
    from . import harness, quiet, store, adapters, env, subbench
    from . import reduce as rd
    from .subbench import REGIME_TO_ENUM

    regime = QUICK_REGIMES[args.regime]
    enum = REGIME_TO_ENUM[regime]
    testees = [args.testee] + ([args.vs] if args.vs else [])
    store_root = args.store or store.scratch_store()
    say = (lambda *a: print(*a, file=sys.stderr)) if not args.quiet_output \
        else (lambda *a: None)
    t0 = time.monotonic()
    results = []
    for tid in testees:
        try:
            res = harness.run_cell(
                args.subbench, tid, regimes=[regime], trials=args.trials,
                iters=args.iters, store_root=store_root,
                machine_id=args.machine_id, pin_cpu=args.pin,
                subject_timeout=args.subject_timeout,
                driver_timeout=args.driver_timeout,
                command_line=["python3", "-m", "pcrecbench"] + sys.argv[1:],
                note="quick: %s / %s / %s, %s subject(s), %d trial(s), "
                     "budget %g s%s"
                     % (args.subbench, args.pattern, regime,
                        args.subjects if args.subjects else "all", args.trials,
                        args.budget, " -- vs %s" % args.vs if args.vs else ""),
                synthetic=args.synthetic, tier=store.TIER_SCRATCH,
                patterns=[args.pattern], subject_limit=args.subjects,
                budget=args.budget, progress=say)
        except quiet.QuietRefusal as e:       # cannot happen at scratch
            print("pcrecbench quick: %s" % e, file=sys.stderr)
            return 3
        except (harness.HarnessError, store.StoreError, adapters.AdapterError,
                env.MachineRegistryError, subbench.SubbenchError) as e:
            print("pcrecbench quick: %s" % e, file=sys.stderr)
            return 1
        results.append((tid, res))
    wall = time.monotonic() - t0

    # -- the comparable ---------------------------------------------------
    reduced = []
    for tid, res in results:
        cells = rd.cells_from_record(res.rows)
        # one pattern x one regime -> one cell; the FORM is whatever the
        # adapter measured the regime on (pcrec's match = whole-subject).
        mine = {k: v for k, v in cells.items()
                if k[0] == args.pattern and k[1] == enum}
        if len(mine) != 1:
            print("pcrecbench quick: expected one cell for (%s, %s) in %s, "
                  "found %d" % (args.pattern, enum, res.path, len(mine)),
                  file=sys.stderr)
            return 1
        (form,), = [tuple(k[2:]) for k in mine]
        reduced.append((tid, res, form, rd.reduce_set_cell(next(iter(mine.values())))))

    n_subj = reduced[0][3].n_subjects
    print("quick  %s / %s / %s   %d subject(s), %d trial(s), tier scratch"
          % (args.subbench, args.pattern, regime, n_subj, args.trials))
    print("%-14s %-14s %14s %14s %14s %6s  %-22s %s"
          % ("testee", "form", "median ns/call", "min", "max", "pass",
             "give-ups", "status"))
    for tid, res, form, r in reduced:
        med = "%.3f" % r.median_ns if r.median_ns is not None else "-"
        mn = "%.3f" % r.min_ns if r.min_ns is not None else "-"
        mx = "%.3f" % r.max_ns if r.max_ns is not None else "-"
        passed = "%d/%d" % (r.n_agreeing, r.n_subjects)
        gu = (", ".join("%s x%d" % (c, n) for c, n in sorted(r.giveup_codes.items()))
              if r.giveup_codes else "-")
        print("%-14s %-14s %14s %14s %14s %6s  %-22s %s"
              % (tid, form, med, mn, mx, passed, gu, res.setup["status"]))
        if r.failing_subjects:
            print("%-14s   EXCLUDED: %d failing subject(s): %s"
                  % ("", len(r.failing_subjects),
                     ", ".join("%s (%s)" % (
                         sid, "/".join("%s x%d" % kv for kv in sorted(
                             r.failing_detail[sid].outcome_counts.items())
                             if kv[0] != "matched-as-expected"))
                         for sid in r.failing_subjects[:8])
                     + (" ..." if len(r.failing_subjects) > 8 else "")))
    if len(reduced) == 2:
        a, b = reduced[0][3], reduced[1][3]
        if a.median_ns is not None and b.median_ns is not None and b.median_ns:
            ratio = a.median_ns / b.median_ns
            print("ratio  %s / %s = %.3fx  (%s is %.2fx %s)"
                  % (reduced[0][0], reduced[1][0], ratio, reduced[0][0],
                     ratio if ratio >= 1 else 1 / ratio,
                     "slower" if ratio >= 1 else "faster"))
        else:
            print("ratio  %s / %s = -  (a cell is excluded; no number to compare)"
                  % (reduced[0][0], reduced[1][0]))
    print("wall   %.1f s" % wall)
    for tid, res, _f, _r in reduced:
        print("record %s" % res.path)
    if args.report:
        print("report: python3 -m pcrecbench report --store %s --subbench %s "
              "--regime %s%s   (the reporter is [B5]'s; quick writes no "
              "report file)"
              % (store_root, reduced[0][1].setup["subbench"]["id"], enum,
                 " --include-synthetic" if args.synthetic else ""))
    return 0


def cmd_index(args):
    from . import store
    n = store.index(args.store)
    print("index: %d record(s) -> %s"
          % (n, os.path.join(args.store, "index.tsv")))
    return 0


def cmd_quiet(args):
    from . import quiet
    worst = None
    for i in range(args.samples):
        load = quiet.loadavg()
        occ = quiet.occupancy(exclude_cpu=args.pin)
        print("load1 %.2f  occupancy %s  max_busy_pct %s"
              % (load[0], occ["verdict"], occ["max_busy_pct"]))
        if occ["max_busy_pct"] is not None:
            worst = max(worst or 0.0, occ["max_busy_pct"])
    print()
    print("thresholds in force: load1 <= %.2f, max_busy_pct <= %.2f"
          % (quiet.LOAD1_LIMIT, quiet.MAX_BUSY_PCT_LIMIT))
    print("derivation: docs/design/quiet_baseline.md")
    if worst is not None and worst > quiet.MAX_BUSY_PCT_LIMIT:
        print("VERDICT: NOT QUIET (worst sample %.2f%% busy)" % worst)
        return 3
    print("VERDICT: quiet")
    return 0


def cmd_testees(args):
    from . import adapters
    for tid, (engine, cfg) in sorted(adapters.all_testees().items()):
        print("%-16s %-8s %s" % (tid, engine, cfg.get("description", "")))
    return 0


def cmd_report(args):
    # Never reached: main() dispatches `report` to pcrecbench.report.main
    # before argparse so the reporter owns its own flags.
    from pcrecbench import report
    return report.main([])

def regimes_arg(s):
    from .subbench import REGIME_TO_ENUM
    out = [x.strip() for x in s.split(",") if x.strip()]
    bad = [x for x in out if x not in REGIME_TO_ENUM]
    if bad:
        raise argparse.ArgumentTypeError(
            "unknown regime(s) %s -- the sub-bench spellings are: %s"
            % (", ".join(bad), ", ".join(sorted(REGIME_TO_ENUM))))
    return out


def build_parser():
    from . import store
    p = argparse.ArgumentParser(
        prog="python3 -m pcrecbench",
        description="pcrec-bench: measure one cell, write one record "
                    "(docs/design/harness_contract.md).",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version",
                   version="pcrecbench %s" % HARNESS_VERSION)
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser(
        "run", help="measure one cell and write one record",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
A CELL is one (sub-bench version x testee) pair. The run refuses on a box
that is not quiet (exit 3) unless --force-unquiet, in which case the record
is written with status `inconclusive-load` and the reporter will not rank it.

NOTE ON --testee: the id here is the adapter's CONFIG id (`pcre2-jit`). The
record and the store path use the DERIVED testee_id
(`libpcre2_10.46_jit-caps-simdna`, record_schema.md 6.4), which carries the
engine, the probed version and the configuration, and which validate.py
checks (rule X5). `python3 -m pcrecbench testees` lists the config ids.""")
    r.add_argument("--subbench", required=True,
                   help="the sub-bench DIRECTORY name under bench/ (e.g. email)")
    r.add_argument("--testee", required=True,
                   help="the adapter's config id (see `testees`)")
    r.add_argument("--trials", type=int, default=5,
                   help="raw trials per (pattern, subject, regime) and per "
                        "compile; the record keeps every one and the REPORTER "
                        "reduces them (default: 5)")
    r.add_argument("--regimes", type=regimes_arg, default=None,
                   help="comma-separated subset of the sub-bench's declared "
                        "regimes: match, search_short, throughput "
                        "(default: all it declares)")
    r.add_argument("--iters", type=int, default=None,
                   help="fix the in-process loop count instead of "
                        "auto-calibrating it to a ~50 ms loop. `--iters 1` is "
                        "what a SMOKE uses; it is not a measurement")
    r.add_argument("--force-unquiet", action="store_true",
                   help="measure on a box that failed the quiet gate. The "
                        "record's status becomes `inconclusive-load` and the "
                        "reasons go in `status_detail`")
    r.add_argument("--tier", choices=list(store.TIERS), default=store.TIER_PINNED,
                   help="the record's TIER (record_schema.md 6.8). `pinned` "
                        "(default): a committed engine revision under the "
                        "quiet gate, into the canonical store. `scratch`: the "
                        "edit-test loop's tier -- no quiet gate, into the "
                        "scratch store, never ranked. A provided-binary "
                        "testee (pcrec-local) is scratch by construction")
    r.add_argument("--store", default=None,
                   help="the store root. Default: the TIER's store -- the "
                        "canonical %s for `pinned`, $PCRECBENCH_SCRATCH_STORE "
                        "or build/scratch-store/ for `scratch`. A scratch "
                        "record into the canonical store is REFUSED"
                        % os.path.relpath(store.DEFAULT_STORE, os.getcwd()))
    r.add_argument("--machine-id", default=None,
                   help="register THIS box under a stable slug. Required the "
                        "first time a box is measured; ids are hand-assigned "
                        "and never derived (record_schema.md 6.5)")
    r.add_argument("--pin", type=int, default=None, metavar="CPU",
                   help="pin the driver to one core with taskset, after the "
                        "occupancy check (requirements 9(d))")
    r.add_argument("--subject-timeout", type=int, default=60, metavar="SECS",
                   help="per-SUBJECT alarm inside the driver; the subject "
                        "that fires it is recorded `timed-out` by name "
                        "(0 = none, default: %(default)s)")
    r.add_argument("--driver-timeout", type=int, default=900, metavar="SECS",
                   help="gnutimeout on the driver PROCESS, the outer backstop "
                        "(default: %(default)s)")
    r.add_argument("--note", default=None,
                   help="a human sentence stored in the record's `note`")
    r.add_argument("--synthetic", action="store_true",
                   help="mark the record `synthetic` -- the reporter excludes "
                        "such records from every query. For fixtures and "
                        "smokes that must never be mistaken for measurements")
    r.add_argument("--quiet-output", action="store_true",
                   help="suppress the progress lines on stderr")
    r.set_defaults(func=cmd_run)

    q = sub.add_parser(
        "quick",
        help="one pattern x one regime, one or two testees, tier scratch, "
             "the comparable inline (seconds, not minutes)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
THE EDIT-TEST LOOP (inbox I-4 (b)). One CELL = one pattern x one regime x
the subjects (all, or the first k), for one testee or two. Every record is
`tier: scratch`: no quiet gate (the box is still sampled and `status` is
honest), written to the scratch store ($PCRECBENCH_SCRATCH_STORE or
build/scratch-store/), never to store/, never ranked. The comparable
printed is the reporter's own set-grain reduction (pcrecbench/reduce.py):
median over trials of the per-trial SUM of per-subject ns/call, with
min/max, pass-rate, give-ups by code, and the ratio testee/vs.

    python3 -m pcrecbench quick --subbench email --pattern orig \\
        --regime search --testee pcrec-local --vs pcre2-jit --subjects 10

`--regime search` is the sub-bench's `search_short`; both spellings work.""")
    q.add_argument("--subbench", required=True,
                   help="the sub-bench DIRECTORY name under bench/")
    q.add_argument("--pattern", required=True,
                   help="ONE pattern id of the sub-bench (e.g. orig)")
    q.add_argument("--regime", required=True, choices=sorted(QUICK_REGIMES),
                   help="ONE regime: search (= search_short), match, throughput")
    q.add_argument("--testee", required=True,
                   help="the adapter's config id (see `testees`)")
    q.add_argument("--vs", default=None, metavar="TESTEE",
                   help="a second testee; the ratio testee/vs is printed")
    q.add_argument("--trials", type=int, default=3,
                   help="raw trials per subject (default: %(default)s)")
    q.add_argument("--iters", type=int, default=None,
                   help="fix the loop count instead of calibrating it "
                        "(--iters 1 is a smoke, not a measurement)")
    q.add_argument("--subjects", type=int, default=None, metavar="K",
                   help="the FIRST k subjects of the regime's set "
                        "(default: all of them)")
    q.add_argument("--budget", type=float, default=2.0, metavar="SECS",
                   help="per-trial calibration cap; the loop count is cut "
                        "so one trial's predicted sweep stays inside it, "
                        "and the record's calibration_note says when it bound "
                        "(default: %(default)s; `run` uses 20)")
    q.add_argument("--store", default=None,
                   help="a SCRATCH store root (default: "
                        "$PCRECBENCH_SCRATCH_STORE or build/scratch-store/); "
                        "the canonical store is refused")
    q.add_argument("--report", action="store_true",
                   help="also print the `pcrecbench report` command line for "
                        "the full report over this scratch store. quick "
                        "itself writes no report file")
    q.add_argument("--machine-id", default=None,
                   help="register THIS box (only needed on a box the "
                        "canonical store's registry does not know)")
    q.add_argument("--pin", type=int, default=None, metavar="CPU",
                   help="pin the driver to one core with taskset")
    q.add_argument("--subject-timeout", type=int, default=60, metavar="SECS")
    q.add_argument("--driver-timeout", type=int, default=900, metavar="SECS")
    q.add_argument("--synthetic", action="store_true",
                   help="mark the records `synthetic` (smokes, fixtures)")
    q.add_argument("--quiet-output", action="store_true",
                   help="suppress the progress lines on stderr")
    q.set_defaults(func=cmd_quick)

    i = sub.add_parser("index", help="regenerate <store>/index.tsv (the "
                                     "canonical store's refuses to list a "
                                     "scratch record)")
    i.add_argument("--store", default=store.DEFAULT_STORE,
                   help="the store root (default: the canonical store; a "
                        "scratch store keeps its own index.tsv)")
    i.set_defaults(func=cmd_index)

    q = sub.add_parser("quiet", help="sample the box and print the verdict")
    q.add_argument("--samples", type=int, default=1)
    q.add_argument("--pin", type=int, default=None, metavar="CPU",
                   help="exclude this core from the occupancy check")
    q.set_defaults(func=cmd_quiet)

    t = sub.add_parser("testees", help="list the testees the adapters provide")
    t.set_defaults(func=cmd_testees)

    rep = sub.add_parser("report", help="the query -> report reducer (pcrecbench/report.py); its flags: python3 -m pcrecbench report --help")
    rep.set_defaults(func=cmd_report)
    return p


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv and argv[0] == "report":
        from pcrecbench import report
        return report.main(argv[1:])
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
