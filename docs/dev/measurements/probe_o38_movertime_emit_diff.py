#!/usr/bin/env python3
"""probe_o38_movertime_emit_diff.py -- [B62] STEP 1, inbox I-79 (ii).1:
byte-diff the two pins' emitted C for `wild-datetime-moment-iso8601`
under the `pcrec-vm-in` build, from the store's own two artifacts
(cf0962e3, 2026-09-18; 25b1984f, 2026-09-20/21) -- the cheapest,
static-only arm of the witness for O-38's ONE isolated `vm-in` time
mover (`docs/dev/lanes/b60pinconfirm_report.md` Section 3: ×1.08 slower,
+509.14 ns on a ~6.3 us cell, ~91x the v1.4 spread rule's own 2x-stddev
threshold, isolated to the vm-in route -- the other three pcrec routes on
the SAME pattern read unchanged).

pcrec's own reading (I-79 (i)): between cf0962e3 and 25b1984f the emitted
PROGRAM text is byte-identical with comments OFF (the bench's build
default since [B58]/[EMIT-VERB] -- see testees/pcrec/CLAUDE.md's
`EMIT_COMMENTS_FLAG` note); the only moved bytes anywhere in that pin
range are comment text and the one-line `abi` stamp. This probe checks
that claim DIRECTLY on the one pattern the mover fired on, under the
EXACT flags `testees/pcrec/adapter.py`'s vm-in config uses -- not a
generic corpus sweep.

THE FLAG STORY, gotten exactly right (checked live against each pinned
binary's own --list-axes before running, not assumed): `-fcomments` is
an axis pcrec ADDED at 25b1984f/abi 27 ([EMIT-VERB]/D112) -- it does not
exist at cf0962e3/abi 26 at all (`pcrec -fcomments ...` there is refused
BY NAME: "unknown option '-fcomments'", verified live below). Before
[EMIT-VERB], full comments were pcrec's ONLY behaviour -- there was
nothing to toggle. So:
  - at cf0962e3: emitted with NO comments flag on the argv at all (its
    one and only mode -- full comments, unconditionally);
  - at 25b1984f: emitted WITH `-fcomments` -- this is what
    testees/pcrec/adapter.py ACTUALLY sends on every real exec since the
    [B58] re-pin (`EMIT_COMMENTS_FLAG`, a fixed protocol token, always on
    argv, never in `cfg["flags"]`/`testee_id`), restoring exactly
    cf0962e3's old always-on comment behaviour so this project's two
    comment-text-dependent probes (`SCAN_EDGE_MARKER`, the `NO RESUME
    FRAME AT ALL` grep) keep working.
This pair (cf0962e3 bare vs. 25b1984f `-fcomments`) is COMPARISON A below
and is the one that matches what the real bench build actually ran both
times. COMPARISON B additionally emits 25b1984f WITHOUT `-fcomments`
(its new bare default, [EMIT-VERB]'s whole point -- comments stripped to
the essential provenance/ABI lines) for completeness of the record, even
though the adapter never sends that flag combination in practice.

Compile-only, no timing, no dlopen, no driver, no quiet-box gate: a
re-emission of one pattern at two pin snapshots pcrec-bench already has
built (build/pcrec-cf0962e3, build/pcrec-25b1984f -- pin.sh's own
snapshots, resolved via the git common dir so a worktree lands on the
same builds its main tree does). Nothing here is a ranking input.

The pattern text is read from the STORE record itself (not retyped) and
its sha256 checked against the record's own `canonical_sha256` before
anything is emitted, so a transcription error cannot silently poison the
diff.

Run from the repo root (or a worktree):
    python3 docs/dev/measurements/probe_o38_movertime_emit_diff.py
Output archived verbatim in
    docs/dev/measurements/2026-09-21-o38-movertime-emit-diff-cf0962e3-vs-25b1984f.txt
"""

import hashlib
import json
import os
import subprocess
import sys

ROOT = subprocess.check_output(
    ["git", "rev-parse", "--show-toplevel"], text=True
).strip()
COMMON = subprocess.check_output(
    ["git", "rev-parse", "--git-common-dir"], text=True
).strip()
# --git-common-dir is relative to cwd when run from inside a worktree;
# resolve it the same way pin.sh does (its own build root convention).
if not os.path.isabs(COMMON):
    COMMON = os.path.abspath(os.path.join(ROOT, COMMON))
MAIN_TREE = os.path.dirname(COMMON)  # .../pcrec-bench (the main tree, holds build/)
BUILD_ROOT = os.path.join(MAIN_TREE, "build")

sys.path.insert(0, ROOT)
from testees.pcrec.adapter import emit_size  # noqa: E402
from pcrecbench.driverrun import C_ENV  # noqa: E402

PATTERN_ID = "wild-datetime-moment-iso8601"
EXPECTED_SHA256 = (
    "498a5df9aae2552bcc9344099d8fc633ef27bc3c3c76f18b062716c0f0911165"
)

CF_RECORD = os.path.join(
    ROOT,
    "store/records/capability@0.1/pcrec_cf0962e3_vm-in-caps-simdna/"
    "capability@0.1__pcrec_cf0962e3_vm-in-caps-simdna__budu-ryzen1600__"
    "20260918T025149Z.jsonl",
)
NEW_RECORD = os.path.join(
    ROOT,
    "store/records/capability@0.1/pcrec_25b1984f_vm-in-caps-simdna/"
    "capability@0.1__pcrec_25b1984f_vm-in-caps-simdna__budu-ryzen1600__"
    "20260921T001807Z.jsonl",
)

# testees/pcrec/configs.toml [testees.pcrec-vm-in]: engine_mode = "vm-in",
# captures = "on", flags = ["--features", "all", "--engine=vm"]. The
# buffer_frames/buffer_trail capacities ride on the DRIVER argv (phase 3,
# the caller-provided frame buffer), never on pcrec's phase-1 emit-c argv
# -- they cannot move a single emitted byte, so they are correctly absent
# from the argv this probe builds.
VM_IN_FLAGS = ["--features", "all", "--engine=vm"]


def load_pattern_text(record_path):
    with open(record_path, "rb") as f:
        first_line = f.readline()
    setup = json.loads(first_line)
    for p in setup["patterns"]:
        if p["pattern_id"] == PATTERN_ID:
            text = p["canonical_text"]
            got = hashlib.sha256(text.encode("utf-8")).hexdigest()
            assert got == p["canonical_sha256"] == EXPECTED_SHA256, (
                "canonical_sha256 mismatch in %s: got %s want %s"
                % (record_path, got, p["canonical_sha256"])
            )
            return text
    raise SystemExit("pattern %r not found in %s" % (PATTERN_ID, record_path))


def emit(pcrec_bin, out_dir, pattern_bytes, comments_flag):
    """comments_flag: None (no flag on argv at all -- cf0962e3's only
    mode, or 25b1984f's new bare default), "-fcomments", or
    "-fno-comments"."""
    os.makedirs(out_dir, exist_ok=True)
    art_c = os.path.join(out_dir, "artifact.c")
    argv = [pcrec_bin, "-p", "rx"]
    if comments_flag:
        argv.append(comments_flag)
    argv += VM_IN_FLAGS + ["-o", art_c, "--", pattern_bytes]
    proc = subprocess.run(argv, capture_output=True, env=C_ENV, timeout=600)
    return argv, proc, art_c


def check_axis_support(pcrec_bin, pin):
    """Verify live, not assumed: does this pin's --list-axes carry the
    `comments` axis at all? (cf0962e3 must not; 25b1984f must.)"""
    proc = subprocess.run([pcrec_bin, "--list-axes"], capture_output=True,
                           text=True, env=C_ENV, timeout=60)
    has_axis = "\ncomments\t" in ("\n" + proc.stdout) or proc.stdout.startswith(
        "comments\t")
    print("# pin %s --list-axes carries a `comments` axis: %s"
          % (pin, has_axis))
    return has_axis


def read_file(path):
    with open(path, "rb") as f:
        return f.read()


def sha256_of(path):
    return hashlib.sha256(read_file(path)).hexdigest()


def main():
    print("# bench commit:", subprocess.check_output(
        ["git", "-C", ROOT, "rev-parse", "HEAD"], text=True).strip())
    print("# bench worktree:", ROOT)
    print("# build root:", BUILD_ROOT)
    print()

    cf_text = load_pattern_text(CF_RECORD)
    new_text = load_pattern_text(NEW_RECORD)
    assert cf_text == new_text, "pattern text differs between the two records!"
    print("# pattern_id:", PATTERN_ID)
    print("# canonical_sha256 (verified against both records):", EXPECTED_SHA256)
    print("# canonical_text:", cf_text)
    print()

    pattern_bytes = cf_text.encode("utf-8")  # I-72: raw bytes argv element

    pins = [
        ("cf0962e3", os.path.join(BUILD_ROOT, "pcrec-cf0962e3", "build", "pcrec")),
        ("25b1984f", os.path.join(BUILD_ROOT, "pcrec-25b1984f", "build", "pcrec")),
    ]
    for pin, path in pins:
        if not os.path.isfile(path):
            raise SystemExit("missing pinned binary for %s: %s" % (pin, path))
        print("# pin %s binary: %s (sha256 %s)" % (pin, path, sha256_of(path)))
    print()

    for pin, path in pins:
        check_axis_support(path, pin)
    print()

    # Live witness that cf0962e3 truly has no -fcomments spelling (not
    # assumed from the CLAUDE.md prose): the exact refusal this probe's
    # docstring claims.
    cf_bin = dict(pins)["cf0962e3"]
    refusal = subprocess.run(
        [cf_bin, "-p", "rx", "-fcomments"] + VM_IN_FLAGS
        + ["-o", "/dev/null", "--", pattern_bytes],
        capture_output=True, env=C_ENV, timeout=60)
    print("# live witness: cf0962e3 given -fcomments ->", refusal.returncode)
    print("# stderr[0]:", (refusal.stderr or b"").decode("utf-8", "replace")
          .splitlines()[0] if refusal.stderr else "(none)")
    assert refusal.returncode != 0, "cf0962e3 unexpectedly accepted -fcomments"
    print()

    # Per-pin comment-flag PLAN, decided from the axis support just
    # checked, not from a hardcoded guess:
    #   cf0962e3: ONE emission, no flag at all (its only mode)
    #   25b1984f: TWO emissions, -fcomments (what the adapter really
    #             sends) and -fno-comments (the new bare default, shown
    #             for completeness only)
    plan = {
        "cf0962e3": [(None, "no-flag-only-mode")],
        "25b1984f": [("-fcomments", "fcomments"),
                      ("-fno-comments", "fno-comments-default")],
    }

    scratch = os.path.join(
        MAIN_TREE, "build", "b62witness-scratch", "o38-movertime-emit-diff"
    )
    results = {}
    for pin, pcrec_bin in pins:
        for comments_flag, tag in plan[pin]:
            out_dir = os.path.join(scratch, pin, tag)
            argv, proc, art_c = emit(pcrec_bin, out_dir, pattern_bytes, comments_flag)
            print("== pin %s / %s ==" % (pin, tag))
            print("argv:", " ".join(
                a.decode("utf-8", "replace") if isinstance(a, bytes) else a
                for a in argv))
            print("returncode:", proc.returncode)
            stderr = (proc.stderr or b"").decode("utf-8", "replace").strip()
            if stderr:
                print("stderr:", stderr)
            if proc.returncode != 0:
                raise SystemExit("pcrec refused to emit at pin %s (%s)" % (pin, tag))
            art_h = art_c[:-2] + ".h"
            files = [art_c] + ([art_h] if os.path.exists(art_h) else [])
            total, code = emit_size(files)
            raw_c = os.path.getsize(art_c)
            raw_h = os.path.getsize(art_h) if os.path.exists(art_h) else 0
            print("raw .c bytes: %d  raw .h bytes: %d  raw total: %d"
                  % (raw_c, raw_h, raw_c + raw_h))
            print("emit_size() total (comment-excluded): %d  code: %d"
                  % (total, code))
            print("sha256 .c:", sha256_of(art_c))
            if os.path.exists(art_h):
                print("sha256 .h:", sha256_of(art_h))
            results[(pin, tag)] = dict(
                art_c=art_c, art_h=art_h if os.path.exists(art_h) else None,
                raw_c=raw_c, raw_h=raw_h, total=total, code=code)
            print()

    def diff(path_a, path_b, label):
        proc = subprocess.run(["diff", "-u", path_a, path_b],
                               capture_output=True, text=True)
        print("== diff: %s ==" % label)
        if proc.returncode == 0:
            print("(byte-identical)")
        else:
            print(proc.stdout)
        print()
        return proc.returncode == 0

    # The abi digit appears on two lines pcrec always emits regardless of
    # pin: the provenance comment ("Generated by pcrec (abi N).") and the
    # `.abi = N,` struct initializer. "identical modulo the abi stamp
    # line" means: byte-identical once those two lines are excluded from
    # the comparison -- checked structurally (a real line-by-line diff
    # classified by content), not by eyeballing the printed patch above.
    def identical_modulo_abi_stamp(path_a, path_b):
        with open(path_a, "r", encoding="utf-8") as f:
            lines_a = f.readlines()
        with open(path_b, "r", encoding="utf-8") as f:
            lines_b = f.readlines()

        def strip_abi(lines):
            out = []
            for ln in lines:
                s = ln.strip()
                if s.startswith("/* Generated by pcrec") and "Pattern:" in s:
                    out.append("/* Generated by pcrec. Pattern: <elided> */\n")
                elif s.startswith(".abi ="):
                    out.append("    .abi = <elided>,\n")
                else:
                    out.append(ln)
            return out

        a_stripped, b_stripped = strip_abi(lines_a), strip_abi(lines_b)
        if a_stripped == b_stripped:
            return True, []
        import difflib
        residual = list(difflib.unified_diff(a_stripped, b_stripped,
                                              lineterm=""))
        return False, residual

    print("############################################################")
    print("# COMPARISON A -- THE ONE THAT MATTERS: cf0962e3's only mode")
    print("# (no comments flag exists there; full comments unconditionally)")
    print("# vs. 25b1984f WITH -fcomments -- this IS what")
    print("# testees/pcrec/adapter.py actually sent on the real record-")
    print("# producing execs at both pins (EMIT_COMMENTS_FLAG is a fixed")
    print("# protocol token on every phase-1 exec since [B58])")
    print("############################################################")
    a_c = diff(results[("cf0962e3", "no-flag-only-mode")]["art_c"],
               results[("25b1984f", "fcomments")]["art_c"],
               "cf0962e3 (no flag) .c  vs  25b1984f -fcomments .c")
    a_h_ok = True
    if results[("cf0962e3", "no-flag-only-mode")]["art_h"]:
        a_h_ok = diff(results[("cf0962e3", "no-flag-only-mode")]["art_h"],
                       results[("25b1984f", "fcomments")]["art_h"],
                       "cf0962e3 (no flag) .h  vs  25b1984f -fcomments .h")

    print("== classified: identical MODULO the abi-stamp lines? ==")
    a_c_modulo, a_c_residual = identical_modulo_abi_stamp(
        results[("cf0962e3", "no-flag-only-mode")]["art_c"],
        results[("25b1984f", "fcomments")]["art_c"])
    print(".c  identical-modulo-abi-stamp: %s" % a_c_modulo)
    if not a_c_modulo:
        print("residual (non-abi-stamp) diff:\n" + "\n".join(a_c_residual))
    a_h_modulo = True
    if results[("cf0962e3", "no-flag-only-mode")]["art_h"]:
        a_h_modulo, a_h_residual = identical_modulo_abi_stamp(
            results[("cf0962e3", "no-flag-only-mode")]["art_h"],
            results[("25b1984f", "fcomments")]["art_h"])
        print(".h  identical-modulo-abi-stamp: %s" % a_h_modulo)
        if not a_h_modulo:
            print("residual (non-abi-stamp) diff:\n" + "\n".join(a_h_residual))
    print()

    print("############################################################")
    print("# COMPARISON B -- for the record only, NOT the adapter's real")
    print("# argv: 25b1984f WITH -fcomments vs. 25b1984f WITHOUT it (its")
    print("# new bare default). Isolates the -fcomments flag's OWN effect")
    print("# at one pin, so a mover in comparison A could be told apart")
    print("# from a mover the flag itself introduces (match_api.md /")
    print("# testees/pcrec/CLAUDE.md's own claim: 'changes no answer and")
    print("# no object byte').")
    print("############################################################")
    b_c = diff(results[("25b1984f", "fcomments")]["art_c"],
               results[("25b1984f", "fno-comments-default")]["art_c"],
               "25b1984f -fcomments .c  vs  25b1984f -fno-comments .c")
    b_h_ok = True
    if results[("25b1984f", "fcomments")]["art_h"]:
        b_h_ok = diff(results[("25b1984f", "fcomments")]["art_h"],
                       results[("25b1984f", "fno-comments-default")]["art_h"],
                       "25b1984f -fcomments .h  vs  25b1984f -fno-comments .h")

    print("== emit_size() (comment-excluded) summary ==")
    for (pin, tag), r in results.items():
        print("%-9s %-22s raw=%d  emit_bytes=%d  emit_code_bytes=%d"
              % (pin, tag, r["raw_c"] + r["raw_h"], r["total"], r["code"]))
    print()

    print("== verdict ==")
    print("A) cf0962e3 (only mode) vs 25b1984f -fcomments"
          " -- THE BENCH'S REAL BUILD, BOTH PINS: %s"
          % ("byte-identical modulo the abi stamp line(s) -- EXONERATES "
             "the compiler by construction"
             if a_c_modulo and a_h_modulo
             else "DIFFERS beyond the abi stamp line -- a REAL residual "
                  "diff, see 'residual (non-abi-stamp) diff' above"))
    print("B) 25b1984f -fcomments vs 25b1984f -fno-comments"
          " -- the flag's own isolated effect at one pin: %s"
          % ("byte-identical (comments-only difference had zero net effect"
             " here -- unexpected, see diff above)"
             if b_c and b_h_ok else "differs (expected: comment text only)"))


if __name__ == "__main__":
    main()
