#!/usr/bin/env python3
"""docs/dev/measurements/probe_b109_reseed_twin.py -- [B109] x86 confirm of
the [OPT-HYB-RESEED] hand-twin (pcrec inbox I-114,
git -C ~/pcrec show origin/main:docs/dev/utf8_attrib_twin/I-114.md, pin
a32bc86e). Every source line below (the three patterns, the 8-line twin
diff, drv.c, the subject generator) is I-114's own text, reproduced
verbatim so this file needs nothing else to run. Compile-only /
timing-only; SCRATCH TIER, never touches store/ or reports/.

Runs from the repo root:
    python3 docs/dev/measurements/probe_b109_reseed_twin.py [--trials N] [--out DIR]

Requires: the a32bc86e pin already built (testees/pcrec/pin.sh a32bc86e),
bench/utf8's throughput subjects generated (python3 bench/utf8/
gen_throughput_subjects.py), gcc and clang on PATH.
"""
import hashlib
import pathlib
import random
import re
import shutil
import statistics as st
import subprocess
import sys
import time

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
PIN = "a32bc86e"

PATTERNS = {
    "row1_varwidth": ("asr-lb-varwidth", "(?<=a|é)x"),
    "row10_neg": ("asr-lb-neg", "(?<!日)本"),
    "row11_fixed": ("asr-lb-fixed", "(?<=é)x"),
}

BENCH_SUBJECTS = [
    "t-64k", "t-256k", "t-1m", "t-64k-lat", "t-64k-cyr", "t-64k-cjk", "t-64k-asc",
]
SYNTH_SUBJECTS = ["synth-1m", "synth-64k-asc", "synth-dense"]

TWIN_BLOCK = """        /* HAND TWIN (reseedtwin, [OPT-HYB-RESEED]): the same three lines as
         * the entry call, emitted unconditionally here instead of only under
         * v->nclamp > 0. */
        {
            ptrdiff_t window[1][2];
            if (rx_prefilter(subject, subject_length, attempt_position, window) != 1) return 0;
            attempt_position = (size_t)window[0][0];
        }
"""

DRV_C = r'''/* drv.c -- from I-114, verbatim (an extra NTRIALS argv + all_us dump added
 * for a median+spread reading, both additive: argc==2 behaves exactly as
 * I-114's own driver, best_us unchanged in meaning). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>
#include <time.h>

extern int rx_search(const unsigned char *subject, size_t subject_length,
                      size_t search_from, ptrdiff_t (*capture_spans)[2]);
extern size_t rx_next_pos(const unsigned char *s, size_t n, size_t pos);

static uint64_t now_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ull + (uint64_t)ts.tv_nsec;
}

static void run_once(const unsigned char *s, size_t n,
                      long *out_matches, uint64_t *out_hash) {
    size_t pos = 0;
    long matches = 0;
    uint64_t h = 1469598103934665603ull;
    const uint64_t prime = 1099511628211ull;
    ptrdiff_t caps[1][2];
    while (pos <= n) {
        int ok = rx_search(s, n, pos, caps);
        if (!ok) break;
        ptrdiff_t start = caps[0][0], end = caps[0][1];
        matches++;
        h ^= (uint64_t)start; h *= prime;
        h ^= (uint64_t)end;   h *= prime;
        if (end > start) pos = (size_t)end;
        else pos = rx_next_pos(s, n, pos);
    }
    *out_matches = matches;
    *out_hash = h;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s SUBJECT_FILE [NTRIALS]\n", argv[0]); return 2; }
    int ntrials = (argc >= 3) ? atoi(argv[2]) : 5;
    if (ntrials < 1) ntrials = 1;
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)sz);
    if (fread(buf, 1, (size_t)sz, f) != (size_t)sz) { perror("fread"); return 2; }
    fclose(f);

    long matches = 0;
    uint64_t hash = 0;
    double best_us = -1.0;
    double *all_us = malloc(sizeof(double) * (size_t)ntrials);
    for (int i = 0; i < ntrials; i++) {
        long m; uint64_t h;
        uint64_t t0 = now_ns();
        run_once(buf, (size_t)sz, &m, &h);
        uint64_t t1 = now_ns();
        double us = (double)(t1 - t0) / 1000.0;
        all_us[i] = us;
        if (i == 0) { matches = m; hash = h; }
        else if (m != matches || h != hash) {
            fprintf(stderr, "NONDETERMINISM run %d: matches %ld->%ld hash %llx->%llx\n",
                    i, matches, m, (unsigned long long)hash, (unsigned long long)h);
        }
        if (best_us < 0 || us < best_us) best_us = us;
    }
    printf("matches=%ld hash=%016llx best_us=%.3f all_us=", matches,
           (unsigned long long)hash, best_us);
    for (int i = 0; i < ntrials; i++) printf("%s%.3f", i ? "," : "", all_us[i]);
    printf("\n");
    free(all_us);
    free(buf);
    return 0;
}
'''

PROBE_DENSITY_C = r'''/* probe_density.c -- NOT I-114's; ours. Counts prefilter-approved
 * candidate positions across a whole subject (the sequence of windows the
 * hand-twin's retry-time rx_prefilter calls would see if every attempt
 * failed) against the real find-all match count, to characterise the
 * sparse/dense split I-114 asks for. #included with the target rowN.c so
 * it can call the static rx_prefilter directly. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <stdint.h>

#include TARGET_FILE

int main(int argc, char **argv) {
    if (argc != 2) { fprintf(stderr, "usage: %s SUBJECT_FILE\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("fopen"); return 2; }
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    unsigned char *buf = malloc((size_t)sz);
    if (fread(buf, 1, (size_t)sz, f) != (size_t)sz) { perror("fread"); return 2; }
    fclose(f);
    size_t n = (size_t)sz;

    long candidates = 0;
    size_t pos = 0;
    ptrdiff_t window[1][2];
    while (pos <= n) {
        if (rx_prefilter(buf, n, pos, window) != 1) break;
        candidates++;
        size_t next = (size_t)window[0][1];
        if (next <= pos) next = pos + 1;
        pos = next;
    }

    long matches = 0;
    pos = 0;
    ptrdiff_t caps[1][2];
    while (pos <= n) {
        int ok = rx_search(buf, n, pos, caps);
        if (!ok) break;
        matches++;
        ptrdiff_t start = caps[0][0], end = caps[0][1];
        if (end > start) pos = (size_t)end;
        else pos = rx_next_pos(buf, n, pos);
    }

    printf("subject_bytes=%ld candidates=%ld matches=%ld candidates_per_match=%.3f reject_rate=%.6f\n",
           sz, candidates, matches,
           matches > 0 ? (double)candidates / (double)matches : -1.0,
           candidates > 0 ? 1.0 - (double)matches / (double)candidates : 0.0);
    free(buf);
    return 0;
}
'''

SEED = 20260927


def gen_mixed_1m(seed=SEED):
    rng = random.Random(seed)
    ascii_words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
                    "cat", "apple", "exit", "axiom", "next", "index", "excess",
                    "extra", "annex", "exam", "text", "context", "example"]
    latin_extra = ["café", "déjà", "naïve", "élan", "exposé", "protégé"]
    cjk_words = ["日本語", "東京都", "本州", "京都府", "本日", "日本"]
    out, size, target = [], 0, 1_000_000
    while size < target:
        r = rng.random()
        if r < 0.85:
            w = rng.choice(ascii_words)
        elif r < 0.95:
            w = rng.choice(latin_extra)
        else:
            w = rng.choice(cjk_words)
        out.append(w)
        out.append(" ")
        size += len(w.encode("utf-8")) + 1
    return "".join(out).encode("utf-8")[:target]


def gen_64k_ascii(seed=SEED + 1):
    rng = random.Random(seed)
    letters = "bcdfghijklmnopqrstuvwyz "
    out, size, target = [], 0, 65536
    while size < target:
        r = rng.random()
        if r < 0.08:
            ch = "x"
        elif r < 0.085:
            ch = "a"
        else:
            ch = rng.choice(letters)
        out.append(ch)
        size += 1
    return "".join(out).encode("ascii")[:target]


def gen_match_dense(seed=SEED + 2):
    rng = random.Random(seed)
    units = ["ax", "éx", "日本", "本", "日", "x", "a"]
    out, size, target = [], 0, 200_000
    while size < target:
        b = rng.choice(units).encode("utf-8")
        out.append(b)
        size += len(b)
    return b"".join(out)[:target]


def run(cmd, **kw):
    print("+ " + " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def sh(cmd):
    print("$ " + cmd)
    return subprocess.run(["/bin/sh", "-c", cmd], check=True, capture_output=True, text=True)


def load_avg():
    return pathlib.Path("/proc/loadavg").read_text().split()[:3]


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=21)
    ap.add_argument("--out", default=None, help="scratch working dir (default: mkdtemp under /var/tmp)")
    args = ap.parse_args()

    import tempfile
    workdir = pathlib.Path(args.out) if args.out else pathlib.Path(tempfile.mkdtemp(prefix="b109twin-", dir="/var/tmp"))
    workdir.mkdir(parents=True, exist_ok=True)
    print(f"=== workdir: {workdir} ===")

    pin_sh = REPO_ROOT / "testees" / "pcrec" / "pin.sh"
    pcrec_bin = run([str(pin_sh), "--path", PIN]).stdout.strip()
    if not pathlib.Path(pcrec_bin).is_file():
        print(f"pin binary not found at {pcrec_bin}; run testees/pcrec/pin.sh {PIN} first", file=sys.stderr)
        return 2
    print(f"=== pcrec binary: {pcrec_bin} ===")
    print(run([pcrec_bin, "--version"]).stdout.strip())

    print(f"=== load before: {load_avg()} ===")

    # 1. compile the three patterns at the pin
    for stem, (name, pat) in PATTERNS.items():
        out_c = workdir / f"{stem}.c"
        run([pcrec_bin, "--features", "all", "-p", "rx", "-e", "utf8",
             "-o", str(out_c), "--pattern", pat])

    # 2. verify the retry-loop shape and apply the 8-line hand twin
    needle = ("        attempt_position++;\n"
              "        while (attempt_position < subject_length\n"
              "               && (subject[attempt_position] & 0xC0) == 0x80) attempt_position++;\n"
              "    }\n")
    for stem in PATTERNS:
        src = (workdir / f"{stem}.c").read_text()
        n = src.count(needle)
        assert n == 1, f"{stem}: retry-loop needle found {n} times (expected 1) -- I-114's shape may not match this pin"
        replacement = needle[:-len("    }\n")] + TWIN_BLOCK + "    }\n"
        twin_src = src.replace(needle, replacement, 1)
        (workdir / f"{stem}_twin.c").write_text(twin_src)
        print(f"=== {stem}: twin applied (needle matched exactly once) ===")

    # 3. write drv.c and the density probe
    (workdir / "drv.c").write_text(DRV_C)
    (workdir / "probe_density.c").write_text(PROBE_DENSITY_C)

    # 4. compile orig+twin x gcc+clang
    (workdir / "bin").mkdir(exist_ok=True)
    ccs = ["gcc", "clang"]
    variants = ["orig", "twin"]
    for stem in PATTERNS:
        for variant in variants:
            src = f"{stem}.c" if variant == "orig" else f"{stem}_twin.c"
            for cc in ccs:
                out_bin = workdir / "bin" / f"{stem}_{variant}_{cc}"
                r = subprocess.run(
                    ["/usr/bin/gnutimeout", "60", cc, "-O2", "-Wall", "-Wextra",
                     "-o", str(out_bin), str(workdir / src), str(workdir / "drv.c"), "-lm"],
                    capture_output=True, text=True, cwd=workdir)
                status = "OK, zero warnings" if (r.returncode == 0 and not r.stderr.strip()) else \
                         ("OK, WITH WARNINGS" if r.returncode == 0 else "BUILD FAILED")
                print(f"=== build {stem}_{variant}_{cc}: {status} ===")
                if r.stderr.strip():
                    print(r.stderr)
                assert r.returncode == 0

    # 5. density probes (gcc only; static rx_prefilter/rx_search counted once
    # per pattern, compiler-independent by construction)
    for stem in PATTERNS:
        out_bin = workdir / "bin" / f"probe_density_{stem}"
        r = subprocess.run(
            ["gcc", "-O2", f"-DTARGET_FILE=\"{stem}.c\"",
             "-o", str(out_bin), str(workdir / "probe_density.c")],
            capture_output=True, text=True, cwd=workdir)
        assert r.returncode == 0, r.stderr
        print(f"=== build probe_density_{stem}: OK ===")

    # 6. subjects: the bench's own seven utf8 throughput subjects + I-114's
    # three synthetic ones (regenerated here, byte-identical by seed)
    (workdir / "subjects").mkdir(exist_ok=True)
    bench_dir = REPO_ROOT / "bench" / "utf8" / "throughput"
    manifest = {}
    for line in (REPO_ROOT / "bench" / "utf8" / "manifest_throughput.tsv").read_text().splitlines()[1:]:
        parts = line.split("\t")
        manifest[parts[0]] = parts[2]
    for subj in BENCH_SUBJECTS:
        src = bench_dir / f"{subj}.bin"
        if not src.is_file():
            print(f"MISSING {src} -- run python3 bench/utf8/gen_throughput_subjects.py first", file=sys.stderr)
            return 2
        dst = workdir / "subjects" / f"{subj}.bin"
        shutil.copy(src, dst)
        got = hashlib.sha256(dst.read_bytes()).hexdigest()
        want = manifest.get(subj)
        assert got == want, f"{subj}: sha256 {got} != manifest {want}"
        print(f"=== subject {subj}.bin: {dst.stat().st_size} B, sha256 matches manifest_throughput.tsv ===")

    (workdir / "subjects" / "synth-1m.bin").write_bytes(gen_mixed_1m())
    (workdir / "subjects" / "synth-64k-asc.bin").write_bytes(gen_64k_ascii())
    (workdir / "subjects" / "synth-dense.bin").write_bytes(gen_match_dense())
    for subj in SYNTH_SUBJECTS:
        p = workdir / "subjects" / f"{subj}.bin"
        print(f"=== subject {subj}.bin: {p.stat().st_size} B, sha256={hashlib.sha256(p.read_bytes()).hexdigest()} ===")

    all_subjects = BENCH_SUBJECTS + SYNTH_SUBJECTS

    # 7. density census
    print()
    print("=== candidate-density census (prefilter candidates vs real matches, per pattern x subject) ===")
    print(f"{'pattern':16} {'subject':14} {'bytes':>10} {'candidates':>12} {'matches':>10} {'cand/match':>12} {'reject_rate':>12}")
    density = {}
    for stem in PATTERNS:
        for subj in all_subjects:
            r = subprocess.run([str(workdir / "bin" / f"probe_density_{stem}"),
                                 str(workdir / "subjects" / f"{subj}.bin")],
                                capture_output=True, text=True, check=True)
            line = r.stdout.strip()
            fields = dict(kv.split("=") for kv in line.split())
            density[(stem, subj)] = fields
            print(f"{stem:16} {subj:14} {fields['subject_bytes']:>10} {fields['candidates']:>12} "
                  f"{fields['matches']:>10} {fields['candidates_per_match']:>12} {fields['reject_rate']:>12}")

    # 8. timing matrix: NTRIALS per cell, drop trial 1 (schedutil frequency
    # ramp-up: verified to bias early trials on this box -- see the report)
    print()
    print(f"=== timing matrix, {args.trials} trials/cell, VERBATIM driver output ===")
    matrix = {}
    for stem in PATTERNS:
        for subj in all_subjects:
            for cc in ccs:
                for variant in variants:
                    bin_path = workdir / "bin" / f"{stem}_{variant}_{cc}"
                    subj_path = workdir / "subjects" / f"{subj}.bin"
                    r = subprocess.run(["/usr/bin/gnutimeout", "120", str(bin_path),
                                         str(subj_path), str(args.trials)],
                                        capture_output=True, text=True)
                    line = r.stdout.strip()
                    print(f"{stem}\t{subj}\t{cc}\t{variant}\t{line}")
                    if r.stderr.strip():
                        print(f"  STDERR: {r.stderr.strip()}")
                    fields = dict(kv.split("=", 1) for kv in line.split(" ", 3) if "=" in kv)
                    matches = int(fields["matches"])
                    hashv = fields["hash"]
                    all_us = [float(x) for x in fields["all_us"].split(",")]
                    matrix[(stem, subj, cc, variant)] = (matches, hashv, all_us)

    print(f"=== load after: {load_avg()} ===")

    # 9. answer identity check
    print()
    print("=== ANSWER IDENTITY: orig vs twin (matches, hash) per (pattern,subject,cc) ===")
    mismatches = []
    for stem in PATTERNS:
        for subj in all_subjects:
            for cc in ccs:
                o = matrix[(stem, subj, cc, "orig")]
                t = matrix[(stem, subj, cc, "twin")]
                ok = (o[0] == t[0] and o[1] == t[1])
                if not ok:
                    mismatches.append((stem, subj, cc, o[:2], t[:2]))
    if mismatches:
        print(f"MISMATCHES: {len(mismatches)}")
        for m in mismatches:
            print("  ", m)
    else:
        n = len(PATTERNS) * len(all_subjects) * len(ccs)
        print(f"ALL IDENTICAL: {n}/{n} (pattern,subject,cc) cells agree, matches and full-span hash.")

    print()
    print("=== ANSWER IDENTITY: gcc vs clang (same variant), a bonus cross-check ===")
    cc_mismatches = []
    for stem in PATTERNS:
        for subj in all_subjects:
            for variant in variants:
                g = matrix[(stem, subj, "gcc", variant)]
                c = matrix[(stem, subj, "clang", variant)]
                if g[0] != c[0] or g[1] != c[1]:
                    cc_mismatches.append((stem, subj, variant, g[:2], c[:2]))
    if cc_mismatches:
        print(f"MISMATCHES: {len(cc_mismatches)}")
        for m in cc_mismatches:
            print("  ", m)
    else:
        n = len(PATTERNS) * len(all_subjects) * len(variants)
        print(f"ALL IDENTICAL: {n}/{n} cells agree.")

    # 10. summary: median (trials[1:], dropping the warm-up trial)+spread, ratio
    print()
    print("=== SUMMARY: median of trials[1:] (us; trial 0 dropped, schedutil warm-up), "
          "spread=max-min, ratio=orig_median/twin_median ===")
    hdr = (f"{'pattern':16} {'label':16} {'subject':14} {'cc':6} {'matches':>8} "
           f"{'cand/match':>11} {'orig_med':>10} {'orig_sprd':>10} {'twin_med':>10} {'twin_sprd':>10} {'ratio':>8}")
    print(hdr)
    summary_rows = []
    for stem, (label, pat) in PATTERNS.items():
        for subj in all_subjects:
            for cc in ccs:
                o = matrix[(stem, subj, cc, "orig")]
                t = matrix[(stem, subj, cc, "twin")]
                o_trials = o[2][1:]
                t_trials = t[2][1:]
                om = st.median(o_trials)
                tm = st.median(t_trials)
                osprd = max(o_trials) - min(o_trials)
                tsprd = max(t_trials) - min(t_trials)
                ratio = om / tm if tm > 0 else float("inf")
                cpm = density[(stem, subj)]["candidates_per_match"]
                summary_rows.append((stem, label, subj, cc, o[0], cpm, om, osprd, tm, tsprd, ratio))
                print(f"{stem:16} {label:16} {subj:14} {cc:6} {o[0]:>8} {cpm:>11} "
                      f"{om:>10.3f} {osprd:>10.3f} {tm:>10.3f} {tsprd:>10.3f} {ratio:>8.3f}")

    print()
    print("=== DONE ===")
    print(f"workdir: {workdir} (not cleaned up; remove by hand if not wanted)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
