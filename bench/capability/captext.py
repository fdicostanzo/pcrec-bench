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
