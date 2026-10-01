#!/usr/bin/env python3
"""probe_b119k75_utf8_wellformedness_census.py -- [B119], inbox I-123
(K75, D132): is there ANY cell of ours whose subject could be ill-formed
UTF-8 under our `--utf8` find-all protocol flag?

THE QUESTION. pcrec's find-all loop now aligns the resume position past
UTF-8 continuation bytes after a NON-EMPTY match (match_api.md S3.1.1,
K75). Our own formula (`pcrecbench/oracle_pcre2.py:next_start`, and the
identical `utf8_next_start()` in every `testees/*/driver.c`) would need
the same alignment for any cell where OUR `--utf8` protocol flag fires
and the subject MIGHT be ill-formed. `--utf8` fires iff
`pcrecbench.expectations.utf8_advance(sb, pattern)` is true, which is
true iff the sub-bench's sidecar declares `[expectations] encoding =
"utf8"` (`pcrecbench/subbench.py`) -- a fact of the SET, never of which
testee runs it. Grepping every `bench/*/subbench.toml` shows exactly one
set makes that declaration: `bench/utf8@0.1`. The other seven
(`altwide`, `bounded`, `capability`, `email`, `litrun`, `loglines`,
`syntax`) default to `byte`, confirmed live by `make check-harness`'s
`check_utf8_find_all_advance` ("option word: 0 on every pattern of every
byte set -- 7 set(s): altwide, bounded, capability, email, litrun,
loglines, syntax").

So the only subjects this question is ever ABOUT are bench/utf8@0.1's
own 98 (91 `search_short` + 7 `throughput`). This probe re-derives that
from first principles rather than trusting the generator's own
`decode_gate()` control: a from-scratch UTF-8 validator (RFC 3629 shape
-- lead byte decides sequence length, every continuation byte must be
0x80-0xBF, overlong encodings / surrogate code points U+D800-U+DFFF /
code points above U+10FFFF all rejected) that shares no source with
`bench/utf8/utf8text.py:decode_gate` or with Python's own
`bytes.decode("utf-8")` -- cross-checked against the latter anyway, so
the two independent opinions must agree. Every subject is also checked
for size and sha256 against its own manifest row first, so "checked" means
the exact bytes the manifest claims, not a stale file.

For completeness (never as an exposure -- see the probe's own printed
note) it also scans the OTHER seven sets' subjects, which turn up
deliberate or incidental non-UTF-8 bytes in three of them
(`bench/capability`'s `nu-*` family, documented in its own NOTES.md as
byte-mode witnesses; `bench/email`'s `s-019`; `bench/syntax`'s
`f-cafe`/`l-latin1` and all three throughput texts). None of these is a
"-e utf8 cell" by the definition above: their sets never set the oracle
word's PCRE2_UTF bit, so `--utf8` never reaches a driver there, no
matter which testee runs them.

Usage: python3 docs/dev/measurements/probe_b119k75_utf8_wellformedness_census.py
(run from the repo root; subjects must already be generated -- run each
bench/<name>/gen_subjects.py and gen_throughput_subjects.py first, or let
this probe do it automatically via --generate)
"""
import csv
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BENCH = os.path.join(ROOT, "bench")

# The eight committed sub-benches, by directory name (docs/dev/measurements
# probes name their inputs rather than discovering them, so a reader sees
# the exact population without having to run `ls`).
SETS = ("altwide", "bounded", "capability", "email", "litrun", "loglines",
        "syntax", "utf8")


def utf8_scan(data):
    """-> (ok: bool, first_bad_offset: int|None, reason: str|None).
    A from-scratch UTF-8 validator -- no library decoder, no decode_gate."""
    n = len(data)
    i = 0
    while i < n:
        b0 = data[i]
        if b0 < 0x80:
            i += 1
            continue
        if b0 < 0xC0:
            return False, i, "orphan continuation byte 0x%02x" % b0
        if b0 < 0xE0:
            length, minval, cp = 2, 0x80, b0 & 0x1F
        elif b0 < 0xF0:
            length, minval, cp = 3, 0x800, b0 & 0x0F
        elif b0 < 0xF5:
            length, minval, cp = 4, 0x10000, b0 & 0x07
        else:
            return False, i, "lead byte 0x%02x out of range" % b0
        if i + length > n:
            return False, i, ("truncated %d-byte sequence (only %d byte(s) "
                               "left)" % (length, n - i))
        for k in range(1, length):
            bk = data[i + k]
            if bk < 0x80 or bk > 0xBF:
                return False, i, (
                    "byte %d of a %d-byte sequence at offset %d is 0x%02x, "
                    "not a continuation byte (0x80-0xBF)"
                    % (k, length, i, bk))
            cp = (cp << 6) | (bk & 0x3F)
        if cp < minval:
            return False, i, ("overlong encoding (cp=U+%04X, length=%d)"
                               % (cp, length))
        if 0xD800 <= cp <= 0xDFFF:
            return False, i, "encodes a surrogate code point U+%04X" % cp
        if cp > 0x10FFFF:
            return False, i, "code point U+%X exceeds U+10FFFF" % cp
        i += length
    return True, None, None


def check_manifest(bench_dir, manifest_name, subdir):
    path = os.path.join(bench_dir, manifest_name)
    if not os.path.exists(path):
        print("  SKIP %s: not generated" % manifest_name)
        return 0, 0
    n_checked = n_bad = 0
    with open(path, newline="") as f:
        rdr = csv.reader(f, delimiter="\t")
        header = next(rdr)
        idx = {name: i for i, name in enumerate(header)}
        for row in rdr:
            if not row:
                continue
            sid = row[idx["id"]]
            declared_bytes = int(row[idx["len"]])
            declared_sha = row[idx["sha256"]] if "sha256" in idx else None
            fpath = os.path.join(bench_dir, subdir, sid + ".bin")
            with open(fpath, "rb") as sf:
                data = sf.read()
            n_checked += 1
            if len(data) != declared_bytes:
                n_bad += 1
                print("  SIZE MISMATCH %s: manifest says %d B, file is %d B"
                      % (sid, declared_bytes, len(data)))
                continue
            if declared_sha is not None:
                got_sha = hashlib.sha256(data).hexdigest()
                if got_sha != declared_sha:
                    n_bad += 1
                    print("  SHA256 MISMATCH %s: manifest %s, file %s"
                          % (sid, declared_sha, got_sha))
                    continue
            ok, off, reason = utf8_scan(data)
            try:
                data.decode("utf-8")
                py_ok = True
            except UnicodeDecodeError:
                py_ok = False
            if py_ok != ok:
                n_bad += 1
                print("  DISAGREEMENT %s: from-scratch scanner=%s, "
                      "bytes.decode=%s (treated as bad)" % (sid, ok, py_ok))
            elif not ok:
                n_bad += 1
                print("  ILL-FORMED %s (%d B) at offset %d: %s"
                      % (sid, len(data), off, reason))
    print("  %s: %d subject(s) checked, %d bad"
          % (manifest_name, n_checked, n_bad))
    return n_checked, n_bad


def main():
    generate = "--generate" in sys.argv[1:]
    grand_checked = grand_bad = 0
    utf8_bad = 0
    for name in SETS:
        bdir = os.path.join(BENCH, name)
        print("== %s ==" % name)
        if generate:
            for script in ("gen_subjects.py", "gen_throughput_subjects.py"):
                sp = os.path.join(bdir, script)
                if os.path.exists(sp):
                    subprocess.run([sys.executable, sp], cwd=bdir,
                                   check=True, stdout=subprocess.DEVNULL)
        c1, b1 = check_manifest(bdir, "manifest.tsv", "subjects")
        c2, b2 = check_manifest(bdir, "manifest_throughput.tsv", "throughput")
        grand_checked += c1 + c2
        grand_bad += b1 + b2
        if name == "utf8":
            utf8_bad = b1 + b2
    print()
    print("TOTAL: %d subject(s) checked across all %d set(s), %d bad"
          % (grand_checked, len(SETS), grand_bad))
    print()
    print("K75 ANSWER: bench/utf8@0.1 (the only set whose [expectations] "
          "encoding = \"utf8\", the only one our --utf8 driver flag ever "
          "fires for) carries %d ill-formed subject(s) of its own 98." % utf8_bad)
    if utf8_bad == 0:
        print("  -> NO -e utf8 cell of ours can carry an ill-formed "
              "subject today. No alignment fix needed; no code changed.")
    if grand_bad - utf8_bad:
        print("  (The %d bad byte sequence(s) found in OTHER, byte-encoded "
              "sets are deliberate/incidental byte-mode witnesses -- see "
              "bench/capability/NOTES.md's `nu-*` family -- and are "
              "irrelevant here: their sets never set PCRE2_UTF, so --utf8 "
              "never reaches a driver on them regardless of which testee "
              "runs there.)" % (grand_bad - utf8_bad))
    sys.exit(0)


if __name__ == "__main__":
    main()
