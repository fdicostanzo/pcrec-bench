#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the utf8 set's seven throughput texts:
`throughput/` (gitignored) + `manifest_throughput.tsv` (committed), per
utf8_set_v1.md 4.3: the three `capability`-style sizes (64 KB / 256 KB /
1 MB) built from the `mix` grammar, PLUS a per-script 64 KB arm (`lat`,
`cyr`, `cjk`, `asc` -- `mix` at 64 KB is already the sweep's first rung).
Seven subjects, ~1.58 MB total.

Every text is built by `utf8text.text()`, which is EXACTLY its named size
in bytes (the size-fitting boundary rule: trim to the last complete
character, pad with ASCII spaces to the exact target -- see utf8text.py's
own docstring) and passed through `utf8text.decode_gate()` before its
manifest row is written.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import utf8text as ut  # noqa: E402

OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

# (id, nbytes, seed, script, description)
SIZES = (
    ("t-64k", 64 * 1024, 0x7f8a001, "mix",
     "throughput/mixed lat+cyr+cjk+asc+emoji grammar, the size sweep's "
     "first rung"),
    ("t-256k", 256 * 1024, 0x7f8a002, "mix",
     "throughput/mixed lat+cyr+cjk+asc+emoji grammar"),
    ("t-1m", 1024 * 1024, 0x7f8a003, "mix",
     "throughput/mixed lat+cyr+cjk+asc+emoji grammar"),
    ("t-64k-lat", 64 * 1024, 0x7f8a010, "lat",
     "throughput/Latin-1-Supplement-heavy (fr/de/es) prose, the "
     "per-script 64 KB arm -- 0xC3 near-universal lead byte"),
    ("t-64k-cyr", 64 * 1024, 0x7f8a011, "cyr",
     "throughput/Russian prose, the per-script 64 KB arm -- 0xD0/0xD1 "
     "the only lead bytes"),
    ("t-64k-cjk", 64 * 1024, 0x7f8a012, "cjk",
     "throughput/Japanese+Chinese prose with a Latin admixture, the "
     "per-script 64 KB arm -- 0xE3-0xE9 lead bytes"),
    ("t-64k-asc", 64 * 1024, 0x7f8a013, "asc",
     "throughput/byte-clean ASCII, the per-script 64 KB arm -- THE "
     "CONTROL, no byte >= 0x80"),
)


def build():
    texts = []
    for sid, nbytes, seed, script, desc in SIZES:
        body = ut.text(nbytes, seed, script)
        assert len(body) == nbytes, (sid, len(body), nbytes)
        ut.decode_gate(body)
        texts.append((sid, body, desc))
    return texts


def _check_decode_gate_has_teeth():
    """Same negative-arm control as `gen_subjects.py`'s own (utf8_set_v1.md
    4.1): a fixture built from a REAL throughput text but truncated at a
    raw byte offset landing INSIDE its final multi-byte character must
    FAIL the decode gate. `good` is deliberately built to END on a 3-byte
    CJK character (never on the ASCII pad `text()` may append) so `[:-1]`
    is guaranteed to cut that character in half, not merely drop a
    trailing pad byte."""
    good = ut.text(4096, 0xDEC0DE, "cjk") + "日".encode("utf-8")
    ut.decode_gate(good)  # the control: well-formed data passes
    truncated = good[:-1]  # one byte short of the trailing 3-byte 日
    try:
        ut.decode_gate(truncated)
    except UnicodeDecodeError:
        pass
    else:
        raise AssertionError(
            "decode gate has no teeth: a mid-character-truncated "
            "throughput fixture was NOT rejected")


def _render(texts):
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, body, desc in texts:
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ut.periodic_field(body)))
    return "\n".join(rows) + "\n"


def main():
    check = "--check" in sys.argv
    texts = build()
    _check_decode_gate_has_teeth()
    if check:
        if not os.path.isdir(OUT) or not os.path.isfile(MANIFEST):
            print("gen_throughput_subjects --check: FAIL (no throughput/ "
                  "or manifest_throughput.tsv -- run without --check "
                  "first)")
            return 1
        ok = True
        with open(MANIFEST, encoding="utf-8") as f:
            committed = f.read()
        rendered = _render(texts)
        if committed != rendered:
            print("gen_throughput_subjects --check: FAIL "
                  "(manifest_throughput.tsv does not reproduce byte for "
                  "byte)")
            ok = False
        for sid, body, _desc in texts:
            path = os.path.join(OUT, sid + ".bin")
            if not os.path.isfile(path) or open(path, "rb").read() != body:
                print("gen_throughput_subjects --check: FAIL (%s does not "
                      "reproduce)" % sid)
                ok = False
        if ok:
            print("gen_throughput_subjects --check: OK (%d texts, decode "
                  "gate negative-arm control passed)" % len(texts))
        return 0 if ok else 1
    os.makedirs(OUT, exist_ok=True)
    for sid, body, _desc in texts:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write(_render(texts))
    total = sum(len(b) for _s, b, _d in texts)
    print("gen_throughput_subjects: %d text(s) (%d B total, ~%.2f MB) -> "
          "%s, manifest -> %s (decode gate negative-arm control passed)"
          % (len(texts), total, total / (1024 * 1024), OUT, MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
