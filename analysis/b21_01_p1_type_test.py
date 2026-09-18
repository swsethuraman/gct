"""B21-01 pilot 1: the isotropic-type test of the pairing B (B20-01 section 4.5(c), reopening condition (c)).

Pre-registered question: do the type components of the tops t_i = Phi_i^{(6)} and the mixed parts
s_i = Phi_i^{(5)} of the four covariants force the degree-11 relation
    4 B(t_1, s_1) = alpha 2[B(t_1,s_2) + B(s_1,t_2)] + beta 2[B(t_3,s_2) + B(s_3,t_2)] ?

Stages, each saved to JSON as it completes:
  0  pins (G9/G10), and the G21 sealed replay: the six sealed rows at P6 point 0 recomputed from the
     recorded slice values of B20-01 pilot 2 with the CORRECTED normalisation det(g)^{-4} (B21-10 R3/R4).
  1  C7 replay: B(X, X') by definition (einsum) versus the four-term type formula, on every pair used.
  2  factorization control at the general point (direct_arc B.1): the twelve halves of q3, q7, n02
     recombine through B to the sealed P6 point 0 values 260975, 301718, 386346.
  3  flag point 0 (the slice form of P6 point 0): t and s of the twelve halves by three-node extraction
     (u-degrees 4, 5, 6 of the half-tensor at the F_1-tuple), type blocks, the relation, type split.
  4  runner cross-check at flag point 0: [u^11] and [u^12] of q3, q7, n02 by the pinned runner at five
     nodes (15 evaluations) versus the covariant route of stage 3.
  5  up to four further seeded flag-locus points (Z_1, Z_2, Z) in W'^3, same treatment as stage 3.

Everything here is producer-only (G18).  Two-column tests decide nothing about ker C.
"""
import hashlib, json, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import b20_01_pinned as pin
import b20_01_flag as fl
import b21_01_types as ty

T0 = time.perf_counter(); DEADLINE = 52.0
OUTDIR = ROOT / 'results/b21_01'; OUTDIR.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / 'p1_type_test.json'


def load_runner_here():
    """As b20_01_pinned.load_runner, but materialising into results/b21_01/pinned/.

    B20-01's packet is sealed: nothing under results/b20_01/ is written by this session.  The patched
    runner's sha256 is compared with the value B20-01's MANIFEST binds, a cross-packet control."""
    PINDIR = OUTDIR / 'pinned'; PINDIR.mkdir(parents=True, exist_ok=True)
    cb, crec = pin.fetch('b18_02_carrier.py'); rb, rrec = pin.fetch('paired_runner.py')
    (PINDIR / 'b18_02_carrier.py').write_bytes(cb)
    src = rb.decode()
    old = "SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'"
    assert old in src
    (PINDIR / 'paired_runner.py').write_text(src.replace(old, "SRC = HERE / 'b18_02_carrier.py'"), newline='\n')
    sys.path.insert(0, str(PINDIR))
    import paired_runner as _pr
    patched = hashlib.sha256((PINDIR / 'paired_runner.py').read_bytes()).hexdigest()
    return _pr, dict(carrier=crec, runner_original=rrec, runner_patched_sha256=patched,
                     patch='carrier path line replaced by SRC = HERE / b18_02_carrier.py (one line)',
                     equals_b20_01_patched_runner=(patched == 'e7ba4ff7ab676a0fb259dd662397d3a52bdbbcc12604f16e292fe005fce210fc'),
                     materialised_under='results/b21_01/pinned/ (results/b20_01/ is not written)')


pr, prrec = load_runner_here(); c = pr.c; np = pr.np; P = pr.P
assert P == fl.P == ty.P

ALPHA, BETA = 265391, 275398          # routeA section 5.3, replayed in arc_target C3 and direct_arc C.2
SEALED_D11 = [86170, 71919, 226580]   # full_P6pt0, f1_new_point_minor.py INH (s3_full_forbidden_rows.json)
SEALED_D12 = [376209, 469277, 41046]
ORDER = ['q3', 'q7', 'n02']
NODES3 = [1, 2, 3]; DEG3 = [4, 5, 6]          # half-tensor u-degrees at an F_1-tuple
SEED = 20260918

rec = dict(pilot='b21_01_p1_type_test', prime=P, seed=SEED, alpha_beta=[ALPHA, BETA],
           code_pins=prrec, inputs=dict(), counts=dict(), checks=dict(), points=[], log=[],
           half_tensor_calls=0, runner_evaluations=0, column_tensors=0,
           half_tensor_wall_s=0.0, runner_wall_s=0.0)


def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1, default=str) + '\n')


def left(): return DEADLINE - (time.perf_counter() - T0)


def get(name):
    b, r = pin.fetch(name); rec['inputs'][name] = r; return b


def pin_local(relpath, expect):
    import hashlib
    b = (ROOT / relpath).read_bytes(); h = hashlib.sha256(b).hexdigest()
    assert h == expect, (relpath, h, expect)
    rec['inputs'][relpath] = dict(path=relpath, sha256=h, bytes=len(b), source='B20-01 MANIFEST.json')
    return b


# ---------------------------------------------------------------- stage 0: pins and the G21 sealed replay
p6 = json.loads(get('p6_basis.json')); n02d = json.loads(get('n02_definition.json'))
for cert, sha in (('q3_definition.json', 'ac93ff59113a1aca83a3a8a2d5a2cd90b2de216be70c793ea5f242c887e8428e'),
                  ('q7_definition.json', '07d066b8f6aada7472e892801cbfd6f1a2708a3d592e18592d9996341af3a252'),
                  ('n02_ordering_hash.json', '34900ea600da8b9a20535988f0a0a6cd901d866cd90ae74699e2ba60de845166')):
    pin_local('results/b20_01/certificates/' + cert, sha)
p2 = json.loads(pin_local('results/b20_01/p2_reduction.json',
                          '6aa3e283f5d0bf39515656dc16375104530a8d651d2b809973c8028083beb812'))

detg = p2['slice_form']['det_g_mod_P']
dm4 = pow(pow(detg, 4, P), P - 2, P)                       # det(g)^{-4}, the corrected factor (B21-10 R3)
replay = []
for i, name in enumerate(ORDER):
    sumF = sum(p2['F_k'][name][str(k)]['coefficients']['11'] for k in range(3)) % P
    top = p2['F_k'][name]['0']['coefficients']['12']
    replay.append(dict(vector=name, degree=11, corrected=(dm4 * sumF) % P, sealed=SEALED_D11[i],
                       match=(dm4 * sumF) % P == SEALED_D11[i]))
    replay.append(dict(vector=name, degree=12, corrected=(dm4 * top) % P, sealed=SEALED_D12[i],
                       match=(dm4 * top) % P == SEALED_D12[i]))
rec['checks']['G21_sealed_replay'] = replay
rec['counts']['sealed_values_replayed'] = len(replay)
rec['counts']['sealed_values_matched'] = sum(1 for r in replay if r['match'])
rec['checks']['G21_sealed_replay_all_match'] = all(r['match'] for r in replay)
rec['checks']['det_g_inv4_mod_P'] = dm4
save('stage0_pins_and_sealed_replay')

# ---------------------------------------------------------------- patterns and halves
def tup(blocks): return [tuple(tuple(int(x) for x in s) for s in b) for b in blocks]
VEC = {}
for b, order in zip(p6['basis'], ((0, 1, 2, 3), (0, 2, 1, 3))):
    VEC['q%d' % b['index']] = dict(pi=tup(b['pi']), rho=tup(b['rho']), pairing=[tuple(x) for x in b['pairing']],
                                   order=order, order_rev=order)
VEC['n02'] = dict(pi=tup(n02d['pi_ordered_blocks']), rho=tup(n02d['rho_ordered_blocks']),
                  pairing=[tuple(x) for x in n02d['pairing']],
                  order=tuple(n02d['hand_plan_column_order']), order_rev=tuple(n02d['hand_plan_column_order_transposed']))
for d in VEC.values():
    assert tuple(pr.hand_plan(d['pi'], d['rho'])[0]) == tuple(d['order'])
    assert tuple(pr.hand_plan(d['rho'], d['pi'])[0]) == tuple(d['order_rev'])
H = {}
for name in ORDER:
    for hn, s in ty.halves(VEC[name]['pi'], VEC[name]['rho'], VEC[name]['pairing']).items():
        H[name + '_' + hn] = s
HNAMES = list(H)
rec['counts']['halves'] = len(HNAMES)
COV = {'Phi_1': 'q3_h1', 'Phi_2': 'q3_h2', 'Phi_3': 'q7_h1', 'Phi_4': 'n02_h1'}
rec['covariants'] = COV
EPSF = ty.balanced_float(c.EPS4)


def colten(T5):
    rec['column_tensors'] += 1
    return c.column_tensor(T5, 5)


def ht(arrF, hname):
    t = time.perf_counter()
    v, peak = ty.half_tensor(arrF, EPSF, H[hname])
    rec['half_tensor_calls'] += 1; rec['half_tensor_wall_s'] += time.perf_counter() - t
    return v, peak


# ---------------------------------------------------------------- stage 1+2: C7 replay and factorization control
def Bpair(LX, LY, X, Y, c7):
    """B via the four-term type formula, with the einsum definition asserted equal (C7 replay)."""
    total, parts = ty.B_types(LX, LY)
    if c7 is not None:
        d = ty.B_direct(X, Y); c7.append(total == d)
    return total, parts


Y0 = np.array(p6['points_entries'][0], dtype=np.int64)
arr0 = ty.col_arr(colten([Y0[i] for i in range(5)]))
c7flags = []
XG = {}
for hn in HNAMES:
    XG[hn], _ = ht(arr0, hn)
fact = {}
for name in ORDER:
    v = (ty.B_direct(XG[name + '_h1'], XG[name + '_h2']) + ty.B_direct(XG[name + '_h1t'], XG[name + '_h2t'])) % P
    sealed = (p6['basis_matrix_pair_by_point'][ORDER.index(name)][0] if name != 'n02'
              else n02d['values']['P6_points_0_to_4'][0])
    fact[name] = dict(recombined=v, sealed=sealed, match=v == sealed)
rec['checks']['factorization_control_general_point'] = fact
rec['checks']['factorization_control_all_match'] = all(d['match'] for d in fact.values())
rec['counts']['factorization_values_checked'] = len(fact)
# type-formula replay on the general-point halves
LG = {hn: ty.lam(XG[hn]) for hn in HNAMES}
for name in ORDER:
    Bpair(LG[name + '_h1'], LG[name + '_h2'], XG[name + '_h1'], XG[name + '_h2'], c7flags)
    Bpair(LG[name + '_h1t'], LG[name + '_h2t'], XG[name + '_h1t'], XG[name + '_h2t'], c7flags)
del arr0, XG, LG
save('stage2_factorization_control')

# ---------------------------------------------------------------- the per-point type computation
def zero_blocks(L):
    return {'%d%d' % (ta + 1, tb + 1): bool(np.all(L[ta, :, tb, :] % P == 0)) for ta in range(2) for tb in range(2)}


def block_ranks(L):
    return {'%d%d' % (ta + 1, tb + 1): fl.rank_mod([[int(x) for x in row] for row in L[ta, :, tb, :]])
            for ta in range(2) for tb in range(2)}


def combine(terms):
    """terms: list of (coefficient, (total, parts)).  Returns (total, parts) of the linear combination."""
    tot = 0; parts = {k: 0 for k in ('11x22', '12x21', '21x12', '22x11')}
    for co, (t, p) in terms:
        tot = (tot + co * t) % P
        for k in parts: parts[k] = (parts[k] + co * p[k]) % P
    return tot, parts


def do_point(label, Z1, Z2, Z, want_c7):
    """t and s of the twelve halves at the F_1-tuple (Z1, Z2, Z + u nu_1, u nu_2, u nu_3); the relation."""
    vals = {hn: [] for hn in HNAMES}
    for u in NODES3:
        arrF = ty.col_arr(colten(fl.tuple_F(Z1, Z2, Z, 0, u)))
        for hn in HNAMES:
            v, _ = ht(arrF, hn); vals[hn].append(v)
        del arrF
    T = {}; S = {}
    for hn in HNAMES:
        co = ty.vander_solve_vec(NODES3, DEG3, vals[hn])
        T[hn] = co[6]; S[hn] = co[5]
    LT = {hn: ty.lam(T[hn]) for hn in HNAMES}; LS = {hn: ty.lam(S[hn]) for hn in HNAMES}
    cf = c7flags if want_c7 else None

    # (A) direct form: q = B(X_h1, X_h2) + B(X_h1t, X_h2t), no coordinate assumption
    z11d = {}; z12d = {}
    for name in ORDER:
        a, b_, at, bt = (name + '_h1', name + '_h2', name + '_h1t', name + '_h2t')
        z12d[name] = combine([(1, Bpair(LT[a], LT[b_], T[a], T[b_], cf)), (1, Bpair(LT[at], LT[bt], T[at], T[bt], cf))])
        z11d[name] = combine([(1, Bpair(LT[a], LS[b_], T[a], S[b_], cf)), (1, Bpair(LS[a], LT[b_], S[a], T[b_], cf)),
                              (1, Bpair(LT[at], LS[bt], T[at], S[bt], cf)), (1, Bpair(LS[at], LT[bt], S[at], T[bt], cf))])
    # (B) Phi form of direct_arc C.3, the form the pre-registered question is about
    t1, t2, t3 = (COV['Phi_1'], COV['Phi_2'], COV['Phi_3'])
    z12p = dict(q3=combine([(2, Bpair(LT[t1], LT[t2], T[t1], T[t2], None))]),
                q7=combine([(2, Bpair(LT[t3], LT[t2], T[t3], T[t2], None))]),
                n02=combine([(2, Bpair(LT[t1], LT[t1], T[t1], T[t1], None))]))
    z11p = dict(q3=combine([(2, Bpair(LT[t1], LS[t2], T[t1], S[t2], None)), (2, Bpair(LS[t1], LT[t2], S[t1], T[t2], None))]),
                q7=combine([(2, Bpair(LT[t3], LS[t2], T[t3], S[t2], None)), (2, Bpair(LS[t3], LT[t2], S[t3], T[t2], None))]),
                n02=combine([(4, Bpair(LT[t1], LS[t1], T[t1], S[t1], None))]))

    def residual(d):
        return combine([(1, d['n02']), (-ALPHA % P, d['q3']), (-BETA % P, d['q7'])])

    r11d, p11d = residual(z11d); r12d, p12d = residual(z12d)
    r11p, p11p = residual(z11p); r12p, p12p = residual(z12p)
    out = dict(
        label=label,
        Z=dict(Z1=Z1.tolist(), Z2=Z2.tolist(), Z=Z.tolist()),
        direct_form=dict(z11={k: z11d[k][0] for k in ORDER}, z12={k: z12d[k][0] for k in ORDER},
                         relation_residual_d11=r11d, relation_residual_d12=r12d,
                         residual_d11_by_type=p11d, residual_d12_by_type=p12d),
        phi_form=dict(z11={k: z11p[k][0] for k in ORDER}, z12={k: z12p[k][0] for k in ORDER},
                      relation_residual_d11=r11p, relation_residual_d12=r12p,
                      residual_d11_by_type=p11p, residual_d12_by_type=p12p),
        forms_agree=dict(z11={k: z11d[k][0] == z11p[k][0] for k in ORDER},
                         z12={k: z12d[k][0] == z12p[k][0] for k in ORDER}),
        phi4_equals_minus_phi1=dict(top=bool(np.all((T[COV['Phi_4']] + T[COV['Phi_1']]) % P == 0)),
                                    mixed=bool(np.all((S[COV['Phi_4']] + S[COV['Phi_1']]) % P == 0))),
        type_blocks={})
    for cname, hn in COV.items():
        out['type_blocks'][cname] = dict(
            half=hn,
            t_zero_blocks=zero_blocks(LT[hn]), t_block_ranks=block_ranks(LT[hn]),
            s_zero_blocks=zero_blocks(LS[hn]), s_block_ranks=block_ranks(LS[hn]),
            t_blocks={'%d%d' % (a + 1, b + 1): LT[hn][a, :, b, :].tolist() for a in range(2) for b in range(2)},
            s_blocks={'%d%d' % (a + 1, b + 1): LS[hn][a, :, b, :].tolist() for a in range(2) for b in range(2)})
    out['pairings_by_type'] = {
        'B(t1,s1)': Bpair(LT[t1], LS[t1], T[t1], S[t1], None)[1],
        'B(t1,s2)': Bpair(LT[t1], LS[t2], T[t1], S[t2], None)[1],
        'B(s1,t2)': Bpair(LS[t1], LT[t2], S[t1], T[t2], None)[1],
        'B(t3,s2)': Bpair(LT[t3], LS[t2], T[t3], S[t2], None)[1],
        'B(s3,t2)': Bpair(LS[t3], LT[t2], S[t3], T[t2], None)[1],
        'B(t1,t1)': Bpair(LT[t1], LT[t1], T[t1], T[t1], None)[1],
        'B(t1,t2)': Bpair(LT[t1], LT[t2], T[t1], T[t2], None)[1],
        'B(t3,t2)': Bpair(LT[t3], LT[t2], T[t3], T[t2], None)[1]}
    return out, T, S


# ---------------------------------------------------------------- stage 3: flag point 0 from P6 point 0
g, detg0, Yt = fl.slice_form(Y0)
Zs = fl.wprime_part(Yt)
rec['checks']['slice_form_det_g'] = dict(recomputed=detg0, pilot2_recorded=detg, match=detg0 == detg)
pt0, T0m, S0m = do_point('P6_point_0_slice', Zs[0], Zs[1], Zs[2], want_c7=True)
rec['points'].append(pt0)
save('stage3_flag_point_0')

# ---------------------------------------------------------------- stage 4: runner cross-check at flag point 0
if left() > 12:
    NODES5 = fl.NODES5
    runner = {}
    for name in ORDER:
        vs = []
        for u in NODES5:
            Tc = colten(fl.tuple_F(Zs[0], Zs[1], Zs[2], 0, u))
            t = time.perf_counter()
            a, m1, _ = pr.evaluate_P(VEC[name]['pi'], VEC[name]['rho'], Tc, VEC[name]['order'])
            b_, m2, _ = pr.evaluate_P(VEC[name]['rho'], VEC[name]['pi'], Tc, VEC[name]['order_rev'])
            rec['runner_evaluations'] += 1; rec['runner_wall_s'] += time.perf_counter() - t
            vs.append((a + b_) % P); del Tc
        co = fl.vandermonde_solve(NODES5, vs, [8, 9, 10, 11, 12])
        runner[name] = dict(values_u1_to_5=vs, u11=co[11], u12=co[12],
                            covariant_z11=pt0['direct_form']['z11'][name], covariant_z12=pt0['direct_form']['z12'][name],
                            z11_match=co[11] == pt0['direct_form']['z11'][name],
                            z12_match=co[12] == pt0['direct_form']['z12'][name])
    rec['checks']['runner_cross_check_flag_point_0'] = runner
    rec['checks']['runner_cross_check_all_match'] = all(d['z11_match'] and d['z12_match'] for d in runner.values())
    rec['counts']['runner_cross_check_values'] = 2 * len(runner)
else:
    rec['log'].append('deadline: runner cross-check skipped')
save('stage4_runner_cross_check')
del T0m, S0m

# ---------------------------------------------------------------- stage 5: further seeded flag points
rng = np.random.default_rng(SEED)
for i in range(4):
    if left() < 9: rec['log'].append('deadline before seeded point %d' % (i + 1)); break
    R = fl.wprime_part(rng.integers(0, P, size=(5, 4, 4), dtype=np.int64))
    pt, _, _ = do_point('seeded_%d' % (i + 1), R[0], R[1], R[2], want_c7=False)
    rec['points'].append(pt)
    save('stage5_seeded_%d' % (i + 1))

# ---------------------------------------------------------------- verdict counters
rec['checks']['C7_four_term_formula_replays'] = dict(count=len(c7flags), all_equal_to_einsum=all(c7flags))
rec['counts']['C7_pairings_checked'] = len(c7flags)
rec['counts']['flag_points'] = len(rec['points'])
never = {}
for key in ('t', 's'):
    for cname in COV:
        z = [p['type_blocks'][cname]['%s_zero_blocks' % key] for p in rec['points']]
        never['%s(%s)' % (key, cname)] = [b for b in ('11', '12', '21', '22') if all(d[b] for d in z)]
rec['checks']['type_blocks_zero_at_every_point'] = never
rec['checks']['any_type_block_identically_zero'] = any(v for v in never.values())
rec['checks']['relation_holds_at_every_point'] = dict(
    direct_form=all(p['direct_form']['relation_residual_d11'] == 0 for p in rec['points']),
    phi_form=all(p['phi_form']['relation_residual_d11'] == 0 for p in rec['points']),
    degree12_direct=all(p['direct_form']['relation_residual_d12'] == 0 for p in rec['points']),
    degree12_phi=all(p['phi_form']['relation_residual_d12'] == 0 for p in rec['points']))
rec['checks']['forms_agree_at_every_point'] = all(all(p['forms_agree']['z11'].values()) and all(p['forms_agree']['z12'].values())
                                                  for p in rec['points'])
rec['checks']['degree12_relation_underdetermines_alpha_beta'] = dict(
    note='one equation in two unknowns: the degree-12 rows are rank 1',
    check=(ALPHA + BETA * 101007 - 295818) % P == 0)
save('done')
print(json.dumps(dict(status=rec['status'], counts=rec['counts'], checks=rec['checks'],
                      half_tensor_calls=rec['half_tensor_calls'], runner_evaluations=rec['runner_evaluations'],
                      column_tensors=rec['column_tensors'], half_tensor_wall_s=rec['half_tensor_wall_s'],
                      runner_wall_s=rec['runner_wall_s'], elapsed_s=rec['elapsed_s'],
                      points=[dict(label=p['label'],
                                   d11_residual_direct=p['direct_form']['relation_residual_d11'],
                                   d11_residual_phi=p['phi_form']['relation_residual_d11'],
                                   d12_residual_direct=p['direct_form']['relation_residual_d12'],
                                   d11_by_type=p['direct_form']['residual_d11_by_type'],
                                   forms_agree=p['forms_agree'],
                                   phi4=p['phi4_equals_minus_phi1'],
                                   zeros={k: v['t_zero_blocks'] for k, v in p['type_blocks'].items()},
                                   szeros={k: v['s_zero_blocks'] for k, v in p['type_blocks'].items()})
                              for p in rec['points']]), indent=1, default=str))
