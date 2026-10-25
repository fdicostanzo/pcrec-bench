#!/bin/sh
# fetch_reference.sh -- download the REAL Apache access log the generated
# subjects are calibrated against, and verify it BEFORE it is used.
#
#   source : github.com/elastic/examples, commit
#            bc53b584c0f9f574d4373193334bf03541a54936,
#            path "Common Data Formats/apache_logs/apache_logs"
#   blob   : git blob 94bf224f30abf42f3707db4fc02c90362e0ba338
#   sha256 : f15c31e905f86c7b4b6ab44aee74d0a2086dce89f010187d983edea7ef0364ef
#   size   : 2,370,789 bytes, 10,000 lines (Apache-2.0, redistribution is
#            permitted but this repository does not redistribute it)
#
# It is DATA. Nothing here (or in calibrate.py) executes, imports or evals
# it. The file lands in build/subst-ref/ (gitignored) -- never committed.
#
# Both digests are checked, SHA-256 and the git blob hash (sha1 over
# "blob <size>\0" + content, computed here without git), and a mismatch on
# either REFUSES: the temporary download is deleted and nothing is placed.
# `make check` never runs this script (it never fetches); a box without the
# file simply skips the calibration check BY NAME (gen_subjects.py --check).
#
# Usage: bench/subst/fetch_reference.sh [DEST_DIR]   (default build/subst-ref)
set -eu

COMMIT=bc53b584c0f9f574d4373193334bf03541a54936
URL="https://raw.githubusercontent.com/elastic/examples/${COMMIT}/Common%20Data%20Formats/apache_logs/apache_logs"
WANT_SHA256=f15c31e905f86c7b4b6ab44aee74d0a2086dce89f010187d983edea7ef0364ef
WANT_BLOB=94bf224f30abf42f3707db4fc02c90362e0ba338

here=$(cd "$(dirname "$0")" && pwd)
root=$(cd "$here/../.." && pwd)
dest=${1:-"$root/build/subst-ref"}

if [ -e "$dest/apache_logs" ]; then
    echo "fetch_reference: $dest/apache_logs already present; verifying only"
    tmp="$dest/apache_logs"
    keep=1
else
    mkdir -p "$dest"
    tmpdir=$(mktemp -d "$dest/.fetch.XXXXXX")
    trap 'rm -rf "$tmpdir"' EXIT
    tmp="$tmpdir/apache_logs"
    curl --fail --silent --show-error --location --proto '=https' \
        --max-filesize 5000000 -o "$tmp" "$URL"
    keep=0
fi

got_sha256=$(sha256sum "$tmp" | cut -d' ' -f1)
size=$(wc -c < "$tmp" | tr -d ' ')
got_blob=$( { printf 'blob %s\0' "$size"; cat "$tmp"; } | sha1sum | cut -d' ' -f1)

fail=0
if [ "$got_sha256" != "$WANT_SHA256" ]; then
    echo "fetch_reference: REFUSED -- sha256 $got_sha256, expected $WANT_SHA256" >&2
    fail=1
fi
if [ "$got_blob" != "$WANT_BLOB" ]; then
    echo "fetch_reference: REFUSED -- git blob $got_blob, expected $WANT_BLOB" >&2
    fail=1
fi
if [ "$fail" -ne 0 ]; then
    [ "$keep" -eq 1 ] || rm -f "$tmp"
    exit 1
fi

if [ "$keep" -eq 0 ]; then
    mv "$tmp" "$dest/apache_logs"
fi
echo "fetch_reference: OK $dest/apache_logs ($size bytes, sha256 and git blob verified)"
