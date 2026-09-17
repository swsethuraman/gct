"""B20-02b pilot 1: exact blockwise rank over Q of D_8 = d_2^{(8)} and M_5 = d_1^{(5)} in sixteen variables,
at det_4 and z per_3, using the torus-weight block decomposition (report Lemmas 2.1, 2.2).

d_2(e_v ^ e_u (x) m) = f_v m e_u - f_u m e_v   (v < u),   d_1(e_v (x) m) = f_v m,   f_v = d_v F.
Weight of e_I (x) m: w(m) + sum_{v in I} (w(F) - w(x_v)). Each block is built as fmpz_mat (tall form) and its
exact rank taken; a block above FALLBACK_ENTRIES would use one modular floor (flagged). JSON rewritten every
200 blocks. Every input file read is hashed into the output.
"""
import argparse, hashlib, itertools, json, math, os, sys, time
from collections import defaultdict
import flint

T0 = time.perf_counter()
NV = 16
FALLBACK_ENTRIES = 250_000
PRIME = 2147483647
ap = argparse.ArgumentParser()
ap.add_argument('--out', required=True)
ap.add_argument('--points', default='det4,zper3')
ap.add_argument('--matrices', default='M5,D8')
args = ap.parse_args()

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()

PINS = {os.path.join('results', 'b20_02b', 'inputs', 'p3_price16_blocks.json'): '54838ca647397a331f6d79586a2d0b4b49d39ed6ea3958d15ab30c14b6ee254a',
        os.path.join('results', 'b20_02b', 'inputs', 'p3_koszul2_exact.json'): 'a83162c2941e1305440cce11ebccdb181408d7471c7dd113ec4be3aeb0f0f151'}
inputs = {}
for p, expect in PINS.items():
    h = sha256(p)
    inputs[p.replace('\\', '/')] = {'sha256': h, 'expected': expect, 'match': h == expect}
    if h != expect:
        print('PIN MISMATCH', p, h, file=sys.stderr); sys.exit(3)
with open(os.path.join('results', 'b20_02b', 'inputs', 'p3_price16_blocks.json')) as fh:
    PRICE = json.load(fh)
with open(os.path.join('results', 'b20_02b', 'inputs', 'p3_koszul2_exact.json')) as fh:
    P3 = json.load(fh)

res = {'script': 'analysis/b20_02b_d8_blockwise.py', 'argv': sys.argv[1:], 'NV': NV, 'inputs_sha256': inputs,
       'flint_version': flint.__version__, 'python': sys.version.split()[0], 'fallback_entries': FALLBACK_ENTRIES,
       'prime_for_fallback': PRIME, 'checks': [], 'results': {}}

def monomials(nvars, deg):
    if nvars == 1:
        yield (deg,)
        return
    for a in range(deg, -1, -1):
        for rest in monomials(nvars - 1, deg - a):
            yield (a,) + rest

def poly_det4():
    F = defaultdict(int)
    for perm in itertools.permutations(range(4)):
        sgn = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if perm[i] > perm[j]:
                    sgn = -sgn
        e = [0] * NV
        for i in range(4):
            e[4 * i + perm[i]] += 1
        F[tuple(e)] += sgn
    return dict(F)

def poly_zper3():
    F = defaultdict(int)
    for perm in itertools.permutations(range(3)):
        e = [0] * NV
        e[0] += 1
        for a in range(3):
            e[1 + 3 * a + perm[a]] += 1
        F[tuple(e)] += 1
    return dict(F)

def partial(F, i):
    G = defaultdict(int)
    for e, cf in F.items():
        if e[i] > 0:
            e2 = list(e); e2[i] -= 1
            G[tuple(e2)] += cf * e[i]
    return dict(G)

# ---- weight systems (Lemma 2.1) ----
def w_det_var(v):
    i, j = divmod(v, 4)
    r = [0] * 4; c = [0] * 4; r[i] = 1; c[j] = 1
    return tuple(r + c)
W_DET_F = tuple([1] * 8)

def w_pad_var(v):
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

def dimS(m):
    return math.comb(m + NV - 1, NV - 1) if m >= 0 else 0

def write_out():
    res['wall_seconds_so_far'] = time.perf_counter() - T0
    with open(args.out, 'w') as fh:
        json.dump(res, fh, indent=1)

def block_rank(nrows, ncols, entries):
    """Exact rank over Q of a sparse block; tall orientation."""
    transposed = ncols > nrows
    R, C = (ncols, nrows) if transposed else (nrows, ncols)
    if R * C > FALLBACK_ENTRIES:
        M = flint.nmod_mat(R, C, PRIME)
        for (r, c), v in entries.items():
            rr, cc = (c, r) if transposed else (r, c)
            M[rr, cc] = v % PRIME
        return M.rank(), 'floor_mod_p'
    M = flint.fmpz_mat(R, C)
    for (r, c), v in entries.items():
        rr, cc = (c, r) if transposed else (r, c)
        M[rr, cc] = v
    return M.rank(), 'exact_Q_fmpz'

def run_point(name, F, wvar, wF):
    parts = [partial(F, v) for v in range(NV)]
    shift = {v: sub(wF, wvar(v)) for v in range(NV)}
    zero_w = tuple([0] * len(wF))
    def wmon(m):
        ws = [tuple(e * x for x in wvar(v)) for v, e in enumerate(m) if e]
        return add(*ws) if ws else zero_w
    mons2 = list(monomials(NV, 2)); mons5 = list(monomials(NV, 5))
    w2 = {m: wmon(m) for m in mons2}; w5 = {m: wmon(m) for m in mons5}
    out = {}
    for mat in args.matrices.split(','):
        t_mat = time.perf_counter()
        rows_by_w = defaultdict(list); cols_by_w = defaultdict(dict)
        if mat == 'M5':
            for v in range(NV):
                for m in mons2:
                    rows_by_w[add(w2[m], shift[v])].append((v, m))
            for m in mons5:
                d = cols_by_w[w5[m]]; d[m] = len(d)
            def row_images(key):
                v, m = key
                for e, cf in parts[v].items():
                    yield tuple(a + b for a, b in zip(e, m)), cf
            n_rows_expected, n_cols_expected = NV * dimS(2), dimS(5)
        elif mat == 'D8':
            for v, u in itertools.combinations(range(NV), 2):
                s = add(shift[v], shift[u])
                for m in mons2:
                    rows_by_w[add(w2[m], s)].append((v, u, m))
            for v in range(NV):
                for m in mons5:
                    d = cols_by_w[add(w5[m], shift[v])]; d[(v, m)] = len(d)
            def row_images(key):
                v, u, m = key
                for e, cf in parts[v].items():          # + f_v m e_u
                    yield (u, tuple(a + b for a, b in zip(e, m))), cf
                for e, cf in parts[u].items():          # - f_u m e_v
                    yield (v, tuple(a + b for a, b in zip(e, m))), -cf
            n_rows_expected, n_cols_expected = math.comb(NV, 2) * dimS(2), NV * dimS(5)
        else:
            raise SystemExit('unknown matrix ' + mat)
        n_rows = sum(len(r) for r in rows_by_w.values()); n_cols = sum(len(c) for c in cols_by_w.values())
        blocks = []; total_rank = 0; n_exact = 0; n_floor = 0; largest = (0, 0); grading_violations = 0
        weights = [w for w in rows_by_w if w in cols_by_w]
        rows_without_cols = sum(len(rows_by_w[w]) for w in rows_by_w if w not in cols_by_w)
        for bi, w in enumerate(weights):
            rkeys = rows_by_w[w]; cidx = cols_by_w[w]
            entries = defaultdict(int)
            for r, key in enumerate(rkeys):
                for ckey, cf in row_images(key):
                    if ckey not in cidx:
                        grading_violations += 1
                        raise SystemExit(f'GRADING VIOLATION in {name} {mat}: row {key} hits column {ckey} of another weight')
                    entries[(r, cidx[ckey])] += cf
            entries = {kk: v for kk, v in entries.items() if v}
            rk, method = block_rank(len(rkeys), len(cidx), entries)
            total_rank += rk
            n_exact += method == 'exact_Q_fmpz'; n_floor += method == 'floor_mod_p'
            if len(rkeys) * len(cidx) > largest[0] * largest[1]:
                largest = (len(rkeys), len(cidx))
            blocks.append({'weight': list(w), 'rows': len(rkeys), 'cols': len(cidx), 'nnz': len(entries), 'rank': rk, 'method': method})
            if (bi + 1) % 200 == 0:
                out[mat] = {'partial': True, 'blocks_done': bi + 1, 'rank_so_far': total_rank}
                res['results'][name] = out; write_out()
                print(name, mat, 'blocks', bi + 1, '/', len(weights), 'rank so far', total_rank, f't={time.perf_counter()-T0:.1f}s', flush=True)
        out[mat] = {'partial': False, 'rank_Q': total_rank, 'rows': n_rows, 'cols': n_cols,
                    'rows_expected': n_rows_expected, 'cols_expected': n_cols_expected,
                    'kernel_dim': n_rows - total_rank, 'n_blocks': len(weights), 'n_blocks_exact': n_exact, 'n_blocks_floor': n_floor,
                    'largest_block_rows_cols': list(largest), 'rows_in_weights_without_columns': rows_without_cols,
                    'grading_violations': grading_violations, 'seconds': time.perf_counter() - t_mat, 'blocks': blocks}
        res['results'][name] = out; write_out()
        print(name, mat, 'rank_Q', total_rank, 'rows', n_rows, 'cols', n_cols, 'kernel', n_rows - total_rank,
              'blocks', len(weights), 'exact', n_exact, 'floor', n_floor, 'largest', largest, f't={time.perf_counter()-T0:.1f}s', flush=True)
    return out

points = {'det4': (poly_det4(), w_det_var, W_DET_F), 'zper3': (poly_zper3(), w_pad_var, W_PAD_F)}
for name in args.points.split(','):
    F, wvar, wF = points[name]
    run_point(name, F, wvar, wF)

# ---- generic maximum and checks (emitted) ----
dimK2_8 = math.comb(NV, 2) * dimS(2); dimK3_8 = math.comb(NV, 3) * dimS(-1)
rho2_8 = dimK2_8 - dimK3_8 + math.comb(NV, 4) * dimS(-4)
res['rho_2_8'] = rho2_8; res['dimK2_8'] = dimK2_8; res['dimK3_8'] = dimK3_8
R = res['results']
def get(name, mat, key):
    return R.get(name, {}).get(mat, {}).get(key)
for name in R:
    for mat in R[name]:
        s = R[name][mat]
        res['checks'].append({'name': f'{name} {mat}: row and column totals over weight buckets equal the full dimensions',
                              'pass': s.get('rows') == s.get('rows_expected') and s.get('cols') == s.get('cols_expected')})
        res['checks'].append({'name': f'{name} {mat}: every block exact over Q (no modular fallback)', 'pass': s.get('n_blocks_floor') == 0})
        res['checks'].append({'name': f'{name} {mat}: no grading violation', 'pass': s.get('grading_violations') == 0})
if get('det4', 'M5', 'rank_Q') is not None:
    res['checks'].append({'name': 'det4 M5: kernel (quadratic syzygies) = 464 as recorded', 'pass': get('det4', 'M5', 'kernel_dim') == 464, 'value': get('det4', 'M5', 'kernel_dim')})
if get('zper3', 'M5', 'rank_Q') is not None:
    res['checks'].append({'name': 'zper3 M5: kernel (quadratic syzygies) = 932 as recorded', 'pass': get('zper3', 'M5', 'kernel_dim') == 932, 'value': get('zper3', 'M5', 'kernel_dim')})
if get('det4', 'D8', 'rank_Q') is not None and get('zper3', 'D8', 'rank_Q') is not None:
    rd, rp = get('det4', 'D8', 'rank_Q'), get('zper3', 'D8', 'rank_Q')
    res['comparison_D8'] = {'rank_det4': rd, 'rank_zper3': rp, 'rho_2_8': rho2_8, 'deficiency_det4': rho2_8 - rd, 'deficiency_zper3': rho2_8 - rp,
                            'reversal_rank_zper3_gt_rank_det4': rp > rd, 'det4_deficient': rd < rho2_8}
    res['checks'].append({'name': 'D8: both ranks <= rho_2(8)', 'pass': rd <= rho2_8 and rp <= rho2_8})
    print('COMPARISON', json.dumps(res['comparison_D8']))
res['wall_seconds'] = time.perf_counter() - T0
res['all_checks_pass'] = all(c['pass'] for c in res['checks'])
n_pass = sum(1 for c in res['checks'] if c['pass']); n_tot = len(res['checks'])
res['checks_passed_over_total'] = [n_pass, n_tot]
write_out()
for c in res['checks']:
    print('PASS' if c['pass'] else 'FAIL', c['name'], c.get('value', ''))
print(f'checks passed {n_pass}/{n_tot}')
print('ALL PASS' if res['all_checks_pass'] else 'SOME CHECK FAILED', f'{res["wall_seconds"]:.1f}s')
