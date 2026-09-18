"""B22-01 step 4: the decisive run at the certified points (docs/b22_01_report.md sec. 1.3, sec. 4).

Modes (each launch is one wrapped piece, <= 60 s / 512 MiB, run name b22_01_p4_decide_<piece>):
  --piece 00                      G21 controls before any new point:
                                  (a) the six sealed values at P6 point 0 by the pinned runner at the slice form,
                                      stated as the identity  slice = det(g)^4 * full  (B21-10 R3/G21), 45 evaluations;
                                  (b) B20-01 pilot 3's flag point 0 replayed by the runner, 15 evaluations;
                                  (c) the relation residuals of every recorded row (arithmetic, no runner).
  --piece NN --points i j ...     the certified points p_i (0..69): F_1 = [u^11] and top = [u^12] of q3, q7, n02
                                  at (Z_1, Z_2, Z + u nu_1, u nu_2, u nu_3), u = 1..5 (15 evaluations per point).
  --final                         ranks and minors of the 140 x 3 rows; coordinates in the certified basis; the
                                  span control at the 10 recorded flag points; the top consistency on 70 rows.
The certificate (results/b22_01/p2_basis.json) is read against its sha256.  JSON written after every point.
Producer-only (G18)."""
import hashlib, json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
T0 = time.perf_counter(); DEADLINE = 52.0
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import b20_01_pinned as pin
import b20_01_flag as fl

OUTDIR = ROOT / 'results/b22_01'; DEC = OUTDIR / 'decide'; DEC.mkdir(parents=True, exist_ok=True)
CERT = OUTDIR / 'p2_basis.json'; CERT_SHA = '7162d852b4490d2f22702b9b974979e403dd0dfb8794cef92b6be894d9a66e79'
ALPHA, BETA = 265391, 275398
ORDER = ['q3', 'q7', 'n02']
args = sys.argv[1:]


def sha(b): return hashlib.sha256(b).hexdigest()
def left(): return DEADLINE - (time.perf_counter() - T0)


def load_cert():
    b = CERT.read_bytes(); assert sha(b) == CERT_SHA, 'certificate hash mismatch'
    return json.loads(b)


def load_runner_here():
    """As B21-01's loader, materialising the pinned runner/carrier under results/b22_01/pinned/."""
    PINDIR = OUTDIR / 'pinned'; PINDIR.mkdir(parents=True, exist_ok=True)
    cb, crec = pin.fetch('b18_02_carrier.py'); rb, rrec = pin.fetch('paired_runner.py')
    (PINDIR / 'b18_02_carrier.py').write_bytes(cb)
    src = rb.decode()
    old = "SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'"
    assert old in src
    (PINDIR / 'paired_runner.py').write_text(src.replace(old, "SRC = HERE / 'b18_02_carrier.py'"), newline='\n')
    sys.path.insert(0, str(PINDIR))
    import paired_runner as _pr
    patched = sha((PINDIR / 'paired_runner.py').read_bytes())
    assert patched == 'e7ba4ff7ab676a0fb259dd662397d3a52bdbbcc12604f16e292fe005fce210fc'
    return _pr, dict(carrier=crec, runner_original=rrec, runner_patched_sha256=patched, equals_b20_01_patched_runner=True,
                     materialised_under='results/b22_01/pinned/')


def vectors(pr, rec):
    p6b, r1 = pin.fetch('p6_basis.json'); n02b, r2 = pin.fetch('n02_definition.json')
    rec['inputs']['p6_basis.json'] = r1; rec['inputs']['n02_definition.json'] = r2
    p6 = json.loads(p6b); n02d = json.loads(n02b)
    def tup(blocks): return tuple(tuple(tuple(int(x) for x in s) for s in b) for b in blocks)
    V = {}
    for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
        V['q%d' % b['index']] = dict(pi=tup(b['pi']), rho=tup(b['rho']), order=order, order_rev=order)
    V['n02'] = dict(pi=tup(n02d['pi_ordered_blocks']), rho=tup(n02d['rho_ordered_blocks']),
                    order=tuple(n02d['hand_plan_column_order']), order_rev=tuple(n02d['hand_plan_column_order_transposed']))
    for d in V.values():
        assert tuple(pr.hand_plan(d['pi'], d['rho'])[0]) == d['order'] and tuple(pr.hand_plan(d['rho'], d['pi'])[0]) == d['order_rev']
    return V, p6


def make_qval(pr, rec):
    P = pr.P
    def qval(d, T):
        te = time.perf_counter()
        a, m1, _ = pr.evaluate_P(d['pi'], d['rho'], T, d['order']); b_, m2, _ = pr.evaluate_P(d['rho'], d['pi'], T, d['order_rev'])
        rec['runner_evaluations'] += 1; rec['runner_wall_s'] += time.perf_counter() - te; assert max(m1, m2) <= 4 ** 10
        return (a + b_) % P
    return qval


def flag_row(pr, qval, V, Z1, Z2, Z):
    """[u^11] and [u^12] of q3, q7, n02 at (Z1, Z2, Z + u nu_1, u nu_2, u nu_3); nodes u = 1..5 fix u^8..u^12 (G22)."""
    c = pr.c
    T = [c.column_tensor(fl.tuple_F(Z1, Z2, Z, 0, u), 5) for u in fl.NODES5]
    out = {}
    for name in ORDER:
        vals = [qval(V[name], t) for t in T]
        co = fl.vandermonde_solve(fl.NODES5, vals, [8, 9, 10, 11, 12])
        out[name] = dict(values_u1_to_5=vals, c=[co[d] for d in (8, 9, 10, 11, 12)])
    return dict(d11=[out[n]['c'][3] for n in ORDER], d12=[out[n]['c'][4] for n in ORDER], raw=out)


def piece_path(tag):
    p = DEC / ('piece_%s.json' % tag); assert not p.exists(), 'receipts and outputs are never overwritten (G10)'
    return p


if '--piece' in args:
    tag = args[args.index('--piece') + 1]
    OUT = piece_path(tag)
    pr, prrec = load_runner_here(); np = pr.np; P = pr.P; assert P == fl.P
    rec = dict(run='b22_01_p4_decide_%s' % tag, prime=P, code_pins=prrec, inputs={}, runner_evaluations=0, runner_wall_s=0.0, log=[],
               code={rel: sha((ROOT / rel).read_bytes()) for rel in ('analysis/b22_01_p4_decide.py', 'analysis/b20_01_flag.py', 'analysis/b20_01_pinned.py')})
    cert = load_cert(); rec['inputs']['certificate'] = dict(path='results/b22_01/p2_basis.json', sha256=CERT_SHA)
    def save(status):
        rec['status'] = status; rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
        OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')
    V, p6 = vectors(pr, rec); qval = make_qval(pr, rec)
    if tag == '00':
        # (a) six sealed values: slice = det(g)^4 * full  <=>  full = det(g)^{-4} * slice
        SEALED = dict(d11=[86170, 71919, 226580], d12=[376209, 469277, 41046])
        Y0 = np.array(p6['points_entries'][0], dtype=np.int64)
        assert fl.reconstruct(Y0)
        g, detg, Yt = fl.slice_form(Y0); Zs = fl.wprime_part(Yt)
        inv4 = pow(pow(detg, 4, P), P - 2, P)
        F = {n: [] for n in ORDER}; TOP = {n: [] for n in ORDER}
        for k in range(3):
            T = [pr.c.column_tensor(fl.tuple_F(Zs[0], Zs[1], Zs[2 + k], k, u), 5) for u in fl.NODES5]
            for name in ORDER:
                vals = [qval(V[name], t) for t in T]
                co = fl.vandermonde_solve(fl.NODES5, vals, [8, 9, 10, 11, 12])
                F[name].append(co[11]); TOP[name].append(co[12])
            save('a_k%d' % k)
        a = {}
        for i, name in enumerate(ORDER):
            s11 = sum(F[name]) % P; s12 = TOP[name][0]
            a[name] = dict(slice_sum_F=s11, slice_top=s12, top_equal_across_k=len(set(TOP[name])) == 1,
                           identity_d11=(s11 == pow(detg, 4, P) * SEALED['d11'][i] % P), identity_d12=(s12 == pow(detg, 4, P) * SEALED['d12'][i] % P),
                           full_d11=inv4 * s11 % P, full_d12=inv4 * s12 % P, sealed_d11=SEALED['d11'][i], sealed_d12=SEALED['d12'][i])
        rec['G21_six_sealed'] = dict(det_g=detg, det_g_inv4=inv4, per_vector=a,
                                     matched=sum(int(a[n]['full_d11'] == a[n]['sealed_d11']) + int(a[n]['full_d12'] == a[n]['sealed_d12']) for n in ORDER))
        save('a_done')
        # (b) B20-01 pilot 3 flag point 0, recorded rows
        p3 = json.loads((ROOT / 'results/b20_01/p3_flag_rows.json').read_bytes())
        rec['inputs']['p3_flag_rows.json'] = sha((ROOT / 'results/b20_01/p3_flag_rows.json').read_bytes())
        e = p3['new_points'][0]
        row = flag_row(pr, qval, V, np.array(e['Z1']), np.array(e['Z2']), np.array(e['Z']))
        rec['G21_p3_point0'] = dict(d11=row['d11'], d12=row['d12'], recorded_d11=e['row_d11'], recorded_d12=e['row_d12'],
                                   matched=sum(int(x == y) for x, y in zip(row['d11'] + row['d12'], e['row_d11'] + e['row_d12'])))
        save('b_done')
        # (c) every recorded row: relation residual n02 - alpha q3 - beta q7
        rows = [(r['label'], r['row']) for r in p3['inherited_rows']]
        for e in p3['new_points']:
            rows += [('b20_01_p3_pt%d_d11' % e['point'], e['row_d11']), ('b20_01_p3_pt%d_d12' % e['point'], e['row_d12'])]
        for pt in cert['points'][75:80]:
            rows += [(pt['label'] + '_d11', pt['recorded_d11']), (pt['label'] + '_d12', pt['recorded_d12'])]
        res = {lab: (r[2] - ALPHA * r[0] - BETA * r[1]) % P for lab, r in rows}
        rec['G21_recorded_rows'] = dict(rows=len(rows), residuals=res, all_zero=all(v == 0 for v in res.values()))
        save('done')
    else:
        idx = [int(x) for x in args[args.index('--points') + 1:]]
        rec['points'] = {}
        for i in idx:
            if left() < 9.0: rec['log'].append('deadline before point %d' % i); break
            pt = cert['points'][i]; assert pt['label'] == 'cert_%02d' % i
            row = flag_row(pr, qval, V, np.array(pt['Z1']), np.array(pt['Z2']), np.array(pt['Z']))
            row['relation_residual_d11'] = (row['d11'][2] - ALPHA * row['d11'][0] - BETA * row['d11'][1]) % P
            row['relation_residual_d12'] = (row['d12'][2] - ALPHA * row['d12'][0] - BETA * row['d12'][1]) % P
            rec['points'][str(i)] = row
            save('point_%d' % i)
        save('done')
    print(json.dumps({k: v for k, v in rec.items() if k in ('run', 'status', 'runner_evaluations', 'runner_wall_s', 'elapsed_s', 'log', 'G21_p3_point0')}
                     | ({'G21_six_sealed_matched': rec['G21_six_sealed']['matched'], 'G21_recorded_rows_all_zero': rec['G21_recorded_rows']['all_zero']} if tag == '00' else
                        {'residuals': {i: (r['relation_residual_d11'], r['relation_residual_d12']) for i, r in rec['points'].items()}}), indent=1, default=int))

elif '--final' in args:
    import numpy as np
    sys.path.insert(0, str(HERE)); import b22_01_typed_v2 as ty
    P = fl.P; assert ty.P == P
    OUT = piece_path('final')
    cert = load_cert()
    rec = dict(run='b22_01_p4_decide_final', prime=P, inputs=dict(certificate=dict(path='results/b22_01/p2_basis.json', sha256=CERT_SHA), pieces={}),
               code={rel: sha((ROOT / rel).read_bytes()) for rel in ('analysis/b22_01_p4_decide.py', 'analysis/b22_01_typed_v2.py', 'analysis/b20_01_flag.py')})
    N11, N12 = {}, {}
    for f in sorted(DEC.glob('piece_*.json')):
        if f.name in ('piece_00.json', 'piece_final.json'): continue
        b = f.read_bytes(); rec['inputs']['pieces'][f.name] = sha(b)
        for i, r in json.loads(b).get('points', {}).items():
            assert int(i) not in N11, 'point evaluated twice'
            N11[int(i)] = r['d11']; N12[int(i)] = r['d12']
    missing = [i for i in range(70) if i not in N11]
    rec['points_present'] = len(N11); rec['points_missing'] = missing
    assert not missing, 'not all 70 certified points evaluated'
    sel11 = [s for s in cert['selected'] if s['block_key'][0] == 11]; sel12 = [s for s in cert['selected'] if s['block_key'][0] == 12]
    assert len(sel11) == 70 and len(sel12) == 4
    E = np.array(cert['certificate']['E_rows_points_cols_patterns'], dtype=np.int64)
    rec['certificate_det_recomputed'] = ty.det_rows(E.tolist())
    assert rec['certificate_det_recomputed'] == cert['certificate']['det_own'] != 0
    A11 = np.array([N11[i] for i in range(70)], dtype=np.int64); A12 = np.array([N12[i] for i in range(70)], dtype=np.int64)
    rows = np.concatenate([A11, A12]) % P
    rec['rank_140x3_mod_P'] = fl.rank_mod(rows.tolist()); rec['rank_d11_rows'] = fl.rank_mod(A11.tolist()); rec['rank_d12_rows'] = fl.rank_mod(A12.tolist())
    minor = None
    if rec['rank_140x3_mod_P'] == 3:
        ech = ty.Echelon(3); pick = []
        for i, r in enumerate(rows.tolist()):
            if ech.add(r): pick.append(i)
            if len(pick) == 3: break
        minor = dict(rows=pick, det=ty.det_rows([rows[i].tolist() for i in pick]), det_b20_01_flag=fl.det_mod([rows[i].tolist() for i in pick]))
    rec['nonzero_3x3_minor'] = minor
    rec['relation_residuals_d11'] = [int((r[2] - ALPHA * r[0] - BETA * r[1]) % P) for r in A11.tolist()]
    rec['relation_residuals_d12'] = [int((r[2] - ALPHA * r[0] - BETA * r[1]) % P) for r in A12.tolist()]
    rec['d12_ratios'] = [[int(r[1] * ty.inv_mod(r[0]) % P), int(r[2] * ty.inv_mod(r[0]) % P)] if r[0] else None for r in A12.tolist()]
    # coordinates in the certified basis, and the span control at the 10 recorded flag points
    X11 = ty.solve_mod(E, A11)                                              # 70 x 3
    rec['coordinates_relation_residual'] = [int(x) for x in (X11[:, 2] - ALPHA * X11[:, 0] - BETA * X11[:, 1]) % P]
    H = np.array([[s['vec80'][70 + r] for s in sel11] for r in range(10)], dtype=np.int64)
    pred11 = (H @ X11) % P                                                  # entries < 70 P^2: exact in int64
    Tm = np.array([[s['vec80'][i] for s in sel12] for i in range(80)], dtype=np.int64)
    mrows = cert['certificate']['top_minor_rows']
    Y12 = ty.solve_mod(Tm[mrows], A12[mrows])                               # 4 x 3
    pred12_all = (Tm @ Y12) % P
    rec_pts = cert['points'][70:80]
    span = []
    for r, pt in enumerate(rec_pts):
        span.append(dict(label=pt['label'], predicted_d11=[int(x) for x in pred11[r]], recorded_d11=pt['recorded_d11'],
                         predicted_d12=[int(x) for x in pred12_all[70 + r]], recorded_d12=pt['recorded_d12'],
                         match_d11=[int(x) for x in pred11[r]] == pt['recorded_d11'], match_d12=[int(x) for x in pred12_all[70 + r]] == pt['recorded_d12']))
    rec['span_control'] = span
    rec['span_control_matches'] = dict(d11=sum(3 * int(s['match_d11']) for s in span), d12=sum(3 * int(s['match_d12']) for s in span), of=30)
    rec['top_consistency_70_rows'] = dict(rows_matching=int(sum(int((pred12_all[i] == A12[i] % P).all()) for i in range(70))), of=70, minor_rows=mrows)
    passed = (rec['span_control_matches']['d11'] == 30 and rec['span_control_matches']['d12'] == 30 and rec['top_consistency_70_rows']['rows_matching'] == 70)
    rec['controls_passed'] = passed
    if not passed:
        rec['verdict'] = 'CONTROL FAILED: the certified basis does not reproduce recorded values; no transcription'
    elif minor and minor['det']:
        rec['verdict'] = 'rank(C|_U) = 3 over Q (nonzero 3x3 minor mod P of integer rows): the identity is FALSE'
    elif rec['rank_140x3_mod_P'] == 2 and all(v == 0 for v in rec['relation_residuals_d11'] + rec['relation_residuals_d12']):
        rec['verdict'] = 'rank(C|_U (x) F_P) = 2: the identity holds modulo P as a polynomial identity (CERTIFIED-modular)'
    else:
        rec['verdict'] = 'UNEXPECTED: rank %d with nonzero relation residuals' % rec['rank_140x3_mod_P']
    rec['elapsed_s'] = round(time.perf_counter() - T0, 3)
    OUT.write_text(json.dumps(rec, indent=1, default=int) + '\n')
    print(json.dumps({k: rec[k] for k in ('verdict', 'rank_140x3_mod_P', 'rank_d11_rows', 'rank_d12_rows', 'nonzero_3x3_minor', 'span_control_matches',
                                          'top_consistency_70_rows', 'controls_passed', 'elapsed_s')}, indent=1, default=int))
