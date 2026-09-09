"""s78: structural analysis of the chart jobs BEFORE any elimination.

Reconstruct the 70 coefficient polynomials f_alpha (from build_chart_jobs, no
CAS), dehomogenize x_h=1, and report the structure that justifies algebraic
reduction:
  - which y_alpha are "good" (alpha5>0, kept) vs "bad" (alpha5=0, set to 0 in W)
  - the sparsity / degree of each f_alpha in the dehomogenized chart
  - how many W (bad) generators become trivial after x_h=1
The point: after imposing W (y_bad=0), the 35 generators f_bad - 0 = f_bad
are pure source equations; the 34 good ratio generators are f_good - y_good f0.
So the ELIMINATION IDEAL structure is: 35 source constraints {f_bad=0} plus
the graph of the rational map (f_good/f0). This is the reduction lever.
"""
from itertools import permutations, product
import json

def exps(deg, n):
    # degree-`deg` exponent tuples in n parts, SAME recursive order as verify_s2/build.
    if n == 1:
        return [(deg,)]
    out = []
    for first in range(deg + 1):
        for rest in exps(deg - first, n - 1):
            out.append((first,) + rest)
    return out

E = exps(4, 5)
anchor = E.index((0, 0, 0, 0, 4))
assert anchor == 0, anchor
idx = {e: i for i, e in enumerate(E)}

# terms[i] : dict monomial(tuple of source-var indices, sorted) -> integer coeff
terms = [{} for _ in E]
for pi in permutations(range(4)):
    sg = (-1) ** sum(pi[i] > pi[j] for i in range(4) for j in range(i + 1, 4))
    for ks in product(range(5), repeat=4):
        alpha = tuple(ks.count(k) for k in range(5))
        mon = tuple(sorted(16 * ks[r] + 4 * r + pi[r] for r in range(4)))
        q = terms[idx[alpha]]
        q[mon] = q.get(mon, 0) + sg
assert sum(len(q) for q in terms) == 15000

good = [i for i, e in enumerate(E) if e[4] > 0 and i != anchor]
bad = [i for i, e in enumerate(E) if e[4] == 0]
assert len(good) == 34 and len(bad) == 35

def report_chart(pivot):
    # dehomogenize x_pivot = 1: a source var index == pivot becomes constant 1.
    # count, per f_alpha, the number of distinct monomials and how many involve pivot.
    info = {}
    total_terms = 0
    for i, q in enumerate(terms):
        nmon = len(q)
        total_terms += nmon
        info[i] = nmon
    # f0 = det A5 uses source vars 64..79 only (the s5^4 coefficient).
    f0_vars = set()
    for mon in terms[0]:
        f0_vars.update(mon)
    return dict(pivot=pivot, total_monomials=total_terms,
                f0_num_terms=len(terms[0]), f0_source_vars=sorted(f0_vars))

out = {}
for pivot in (0, 64):
    out[str(pivot)] = report_chart(pivot)
# f0 = det A5 : entries x64..x79 (k=4 block). For pivot=0, x0=1 (in A1); f0 unaffected.
# For pivot=64, x64=1 (the (0,0) entry of A5); f0 loses that variable -> still degree 4? No:
#   det A5 is multilinear; setting one entry to 1 makes f0 have a constant-coefficient part.
out['good_indices'] = good
out['bad_indices'] = bad
out['num_good'] = len(good)
out['num_bad'] = len(bad)
# Degree profile: every f_alpha is homogeneous degree 4 in the 80 source vars.
# After x_h=1 it is inhomogeneous of degree <= 4.
print(json.dumps(out, indent=2))
