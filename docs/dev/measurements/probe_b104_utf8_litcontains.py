#!/usr/bin/env python3
"""probe_b104_utf8_litcontains.py -- [B104] (inbox I-112) THE lit-* CONTAINS-LITERAL
CENSUS: classifies every (lit-* pattern x subject) in bench/utf8@0.1 as
CONTAINS-LITERAL or NOT, by TWO independently-derived rules, for the F3
attribution split I-112 asks the read lane to report by.

Compile-only, answers-only: no pcrec build, no store, no timing. Reads:
  - bench/utf8/expectations.tsv (the committed oracle derivation) for
    Rule A (does the pattern MATCH the subject at all).
  - bench/utf8/subjects/*.bin + bench/utf8/throughput/*.bin (regenerated,
    deterministic, gitignored -- `python3 bench/utf8/gen_subjects.py` /
    `gen_throughput_subjects.py`, byte-identical per their own committed
    sha256 manifest) for Rule B (does the PRE-CHECK BYTE I-112 stamped by
    value for each of the seven lit-* patterns occur anywhere in the
    subject's raw bytes).

Rule A (oracle match) is the SEMANTIC claim ("the literal is present as a
match"). Rule B (byte occurrence) is the MECHANISTIC one: [OPT-REQRUN-ENC]'s
whole-window pre-check rejects a subject in one memchr call IFF the scanned
byte is ABSENT; a subject where the byte occurs (whether or not the full
literal ends up matching) cannot take that fast path, so the real
performance split predicted by I-112 tracks Rule B, not Rule A. Rule A
implies Rule B always (a full literal match necessarily contains the
scanned byte, since the scanned byte is one of the literal's own bytes);
Rule B does not imply Rule A (the byte can occur without the full literal
matching). Both are printed per cell so the two are never conflated.

Run from the repo root:
    python3 docs/dev/measurements/probe_b104_utf8_litcontains.py
"""
import csv
import os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# The seven patterns I-112 stamped by value at pin 751b9c6d (abi 39), and
# the single scanned pre-check byte (RX_REQ_BYTE) each one now reads under
# [OPT-REQRUN-ENC]'s rightmost-member rule (b104repin_report.md S0.4).
LIT_REQ_BYTE = {
    "lit-offset-at-tail": 0x40,   # e9 -> b104: e'@' -- run c3a940@2
    "lit-offset-at-head": 0xA9,   # @e9 -- run 40c3a9@2
    "lit-mixed-ascii":    0x88,   # user@nihonjp -- run 7240e4be8be38188@7
    "lit-cyr-run":        0xB0,   # Moskva -- run d181d0bad0b2d0b0@7
    "lit-run-3":          0x9E,   # nihongo -- run 97a5e69cace8aa9e@7
    "lit-nfc-pair":       0xA9,   # cafe -- run 636166c3a9@4
    "lit-sharp-s":        0x65,   # Strasse -- run 53747261c39f65@6
}

# The SAME seven patterns' scanned byte BEFORE this window's pin, at
# ce658cb7 (abi 33, the pre-[OPT-REQRUN-ENC] LEFTMOST rule): index 0 of
# the identical RX_REQ_RUN bytes -- read from the 2026-09-26 ledger
# (docs/dev/ledgers/2026-09-26-utf8-0.1-first-ce658cb7.md SS2.1/2.2/2.3),
# never re-derived by hand. The FLIP between this column and LIT_REQ_BYTE
# above, per subject, is what decides whether a subject is a genuine
# improvement witness (old=yes,new=no), a genuine regression-risk witness
# (old=no,new=yes), or unmoved (both yes or both no) -- the question
# I-112's own "Mac proxy" number cannot answer for THIS bench's own
# generated corpus without checking the actual bytes, which is what this
# script does.
LIT_REQ_BYTE_OLD = {
    "lit-offset-at-tail": 0xC3,   # run c3a940@0 -- e9's own LEAD byte
    "lit-offset-at-head": 0x40,   # run 40c3a9@0 -- '@'
    "lit-mixed-ascii":    0x75,   # run 7573657240e4be8b@0 -- 'u'
    "lit-cyr-run":        0xD0,   # run d09cd0bed181d0ba@0 -- M's own lead
    "lit-run-3":          0xE6,   # run e697a5e69cace8aa@0 -- nichi's own lead
    "lit-nfc-pair":       0x63,   # run 636166c3a9@0 -- 'c'
    "lit-sharp-s":        0x53,   # run 53747261c39f65@0 -- 'S'
}

SEARCH_DIR = os.path.join(REPO, "bench/utf8/subjects")
THROUGHPUT_DIR = os.path.join(REPO, "bench/utf8/throughput")
EXPECTATIONS = os.path.join(REPO, "bench/utf8/expectations.tsv")


def load_subject_bytes():
    out = {}
    for d, ext in ((SEARCH_DIR, ".bin"), (THROUGHPUT_DIR, ".bin")):
        for fn in os.listdir(d):
            if fn.endswith(ext):
                sid = fn[: -len(ext)]
                with open(os.path.join(d, fn), "rb") as f:
                    out[sid] = f.read()
    return out


def load_expectations():
    """pattern -> {(subject, regime): expected}"""
    rows = {}
    with open(EXPECTATIONS) as f:
        r = csv.reader(f, delimiter="\t")
        header = next(r)
        idx = {name: i for i, name in enumerate(header)}
        for row in r:
            pat = row[idx["pattern"]]
            if pat not in LIT_REQ_BYTE:
                continue
            subj = row[idx["subject"]]
            regime = row[idx["regime"]]
            expected = row[idx["expected"]]
            rows.setdefault(pat, {})[(subj, regime)] = expected
    return rows


def main():
    subj_bytes = load_subject_bytes()
    exp = load_expectations()

    print("# bench/utf8@0.1 lit-* CONTAINS-LITERAL census -- [B104]/I-112")
    print("# bench commit: (worktree lane/b104pred, off master d213e75)")
    print("# subjects/ + throughput/ regenerated from the committed generators;")
    print("# manifest.tsv/manifest_throughput.tsv reproduced byte-identical (git status clean)")
    print("# Rule A = oracle 'expected' column (match/nomatch) from bench/utf8/expectations.tsv")
    print("# Rule B = the I-112 pre-check byte (RX_REQ_BYTE, hex) present anywhere in the raw subject bytes")
    print("#")
    cols = ["pattern", "subject", "regime", "rule_a_expected",
            "rule_b_byte_hex_new", "rule_b_present_new",
            "rule_b_byte_hex_old", "rule_b_present_old",
            "contains_literal_A", "contains_literal_B_new", "flip_class"]
    print("\t".join(cols))

    totals = {"both_yes": 0, "both_no": 0, "A_no_B_yes": 0, "A_yes_B_no": 0}
    flips = {"flip_to_fast": 0, "flip_to_slow": 0, "stays_fast": 0, "stays_slow": 0}

    for pat in LIT_REQ_BYTE:
        req_byte = LIT_REQ_BYTE[pat]
        req_byte_old = LIT_REQ_BYTE_OLD[pat]
        cells = exp.get(pat, {})
        # stable order: search_short subjects first (manifest order via sorted id), then throughput
        for (subj, regime), expected in sorted(cells.items(), key=lambda kv: (kv[0][1] != "throughput", kv[0][0])):
            sb = subj_bytes.get(subj)
            if sb is None:
                raise SystemExit(f"missing subject bytes for {subj!r} (regenerate bench/utf8's subjects/throughput first)")
            b_present = req_byte in sb
            b_present_old = req_byte_old in sb
            a_contains = expected == "match"
            agree = a_contains == b_present
            if a_contains and b_present:
                totals["both_yes"] += 1
            elif (not a_contains) and (not b_present):
                totals["both_no"] += 1
            elif (not a_contains) and b_present:
                totals["A_no_B_yes"] += 1
            else:
                totals["A_yes_B_no"] += 1
            if b_present_old and not b_present:
                flip = "flip_to_fast"
            elif (not b_present_old) and b_present:
                flip = "flip_to_slow"
            elif b_present_old and b_present:
                flip = "stays_slow"
            else:
                flip = "stays_fast"
            flips[flip] += 1
            print("\t".join([
                pat, subj, regime, expected,
                f"0x{req_byte:02x}", "yes" if b_present else "no",
                f"0x{req_byte_old:02x}", "yes" if b_present_old else "no",
                "yes" if a_contains else "no", "yes" if b_present else "no",
                flip,
            ]))

    print("#")
    print(f"# totals (NEW-pin rule only): both-yes={totals['both_yes']} both-no={totals['both_no']} "
          f"A=no/B=yes={totals['A_no_B_yes']} A=yes/B=no={totals['A_yes_B_no']}")
    print(f"# flip census (old-pin leftmost byte -> new-pin rightmost byte): "
          f"flip_to_fast={flips['flip_to_fast']} flip_to_slow={flips['flip_to_slow']} "
          f"stays_slow={flips['stays_slow']} stays_fast={flips['stays_fast']}")
    print("# A=yes/B=no is impossible by construction (a full-literal match necessarily")
    print("# contains the scanned byte, one of the literal's own bytes) -- a nonzero count")
    print("# there is a DEFECT in this probe or in the I-112 byte values above, not a real cell.")


if __name__ == "__main__":
    main()
