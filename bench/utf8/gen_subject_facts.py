#!/usr/bin/env python3
"""gen_subject_facts.py -- `subject_facts.tsv`: per subject, the UTF-8
LEAD-BYTE HISTOGRAM (utf8_set_v1.md 4.2), re-derived and committed so "the
histogram is unlike English" is a FACT rather than a claim.

WHY THIS FILE EXISTS. A subject manifest takes 4 or 5 columns
(`bench/CLAUDE.md`: "the loader takes 4 or 5" -- a sixth is not accepted),
so the per-corpus byte-class breakdown this set's whole objective depends
on cannot live in `manifest.tsv`/`manifest_throughput.tsv` themselves. It
lives here instead, over EVERY subject in both manifests (search-short and
throughput alike), derived from the subject bytes on disk and re-derived
by `--check`, in `bench/bounded/gen_pattern_facts.py`'s own precedent (a
derived FACTS table beside the manifest, never typed by hand).

COLUMNS
  id                the subject id (matches a manifest row)
  source             `search_short` | `throughput`
  len                 the subject's byte length (must equal the manifest's
                     own `len` column -- cross-checked in `--check`)
  n_chars             the DECODED character count (Unicode code points)
  n_ascii             bytes in [0x00, 0x7F] -- 1-byte characters
  n_lead2             LEAD bytes of a 2-byte character ([0xC2, 0xDF])
  n_lead3             LEAD bytes of a 3-byte character ([0xE0, 0xEF])
  n_lead4             LEAD bytes of a 4-byte character ([0xF0, 0xF4])
  n_cont              CONTINUATION bytes ([0x80, 0xBF]) -- every
                     multi-byte character's 2nd/3rd/4th byte
  pct_ascii           n_ascii / len, four decimals
  pct_multibyte       1 - pct_ascii, four decimals
  dominant_lead       the most frequent lead byte in [0x80, 0xFF] as
                     `0xHH`, or `n/a` if the subject is byte-clean ASCII
  avg_bytes_per_char  len / n_chars, four decimals (the encoded-length
                     claim as a number: `asc` reads ~1.0, `cjk` ~3.0)

The classification counts BYTES by their UTF-8 ROLE (lead-vs-continuation,
by value range), which is independent of the corpus's own DECODED
character count -- both are derived here from the same well-formed byte
string (`--check`'s own `_derive` re-decodes it), so a mismatch between
"how many lead bytes of width N" and "how many characters decode" would
itself be a finding, not something this module could silently paper over.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import utf8text as ut  # noqa: E402

OUT = os.path.join(HERE, "subject_facts.tsv")

HEADER = ("id\tsource\tlen\tn_chars\tn_ascii\tn_lead2\tn_lead3\tn_lead4"
          "\tn_cont\tpct_ascii\tpct_multibyte\tdominant_lead"
          "\tavg_bytes_per_char")

_MANIFESTS = (
    ("search_short", os.path.join(HERE, "manifest.tsv"),
     os.path.join(HERE, "subjects")),
    ("throughput", os.path.join(HERE, "manifest_throughput.tsv"),
     os.path.join(HERE, "throughput")),
)


def _read_manifest(path):
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    rows = []
    for ln in lines[1:]:
        if not ln:
            continue
        cols = ln.split("\t")
        rows.append((cols[0], int(cols[1])))  # (id, len)
    return rows


def _classify(body):
    """(n_ascii, n_lead2, n_lead3, n_lead4, n_cont, dominant_lead_or_none)
    over the raw bytes, by UTF-8 role -- independent of decoding."""
    n_ascii = n_lead2 = n_lead3 = n_lead4 = n_cont = 0
    lead_counts = {}
    for b in body:
        if b <= 0x7F:
            n_ascii += 1
        elif 0xC2 <= b <= 0xDF:
            n_lead2 += 1
            lead_counts[b] = lead_counts.get(b, 0) + 1
        elif 0xE0 <= b <= 0xEF:
            n_lead3 += 1
            lead_counts[b] = lead_counts.get(b, 0) + 1
        elif 0xF0 <= b <= 0xF4:
            n_lead4 += 1
            lead_counts[b] = lead_counts.get(b, 0) + 1
        elif 0x80 <= b <= 0xBF:
            n_cont += 1
        else:
            raise ValueError("byte 0x%02x is not valid UTF-8 lead/ASCII/"
                              "continuation -- ill-formed input" % b)
    dominant = None
    if lead_counts:
        dominant = max(lead_counts.items(), key=lambda kv: (kv[1], kv[0]))[0]
    return n_ascii, n_lead2, n_lead3, n_lead4, n_cont, dominant


def _derive_row(sid, source, body):
    ut.decode_gate(body)  # must be well-formed before anything else
    n_chars = len(body.decode("utf-8"))
    n_ascii, n_lead2, n_lead3, n_lead4, n_cont, dominant = _classify(body)
    n = len(body)
    pct_ascii = n_ascii / n if n else 0.0
    pct_multi = 1.0 - pct_ascii
    dom = ("0x%02x" % dominant) if dominant is not None else "n/a"
    avg_bpc = n / n_chars if n_chars else 0.0
    return "%s\t%s\t%d\t%d\t%d\t%d\t%d\t%d\t%d\t%.4f\t%.4f\t%s\t%.4f" % (
        sid, source, n, n_chars, n_ascii, n_lead2, n_lead3, n_lead4, n_cont,
        pct_ascii, pct_multi, dom, avg_bpc)


def build():
    rows = []
    for source, manifest_path, subj_dir in _MANIFESTS:
        for sid, mlen in _read_manifest(manifest_path):
            path = os.path.join(subj_dir, sid + ".bin")
            with open(path, "rb") as f:
                body = f.read()
            assert len(body) == mlen, (
                "subject_facts: %s length %d disagrees with %s's own "
                "manifest row (%d)" % (sid, len(body), manifest_path, mlen))
            rows.append(_derive_row(sid, source, body))
    return rows


def _render(rows):
    return "\n".join([HEADER] + rows) + "\n"


def main():
    check = "--check" in sys.argv
    if not (os.path.isdir(_MANIFESTS[0][2]) and os.path.isfile(
            _MANIFESTS[0][1])):
        print("gen_subject_facts: FAIL (run gen_subjects.py and "
              "gen_throughput_subjects.py first)")
        return 1
    rows = build()
    rendered = _render(rows)
    if check:
        if not os.path.isfile(OUT):
            print("gen_subject_facts --check: FAIL (no subject_facts.tsv "
                  "-- run without --check first)")
            return 1
        with open(OUT, encoding="utf-8") as f:
            committed = f.read()
        if committed != rendered:
            print("gen_subject_facts --check: FAIL (subject_facts.tsv "
                  "does not reproduce byte for byte)")
            return 1
        print("gen_subject_facts --check: OK (%d rows)" % len(rows))
        return 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(rendered)
    print("gen_subject_facts: %d rows -> %s" % (len(rows), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
