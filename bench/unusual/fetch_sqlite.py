#!/usr/bin/env python3
"""fetch_sqlite.py -- fetch + verify the SQLite amalgamation for the F2
`sqlite-bodies` subjects (docs/design/unusual_set_v1.md 4.2, OQ-3 RULED).

STATUS: WRITTEN, NOT RUN. The table below is EMPTY, and an empty table is a
refusal BY NAME: this script downloads nothing until the manager has shown
Frank the exact URL and sha256 below and Frank has approved them (user
CLAUDE.md "Security": never download and run -- or even fetch -- an
artifact without showing the exact file first; prefer a pinned version with a
published checksum, verified before use, inside the project tree).

To enable it, fill in ALL FOUR fields from the sqlite.org download page and
the archive's published SHA3-256/SHA-256, then commit the change:

    SQLITE_VERSION = "3.NN.N"
    ARCHIVE_URL    = "https://www.sqlite.org/<year>/sqlite-amalgamation-<NNNNNNN>.zip"
                     (<NNNNNNN> = 3 + two-digit minor + two-digit patch + "00",
                      e.g. 3.46.1 -> 3460100)
    ARCHIVE_SHA256 = "<64 hex>"       sha256 of the .zip as downloaded
    SQLITE3C_SHA256 = "<64 hex>"      sha256 of the sqlite3.c inside it

What it does when filled (nothing else):
  1. downloads ARCHIVE_URL (urllib, no redirect to a non-sqlite.org host
     accepted) into build/unusual/sqlite/dl/ -- a NEW EMPTY directory it creates;
  2. verifies ARCHIVE_SHA256 BEFORE opening the archive;
  3. extracts ONLY the member named `sqlite-amalgamation-*/sqlite3.c`
     (zipfile, never extractall) into build/unusual/sqlite/src/;
  4. verifies SQLITE3C_SHA256;
  5. writes vendor/sqlite3.c.xz (xz of the file) and vendor/sqlite3.c.xz.sha256
     with the sha256 of the archive and of the decompressed file.
It never executes anything from the archive. Run it with `python3 -I`.

    python3 -I bench/unusual/fetch_sqlite.py
"""
import hashlib
import lzma
import os
import sys
import urllib.parse
import urllib.request
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

# ---- THE TABLE (empty until approved) ------------------------------------
SQLITE_VERSION = ""
ARCHIVE_URL = ""
ARCHIVE_SHA256 = ""
SQLITE3C_SHA256 = ""
# ---------------------------------------------------------------------------

WORK = os.path.join(ROOT, "build", "unusual", "sqlite")


def refuse(msg):
    sys.stderr.write("fetch_sqlite: REFUSED -- %s\n" % msg)
    return 2


def sha(path_or_bytes):
    h = hashlib.sha256()
    if isinstance(path_or_bytes, bytes):
        h.update(path_or_bytes)
    else:
        with open(path_or_bytes, "rb") as f:
            for blk in iter(lambda: f.read(1 << 20), b""):
                h.update(blk)
    return h.hexdigest()


def main():
    missing = [n for n, v in (("SQLITE_VERSION", SQLITE_VERSION), ("ARCHIVE_URL", ARCHIVE_URL),
                              ("ARCHIVE_SHA256", ARCHIVE_SHA256), ("SQLITE3C_SHA256", SQLITE3C_SHA256)) if not v]
    if missing:
        return refuse("the pinned-fetch table is empty (%s). The F2 sqlite-bodies subjects are skipped BY NAME "
                      "(skipped_subjects.tsv) until Frank approves the exact URL + sha256." % ", ".join(missing))
    u = urllib.parse.urlparse(ARCHIVE_URL)
    if u.scheme != "https" or u.hostname != "www.sqlite.org":
        return refuse("ARCHIVE_URL must be https://www.sqlite.org/...; got %r" % ARCHIVE_URL)
    dl = os.path.join(WORK, "dl")
    src = os.path.join(WORK, "src")
    for d in (dl, src):
        if os.path.exists(d) and os.listdir(d):
            return refuse("%s is not empty; remove it by hand (this script writes only into new empty directories)" % d)
        os.makedirs(d, exist_ok=True)
    archive = os.path.join(dl, "sqlite-amalgamation.zip")
    req = urllib.request.Request(ARCHIVE_URL, headers={"User-Agent": "pcrec-bench-fetch/1"})
    with urllib.request.urlopen(req, timeout=120) as r:
        if urllib.parse.urlparse(r.geturl()).hostname != "www.sqlite.org":
            return refuse("redirected away from www.sqlite.org: %s" % r.geturl())
        with open(archive, "wb") as f:
            f.write(r.read())
    if sha(archive) != ARCHIVE_SHA256:
        return refuse("archive sha256 %s != pinned %s" % (sha(archive), ARCHIVE_SHA256))
    with zipfile.ZipFile(archive) as z:
        names = [n for n in z.namelist() if n.endswith("/sqlite3.c") and n.count("/") == 1]
        if len(names) != 1:
            return refuse("expected exactly one sqlite-amalgamation-*/sqlite3.c member, found %r" % names)
        data = z.read(names[0])
    if sha(data) != SQLITE3C_SHA256:
        return refuse("sqlite3.c sha256 %s != pinned %s" % (sha(data), SQLITE3C_SHA256))
    with open(os.path.join(src, "sqlite3.c"), "wb") as f:
        f.write(data)
    vend = os.path.join(HERE, "vendor")
    os.makedirs(vend, exist_ok=True)
    with lzma.open(os.path.join(vend, "sqlite3.c.xz"), "wb") as f:
        f.write(data)
    with open(os.path.join(vend, "sqlite3.c.xz.sha256"), "w") as f:
        f.write("version\t%s\nurl\t%s\narchive_sha256\t%s\nsqlite3_c_sha256\t%s\nxz_sha256\t%s\n"
                % (SQLITE_VERSION, ARCHIVE_URL, ARCHIVE_SHA256, SQLITE3C_SHA256,
                   sha(os.path.join(vend, "sqlite3.c.xz"))))
    print("fetched sqlite %s: %d bytes of sqlite3.c, vendored as vendor/sqlite3.c.xz" % (SQLITE_VERSION, len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
