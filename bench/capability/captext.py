"""captext.py -- the capability set's shared randomness primitive and
throughput-text grammar, in the shape of `bench/syntax/censustext.py`
(same xorshift64* PRNG, same "re-export `periodic_field`" convention).

The GRAMMAR mixes four parts per capability_set_v1.md 3.4's own words --
"log-line, HTTP-request-ish, source-code and prose parts" -- so every
family's typed short-subject vocabulary (validators, log lines, WAF
payloads, secrets-shaped tokens, dates, JSON) has a REALISTIC background
to be sparse in, at throughput scale. Deterministic: every text() call
with the same seed reproduces the same bytes byte for byte.
"""
from pcrecbench.periodic import periodic_field  # noqa: F401  (re-export)

MASK64 = (1 << 64) - 1


class Rng:
    """xorshift64* -- the same primitive `bench/syntax/censustext.py` uses,
    copied rather than imported so this set's throughput texts never move
    when that one's generator changes."""

    def __init__(self, seed):
        self.state = seed & MASK64 or 0x2545F4914F6CDD1D

    def next64(self):
        x = self.state
        x ^= (x >> 12)
        x ^= (x << 25) & MASK64
        x ^= (x >> 27)
        self.state = x & MASK64
        return (x * 0x2545F4914F6CDD1D) & MASK64

    def randrange(self, n):
        return self.next64() % n

    def choice(self, seq):
        return seq[self.randrange(len(seq))]


_WORDS = ("the", "a", "user", "session", "request", "payload", "value",
          "token", "server", "client", "error", "status", "handler",
          "module", "config", "field", "record", "index", "cache",
          "queue", "worker", "signal", "buffer", "socket", "stream")
_NAMES = ("alice", "bob", "carol", "dave", "erin", "frank", "grace")
_HOSTS = ("web01", "db02", "cache03", "api-gw", "worker-7", "edge-node")
_PROGS = ("sshd", "nginx", "cron", "systemd", "app")
_EXT = ("tar.gz", "json", "log", "csv", "py")

_LOG_LEVELS = ("INFO", "WARN", "ERROR", "DEBUG")


def _log_line(rng):
    host = rng.choice(_HOSTS)
    prog = rng.choice(_PROGS)
    pid = 1000 + rng.randrange(9000)
    level = rng.choice(_LOG_LEVELS)
    w1, w2 = rng.choice(_WORDS), rng.choice(_WORDS)
    return "%s %s[%d]: %s %s %s" % (host, prog, pid, level, w1, w2)


def _http_line(rng):
    verb = rng.choice(("GET", "POST", "PUT", "DELETE"))
    path = "/api/v1/%s/%d" % (rng.choice(_WORDS), rng.randrange(9999))
    status = rng.choice((200, 301, 400, 404, 500))
    return "%s %s HTTP/1.1 %d %dms" % (verb, path, status,
                                        1 + rng.randrange(500))


def _source_line(rng):
    # Roughly every other source line carries a double-quoted string
    # literal (a log call or an f-string), a REAL, common source-code
    # shape -- and, not incidentally, what keeps this grammar SAFE for an
    # unanchored `[^"\\]+`-shaped pattern (capability_set_v1.md 3.1
    # family 6's own `codegrammar-flat`): with NO quote in the whole
    # background text, that construct's negated class never finds its
    # terminator anywhere in a 1 MB subject and backtracks QUADRATICALLY
    # over the entire unbroken run (measured: 37s on a 64 KB throughput
    # text alone, projecting to hours at 1 MB -- found by this lane's own
    # diagnostic sweep, `diag_expectations_timing.py`, not by inspection).
    # A quote roughly every ~40-80 bytes bounds that worst case to one
    # line's length, not the whole subject's.
    name = rng.choice(_WORDS)
    val = rng.randrange(1000)
    if rng.randrange(2) == 0:
        return 'log.info("%s_%d")' % (name, val)
    return "def %s_%d(x): return x + %d  # %s" % (
        name, rng.randrange(99), val, rng.choice(_WORDS))


def _prose_line(rng):
    n = 6 + rng.randrange(8)
    words = [rng.choice(_WORDS) for _ in range(n)]
    words[0] = words[0].capitalize()
    return " ".join(words) + "."


_LINE_KINDS = (_log_line, _http_line, _source_line, _prose_line)


def text(nbytes, seed):
    """`nbytes` (approximately -- the last line is trimmed to fit) of
    mixed log/HTTP/source/prose text, deterministic in `seed`. No control
    bytes, no `#` (the floor's own reservation, capability_set_v1.md
    3.3), no `\\r`."""
    rng = Rng(seed)
    out = []
    total = 0
    while total < nbytes:
        kind = rng.choice(_LINE_KINDS)
        line = kind(rng)
        if total + len(line) + 1 > nbytes:
            remaining = nbytes - total - 1
            if remaining > 0:
                out.append(line[:remaining])
            break
        out.append(line)
        total += len(line) + 1
    return ("\n".join(out) + "\n").encode("ascii", "replace")


# ---------------------------------------------------------------------------
# [B125] capability@0.2 -- the additions. EVERYTHING BELOW IS NEW CODE: the
# four functions above (Rng, text and its line kinds) are untouched, and every
# function here seeds a FRESH Rng, so no 0.1 subject's bytes can move
# (gen_throughput_subjects.py asserts the three 0.1 sha256s). They draw their
# randomness AFTER 0.1's, in the only sense that matters for a set whose
# subjects are independent files: new seeds, new streams, appended manifest
# rows.
# ---------------------------------------------------------------------------

_HEX = "0123456789abcdef"
_B36 = "0123456789abcdefghijklmnopqrstuvwxyz"
_SEPS = " -_.:/,;="
_FILE_EXT = ("txt", "log", "json", "csv")


def letter_run(nbytes, seed):
    """`nbytes` of uniformly random [a-z] -- the long MATCHING subject of
    `^(([a-z]+)*)+$` (and, plus one terminating `!`, its near-miss)."""
    rng = Rng(seed)
    return bytes(97 + rng.randrange(26) for _ in range(nbytes))


def ws_run(nbytes, seed):
    """`nbytes` of mixed \\s bytes (space 70%, tab 15%, LF 10%, CR 2%, FF 2%,
    VT 1%), ending in a SPACE so `$`'s before-a-final-newline
    allowance never decides the span. The long MATCHING subject of
    `^(\\s+)*$` (plus one terminating `x`, its near-miss)."""
    rng = Rng(seed)
    out = bytearray()
    for _ in range(nbytes):
        r = rng.randrange(100)
        out.append(32 if r < 70 else 9 if r < 85 else 10 if r < 95
                   else 13 if r < 97 else 12 if r < 99 else 11)
    out[-1] = 32
    return bytes(out)


def mixed_runs(nbytes, seed):
    """`nbytes` of interleaved SHORT runs -- letters (1-6), digits (1-4),
    hex (2-8), a signed decimal, a lone separator, now and then a standalone
    8-hex id -- the way real identifiers, versions and log fields interleave,
    in place of the pure single-class runs every other subject here is. The
    last byte is a letter (an end-anchored `[a-z]{0,N}\\z` ends non-empty)."""
    rng = Rng(seed)
    out = []
    total = 0
    while total < nbytes:
        k = rng.randrange(14)
        if k < 4:
            tok = "".join(chr(97 + rng.randrange(26))
                          for _ in range(1 + rng.randrange(6)))
        elif k < 6:
            tok = "".join(str(rng.randrange(10))
                          for _ in range(1 + rng.randrange(4)))
        elif k < 8:
            tok = "".join(_HEX[rng.randrange(16)]
                          for _ in range(2 + rng.randrange(7)))
        elif k < 10:
            tok = _SEPS[rng.randrange(len(_SEPS))]
        elif k < 12:
            tok = (rng.choice(("", "-", "+"))
                   + "".join(str(rng.randrange(10))
                             for _ in range(1 + rng.randrange(4)))
                   + ("." + "".join(str(rng.randrange(10))
                                    for _ in range(1 + rng.randrange(3)))
                      if rng.randrange(2) else ""))
        else:
            tok = " " + "".join(_HEX[rng.randrange(16)] for _ in range(8)) + " "
        out.append(tok)
        total += len(tok)
    body = "".join(out)[:nbytes]
    return (body[:-1] + "z").encode("ascii")


def prose(nbytes, seed, tail):
    """~`nbytes` of generated prose (whole lines of 6-13 words, the 0.1
    grammar's `_WORDS`), with, per line, a 1-in-8 chance of a number in place
    of a word, 1-in-40 of a `name.ext` file mention and 1-in-60 of a lone
    8-hex id -- real prose is not digit-free, and an end-anchored `\\d+$` or
    `.*\\.txt$` must be able to start somewhere and fail. The prose is the
    SAME bytes for every `tail` (same seed); the subject is
    `prose + "\\n" + tail`, `tail` a bytes line with no trailing newline."""
    rng = Rng(seed)
    lines = []
    total = 0
    while True:
        n = 6 + rng.randrange(8)
        words = [rng.choice(_WORDS) for _ in range(n)]
        for j in range(n):
            if rng.randrange(8) == 0:
                words[j] = str(rng.randrange(100000))
        if rng.randrange(40) == 0:
            words[rng.randrange(n)] = "%s.%s" % (rng.choice(_WORDS),
                                                 rng.choice(_FILE_EXT))
        if rng.randrange(60) == 0:
            words[rng.randrange(n)] = "%08x" % rng.randrange(1 << 32)
        words[0] = words[0].capitalize()
        line = " ".join(words) + "."
        if total + len(line) + 1 > nbytes:
            break
        lines.append(line)
        total += len(line) + 1
    return ("\n".join(lines) + "\n").encode("ascii") + tail


# ---------------------------------------------------------------------------
# [B123] capability@0.3 -- the capture-forced-hybrid MATCH subjects (pcrec
# I-125 Q10 / I-127 [BENCH-ASKS-PENDING] (2)): 1-64 KiB subjects on which the
# 17 `RX_VM_PREFILTER "hybrid"` + `RX_ENGINE_WHY "capture group"` patterns
# actually MATCH, in place of the 5-93 byte hand literals. Again NEW code only:
# every function seeds a fresh Rng and no 0.1/0.2 subject can move.
#
# Two kinds, because the 17 are two kinds of pattern:
#   * the UNANCHORED seven-plus (JSON key, syslog prefix, secrets, a
#     credentials pair, `(a|)*\d`) match INSIDE text: `hyb_embed`, a ladder
#     of three sizes of one log/config/JSON grammar with planted instances;
#   * the `^...$` / `^...@` ones match the WHOLE SUBJECT (or its prefix): one
#     generated subject per shape, `hyb_logline`, `hyb_datepath`,
#     `hyb_digits`, each safe against the set's ReDoS family (every `^`-
#     anchored hazard pattern attempts offset 0 only, and the first run of
#     its alphabet at offset 0 is a few bytes long by construction).
# `ipv4`, `us-zip` and `moment-iso8601` have NO realistic 1-64 KiB matching
# subject (their languages are bounded at <= ~30 B; a long leading `\s*` pad
# would be the `^(\s+)*$` family's catastrophic near-miss): NOTES.md, 0.3.
# ---------------------------------------------------------------------------

_ALNUM_LC = "abcdefghijklmnopqrstuvwxyz0123456789_"
_ALNUM_UC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_ALNUM_MIX = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
_MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
           "Oct", "Nov", "Dec")
_PASSWORDS = ("hunter22", "s3cretpw", "letmein99", "correcthorse")


def _pick(rng, alphabet, n):
    return "".join(alphabet[rng.randrange(len(alphabet))] for _ in range(n))


def _json_line(rng):
    return '  {"id": %d, "name": "%s", "kind": "%s", "ok": %s}' % (
        rng.randrange(100000), rng.choice(_WORDS), rng.choice(_WORDS),
        rng.choice(("true", "false")))


def _syslog_line(rng):
    return "%s %2d %02d:%02d:%02d %s %s[%d]: %s %s" % (
        rng.choice(_MONTHS), 1 + rng.randrange(28), rng.randrange(24),
        rng.randrange(60), rng.randrange(60), rng.choice(_HOSTS),
        rng.choice(_PROGS), 1000 + rng.randrange(9000),
        rng.choice(_WORDS), rng.choice(_WORDS))


def _aws_line(rng):
    return "aws_access_key_id = AKIA%s" % _pick(rng, _ALNUM_UC, 16)


def _github_line(rng):
    return "token: github_pat_%s" % _pick(rng, _ALNUM_MIX, 82)


def _slack_line(rng):
    return "webhook = https://hooks.slack.com/services/T%s/B%s/%s" % (
        _pick(rng, _ALNUM_LC, 8), _pick(rng, _ALNUM_LC, 8 + rng.randrange(5)),
        _pick(rng, _ALNUM_LC, 24))


def _creds_block(rng):
    return 'username = "%s"\npassword = "%s"' % (rng.choice(_NAMES),
                                                   rng.choice(_PASSWORDS))


_EMBED_PLANTS = (_json_line, _syslog_line, _aws_line, _github_line,
                 _slack_line, _creds_block)
_EMBED_BACKGROUND = (_log_line, _http_line, _source_line, _prose_line)


def hyb_embed(nbytes, seed):
    """EXACTLY `nbytes` of log/config/JSON text (the last line is cut at the
    byte boundary, as `text()` does). Line 1 is
    an address line (`alice.smith+lists@example.com wrote:`) so the `^`-
    prefix `^([a-zA-Z0-9._%+-]+)+@` matches at offset 0; the next six lines
    plant ONE instance of each embedded family (JSON key, syslog prefix, AWS
    key id, GitHub PAT, Slack webhook, credentials pair), so even the 1 KiB
    rung holds every instance; after that each line is a plant with
    probability 1/4 (kinds uniform) and a background line (the 0.1 grammar's
    four kinds) otherwise. Source lines keep their quoted strings, so an
    unanchored `[^"\\\\]+` class stays bounded by one gap between quotes."""
    rng = Rng(seed)
    lines = ["alice.smith+lists@example.com wrote:"]
    lines += [p(rng) for p in _EMBED_PLANTS]
    total = sum(len(l) + 1 for l in lines)
    while total < nbytes:
        if rng.randrange(4) == 0:
            line = rng.choice(_EMBED_PLANTS)(rng)
        else:
            line = rng.choice(_EMBED_BACKGROUND)(rng)
        lines.append(line)
        total += len(line) + 1
    return ("\n".join(lines) + "\n").encode("ascii")[:nbytes]


def hyb_logline(nbytes, seed):
    """EXACTLY `nbytes` of ONE line, no newline: `kern.err: ` then prose
    words. The whole subject is the match of `logparse-atomic` (and its
    `-removed` twin), `^(?>facility.level): (.*)$` -- a long message, the way
    a stack trace or a JSON payload rides inside one syslog line."""
    rng = Rng(seed)
    words = ["kern.err:"]
    total = len(words[0])
    while total < nbytes:
        w = rng.choice(_WORDS)
        words.append(w)
        total += 1 + len(w)
    body = " ".join(words)[:nbytes]
    return (body[:-1] + ("x" if body[-1] == " " else body[-1])).encode("ascii")


def hyb_datepath(nbytes, seed):
    """EXACTLY `nbytes`: digit groups (1-4) each closed by `/` (three in four)
    or `-`, the first group fixed `2025/` so offset 0's first alphabet run is
    5 bytes, ending in a `/`. The whole subject is the match of
    `date-nested-plus`, `^(([0-9]+[-/])+)+$` -- a URL/date path."""
    rng = Rng(seed)
    out = ["2025/"]
    total = 5
    while True:
        tok = _pick(rng, "0123456789", 1 + rng.randrange(4)) + (
            "-" if rng.randrange(4) == 0 else "/")
        if total + len(tok) > nbytes:
            break
        out.append(tok)
        total += len(tok)
    body = "".join(out)
    pad = nbytes - len(body)
    return (body[:-1] + "0" * pad + "/").encode("ascii") if pad else \
        body.encode("ascii")


def hyb_digits(nbytes, seed):
    """EXACTLY `nbytes` random decimal digits (first non-zero). The whole
    subject is the match of `numeric-id-nested-plus` `^(\\d+)+$` and of
    `phone-list-nested-plus` `^(\\d+\\s*)+$` -- and a would-be catastrophic
    near-miss for `email-nested-plus` (the digits are in its class, there is
    no `@`): libpcre2's required-code-unit check dismisses it at once
    (measured 0.0 s through the oracle), so the oracle needs no fallback
    method here; an engine WITHOUT that check backtracks and may give up."""
    rng = Rng(seed)
    return (str(1 + rng.randrange(9)) + _pick(rng, "0123456789", nbytes - 1)
            ).encode("ascii")


# ---------------------------------------------------------------------------
# [B172] capability@0.4 -- the URL query-string subjects (pcrec I-172): access-
# log query parts, one per line, `k1=v1&k2=v2&...`, on which `dup-param-detect`
# (`\b(\w+)=[^&]*&(?:[^&]*&)*\1=`) does real work. NEW code only; every function
# seeds a fresh Rng, no 0.1-0.3 subject can move.
#
# THE SEMANTICS THE GENERATOR IS BUILT AROUND (NOTES.md, 0.4): `[^&]` matches
# the newline, so the pattern is LINE-BLIND -- a key repeated on a LATER LINE
# is a duplicate to it. A realistic vocabulary (`id`, `page`, `utm_source`
# on every line) would therefore make the very first key a "duplicate" of the
# last line's and one greedy match would swallow the subject. So the allocator
# below hands out each key text AT MOST ONCE per subject (a stem's first use is
# the bare stem, later uses `stem_k3f` with a short base-36 tag), and the ONLY repeated keys are the declared,
# planted duplicates.
# ---------------------------------------------------------------------------

_QS_STEMS = (
    ("utm_source", 3), ("utm_medium", 3), ("utm_campaign", 3),
    ("utm_term", 1), ("utm_content", 1), ("id", 6), ("page", 4), ("q", 4),
    ("sort", 3), ("order", 2), ("lang", 2), ("ref", 3), ("sid", 2),
    ("session", 2), ("token", 2), ("filter", 4), ("cat", 3), ("tag", 3),
    ("limit", 2), ("offset", 2), ("ts", 2), ("v", 2), ("cb", 1), ("fbclid", 1),
    ("gclid", 1), ("user", 2), ("item", 3), ("lat", 1), ("lng", 1), ("sku", 2),
)
_QS_STEM_BAG = tuple(s for s, w in _QS_STEMS for _ in range(w))
_QS_STEM_MAP = dict(_QS_STEMS)
# near-miss twists: keys that share a prefix/suffix with an existing key.
_QS_TWIST = ("x", "s", "_id", "_2", "id")
_QS_WORDS = ("summer", "sale", "email", "newsletter", "cpc", "organic",
             "search", "home", "shoes", "red", "blue", "mobile", "desktop",
             "en", "de", "fr", "asc", "desc", "price", "date", "name")
_QS_PCT = ("%20", "%2F", "%3A", "%2C", "%40", "%C3%A9", "%E2%9C%93", "%2B",
           "%3F", "%23")
_HEX = "0123456789abcdef"
_B36 = "0123456789abcdefghijklmnopqrstuvwxyz"


class _QsKeys:
    """Hands out each key text at most once per subject (see the banner)."""

    def __init__(self, rng, twist=False):
        self.rng = rng
        self.twist = twist
        self.used = set()

    def fresh(self):
        rng = self.rng
        stem = _QS_STEM_BAG[rng.randrange(len(_QS_STEM_BAG))]
        if self.twist and rng.randrange(3) == 0 and stem in self.used:
            # a prefix/suffix relative of a key already used: `id` -> `idx`,
            # `ids`, `id_id`, `id_2`, `idid`; never the same text.
            key = stem + _QS_TWIST[rng.randrange(len(_QS_TWIST))]
            if key not in self.used:
                self.used.add(key)
                return key
        if stem not in self.used:
            self.used.add(stem)
            return stem
        # a stem's later uses carry a short base-36 tag (`id_k3f`, the way
        # services mint `utm_x9q` / `ref_a1b2` custom parameters); 3 chars,
        # then 4 if the 3-char space is crowded
        width = 3
        while True:
            key = "%s_%s" % (stem, _pick(rng, _B36, width))
            if key not in self.used:
                self.used.add(key)
                return key
            width = 4


def _qs_value(rng):
    r = rng.randrange(100)
    if r < 8:
        return ""
    if r < 38:
        return str(rng.randrange(1000000))
    if r < 55:
        return _pick(rng, _HEX, 8 + rng.randrange(25))
    if r < 80:
        return rng.choice(_QS_WORDS)
    if r < 92:
        return "%s%s%s" % (rng.choice(_QS_WORDS), rng.choice(_QS_PCT),
                           rng.choice(_QS_WORDS))
    return "%s%%40%s.com" % (rng.choice(_NAMES), rng.choice(_QS_WORDS))


def qs_text(nbytes, seed, dup_ppm=35000, twist=False):
    """-> (bytes, stats). Whole lines only, total length <= `nbytes` and
    within one line of it. Each line is `k=v&k=v...` (no `?`, no trailing
    `&`): 2-10 params, one line in 300 a LONG line of 150-400 params. With
    probability `dup_ppm`/1e6 per line (`dup_ppm=0`: none) the line PLANTS a
    duplicate: one key of the line is scheduled to recur (as a second `k=v`
    with a fresh value) -- on the same line 1-30 params later (40%), on the
    next line (25%), 2-40 lines later (30%), or 300-3000 lines later (5%, the
    FAR duplicates). A planted key recurs exactly once, so every other key is
    unique in the subject. `twist=True` makes unique keys share prefixes and
    suffixes with earlier ones (`id`, `idx`, `ids`, `id_2`)."""
    rng = Rng(seed)
    keys = _QsKeys(rng, twist)
    pending = {}                     # line index -> [key to repeat there]
    lines = []
    total = 0
    dup_lines = 0
    li = 0
    while True:
        long_line = rng.randrange(300) == 0
        n = 150 + rng.randrange(251) if long_line else 2 + rng.randrange(9)
        ks = [keys.fresh() for _ in range(n)]
        # the first occurrences of this line's planted dups sit on this line
        # (or, for a cross-line dup, are scheduled at a later line)
        plant = dup_ppm and rng.randrange(1000000) < dup_ppm
        if plant:
            r = rng.randrange(100)
            key = ks[rng.randrange(len(ks))]
            if r < 40 and len(ks) >= 3:
                i = rng.randrange(len(ks) - 1)
                key = ks[i]
                ks.insert(min(len(ks), i + 2 + rng.randrange(30)), key)
            else:
                if r < 65:
                    d = 1
                elif r < 95:
                    d = 2 + rng.randrange(39)
                else:
                    d = 300 + rng.randrange(2701)
                pending.setdefault(li + d, []).append(key)
        for key in pending.pop(li, ()):
            ks.insert(rng.randrange(len(ks) + 1), key)
        line = "&".join("%s=%s" % (k, _qs_value(rng)) for k in ks)
        if total + len(line) + 1 > nbytes:
            break
        lines.append(line)
        total += len(line) + 1
        li += 1
    body = ("\n".join(lines) + "\n").encode("ascii")
    # stats from the text itself, not from the schedule
    seen = {}
    dup_lines = 0
    for line in lines:
        has = False
        for p in line.split("&"):
            k = p.split("=", 1)[0]
            if k in seen:
                has = True
            seen[k] = seen.get(k, 0) + 1
        dup_lines += has
    stats = {"lines": len(lines), "bytes": len(body),
             "params": sum(seen.values()),
             "dup_keys": sum(1 for v in seen.values() if v > 1),
             "dup_lines": dup_lines,
             "max_params": max(l.count("&") + 1 for l in lines)}
    return body, stats
