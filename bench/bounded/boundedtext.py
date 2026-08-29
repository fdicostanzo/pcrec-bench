#!/usr/bin/env python3
"""boundedtext.py -- the subject GRAMMAR of the bounded-repeat sub-bench: the
three subject families `gen_subjects.py` draws from, and the one randomness
primitive they share.

WHY THREE FAMILIES. This sub-bench has two axes (NOTES.md): the everyday
bounded shapes (`\\d{4}`, `[0-9a-f]{32}`, `.{8,64}`, nested octet counts, a
bounded lazy gap before a `\\b` alternation) and a COUNT LADDER on a few
skeletons whose counts run to PCRE2's own ceiling. No one kind of subject
serves both, so there are three:

  FIELDS  4-65 B candidate strings for the MATCH regime -- the thing a
          validator is handed whole: a year, a 32-hex id, a password, a
          dotted quad, a CSV record. Each shape appears as the exact
          match, as a NEAR-MISS THAT FAILS AT THE LAST REPETITION (31 hex
          where 32 are wanted; three octets where four are), and as an
          over-run that fails only at the end anchor.
  LINES   43-256 B lines of ops prose (a timestamp, a host, a pid, words,
          numbers, hex tokens, dotted versions, paths). The SEARCH regime's
          text. The background is NEAR-MISSES by construction -- numbers of
          at most three digits, hex of at most 12, three-part versions, five-
          group MACs, `failure`/`aborted`/`panicked` where the patterns want
          `fail`/`abort`/`panic` as whole words -- and each everyday shape is
          injected into an exactly allocated minority of lines. The bounded-
          context lines carry a trigger word and a context word at a DESIGNED
          gap (32, 96, 160 B) so the `ctx-*` rung ladder has a matching
          arm that grows with the count.
  RUNS    homogeneous-CLASS runs -- random lowercase letters, random digits
          -- at lengths sitting exactly on the ladder's rungs and one off
          them (256/257 letters for the 256 rung; 16/17 and 27/28 digits
          for the nested rungs). They are the count ladder's MATCH-regime
          subjects: the exact count matches, one short fails at the last
          repetition, one long fails at the end anchor. The LARGE rungs
          (4096 .. 65535) get 4 KB / 16 KB / 64 KB runs in the `throughput`
          regime instead (gen_throughput_subjects.py), where find-all
          search drives each counter to its full value without a 16 KB
          subject sitting in a match set whose median is 40 B.

WHY THE RUNS ARE RANDOM WITHIN THE CLASS AND NOT A REPEATED BYTE. Inbox
I-10 / [B17]: a periodic subject flatters any per-byte number by making the
loop's one data-dependent branch perfectly predictable. A run of `a` has
period 1. A run of RANDOM letters is still every byte in `[a-z]` -- which is
all the class ladder tests -- and the manifest's `periodic` column
(`pcrecbench.periodic`, the same function every manifest uses) reads `no`
on every subject here. The price is that a LITERAL-body rung (`a{0,n}`)
has nothing here it matches at length: its row is the compile axis only,
and NOTES.md says so.

WHY THE RUN LENGTHS STOP WHERE THEY DO. A nested bounded repeat is
ambiguous -- a run of the body class decomposes into iterations many ways --
and a near-miss LONGER than the pattern's maximum makes a backtracking
engine try them all. MEASURED on the oracle while designing this set
(NOTES.md, "The runs and the oracle"): `(?:\\d{1,16}){1,16}` on 257 digits
and `(?:(?:\\d{1,4}){1,4}){1,4}` on 65 digits both exhaust PCRE2's match
limit (-47), and an expectation the oracle cannot state is a cell the
harness cannot judge. So the digit runs are 16/17 (the k=4 rung's exact and
near-miss), 27/28 (the triple k=3 rung's) and 256 (the k=16 rung's exact
maximum, and BELOW every larger rung's) -- near-misses exist only where the
oracle finishes them, and each one is stated per pattern in NOTES.md.

DETERMINISM. One primitive, `random.Random(seed).getrandbits(32)`, which
CPython documents as stable; `Rng` builds every draw on it. `choice`,
`sample`, `randrange`, `shuffle` are not used: their internals have moved
between CPython releases and a committed manifest cannot rest on that.
(The same posture, for the same reason, as bench/loglines/logtext.py.)
"""

import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

from pcrecbench.periodic import (periodic_field,  # noqa: E402,F401
                                 smallest_period)


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

    def letters(self, n):
        return "".join(self.pick("abcdefghijklmnopqrstuvwxyz") for _ in range(n))

    def digits(self, n):
        return "".join(self.pick("0123456789") for _ in range(n))

    def hexs(self, n):
        return "".join(self.pick("0123456789abcdef") for _ in range(n))

    def shuffled_indices(self, n):
        """Fisher-Yates over `below`, so an allocation without replacement
        does not go through `random.sample`."""
        idx = list(range(n))
        for i in range(n - 1, 0, -1):
            j = self.below(i + 1)
            idx[i], idx[j] = idx[j], idx[i]
        return idx


# ------------------------------------------------------------------ words

# Ops prose. NO word here is `fail`, `abort` or `panic` (the ctx triggers)
# nor `disk`, `memory`, `socket` or `quota` (the ctx context words): the
# background must not match a ctx rung by accident, and the near-miss forms
# below are what make the `\b` in those patterns do work.
WORDS = (
    "request", "handler", "worker", "queue", "retry", "backoff", "session",
    "token", "expired", "renewed", "cache", "miss", "hit", "flush", "commit",
    "rollback", "lease", "leader", "follower", "election", "snapshot",
    "compaction", "index", "segment", "replica", "shard", "route", "upstream",
    "downstream", "latency", "budget", "deadline", "exceeded", "throttled",
    "resumed", "paused", "drained", "scaled", "warmup", "cold", "start",
    "stop", "reload", "config", "applied", "rejected", "accepted", "pending",
    "ready", "healthy", "degraded", "recovered", "closing", "opened",
    "listening", "bound", "unbound", "attached", "detached", "mounted",
    "unmounted", "rotated", "archived", "restored", "verified", "checksum",
    "mismatch", "timeout", "refused", "denied", "granted", "elevated",
)

# NEAR-MISSES of the trigger and context words: each contains one as a
# SUBSTRING but not as a whole word, so `\bfail\b` etc. reject them.
NEAR_WORDS = ("failure", "failing", "aborted", "aborting", "panicked",
              "panics", "disks", "diskless", "memoryless", "sockets",
              "quotas", "socketpair")

TRIGGERS = ("fail", "abort", "panic")
CONTEXTS = ("disk", "memory", "socket", "quota")

HOSTS = ("web-07", "db-02", "cache-11", "edge-3", "batch-19", "auth-1",
         "proxy-4", "store-8")
PROCS = ("sshd", "nginx", "kubelet", "etcd", "postgres", "redis", "cron",
         "systemd", "journald", "containerd")
PATHS = ("/var/lib/data", "/srv/queue", "/opt/app/etc", "/tmp/spool",
         "/mnt/vol1", "/home/svc/.cache", "/run/lock", "/var/log/app")


def _number(rng):
    """1-3 digits: the near-miss of `\\d{4}` and of a 4-digit year."""
    return rng.digits(rng.between(1, 3))


def _hex_short(rng):
    """8-12 hex: the near-miss of `[0-9a-f]{32}`. Forced to carry a letter so
    an all-digit token is never a digit run longer than three (the `\\d{4}`
    near-miss rule above would otherwise be broken about once in 1e4)."""
    n = rng.between(8, 12)
    h = list(rng.hexs(n))
    h[rng.below(n)] = rng.pick("abcdef")
    return "".join(h)


def _version3(rng):
    """Three dotted parts: the near-miss of a dotted quad."""
    return "%s.%s.%s" % (_number(rng), _number(rng), _number(rng))


def _mac5(rng):
    """Five colon-hex groups: the near-miss of a six-group MAC."""
    return ":".join(rng.hexs(2) for _ in range(5))


def _timestamp(rng):
    """`Aug 29 14:03:11` -- month-name form, never a 4-digit year."""
    return "%s %02d %02d:%02d:%02d" % (
        rng.pick(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                  "Sep", "Oct", "Nov", "Dec")),
        rng.between(1, 28), rng.between(0, 23), rng.between(0, 59),
        rng.between(0, 59))


def token(rng):
    """One background token. Weighted toward words so a line reads as prose;
    every non-word token is a near-miss of some everyday shape."""
    k = rng.below(100)
    if k < 62:
        return rng.pick(WORDS)
    if k < 70:
        return rng.pick(NEAR_WORDS)
    if k < 78:
        return _number(rng)
    if k < 84:
        return _hex_short(rng)
    if k < 89:
        return _version3(rng)
    if k < 92:
        return _mac5(rng)
    if k < 96:
        return rng.pick(PATHS)
    return "pid=" + _number(rng)


def prefix(rng):
    return "%s %s %s[%s]:" % (_timestamp(rng), rng.pick(HOSTS),
                              rng.pick(PROCS), _number(rng))


def prose(rng, nbytes):
    """Background tokens, space-joined, until at least `nbytes` bytes."""
    out = []
    size = -1
    while size < nbytes:
        t = token(rng)
        out.append(t)
        size += len(t) + 1
    return " ".join(out)


# ------------------------------------------------------------ the shapes

def year4(rng):
    return "%d" % rng.between(1990, 2035)


def hex32(rng):
    h = list(rng.hexs(32))
    h[rng.below(32)] = rng.pick("abcdef")
    return "".join(h)


def dotted4(rng):
    return ".".join(str(rng.between(0, 255)) for _ in range(4))


def csv5(rng):
    return ",".join(rng.pick(WORDS) if rng.below(3) else _number(rng)
                    for _ in range(5))


def password(rng, n):
    """`n` printable bytes with letters, digits and punctuation mixed."""
    alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789!#%&*+-=?@_~")
    return "".join(rng.pick(alphabet) for _ in range(n))
