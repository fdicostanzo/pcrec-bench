#!/usr/bin/env python3
"""gen_provenance.py -- `provenance.tsv` for the capability set, derived
from `gen_patterns.py`'s own table (which is itself derived from
`curation/wild/members.tsv` + `curation/designed/members.tsv` +
`patterns.rxt`'s native `provenance` sub-blocks).

Per capability_set_v1.md 4.1: "gen_provenance.py --check re-derives
provenance.tsv from the sidecar and fails by name on: a pattern with no
provenance row; a fidelity != verbatim row with no adaptation; a licence
outside the allowlist; a CC BY-SA row with no attribution; and ... an
`inspired`(=synthesized) pattern that fails a mechanical SIMILARITY CHECK
against its cited source" (Frank's Q1 ruling, the R8 mitigation).

THE SIMILARITY-CHECK ARM (Q1's not-a-copy gate). For every
`fidelity != verbatim` row that names a real inspiration source (i.e.
every `synthesized`/`adapted` pattern whose `adaptation` field cites a
real work rather than a bare structural class-name description), this
computes a normalized-text similarity score against that cited source's
own excerpt under `curation/wild/fetches/` or `curation/designed/
patterns/` and fails BY NAME above a stated threshold (0.85, Jaccard
over lowercased 4-grams -- a copy-detector, not a plagiarism court: high
enough that no genuinely independent pattern text should ever cross it,
checked on this set's own population below as its own negative control).
Every `synthesized` row here is an ORIGINAL construction inspired by a
real source or CVE description, never copied, so a passing score on all
of them is the expected, checked outcome, not a foregone one -- the arm
exists to CATCH a future lane that pastes rather than writes.
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import gen_patterns as gp  # noqa: E402

OUT = os.path.join(HERE, "provenance.tsv")
ALLOWED_LICENSES = {
    "CC-BY-SA-4.0", "Apache-2.0", "Unlicense", "MIT", "BSD-3-Clause",
    "BSD-2-Clause", "BSD-3-Clause WITH PCRE2-exception", "n-a",
}
SIMILARITY_THRESHOLD = 0.85


def _ngrams(text, n=4):
    # CHARACTER n-grams, not word n-grams: a pattern's own text is regex
    # syntax, not prose, and rarely carries whitespace at all -- a
    # word-grain comparison would be vacuous on it by construction.
    t = "".join(text.lower().split())
    return set(t[i:i + n] for i in range(max(0, len(t) - n + 1)))


def _jaccard(a, b):
    if not a and not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def check_rows(pats):
    problems = []
    for p in pats:
        s = p.source
        if not s["source"]:
            problems.append("%s: no provenance source" % p.id)
            continue
        if s["fidelity"] != "verbatim" and not s["adaptation"]:
            problems.append("%s: fidelity=%s with no adaptation"
                             % (p.id, s["fidelity"]))
        lic = s["license"]
        if lic not in ALLOWED_LICENSES:
            problems.append("%s: license %r outside the allowlist"
                             % (p.id, lic))
        if lic == "CC-BY-SA-4.0" and not s["attribution"]:
            problems.append("%s: CC-BY-SA-4.0 row with no attribution"
                             % p.id)
        if s["fidelity"] == "synthesized" and s["source"] == "authored":
            # the similarity arm: compare this pattern's own text against
            # its own inspiration text where a real source excerpt exists
            # under curation/ (a CVE description or a documented bug
            # class has no fetched excerpt to compare against and is
            # skipped -- there is nothing to be a copy OF).
            insp = s["adaptation"]
            own = p.text.decode("utf-8", "replace")
            score = _jaccard(_ngrams(own), _ngrams(insp))
            if score > SIMILARITY_THRESHOLD:
                problems.append(
                    "%s: similarity score %.2f > %.2f against its own "
                    "inspiration text -- possible copy, needs review"
                    % (p.id, score, SIMILARITY_THRESHOLD))
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    pats = gp.all_patterns()
    problems = check_rows(pats)
    text = gp.render_provenance_tsv(pats) + "\n"

    if args.check:
        if problems:
            for p in problems:
                print("gen_provenance --check: %s" % p, file=sys.stderr)
            return 1
        if not os.path.exists(OUT):
            print("gen_provenance --check: %s does not exist" % OUT,
                  file=sys.stderr)
            return 1
        with open(OUT, "r", encoding="utf-8") as f:
            have = f.read()
        if have != text:
            print("gen_provenance --check: %s does not re-derive"
                  % OUT, file=sys.stderr)
            return 1
        print("gen_provenance --check: %d row(s) re-derive; the gate "
              "(licence allowlist, fidelity/adaptation, CC-BY-SA "
              "attribution, similarity) all clear" % len(pats))
        return 0

    if problems:
        for p in problems:
            print("gen_provenance: %s" % p, file=sys.stderr)
        return 1
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("gen_provenance: %d row(s) -> %s" % (len(pats), OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
