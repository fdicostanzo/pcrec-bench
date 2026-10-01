"""docs/dev/measurements/probe_b120_reseed_multilaunch.py -- [B120]
(lane b120reseed, inbox I-124) PHASE C items 1+2: the [OPT-HYB-RESEED]
adaptive-retry x86 TIMING, at the pin fc719ca4 (abi 50) -- the SAME
compile-only-twin-plus-multilaunch protocol `probe_b109_reseed_twin.py`
+ `probe_b109_multilaunch.sh` used for the hand-twin's own x86 confirm,
with ONE difference: the "twin" here IS the pin's own `-fno-hyb-reseed`
deny flag, a real pcrec CLI option, so no source patching is needed at
all (I-114's 8-line hand-twin diff and its TWIN_BLOCK do not appear
here).

TWO GROUPS, matching I-124's own two items:

  GROUP U (item 1): utf8@0.1's `asr-lb-varwidth` / `asr-lb-fixed` /
  `asr-lb-neg`, compiled `-e utf8`, default vs `-fno-hyb-reseed`, BOTH
  gcc and clang (O-68's bimodality note), over all seven bench/utf8
  throughput subjects PLUS I-114's three synthetic subjects (its own
  embedded generator, seed 20260927, reproduced verbatim from
  `probe_b109_reseed_twin.py` -- the SAME subjects, so a reader can
  compare this file's numbers against that one's directly).

  GROUP S (item 2): syntax@0.1's `lka-pos` / `lka-verb`, byte encoding,
  THREE arms (default / `-fno-hyb-reseed` / forced `--engine=vm`), gcc
  only (I-124 item 2 does not ask for both compilers), over syntax@0.1's
  three throughput subjects (t-64k/t-256k/t-1m) plus its own
  search-short subjects (sparse-candidate controls).

Both groups share ONE driver (I-114's own `drv.c`, reproduced verbatim
from `probe_b109_reseed_twin.py` -- pattern-agnostic: it links against
whichever artifact the build step produces) and the SAME per-process
multi-launch harness `probe_b109_multilaunch.sh` already proved
necessary (one-process timing on this box is bimodal per [B112]'s own
later diagnosis; this file launches N FRESH processes per cell and
keeps every one, exactly like that precedent).

Answer identity (match count + full-span FNV-1a hash) is checked on
EVERY cell before any ratio is trusted -- I-124's own closing
instruction ("answers are identical by construction; a cell whose
answer moves is a finding, to be reported before any timing").

RUN 2026-10-01 (cleared by the manager; box quiet, verdict `quiet`,
load1 0.07-0.09): `--trials 21 --launches 15`, the real run, archived
at docs/dev/measurements/2026-10-01-b120-reseed-multilaunch.txt. Zero
`NONDETERMINISM` anywhere; a separate cross-arm answer check (default
vs denied vs forced-vm, both compilers) found 0/138 mismatches. `--smoke`
(one launch, one trial, build + answer-check only, no timing claim)
remains for a quick correctness re-check before any future re-run.

Run from the repo root (pin.sh must have built fc719ca4 already):

    python3 docs/dev/measurements/probe_b120_reseed_multilaunch.py --smoke
    python3 docs/dev/measurements/probe_b120_reseed_multilaunch.py --trials 21 --launches 15
"""
import os
import pathlib
import random
import re
import subprocess
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
PIN = "fc719ca4"

sys.path.insert(0, str(REPO_ROOT))

# ---------------------------------------------------------------------------
# I-114's own drv.c, reproduced verbatim from probe_b109_reseed_twin.py
# (an extra NTRIALS argv + all_us dump added for a median+spread reading,
# both additive). Pattern-agnostic: links against rx_search/rx_next_pos,
# whichever artifact the build step produces.
DRV_C = r'''/* drv.c -- from I-114 via probe_b109_reseed_twin.py, verbatim. */
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

SEED = 20260927


# -- I-114's three synthetic generators, reproduced verbatim from
# probe_b109_reseed_twin.py (so this file's GROUP U numbers compare
# directly against the [B109] x86 confirm's own).
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


SYNTH_SUBJECTS = {
    "synth-1m": gen_mixed_1m,
    "synth-64k-asc": gen_64k_ascii,
    "synth-dense": gen_match_dense,
}


def run(cmd, **kw):
    print("+ " + " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def load_avg():
    return pathlib.Path("/proc/loadavg").read_text().split()[:3]


def emit(binary, flags, pattern, out_c):
    for p in (out_c, out_c[:-2] + ".h"):
        if os.path.exists(p):
            os.unlink(p)
    argv = [binary, "-p", "rx"] + list(flags) + ["-o", out_c, "--pattern", bytes(pattern)]
    r = subprocess.run(argv, capture_output=True)
    if r.returncode != 0:
        print("REFUSED:", r.stderr.decode("utf-8", "replace"))
        return False
    return True


def build(cc, sources, out_bin, workdir):
    argv = ["/usr/bin/gnutimeout", "60", cc, "-O2", "-Wall", "-Wextra",
            "-o", str(out_bin)] + [str(s) for s in sources] + ["-lm"]
    r = subprocess.run(argv, capture_output=True, text=True, cwd=workdir)
    if r.returncode != 0 or r.stderr.strip():
        print("BUILD %s: rc=%d\n%s" % (out_bin, r.returncode, r.stderr))
    return r.returncode == 0


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=21)
    ap.add_argument("--launches", type=int, default=15)
    ap.add_argument("--smoke", action="store_true",
                     help="one launch, one trial, build+answer-check only")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.smoke:
        args.trials, args.launches = 1, 1

    import tempfile
    workdir = pathlib.Path(args.out) if args.out else pathlib.Path(
        tempfile.mkdtemp(prefix="b120reseed-", dir="/var/tmp"))
    workdir.mkdir(parents=True, exist_ok=True)
    print("=== workdir: %s ===" % workdir)

    pin_sh = REPO_ROOT / "testees" / "pcrec" / "pin.sh"
    pcrec_bin = run([str(pin_sh), "--path", PIN]).stdout.strip()
    if not pathlib.Path(pcrec_bin).is_file():
        sys.exit("pin binary not found at %s" % pcrec_bin)
    print("=== pcrec binary: %s ===" % pcrec_bin)
    print("=== load before: %s ===" % (load_avg(),))

    from pcrecbench import subbench as _sb

    utf8_sb = _sb.find("utf8")
    syntax_sb = _sb.find("syntax")

    GROUP_U = [("asr-lb-varwidth", utf8_sb.pattern_bytes("asr-lb-varwidth")),
               ("asr-lb-fixed", utf8_sb.pattern_bytes("asr-lb-fixed")),
               ("asr-lb-neg", utf8_sb.pattern_bytes("asr-lb-neg"))]
    GROUP_S = [("lka-pos", syntax_sb.pattern_bytes("lka-pos")),
               ("lka-verb", syntax_sb.pattern_bytes("lka-verb"))]

    (workdir / "drv.c").write_text(DRV_C)

    # ---- compile GROUP U: default / denied, both cc -------------------
    CAPS_UTF8 = ["--features", "all", "-e", "utf8"]
    DENY = ["-fno-hyb-reseed"]
    u_bins = {}
    for stem, pat in GROUP_U:
        for variant, flags in (("default", CAPS_UTF8), ("denied", CAPS_UTF8 + DENY)):
            out_c = workdir / ("%s_%s.c" % (stem, variant))
            if not emit(pcrec_bin, flags, pat, str(out_c)):
                continue
            for cc in ("gcc", "clang"):
                out_bin = workdir / "bin" / ("%s_%s_%s" % (stem, variant, cc))
                out_bin.parent.mkdir(exist_ok=True)
                if build(cc, [out_c, workdir / "drv.c"], out_bin, workdir):
                    u_bins[(stem, variant, cc)] = out_bin

    # ---- compile GROUP S: default / denied / forced-vm, gcc only ------
    CAPS = ["--features", "all"]
    VM = ["--engine=vm"]
    s_bins = {}
    for stem, pat in GROUP_S:
        for variant, flags in (("default", CAPS), ("denied", CAPS + DENY),
                                ("forced-vm", CAPS + VM)):
            out_c = workdir / ("%s_%s.c" % (stem, variant))
            if not emit(pcrec_bin, flags, pat, str(out_c)):
                continue
            out_bin = workdir / "bin" / ("%s_%s_gcc" % (stem, variant))
            out_bin.parent.mkdir(exist_ok=True)
            if build("gcc", [out_c, workdir / "drv.c"], out_bin, workdir):
                s_bins[(stem, variant, "gcc")] = out_bin

    print("=== GROUP U binaries built: %d/%d ===" % (len(u_bins), 3 * 2 * 2))
    print("=== GROUP S binaries built: %d/%d ===" % (len(s_bins), 2 * 3))

    # ---- subjects -------------------------------------------------------
    subj_dir = workdir / "subjects"
    subj_dir.mkdir(exist_ok=True)
    u_subjects = {}
    utf8_tp_dir = REPO_ROOT / "bench" / "utf8" / "throughput"
    if utf8_tp_dir.is_dir():
        for p in sorted(utf8_tp_dir.glob("*.bin")):
            u_subjects[p.stem] = p
    for name, gen in SYNTH_SUBJECTS.items():
        p = subj_dir / (name + ".bin")
        p.write_bytes(gen())
        u_subjects[name] = p
    print("=== GROUP U subjects: %s ===" % sorted(u_subjects))

    s_subjects = {}
    syntax_tp_dir = REPO_ROOT / "bench" / "syntax" / "throughput"
    if syntax_tp_dir.is_dir():
        for p in sorted(syntax_tp_dir.glob("*.bin")):
            s_subjects[p.stem] = p
    print("=== GROUP S subjects: %s ===" % sorted(s_subjects))

    # ---- run (smoke: one launch, one trial; else: the real multilaunch) -
    def one_cell(binpath, subj, ntrials):
        r = subprocess.run(["/usr/bin/gnutimeout", "30", str(binpath), str(subj),
                             str(ntrials)], capture_output=True, text=True)
        return r

    print("=== running (launches=%d trials=%d) ===" % (args.launches, args.trials))
    rows = []
    for (stem, variant, cc), binpath in sorted(u_bins.items()):
        for sname, spath in sorted(u_subjects.items()):
            bests = []
            for _ in range(args.launches):
                r = one_cell(binpath, spath, args.trials)
                m = re.search(r"best_us=([0-9.]+)", r.stdout)
                if "NONDETERMINISM" in r.stderr:
                    print("NONDETERMINISM:", stem, variant, cc, sname, r.stderr)
                if m:
                    bests.append(float(m.group(1)))
            if bests:
                rows.append(("U", stem, variant, cc, sname,
                              min(bests), sorted(bests)[len(bests) // 2], max(bests)))

    for (stem, variant, cc), binpath in sorted(s_bins.items()):
        for sname, spath in sorted(s_subjects.items()):
            bests = []
            for _ in range(args.launches):
                r = one_cell(binpath, spath, args.trials)
                m = re.search(r"best_us=([0-9.]+)", r.stdout)
                if "NONDETERMINISM" in r.stderr:
                    print("NONDETERMINISM:", stem, variant, cc, sname, r.stderr)
                if m:
                    bests.append(float(m.group(1)))
            if bests:
                rows.append(("S", stem, variant, cc, sname,
                              min(bests), sorted(bests)[len(bests) // 2], max(bests)))

    print("=== load after: %s ===" % (load_avg(),))
    print("group\tpattern\tvariant\tcc\tsubject\tmin_us\tmed_us\tmax_us")
    for r in rows:
        print("\t".join(str(x) for x in r))

    if args.smoke:
        print("=== SMOKE ONLY -- not a measurement; re-run with --trials 21 "
              "--launches 15 for real numbers ===")


if __name__ == "__main__":
    main()
