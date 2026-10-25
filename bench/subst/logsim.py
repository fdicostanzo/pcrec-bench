"""logsim.py -- the substitution set's Apache-combined access-log SIMULATOR.

A STREAM: `stream(n_lines)` yields the first `n_lines` lines of ONE infinite,
deterministic log, so every smaller subject is a byte PREFIX of every larger
one (`gen_subjects.py` writes `acc-small` and `acc-main` from the same
stream and `--check` proves the prefix property). Non-periodic by
construction at any size: the site model turns over every EPOCH_LINES lines
(new pages, new returning clients) and every line draws fresh randomness.

WHAT IT MODELS, and why it is a model and not a template. A real access log
is not i.i.d. lines: it is interleaved SESSIONS. A browser fetches a page
and then its stylesheet, favicon and images with the page as Referer and one
User-Agent; a crawler walks many pages with one agent; a feed reader polls
one URL; drive-by scanners fetch one URL and vanish. That structure is what
makes a real log so compressible (gzip -6 ~ 0.10, xz ~ 0.055 on the
reference) and gives it its field variety (1.7 k distinct client addresses
and ~560 distinct agents per 10 k lines), and a generator that draws every
field independently misses both by a factor of two. `calibrate.py` measures
exactly those properties against a real log (elastic/examples
apache_logs, see NOTES.md "Calibration") and the constants below were tuned
until they agreed within the stated tolerances.

ENGINE-NEUTRAL (R-BENCH-4): nothing here names a regex engine or knows a
case's pattern text. The PLANTED structures (the cases' by-design densities)
are named by their purpose below: the rare blocked path (case 2), the
e-mail address (case 5b), the multi-field URL mix (case 7). Everything else
is "natural" and calibrated against the reference.

DETERMINISM. `Rng` is `random.Random(seed).getrandbits` only, integer
arithmetic throughout (no float, no libm): bit-for-bit identical across
CPython versions and platforms, which a committed sha256 manifest needs.
"""
import bisect
import random

SEED = "b140-subst-0.1"

# ----------------------------------------------------------------- tunables
# (every constant here is a calibration knob; the table in
# docs/dev/measurements/2026-10-24-b140-subject-calibration/ is its audit)

EPOCH_LINES = 25_000          # the site/returning-client model turns over
DT_SAME = (0, 0, 0, 0, 0, 0, 0, 1)   # gap (s) when the line continues the previous line's session (a page and its assets load within a second)
DT_NEW_MAX = 113              # gap uniform in [5, DT_NEW_MAX] s when it does not (overall mean ~26 s)
START_EPOCH_DAY = 16801       # 2016-01-01 as days since 1970-01-01

# session-kind weights (per mille)

# planted densities (per mille of LINES) -- BY DESIGN, stated in NOTES.md
P_EMAIL = 50                  # case 5b: 1 line in 20
P_URL7 = 25                   # case 7: 1 line in 40
RARE_BLOCK = 10_000           # case 2: exactly one planted line per block

URL7_MIX = (("correct", 400), ("wrong", 250), ("missing_noq", 150),
            ("missing_q", 200))

#: THE CALIBRATION KNOBS (everything `calibrate.py` was tuned with). Plain
#: numbers read at stream time; per mille unless the name says otherwise.
K = {
    "MAX_ACTIVE": 5,          # interleaved sessions at once
    "P_STICK": 534,           # next line continues the same session
    "P_NEW_SESSION": 260,     # (of the rest) start a session
    "W_BROWSE": 313, "W_CRAWL": 42, "W_FEED": 249, "W_SINGLE": 560,
    "W_PAIR": 121, "W_HEAVY": 11,
    "P_BROWSE_TAIL": 110,     # a browse page view from the wide tail
    "RET_SHARE": 116,         # browse sessions by a returning client
    "REF_DASH": 57,           # percent: main-doc Referer is "-"
    "REF_SEARCH": 13,         # percent: a long search-engine Referer
    "M_304": 16, "M_206": 370,    # main doc: 304 revalidation / 206 ranged download (per mille)
    "A_304_SITE": 5, "A_304_DOC": 1, "A_304_HEAVY": 20, "FEED_304": 16,
    "S_404": 2,               # percent of drive-by extra paths that 404
    "UA_Q": 23, "UA_DEN": 10, "DOCS_Q": 120, "HOT_DOCS": 110, "N_AGENTS": 1573,
    "CRAWL_LONG": 19, "DOC_MOVED": 42, "DOC_MISSING": 22,
    "SLUG_WORDS": 105, "SLUG_MAXN": 2,
    "P1_0": 1, "TALK_IMG_MAX": 4, "SEARCH_PAD": 2,
    "HOST_ALT": 5,           # percent of sessions using the bare-host site URL
    "EXT_URL": 49,            # percent of external referrers that are a distinct page URL
    "P_TRACK": 18,            # per mille of main docs carrying a long tracking query
    "P_UTM_FEED": 23,         # per mille of main .html docs reached from a feed campaign
                # percent of browse sessions on HTTP/1.0
    "TS_NEW_MAX": 67,
}

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MDAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Rng:
    def __init__(self, seed):
        self._g = random.Random(seed).getrandbits

    def below(self, n):
        return self._g(48) % n

    def between(self, lo, hi):
        return lo + self._g(48) % (hi - lo + 1)

    def pick(self, seq):
        return seq[self._g(48) % len(seq)]

    def pm(self, per_mille):
        return self._g(32) % 1000 < per_mille

    def weighted(self, pairs):
        tot = sum(w for _, w in pairs)
        x = self._g(48) % tot
        for v, w in pairs:
            if x < w:
                return v
            x -= w
        return pairs[-1][0]


class Zipf:
    """Integer Zipf-Mandelbrot over ranks 0..n-1: weight 10**9 // (r + q)."""

    def __init__(self, n, q=1, den=1):
        """weight(r) = 10**9 / (r + q/den): the rational offset keeps the
        arithmetic integer."""
        acc = 0
        cdf = []
        for r in range(n):
            acc += 10 ** 9 * den // (den * r + q)
            cdf.append(acc)
        self.cdf = cdf
        self.total = acc

    def draw(self, rng):
        return bisect.bisect_right(self.cdf, rng._g(64) % self.total)


# --------------------------------------------------------------- vocabulary

TECH = ("logstash puppet kibana elastic grok fpm xdotool fedora yum dns dhcp "
        "nagios ruby python jruby redis rabbit syslog statsd graphite "
        "collectd ganglia cron bash vim tmux ssh zsh git svn mysql postgres "
        "nginx haproxy varnish docker ansible chef salt cfengine monit munin "
        "rsyslog snmp ldap kerberos bind dnsmasq iptables tcpdump strace "
        "dtrace perf gdb valgrind make autoconf cmake gcc llvm jenkins rpm "
        "deb apt vagrant kvm xen cloud metrics alerts queue broker parser "
        "filter plugin config deploy backup restore monitor tuning scaling "
        "cache index search shard replica cluster node client server proxy "
        "gateway router switch firewall vpn tunnel socket stream batch job "
        "task worker agent daemon service module package library release "
        "tutorial notes howto faq guide review slides talk paper demo "
        "example test bench report design spec draft patch fix bug issue "
        "ticket").split()
CATS = "web rants sysadmin unix code linux life tools".split()
EXTS_IMG = ("png", "png", "png", "jpg", "gif")
UTM_CAMPAIGNS = ("geekery", "sysadmin-feed", "unix-rants", "tools-feed", "web-feed", "all")
SITE_HOSTS = ("http://www.example.net", "http://example.net")
SITE_ASSETS = ("/favicon.ico", "/style2.css", "/reset.css",
               "/images/avatar-80.png", "/images/web/2012/banner.png")
SITE_ASSET_P = (960, 930, 930, 900, 880)   # per mille, first view of a session
FEEDS = ("/blog/tags/puppet?flav=rss20", "/?flav=rss20", "/?flav=atom",
         "/blog/tags/logstash?flav=rss20", "/blog/?flav=atom")
EXTERNAL_REFS = (
    "https://www.google.com/", "https://www.google.com/", "http://www.google.com/",
    "http://www.google.co.uk/", "http://www.google.de/", "http://www.google.fr/",
    "http://www.google.ca/", "https://www.google.de/", "http://www.bing.com/",
    "http://search.yahoo.com/", "http://stackoverflow.com/questions/1032/",
    "http://news.ycombinator.com/", "http://www.reddit.com/r/sysadmin/",
    "http://t.co/", "http://duckduckgo.com/", "http://www.baidu.com/",
    "http://planet.example.org/", "http://blog.example.org/links/",
    "http://wiki.example.com/Tools", "http://forum.example.com/t/174",
)

# Agent templates. %-fields are filled by `build_agents` from the stable
# agent RNG; the FORMS follow the real shapes that exist in the wild (the
# four-part legacy versions `rv:1.8.1.4` / `Firefox/2.0.0.4` are IPv4-shaped
# text, which is why they are here: a real log carries them).
_WIN = ("Windows NT 6.1; WOW64", "Windows NT 6.1; Win64; x64",
        "Windows NT 6.3; WOW64", "Windows NT 10.0; Win64; x64",
        "Windows NT 6.2; WOW64", "Windows NT 5.1")
_MAC = ("Macintosh; Intel Mac OS X 10_9_%d", "Macintosh; Intel Mac OS X 10_8_%d",
        "Macintosh; Intel Mac OS X 10_10_%d", "Macintosh; Intel Mac OS X 10_11_%d")
_LIN = ("X11; Linux x86_64", "X11; Ubuntu; Linux x86_64", "X11; Linux i686",
        "X11; Fedora; Linux x86_64")
_FEEDBOTS = (
    "UniversalFeedParser/4.2-pre-314-svn +http://feedparser.org/",
    "Tiny Tiny RSS/1.11 (http://tt-rss.org/)",
    "Feedly/1.0 (+http://www.feedly.com/fetcher.html; like FeedFetcher-Google)",
    "Apache-HttpClient/4.2.3 (java 1.5)",
    "NewsBlur Feed Fetcher - 3 subscribers - http://www.newsblur.com",
    "Python-urllib/2.7",
    "Liferea/1.8.12 (Linux; en_US.UTF-8; http://liferea.sf.net/)",
)
_CRAWLERS = (
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; AhrefsBot/5.0; +http://ahrefs.com/robot/)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/5.0 (compatible; Ezooms/1.0; +http://www.example.org/bot)",
    "Mozilla/5.0 (compatible; MJ12bot/v1.4.5; http://www.majestic12.co.uk/bot.php?+)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 "
    "(KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 "
    "(compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Exabot/3.0; +http://www.exabot.com/go/robot)",
    "Mozilla/5.0 (compatible; SeznamBot/3.2; +http://fulltext.sblog.cz/)",
    "curl/7.29.0", "Wget/1.15 (linux-gnu)", "-",
)


def build_agents(rng, n):
    """~n distinct browser agent strings, in a stable order (index = Zipf
    rank): the most common shapes first."""
    out = []
    seen = set()

    def add(s):
        if s not in seen:
            seen.add(s)
            out.append(s)

    chrome_maj = (32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46)
    ff_maj = (24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38)
    guard = 0
    while len(out) < n and guard < n * 20:
        guard += 1
        k = rng.below(100)
        if k < 40:                                            # Chrome
            osn = rng.pick(_WIN + _LIN + tuple(m % rng.between(0, 5) for m in _MAC)
                           ) if False else None
            kind = rng.below(10)
            if kind < 5:
                osn = rng.pick(_WIN)
            elif kind < 8:
                osn = rng.pick(_MAC) % rng.between(0, 5)
            else:
                osn = rng.pick(_LIN)
            add("Mozilla/5.0 (%s) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/%d.0.%d.%d Safari/537.36"
                % (osn, rng.pick(chrome_maj), rng.between(1500, 2700),
                   rng.between(1, 140)))
        elif k < 65:                                          # Firefox
            osn = rng.pick(_WIN + _LIN) if rng.below(10) < 7 else (
                rng.pick(_MAC) % rng.between(0, 5)).replace("Intel Mac OS X",
                                                              "Intel Mac OS X")
            mj = rng.pick(ff_maj)
            add("Mozilla/5.0 (%s; rv:%d.0) Gecko/20100101 Firefox/%d.0"
                % (osn, mj, mj))
        elif k < 75:                                          # Safari/mobile
            if rng.below(2):
                add("Mozilla/5.0 (%s) AppleWebKit/%d.%d (KHTML, like Gecko) "
                    "Version/%d.0.%d Safari/%d.%d.%d"
                    % (rng.pick(_MAC) % rng.between(0, 5), 537, rng.between(36, 78),
                       rng.between(6, 9), rng.between(0, 5), 537, rng.between(36, 78),
                       rng.between(1, 85)))
            else:
                add("Mozilla/5.0 (iPhone; CPU iPhone OS %d_%d like Mac OS X) "
                    "AppleWebKit/%d.%d (KHTML, like Gecko) Version/%d.0 "
                    "Mobile/%dA%d Safari/%d.%d"
                    % (rng.between(6, 9), rng.between(0, 3), 600, rng.between(1, 50),
                       rng.between(6, 9), rng.between(10, 12), rng.between(300, 5600),
                       rng.between(8500, 9500), rng.between(1, 30)))
        elif k < 85:                                          # MSIE / Trident
            if rng.below(2):
                add("Mozilla/5.0 (compatible; MSIE %d.0; %s; Trident/%d.0)"
                    % (rng.between(9, 11), rng.pick(_WIN), rng.between(5, 7)))
            else:
                add("Mozilla/5.0 (%s; Trident/7.0; rv:11.0) like Gecko"
                    % rng.pick(_WIN))
        elif k < 92:                                          # Android
            add("Mozilla/5.0 (Linux; Android %d.%d.%d; %s Build/%s) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%d.0.%d.%d "
                "Mobile Safari/537.36"
                % (rng.between(4, 6), rng.between(0, 4), rng.between(0, 3),
                   rng.pick(("Nexus 5", "GT-I9505", "SM-G900F", "HTC One", "XT1058")),
                   rng.pick(("KOT49H", "LRX21O", "JDQ39", "LMY47D")),
                   rng.pick(chrome_maj), rng.between(1500, 2700), rng.between(1, 140)))
        elif k < 96:                                          # legacy, 4-part versions
            add(rng.pick((
                "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1.4) "
                "Gecko/20070515 Firefox/2.0.0.4",
                "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19) "
                "Gecko/2010031422 Firefox/3.0.19",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) "
                "Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13",
                "Nokia6280/2.0 (03.60) Profile/MIDP-2.0 Configuration/CLDC-1.1 "
                "UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like "
                "Gecko) Chrome/17.0.963.79 Safari/535.11 CoolNovo/2.0.9.20")))
        else:                                                 # Opera / old MSIE
            add(rng.pick((
                "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.%d.%d Version/%d.%d"
                % (rng.between(8, 12), rng.between(100, 400), rng.between(10, 12),
                   rng.between(0, 62)),
                "Mozilla/4.0 (compatible; MSIE %d.0; Windows NT %d.%d; "
                ".NET CLR %d.%d.%d)" % (rng.between(6, 8), rng.between(5, 6),
                                        rng.between(0, 2), rng.between(1, 3),
                                        rng.between(0, 5), rng.between(1000, 50727)))))
    return out


# ---------------------------------------------------------------- the world

def _slug(rng, nmax=3, joiner=None):
    n = rng.between(1, min(nmax, K["SLUG_MAXN"]))
    j = joiner or rng.pick("--_")
    words = TECH[:K["SLUG_WORDS"]]
    return j.join(rng.pick(words) for _ in range(n))


class World:
    """The site at one epoch: its documents (a main path + embedded assets),
    the returning-client and external-referrer pools. The HEAD of each pool
    is shared by every epoch (the popular pages stay popular); the TAIL is
    re-drawn per epoch (the long tail turns over). Built from separate Rngs
    so the stream's own randomness never feeds the model."""

    DOCS = 1500
    HEAD = 150

    def __init__(self, epoch, agents, zipf_docs, zipf_ret, zipf_ua):
        self.epoch = epoch
        self.agents = agents
        self.zipf_docs = zipf_docs
        self.zipf_ret = zipf_ret
        self.zipf_ua = zipf_ua
        self.docs = []
        for i in range(self.DOCS):
            r = Rng("%s/doc/%s" % (SEED, ("h%d" % i) if i < self.HEAD
                                    else ("e%d.%d" % (epoch, i))))
            d = self._doc(r)
            x = r.below(1000)
            state = ("moved" if x < K["DOC_MOVED"] else
                     "missing" if x < K["DOC_MOVED"] + K["DOC_MISSING"] else "ok")
            self.docs.append(d + (state,))
        # returning clients: (ip, agent index) pairs, head shared
        self.returning = []
        for i in range(zipf_ret.n):
            r = Rng("%s/ret/%s" % (SEED, ("h%d" % i) if i < 40
                                    else ("e%d.%d" % (epoch, i))))
            self.returning.append((random_ip(r), zipf_ua.draw(r)))
        self.crawlers = []
        for i in range(24):
            r = Rng("%s/crawler/%d" % (SEED, i))
            self.crawlers.append((random_ip(r), _CRAWLERS[i % len(_CRAWLERS)],
                                  r.below(3) == 0))
        self.feedreaders = []
        for i in range(10):
            r = Rng("%s/feed/%d" % (SEED, i))
            self.feedreaders.append((random_ip(r), _FEEDBOTS[i % len(_FEEDBOTS)],
                                     FEEDS[i % len(FEEDS)]))

    def _doc(self, r):
        k = r.weighted((("talk", 300), ("post", 360), ("project", 70),
                        ("article", 50), ("tag", 70), ("file", 60),
                        ("hotlink", 25)))
        if k == "talk":
            slug = _slug(r, 2, "-") + "-" + str(r.between(2009, 2015))
            base = "/presentations/%s/" % slug
            assets = tuple("%simages/%s.%s" % (base, _slug(r, 2, "-"), r.pick(EXTS_IMG))
                           for _ in range(r.between(1, K["TALK_IMG_MAX"])))
            assets += tuple("%splugin/%s/%s.js" % (base, r.pick(TECH), r.pick(TECH))
                            for _ in range(r.between(0, 2)))
            return (base, assets, k)
        if k == "post":
            if r.below(3) == 0:
                name = "%d.html" % r.between(1, 480)
            else:
                name = _slug(r, 3) + ".html"
            main = "/blog/%s/%s" % (r.pick(CATS), name)
            assets = tuple("/images/%s.%s" % (_slug(r, 2, "-"), r.pick(EXTS_IMG))
                           for _ in range(r.between(0, 2) if r.below(100) < 35 else 0))
            return (main, assets, k)
        if k == "project":
            p = r.pick(TECH)
            main = "/projects/%s/" % p
            sub = tuple("/projects/%s/%s" % (p, r.pick(("index.html", "docs.html",
                                                          "changes.txt", "faq.html")))
                        for _ in range(r.between(0, 2)))
            return (main, sub, k)
        if k == "article":
            return ("/articles/%s/" % _slug(r, 3, "-"),
                    tuple("/articles/%s.%s" % (_slug(r, 2, "-"), r.pick(EXTS_IMG))
                          for _ in range(r.between(0, 2))), k)
        if k == "tag":
            return ("/blog/tags/%s" % r.pick(TECH), (), k)
        if k == "file":
            return ("/files/%s-%d.%d.%d.%s" % (
                r.pick(TECH), r.between(0, 3), r.between(0, 12), r.between(0, 9),
                r.pick(("tar.gz", "tar.gz", "jar", "zip", "rpm", "deb"))), (), k)
        return ("/images/%s-%d.%s" % (r.pick(TECH), r.between(1, 99), r.pick(EXTS_IMG)),
                (), k)


class _ZipfN(Zipf):
    def __init__(self, n, q, den=1):
        super().__init__(n, q, den)
        self.n = n


def random_ip(r):
    a = r.pick((r.between(1, 9), r.between(11, 126), r.between(128, 172),
                r.between(174, 191), r.between(193, 223), r.between(11, 223)))
    return "%d.%d.%d.%d" % (a, r.between(0, 255), r.between(0, 255),
                            r.between(1, 254))


def _b64(r, n):
    al = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    return "".join(al[r.below(64)] for _ in range(n))


def ext_ref(r):
    """An external referrer: a search-engine home page (a handful of
    variants) or a page on some other site (many distinct URLs)."""
    if r.below(100) >= K["EXT_URL"]:
        return r.pick(EXTERNAL_REFS)
    return "http://%s.example.%s/%s/%d" % (
        r.pick(("forum", "news", "wiki", "blog", "links", "planet", "reddit")),
        r.pick(("org", "com", "net", "io")), r.pick(TECH), r.between(1, 400))


def doc_status(dstate, dk, rng):
    """A document's status: its fixed state (moved / missing), else a cache
    revalidation (304) or a ranged download (206) for a fraction of views."""
    if dstate == "moved":
        return 301
    if dstate == "missing":
        return 404
    x = rng.below(1000)
    if x < K["M_304"] and dk != "tag":
        return 304
    if dk == "file" and x < K["M_206"]:
        return 206
    return 200


def host_url(r):
    return SITE_HOSTS[0] if r.below(100) >= K["HOST_ALT"] else SITE_HOSTS[1]


SEARCH_PADS = ("", "&biw=1280&bih=720&sa=X",
               "&biw=1280&bih=720&sa=X&sqi=2&tbm=isch&source=lnms&dpr=1")


def search_ref(r):
    """A long search-engine results referrer (the real log's ~3 % of lines
    with a 200-300 byte Referer)."""
    pad = SEARCH_PADS[K["SEARCH_PAD"]]
    if r.below(2):
        return ("https://www.google.com/imgres?imgurl=http%%3A%%2F%%2Fwww.example.net%%2Fimages%%2F%s.png"
                "&imgrefurl=http%%3A%%2F%%2Fwww.example.net%%2Fblog%%2F%s.html&tbnid=%s&docid=%s"
                "&w=%d&h=%d&ei=%s&zoom=1&iact=rc&dur=%d&page=1&start=0&ndsp=%d&ved=0C%s"
                % (_slug(r, 2, "-"), _slug(r, 2, "-"), _b64(r, 14), _b64(r, 14),
                   r.between(200, 1200), r.between(150, 900), _b64(r, 22),
                   r.between(100, 2000), r.between(20, 60), _b64(r, 9))) + pad
    return ("http://www.google.com/url?sa=t&rct=j&q=%s&esrc=s&source=web&cd=%d&ved=0C%s"
            "&url=http%%3A%%2F%%2Fwww.example.net%%2F%s%%2F&ei=%s&usg=AFQjC%s"
            % ("+".join(r.pick(TECH) for _ in range(r.between(1, 4))), r.between(1, 9),
               _b64(r, 8), _slug(r, 2, "-"), _b64(r, 20), _b64(r, 32))) + pad


# ---------------------------------------------------------- planted strings

EMAIL_USERS = ("alice", "bob.smith", "carol_jones", "dave99", "erin.o.neil",
               "frank", "grace.h", "heidi_m", "ivan.p", "judy.k", "mallory",
               "niaj", "olivia.d", "peggy", "sybil.t", "trent", "wendy.w",
               "info", "sales.team", "j.doe", "m.curie", "a.turing", "d.knuth")
EMAIL_DOMS = ("example.com", "example.org", "mail.example.net", "corp.example.com",
              "students.example.edu", "example.co.uk", "mx.example.de", "example.io",
              "post.example.fr", "example.nl")
URL7_NAMES = ("acme", "globex", "initech", "umbrella", "hooli")
URL7_TLDS = ("com", "de", "fr", "nl", "org")
URL7_PATHS = ("shop", "cart", "checkout", "p/item", "catalog/new", "deals", "ref/partner")
URL7_FIELDS = ("a=1", "utm_source=news", "cid=7731", "page=2", "sort=price", "lang=en")
RARE_PATHS = ("/phpmyadmin/index.php", "/phpmyadmin/setup.php",
              "/wp-admin/admin.php", "/wp-admin/install.php",
              "/phpmyadmin/scripts.php", "/wp-admin/upgrade.php")


def url7(r):
    """-> (url, kind) one of the four case-7 populations."""
    kind = r.weighted(URL7_MIX)
    name, tld = r.pick(URL7_NAMES), r.pick(URL7_TLDS)
    path = r.pick(URL7_PATHS)
    base = "https://www.%s.%s/%s" % (name, tld, path)
    others = [r.pick(URL7_FIELDS) for _ in range(r.between(1, 2))]
    if len(others) == 2 and others[0] == others[1]:
        others = others[:1]
    other_tlds = [t for t in URL7_TLDS if t != tld]
    if kind == "correct":
        pos = r.below(3)
        f = ["tld=" + tld]
        if pos == 0:
            fields = f + others
        elif pos == 1:
            fields = others + f
        else:
            fields = f
        return base + "?" + "&".join(fields), kind
    if kind == "wrong":
        wrong = r.pick(other_tlds) if r.below(5) else r.pick(("xx", "uk", "dex", "c"))
        f = ["tld=" + wrong]
        pos = r.below(3)
        if pos == 0:
            fields = f + others
        elif pos == 1:
            fields = others + f
        else:
            fields = f
        return base + "?" + "&".join(fields), kind
    if kind == "missing_noq":
        return base, kind
    return base + "?" + "&".join(others), kind


def email(r):
    return "%s@%s" % (r.pick(EMAIL_USERS), r.pick(EMAIL_DOMS))


# ------------------------------------------------------------------ streams

def _day_to_ymd(days):
    y = 1970
    while True:
        leap = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0
        yl = 366 if leap else 365
        if days < yl:
            break
        days -= yl
        y += 1
    m = 0
    while True:
        ml = MDAYS[m] + (1 if (m == 1 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)) else 0)
        if days < ml:
            return y, m, days + 1
        days -= ml
        m += 1


class Planted:
    """Counts of what the stream planted (oracle-independent)."""
    KEYS = ("rare", "email", "url7_correct", "url7_wrong", "url7_missing_noq",
            "url7_missing_q")

    def __init__(self):
        self.n = dict.fromkeys(self.KEYS, 0)
        self.kind_lines = {}          # lines per session kind (calibration aid)


def stream(n_lines, planted=None):
    """Yield the first `n_lines` lines (bytes, each ending b"\\n")."""
    if planted is None:
        planted = Planted()
    cnt = planted.n
    agents_rng = Rng(SEED + "/agents")
    agents = build_agents(agents_rng, K["N_AGENTS"])
    zipf_docs = _ZipfN(World.DOCS, K["DOCS_Q"])          # wide: crawlers, drive-bys
    zipf_crawl = _ZipfN(24, 2)
    zipf_feed = _ZipfN(10, 1)
    zipf_heavy = _ZipfN(60, 1)
    zipf_hot = _ZipfN(K["HOT_DOCS"], 1)                  # the pages people read
    zipf_ret = _ZipfN(420, 2)
    zipf_ua = _ZipfN(len(agents), K["UA_Q"], K["UA_DEN"])
    # ret pool uses agent indices
    rng = Rng(SEED + "/stream")
    prng = Rng(SEED + "/plant")      # planting never perturbs the natural draws
    ts = START_EPOCH_DAY * 86400 + 10 * 3600
    day_cache = {}
    world = None
    world_epoch = -1
    active = []
    cur = None
    rare_pos = {}

    def req_bytes(path, kind_hint, cache):
        b = cache.get(path)
        if b is None:
            h = sum(path.encode()) * 2654435761 % (1 << 32)
            bits = {"css": (9, 11), "js": (10, 14), "img": (10, 17),
                    "doc": (11, 15), "file": (16, 22), "ico": (11, 12)}[kind_hint]
            hb = (h >> 3) % (bits[1] - bits[0] + 1) + bits[0]
            b = (1 << hb) + (h * 40503 >> 5) % (1 << hb)
            cache[path] = b
        return b

    size_cache = {}

    def kind_of(path):
        if path.endswith((".css",)):
            return "css"
        if path.endswith(".js"):
            return "js"
        if path.endswith(".ico"):
            return "ico"
        if path.endswith((".png", ".jpg", ".gif")):
            return "img"
        if path.endswith((".tar.gz", ".jar", ".zip", ".rpm", ".deb")):
            return "file"
        return "doc"

    def new_session(w):
        k = rng.weighted((("browse", K["W_BROWSE"]), ("crawl", K["W_CRAWL"]),
                          ("feed", K["W_FEED"]), ("single", K["W_SINGLE"]),
                          ("pair", K["W_PAIR"]), ("heavy", K["W_HEAVY"])))
        q = []          # queue of (method, path, status, bytes_or_None, ref)
        if k == "browse":
            if rng.below(1000) < K["RET_SHARE"]:
                ip, ai = w.returning[zipf_ret.draw(rng)]
                ua = agents[ai]
            else:
                ip = random_ip(rng)
                ua = agents[zipf_ua.draw(rng)]
            proto = "HTTP/1.1" if rng.below(100) >= K["P1_0"] else "HTTP/1.0"
            host = SITE_HOSTS[0] if rng.below(100) >= K["HOST_ALT"] else SITE_HOSTS[1]
            first = True
            ref_prev = None
            for _v in range(1 + (rng.below(100) < 30) + (rng.below(100) < 10)
                            + (rng.below(100) < 4)):
                main, assets, dk, dstate = w.docs[zipf_docs.draw(rng) if rng.below(1000)
                                                  < K["P_BROWSE_TAIL"] else zipf_hot.draw(rng)]
                if dk == "hotlink":
                    ref = ext_ref(rng)
                    q.append(("GET", main, 200, None, ref))
                    continue
                if ref_prev is not None and rng.below(100) < 80:
                    ref = ref_prev
                else:
                    x = rng.below(100)
                    ref = "-" if x < K["REF_DASH"] else (search_ref(rng) if x < K["REF_DASH"] + K["REF_SEARCH"] else ext_ref(rng))
                st = doc_status(dstate, dk, rng)
                if rng.below(1000) < K["P_UTM_FEED"] and main.endswith(".html"):
                    main = main + "?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+" + rng.pick(UTM_CAMPAIGNS)
                if rng.below(1000) < K["P_TRACK"] and "?" not in main:
                    main = main + "?utm_source=" + rng.pick(("newsletter", "twitter", "feedburner")) + "&utm_medium=" + rng.pick(("email", "social", "feed")) + "&utm_campaign=" + _slug(rng, 3, "_") + "&gclid=" + _b64(rng, rng.between(40, 90))
                q.append(("GET", main, st, None, ref))
                page_url = host + main
                if first:
                    for ap, pp in zip(SITE_ASSETS, SITE_ASSET_P):
                        if rng.below(1000) < pp:
                            q.append(("GET", ap, 304 if rng.below(100) < K["A_304_SITE"] else 200,
                                      None, page_url))
                for ap in assets:
                    q.append(("GET", ap, 304 if rng.below(100) < K["A_304_DOC"] else 200,
                              None, page_url))
                first = False
                ref_prev = page_url
            return [ip, ua, proto, q, k]
        if k == "crawl":
            ip, ua, h10 = w.crawlers[zipf_crawl.draw(rng)]
            proto = "HTTP/1.0" if h10 else "HTTP/1.1"
            if rng.below(100) < 18:
                q.append(("GET", "/robots.txt", 200, None, "-"))
            for _v in range(rng.between(2, 40) if rng.below(100) >= K["CRAWL_LONG"] else rng.between(40, 140)):
                main, assets, dk, dstate = w.docs[zipf_docs.draw(rng)]
                st = doc_status(dstate, dk, rng)
                q.append(("GET" if rng.below(1000) < 990 else "HEAD", main, st, None, "-"))
            return [ip, ua, proto, q, k]
        if k == "feed":
            ip, ua, fp = w.feedreaders[zipf_feed.draw(rng)]
            for _v in range(rng.between(1, 3)):
                q.append(("GET", fp, 304 if rng.below(100) < K["FEED_304"] else 200, None, "-"))
            return [ip, ua, "HTTP/1.1" if rng.below(100) < 70 else "HTTP/1.0", q, k]
        if k == "heavy":
            # a returning power user: many page views, mostly cached assets
            ip, ai = w.returning[zipf_heavy.draw(rng)]
            ua = agents[ai]
            host = host_url(rng)
            ref_prev = None
            for _v in range(rng.between(3, 12)):
                main, assets, dk, dstate = w.docs[zipf_docs.draw(rng) if rng.below(1000)
                                                  < 300 else zipf_hot.draw(rng)]
                if dk == "hotlink":
                    continue
                st = doc_status(dstate, dk, rng)
                q.append(("GET", main, 304 if st == 200 and rng.below(100) < K["A_304_HEAVY"] else st,
                          None, ref_prev or "-"))
                page_url = host + main
                for ap in assets:
                    q.append(("GET", ap, 304 if rng.below(100) < K["A_304_HEAVY"] else 200,
                              None, page_url))
                ref_prev = page_url
            if not q:
                q.append(("GET", SITE_ASSETS[0], 304, None, "-"))
            return [ip, ua, "HTTP/1.1", q, k]
        if k == "pair":
            # a link checker / preview fetcher: a page and one asset, or HEAD+GET
            ip = random_ip(rng)
            ua = agents[zipf_ua.draw(rng)]
            main, assets, dk, dstate = w.docs[zipf_docs.draw(rng)]
            q.append(("GET", main, doc_status(dstate, dk, rng), None, "-"))
            q.append(("GET", SITE_ASSETS[0], 200, None, host_url(rng) + main))
            return [ip, ua, "HTTP/1.1" if rng.below(100) < 80 else "HTTP/1.0", q, k]
        # single drive-by
        ip = random_ip(rng)
        if rng.below(100) < 6:
            ua = rng.pick(_CRAWLERS)
        else:
            ua = agents[zipf_ua.draw(rng)]
        main, assets, dk, dstate = w.docs[zipf_docs.draw(rng)]
        path = main
        x = rng.below(100)
        if x < 12:
            path = rng.pick(("/wp-login.php", "/xmlrpc.php", "/administrator/index.php",
                             "/.env", "/cgi-bin/test.cgi", "/user/login", "/admin/"))
        elif x < 40 and assets:
            path = rng.pick(assets)
        st = doc_status(dstate, dk, rng) if path == main else (200 if rng.below(100) >= K["S_404"] else 404)
        if path in ("/wp-login.php", "/xmlrpc.php", "/administrator/index.php",
                    "/.env", "/cgi-bin/test.cgi", "/user/login", "/admin/"):
            st = 404 if rng.below(4) else 200
        ref = "-" if rng.below(100) < 70 else ext_ref(rng)
        q.append(("GET", path, st, None, ref))
        return [ip, ua, "HTTP/1.1" if rng.below(100) < 90 else "HTTP/1.0", q, "single"]

    for i in range(n_lines):
        epoch = i // EPOCH_LINES
        if epoch != world_epoch:
            world = World(epoch, agents, zipf_docs, zipf_ret, zipf_ua)
            world_epoch = epoch
            size_cache = {}
        same = cur is not None and rng.below(1000) < K["P_STICK"]
        ts += rng.pick(DT_SAME) if same else rng.between(5, K["TS_NEW_MAX"])
        days, sod = divmod(ts, 86400)
        dstr = day_cache.get(days)
        if dstr is None:
            y, m, d = _day_to_ymd(days)
            dstr = "%02d/%s/%d" % (d, MONTHS[m], y)
            day_cache[days] = dstr
        stamp = "%s:%02d:%02d:%02d +0000" % (dstr, sod // 3600, sod // 60 % 60, sod % 60)
        # --- case 2: exactly one planted blocked-path line per RARE_BLOCK
        blk = i // RARE_BLOCK
        pos = rare_pos.get(blk)
        if pos is None:
            rr = Rng("%s/rare/%d" % (SEED, blk))
            pos = rr.below(RARE_BLOCK)
            rare_pos[blk] = pos
        if i % RARE_BLOCK == pos:
            rr = Rng("%s/rareline/%d" % (SEED, blk))
            cnt["rare"] += 1
            line = '%s - - [%s] "GET %s HTTP/1.1" 404 %d "-" "%s"\n' % (
                random_ip(rr), stamp, rr.pick(RARE_PATHS), rr.between(200, 520),
                rr.pick(_CRAWLERS[10:] + ("Mozilla/5.0 (compatible; zgrab/0.x)",)))
            yield line.encode("ascii")
            continue
        if same:
            s = cur
        elif not active or (len(active) < K["MAX_ACTIVE"]
                            and rng.below(1000) < K["P_NEW_SESSION"]):
            s = new_session(world)
            active.append(s)
        else:
            s = active[rng.below(len(active))]
        cur = s
        method, path, status, _b, ref = s[3].pop(0)
        planted.kind_lines[s[4]] = planted.kind_lines.get(s[4], 0) + 1
        if not s[3]:
            active.remove(s)
            cur = None
        # bytes: fixed per path; 304 carries "-"; some 200s "-"
        if status == 304 or (status == 200 and rng.below(1000) < 20):
            nbytes = "-"
        elif status == 404:
            nbytes = str(300 + (sum(path.encode()) % 40))
        elif status == 301:
            nbytes = str(320 + (sum(path.encode()) % 30))
        else:
            nbytes = str(req_bytes(path, kind_of(path), size_cache))
        # --- planted: e-mail (case 5b) and the case-7 URL mix
        e = prng.below(1000)
        if e < P_EMAIL:
            addr = email(prng)
            cnt["email"] += 1
            if prng.below(2):
                path = path + ("&" if "?" in path else "?") + prng.pick(
                    ("contact", "email", "mail", "to")) + "=" + addr
            else:
                ref = "http://www.example.net/%s?%s=%s" % (
                    prng.pick(("contact", "unsubscribe", "signup", "feedback")),
                    prng.pick(("email", "mail", "addr")), addr)
        elif e < P_EMAIL + P_URL7:
            ref, kind = url7(prng)
            cnt["url7_" + kind] += 1
        line = '%s - - [%s] "%s %s %s" %d %s "%s" "%s"\n' % (
            s[0], stamp, method, path, s[2], status, nbytes, ref, s[1])
        yield line.encode("ascii")
