"""docs/dev/measurements/probe_b120b121read_step0_pin_control.py -- lane
b120b121read, step 0 (manager's brief): re-measure [B120]'s own named
BIMODAL cell -- `asr-lb-fixed` gcc `synth-64k-asc`, default vs
`-fno-hyb-reseed` -- the one `probe_b120_reseed_multilaunch.py` flagged
("default's own min undercuts denied's own min ... re-measure with more
launches before trusting the median"). O-69/[B112]'s own finding is that
`taskset -c N` pinning removes the per-launch CPU-governor lottery
(0/40 slow launches pinned vs 13-20% unpinned); this probe asks directly
whether the ×0.49ish inversion the manager cited survives pinning.

Restricted to ONE (pattern, subject, cc) pair, two arms (default/denied),
at 45 FRESH launches each unpinned plus a `taskset -c 3`-pinned arm at 15
launches each (core 3 chosen to match [B112]'s own probe, which pinned
core 3 and found 0/40 slow there). Same compile recipe, driver and
subject generator as `probe_b120_reseed_multilaunch.py` (imported
verbatim where possible; the two generators below are copy-pasted
byte-for-byte from that file's own `gen_64k_ascii`/DRV_C, deliberately,
so this file's numbers are directly comparable without depending on the
other file's CLI).

Run from the repo root (pin.sh must have built fc719ca4 already):

    python3 docs/dev/measurements/probe_b120b121read_step0_pin_control.py
"""
import pathlib
import random
import re
import subprocess
import sys
import tempfile

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
PIN = "fc719ca4"

sys.path.insert(0, str(REPO_ROOT))

# -- verbatim from probe_b120_reseed_multilaunch.py (DRV_C) -----------------
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

SEED = 20260927 + 1  # gen_64k_ascii's own seed offset, verbatim


def gen_64k_ascii(seed=SEED):
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


def run(cmd, **kw):
    print("+ " + " ".join(str(c) for c in cmd))
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def load_avg():
    return pathlib.Path("/proc/loadavg").read_text().split()[:3]


def mpstat_snapshot():
    r = subprocess.run(["mpstat", "-P", "ALL", "1", "1"], capture_output=True, text=True)
    return r.stdout


def emit(binary, flags, pattern, out_c):
    for p in (out_c, out_c[:-2] + ".h"):
        if pathlib.Path(p).exists():
            pathlib.Path(p).unlink()
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


def one_cell(binpath, subj, ntrials, taskset_core=None):
    cmd = ["/usr/bin/gnutimeout", "30"]
    if taskset_core is not None:
        cmd += ["taskset", "-c", str(taskset_core)]
    cmd += [str(binpath), str(subj), str(ntrials)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r


def stats(bests):
    s = sorted(bests)
    n = len(s)
    med = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0
    return {"n": n, "min": s[0], "max": s[-1], "median": med,
            "slow_count_1_5x_min": sum(1 for v in s if v > 1.5 * s[0])}


def main():
    print("=== source: docs/dev/measurements/probe_b120b121read_step0_pin_control.py ===")
    print("=== lane b120b121read, step 0 -- the manager's [B120] bimodal-cell re-measure ===")
    print("=== date: 2026-10-02 ===")
    print("=== pin: %s ===" % PIN)

    workdir = pathlib.Path(tempfile.mkdtemp(prefix="b120b121read-step0-", dir="/var/tmp"))
    print("=== workdir: %s ===" % workdir)

    pin_sh = REPO_ROOT / "testees" / "pcrec" / "pin.sh"
    pcrec_bin = run([str(pin_sh), "--path", PIN]).stdout.strip()
    if not pathlib.Path(pcrec_bin).is_file():
        sys.exit("pin binary not found at %s" % pcrec_bin)
    print("=== pcrec binary: %s ===" % pcrec_bin)

    qr = subprocess.run([sys.executable, "-m", "pcrecbench", "quiet", "--samples", "5"],
                         capture_output=True, text=True, cwd=REPO_ROOT)
    print("=== quiet gate ===")
    print(qr.stdout)
    print("=== load before: %s ===" % (load_avg(),))
    print("=== mpstat before ===")
    print(mpstat_snapshot())

    from pcrecbench import subbench as _sb
    utf8_sb = _sb.find("utf8")
    pat = utf8_sb.pattern_bytes("asr-lb-fixed")

    (workdir / "drv.c").write_text(DRV_C)

    CAPS_UTF8 = ["--features", "all", "-e", "utf8"]
    DENY = ["-fno-hyb-reseed"]
    bins = {}
    for variant, flags in (("default", CAPS_UTF8), ("denied", CAPS_UTF8 + DENY)):
        out_c = workdir / ("asr-lb-fixed_%s.c" % variant)
        if not emit(pcrec_bin, flags, pat, str(out_c)):
            continue
        out_bin = workdir / "bin" / ("asr-lb-fixed_%s_gcc" % variant)
        out_bin.parent.mkdir(exist_ok=True, parents=True)
        if build("gcc", [out_c, workdir / "drv.c"], out_bin, workdir):
            bins[variant] = out_bin
    print("=== binaries built: %d/2 ===" % len(bins))

    subj_dir = workdir / "subjects"
    subj_dir.mkdir(exist_ok=True)
    subj = subj_dir / "synth-64k-asc.bin"
    subj.write_bytes(gen_64k_ascii())
    print("=== subject: synth-64k-asc.bin, %d bytes ===" % subj.stat().st_size)

    NTRIALS = 21
    results = {}
    answer = {}

    print("=== UNPINNED: 45 fresh launches per arm ===")
    for variant, binpath in sorted(bins.items()):
        bests = []
        answers = set()
        for _ in range(45):
            r = one_cell(binpath, subj, NTRIALS)
            m = re.search(r"best_us=([0-9.]+)", r.stdout)
            a = re.search(r"matches=(\d+) hash=([0-9a-f]+)", r.stdout)
            if "NONDETERMINISM" in r.stderr:
                print("NONDETERMINISM:", variant, r.stderr)
            if m:
                bests.append(float(m.group(1)))
            if a:
                answers.add((a.group(1), a.group(2)))
        results[("unpinned", variant)] = bests
        answer[("unpinned", variant)] = answers
        print("raw unpinned %s bests_us=%s" % (variant, bests))

    print("=== PINNED (taskset -c 3): 15 fresh launches per arm ===")
    for variant, binpath in sorted(bins.items()):
        bests = []
        answers = set()
        for _ in range(15):
            r = one_cell(binpath, subj, NTRIALS, taskset_core=3)
            m = re.search(r"best_us=([0-9.]+)", r.stdout)
            a = re.search(r"matches=(\d+) hash=([0-9a-f]+)", r.stdout)
            if "NONDETERMINISM" in r.stderr:
                print("NONDETERMINISM:", variant, r.stderr)
            if m:
                bests.append(float(m.group(1)))
            if a:
                answers.add((a.group(1), a.group(2)))
        results[("pinned", variant)] = bests
        answer[("pinned", variant)] = answers
        print("raw pinned %s bests_us=%s" % (variant, bests))

    print("=== load after: %s ===" % (load_avg(),))
    print("=== mpstat after ===")
    print(mpstat_snapshot())

    print("=== ANSWER IDENTITY ===")
    all_answers = set()
    for k, v in answer.items():
        print(k, "->", v)
        all_answers |= v
    print("distinct answers across all arms: %d (1 == no answer movement)" % len(all_answers))

    print("=== SUMMARY ===")
    print("arm_group\tvariant\tn\tmin_us\tmedian_us\tmax_us\tn_slow_gt_1.5x_min")
    for key in [("unpinned", "default"), ("unpinned", "denied"),
                ("pinned", "default"), ("pinned", "denied")]:
        if key not in results or not results[key]:
            continue
        st = stats(results[key])
        print("%s\t%s\t%d\t%.1f\t%.1f\t%.1f\t%d" % (
            key[0], key[1], st["n"], st["min"], st["median"], st["max"],
            st["slow_count_1_5x_min"]))

    for group in ("unpinned", "pinned"):
        d = results.get((group, "default"))
        n = results.get((group, "denied"))
        if d and n:
            sd, sn = stats(d), stats(n)
            print("%s ratio (default/denied) median: %.4f  min/min: %.4f" % (
                group, sd["median"] / sn["median"], sd["min"] / sn["min"]))


if __name__ == "__main__":
    main()
