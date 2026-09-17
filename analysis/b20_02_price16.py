"""B20-02 pilot 3: PRICING ONLY (no rank is computed) for the sixteen-variable remainder of Candidate A.

Torus-weight block structure of
  M_5 = d_1^{(5)} : K_1(5) = C^16 (x) S_2  ->  S_5          (2176 x 15504; its left kernel is the quadratic syzygy space)
  D_8 = d_2^{(8)} : K_2(8) = Lambda^2 C^16 (x) S_2  ->  K_1(8) = C^16 (x) S_5   (16320 x 248064)
at det_4 (Z^4 x Z^4 row/column-sum grading) and at z per_3 (Z x Z^3 x Z^3 x Z^6 grading).
Basis element e_I (x) m gets weight w(m) + sum_{v in I} (w(F) - w(x_v)); every differential preserves it,
so each matrix is block-diagonal after sorting rows and columns by weight. This script counts the blocks.
"""
import argparse, itertools, json, math, os, sys, time
from collections import defaultdict

T0 = time.perf_counter()
ap = argparse.ArgumentParser()
ap.add_argument('--out', required=True)
args = ap.parse_args()
NV = 16

def monomials(nvars, deg):
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

# ---- weight systems ----
def w_det_var(v):          # x_v = x_{ij}, v = 4i + j
    i, j = divmod(v, 4)
    r = [0] * 4; c = [0] * 4; r[i] = 1; c[j] = 1
    return tuple(r + c)
W_DET_F = tuple([1] * 8)

def w_pad_var(v):          # x = (z, y_11..y_33, w_1..w_6)
    if v == 0:
        return tuple([1] + [0] * 12)
    if 1 <= v <= 9:
        a, b = divmod(v - 1, 3)
        r = [0] * 3; c = [0] * 3; r[a] = 1; c[b] = 1
        return tuple([0] + r + c + [0] * 6)
    ww = [0] * 6; ww[v - 10] = 1
    return tuple([0] * 7 + ww)
W_PAD_F = tuple([1] + [1] * 6 + [0] * 6)

def add(*ws):
    return tuple(sum(t) for t in zip(*ws))
def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def price(wvar, wF, label):
    out = {'label': label}
    mons2 = list(monomials(NV, 2)); mons5 = list(monomials(NV, 5))
    def wmon(m):
        return add(*[tuple(e * x for x in wvar(v)) for v, e in enumerate(m) if e]) if any(m) else tuple([0] * len(wF))
    w2 = {m: wmon(m) for m in mons2}
    w5 = {m: wmon(m) for m in mons5}
    shift1 = {v: sub(wF, wvar(v)) for v in range(NV)}
    # K_1(5) rows (v, m2); S_5 columns
    rows_M5 = defaultdict(int)
    for v in range(NV):
        for m in mons2:
            rows_M5[add(w2[m], shift1[v])] += 1
    cols_M5 = defaultdict(int)
    for m in mons5:
        cols_M5[w5[m]] += 1
    # K_2(8) rows (v<u, m2); K_1(8) columns (v, m5)
    rows_D8 = defaultdict(int)
    for v, u in itertools.combinations(range(NV), 2):
        s = add(shift1[v], shift1[u])
        for m in mons2:
            rows_D8[add(w2[m], s)] += 1
    cols_D8 = defaultdict(int)
    for v in range(NV):
        for m in mons5:
            cols_D8[add(w5[m], shift1[v])] += 1
    def summarize(rows, cols, name):
        blocks = [(rows[w], cols[w]) for w in rows if w in cols and rows[w] > 0 and cols[w] > 0]
        tot_entries = sum(r * c for r, c in blocks)
        big = max(blocks, key=lambda rc: rc[0] * rc[1]) if blocks else (0, 0)
        flops = sum(r * c * min(r, c) for r, c in blocks)
        return {'matrix': name, 'rows_total': sum(rows.values()), 'cols_total': sum(cols.values()),
                'dense_entries_unblocked': sum(rows.values()) * sum(cols.values()),
                'dense_bytes_unblocked_8B': 8 * sum(rows.values()) * sum(cols.values()),
                'n_blocks_nonempty': len(blocks), 'largest_block_rows_cols': list(big),
                'largest_block_bytes_8B': 8 * big[0] * big[1], 'sum_block_entries': tot_entries,
                'sum_block_bytes_8B': 8 * tot_entries, 'elimination_flops_upper_bound': flops,
                'rows_in_blocks_without_columns': sum(rows[w] for w in rows if cols.get(w, 0) == 0),
                'cols_in_blocks_without_rows': sum(cols[w] for w in cols if rows.get(w, 0) == 0)}
    out['M5'] = summarize(rows_M5, cols_M5, 'M_5 = d_1^{(5)}')
    out['D8'] = summarize(rows_D8, cols_D8, 'D_8 = d_2^{(8)}')
    return out

res = {'script': 'analysis/b20_02_price16.py', 'NV': NV, 'pricing_only': True, 'ranks_computed': False,
       'dimS2': math.comb(17, 15), 'dimS5': math.comb(20, 15), 'K2_8_rows': 120 * math.comb(17, 15), 'K1_8_cols': 16 * math.comb(20, 15)}
res['det4'] = price(w_det_var, W_DET_F, 'det_4, torus Z^4 x Z^4 (row and column sums)')
res['zper3'] = price(w_pad_var, W_PAD_F, 'z per_3, torus Z x Z^3 x Z^3 x Z^6')
res['wall_seconds'] = time.perf_counter() - T0
os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
with open(args.out, 'w') as fh:
    json.dump(res, fh, indent=1)
for name in ('det4', 'zper3'):
    for mat in ('M5', 'D8'):
        s = res[name][mat]
        print(name, mat, 'blocks', s['n_blocks_nonempty'], 'largest', s['largest_block_rows_cols'],
              'largest_MiB', round(s['largest_block_bytes_8B'] / 2**20, 2), 'sum_block_MiB', round(s['sum_block_bytes_8B'] / 2**20, 2),
              'unblocked_MiB', round(s['dense_bytes_unblocked_8B'] / 2**20, 1), 'flops_ub', s['elimination_flops_upper_bound'])
print(f'PRICING DONE {res["wall_seconds"]:.1f}s (no rank computed)')
