#!/usr/bin/env python3
"""The mojibake-curly-quote span probe (O-31 ask 4 / pcrecdev1's charter).

Runs one `quick` scratch cell per testee on bench/capability's
`mojibake-curly-quote` x `search_short` and prints every testee's
observation on subject `nu-mojibake` (raw bytes 93 68 65 6c 6c 6f 94,
i.e. \\x93hello\\x94; oracle libpcre2-differential says match [0,7)).

Findings this probe archives (2026-09-17, pin a770139e):
  - all four pcrec configs observe NOMATCH (a total dismissal, not a
    span disagreement), both pcre2 configs match as the oracle;
  - the within-set discriminator: `mojibake-curly-quote` is authored
    `pattern-esc "\\x93[\\\\x20-\\\\x7e]*\\x94"`, so its pattern TEXT
    carries RAW bytes 0x93/0x94; its clean family sibling
    `utf8-lead-no-cont` (`pattern [\\xc2-\\xdf](?![\\x80-\\xbf])`)
    spells its high bytes as REGEX-LEVEL escapes and matches correctly
    on every pcrec config (this sample's report, no exclusion row).
    The divergence therefore tracks RAW HIGH LITERAL BYTES IN THE
    PATTERN TEXT, not high bytes in the subject (nu-lead-no-cont's
    subject carries a raw 0xC2 and pcrec answers it right) and not the
    bench's `.rxt` load path (the pcre2 arms receive the same bytes
    from the same loader and match).

Usage: python3 docs/dev/measurements/probe_mojibake_span.py
Runs from the repository root; writes its scratch store under
$PCRECBENCH_SCRATCH_STORE or a tempdir; ~15 s on a quiet box.
"""
import glob
import json
import os
import subprocess
import sys
import tempfile

TESTEES = ["pcrec-auto", "pcrec-nocaps", "pcrec-vm", "pcrec-vm-in",
           "pcre2-jit", "pcre2-interp"]
SUBJECT = "nu-mojibake"


def main():
    store = os.environ.get("PCRECBENCH_SCRATCH_STORE")
    tmp = None
    if not store:
        tmp = tempfile.TemporaryDirectory(prefix="mojibake-probe-")
        store = tmp.name
        os.environ["PCRECBENCH_SCRATCH_STORE"] = store
    for t in TESTEES:
        rc = subprocess.call(
            ["gnutimeout", "600", sys.executable, "-m", "pcrecbench",
             "quick", "--subbench", "capability",
             "--pattern", "mojibake-curly-quote",
             "--regime", "search_short", "--testee", t,
             "--trials", "1", "--iters", "1", "--quiet-output"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("quick %-14s rc=%d" % (t, rc))
    print()
    for f in sorted(glob.glob(os.path.join(
            store, "records", "capability@0.1", "*", "*.jsonl"))):
        testee = os.path.basename(os.path.dirname(f))
        for line in open(f):
            row = json.loads(line)
            if row.get("kind") == "match" and \
                    row.get("subject_id") == SUBJECT:
                o = row.get("observed") or {}
                print("%-44s outcome=%-28s matched=%s span=%s diag=%s"
                      % (testee, row.get("match_outcome"),
                         o.get("matched"), o.get("span"),
                         row.get("diagnostic")))
                break


if __name__ == "__main__":
    main()
