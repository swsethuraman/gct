"""B20-01 pilot 1: portable definition certificates for q_3 and q_7 (gate G8, defect D3).

Emits results/b20_01/certificates/q3_definition.json and q7_definition.json in the format of the sealed
n02_definition.json, each carrying the ORDERED epsilon blocks, the hand-plan column orders (both
orientations), an explicit ordering hash, the evaluation points (the five sealed P6 points and P7 S0 point 0)
and the recorded values, replayed here with the pinned runner.  Verifies the orderings against the four
script literals (s1, s2, s3, f1), against paired_runner.hand_plan, and regenerates the blocks from the
sealed seed.  Also cross-checks n02_definition.json against candidates_selected.json and assigns it the
same ordering-hash scheme (in a sibling file; the sealed certificate is not touched).
Usage: python b20_01_p1_definitions.py [--dry]   (--dry: label-only, no runner evaluation)"""
import hashlib, json, re, sys, time
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent; ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import b20_01_pinned as pin
DRY = '--dry' in sys.argv
OUTDIR = ROOT / 'results/b20_01'; CERT = OUTDIR / 'certificates'; CERT.mkdir(parents=True, exist_ok=True)
OUT = OUTDIR / ('p1_definitions_dry.json' if DRY else 'p1_definitions.json')
T0 = time.perf_counter()
pr, prrec = pin.load_runner(); c = pr.c; np = pr.np; P = pr.P
rec = dict(pilot='b20_01_p1_definitions', dry=DRY, prime=P, code_pins=prrec, inputs=dict(), checks=dict(), evaluations=0, eval_wall_s=0.0, log=[])
def save(status):
    rec['status'] = status; rec['elapsed_s'] = time.perf_counter() - T0
    OUT.write_text(json.dumps(rec, indent=1) + '\n')
def get(name):
    b, r = pin.fetch(name); rec['inputs'][name] = r; return b
p6 = json.loads(get('p6_basis.json')); p7 = json.loads(get('p7_arc_S0.json'))
n02d = json.loads(get('n02_definition.json')); cand = json.loads(get('candidates_selected.json'))
scripts = {k: get(k).decode() for k in ('s1_screen_arc.py', 's2_certify_n02_and_new.py', 's3_full_forbidden_rows.py', 'f1_new_point_minor.py')}

# ---- 1. the four script literals
LIT = re.compile(r"zip\(p6\['basis'\],\s*\(\((\d(?:,\s*\d)*)\),\s*\((\d(?:,\s*\d)*)\)\)\)")
lits = {}
for k, s in scripts.items():
    m = LIT.findall(s); assert len(m) == 1, (k, m)
    lits[k] = [tuple(int(x) for x in re.split(r',\s*', g)) for g in m[0]]
rec['checks']['script_literals'] = {k: [list(o) for o in v] for k, v in lits.items()}
LITERAL = [(0, 1, 2, 3), (0, 2, 1, 3)]
rec['checks']['four_literals_agree'] = all(v == LITERAL for v in lits.values())
assert rec['checks']['four_literals_agree']
# in every script the zip pairs p6['basis'][0] (index 3) with the first order and p6['basis'][1] (index 7) with the second
assert [b['index'] for b in p6['basis']] == [3, 7]
def tup(blocks): return tuple(tuple(tuple(int(x) for x in s) for s in b) for b in blocks)

# ---- 2. regeneration from the sealed seed (label-only; sealed generator p6_basis.py lines 36-41)
rng = np.random.default_rng(20260916)
PAIRINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
regen = {}
for n in range(30):
    prg = PAIRINGS[n % 3]
    regen[n] = dict(pairing=prg, pi=tuple(pr.paired_partition(rng, prg)), rho=tuple(pr.paired_partition(rng, prg)))
pts_regen = [rng.integers(-3, 4, size=(5, 4, 4)).astype(np.int64) for _ in range(5)]
rec['checks']['regeneration'] = {}
for b in p6['basis']:
    g = regen[b['index']]
    rec['checks']['regeneration']['q%d' % b['index']] = dict(pi_equal=(tup(b['pi']) == tup(g['pi'])), rho_equal=(tup(b['rho']) == tup(g['rho'])), pairing_equal=(tuple(tuple(x) for x in b['pairing']) == g['pairing']))
rec['checks']['regeneration']['P6_points_equal'] = all(np.array_equal(np.array(p6['points_entries'][i]), pts_regen[i]) for i in range(5))
assert all(all(v.values()) for k, v in rec['checks']['regeneration'].items() if k != 'P6_points_equal') and rec['checks']['regeneration']['P6_points_equal']

# ---- 3. hand plans and ordering hashes
def canon(obj): return json.dumps(obj, sort_keys=True, separators=(',', ':'))
SCHEME = ('sha256 of the canonical JSON (sort_keys, separators (",",":")) of {"hand_plan_column_order", "hand_plan_column_order_transposed", '
          '"pi_ordered_blocks", "rho_ordered_blocks"} with blocks as nested lists of [column, position] integers, in listed order')
def ordering_hash(pi, rho, order, order_rev):
    return hashlib.sha256(canon(dict(pi_ordered_blocks=[[list(s) for s in b] for b in pi], rho_ordered_blocks=[[list(s) for s in b] for b in rho],
                                    hand_plan_column_order=list(order), hand_plan_column_order_transposed=list(order_rev))).encode()).hexdigest()
defs = {}
for b, order in zip(p6['basis'], LITERAL):
    pi, rho = tup(b['pi']), tup(b['rho'])
    hp, hr = pr.hand_plan(pi, rho), pr.hand_plan(rho, pi)
    assert tuple(hp[0]) == order and tuple(hr[0]) == order, (b['index'], hp, hr)
    assert max(hp[1], hr[1]) <= 4 ** 10
    _, mi_f, fl_f = pr._plan(pi, rho, order); _, mi_r, fl_r = pr._plan(rho, pi, order)
    assert {s[0] for blk in pi for s in blk} == {0, 1, 2, 3} and len({s for blk in pi for s in blk}) == 20 and len({s for blk in rho for s in blk}) == 20
    defs['q%d' % b['index']] = dict(index=b['index'], pairing=tuple(tuple(x) for x in b['pairing']), pi=pi, rho=rho, order=order, order_rev=order,
                                    maxint=max(mi_f, mi_r), flops=fl_f + fl_r, ordering_hash=ordering_hash(pi, rho, order, order))
rec['checks']['hand_plan_orders_match_literals'] = True
# n02 cross-check
n02c = next(cd for cd in cand['candidates'] if cd['name'] == 'n02')
n02_pi, n02_rho = tup(n02d['pi_ordered_blocks']), tup(n02d['rho_ordered_blocks'])
rec['checks']['n02_definition_vs_candidates_selected'] = dict(pi_equal=(n02_pi == tup(n02c['pi'])), rho_equal=(n02_rho == tup(n02c['rho'])),
    order_equal=(list(n02d['hand_plan_column_order']) == list(n02c['order']) and list(n02d['hand_plan_column_order_transposed']) == list(n02c['order_rev'])),
    hand_plan_recomputed=[list(pr.hand_plan(n02_pi, n02_rho)[0]), list(pr.hand_plan(n02_rho, n02_pi)[0])])
n02_hash = ordering_hash(n02_pi, n02_rho, n02d['hand_plan_column_order'], n02d['hand_plan_column_order_transposed'])
save('label_only_done')

# ---- 4. replay of the recorded values (runner evaluations; skipped in --dry)
def qval(d, T):
    te = time.perf_counter()
    a, m1, _ = pr.evaluate_P(d['pi'], d['rho'], T, d['order']); b_, m2, _ = pr.evaluate_P(d['rho'], d['pi'], T, d['order_rev'])
    rec['evaluations'] += 1; rec['eval_wall_s'] += time.perf_counter() - te
    assert max(m1, m2) <= 4 ** 10
    return (a + b_) % P
pts6 = [np.array(Y, dtype=np.int64) for Y in p6['points_entries']]
sealed = {'q3': p6['basis_matrix_pair_by_point'][0], 'q7': p6['basis_matrix_pair_by_point'][1]}
p7pt0 = np.array(p7['points'][0]['entries'], dtype=np.int64)
def scale_a(Y, t):
    Z = Y.copy() % P; Z[:, 0, 0] = (Z[:, 0, 0] * t) % P; return Z
sealed_S0 = {'q3': p7['points'][0]['values_t0_t1_t2_t3'][0][0], 'q7': p7['points'][0]['values_t0_t1_t2_t3'][0][1]}
rec['checks']['sealed_S0_pt0_t0_values'] = sealed_S0
replay = {}
if not DRY:
    T6 = [c.column_tensor(Y % P, 5) for Y in pts6]
    T7 = c.column_tensor(scale_a(p7pt0, 0), 5)
    for name, d in defs.items():
        vals = [qval(d, T) for T in T6]; v7 = qval(d, T7)
        replay[name] = dict(P6_points_0_to_4=vals, sealed_P6=sealed[name], P6_match=(vals == sealed[name]),
                            P7_S0_point0_t0=v7, sealed_P7_S0_point0_t0=sealed_S0[name], P7_match=(v7 == sealed_S0[name]))
        save('replay_' + name)
    rec['checks']['replay'] = replay
    assert all(r['P6_match'] and r['P7_match'] for r in replay.values())

# ---- 5. certificates
for name, d in defs.items():
    cert = dict(name=name, description=('Source vector of M_(4^5): q = P_{pi,rho} + P_{rho,pi} (B18-02 Prop. 2.2 eq. (2.1)); membership by construction. '
                'Slots [column, position], columns 0..3 of height 5, position c = 4a+b (row a, column b of the 4x4 matrix); epsilon blocks are ORDERED lists; '
                'pi blocks contract row indices a, rho blocks column indices b, eps(0,1,2,3)=+1; column tensor D[c_0..c_4] = det[(Y_i)_{c_k}]_{i=1..5,k=0..4}. '
                'Values are integers; recorded mod P = 524287.  The sealed generator p6_basis.py evaluated this vector with the hand-ordered runner; the column '
                'orders below are the sealed hand plans (paired_runner.hand_plan), identical for both orientations, previously present only as script literals (D3).'),
                prime=P, pairing=[list(x) for x in d['pairing']], generator_seed=20260916,
                generator='descent_followup_claude_20260916/pilots/p6_basis.py (numpy default_rng(20260916); paired_partition for pairing, candidate index %d; regenerated here label-only and equal)' % d['index'],
                p6_basis_index=d['index'], source_record=dict(file='p6_basis.json', field='basis', **{k: v for k, v in rec['inputs']['p6_basis.json'].items()}),
                pi_ordered_blocks=[[list(s) for s in b] for b in d['pi']], rho_ordered_blocks=[[list(s) for s in b] for b in d['rho']],
                hand_plan_column_order=list(d['order']), hand_plan_column_order_transposed=list(d['order_rev']),
                ordering_hash=d['ordering_hash'], ordering_hash_scheme=SCHEME,
                hand_plan_verified_against=dict(script_literals={k: [list(o) for o in v] for k, v in lits.items()}, script_pins={k: rec['inputs'][k] for k in scripts},
                                                paired_runner_hand_plan=True),
                max_intermediate_entries=d['maxint'], flop_units_both_orientations=d['flops'],
                evaluation_points=dict(P6_points_0_to_4=p6['points_entries'], P7_S0_point0_entries_before_a_scaling=p7['points'][0]['entries'],
                                       P7_S0_note='S0 value at t = 0: entry Y[i][0][0] multiplied by t = 0 (p7_arc_S0.py scale_a)'),
                values=dict(P6_points_0_to_4=sealed[name], P7_S0_point0_t0=sealed_S0[name]),
                values_replayed_here=(replay.get(name) if replay else 'not replayed (dry run)'),
                runner=dict(carrier=prrec['carrier'], runner=prrec['runner_original']))
    (CERT / ('%s_definition.json' % name)).write_text(json.dumps(cert, indent=1) + '\n')
    rec.setdefault('certificates', {})[name] = dict(path=str((CERT / ('%s_definition.json' % name)).relative_to(ROOT)), ordering_hash=d['ordering_hash'])
n02x = dict(name='n02', note='Cross-check of the sealed n02_definition.json (not modified) and its ordering hash under the same scheme as q3/q7.',
            sealed_certificate=rec['inputs']['n02_definition.json'], candidates_selected=rec['inputs']['candidates_selected.json'],
            checks=rec['checks']['n02_definition_vs_candidates_selected'], ordering_hash=n02_hash, ordering_hash_scheme=SCHEME,
            hand_plan_column_order=list(n02d['hand_plan_column_order']), hand_plan_column_order_transposed=list(n02d['hand_plan_column_order_transposed']))
(CERT / 'n02_ordering_hash.json').write_text(json.dumps(n02x, indent=1) + '\n')
rec['certificates']['n02_ordering_hash'] = dict(path='results/b20_01/certificates/n02_ordering_hash.json', ordering_hash=n02_hash)
save('done')
print(json.dumps(dict(status=rec['status'], checks=rec['checks'], certificates=rec['certificates'], evaluations=rec['evaluations'], eval_wall_s=rec['eval_wall_s'], elapsed_s=rec['elapsed_s']), indent=1, default=str))
