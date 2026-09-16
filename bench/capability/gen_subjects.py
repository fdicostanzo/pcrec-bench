#!/usr/bin/env python3
"""gen_subjects.py -- the capability set's short subjects: `subjects/`
(gitignored) + `manifest.tsv` (committed).

TYPED, not drawn, per capability_set_v1.md 3.4: each subject is at least
one pattern's designed HIT and, where a family has a semantic or
capability edge, another pattern's designed near-miss or MISS. Unlike
`bench/syntax` (one small "cat" vocabulary every pattern shares), this
set's patterns are real, heterogeneous shapes, so subjects are grouped by
FAMILY rather than typed against one shared body -- the census's R3/R4
outlier rules (spelling groups, one shared body) do not transfer, exactly
as NOTES.md's own outlier rule states.

Every subject's ACTUAL match/no-match answer is derived by the libpcre2
oracle in `gen_expectations.py`, never hand-verified here -- this module
only states the INTENT each subject was typed for (the description
column), the same discipline `bench/syntax/gen_subjects.py` uses.

Three subjects (`nu-high-byte`, `nu-mojibake`, `nu-lead-no-cont`) carry
RAW NON-UTF-8 BYTES for family 12 (`binary-nonutf8`) -- legitimate here
because subjects live as raw `.bin` files, never as TSV cells.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))

import captext as ct  # noqa: E402

OUT = os.path.join(HERE, "subjects")
MANIFEST = os.path.join(HERE, "manifest.tsv")
MAX_LINE = 512

# (id, description, bytes)
SUBJECTS = (
    # -- wild-validator (family 1): email/ipv4/us-zip/uuid + two near-miss
    # twins (uuid, ipv4). The ipv4 twin is answer-IDENTICAL to the OWASP
    # import on every subject here (both bound each octet 0-255) -- a
    # finding NOTES.md states rather than a subject-design gap (R1: "if
    # they agree everywhere, that IS the finding").
    ("v-email", "field/hit a plausible email address: the OWASP validator "
     "and every real mail-address consumer's common case",
     b"user.name+tag@example.co"),
    ("v-ipv4", "field/hit a valid dotted-quad: OWASP's IPv4 validator and "
     "its designed twin (answer-identical -- both octet-range-bound)",
     b"192.168.1.1"),
    ("v-ipv4-oor", "field/miss an out-of-range octet: both the OWASP "
     "IPv4 validator and its twin correctly reject it (the naive "
     "\\d{1,3}-per-octet gotcha the twin was modeled on does NOT apply "
     "to either -- see v-ipv4's own description)", b"999.1.1.1"),
    ("v-us-zip", "field/hit a plain 5-digit ZIP", b"90210"),
    ("v-us-zip-plus4", "field/hit the ZIP+4 extended form", b"90210-1234"),
    ("v-uuid-valid", "field/hit a version-1/variant-8 UUID: the grok "
     "class-heavy import AND its RFC-4122-strict twin both accept it",
     b"a1b2c3d4-e5f6-1234-8abc-1234567890ab"),
    ("v-uuid-badnibble", "field/edge a UUID-shaped string with an "
     "out-of-range version nibble ('0') and variant nibble ('1'): the "
     "grok import (pure hex-range classes) still HITS; the RFC-4122-"
     "strict twin MISSES -- the pair's whole point",
     b"a1b2c3d4-e5f6-0234-1abc-1234567890ab"),

    # -- wild-logparse (family 2): base10num/quotedstring (+ noatomic
    # controls), winpath, syslogbase, + two reassigned near-miss twins
    # (base10num, winpath -- see NOTES.md's twin-pairing reconciliation)
    # and the atomic/non-atomic authored pair.
    ("lp-num-neg-dec", "field/hit a signed decimal: grok BASE10NUM "
     "(atomic and non-atomic) and the near-miss twin all accept it",
     b"-123.45"),
    ("lp-num-leadzero", "field/edge a leading-zero integer: grok's "
     "BASE10NUM (unanchored SEARCH, no leading-zero rule) still HITS; "
     "the near-miss twin (anchored, JSON-strict '0'|'[1-9]\\d*') MISSES",
     b"0123"),
    ("lp-quoted", "field/hit a double-quoted string, no escapes",
     b'"quoted text"'),
    ("lp-quoted-escaped", "field/edge a double-quoted string with an "
     "escaped quote inside: the atomic QUOTEDSTRING's own "
     "`\\\\.|[^\\\\\"]+` alternation", b'"say \\"hi\\" now"'),
    ("lp-winpath", "field/hit a Windows path: grok WINPATH and its "
     "near-miss twin both accept it (no reserved character)",
     b"C:\\Users\\test\\file.txt"),
    ("lp-winpath-reserved", "field/edge a Windows path with a reserved "
     "character ('<') in a segment: grok WINPATH (permissive "
     "`[^\\\\?*]*`) still HITS; the near-miss twin (rejects all nine "
     "reserved characters) MISSES",
     b"C:\\Users\\<test>\\file.txt"),
    ("lp-syslog", "field/hit a realistic syslog line: facility.priority "
     "prefix, timestamp, host, program[pid]:",
     b"<34>Jan 15 12:34:56 myhost sshd[1234]: Accepted password"),
    ("lp-atomic-hit", "field/hit a valid facility.severity tag: both the "
     "atomic and non-atomic authored control pair accept it",
     b"kern.err: disk failure reported"),
    ("lp-atomic-nonmatch", "field/miss a facility-shaped but invalid "
     "token (no such facility): both members of the control pair "
     "reject it identically -- only their COST differs on a line built "
     "to make the atomic form fail fast", b"kernphemeral.err: bogus"),

    # -- wild-waf (family 3): five CRS SQLi rules
    ("waf-dbnames", "field/hit an information_schema reference",
     b"SELECT * FROM information_schema.tables"),
    ("waf-sleep", "field/hit a time-based blind SQLi payload",
     b"1' OR SLEEP(5)--"),
    ("waf-union", "field/hit a UNION SELECT payload",
     b"1 UNION SELECT username,password FROM users"),
    ("waf-concat", "field/hit a CONCAT-based exfiltration payload",
     b"SELECT CONCAT(username,0x3a,password) FROM users"),
    ("waf-comment-obfuscation", "field/hit a MySQL versioned-comment "
     "obfuscated payload", b"/*!50000SELECT*/ 1"),
    ("waf-benign", "line/miss an ordinary request body with none of the "
     "five CRS SQLi shapes", b"GET /products?category=shoes&sort=price"),

    # -- wild-secrets (family 4): four token shapes, exact-length hits
    ("sec-aws-key", "field/hit an AWS access key id (the documented "
     "AKIA... exemplar shape)", b"AKIAIOSFODNN7EXAMPLE"),
    ("sec-github-pat", "field/hit a fine-grained GitHub PAT (82 hex/"
     "alnum characters after the prefix, exact length)",
     b"github_pat_" + b"A" * 41 + b"a" * 41),
    ("sec-slack-webhook", "field/hit a Slack incoming-webhook URL "
     "(exact per-segment lengths: T+8, B+8..12, +24)",
     b"https://hooks.slack.com/services/T12345678/B123456789012/"
     b"abcdefghijklmnopqrstuvwx"),
    ("sec-userpass", "line/hit a username=...password=... pair, the "
     "HTTP-Parameter-Pollution-style shape",
     b'username="bob" password="hunter2"'),

    # -- wild-datetime (family 5): one ISO-8601 hit, one prose-month hit
    ("dt-iso8601", "field/hit a full ISO-8601 UTC timestamp",
     b"2026-09-16T12:34:56Z"),
    ("dt-prose-month", "field/hit a spelled-month date: the "
     "datefinder alternation's month-name branch",
     b"March 5, 2026"),

    # -- wild-codegrammar (family 6): five JSON-grammar fragments +
    # the (?x)/flat control pair
    ("cg-array-begin", "field/hit a JSON array opener", b"["),
    ("cg-constant", "field/hit a JSON boolean constant", b"true"),
    ("cg-object-begin", "field/hit a JSON object opener", b"{"),
    ("cg-number", "field/hit a signed float in exponential form",
     b"-123.45e10"),
    ("cg-string-escape", "field/hit a JSON string escape sequence "
     "(backslash + n, two literal bytes, not a real newline)", b"\\n"),
    ("cg-key-colon", "field/hit a quoted object key followed by its "
     "colon: both the (?x) and flattened control-pair members",
     b'"key": '),

    # -- cap-backref (family 7): five deployed backreference idioms
    ("br-doubled-word", "field/hit a doubled word", b"the the cat sat"),
    ("br-tag-pair", "field/hit a matching open/close tag pair",
     b"<div>content</div>"),
    ("br-tag-mismatch", "field/miss a MISMATCHED tag pair",
     b"<div>content</span>"),
    ("br-palindrome", "field/hit a 6-digit palindrome number",
     b"123321"),
    ("br-quoted-delim", "field/hit a single-quoted string",
     b"'single quoted'"),
    ("br-dup-param", "field/hit a query string repeating one key "
     "(HTTP Parameter Pollution shape)", b"a=1&b=2&a=3"),

    # -- cap-lookaround (family 8): password strength, float boundary,
    # email dot-dot, currency lookbehind, negation-scope variable
    # lookbehind
    ("la-pwd-strong", "field/hit a password meeting all four lookahead "
     "classes (lower/upper/digit/symbol, >=8)", b"Abcd123!"),
    ("la-pwd-weak", "field/miss a password missing the symbol class",
     b"Abcdefg123"),
    ("la-float-bound", "field/hit a standalone float literal",
     b"pi=3.14 units"),
    ("la-float-dotted", "field/miss a float-shaped substring inside a "
     "longer dotted token (a version string)", b"v3.14.159"),
    ("la-email-nodup", "field/hit an email local-part with no "
     "consecutive dots", b"john.doe@"),
    ("la-email-dotdot", "field/miss an email local-part WITH "
     "consecutive dots", b"john..doe@"),
    ("la-currency", "field/hit a dollar-prefixed amount",
     b"$42.50 due"),
    ("la-negation-hit", "field/hit 'available' with no negation window "
     "before it", b"currently available"),
    ("la-negation-miss", "field/miss 'available' preceded by a short "
     "negation phrase within the bounded lookbehind window",
     b"not currently available"),

    # -- cap-recursion (family 9): balanced parens, DEFINE array,
    # nested comment, depth-3 bound (no recursion construct)
    ("rec-parens-balanced", "field/hit balanced nested parens",
     b"(a(b)c)"),
    ("rec-parens-unbalanced", "field/miss an unbalanced opener",
     b"(a(bc"),
    ("rec-array-define", "field/hit a nested bracket array",
     b"[1,[2,3],4]"),
    ("rec-comment-nested", "field/hit a nested block comment",
     b"/* outer /* inner */ still open */"),
    ("rec-tag-depth3", "field/hit three levels of nested tags",
     b"<a><b><c>x</c></b></a>"),

    # -- redos-nested (family 10): six hits + one SHORT near-miss per
    # shape, kept <= 20 bytes so a catastrophic-backtracking miss stays
    # bounded during oracle derivation (capability_set_v1.md 3.5's own
    # calibration-risk note; the REAL harness cell's mitigation is a
    # fixed --iters override, a separate, later concern)
    ("rd-email-hit", "field/hit a normal email local-part",
     b"john.doe@x"),
    ("rd-email-near-miss", "field/near-miss SHORT nested-quantifier "
     "trigger with no terminating '@' (20 bytes, bounded)",
     b"aaaaaaaaaaaaaaaaaaaa"),
    ("rd-trim-hit", "field/hit an all-whitespace line", b"    "),
    ("rd-trim-near-miss", "field/near-miss SHORT whitespace run with a "
     "non-whitespace tail (20 bytes)", b" " * 19 + b"x"),
    ("rd-evil-alt-hit", "field/hit the evil-alternation shape's "
     "simplest accept", b"aaaa"),
    ("rd-evil-alt-near-miss", "field/near-miss SHORT nested-alternation "
     "trigger with a trailing non-letter (18 bytes)",
     b"a" * 17 + b"!"),
    ("rd-numeric-id-hit", "field/hit a plain digit run", b"1234"),
    ("rd-numeric-id-near-miss", "field/near-miss SHORT nested-plus "
     "digit trigger (20 bytes)", b"1" * 19 + b"x"),
    ("rd-phone-list-hit", "field/hit a space-separated digit run",
     b"123 456"),
    ("rd-date-hit", "field/hit a simple delimited numeric token",
     b"12-25"),

    # -- semantics-divergence (family 11): alternation order
    ("sd-router-short", "field/edge 'user' vs 'users': leftmost-first "
     "reports the 5-byte 'user' branch; leftmost-longest would report "
     "the 6-byte 'users' branch (under posix-leftmost-longest)",
     b"/users"),
    ("sd-fileext-short", "field/edge '.tar' vs '.tar.gz': same "
     "leftmost-first/longest divergence", b"archive.tar.gz"),
    ("sd-keyword-short", "field/edge 'in' vs 'instanceof': same "
     "divergence, the classic hand-rolled-lexer bug", b"instanceof"),
    ("sd-empty-alt-hit", "field/hit `(a|)*\\d`'s PCRE2 testdata case: "
     "60 a's then a digit", b"a" * 60 + b"5"),
    ("sd-empty-alt-miss", "field/miss the same case with NO trailing "
     "digit -- PCRE2's own testdata 'Expect no match'", b"a" * 60),
    ("sd-dollar-nl", "field/edge `abc$` against 'abc\\n' vs 'abc\\ndef' "
     "(the PCRE2 testdata pair, joined as one subject via the search "
     "regime's own scan -- see NOTES.md)", b"abc\ndef"),

    # -- binary-nonutf8 (family 12): raw bytes, legitimate here since
    # subjects are files, never TSV cells
    ("nu-high-byte", "field/hit two consecutive high bytes (0x81 0x82)",
     b"\x81\x82"),
    ("nu-mojibake", "field/hit a curly-quote byte pair (0x93/0x94) "
     "around printable ASCII -- the mojibake-repair shape",
     b"\x93hello\x94"),
    ("nu-lead-no-cont", "field/hit a UTF-8 lead byte (0xc2) NOT "
     "followed by a valid continuation byte", b"\xc2X"),
    ("nu-lead-with-cont", "field/miss a well-formed two-byte UTF-8 "
     "sequence (0xc3 0xa9, 'e' with acute) -- the lead byte IS followed "
     "by a valid continuation, so utf8-lead-no-cont must NOT hit here",
     b"\xc3\xa9"),

    # -- floor
    ("floor-hit", "field/hit the floor byte '~', per-call overhead "
     "control", b"~"),
)


def build():
    seen = set()
    for sid, desc, body in SUBJECTS:
        assert sid not in seen, sid
        seen.add(sid)
        assert "\t" not in desc, sid
        assert len(body) <= MAX_LINE, (sid, len(body))
    return SUBJECTS


def main():
    subjects = build()
    os.makedirs(OUT, exist_ok=True)
    rows = ["id\tlen\tsha256\tdescription\tperiodic"]
    for sid, desc, body in subjects:
        with open(os.path.join(OUT, sid + ".bin"), "wb") as f:
            f.write(body)
        rows.append("%s\t%d\t%s\t%s\t%s" % (
            sid, len(body), hashlib.sha256(body).hexdigest(), desc,
            ct.periodic_field(body)))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as mf:
        mf.write("\n".join(rows) + "\n")
    sizes = [len(b) for _s, _d, b in subjects]
    print("gen_subjects: %d subjects (%d B, %d..%d) -> %s, manifest -> %s"
          % (len(subjects), sum(sizes), min(sizes), max(sizes), OUT,
             MANIFEST))
    return 0


if __name__ == "__main__":
    sys.exit(main())
