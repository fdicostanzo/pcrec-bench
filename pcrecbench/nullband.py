"""nullband.py -- [B79] THE NULL-CONTROL BAND's arithmetic (reader side).

`docs/design/null_band_v1.md` is the design note; inbox I-93 block B and
I-104 are the ask. Pure functions only: `report.py` gathers the cells and
renders; this module decides nothing about which records are in a report.

THE BAND. Between two pins of one engine config, the cells whose artifact
is PROGRAM-IDENTICAL on both sides (`tools/program_identity.py`'s census,
`reports/identity/...`) moved only because the WINDOW moved -- a Δ there
is the between-window noise the D119 bar's within-window IQR cannot see
(pcrec's cycle2 reading §1: up to +41% at floor scale on cells whose
program did not change). The band is computed per STRATUM = (regime,
baseline scale), baseline scale from the BEFORE (older pin) set-grain
median:

    >=1us       median >= 1,000 ns
    100ns-1us   100 <= median < 1,000 ns
    <100ns      median < 100 ns

and is SYMMETRIC: its half-width is the largest |Δ%| any null cell of the
stratum reached (pcrec's own "worst null cell" reading, I-104's worked
example). A real cell must move further than every no-change cell of its
own regime and scale did.

THE BAR (D119, restated per I-93/I-104):  |Δ%| > max(IQR%, band)
    Δ%   = (after_median - before_median) / before_median * 100
    IQR% = before-side Type-7 IQR of the per-trial set sums / before_median
           * 100 (the ledgers' own "before-IQR" reading; for 5 trials
           x3 - x1 of the sorted sums)

THE SUFFICIENCY THRESHOLD, `N_MIN = 10`. The half-width is a sample
maximum; for exchangeable null cells the chance that one more null cell
exceeds the maximum of n is 1/(n+1). At n = 10 that is <= 9.1% -- the
loosest bound this project is willing to call a noise floor; below it
the stratum is INSUFFICIENT and says so by name (`insufficient (n=K <
10)`, or `empty (n=0)`), its band is never used, and every verdict in it
is rendered `...(IQR only: band n=K < 10)` -- a stated fallback, never a
silent one.
"""

import math

N_MIN = 10

SCALE_BINS = (">=1us", "100ns-1us", "<100ns")


def scale_bin(median_ns):
    if median_ns >= 1000.0:
        return ">=1us"
    if median_ns >= 100.0:
        return "100ns-1us"
    return "<100ns"


def type7_quantile(xs, q):
    """Hyndman-Fan Type 7 (numpy's default, the ledgers' own)."""
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return None
    if n == 1:
        return s[0]
    h = (n - 1) * q
    lo = math.floor(h)
    hi = min(lo + 1, n - 1)
    return s[lo] + (h - lo) * (s[hi] - s[lo])


def iqr(xs):
    if not xs or len(xs) < 2:
        return None
    return type7_quantile(xs, 0.75) - type7_quantile(xs, 0.25)


def delta_pct(before, after):
    if not before:
        return None
    return (after - before) / before * 100.0


class Stratum:
    __slots__ = ("regime", "scale", "deltas", "n", "lo", "median", "hi",
                 "half_width", "status")

    def __init__(self, regime, scale, deltas, n_min=N_MIN):
        self.regime = regime
        self.scale = scale
        self.deltas = sorted(deltas)
        self.n = len(self.deltas)
        if self.n:
            self.lo = self.deltas[0]
            self.hi = self.deltas[-1]
            self.median = type7_quantile(self.deltas, 0.5)
            self.half_width = max(abs(self.lo), abs(self.hi))
        else:
            self.lo = self.hi = self.median = self.half_width = None
        if self.n == 0:
            self.status = "empty"
        elif self.n < n_min:
            self.status = "insufficient"
        else:
            self.status = "ok"

    @property
    def usable(self):
        return self.status == "ok"

    def status_text(self, n_min=N_MIN):
        if self.status == "ok":
            return "ok"
        if self.status == "empty":
            return "empty (n=0)"
        return f"insufficient (n={self.n} < {n_min})"


def build_strata(null_cells, regimes, n_min=N_MIN):
    """`null_cells`: iterable of (regime, before_median_ns, delta_pct).
    `regimes`: every regime the pair's cells span (so a regime with NO
    null cell still gets its three EMPTY strata printed). -> {(regime,
    scale): Stratum}, every (regime, scale) present."""
    buckets = {(r, s): [] for r in regimes for s in SCALE_BINS}
    for regime, before, d in null_cells:
        buckets.setdefault((regime, scale_bin(before)), []).append(d)
    return {k: Stratum(k[0], k[1], v, n_min) for k, v in buckets.items()}


def d119_verdict(delta, iqr_pct, stratum, n_min=N_MIN):
    """-> (verdict, bar_pct, bar_source). verdict in improve / regress /
    within, with the ` (IQR only: ...)` suffix when the stratum's band is
    not usable. `bar_source` names which term set the bar: `band`, `IQR`
    or `IQR-only`."""
    if stratum is not None and stratum.usable:
        band = stratum.half_width
        bar = max(iqr_pct, band)
        source = "band" if band >= iqr_pct else "IQR"
        suffix = ""
    else:
        bar = iqr_pct
        source = "IQR-only"
        n = stratum.n if stratum is not None else 0
        suffix = f" (IQR only: band n={n} < {n_min})"
    if delta > bar:
        v = "regress"
    elif delta < -bar:
        v = "improve"
    else:
        v = "within"
    return v + suffix, bar, source
