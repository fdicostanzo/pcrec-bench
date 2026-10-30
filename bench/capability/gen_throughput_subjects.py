#!/usr/bin/env python3
"""gen_throughput_subjects.py -- the capability set's three throughput
texts ([B125] 0.2 appends eight, [B123] 0.3 appends six `t-hyb-*` MATCH
subjects, 1-64 KiB, [B172] 0.4 appends two `t-qs-*` query-string subjects): `throughput/` (gitignored) + `manifest_throughput.tsv`
(committed), in `bench/syntax/gen_throughput_subjects.py`'s shape:
`captext.text()` at three sizes and three seeds, a SIZE SWEEP at fixed
"grammar", not a density cross (capability_set_v1.md 3.5).

SAFETY NOTE for family 10 (`redos-nested`): every pattern in that family
is anchored at `^` (checked in NOTES.md's authoring review), so a
`find_all` scan over these texts attempts a real match only at offset 0
-- every later scan position fails in O(1) because `^` (no MULTILINE
anywhere in this set) cannot match past the subject's start. The
generated grammar also never emits a long uniform run of one character
class (captext's four line kinds all interleave words/punctuation/
digits), so no accidental adversarial prefix can arise. `--check`'s own
run empirically re-times every redos pattern against all three texts
(the `_redos_safety_check` below) as a belt-and-braces control beyond
the structural argument.
"""
import hashlib
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import captext as ct  # noqa: E402

OUT = os.path.join(HERE, "throughput")
MANIFEST = os.path.join(HERE, "manifest_throughput.tsv")

SIZES = (
    ("t-64k", 64 * 1024, 0xC0FFEE1),
    ("t-256k", 256 * 1024, 0xC0FFEE2),
    ("t-1m", 1024 * 1024, 0xC0FFEE3),
)

# [B125] capability@0.2: the subjects APPENDED after the three 0.1 texts
# (manifest rows 4..; the 0.1 rows and files are untouched, asserted by
# main()). All are > short_search_max_bytes, so they enter the THROUGHPUT
# regime only -- and, because the throughput regime is "every pattern x every
# throughput subject", every pattern of the set is run on each of them.
#   (id, generator-call, description)
_PROSE_BYTES = 1024 * 1024 - 64
_TAILS = (
    ("t-tail-digits-1m", b"total 20250614",
     "throughput/[B125] ~1 MiB generated prose (seed 0xC0FFEE21), last line "
     "'total 20250614': the tail `\\d+$` and `\\w+\\z` MATCH, `\\s+$`, "
     "`[a-z]+\\.txt$` and `.*\\.txt$` do not"),
    ("t-tail-txt-1m", b"saved to report.txt",
     "throughput/[B125] the SAME prose, last line 'saved to report.txt': "
     "`[a-z]+\\.txt$`, `.*\\.txt$` and `\\w+\\z` ('txt') MATCH, `\\d+$` and "
     "`\\s+$` do not"),
    ("t-tail-space-1m", b"end of file   ",
     "throughput/[B125] the SAME prose, last line 'end of file' + three "
     "spaces: `\\s+$` MATCHES, `\\d+$`, `\\w+\\z`, `[a-z]+\\.txt$` and "
     "`.*\\.txt$` do not"),
)
_LONG = 60 * 1024
_NEAR = 16 * 1024      # the near-misses: a 16 KiB prefix of the matching run + 1 byte


def extra_subjects():
    """-> [(id, bytes, description)] in manifest order. The long
    ReDoS-family subjects pair a 60 KiB MATCHING run with a 16 KiB NEAR-MISS (a
    prefix of the SAME run plus one terminating non-member byte), for `^(([a-z]+)*)+$` and
    `^(\\s+)*$`; the mixed-run subject is ~4 KB of interleaved short runs;
    the three tail subjects share one ~1 MiB prose body and differ only in
    their last line."""
    letters = ct.letter_run(_LONG, 0xC0FFEE11)
    spaces = ct.ws_run(_LONG, 0xC0FFEE12)
    out = [
        ("t-evil-match-60k", letters,
         "throughput/[B125] 60 KiB of random [a-z], nothing else: the "
         "long MATCHING subject of `^(([a-z]+)*)+$` (whole subject; the "
         "backtracker's first greedy path)"),
        ("t-evil-nearmiss-16k", letters[:_NEAR] + b"!",
         "throughput/[B125] the first 16 KiB of t-evil-match-60k + one '!': the "
         "long NEAR-MISS (the same run plus one terminating non-member byte) "
         "-- exponential for a backtracker; the oracle's structural-alphabet "
         "rule answers it"),
        ("t-trim-match-60k", spaces,
         "throughput/[B125] 60 KiB of mixed \\s bytes (space/tab/LF/CR/FF/VT), "
         "ending in a space: the long MATCHING subject of `^(\\s+)*$`"),
        ("t-trim-nearmiss-16k", spaces[:_NEAR] + b"x",
         "throughput/[B125] the first 16 KiB of t-trim-match-60k + one 'x': the "
         "long NEAR-MISS"),
        ("t-mixed-runs-4k", ct.mixed_runs(4096, 0xC0FFEE13),
         "throughput/[B125] 4096 B of interleaved SHORT runs (letters, "
         "digits, hex, signed decimals, separators, standalone 8-hex ids), "
         "ending in a letter: the real-text shape no pure-run subject has"),
    ]
    for sid, tail, desc in _TAILS:
        out.append((sid, ct.prose(_PROSE_BYTES, 0xC0FFEE21, tail), desc))
    return out


# [B123] capability@0.3: the capture-forced-hybrid MATCH subjects, APPENDED after
# the eleven 0.1/0.2 rows (which are untouched, asserted by main()). All are
# > short_search_max_bytes, so THROUGHPUT only; 1 KiB .. 64 KiB (pcrec I-125 Q10).
# Which of the 17 `RX_VM_PREFILTER "hybrid"` + `RX_ENGINE_WHY "capture group"`
# patterns each one is the matching subject of is in each description and in
# NOTES.md's 0.3 section.
_HYB_EMBED = (
    ("t-hyb-embed-1k", 1024, 0xC0FFEE31),
    ("t-hyb-embed-8k", 8192, 0xC0FFEE32),
    ("t-hyb-embed-64k", 65536, 0xC0FFEE33),
)
_HYB_EMBED_WHO = (
    "a ladder rung of one log/config/JSON grammar with planted instances "
    "(an address first line; a JSON line, a syslog line, an AWS key id, a "
    "GitHub PAT, a Slack webhook URL and a username/password pair in the "
    "first seven lines, then one line in four a plant): find-all MATCHES "
    "codegrammar-flat, codegrammar-xflag, wild-logparse-syslogbase-expanded, "
    "wild-secrets-aws-access-key-id, -github-pat, -slack-webhook-url, "
    "-username-password-pair, wild-semdiv-empty-alt-repeat-pcre2 (every "
    "digit) and, once at offset 0, email-nested-plus")


def hyb_subjects():
    """-> [(id, bytes, description)] in manifest order: the embed ladder, then
    the three whole-subject shapes."""
    out = []
    for sid, n, seed in _HYB_EMBED:
        out.append((sid, ct.hyb_embed(n, seed),
                    "throughput/[B123] %d B, seed 0x%X: %s"
                    % (n, seed, _HYB_EMBED_WHO)))
    out.append((
        "t-hyb-logline-16k", ct.hyb_logline(16384, 0xC0FFEE34),
        "throughput/[B123] 16384 B, ONE line, no newline, `kern.err: ` then "
        "prose words: the whole subject is the match of logparse-atomic and "
        "logparse-atomic-removed (a long syslog message)"))
    out.append((
        "t-hyb-datepath-16k", ct.hyb_datepath(16384, 0xC0FFEE35),
        "throughput/[B123] 16384 B of digit groups closed by `/` (or, one in "
        "four, `-`), first group `2025/`, ending in `/`: the whole subject is "
        "the match of date-nested-plus"))
    out.append((
        "t-hyb-digits-4k", ct.hyb_digits(4096, 0xC0FFEE36),
        "throughput/[B123] 4096 random decimal digits: the whole subject is "
        "the match of numeric-id-nested-plus and phone-list-nested-plus, and "
        "email-nested-plus's would-be catastrophic near-miss (the digits are in "
        "its class and there is no '@': PCRE2's required-code-unit check "
        "dismisses it at once, an engine without one would backtrack)"))
    return out


_0_2_SHA256 = {
    "t-evil-match-60k": "7e997b935b2b6fc8914f888a146f90163a59ee7e9a356b22880999d4c4427ee1",
    "t-evil-nearmiss-16k": "7783c01caab83dfdc8bf4859f2dd1bab0e2bbd5fb6d3d12278b8c064fb2728af",
    "t-trim-match-60k": "eb6cb8751e37a9cb75812a3cb05b1a939624c1e9e6ef3f0716bb1e0739f3e80a",
    "t-trim-nearmiss-16k": "41783dc6c35a4a0670ac026a91cf8c9569b5d479e9d0436613d0fa0e17fbcd47",
    "t-mixed-runs-4k": "04db4aaa9e01339995fb7acc0dfdb216042f5913b41e938b368cbd75f411b7d5",
    "t-tail-digits-1m": "06a2c18097ee1b62860a53250be52e50a9be2b284e0e67b4afae3ff8c0a3dbd2",
    "t-tail-txt-1m": "e1fc06ff899dffd8fad1239d20ca32c72f2708881c311d27cc4c9fbbe19fc057",
    "t-tail-space-1m": "9d6c19081540d136581fc08ba781a0d5062abf696693c4d5ace1142b7254b3b1",
}


# [B172] capability@0.4: the URL query-string subjects (pcrec I-172), APPENDED
# after the seventeen 0.1-0.3 rows (asserted by main()). Throughput only. The
# MATCHING subject (3.5-3.8 % of lines carry a duplicate key) is ~1 MiB; the
# NEAR-MISS (no duplicate key anywhere, keys sharing prefixes) is 256 KiB
# because a failing `dup-param-detect` start scans to the end of the subject, so
# its cost is quadratic in size (NOTES.md, 0.4).
_QS = (
    ("t-qs-1m", 1024 * 1024, 0xC0FFEE41, 35000, False),
    ("t-qs-nearmiss-256k", 256 * 1024, 0xC0FFEE42, 0, True),
)


def qs_subjects():
    """-> [(id, bytes, description, stats)] in manifest order."""
    out = []
    for sid, n, seed, ppm, twist in _QS:
        body, st = ct.qs_text(n, seed, ppm, twist)
        if ppm:
            desc = (
                "throughput/[B172] %d B target (%d lines), seed 0x%X: URL "
                "query-string parts, one `k=v&k=v...` per line, every key text "
                "unique in the subject except %d planted duplicate keys (%.1f %% "
                "of lines carry the second occurrence; same line, next line, "
                "2-40 lines on, and 300-3000 lines on), a few lines of up to "
                "~%d params: the matching subject of dup-param-detect"
                % (n, st["lines"], seed, st["dup_keys"],
                   100.0 * st["dup_lines"] / st["lines"], st["max_params"]))
        else:
            desc = (
                "throughput/[B172] %d B target (%d lines), seed 0x%X: the "
                "same query-string grammar with NO duplicate key anywhere and "
                "keys sharing prefixes (`id`, `idx`, `ids`, `id_2`, `id_k3f`): "
                "the NEAR-MISS of dup-param-detect, every start scans to the "
                "end of the subject and fails" % (n, st["lines"], seed))
        out.append((sid, body, desc, st))
    return out


_0_3_SHA256 = {
    "t-hyb-embed-1k": "cac80cd7907525851d555bee0b87a9d71d84450df6870588d8bfed3a751a9d93",
    "t-hyb-embed-8k": "ffda00a030093eed090bdc2e7d16a164b4c9d96f0058d6727745f6ef40216477",
    "t-hyb-embed-64k": "dbebe4c6a0ae5d10d0453b7afd828306fcebf900f1bef23f07d8e5ab93115fe8",
    "t-hyb-logline-16k": "4bc9fc30a5db511207ecfd20e438dc8419046074e5e89df15b11a01a814074f7",
    "t-hyb-datepath-16k": "2177ff71a237fb05ed6a9fade5013f361cefcd4258be4909efbdb782a878dfeb",
    "t-hyb-digits-4k": "100d062ce158832630a2084cb999e5f8be002a947aaff04158739c34e9382452",
}


_REDOS_PATTERNS = (
    r"^([a-zA-Z0-9._%+-]+)+@",
    r"^(\s+)*$",
    r"^(([a-z]+)*)+$",
    r"^(\d+)+$",
    r"^(\d+\s*)+$",
    r"^(([0-9]+[-/])+)+$",
)


def _redos_safety_check(texts):
    sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
    from pcrecbench import oracle_pcre2 as oracle
    for name, body in texts:
        for pat in _REDOS_PATTERNS:
            rx = oracle.compile(pat)
            t0 = time.time()
            try:
                rx.find_all(body)
            except oracle.Pcre2Error:
                pass  # a bounded give-up is fine; a HANG is what we guard
            dt = time.time() - t0
            if dt > 2.0:
                raise AssertionError(
                    "redos safety check: %r over %s took %.2fs (> 2s "
                    "guard) -- family 10's ^-anchor argument may not "
                    "hold for this text" % (pat, name, dt))


# The 0.1 rows, byte for byte: capability@0.2 EXTENDS the manifest, it never
# re-draws it. A change to captext.text() that moved a 0.1 text would fail
# here before it reached a manifest.
_0_1_SHA256 = {
    "t-64k": "d2e4f134473cc40a9a4e7df7a30e0efa11f566d96ee990c62cd663a2439c8524",
    "t-256k": "3cf7b248873da164518b74e039cc2380f39e233b2899716c82c8eb4b7b49b5a7",
    "t-1m": "ccbdf7eb97f15776a68b8bbb9d6387870cd01d4796207fb20032958caf9754ee",
}


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    texts = []
    for sid, nbytes, seed in SIZES:
        body = ct.text(nbytes, seed)
        texts.append((sid, body))
        assert hashlib.sha256(body).hexdigest() == _0_1_SHA256[sid], (
            "capability@0.2 moved a 0.1 throughput text: %s" % sid)
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(),
            "throughput/mixed log+http+source+prose grammar, seed 0x%x"
            % seed, ct.periodic_field(body)))
    for sid, body, desc in extra_subjects():
        assert len(body) > 512, sid       # throughput-only, by size
        assert hashlib.sha256(body).hexdigest() == _0_2_SHA256[sid], (
            "capability@0.3 moved a 0.2 throughput text: %s" % sid)
        texts.append((sid, body))
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    for sid, body, desc in hyb_subjects():
        assert 1024 <= len(body) <= 65536, sid     # I-125 Q10's band
        assert hashlib.sha256(body).hexdigest() == _0_3_SHA256[sid], (
            "capability@0.4 moved a 0.3 throughput text: %s" % sid)
        texts.append((sid, body))
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    for sid, body, desc, st in qs_subjects():
        assert len(body) > 512, sid
        texts.append((sid, body))
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
        print("  %s: %s" % (sid, st))
    _redos_safety_check(texts)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    print("gen_throughput_subjects: %d text(s) -> %s, manifest -> %s "
          "(redos safety check: OK)" % (len(texts), OUT, MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
