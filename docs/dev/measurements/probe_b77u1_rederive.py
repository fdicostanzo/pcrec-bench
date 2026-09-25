#!/usr/bin/env python3
"""probe_b77u1_rederive.py -- [B77] lane U1's ACCEPTANCE PROOF
(docs/design/utf8_set_v1.md 13 + 15 R1): every existing
`bench/*/expectations.tsv` re-derives BYTE-IDENTICALLY under the CHANGED
oracle (the per-pattern option word + the character-boundary find-all
advance) when no UTF option is requested -- with NEGATIVE arms showing the
comparison can fail.

Method (every arm prints one line; the archive of a run is its stdout):

  P0  PRECONDITION: for every pattern of every set, the option word the
      changed code computes (`pcrecbench.expectations.oracle_option_word`)
      is 0 and `sb.encoding == "byte"` -- i.e. "no UTF option requested"
      is a MEASURED fact about each set, not an assumption.
  P1  THE PROOF: each set's OWN `gen_expectations.py` (the real CLI, the
      path `make check-harness` runs) is invoked with `--out` into a
      scratch directory; the output is compared BYTE FOR BYTE (`cmp`
      semantics, Python `==` on bytes) with the committed file; both
      sha256s and the row count are printed.
  N1  COMPARATOR CONTROL: a copy of each committed file with ONE byte of
      one data row changed must compare UNEQUAL -- the comparator is not
      vacuous.
  N2  PIPELINE CONTROL: each set re-derived IN-PROCESS with the option word
      sabotaged to PCRE2_ANCHORED (0x80000000, a legal COMPILE option:
      every search anchored at its start offset) must come out DIFFERENT
      from the
      committed file -- proving the derivation actually reads the option
      word (the new parameter is live, not bypassed), so P1's identity is
      the word being 0 and not the word being ignored. bench/email carries
      its own local derive() (it predates the shared module); its
      sabotage patches `oracle.compile` instead, which is where its local
      copy takes the word.
  I1  (informational, --utf) the same in-process derivation with PCRE2_UTF
      forced on, per set: identical / differs / giveups. Not a pass/fail
      arm -- it says which sets' answers the UTF bit would move at all.

Usage:  python3 docs/dev/measurements/probe_b77u1_rederive.py [--out DIR]
        [--sets a,b] [--utf]
Exit 0 iff P0, P1, N1 and N2 all pass.
"""
import argparse
import hashlib
import importlib.util
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from pcrecbench import expectations as _exp  # noqa: E402
from pcrecbench import oracle_pcre2 as _o  # noqa: E402
from pcrecbench.subbench import load as _load  # noqa: E402

SETS = ("email", "loglines", "bounded", "altwide", "syntax", "capability")
# The N2 sabotage. PCRE2_CASELESS (0x8) was tried FIRST and is NOT a usable
# control: bench/loglines re-derives IDENTICALLY under it (its patterns and
# subjects do not depend on case) -- so a sabotage must be chosen that moves
# an answer on EVERY set, and anchoring every search does.
PCRE2_SABOTAGE = 0x80000000   # PCRE2_ANCHORED as a compile option


def sha(b):
    return hashlib.sha256(b).hexdigest()


def text_of(rows):
    return (_exp.HEADER + "\n" + "\n".join("\t".join(r) for r in rows)
            + "\n").encode("utf-8")


def derive_with_word(name, sb, word):
    """In-process re-derivation with every pattern's option word forced to
    `word`. Returns (bytes, ngiveups)."""
    real_word = _exp.oracle_option_word
    real_compile = _o.compile
    try:
        if name == "email":
            spec = importlib.util.spec_from_file_location(
                "b77u1_email_gen", os.path.join(ROOT, "bench", "email",
                                                "gen_expectations.py"))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            mod.oracle.compile = lambda p, options=0: real_compile(p, word)
            rows, giveups, _v = mod.derive(sb)
        else:
            _exp.oracle_option_word = lambda _sb, _p: word
            rows, giveups, _v = _exp.derive(sb)
    finally:
        _exp.oracle_option_word = real_word
        _o.compile = real_compile
    return text_of(rows), len(giveups)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join("/var/tmp", "b77u1-rederive"))
    ap.add_argument("--sets", default=",".join(SETS))
    ap.add_argument("--utf", action="store_true")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    sets = [s for s in args.sets.split(",") if s]
    fails = 0
    print("libpcre2 %s; repo %s; git HEAD %s" % (
        _o.version(), ROOT, subprocess.run(
            ["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True,
            text=True).stdout.strip()))
    for name in sets:
        bench = os.path.join(ROOT, "bench", name)
        committed_path = os.path.join(bench, "expectations.tsv")
        with open(committed_path, "rb") as f:
            committed = f.read()
        sb = _load(bench)

        # P0
        words = sorted({_exp.oracle_option_word(sb, p) for p in sb.patterns})
        p0 = (words == [0] and sb.encoding == "byte")
        print("P0 %-10s encoding=%s option words over %d patterns=%s -> %s"
              % (name, sb.encoding, len(sb.patterns), words,
                 "PASS" if p0 else "FAIL"))
        fails += not p0

        # P1 -- the set's own CLI
        out = os.path.join(args.out, name + ".expectations.tsv")
        t0 = time.time()
        proc = subprocess.run(
            ["/usr/bin/gnutimeout", "3600", sys.executable,
             os.path.join(bench, "gen_expectations.py"), "--out", out],
            capture_output=True, text=True, cwd=ROOT)
        dt = time.time() - t0
        if proc.returncode != 0 or not os.path.exists(out):
            print("P1 %-10s gen_expectations.py rc=%d: %s -> FAIL"
                  % (name, proc.returncode, proc.stderr[-400:]))
            fails += 1
            continue
        with open(out, "rb") as f:
            derived = f.read()
        same = derived == committed
        nrows = committed.count(b"\n") - 1
        print("P1 %-10s rows=%d committed=%s derived=%s (%.1fs) -> %s"
              % (name, nrows, sha(committed)[:16], sha(derived)[:16], dt,
                 "BYTE-IDENTICAL" if same else "DIFFERS (FAIL)"))
        fails += not same

        # N1 -- one byte of the last data row changed
        mutated = bytearray(committed)
        i = committed.rstrip(b"\n").rfind(b"\t") + 1   # the oracle column
        mutated[i] = ord("X") if mutated[i] != ord("X") else ord("Y")
        n1 = bytes(mutated) != derived
        print("N1 %-10s one-byte-mutated copy vs derived -> %s"
              % (name, "UNEQUAL (PASS: the comparator can fail)" if n1
                 else "EQUAL (FAIL)"))
        fails += not n1

        # N2 -- sabotaged option word
        t0 = time.time()
        sab, ng = derive_with_word(name, sb, PCRE2_SABOTAGE)
        n2 = sab != committed
        print("N2 %-10s option word forced to PCRE2_ANCHORED: %s giveups=%d "
              "(%.1fs) -> %s" % (name, sha(sab)[:16], ng, time.time() - t0,
                                 "DIFFERS (PASS: the word is live)" if n2
                                 else "IDENTICAL (FAIL)"))
        fails += not n2

        # I1 -- informational
        if args.utf:
            t0 = time.time()
            try:
                u, ng = derive_with_word(name, sb, _o.PCRE2_UTF)
                print("I1 %-10s option word forced to PCRE2_UTF: %s giveups=%d "
                      "(%.1fs) -> %s" % (name, sha(u)[:16], ng, time.time() - t0,
                                         "identical" if u == committed
                                         else "differs"))
            except _o.Pcre2Error as e:
                print("I1 %-10s PCRE2_UTF: compile refused: %s" % (name, e))
    print("RESULT %s (%d failing arm(s))" % ("PASS" if not fails else "FAIL",
                                             fails))
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
