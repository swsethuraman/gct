#!/usr/bin/env python3
"""
Session 57 -- shared routines for the rank-loss selector.

Everything here is exact integer arithmetic.  Two independent routes exist for
the plethysm multiplicity a(lam, delta):

  * the Frobenius / Murnaghan-Nakayama route of the s39 C engine
    (wk9_s39_chars.PlethEngine, N = 4 delta <= 64), and
  * the Weyl-alternation route  a = sum_w sgn(w) K(w(lam+rho) - rho), with the
    weight multiplicity K by a tail DP.  The house tail DP is
    wk9_s42_census.N_S_tail_n (numpy int64); this file adds a SECOND tail DP,
    written from the generating function rather than ported, that runs mod two
    61-bit primes in uint64 and reconstructs by CRT (values are far below
    2^122).  The two DPs are asserted equal wherever both run.

The Weyl alternation itself is also re-implemented here (weyl_terms) rather than
imported, so that the modular route shares no code with wk9_s42_census except
the notion of a partition.

Cells, ladders, the region, the negative record, and the criteria of the
pre-registration are all defined here so that the table script, the ladder
script and the falsification script agree on every definition.
"""
import os, sys, re, json, csv, gzip, time
from math import factorial
from collections import Counter
from functools import lru_cache
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, HERE)

P1 = (1 << 61) - 1                 # 2^61 - 1 (Mersenne prime)
P2 = 2305843009213693921           # the prime below 2^61 used by the s39 engine
PRIMES = (P1, P2)

# ------------------------------------------------------------------ partitions
def partitions_exact(n, k, maxpart=None):
    """partitions of n into exactly k parts, each <= maxpart, descending tuples."""
    if maxpart is None: maxpart = n
    out = []
    def rec(rem, kk, mp, cur):
        if kk == 0:
            if rem == 0: out.append(tuple(cur))
            return
        lo = (rem + kk - 1) // kk
        hi = min(mp, rem - (kk - 1))
        for f in range(hi, lo - 1, -1):
            rec(rem - f, kk - 1, f, cur + [f])
    rec(n, k, maxpart, [])
    return out

def region_cells(delta, ell, n=4):
    """all lam |- n*delta with exactly ell parts and lam_1 >= delta (the brief's region)."""
    N = n * delta
    out = []
    for first in range(delta, N - ell + 2):
        for rest in partitions_exact(N - first, ell - 1, first):
            out.append((first,) + rest)
    return out

@lru_cache(maxsize=None)
def count_exact(n, k, m):
    """number of partitions of n into exactly k parts each <= m."""
    if k == 0: return 1 if n == 0 else 0
    if n < k or m <= 0: return 0
    tot = 0
    for f in range((n + k - 1) // k, min(m, n - k + 1) + 1):
        tot += count_exact(n - f, k - 1, f)
    return tot

def count_region(delta, ell, n=4):
    N = n * delta
    return sum(count_exact(N - f, ell - 1, f) for f in range(delta, N - ell + 2))

def stab_order(lam):
    o = 1
    for v, k in Counter(lam).items(): o *= factorial(k)
    return o

def balance(lam): return lam[0] - lam[-1]

def tail_of(lam): return tuple(lam[1:])

def ladder_cell(tail, delta, n=4):
    """the cell of ladder `tail` at degree delta, or None if not a partition."""
    first = n * delta - sum(tail)
    if first < (tail[0] if tail else 0): return None
    return (first,) + tuple(tail)

def ladder_bottom_delta(tail, n=4):
    """least delta at which (n delta - |tail|, tail) is a partition with ell <= delta."""
    s = sum(tail); t1 = tail[0] if tail else 0
    d = 0
    while n * d - s < t1 or d < len(tail) + 1: d += 1
    return d

def eligible(lam, delta): return lam[0] >= delta

# ------------------------------------------------------ the modular tail DP (route 2)
def _tails(r, n):
    out = []
    def rec(k, left, cur):
        if k == r - 1: out.append(tuple(cur)); return
        for v in range(left + 1): rec(k + 1, left - v, cur + [v])
    rec(0, n, [])
    return out

_TAILS = {}
def tails(r, n=4):
    key = (r, n)
    if key not in _TAILS: _TAILS[key] = _tails(r, n)
    return _TAILS[key]

def K_mod(mu, delta, n, p):
    """weight multiplicity of Sym^delta(Sym^n C^r) at the composition mu, mod p.

    Generating function prod_{|alpha| = n} (1 - t x^alpha)^{-1}: the exponent of
    x_1 in each alpha is n - |beta| with beta the tail, so a monomial of weight
    mu is a delta-multiset of tails beta (|beta| <= n) with tail sum mu[1:]; the
    x_1 budget is then automatic when |mu| = n delta.  DP over (count, tail sum)."""
    mu = tuple(int(x) for x in mu); r = len(mu)
    if any(x < 0 for x in mu) or sum(mu) != n * delta: return 0
    tl = mu[1:]
    if r == 1: return 1
    shape = (delta + 1,) + tuple(t + 1 for t in tl)
    F = np.zeros(shape, dtype=np.uint64)
    F[(0,) * len(shape)] = 1
    pp = np.uint64(p)
    for beta in tails(r, n):
        if any(beta[i] > tl[i] for i in range(r - 1)): continue
        src = tuple(slice(0, tl[i] + 1 - beta[i]) for i in range(r - 1))
        dst = tuple(slice(beta[i], tl[i] + 1) for i in range(r - 1))
        for d in range(1, delta + 1):
            blk = F[(d,) + dst]
            blk += F[(d - 1,) + src]
            blk %= pp
    return int(F[(delta,) + tl])

def box_size(mu, delta):
    b = delta + 1
    for x in mu[1:]: b *= (int(x) + 1)
    return b

def sort_desc(mu): return tuple(sorted((int(x) for x in mu), reverse=True))

def weyl_terms(lam):
    """(sign, mu) over w in S_r with mu = w(lam + rho) - rho having all entries >= 0.
    Own enumeration: assign to each position i the value (lam+rho)_{sigma(i)}."""
    lam = tuple(lam); r = len(lam)
    rho = [r - 1 - i for i in range(r)]
    lr = [lam[i] + rho[i] for i in range(r)]
    out = []
    used = [False] * r
    perm = [0] * r
    def sign_of(pm):
        s = 1
        for i in range(r):
            for j in range(i + 1, r):
                if pm[i] > pm[j]: s = -s
        return s
    def rec(i):
        if i == r:
            mu = tuple(lr[perm[t]] - rho[t] for t in range(r))
            out.append((sign_of(perm), mu)); return
        for j in range(r):
            if not used[j] and lr[j] - rho[i] >= 0:
                used[j] = True; perm[i] = j
                rec(i + 1)
                used[j] = False
    rec(0)
    return out

def crt2(r1, r2):
    M = P1 * P2
    x = (r1 + P1 * (((r2 - r1) * pow(P1, -1, P2)) % P2)) % M
    return x if x <= M // 2 else x - M

def a_weyl_mod(lam, delta, n=4, cache=None, box_cap=None, terms_cap=None):
    """plethysm multiplicity by the Weyl alternation, each K mod two primes, CRT.
    Returns (a, nterms, ndistinct).  Raises MemoryError if a box exceeds box_cap
    or the number of surviving Weyl terms exceeds terms_cap."""
    lam = tuple(x for x in lam if x)
    acc = [0, 0]
    terms = weyl_terms(lam)
    if terms_cap is not None and len(terms) > terms_cap:
        raise MemoryError(f"{len(terms)} Weyl terms > cap")
    seen = {}
    for sgn, mu in terms:
        key = sort_desc(mu)          # K is symmetric under permutation of the weight
        if key not in seen:
            if cache is not None and (key, delta, n) in cache:
                seen[key] = cache[(key, delta, n)]
            else:
                if box_cap is not None and box_size(key, delta) > box_cap:
                    raise MemoryError(f"tail box {box_size(key, delta)} > cap for {key}")
                v = (K_mod(key, delta, n, P1), K_mod(key, delta, n, P2))
                seen[key] = v
                if cache is not None: cache[(key, delta, n)] = v
        v = seen[key]
        acc[0] = (acc[0] + sgn * v[0]) % P1
        acc[1] = (acc[1] + sgn * v[1]) % P2
    a = crt2(acc[0], acc[1])
    assert a >= 0, ("negative plethysm coefficient", lam, delta, a)
    return a, len(terms), len(seen)

def N_S_mod(lam, delta, n=4):
    """weight-space dimension N_S, exact by CRT of the two modular DPs."""
    return crt2(K_mod(lam, delta, n, P1), K_mod(lam, delta, n, P2))

def merged_lower_bound(lam, delta, n=4):
    """N_S(lam) >= N_S(mu) for the merged 5-part weight (dominance monotonicity, s42)."""
    lam = tuple(lam)
    if len(lam) <= 5: return N_S_mod(lam, delta, n)
    mu = tuple(lam[:4]) + (sum(lam[4:]),)
    return N_S_mod(mu, delta, n)

# ----------------------------------------------------------------- h_pad (s42 def.)
def pieri_strips(lam, delta):
    """nu with lam_{i+1} <= nu_i <= lam_i, |nu| = |lam| - delta (lam/nu a horizontal delta-strip)."""
    lam = tuple(lam); r = len(lam); target = sum(lam) - delta
    out = []
    def rec(i, cur, s):
        if s > target: return
        if i == r:
            if s == target: out.append(tuple(cur))
            return
        lo = lam[i + 1] if i + 1 < r else 0
        for v in range(lo, lam[i] + 1):
            rec(i + 1, cur + [v], s + v)
    rec(0, [], 0)
    return out

def h_pad_from_table(lam, delta, cubic):
    """h_pad = sum over Pieri strips nu of c_nu(Sym^delta(Sym^3)); `cubic` maps
    nu (no trailing zeros) -> coefficient (missing = 0)."""
    tot = 0
    for nu in pieri_strips(lam, delta):
        key = tuple(x for x in nu if x)
        tot += cubic.get(key, 0)
    return tot

def h_pad_weyl_mod(lam, delta, cache=None, box_cap=None, terms_cap=None):
    tot = 0
    for nu in pieri_strips(lam, delta):
        key = tuple(x for x in nu if x)
        if len(key) > delta: continue          # Sym^delta(Sym^3) has <= delta rows
        a3, _, _ = a_weyl_mod(key, delta, 3, cache, box_cap, terms_cap)
        tot += a3
    return tot

# ------------------------------------------------------------- the LMR shapes (F3)
def lmr_weight(k, d=4):
    """lambda(k, d) of LMR Thm 2.3.1 written as a partition; for d = 4:
    (8k+17, 2k+5, 2^{k+1}) at delta = 3(k+2).  Derived from
    Omega(k,d) = (d-1)(d-2)(k+2) w_1 + (d(k+2)-2k-5) w_2 + 2 w_{k+3}."""
    c1 = (d - 1) * (d - 2) * (k + 2); c2 = d * (k + 2) - 2 * k - 5; c3 = 2
    # fundamental weights -> partition: lam_i = sum_{j >= i} c_j over the w_j present
    parts = [c1 + c2 + c3, c2 + c3] + [c3] * (k + 1)
    delta = (k + 2) * (d - 1)
    assert sum(parts) == d * delta, (parts, delta)
    return tuple(parts), delta

def most_balanced_eligible(delta, ell, n=4, k=5):
    """the k most balanced (min lam_1 - lam_ell) cells of the region slice, ties by lam_1 then lex."""
    cells = region_cells(delta, ell, n)
    cells.sort(key=lambda l: (l[0] - l[-1], l[0], l))
    return cells[:k]

# --------------------------------------------------------------- the negative record
LAMRE = re.compile(r'`\((\s*\d+(?:\s*,\s*\d+)*)\s*\)`')

def _cells_from_md(path, col_lam, col_delta, col_a, col_mdet, fixed_delta_from_lam=False):
    """rows of a markdown ledger table -> (lam, delta, a, mult_det); indices are
    0-based over the '|'-split cells of the row."""
    out = []
    for ln in open(os.path.join(ROOT, path), encoding='utf-8'):
        s = ln.strip()
        if not s.startswith('|'): continue
        m = LAMRE.search(s)
        if not m: continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        lam = tuple(int(x) for x in m.group(1).split(','))
        try:
            a = int(cells[col_a].strip('`* '))
            md_raw = cells[col_mdet].strip('`* ')
            md = int(re.match(r'-?\d+', md_raw).group(0))
            delta = sum(lam) // 4 if fixed_delta_from_lam else int(cells[col_delta].strip('`* '))
        except (ValueError, IndexError, AttributeError):
            continue
        if sum(lam) != 4 * delta: continue
        out.append((lam, delta, a, md))
    return out

def negative_record():
    """every cell with a measured mult_det in the ledgers; returns dict
    (lam, delta) -> (a, mult_det, source).  Every row is checked mult_det == a
    by the caller."""
    rec = {}
    def add(rows, src):
        for lam, delta, a, md in rows:
            key = (lam, delta)
            if key in rec and rec[key][:2] != (a, md):
                raise ValueError(f"ledger disagreement at {key}: {rec[key]} vs {(a, md, src)}")
            rec.setdefault(key, (a, md, src))
    # s36 ledger: | stratum | lam | delta | ell | a | N_S | Stab | n_chi | rows | route | mult_det | ...
    add(_cells_from_md('results/s36_ledger.md', 1, 2, 4, 10), 's36_ledger')
    # s36 a=1 extension: | ell | delta | lam | a | N_S | n_chi | mult_det | mult_pad | mult_red | D |
    add(_cells_from_md('results/s36_aone.md', 2, 1, 3, 6), 's36_aone')
    # s41 / s43: | delta | lam | a | m_det | N_S | Stab | n_chi | rows | route | mult_det | ...
    add(_cells_from_md('results/s41_ledger.md', 1, 0, 2, 9), 's41')
    add(_cells_from_md('results/s43_ledger.md', 1, 0, 2, 9), 's43')
    # s45: | δ | λ | elig | bal | a | full-E | N_S | Stab | n_χ | rows | nnz | nnz/n_χ | nullity | mult_det | ...
    add(_cells_from_md('results/s45_ledger.md', 1, 0, 4, 13), 's45')
    # s46: | δ | λ | elig | bal | a | h_pad | N_S | Stab | n_χ | rows | nnz | nnz_c | level | nullity | mult_det | ...
    add(_cells_from_md('results/s46_ledger.md', 1, 0, 4, 14), 's46')
    # s52 ledger (jsonl)
    rows = []
    for ln in open(os.path.join(ROOT, 'results/s52_ledger.jsonl')):
        r = json.loads(ln)
        if r.get('mult_det') is None: continue
        rows.append((tuple(r['lam']), r['delta'], r['a'], r['mult_det']))
    add(rows, 's52')
    # s54 length-5 cells (jsonl)
    rows = []
    for d in (6, 7, 8, 9):
        for ln in open(os.path.join(ROOT, f'results/s54_cells_d{d}.jsonl')):
            r = json.loads(ln)
            if r.get('mult_det') is None: continue
            rows.append((tuple(r['lam']), r['delta'], r['a'], r['mult_det']))
    add(rows, 's54')
    return rec

# --------------------------------------------------------------- the s39 table
def load_s39():
    """results/longweight_screen.csv -> {(lam, delta): (a, m_det)} for a >= 1 cells,
    plus the set of a = 0 candidates."""
    vals, zeros = {}, set()
    with open(os.path.join(ROOT, 'results/longweight_screen.csv')) as fh:
        for r in csv.DictReader(fh):
            lam = tuple(int(x) for x in r['lam'].split('|')); d = int(r['delta'])
            a = int(r['a'])
            if a == 0: zeros.add((lam, d)); continue
            vals[(lam, d)] = (a, int(r['m_det']))
    return vals, zeros

# ------------------------------------------------------------------ banking
def bank_open(path):
    """append-only jsonl bank; returns (set of banked keys, file handle)."""
    keys = set()
    if os.path.exists(path):
        for ln in open(path):
            try: r = json.loads(ln)
            except json.JSONDecodeError: continue
            keys.add((tuple(r['lam']), r['delta'], r.get('col')))
    return keys, open(path, 'a')

def load_json_any(path, default=None):
    """read path if present, else path + '.gz' (the large analysis files are committed gzipped)."""
    if os.path.exists(path): return json.load(open(path))
    if os.path.exists(path + '.gz'):
        with gzip.open(path + '.gz', 'rt') as fh: return json.load(fh)
    return default

def gzip_copy(path):
    """write path + '.gz' beside path (for files over the commit limit)."""
    with open(path, 'rb') as fi, gzip.open(path + '.gz', 'wb') as fo: fo.write(fi.read())
    return os.path.getsize(path + '.gz')

def log(*a):
    print(time.strftime('%H:%M:%S'), *a, file=sys.stderr, flush=True)
