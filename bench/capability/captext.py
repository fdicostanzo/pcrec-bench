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
