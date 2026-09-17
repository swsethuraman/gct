"""P1: dimensions and contraction pricing for d=5, lambda=(4^5). No tensor is formed."""
import importlib.util, itertools, json, sys, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / 'work/batch15_workers/B15-02/analysis/b18_02_carrier.py'
spec = importlib.util.spec_from_file_location('carrier', SRC); c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
np = c.np
t0 = time.perf_counter()
LAM = (4, 4, 4, 4, 4); D = 5
s, g = c.s_and_g(LAM, D)
# ambient a by Weyl alternant on weight multiplicities of Sym^5(Sym^4 C^5)
monos = [mu for mu in itertools.product(range(5), repeat=5) if sum(mu) == 4]
from collections import Counter
wt = Counter()
for combo in itertools.combinations_with_replacement(range(len(monos)), D):
    wt[tuple(sum(monos[i][k] for i in combo) for k in range(5))] += 1
rho = (4, 3, 2, 1, 0); a = 0
for w in itertools.permutations(range(5)):
    mu = tuple(LAM[k] + rho[k] - rho[w[k]] for k in range(5))
    if min(mu) >= 0: a += c.perm_sign(w) * wt.get(mu, 0)
# controls for s_and_g: d=1 (4)->1 ; d=3 (6,3,1,1,1)->g3,s1 ; (5,3,2,1,1)->g4,s2 ; (4,2,2,2,2)->2,2
controls = {'(4),d=1': c.s_and_g((4,), 1), '(6,3,1,1,1),d=3': c.s_and_g((6,3,1,1,1), 3),
            '(5,3,2,1,1),d=3': c.s_and_g((5,3,2,1,1), 3), '(4,2,2,2,2),d=3': c.s_and_g((4,2,2,2,2), 3)}
rng = np.random.default_rng(20260916)
price = c.plan_only(LAM, D, rng, trials=12)
out = dict(cell=dict(d=D, lam=list(LAM)), s_recomputed=s, g_recomputed=g, a_recomputed=a,
           inherited=dict(s=5, g=6, a=1, source='CLAUDE_DESCENT_FOLLOWUP_20260916.md'),
           character_controls={k: list(v) for k, v in controls.items()},
           pricing=price, guard_max_intermediate=c.MAX_INTERMEDIATE, elapsed_s=time.perf_counter() - t0)
Path(HERE / 'p1_dimensions_pricing.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
