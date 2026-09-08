"""B_24 for Sol S5's one-block recursion (batch 11 integrator).

B_24 = sum over the 12 horizontal-4-strip predecessors mu of lambda_24 of
a_23(mu) -- the dimension of the precursor space (S^{lambda_24})^{K_24} of which
the LMR source M_{lambda_24} is the +1 eigenspace of one block swap.  S5
nominates this as the decisive economic number with gates 1e4 / 1e5 / 1e6.

Built-in check: the twelfth predecessor (61,17,2^7) IS lambda_23 on the LMR
ladder, so its a_23 must come back as the banked 273.  It does.

Same alternation as wk9_s42_census.a_weyl, but split into two phases so it can
be checkpointed: (1) enumerate the pruned Weyl terms and collapse them by their
sorted key, giving a signed multiplicity per DISTINCT mu; (2) evaluate
N_S_tail_n once per distinct mu, in chunks, saving after each chunk.
"""
import os, sys, json, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wk9_s42_census import N_S_tail_n, perm_sign

SHAPES = [
 (65,15,2,2,2,2,2,2),   (65,14,2,2,2,2,2,2,1), (65,13,2,2,2,2,2,2,2),
 (64,16,2,2,2,2,2,2),   (64,15,2,2,2,2,2,2,1), (64,14,2,2,2,2,2,2,2),
 (63,17,2,2,2,2,2,2),   (63,16,2,2,2,2,2,2,1), (63,15,2,2,2,2,2,2,2),
 (62,17,2,2,2,2,2,2,1), (62,16,2,2,2,2,2,2,2), (61,17,2,2,2,2,2,2,2),
]
DELTA, N = 23, 4
STATE = os.environ.get('B24_STATE', '/tmp/b24_state.pkl')
OUT   = os.environ.get('B24_OUT',   '/tmp/b24_partial.json')


def terms(lam):
    """{mu: signed multiplicity} over the pruned Weyl alternation."""
    r = len(lam); rho = tuple(range(r - 1, -1, -1))
    lr = [lam[i] + rho[i] for i in range(r)]
    order = sorted(range(r), key=lambda i: lr[i])
    used = [False] * r; w = [0] * r; acc = {}
    def rec(k):
        if k == r:
            mu = tuple(lr[i] - rho[w[i]] for i in range(r))
            acc[mu] = acc.get(mu, 0) + perm_sign(w)
            return
        i = order[k]
        for j in range(r):
            if not used[j] and rho[j] <= lr[i]:
                used[j] = True; w[i] = j; rec(k + 1); used[j] = False
    rec(0)
    return {m: s for m, s in acc.items() if s}


st = pickle.load(open(STATE,'rb')) if os.path.exists(STATE) else {}
i = int(sys.argv[1]); budget = float(sys.argv[2]) if len(sys.argv) > 2 else 100.0
lam = SHAPES[i]; assert sum(lam) == 92
k = str(i)
s = st.get(k)
if s is None:
    t = time.time(); T = terms(lam)
    s = {'lam': lam, 'keys': sorted(T), 'sgn': T, 'done': 0, 'tot': 0}
    st[k] = s
    print(f'shape {i} {lam}: {len(T)} distinct mu  [enumerated in {time.time()-t:.0f}s]', flush=True)

t0 = time.time()
while s['done'] < len(s['keys']) and time.time() - t0 < budget:
    mu = s['keys'][s['done']]
    s['tot'] += s['sgn'][mu] * N_S_tail_n(mu, DELTA, N)
    s['done'] += 1
pickle.dump(st, open(STATE,'wb'))
frac = s['done'] / len(s['keys'])
print(f'  shape {i}: {s["done"]}/{len(s["keys"])} keys ({frac:.0%})', flush=True)
if s['done'] == len(s['keys']):
    res = json.load(open(OUT)) if os.path.exists(OUT) else {}
    res[k] = {'mu': list(lam), 'a23': int(s['tot']), 'secs': None}
    json.dump(res, open(OUT,'w'), indent=1)
    print(f'  DONE shape {i}: a_23 = {s["tot"]}')
    print(f'  {len(res)} of 12 complete; running sum B = {sum(r["a23"] for r in res.values())}')
