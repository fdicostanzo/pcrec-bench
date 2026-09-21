#!/usr/bin/env python3
"""probe_altwide_rung_attribution.py -- [B65], inbox I-80: THE RUNG
ATTRIBUTION for [B63]'s altwide DFA/auto refusal-boundary move.

[B63]'s window found the DFA/auto route's compile-time refusal set on
bench/altwide@0.2 SHRANK from 18 patterns at pcrec d34c9131 to 4 at
25b1984f (`docs/dev/lanes/b63window_report.md` section 3) -- i.e. 14
patterns that refused before now compile. This project's own committed
prose (reports/CLAUDE.md, O-40) stated the mechanism as a HYPOTHESIS:
cf0962e3's `[OPT-DIAL]`/K59 "premul drop-ladder rung", explicitly
labelled unproven.

pcrec's own reading, inbox I-80, CORRECTS this: the mechanism is
`Ctx.size_drop_rung`, a TWO-RUNG retry ladder stamped
`RX_ENGINE_SEL "size-cap-retry"`:
  - rung 1 -- SDR_NO_ANCHORED (K53-SELRETRY, fixed 2026-09-10): drop the
    OPTIONAL anchored match-here machine ([ENG-ABS]); `RX_DFA_MATCH`
    falls back to `"search-filter"`.
  - rung 2 -- SDR_NO_PREMUL (K59, fixed 2026-09-17): if STILL over the
    cap after rung 1, additionally drop the premultiplied DFA
    transition table.
Rungs are ORDINAL and compose (rung 2 implies rung 1 already fired).
CAUTION (I-80, confirmed live below): `RX_DFA_TABLE "mixed"` is NOT
evidence rung 2 fired -- the artifact's OWN `pcrec: note:` line(s), one
per rung, are the only correct attribution, because a machine can read
"mixed" (its surviving machines differ in FORM) under rung 1 alone.

This probe re-emits each of the 14 rescued patterns, BOTH forms (plain,
whole-subject `(?:<pattern>)\\z`), through the pinned 25b1984f binary,
under testees/pcrec/adapter.py's REAL phase-1 argv shape
(`-p rx -fcomments --features all -o artifact.c -- <pattern>`, the
[B58] `-fcomments` protocol token included, per-pattern-per-form
`artifact.c` basename so byte counts compare directly against the
store's own committed records), and:
  1. verifies the pattern text against the pattern's own
     `canonical_sha256` in the d34c9131 store record (never retyped);
  2. captures pcrec's stderr VERBATIM and extracts every `pcrec: note:`
     line (the rung(s) fired) and `pcrec: warning:` line (the size);
  3. reads `RX_ENGINE_SEL` / `RX_DFA_TABLE` / `RX_DFA_MATCH` /
     `RX_DFA_PREFILTER` / `RX_ENGINE` off the emitted .c (comments on,
     so the rx_info doc-comment block and the macro `#define` lines are
     both present -- the macros are CODE, unaffected by [EMIT-VERB]);
  4. classifies each note line against the two known rung texts and
     FLAGS (does not silently absorb) any note line matching neither;
  5. cross-cites the OLD (d34c9131) refusal: for each pattern/form,
     whether the pattern's compile row in the d34c9131 store record was
     `did-not-compile`, and if so its verbatim `diagnostic` (the
     "pattern too large: N bytes ... (limit M)" line).

Compile-only: no timing, no dlopen, no driver, no quiet-box gate.
Nothing here is a ranking input.

Run from the repo root (or a worktree):
    python3 docs/dev/measurements/probe_altwide_rung_attribution.py
Output archived verbatim in
    docs/dev/measurements/2026-09-21-altwide-rung-attribution-25b1984f.txt
"""

import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()
COMMON = subprocess.check_output(
    ["git", "rev-parse", "--git-common-dir"], text=True
).strip()
if not os.path.isabs(COMMON):
    COMMON = os.path.abspath(os.path.join(ROOT, COMMON))
MAIN_TREE = os.path.dirname(COMMON)
BUILD_ROOT = os.path.join(MAIN_TREE, "build")
PCREC_BIN = os.path.join(BUILD_ROOT, "pcrec-25b1984f", "build", "pcrec")

sys.path.insert(0, ROOT)
from pcrecbench.driverrun import C_ENV  # noqa: E402

# The 14 patterns [B65]'s brief names, derived independently in the lane
# report from the two altwide pcrec-auto records' own compile rows (the
# d34c9131 one and the 20260921T053254Z 25b1984f one): every pattern
# whose d34c9131 compile row(s) are ALL `did-not-compile` and whose
# 25b1984f compile row(s) are ALL `compiled`. 18 - 4 = 14, matching
# b63window_report.md's own reconciliation.
PATTERNS = [
    "ci-256", "ci-512", "cnt-64", "nar4-512", "pfx3-512", "sfx-512",
    "sh1-512", "srt-256", "srt-512", "w-256", "w-384", "w-512",
    "wb-256", "wb-512",
]

OLD_RECORD = os.path.join(
    ROOT,
    "store/records/altwide@0.2/pcrec_d34c9131_auto-caps-simdna/"
    "altwide@0.2__pcrec_d34c9131_auto-caps-simdna__budu-ryzen1600__"
    "20260906T162430Z.jsonl",
)

# testees/pcrec/configs.toml [testees.pcrec-auto]: flags = ["--features",
# "all"]. -fcomments is [B58]'s FIXED PROTOCOL TOKEN, always on the real
# argv since the 25b1984f re-pin, never in cfg["flags"] (adapter.py's
# EMIT_COMMENTS_FLAG).
PCREC_FLAGS = ["--features", "all"]
EMIT_COMMENTS_FLAG = "-fcomments"

# I-80's two known rung note-line texts (matched by substring so a
# pcrec wording tweak that keeps the meaning does not spuriously FLAG;
# an unrecognised note line still flags because it matches neither).
RUNG1_MARKER = "dropped the optional anchored match-here machine"
RUNG2_MARKER = "dropped the premultiplied DFA transition table"

STAMPS = ["RX_ENGINE_SEL", "RX_DFA_TABLE", "RX_DFA_MATCH",
          "RX_DFA_PREFILTER", "RX_ENGINE"]


def load_old_records():
    """pattern_id -> list of old (d34c9131) compile rows, and the
    pattern's canonical_sha256 (from the first line's `patterns` block)."""
    rows = {}
    shas = {}
    with open(OLD_RECORD) as f:
        first = json.loads(f.readline())
        for p in first["patterns"]:
            if p["pattern_id"] in PATTERNS:
                shas[p["pattern_id"]] = p["canonical_sha256"]
        f.seek(0)
        for line in f:
            r = json.loads(line)
            if r.get("kind") != "compile":
                continue
            pid = r.get("pattern_id")
            if pid in PATTERNS:
                rows.setdefault(pid, []).append(r)
    return rows, shas


def pattern_bytes(pattern_id):
    path = os.path.join(ROOT, "bench", "altwide", "patterns",
                         "%s.rx" % pattern_id)
    with open(path, "rb") as f:
        text = f.read()
    if text.endswith(b"\n"):
        text = text[:-1]
    return text


def whole_subject(pattern):
    return b"(?:" + pattern + rb")\z"


def emit(out_dir, text):
    os.makedirs(out_dir, exist_ok=True)
    art_c = os.path.join(out_dir, "artifact.c")
    argv = ([PCREC_BIN, "-p", "rx", EMIT_COMMENTS_FLAG] + PCREC_FLAGS
            + ["-o", art_c, "--", text])
    proc = subprocess.run(["gnutimeout", "300"] + argv, capture_output=True,
                           env=C_ENV, timeout=310)
    return argv, proc, art_c


def classify_notes(stderr_text):
    notes = [ln for ln in stderr_text.splitlines()
              if ln.startswith("pcrec: note:")]
    warns = [ln for ln in stderr_text.splitlines()
              if ln.startswith("pcrec: warning:")]
    rungs = []
    flagged = []
    for ln in notes:
        if RUNG1_MARKER in ln:
            rungs.append(1)
        elif RUNG2_MARKER in ln:
            rungs.append(2)
        else:
            flagged.append(ln)
    return notes, warns, sorted(set(rungs)), flagged


def read_stamps(art_c):
    with open(art_c, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    out = {}
    for s in STAMPS:
        m = re.search(r'#define\s+' + s + r'\s+"([^"]*)"', text)
        if m:
            out[s] = m.group(1)
    return out


def main():
    print("# bench commit:", subprocess.check_output(
        ["git", "-C", ROOT, "rev-parse", "HEAD"], text=True).strip())
    print("# bench worktree:", ROOT)
    print("# pcrec pin: 25b1984f  binary:", PCREC_BIN)
    if not os.path.isfile(PCREC_BIN):
        raise SystemExit("missing pinned binary: %s" % PCREC_BIN)
    print("# pcrec binary sha256:",
          hashlib.sha256(open(PCREC_BIN, "rb").read()).hexdigest())
    print("# old (d34c9131) record:", OLD_RECORD)
    print()

    old_rows, shas = load_old_records()
    scratch = os.path.join(MAIN_TREE, "build", "b65attrib-scratch",
                            "rung-attribution")

    any_flagged = False
    summary_rows = []

    for pid in PATTERNS:
        print("=" * 72)
        print("== %s ==" % pid)
        raw = pattern_bytes(pid)
        got_sha = hashlib.sha256(raw).hexdigest()
        want_sha = shas.get(pid)
        assert got_sha == want_sha, (
            "%s: canonical_sha256 mismatch: file %s, old record %s"
            % (pid, got_sha, want_sha))
        print("pattern bytes sha256 (verified against d34c9131 record's "
              "canonical_sha256): %s" % got_sha)

        old_refusals = {}
        for r in old_rows.get(pid, []):
            if r.get("compile_outcome") != "compiled":
                old_refusals[r["seq"]] = r.get("diagnostic")
        n_old_refused = len(old_refusals)
        print("d34c9131 refused forms: %d of %d compile row(s)"
              % (n_old_refused, len(old_rows.get(pid, []))))
        for seq in sorted(old_refusals):
            print("  seq %d: %s" % (seq, old_refusals[seq]))

        forms = {"plain": raw, "whole-subject": whole_subject(raw)}
        for form, text in forms.items():
            out_dir = os.path.join(scratch, pid, form.replace("-", "_"))
            argv, proc, art_c = emit(out_dir, text)
            stderr_text = (proc.stderr or b"").decode("utf-8", "replace")
            print("-- %s / %s --" % (pid, form))
            # argv reprinted with the PATTERN element elided to its length +
            # sha256 (altwide patterns run to several KB of alternation
            # text; the full argv is in the scratch dir beside artifact.c
            # for anyone who wants it byte for byte -- this file's job is
            # the note lines and the stamps, not a second copy of the
            # pattern corpus).
            argv_display = list(argv[:-1]) + [
                "<pattern: %d bytes, sha256 %s>"
                % (len(text), hashlib.sha256(text).hexdigest())]
            print("argv:", " ".join(
                a.decode("utf-8", "replace") if isinstance(a, bytes) else a
                for a in argv_display))
            print("returncode:", proc.returncode)
            if proc.returncode != 0:
                print("REFUSED (still refused at 25b1984f -- not one of "
                      "the 14 rescued forms):", stderr_text.strip())
                summary_rows.append((pid, form, "REFUSED", [], [], {}))
                print()
                continue
            size = os.path.getsize(art_c)
            notes, warns, rungs, flagged = classify_notes(stderr_text)
            stamps = read_stamps(art_c)
            print("emitted .c size: %d B" % size)
            for w in warns:
                print("WARNING:", w)
            for n in notes:
                print("NOTE:", n)
            if flagged:
                any_flagged = True
                print("*** STOP-AND-FLAG: note line matches NEITHER known "
                      "rung text: %r" % flagged)
            print("stamps:", stamps)
            print("rungs fired:", rungs if rungs else "(none -- fits "
                  "under the cap without a retry)")
            print()
            summary_rows.append((pid, form, "compiled", rungs, flagged,
                                  {"size": size, **stamps}))

    print("=" * 72)
    print("SUMMARY (pattern, form, outcome, rungs, stamps)")
    print("=" * 72)
    for pid, form, outcome, rungs, flagged, meta in summary_rows:
        tag = " FLAGGED=%r" % flagged if flagged else ""
        print("%-10s %-14s %-9s rungs=%-6s %s%s"
              % (pid, form, outcome, rungs or "-", meta, tag))

    print()
    print("any note line unrecognised by the two known rung texts:",
          any_flagged)


if __name__ == "__main__":
    main()
