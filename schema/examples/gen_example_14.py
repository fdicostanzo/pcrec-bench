#!/usr/bin/env python3
"""gen_example_14.py -- GENERATE the schema v1.4 good example, deterministically.

docs/design/gate_shape_v14.md 4 E1: the 1.4 example is BUILT FROM the pcrec
1.1 example beside it (the precedent since 1.1 -> 1.2 is that no example is
ever re-stamped; the 1.1 and 1.2 files stay at their versions so `make
check-schema` proves the minor bumps are additive) and is generated rather
than hand-written, because five trials x every match-row key with dense
`seq` and per-row `calibration` is not hand-edit material -- and because
every sabotage in `bad/` that controls a v1.4 rule is a ONE-FIELD mutation
of this file's output, so the output has to be reproducible to the byte.

What it exercises, all in one record that VALIDATES (E1):

  * `schema_version` 1.4, `tier: pinned`, a new `run.timestamp` (so a new
    `record_id`, a new file name, a re-stamped `content_hash`);
  * every match-row key GROWN TO 5 TRIALS (X9 dense 1..5; X18 `seq`
    renumbered dense over ALL rows; X21 calibration on every timed row);
  * `pinning.cpu = 2` with `occupancy.<sample>.target_busy_pct` on BOTH
    samples (a number under the limit on `before`; our own driver's decay
    on `after`);
  * a FAILED after sample (`occupancy.after.verdict = fail` at 20.20 %,
    X26 holding) and `load.after.load1 = 11.40` with `load.verdict =
    loaded` (X20 holding) beside `status = measured` -- the after samples
    are PROVENANCE at 1.4 (the same sabotages `bad/x13-occupancy-after-fail`
    and `bad/x13-measured-but-loaded` are REJECTED at 1.1: one sabotage,
    two versions, two verdicts);
  * the `trial_agreement` block, computed by the HARNESS's own derivation
    (`pcrecbench.reduce.judge_trial_agreement`) so that `make check-schema`
    proves the validator's independent second implementation (X32) agrees
    with it -- verdict `agree`, 5 trials;
  * ONE `did-not-compile` compile row carrying `cost` (S5, KB-4's schema
    half: the bench's own clock around the engine's exec);
  * a per-group occupancy `timeline` with one item per (pattern, regime,
    form) group (S6, provenance).

Usage:
    python3 schema/examples/gen_example_14.py            # (re)write the file
    python3 schema/examples/gen_example_14.py --check    # exit 1 if the
                                                         # committed file differs
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "schema"))

from pcrecbench.reduce import judge_trial_agreement   # noqa: E402  the harness's derivation
import validate as V                                   # noqa: E402  the shared validator

SOURCE = os.path.join(
    HERE, "email-specimen@0.1__pcrec_0.9.0-g1a2b3c4_vm-caps-simdna__example-box"
          "__20260825T031800Z.jsonl")
TIMESTAMP = "2026-08-30T12:00:00Z"
TRIALS = 5


def dumps(obj):
    """The store's own serialization (store.serialize): sorted keys, compact
    separators, UTF-8 kept -- so the example is byte-shaped like a record."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def load_source():
    with open(SOURCE, encoding="utf-8") as fh:
        lines = [ln for ln in fh.read().split("\n") if ln.strip()]
    return json.loads(lines[0]), [json.loads(ln) for ln in lines[1:]]


def grow_trials(rows):
    """Every match-row KEY gets trials 1..TRIALS. A timed row's extra trials
    take elapsed_ns values derived from the existing ones (a deterministic
    +0.8 % / -0.6 % of trial 1 -- inside the box's own spread, nothing
    the rule notices); an untimed (failing) row is repeated as it is."""
    out = []
    by_key = {}
    for r in rows:
        if r.get("kind") != "match":
            out.append(r)
            continue
        key = (r["pattern_id"], r["regime"], r.get("form", "plain"), r["subject_id"])
        by_key.setdefault(key, []).append(r)
        out.append(r)
        # append the grown trials right after the key's LAST existing trial
        existing = by_key[key]
        if len(existing) == sum(1 for x in rows if x.get("kind") == "match"
                                and (x["pattern_id"], x["regime"], x.get("form", "plain"),
                                     x["subject_id"]) == key):
            first = existing[0]
            for t in range(len(existing) + 1, TRIALS + 1):
                g = json.loads(json.dumps(first))
                g["trial"] = t
                if "timing" in g:
                    base = first["timing"]["elapsed_ns"]
                    factor = {4: 1.008, 5: 0.994}.get(t, 1.0)
                    g["timing"]["elapsed_ns"] = int(round(base * factor))
                out.append(g)
    return out


def main(argv):
    check = "--check" in argv
    setup, rows = load_source()

    # -- identity, version, tier ------------------------------------------
    setup["schema_version"] = "1.4"
    setup["tier"] = "pinned"
    setup["run"]["timestamp"] = TIMESTAMP
    setup["run"]["run_id"] = "example-run-0014"
    setup["run"]["command_line"] = [
        "python3", "-m", "pcrecbench", "run", "--subbench", "email",
        "--testee", "pcrec-vm", "--trials", "5", "--pin", "2"]
    setup["note"] = (
        "SYNTHETIC EXAMPLE (schema v1.4, GENERATED by schema/examples/"
        "gen_example_14.py from the 1.1 pcrec example) -- every value is "
        "INVENTED to exercise the schema; no engine was run, no box was quiet, "
        "the timings are made up, and the reporter excludes `synthetic` records "
        "from every query. | after-sample (provenance, not a verdict): occupancy "
        "after the run 20.20% busy on the busiest non-target core (limit 10.00%); "
        "the trials' agreement decided the status (v1.4 X13); after-sample "
        "(provenance, not a verdict): load1 after the run 11.40 exceeds the limit "
        "6.00; the trials' agreement decided the status (v1.4 X13)")

    # -- the samples: the pre-flight clean, the after samples FAILED ----------
    env = setup["environment"]
    env["load"]["before"].update({"sampled_at": "2026-08-30T11:59:52Z"})
    env["load"]["after"] = {"loadavg_raw": "11.40 8.00 5.00 9/561 41880",
                            "sampled_at": "2026-08-30T12:00:44Z",
                            "load1": 11.4, "load5": 8.0, "load15": 5.0}
    env["load"]["verdict"] = "loaded"
    occ = env["occupancy"]
    occ["tool"] = "mpstat -P ALL 1 5"
    occ["before"] = {
        "verdict": "pass", "max_busy_pct": 1.2, "target_busy_pct": 1.5,
        "raw": "(illustrative) the mpstat -P ALL 1 5 Average: block taken BEFORE "
               "the run; a real record carries it verbatim, one line per core, "
               "plus the per-second peaks and the target cpu2 line (BD7)"}
    occ["after"] = {
        "verdict": "fail", "max_busy_pct": 20.2, "target_busy_pct": 37.4,
        "raw": "(illustrative) the same block taken AFTER the run -- a SECOND "
               "sample: one non-target core read 20.20% over the five seconds "
               "(a competitor that arrived as the cell ended), and the target "
               "cpu2 reads our own driver's decay. PROVENANCE at v1.4, never a "
               "verdict on the status"}
    assert env["pinning"] == {"mode": "chrt+taskset", "cpu": 2}

    # -- rows: grown to 5 trials; one refusal carrying its cost (KB-4) --------
    rows = grow_trials(rows)
    for r in rows:
        if r.get("kind") == "compile" and r["pattern_id"] == "p-backref-domain":
            r["compile_outcome"] = "did-not-compile"
            r.pop("declaration_ref", None)
            r["diagnostic"] = ("pcrec: backreference \\k<lab> is module 'backrefs', "
                               "not implemented at this pin (illustrative refusal)")
            # S5 / KB-4: the bench's clock around the pcrec exec, on a refusal
            r["cost"] = {"total_ns": 1310000}
    for i, r in enumerate(rows, start=1):
        r["seq"] = i

    # -- the per-group occupancy timeline (3.6, provenance) -----------------
    groups = []
    for r in rows:
        if r.get("kind") != "match":
            continue
        key = (r["pattern_id"], r["regime"], r.get("form", "plain"))
        if key not in groups:
            groups.append(key)
    illustrative = {
        ("p-addrspec", "match-compliance", "whole-subject"): (3810, 99.7, 1.1, 2.4, 7),
        ("p-addrspec", "large-subject-throughput", "plain"): (412, 98.9, 0.8, 3.0, 9),
        ("p-quoted-local", "short-subject-search", "plain"): (1345, 99.5, 1.3, 2.1, 4),
        ("p-quoted-local", "match-compliance", "whole-subject"): (96, 97.2, 0.9, 2.6, 7),
    }
    occ["timeline"] = []
    for key in groups:
        ms, tgt, sib, oth, cpu = illustrative[key]
        occ["timeline"].append({
            "pattern_id": key[0], "regime": key[1], "form": key[2],
            "elapsed_ms": ms, "target_busy_pct": tgt, "sibling_busy_pct": sib,
            "max_other_busy_pct": oth, "max_other_cpu": cpu})
    occ["timeline_tool"] = "/proc/stat"

    # -- the block, by the harness's own derivation (X32 re-derives it) -------
    setup["trial_agreement"] = judge_trial_agreement(rows)
    assert setup["trial_agreement"]["verdict"] == "agree", setup["trial_agreement"]
    setup["status"] = "measured"

    # -- identity re-derived, hash re-stamped ---------------------------------
    setup["record_id"] = V.derive_record_id(setup)
    row_lines = [dumps(r) for r in rows]
    setup["content_hash"] = {"algorithm": "sha256",
                             "value": V.compute_content_hash(setup, row_lines)}
    text = "\n".join([dumps(setup)] + row_lines) + "\n"
    target = os.path.join(HERE, setup["record_id"] + ".jsonl")

    if check:
        try:
            with open(target, encoding="utf-8") as fh:
                committed = fh.read()
        except OSError:
            print("gen_example_14: %s is MISSING" % target, file=sys.stderr)
            return 1
        if committed != text:
            print("gen_example_14: the committed 1.4 example differs from what "
                  "this generator produces; regenerate it (and re-derive every "
                  "bad/ sabotage of it)", file=sys.stderr)
            return 1
        print("gen_example_14: OK -- %s reproduces byte for byte"
              % os.path.basename(target))
        return 0
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("gen_example_14: wrote %s (%d rows)" % (target, len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
