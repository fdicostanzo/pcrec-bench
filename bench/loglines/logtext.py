#!/usr/bin/env python3
"""logtext.py -- the log-line GRAMMAR both generators of this sub-bench draw
from, and the two facts committed about the bytes they produce.

WHY IT IS ITS OWN MODULE. `gen_subjects.py` (the 256 B - 4 KB search band) and
`gen_throughput_subjects.py` (the 16 KB - 1 MB size sweep) must emit the SAME
kind of text -- a size sweep whose text differs from the search band's would
sweep two things at once. One grammar, two callers, one seed.

DETERMINISM. The only randomness primitive used anywhere in this sub-bench is
`random.Random(seed).getrandbits(32)`, which CPython documents as stable
across versions; `Rng` below builds every other draw on it. `random.choice`,
`random.sample` and `random.randrange` are NOT used: their internals have
changed between CPython releases, and a committed manifest that must
reproduce byte for byte cannot rest on that. `Rng.below()` takes the modulo
of a 32-bit draw -- a bias of at most 2^-32 per call, deliberately accepted,
because determinism is the property this file needs and uniformity to 1 part
in 4 billion is not.

THE BACKGROUND IS SHAPE-FREE BY CONSTRUCTION, AND FULL OF NEAR-MISSES. Every
line the `background()` grammar can emit is built so that NO member pattern of
this sub-bench matches it: BSD-syslog and klog timestamps (never ISO-8601),
hostnames where an access log would carry an IP, three-part version numbers
(never a dotted quad), 12-hex container ids (never 32), hyphenated short ids
(never the 8-4-4-4-12 UUID shape), digit runs of at most 8 (never 10+).
Those are near-misses on purpose: a failing subject whose bytes are rejected
at the first byte measures nothing, and this sub-bench's whole point is the
cost of FAILING over text that keeps the engine interested.

The shapes the patterns look for enter only through `feature_lines()`, which
the callers inject into a drawn minority of subjects. That is what sets the
match rate; `NOTES.md` states the resulting m/n per pattern, from the oracle.

THE `periodic` FACT (inbox I-10). `smallest_period()` is the manifest column's
definition: the smallest p in 1..limit such that b[i] == b[i-p] for every
i >= p, or None ("no") if there is none. Log text drawn field by field has
none; the fact is COMPUTED and committed rather than claimed, because "it is
non-periodic by construction" is exactly the kind of claim that stops being
true when someone edits the vocabulary.
"""

import random

# --------------------------------------------------------------------- rng


class Rng:
    """The one randomness primitive (see the module header)."""

    def __init__(self, seed):
        self._r = random.Random(seed)

    def below(self, n):
        return self._r.getrandbits(32) % n

    def between(self, lo, hi):
        """Inclusive on both ends."""
        return lo + self.below(hi - lo + 1)

    def pick(self, seq):
        return seq[self.below(len(seq))]

    def chance(self, per_mille):
        return self.below(1000) < per_mille

    def hexs(self, n):
        return "".join(self.pick("0123456789abcdef") for _ in range(n))

    def digits(self, n):
        return "".join(self.pick("0123456789") for _ in range(n))


# ------------------------------------------------------------- vocabulary

HOSTS = ["web-01", "web-02", "web-03", "api-01", "api-04", "cache-07",
         "db-02", "worker-11", "edge-04", "batch-09", "mq-05", "ingest-06"]
SERVICES = ["order-service", "cart", "auth", "billing", "search-idx",
            "notifier", "gateway", "sessiond", "inventory", "pricing"]
DAEMONS = ["sshd", "systemd", "cron", "kubelet", "containerd", "systemd-logind",
           "dbus-daemon", "chronyd", "rsyslogd", "snapd"]
USERS = ["deploy", "root", "svc-batch", "jenkins", "alice", "bob", "ops",
         "ci-runner", "backup"]
PATHS = ["/api/v1/orders", "/api/v1/users", "/healthz", "/static/app.css",
         "/v2/checkout", "/metrics", "/login", "/assets/logo.png",
         "/api/v1/carts", "/favicon.ico", "/api/v2/search", "/ready"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
UA = ["curl/8.5.0", "Mozilla/5.0 (X11; Linux x86_64)", "python-requests/2.31",
      "kube-probe/1.29", "Go-http-client/2.0", "Prometheus/2.48"]
GO_FILES = ["controller.go", "reflector.go", "kubelet.go", "scheduler.go",
            "informer.go", "endpoint.go", "volume_manager.go"]
JAVA_PKGS = ["com.example.shop", "com.example.auth", "org.springframework.web",
             "io.netty.channel", "com.example.billing"]
JAVA_CLASSES = ["OrderController", "CartService", "TokenFilter",
                "PriceResolver", "InventoryClient", "HttpDispatcher"]
JAVA_EXC = ["java.lang.NullPointerException",
            "java.lang.IllegalStateException",
            "java.util.concurrent.TimeoutException",
            "com.example.shop.OrderNotFoundException"]

SYSLOG_MSGS = [
    "Started Session {n} of user {user}.",
    "Stopping User Manager for UID {n}",
    "pam_unix(cron:session): session closed for user {user}",
    "session opened for user {user} by (uid={n})",
    "Removed slice User Slice of UID {n}",
    "Reloading configuration, {n} units affected",
    "Time step corrected by {ms} us",
    "Received disconnect from port {k}22",
    "Finished daily apt download activity.",
    "Closed D-Bus User Message Bus Socket.",
]

APP_MSGS = [
    "handled {method} {path} in {ms}ms",
    "cache warm complete (entries={n})",
    "flushed {n} rows to shard-{k}",
    "connection pool resized to {k}",
    "publishing {n} events to topic orders-v3",
    "reaped {k} idle workers",
    "config reload ok (revision {k})",
    "shard-{k} lag {ms}ms",
    "compaction finished, reclaimed {n}kB",
    "renewed lease for {user}",
]

KLOG_MSGS = [
    "Syncing configmap default/app-config",
    "Container runtime status check succeeded",
    "Probe succeeded for pod {svc}-{sid}",
    "Updating node lease, resourceVersion {n}",
    "Started container {svc}",
    "Volume detached for volume pvc-{sid}",
    "SyncLoop DELETE api pods default/{svc}-{sid}",
]

NGINX_ERR_MSGS = [
    "upstream server temporarily disabled while connecting to upstream, "
    "client: {host}, server: shop.example.net",
    "open() \"/srv/www{path}\" failed (2: No such file or directory), "
    "client: {host}",
    "recv() failed (104: Connection reset by peer) while reading upstream, "
    "client: {host}",
]

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"]
OK_STATUS = ["200", "201", "204", "301", "302", "304", "400", "401", "403",
             "404", "429"]
BAD_STATUS = ["500", "502", "503", "504"]


# ---------------------------------------------------------- the background


def _bsd_stamp(rng):
    return "%s %2d %02d:%02d:%02d" % (rng.pick(MONTHS), rng.between(1, 28),
                                      rng.between(0, 23), rng.between(0, 59),
                                      rng.between(0, 59))


def _clock(rng):
    return "%02d:%02d:%02d.%s" % (rng.between(0, 23), rng.between(0, 59),
                                  rng.between(0, 59), rng.digits(3))


def _shortid(rng):
    """A 12-hex container/pod id -- a NEAR-MISS for `hex32-id` (which wants
    32) and for `uuid` (which wants 8-4-4-4-12 with hyphens).

    At least one of the twelve is forced to a-f. MEASURED, and the reason
    this line exists: 62.5 % of hex digits are decimal, so an unconstrained
    12-hex id is all-digits about once in 290 -- and an all-digit 12-hex id
    IS a 12-digit number, which `bignum` (`\\b[0-9]{10,19}\\b`) matches. One
    such coincidence turned up in the first 112 subjects and would have
    turned up ~35 times in a 1 MB failing subject, which is the subject whose
    whole value is that NO member pattern matches it."""
    s = list(rng.hexs(12))
    s[rng.below(12)] = rng.pick("abcdef")
    return "".join(s)


def _dashid(rng):
    """A hyphenated short id: the near-miss for the UUID shape."""
    return "%s-%s-%s" % (rng.hexs(4), rng.hexs(4), rng.hexs(6))


def _version(rng):
    """THREE parts, never four: a dotted quad is what `ipv4` looks for."""
    return "%d.%d.%d" % (rng.between(0, 9), rng.between(0, 40),
                         rng.between(0, 9))


def _fill(rng, template):
    """`{n}` is capped at six digits and `{ms}` at four: the background must
    never contain a run of 10+ digits, which is what `bignum` looks for."""
    return (template
            .replace("{ms}", str(rng.between(1, 9000)))
            .replace("{n}", str(rng.between(1, 999999)))
            .replace("{k}", str(rng.between(1, 64)))
            .replace("{user}", rng.pick(USERS))
            .replace("{svc}", rng.pick(SERVICES))
            .replace("{sid}", _shortid(rng))
            .replace("{host}", rng.pick(HOSTS))
            .replace("{path}", rng.pick(PATHS))
            .replace("{method}", rng.pick(METHODS)))


def _syslog(rng):
    return "%s %s %s[%d]: %s" % (
        _bsd_stamp(rng), rng.pick(HOSTS), rng.pick(DAEMONS),
        rng.between(1, 32767), _fill(rng, rng.pick(SYSLOG_MSGS)))


def _applog(rng):
    return "%s %-5s %s - %s" % (
        _clock(rng), rng.pick(["INFO", "DEBUG", "WARN", "TRACE"]),
        rng.pick(SERVICES), _fill(rng, rng.pick(APP_MSGS)))


def _klog(rng):
    """kubernetes klog: `I0827 14:03:11.812345       1 controller.go:212] msg`
    -- a timestamp with NO year and NO hyphens, which is why `iso-ts` does not
    match it, and a 6-digit microsecond field, which is why `bignum` (10+
    digits) does not either."""
    return "%s%02d%02d %02d:%02d:%02d.%s %7d %s:%d] %s" % (
        rng.pick("IWE"), rng.between(1, 12), rng.between(1, 28),
        rng.between(0, 23), rng.between(0, 59), rng.between(0, 59),
        rng.digits(6), rng.between(1, 9999), rng.pick(GO_FILES),
        rng.between(20, 990), _fill(rng, rng.pick(KLOG_MSGS)))


def _nginx_err(rng):
    return "%04d/%02d/%02d %02d:%02d:%02d [%s] %d#%d: *%d %s" % (
        2026, rng.between(1, 12), rng.between(1, 28), rng.between(0, 23),
        rng.between(0, 59), rng.between(0, 59),
        rng.pick(["warn", "error", "notice"]), rng.between(1, 9999),
        rng.between(1, 9999), rng.between(1, 999999),
        _fill(rng, rng.pick(NGINX_ERR_MSGS)))


def _journald(rng):
    return "%s %s %s[%d]: image=%s:%s id=%s" % (
        _bsd_stamp(rng), rng.pick(HOSTS), "containerd", rng.between(1, 32767),
        rng.pick(SERVICES), _version(rng), _shortid(rng))


def _agentlog(rng):
    return "%s %s ua=%s ver=%s ref=%s" % (
        _clock(rng), rng.pick(HOSTS), rng.pick(UA), _version(rng),
        _dashid(rng))


BACKGROUND = (_syslog, _applog, _klog, _nginx_err, _journald, _agentlog)


# The messages with no parenthesis and no double quote in them. `syslog_only`
# below is built from these, and the exclusion is the whole point of it.
PLAIN_MSGS = [m for m in SYSLOG_MSGS if "(" not in m and '"' not in m]


def syslog_only(rng):
    """One line of a SINGLE-SOURCE BSD-syslog stream -- what `journalctl -o
    short` or one host's /var/log/syslog looks like.

    WHY THIS EXISTS BESIDE `background()`. Mixed log text contains every
    punctuation byte somewhere, so on a large mixed subject PCRE2's
    required-code-unit dismissal never fires: `:` `.` `-` and a digit are
    structural, and every literal-bearing pattern in this set requires one of
    those. MEASURED on the first cut of this sub-bench -- all eight throughput
    subjects contained every required byte, so not one of them was the
    analogue of bench/email's `t-b-no-at` (inbox I-7 1), the row where
    pcre2-interp dismissed a 1 MB subject at memchr speed.

    These lines carry NO `"` and NO `)`, which are exactly the required code
    units of `kv-quoted` and `stack-frame`. So on a `-syslog` subject those
    two patterns ARE dismissible without a scan and the rest are not, and one
    subject set holds both cases. `pattern_facts.tsv` names which is which,
    from PCRE2, rather than from this docstring."""
    return "%s %s %s[%d]: %s" % (
        _bsd_stamp(rng), rng.pick(HOSTS), rng.pick(DAEMONS),
        rng.between(1, 32767), _fill(rng, rng.pick(PLAIN_MSGS)))


def background(rng):
    """One background line (no trailing newline). Matches no member pattern
    of this sub-bench -- asserted by the oracle, not by this comment: the
    `fail` throughput subjects are pure background and their expectations are
    `nomatch` for every member (NOTES.md, "the failing subjects")."""
    return BACKGROUND[rng.below(len(BACKGROUND))](rng)


# ------------------------------------------------------------- the shapes

FEATURES = ("iso-ts", "ipv4", "ipv6", "kv-quoted", "level-context",
            "http-5xx", "uuid", "hex32-id", "bignum", "stack-frame")


def _iso_stamp(rng):
    return "2026-%02d-%02dT%02d:%02d:%02d.%sZ" % (
        rng.between(1, 12), rng.between(1, 28), rng.between(0, 23),
        rng.between(0, 59), rng.between(0, 59), rng.digits(3))


def _ipv4(rng):
    return "%d.%d.%d.%d" % (rng.between(10, 203), rng.between(0, 255),
                            rng.between(0, 255), rng.between(1, 254))


def _ipv6(rng):
    return "2001:0db8:%s:%s:%s:%s:%s:%s" % tuple(rng.hexs(4) for _ in range(6))


def _uuid(rng):
    return "%s-%s-%d%s-%s%s-%s" % (
        rng.hexs(8), rng.hexs(4), rng.between(1, 5), rng.hexs(3),
        rng.pick("89ab"), rng.hexs(3), rng.hexs(12))


def _access(rng, status, client=None):
    """An nginx/apache combined access line. The client field is the ONLY
    place an address occurs in this corpus, so `ipv4` and `ipv6` reach the
    text exactly through the access lines the callers inject."""
    if client is None:
        client = _ipv4(rng)
    return ('%s - - [%02d/%s/2026:%02d:%02d:%02d +0000] "%s %s HTTP/1.1" '
            '%s %d "-" "%s"'
            % (client, rng.between(1, 28), rng.pick(MONTHS), rng.between(0, 23),
               rng.between(0, 59), rng.between(0, 59), rng.pick(METHODS),
               rng.pick(PATHS), status, rng.between(120, 998877),
               rng.pick(UA)))


def feature_line(rng, feature):
    """The line (or block of lines) that carries ONE shape. Returns a list of
    lines. Each is a real line of its format -- the shape is what an operator
    would actually be grepping for, in the format it actually occurs in."""
    if feature == "iso-ts":
        return ["%s %s [%s] handled %s %s in %dms"
                % (_iso_stamp(rng), rng.pick(["INFO", "WARN"]),
                   rng.pick(SERVICES), rng.pick(METHODS), rng.pick(PATHS),
                   rng.between(1, 4000))]
    if feature == "ipv4":
        return [_access(rng, rng.pick(OK_STATUS))]
    if feature == "ipv6":
        return [_access(rng, rng.pick(OK_STATUS), client=_ipv6(rng))]
    if feature == "kv-quoted":
        return ['%s %-5s %s - request rejected reason="%s" rule="%s"'
                % (_clock(rng), "WARN", rng.pick(SERVICES),
                   rng.pick(["quota exceeded", "bad signature",
                             "unknown tenant", "payload too large"]),
                   rng.pick(["rate-limit", "authz-01", "schema-v3"]))]
    if feature == "level-context":
        return ["%s %-5s %s - %s: %s"
                % (_clock(rng), rng.pick(["ERROR", "FATAL", "CRIT"]),
                   rng.pick(SERVICES),
                   rng.pick(["upstream call failed", "backend unavailable",
                             "lease renewal failed"]),
                   rng.pick(["connection refused by pool",
                             "read timeout after 30s",
                             "access denied for principal svc-batch",
                             "host unreachable via edge"]))]
    if feature == "http-5xx":
        return [_access(rng, rng.pick(BAD_STATUS))]
    if feature == "uuid":
        return ["%s %-5s %s - accepted job request_id=%s"
                % (_clock(rng), "INFO", rng.pick(SERVICES), _uuid(rng))]
    if feature == "hex32-id":
        return ["%s %-5s %s - span closed trace=%s parent=%s"
                % (_clock(rng), "DEBUG", rng.pick(SERVICES), rng.hexs(32),
                   _shortid(rng))]
    if feature == "bignum":
        return ['{"ts":%s,"level":"info","svc":"%s","msg":"%s","bytes":%s}'
                % (rng.digits(13), rng.pick(SERVICES),
                   rng.pick(["batch committed", "snapshot written",
                             "segment sealed"]), rng.digits(10))]
    if feature == "stack-frame":
        lines = ['%s %-5s %s - unhandled exception, aborting request'
                 % (_clock(rng), "ERROR", rng.pick(SERVICES)),
                 'Exception in thread "http-%d" %s: %s'
                 % (rng.between(1, 64), rng.pick(JAVA_EXC),
                    rng.pick(["order id missing", "pool closed",
                              "no route to shard"]))]
        for _ in range(rng.between(2, 5)):
            lines.append("\tat %s.%s.%s(%s.java:%d)"
                         % (rng.pick(JAVA_PKGS), rng.pick(JAVA_CLASSES),
                            rng.pick(["handle", "resolve", "dispatch", "get",
                                      "apply"]), rng.pick(JAVA_CLASSES),
                            rng.between(20, 990)))
        return lines
    raise ValueError("unknown feature %r" % feature)


# ------------------------------------------------------------ the periodic
# fact (inbox I-10). The manifest column's DEFINITION lives here.


def smallest_period(b, limit=4096):
    """The smallest p in 1..min(limit, len(b)-1) with b[i] == b[i-p] for every
    i >= p, or None if there is none.

    `b[p:] == b[:-p]` is exactly that condition, done as one memcmp; the
    cheap `b[p] != b[0]` pre-test in front of it kills most candidates
    without touching the rest of the buffer, which is what makes this
    affordable on a 1 MB subject."""
    n = len(b)
    for p in range(1, min(limit, n - 1) + 1):
        if b[p] != b[0]:
            continue
        if b[p:] == b[:-p]:
            return p
    return None


def periodic_field(b, limit=4096):
    p = smallest_period(b, limit)
    return "no" if p is None else str(p)
