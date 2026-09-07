#!/usr/bin/env python3
"""Move fully-acked, aged-out entries out of docs/dev/inbox_from_pcrec.md
into docs/dev/inbox_from_pcrec_archive.md.

PROTOCOL CONTEXT (BD5, pcrec D78; amended BD11 2026-09-07). The inbox
file has one writer, the pcrec manager session; this session's only
documented write there is a single `ack:` line per item, and the file's
own header says items are "never deleted; superseded items say so in
place". BD11 adds ONE exception to that, ruled by Frank directly: an
item may be RELOCATED, verbatim, byte-for-byte, once it (a) carries at
least one `ack:` line — proof this session already acted on it and
recorded where — and (b) is not among the most recent `--keep-recent`
entries by file position (recency is judged by position in the file,
not by parsing item numbers or dates: item numbers are not strictly
monotonic with time in this file — e.g. I-19/I-20 appear out of numeric
order — but file position always is). Nothing is ever edited, only
moved; the archive file inherits the same never-delete rule the source
states. An item with no ack line is NEVER touched, regardless of age.

Usage:
    python3 tools/archive_inbox.py [--keep-recent N] [--dry-run]

Safety properties, all enforced in-line (not just asserted in prose):
  1. Refuses to run at all if splitting the source file does not
     reconstruct it byte-for-byte (a malformed entry boundary would
     otherwise silently drop text).
  2. Idempotent: entries already present in the archive (by item id)
     are skipped on a re-run rather than duplicated.
  3. After writing, re-reads the archive file and asserts every entry
     just archived is present in it verbatim before touching the source.
"""
import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INBOX = REPO_ROOT / "docs" / "dev" / "inbox_from_pcrec.md"
ARCHIVE = REPO_ROOT / "docs" / "dev" / "inbox_from_pcrec_archive.md"

ENTRY_SPLIT_RE = re.compile(r"(?m)^(?=## I-)")
HEADER_ID_RE = re.compile(r"^## (I-\S+)")
ACK_RE = re.compile(r"(?m)^ack: ")

ARCHIVE_HEADER = """# Archive of fully-acked inbox_from_pcrec.md entries

Moved here verbatim by `tools/archive_inbox.py` (BD11, 2026-09-07):
`docs/dev/inbox_from_pcrec.md` keeps a recent window of entries live for
fast wake-time reading; an entry moves here once it (a) carries at least
one `ack:` line — this session already acted on it — and (b) has aged
out of the live file's `--keep-recent` window by file position. Content
is byte-identical to what stood in the live file (header line, body, ack
line(s)); an archived entry is never edited or deleted afterward, same
as the source file's own rule. Entries below are in original file order
(oldest first); the archiving script appends new entries to the end.

---

"""


def split_entries(text):
    parts = ENTRY_SPLIT_RE.split(text)
    return parts[0], parts[1:]


def entry_id(entry):
    m = HEADER_ID_RE.match(entry)
    return m.group(1) if m else None


def has_ack(entry):
    return bool(ACK_RE.search(entry))


def existing_archive_ids(archive_text):
    if not archive_text:
        return set()
    _, entries = split_entries(archive_text)
    return {entry_id(e) for e in entries}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--keep-recent",
        type=int,
        default=15,
        help="always keep this many most-recent entries (by file position) "
        "live, regardless of ack status (default: 15)",
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="report what would move, write nothing"
    )
    args = ap.parse_args()

    if not INBOX.exists():
        print(f"ERROR: {INBOX} not found", file=sys.stderr)
        return 1

    source_text = INBOX.read_text()
    preamble, entries = split_entries(source_text)
    if preamble + "".join(entries) != source_text:
        print(
            "ERROR: splitting the inbox into entries does not reconstruct it "
            "byte-for-byte — refusing to touch the file (a malformed '## I-' "
            "boundary would otherwise silently drop text)",
            file=sys.stderr,
        )
        return 1

    n = len(entries)
    cutoff = max(0, n - args.keep_recent)  # positions [0, cutoff) are "old enough"

    to_archive = []
    to_keep = []
    for i, e in enumerate(entries):
        if i < cutoff and has_ack(e):
            to_archive.append(e)
        else:
            to_keep.append(e)

    print(
        f"{n} entries total; keep-recent={args.keep_recent}; "
        f"{len(to_archive)} eligible to archive, {len(to_keep)} stay live."
    )

    if not to_archive:
        print("Nothing to archive.")
        return 0

    ids = [entry_id(e) or "?" for e in to_archive]
    print("Archiving: " + ", ".join(ids))

    if args.dry_run:
        print("(dry run — nothing written)")
        return 0

    existing_text = ARCHIVE.read_text() if ARCHIVE.exists() else ""
    already = existing_archive_ids(existing_text)
    new_to_archive = [e for e in to_archive if entry_id(e) not in already]
    skipped = len(to_archive) - len(new_to_archive)
    if skipped:
        print(f"NOTE: {skipped} already present in the archive — skipped (idempotent re-run)")

    if not new_to_archive:
        print("Nothing new to write to the archive; leaving the inbox untouched.")
        return 0

    if not ARCHIVE.exists():
        ARCHIVE.write_text(ARCHIVE_HEADER + "".join(new_to_archive))
    else:
        with ARCHIVE.open("a") as f:
            f.write("".join(new_to_archive))

    # Safety property 3: verify every entry we intended to archive (not just
    # the newly-written ones) reads back verbatim from the archive file
    # before we touch the source.
    archive_text_after = ARCHIVE.read_text()
    for e in to_archive:
        if e not in archive_text_after:
            print(
                f"ERROR: post-write verification failed for {entry_id(e)} — "
                "the archive does not contain it verbatim. NOT touching the "
                "inbox file. Investigate before re-running.",
                file=sys.stderr,
            )
            return 1

    INBOX.write_text(preamble + "".join(to_keep))

    print(f"Wrote {len(new_to_archive)} entries to {ARCHIVE.relative_to(REPO_ROOT)}")
    print(f"Rewrote {INBOX.relative_to(REPO_ROOT)}: {len(to_keep)} entries remain live.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
