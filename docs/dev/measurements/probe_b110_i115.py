#!/usr/bin/env python3
"""[B110] inbox I-115 Q1/Q4/Q5/Q6/Q7 -- compile-side and scratch-tier
probes separating PLACEMENT from CODE for O-64/O-65's [OPT-LITSCAN] S2a
reading, at pin a32bc86e.

Every probe below is COMPILE-SIDE or a SCRATCH-TIER instrumented build:
no `perf` (kernel.perf_event_paranoid=4 on this box, unprivileged perf is
refused, no sudo used), no pinned record written, nothing that touches
`store/`. Q1/Q4/Q5's "per-call counter" answers come from an
INSTRUMENTED COPY of the real emitted artifact -- a global counter
inserted at the entry of the mechanism function named (rx_match_anchored
for a VM "verify" call, rx_prefilter for the DFA/attempt scan, a
`counted_memchr` wrapper `#define`d over `memchr` before including the
artifact's own `.c`) -- built and run standalone (never through
shim.c/driver.c, whose own find-all loop this script's `main()` mirrors
exactly: KB-29's own advance rule, byte encoding, `pos = end>start ?
end : start+1`). Q6 is real objdump on the REAL adapter recipe (`gcc -O2
-std=gnu11 -fPIC -shared shim.c -DPB_ARTIFACT="..."`, shim.c copied
unmodified from testees/pcrec/shim.c). Q7 is a pure read of the
committed expectations.tsv plus a sha256 cross-check of the physical
subject files pcrec-bench already generated.

Usage: python3 docs/dev/measurements/probe_b110_i115.py [--keep-tmp]
Run from the repo root. Needs PCREC_BIN unset (the pin is resolved via
testees/pcrec's own pin_binary()) and gcc on PATH. ~30-60 s.
"""
import argparse
import glob
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "testees", "pcrec"))

import pcrecbench.adapters as _ad  # noqa: E402


def sh(argv, **kw):
    kw.setdefault("capture_output", True)
    kw.setdefault("text", True)
    r = subprocess.run(argv, **kw)
    if r.returncode != 0:
        raise RuntimeError("FAILED: %s\n%s\n%s" % (" ".join(argv), r.stdout, r.stderr))
    return r


def compile_pattern(pcrec_bin, tmp, name, pattern, extra_flags):
    """-> (c_path, h_path). extra_flags is pcrec's OWN argv tail."""
    c_path = os.path.join(tmp, name + ".c")
    argv = [pcrec_bin, "-p", "rx", "-fcomments", "--features", "all"] \
        + extra_flags + ["-o", c_path, "--pattern", pattern]
    sh(argv)
    return c_path, c_path[:-2] + ".h"


def instrument_counter(c_path, out_path, func_marker_re, macro_name,
                        extra_counter=None, extra_marker_re=None,
                        extra_macro=None):
    """Insert `long <macro_name> = 0;` after the artifact's own
    `#include <string.h>` line and `<macro_name>++;` as the first
    statement of the function whose signature (any qualifiers) matches
    func_marker_re. Rewrites the header include to the copied .h path's
    own basename (both files are copied beside out_path first)."""
    src = open(c_path).read()
    hdr_path = c_path[:-2] + ".h"
    hdr_base = os.path.basename(out_path)[:-2] + ".h"
    shutil.copy(hdr_path, os.path.join(os.path.dirname(out_path), hdr_base))
    src = re.sub(r'#include "[^"]+\.h"', '#include "%s"' % hdr_base, src, count=1)
    assert "#include <string.h>\n" in src
    decl = "#include <string.h>\nlong %s = 0;\n" % macro_name
    if extra_macro:
        decl += "long %s = 0;\n" % extra_macro
    src = src.replace("#include <string.h>\n", decl, 1)
    pat = re.compile(func_marker_re)
    ms = pat.findall(src)
    assert len(ms) == 1, (func_marker_re, len(ms))
    src = pat.sub(lambda mo: mo.group(0) + "\n    %s++;" % macro_name, src, count=1)
    if extra_marker_re:
        pat2 = re.compile(extra_marker_re)
        ms2 = pat2.findall(src)
        assert len(ms2) == 1, (extra_marker_re, len(ms2))
        src = pat2.sub(lambda mo: mo.group(0) + "\n    %s++;" % extra_macro, src, count=1)
    open(out_path, "w").write(src)


MAIN_TEMPLATE = r'''
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "%(hdr)s"
%(externs)s
extern int rx_search(const unsigned char *subject, size_t subject_length,
                      size_t search_from, ptrdiff_t (*capture_spans)[2]);
static unsigned char *read_file(const char *path, size_t *out_len) {
    FILE *f = fopen(path, "rb");
    if (!f) { perror(path); exit(1); }
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)n);
    if (fread(buf, 1, (size_t)n, f) != (size_t)n) { perror("fread"); exit(1); }
    fclose(f);
    *out_len = (size_t)n;
    return buf;
}
int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %%s subject\n", argv[0]); return 2; }
    size_t len; unsigned char *subj = read_file(argv[1], &len);
    ptrdiff_t caps[RX_NCAPS][2];
    size_t pos = 0; long count = 0, search_calls = 0;
    for (;;) {
        search_calls++;
        int r = rx_search(subj, len, pos, caps);
        if (r == 0) break;
        if (r < 0) { printf("giveup %%d\n", r); break; }
        count++;
        size_t start = (size_t)caps[0][0], end = (size_t)caps[0][1];
        pos = (end > start) ? end : start + 1;
        if (pos > len) break;
    }
    printf("bytes=%%zu\trx_search_calls=%%ld\tmatches=%%ld%(prints)s\n",
           len, search_calls, count%(printargs)s);
    return 0;
}
'''


def build_and_run(tmp, instr_c, hdr_base, counters, subject_path, exe_name):
    externs = "\n".join("extern long %s;" % c for c in counters)
    prints = "".join("\t%s=%%ld" % c for c in counters)
    printargs = "".join(", %s" % c for c in counters)
    main_c = os.path.join(tmp, exe_name + "_main.c")
    open(main_c, "w").write(MAIN_TEMPLATE % dict(
        hdr=hdr_base, externs=externs, prints=prints, printargs=printargs))
    exe = os.path.join(tmp, exe_name)
    sh(["gcc", "-O2", "-o", exe, instr_c, main_c])
    r = sh(["/usr/bin/gnutimeout", "30", exe, subject_path])
    return r.stdout.strip()


def q1_aws(pcrec_bin, tmp, capa_thr):
    print("=" * 78)
    print("Q1: aws-access-key-id throughput (t-64k/t-256k/t-1m) -- matches "
          "and VM verify calls")
    print("=" * 78)
    pattern = (r'\b((?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)'
               r'[A-Z0-9]{16})\b')
    c, h = compile_pattern(pcrec_bin, tmp, "q1_aws", pattern, [])
    for line in open(c):
        if line.startswith("#define RX_ENGINE") or line.startswith("#define RX_DFA_") \
                or line.startswith("#define RX_VM_PREFILTER"):
            print("  " + line.strip())
    instr = os.path.join(tmp, "q1_aws_instr.c")
    instrument_counter(
        c, instr,
        r'rx_match_anchored\(const rx_ctx \*ctx, rx_run_state \*run\)\n\{',
        "g_verify_calls")
    hdr_base = os.path.basename(instr)[:-2] + ".h"
    for name in ("t-64k", "t-256k", "t-1m"):
        subj = os.path.join(capa_thr, name + ".bin")
        out = build_and_run(tmp, instr, hdr_base, ["g_verify_calls"], subj,
                             "q1_" + name.replace("-", "_"))
        print("  %s\t%s" % (name, out))
    print()


def q4_lpr_subjects(capa_root):
    print("=" * 78)
    print("Q4 (first half): logparse-atomic-removed's 75 short-search "
          "subjects -- prefix match then fail at \": \" vs full match "
          "vs no prefix match")
    print("=" * 78)
    facprefix = re.compile(
        rb'^(?:kern|user|mail|daemon|auth|syslog|cron)\.'
        rb'(?:emerg|alert|crit|err|warning|notice|info|debug)')
    full = re.compile(
        rb'^(?:(?:kern|user|mail|daemon|auth|syslog|cron)\.'
        rb'(?:emerg|alert|crit|err|warning|notice|info|debug)): (.*)$')
    manifest = os.path.join(capa_root, "manifest.tsv")
    expfile = os.path.join(capa_root, "expectations.tsv")
    exp = {}
    with open(expfile) as f:
        header = next(f).rstrip("\n").split("\t")
        for line in f:
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            if row["pattern"] == "logparse-atomic-removed" and row["regime"] == "search_short":
                exp[row["subject"]] = row["expected"]
    cat_a, cat_b, cat_c = [], [], []
    with open(manifest) as f:
        header = next(f).rstrip("\n").split("\t")
        for line in f:
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            sid = row["id"]
            if sid not in exp:
                continue
            data = open(os.path.join(capa_root, "subjects", sid + ".bin"), "rb").read()
            m_full, m_pref = full.match(data), facprefix.match(data)
            if m_full:
                cat_c.append((sid, exp[sid]))
            elif m_pref:
                cat_b.append((sid, exp[sid]))
            else:
                cat_a.append((sid, exp[sid]))
    print("  total subjects: %d" % (len(cat_a) + len(cat_b) + len(cat_c)))
    print("  category C (full match, facility.severity + ': ' + rest): %d -- %s"
          % (len(cat_c), cat_c))
    print("  category B (facility.severity matches, THEN fails at ': '): %d -- %s"
          % (len(cat_b), cat_b))
    print("  category A (no facility.severity prefix match at all): %d" % len(cat_a))
    print()


def q4_lpr_throughput(pcrec_bin, tmp, capa_thr):
    print("=" * 78)
    print("Q4 (second half): logparse-atomic-removed on the 3 throughput "
          "subjects -- does the VM run, or does the prefilter reject?")
    print("=" * 78)
    pattern = (r'^(?:(?:kern|user|mail|daemon|auth|syslog|cron)\.'
               r'(?:emerg|alert|crit|err|warning|notice|info|debug)): (.*)$')
    c, h = compile_pattern(pcrec_bin, tmp, "q4_lpr", pattern, [])
    for line in open(c):
        if line.startswith("#define RX_ENGINE") or line.startswith("#define RX_DFA_") \
                or line.startswith("#define RX_REQ_"):
            print("  " + line.strip())
    instr = os.path.join(tmp, "q4_lpr_instr.c")
    instrument_counter(
        c, instr,
        r'rx_match_anchored\(const rx_ctx \*ctx, rx_run_state \*run\)\n\{',
        "g_verify_calls",
        extra_marker_re=r'rx_prefilter\(const unsigned char \*subject, '
                         r'size_t subject_length, size_t search_from, '
                         r'ptrdiff_t \(\*capture_spans\)\[2\]\)\n\{',
        extra_macro="g_prefilter_calls")
    hdr_base = os.path.basename(instr)[:-2] + ".h"
    for name in ("t-64k", "t-256k", "t-1m"):
        subj = os.path.join(capa_thr, name + ".bin")
        out = build_and_run(tmp, instr, hdr_base,
                             ["g_prefilter_calls", "g_verify_calls"], subj,
                             "q4_" + name.replace("-", "_"))
        print("  %s\t%s" % (name, out))
    print()


def q5_dense_match_memchr(pcrec_bin, tmp, litrun_thr):
    print("=" * 78)
    print("Q5: the dense-match pre-check's memchr count per rx_search "
          "call, `pcrec-vm` (pre-checks ON) on mat-l<L>")
    print("=" * 78)
    Ls = [2, 3, 4, 7, 8, 10, 16, 31, 40]
    for L in Ls:
        pat_path = os.path.join(ROOT, "bench", "litrun", "patterns",
                                 "lit-l%d.rx" % L)
        pattern = open(pat_path).read()
        c, h = compile_pattern(pcrec_bin, tmp, "q5_l%d" % L, pattern,
                                ["--engine=vm"])
        instr = os.path.join(tmp, "q5_l%d_instr.c" % L)
        src = open(c).read()
        hdr_base = os.path.basename(instr)[:-2] + ".h"
        shutil.copy(h, os.path.join(tmp, hdr_base))
        src = re.sub(r'#include "[^"]+\.h"', '#include "%s"' % hdr_base, src, count=1)
        assert "#include <string.h>\n" in src
        wrap = (
            "#include <string.h>\n"
            "long g_memchr_calls = 0;\n"
            "long g_verify_calls = 0;\n"
            "static void *counted_memchr(const void *s, int ch, size_t n) {\n"
            "    g_memchr_calls++;\n"
            "    return memchr(s, ch, n);\n"
            "}\n"
            "#define memchr counted_memchr\n")
        src = src.replace("#include <string.h>\n", wrap, 1)
        pat = re.compile(r'rx_match_anchored\(const rx_ctx \*ctx, '
                          r'rx_run_state \*run\)\n\{')
        assert len(pat.findall(src)) == 1, L
        src = pat.sub(lambda mo: mo.group(0) + "\n    g_verify_calls++;", src, count=1)
        open(instr, "w").write(src)
        subj = os.path.join(litrun_thr, "mat-l%d.bin" % L)
        out = build_and_run(tmp, instr, hdr_base,
                             ["g_memchr_calls", "g_verify_calls"], subj,
                             "q5_l%d" % L)
        fields = dict(kv.split("=") for kv in out.split("\t"))
        rate = (int(fields["g_memchr_calls"]) / int(fields["rx_search_calls"])
                if int(fields["rx_search_calls"]) else 0.0)
        print("  L=%-3d %s\tmemchr_per_rx_search_call=%.4f" % (L, out, rate))
    print()


def q6_loophead_alignment(pcrec_bin, tmp):
    print("=" * 78)
    print("Q6: PRIMARY row (--engine=vm -fno-req-byte -fno-req-run) "
          "lit-l<L> attempt-loop head, real .so, objdump loop-head "
          "alignment mod 16")
    print("=" * 78)
    shim_src = os.path.join(ROOT, "testees", "pcrec", "shim.c")
    shim_copy = os.path.join(tmp, "shim.c")
    shutil.copy(shim_src, shim_copy)
    Ls = [2, 3, 4, 7, 8, 10, 16, 31, 40]
    rows = []
    for L in Ls:
        pat_path = os.path.join(ROOT, "bench", "litrun", "patterns",
                                 "lit-l%d.rx" % L)
        pattern = open(pat_path).read()
        c, h = compile_pattern(pcrec_bin, tmp, "q6_l%d" % L, pattern,
                                ["--engine=vm", "-fno-req-byte", "-fno-req-run"])
        so_path = os.path.join(tmp, "q6_l%d.so" % L)
        sh(["gcc", "-O2", "-std=gnu11", "-fPIC", "-shared", shim_copy,
            "-DPB_ARTIFACT=\"%s\"" % c, "-I", tmp, "-o", so_path])
        dis = sh(["objdump", "-d", "--disassemble=rx_search_in", so_path]).stdout
        m = re.findall(r'^\s*[0-9a-f]+:\s+eb [0-9a-f]{2}\s+jmp\s+([0-9a-f]+)',
                        dis, re.M)
        addr = m[0] if m else None
        mod16 = int(addr, 16) % 16 if addr else None
        rows.append((L, addr, mod16))
        if L in (3, 7, 10, 40):
            print("  -- L=%d loop excerpt --" % L)
            block = re.search(r'<rx_search_in>:\n(.*?)\n\n', dis, re.S)
            if block:
                for line in block.group(1).splitlines():
                    print("    " + line)
    print()
    print("  L   loop_head   mod16")
    for L, addr, mod16 in rows:
        print("  %-3d 0x%-8s %s" % (L, addr, mod16))
    print()


def q7_ctx_subjects(bounded_root):
    print("=" * 78)
    print("Q7: are the ctx-lazy-64/256/1024 (+ctx-greedy-256) whole-subject "
          "match subjects the SAME byte strings across rungs?")
    print("=" * 78)
    expfile = os.path.join(bounded_root, "expectations.tsv")
    by_pattern = {}
    with open(expfile) as f:
        header = next(f).rstrip("\n").split("\t")
        for line in f:
            row = dict(zip(header, line.rstrip("\n").split("\t")))
            if row["regime"] == "match" and row["pattern"] in (
                    "ctx-lazy-64", "ctx-lazy-256", "ctx-lazy-1024",
                    "ctx-greedy-256"):
                by_pattern.setdefault(row["pattern"], set()).add(row["subject"])
    names = ["ctx-lazy-64", "ctx-lazy-256", "ctx-lazy-1024", "ctx-greedy-256"]
    for n in names:
        print("  %s: %d match-regime subjects" % (n, len(by_pattern.get(n, ()))))
    base = by_pattern.get("ctx-lazy-64", set())
    all_same = all(by_pattern.get(n, set()) == base for n in names)
    print("  identical subject-id SET across all four: %s" % all_same)
    # cross-check the physical bytes: these ids all resolve to the SAME
    # single subjects/ directory (one file per id, not duplicated per
    # pattern), so byte identity is structural, not merely id identity --
    # confirmed here by hashing every referenced file once.
    hashes = {}
    for sid in sorted(base):
        p = os.path.join(bounded_root, "subjects", sid + ".bin")
        hashes[sid] = hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]
    print("  sample sha256[:16] (first 5, alphabetical): %s"
          % dict(list(hashes.items())[:5]))
    print("  (all four patterns' cells read this ONE subjects/ directory, "
          "by construction -- subjects_for() applies no filter to the "
          "match regime, so the same physical files back every rung)")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keep-tmp", action="store_true")
    args = ap.parse_args()

    os.environ.pop("PCREC_BIN", None)
    adapter = _ad.discover()["pcrec"]
    pcrec_bin = adapter.pin_binary()
    print("# source: [B110] docs/dev/measurements/probe_b110_i115.py")
    print("# bench commit: %s" % sh(["git", "-C", ROOT, "rev-parse", "HEAD"]).stdout.strip())
    print("# pcrec pin: a32bc86e, binary %s" % pcrec_bin)
    print("# pcrec binary sha256: %s"
          % hashlib.sha256(open(pcrec_bin, "rb").read()).hexdigest())
    print("# gcc: %s" % sh(["gcc", "--version"]).stdout.splitlines()[0])
    print("# box: %s" % sh(["hostname"]).stdout.strip())
    print("# load (before): %s" % open("/proc/loadavg").read().strip())
    print()

    tmp = tempfile.mkdtemp(prefix="b110probe-i115-")
    capa_root = os.path.join(ROOT, "bench", "capability")
    capa_thr = os.path.join(capa_root, "throughput")
    litrun_thr = os.path.join(ROOT, "bench", "litrun", "throughput")
    bounded_root = os.path.join(ROOT, "bench", "bounded")
    try:
        q1_aws(pcrec_bin, tmp, capa_thr)
        q4_lpr_subjects(capa_root)
        q4_lpr_throughput(pcrec_bin, tmp, capa_thr)
        q5_dense_match_memchr(pcrec_bin, tmp, litrun_thr)
        q6_loophead_alignment(pcrec_bin, tmp)
        q7_ctx_subjects(bounded_root)
    finally:
        print("# load (after): %s" % open("/proc/loadavg").read().strip())
        if args.keep_tmp:
            print("# tmp kept at %s" % tmp)
        else:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
