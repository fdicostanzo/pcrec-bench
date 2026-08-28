#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the email sub-bench's 1 MB throughput subjects.

`t-a-valid-addrs`, `t-b-no-at`, `t-c-long-atom-run` are COPIED from pcrec
docs/design/subroutines_measurements/email_specimen/gen_throughput_subjects.py
(read-only origin; see CLAUDE.md) verbatim -- byte-identical to the ones
pcrec's srEmail lane measured. What changed for those three is only the
output shape: schema-slug ids, and a committed `manifest_throughput.tsv`
with a sha256 column.

1 MB is a KNOWN-SMALLER departure from pcrec's own 8-64 MB convention and is
inherited deliberately, not chosen: requirements 3 defers the standard size to
OD-B10 (spread at 1 MB vs 8 MB, measured on this box, at [B4]).

`t-d-prose-sparse-addrs` and `t-e-prose-no-at` are NEW ([B17], inbox I-10):
pcrecdev1 measured that all three original subjects are PERIODIC --
`t-a-valid-addrs` period 26 B (the repeated address token), `t-b-no-at`
period 55 B (the repeated sentence), `t-c-long-atom-run` period 1 B (one
repeated byte) -- which makes the DFA loop's one data-dependent branch
perfectly history-predictable and flatters any per-byte number measured
only on them. `periodic.py`'s `smallest_period` confirms this mechanically
below rather than assuming it (`--check` fails loudly if a re-derivation
ever disagrees with I-10's own figures). t-d and t-e are generated PROSE:
a word is drawn per token from a fixed vocabulary of VARYING length with a
seeded `random.Random(GEN_SEED)` (no fixed period by construction), broken
into sentences with terminal punctuation and occasional line breaks. t-d
inserts a valid email address, drawn from a small varied list, roughly
every WORD_GAP_MIN..WORD_GAP_MAX words; t-e runs the identical generator
with insertion turned off, so it is prose-shaped but contains no '@'
anywhere -- the two are the same text-generation process, differing only
in whether the address-insertion step ever fires. KEEP the original three:
they isolate the steady-state loop cost (I-10's own words), which is what
[OPT-3] STEP 1/STEP 2 measure; t-d/t-e ADD the non-periodic case beside
them, they do not replace anything.

GEN_SEED is fixed and recorded here (this docstring) and in each new
subject's manifest description, per I-10's "record the generator + seed in
the sidecar" ask -- the sidecar itself (`subbench.toml`) points at this
file as `throughput_generator`, so recording the seed HERE is recording it
in the thing the sidecar names.

WORD_GAP_MIN/MAX (200/400 words) is I-10's own figure, taken literally.
With this vocabulary's average word length, that yields addr_count in the
LOW HUNDREDS per MB, not literally the "few thousand" some scratch
discussion mentioned -- reported as measured (see NOTES.md), not inflated
to fit: 200-400 words between addresses over ~5.5 bytes/word (this
vocabulary's average, punctuation included) is roughly 180-190k words per
MB, so a few hundred insertions is what that gap actually produces.

Deterministic: no randomness beyond `random.Random(GEN_SEED)` (a fixed,
recorded seed), no clock, no environment.
"""
import hashlib
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

sys.path.insert(0, HERE)
from periodic import periodic_field  # noqa: E402

TARGET = 1024 * 1024

# [B17] / I-10: the fixed seed for the two new prose subjects. Recorded here
# (the generator the sidecar names) and repeated in each subject's manifest
# description.
GEN_SEED = 20260828

# A vocabulary of deliberately VARIED word lengths (1..11 bytes) -- ordinary
# English words, not a rotating small set, so there is no short cycle for
# `random.choice` to fall into. Order is fixed (a plain list); randomness
# comes only from `GEN_SEED`.
VOCAB = [
    "a", "an", "the", "of", "to", "in", "on", "at", "by", "for", "and",
    "or", "but", "so", "if", "is", "are", "was", "were", "be", "been",
    "has", "have", "had", "not", "no", "yes", "it", "its", "he", "she",
    "they", "we", "you", "who", "what", "when", "where", "why", "how",
    "this", "that", "these", "those", "here", "there", "then", "than",
    "with", "from", "into", "over", "under", "after", "before", "again",
    "system", "process", "record", "report", "server", "client", "engine",
    "vendor", "invoice", "account", "customer", "project", "release",
    "version", "update", "review", "ticket", "budget", "meeting", "schedule",
    "quarter", "region", "office", "manager", "director", "assistant",
    "contract", "shipment", "delivery", "warehouse", "inventory",
    "supplier", "purchase", "payment", "balance", "transfer", "deposit",
    "withdrawal", "statement", "summary", "overview", "analysis", "metric",
    "dashboard", "pipeline", "workflow", "approval", "escalation", "incident",
    "outage", "latency", "throughput", "capacity", "cluster", "database",
    "network", "gateway", "endpoint", "protocol", "package", "module",
    "library", "function", "variable", "constant", "iterator", "generator",
    "sequence", "matrix", "vector", "graph", "tree", "queue", "stack",
    "buffer", "cache", "index", "table", "column", "row", "field", "key",
    "value", "token", "stream", "channel", "signal", "sensor", "actuator",
    "controller", "regulator", "monitor", "alarm", "threshold", "baseline",
    "sample", "trial", "batch", "cycle", "phase", "stage", "milestone",
    "deadline", "timeline", "calendar", "agenda", "minutes", "notes",
    "draft", "revision", "edition", "chapter", "section", "paragraph",
    "sentence", "clause", "phrase", "syllable", "letter", "symbol",
    "quarterly", "annual", "monthly", "weekly", "daily", "hourly",
    "north", "south", "east", "west", "upper", "lower", "inner", "outer",
    "primary", "secondary", "tertiary", "final", "initial", "interim",
    "pending", "approved", "rejected", "closed", "open", "active", "idle",
    "urgent", "routine", "critical", "minor", "major", "trivial", "severe",
]

# A small varied list of VALID dot-atom addresses (the same forms
# gen_subjects.py's "valid dot-atom ..." entries use, oracle-verified
# elsewhere in this sub-bench): different local-part and domain shapes and
# lengths, so t-d's inserted addresses are not themselves a fixed-length
# repeating token.
VALID_ADDRS = [
    b"user@example.com",
    b"a.b.c@sub.example.org",
    b"jane.doe42@mail-server.net",
    b"contact.info@my-company.co",
    b"test.user99@sub.domain.example.com",
    b"admin@x-y-z.org",
    b"sales.team@corp.example.net",
    b"first.last@department.example.edu",
]

PUNCT = [b".", b".", b".", b"?", b"!"]  # weighted toward '.'

WORD_GAP_MIN, WORD_GAP_MAX = 200, 400   # I-10: "roughly every 200-400 words"
SENT_MIN, SENT_MAX = 6, 14              # words per generated sentence

SUBJECTS = []


def build_prose(target_bytes, seed, insert_addrs):
    """The shared generator for t-d and t-e. Returns (bytes, addr_count).

    Builds whole tokens only -- never truncates a word or an address mid-
    way -- so the exact byte count is reached by padding with a filler byte
    guaranteed not to be '@' (`x`), never by cutting a token. That also
    makes `addr_count` exact: it is the number of address tokens actually
    appended, not an estimate."""
    rng = random.Random(seed)
    out = bytearray()
    addr_count = 0
    words_since_addr = 0
    next_gap = rng.randint(WORD_GAP_MIN, WORD_GAP_MAX)
    sentence_words = 0
    sentence_len = rng.randint(SENT_MIN, SENT_MAX)

    while True:
        word = rng.choice(VOCAB).encode("ascii")
        piece = word + b" "
        if len(out) + len(piece) > target_bytes:
            break
        out += piece
        words_since_addr += 1
        sentence_words += 1

        if sentence_words >= sentence_len:
            punct = rng.choice(PUNCT)
            sep = b"\n" if rng.random() < 0.12 else b" "
            # replace the trailing space just written with punct + sep
            out = out[:-1] + punct + sep
            sentence_words = 0
            sentence_len = rng.randint(SENT_MIN, SENT_MAX)

        if insert_addrs and words_since_addr >= next_gap:
            addr = rng.choice(VALID_ADDRS)
            piece2 = addr + b" "
            if len(out) + len(piece2) > target_bytes:
                break
            out += piece2
            addr_count += 1
            words_since_addr = 0
            next_gap = rng.randint(WORD_GAP_MIN, WORD_GAP_MAX)

    remainder = target_bytes - len(out)
    if remainder > 0:
        # 'x' -- ASCII, never '@', never a token boundary that could merge
        # with an atom-class run; always preceded by whitespace.
        out += b"x" * remainder
    assert len(out) == target_bytes, \
        "build_prose: %d bytes, wanted %d" % (len(out), target_bytes)
    return bytes(out), addr_count


def build():
    # (a) valid addresses separated by spaces
    addr = b"user.name@sub.example.com "
    SUBJECTS.append(("t-a-valid-addrs",
                     "1 MB of valid dot-atom addresses separated by spaces",
                     (addr * (TARGET // len(addr) + 1))[:TARGET]))

    # (b) no '@' at all
    line = b"the quick brown fox jumps over the lazy dog 1234567890 "
    SUBJECTS.append(("t-b-no-at",
                     "1 MB of prose with no '@' anywhere (the prefilter case)",
                     (line * (TARGET // len(line) + 1))[:TARGET]))

    # (c) one long atom run (no @, no dots, no spaces -- pure atom-class bytes)
    SUBJECTS.append(("t-c-long-atom-run",
                     "1 MB of 'a' -- one unbroken atom-class run, no '@'",
                     b"a" * TARGET))

    # (d) [B17]/I-10: generated prose, sparse addresses -- non-periodic by
    # construction (a seeded PRNG choosing among varied-length words).
    d_bytes, d_addr_count = build_prose(TARGET, GEN_SEED, insert_addrs=True)
    assert d_bytes.count(b"@") == d_addr_count, (
        "t-d: %d '@' byte(s) but %d address token(s) were inserted -- an "
        "'@' appeared somewhere other than an inserted address"
        % (d_bytes.count(b"@"), d_addr_count))
    assert d_addr_count > 0, "t-d: no addresses were inserted at all"
    SUBJECTS.append(("t-d-prose-sparse-addrs",
                     "1 MB of generated prose (seed %d, vocabulary of %d "
                     "varied-length words), a valid dot-atom address "
                     "inserted every %d-%d words (%d addresses total)"
                     % (GEN_SEED, len(VOCAB), WORD_GAP_MIN, WORD_GAP_MAX,
                        d_addr_count),
                     d_bytes))

    # (e) [B17]/I-10: the same generator, no '@' anywhere -- the failing
    # subject: every byte scanned, no match.
    e_bytes, e_addr_count = build_prose(TARGET, GEN_SEED, insert_addrs=False)
    assert e_addr_count == 0 and e_bytes.count(b"@") == 0, (
        "t-e: expected zero '@' bytes, found %d (addr_count=%d)"
        % (e_bytes.count(b"@"), e_addr_count))
    SUBJECTS.append(("t-e-prose-no-at",
                     "1 MB of generated prose (seed %d, vocabulary of %d "
                     "varied-length words), the same generator as "
                     "t-d-prose-sparse-addrs with address insertion off -- "
                     "no '@' anywhere"
                     % (GEN_SEED, len(VOCAB)),
                     e_bytes))


def main():
    build()
    os.makedirs(OUT, exist_ok=True)
    lines = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, buf in SUBJECTS:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(buf)
        lines.append("%s\t%d\t%s\t%s\t%s"
                     % (sid, len(buf), hashlib.sha256(buf).hexdigest(), desc,
                        periodic_field(buf)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(lines) + "\n")
    print("gen_throughput_subjects: %d subjects -> %s, manifest -> %s"
          % (len(SUBJECTS), OUT, MANIFEST))


if __name__ == "__main__":
    main()
