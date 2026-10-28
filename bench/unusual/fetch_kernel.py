#!/usr/bin/env python3
"""fetch_kernel.py -- fetch + verify the five Linux kernel source files for
the F2 `kernel-bodies` subjects (docs/design/unusual_set_v1.md 4.2, OQ-4 RULED).

STATUS: WRITTEN, NOT RUN. Every row of TABLE below has an EMPTY url/sha256, and
an empty row is a refusal BY NAME: nothing is fetched until the manager has
shown Frank EACH FILE's exact URL and sha256 and Frank has approved that file
(one approval per file; user CLAUDE.md "Security"). A row filled and approved
fetches that file alone; the other rows stay refused.

The five files (at the LATEST STABLE tag at fetch time, the tag recorded in
KERNEL_TAG once chosen):
    kernel/sched/core.c    mm/memory.c    fs/namei.c    net/core/dev.c    lib/vsprintf.c

URL shape to fill in (raw file at a tag, https only, kernel.org or its
GitHub mirror -- the host is checked):
    https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/<path>?h=<KERNEL_TAG>
GPL-2.0: the text is fetched to build/unusual/kernel/ (gitignored) and NEVER
committed or redistributed; the generated subjects are gitignored like every
set's. Absent file = that file's `kernel-bodies` subject skipped BY NAME.
Run with `python3 -I`; each file lands in its own new empty directory.

    python3 -I bench/unusual/fetch_kernel.py [path ...]    # default: every approved row
"""
import hashlib
import os
import sys
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(ROOT, "build", "unusual", "kernel")

KERNEL_TAG = ""        # e.g. "v7.0.9" -- chosen and shown to Frank at fetch time

# path in the tree -> (exact url, sha256 of the file as served); empty = not approved
TABLE = {
    "kernel/sched/core.c": ("", ""),
    "mm/memory.c": ("", ""),
    "fs/namei.c": ("", ""),
    "net/core/dev.c": ("", ""),
    "lib/vsprintf.c": ("", ""),
}
ALLOWED_HOSTS = ("git.kernel.org", "raw.githubusercontent.com")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def fetch_one(path):
    url, want = TABLE[path]
    if not url or not want or not KERNEL_TAG:
        sys.stderr.write("fetch_kernel: REFUSED %s -- url/sha256/KERNEL_TAG not filled (no approval recorded); "
                         "its kernel-bodies subject is skipped BY NAME\n" % path)
        return 2
    u = urllib.parse.urlparse(url)
    if u.scheme != "https" or u.hostname not in ALLOWED_HOSTS:
        sys.stderr.write("fetch_kernel: REFUSED %s -- host %r not in %r\n" % (path, u.hostname, ALLOWED_HOSTS))
        return 2
    d = os.path.join(WORK, path.replace("/", "__"))
    if os.path.exists(d) and os.listdir(d):
        sys.stderr.write("fetch_kernel: REFUSED %s -- %s is not empty\n" % (path, d))
        return 2
    os.makedirs(d, exist_ok=True)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "pcrec-bench-fetch/1"}), timeout=120) as r:
        if urllib.parse.urlparse(r.geturl()).hostname not in ALLOWED_HOSTS:
            sys.stderr.write("fetch_kernel: REFUSED %s -- redirected to %s\n" % (path, r.geturl()))
            return 2
        data = r.read()
    if sha(data) != want:
        sys.stderr.write("fetch_kernel: REFUSED %s -- sha256 %s != pinned %s (nothing written)\n" % (path, sha(data), want))
        return 2
    with open(os.path.join(d, os.path.basename(path)), "wb") as f:
        f.write(data)
    print("fetched %s (%d bytes, tag %s)" % (path, len(data), KERNEL_TAG))
    return 0


def main(argv):
    paths = argv or list(TABLE)
    rc = 0
    for p in paths:
        if p not in TABLE:
            sys.stderr.write("fetch_kernel: unknown path %s\n" % p)
            rc = 2
            continue
        rc = max(rc, fetch_one(p))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
