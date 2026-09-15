"""Small exact controls, not a highest-weight multiplicity computation.

Run only through the inspected retained b15_bound.py, from this directory.
Uses the standard library, one process, no numerical worker threads.
"""
from fractions import Fraction as Q
from itertools import permutations, combinations
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
INPUTS = [
    "Batch16/BOARD.md", "Batch16/CLAUDE_FOCUSED_REVIEW.md", "Batch16/GEMINI_REVIEW.md",
    "Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/REPORT.md",
    "Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/integrator_review.json",
    "Batch15_Launch/native_20260913/equation_review/padding_test/REPORT.md",
    "work/batch15_workers/B15-06/analysis/b15_06_geometry.py",
    "Batch15_Launch/native_20260913/equation_review/evidence/analysis/b15_bound.py",
    "work/batch15_workers/B15-06/analysis/b15_06_census.py",
    "work/batch15_workers/B15-06/results/b15_06/census.json",
    "work/batch15_workers/B15-12/docs/b15_12_report.md",
]

def hashes():
    return {s: {"sha256": hashlib.sha256((ROOT/s).read_bytes()).hexdigest(),
                "bytes": (ROOT/s).stat().st_size} for s in INPUTS}

def det(A):
    A = [[Q(v) for v in row] for row in A]
    n, out = len(A), Q(1)
    for j in range(n):
        k = next((k for k in range(j,n) if A[k][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            A[k], A[j] = A[j], A[k]
            out = -out
        p = A[j][j]
        out *= p
        for k in range(j+1,n):
            m = A[k][j]/p
            for l in range(j+1,n):
                A[k][l] -= m*A[j][l]
    return out

def rank(A):
    A = [[Q(v) for v in row] for row in A]
    n, m, r = len(A), len(A[0]), 0
    for j in range(m):
        k = next((k for k in range(r,n) if A[k][j]), None)
        if k is None:
            continue
        A[k], A[r] = A[r], A[k]
        p = A[r][j]
        for l in range(j,m):
            A[r][l] /= p
        for k in range(r+1,n):
            q = A[k][j]
            for l in range(j,m):
                A[k][l] -= q*A[r][l]
        r += 1
        if r == n:
            break
    return r

def perm_mons(n):
    return [tuple(n*i+p[i] for i in range(n)) for p in permutations(range(n))]

def jets(x, mons):
    n = len(x)
    value = sum(math.prod(x[i] for i in mon) for mon in mons)
    g = [sum(math.prod(x[k] for k in mon if k != i) for mon in mons if i in mon)
         for i in range(n)]
    H = [[0 if i == j else sum(math.prod(x[k] for k in mon if k not in (i,j))
             for mon in mons if i in mon and j in mon) for j in range(n)] for i in range(n)]
    return value, g, H

def padded(x,z):
    C,g,H = jets(x,perm_mons(3))
    B = [[0]+g] + [[g[i]]+[z*a for a in H[i]] for i in range(9)]
    return C,g,H,B

def integer(v):
    v = Q(v)
    assert v.denominator == 1
    return int(v)

def add(a,b):
    c = list(a)+[Q(0)]*max(0,len(b)-len(a))
    for i,v in enumerate(b):
        c[i] += v
    while len(c)>1 and not c[-1]: c.pop()
    return c

def mul(a,b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j] += x*y
    while len(c)>1 and not c[-1]: c.pop()
    return c

def evalp(a,t):
    out = Q(0)
    for v in reversed(a): out = out*t+v
    return out

def interpolate(values):
    # Exact Newton forward differences at consecutive integer nodes.
    layer = [Q(v) for v in values]
    coeffs = []
    while layer:
        coeffs.append(layer[0])
        layer = [layer[i+1]-layer[i] for i in range(len(layer)-1)]
    out, basis = [Q(0)], [Q(1)]
    for k,c in enumerate(coeffs):
        out = add(out,[c*v for v in basis])
        basis = [v/Q(k+1) for v in mul(basis,[-k,1])]
    return out

def remainder(a,b):
    a = list(a)
    while len(a)>=len(b):
        q,shift = a[-1]/b[-1],len(a)-len(b)
        for i,v in enumerate(b): a[i+shift] -= q*v
        while len(a)>1 and not a[-1]: a.pop()
        if a == [0]: break
    return a

def main():
    before = hashes()
    X = [[1,1,1],[1,2,3],[1,1,-3]]
    x = sum(X,[])
    C,g,H,B = padded(x,1)
    G = [g[3*i:3*i+3] for i in range(3)]
    assert C == 0 and det(G) == 48
    assert all(sum(H[i][j]*x[j] for j in range(9)) == 2*g[i] for i in range(9))
    assert all(sum(B[i][j]*([-2]+x)[j] for j in range(10)) == 0 for i in range(10))
    source_control = {"X":X,"permanent":C,"first_partial_matrix":G,
                      "first_partial_matrix_determinant":integer(det(G)),
                      "permanent_Hessian_rank":rank(H),
                      "padded_Hessian_rank_at_z1":rank(B),
                      "padded_kernel_vector":[-2]+x}
    # Formal six monomials, without random point sampling, check essential rank.
    mons = [(0,)+tuple(i+1 for i in m) for m in perm_mons(3)]
    deriv = [{tuple(k for k in mon if k!=i):1 for mon in mons if i in mon} for i in range(10)]
    keys = sorted(set().union(*(set(d) for d in deriv)))
    essential = rank([[d.get(k,0) for k in keys] for d in deriv])
    assert essential == 10
    # Independently differentiate the 24 determinant monomials at diag(0,1,1,1).
    M = [int(i==j and i>0) for i in range(4) for j in range(4)]
    DH = [[0]*16 for _ in range(16)]
    for p in permutations(range(4)):
        sign = (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        mon = tuple(4*i+p[i] for i in range(4))
        for i,j in permutations(mon,2):
            DH[i][j] += sign*math.prod(M[k] for k in mon if k not in (i,j))
    assert rank(DH) == 8
    # The complete 21-node interpolation certifies equality on this one line.
    # Hess(z*C) entries have degree <=2, determinant degree <=20.
    base = [1,2,1,3,1,2,2,1,4]
    def line(t): return [base[i]+(t if i in (0,4,8) else 0) for i in range(9)]
    Dvalues, Hvalues, Cvalues = [],[],[]
    for t in range(21):
        c,gg,hh,bb = padded(line(t),t+2)
        lhs, rhs = det(bb), -Q(3,2)*(t+2)**8*c*det(hh)
        assert lhs == rhs
        Dvalues.append(lhs)
        if t<10: Hvalues.append(det(hh))
        if t<4: Cvalues.append(c)
    D = interpolate(Dvalues)
    HC = interpolate(Hvalues)
    CP = interpolate(Cvalues)
    z8 = [Q(1)]
    for _ in range(8): z8 = mul(z8,[2,1])
    assert D == [(-Q(3,2))*v for v in mul(mul(z8,CP),HC)]
    P = mul([2,1],CP)
    remP = remainder(D,P)
    remP2 = remainder(D,mul(P,P))
    assert remP == [0]
    assert remP2 != [0]
    quotient = remainder(D,[2,1])
    assert quotient == [0]
    # Multiplicity at the distinguished factor root is at least eight.
    quot = list(D)
    for _ in range(8):
        assert remainder(quot,[2,1]) == [0]
        # synthetic division in ascending order
        q = [Q(0)]*(len(quot)-1)
        q[-1] = quot[-1]
        for i in range(len(q)-2,-1,-1): q[i] = quot[i+1]-2*q[i+1]
        quot = q
    line_control = {"base_X_row_major":base,"X_direction":"identity3","z":[2,1],
                    "C_coefficients":list(map(integer,CP)),
                    "det_Hess_C_coefficients":list(map(integer,HC)),
                    "det_Hess_P_coefficients":list(map(integer,D)),
                    "D_mod_P":list(map(integer,remP)),
                    "D_mod_P_squared":list(map(integer,remP2)),
                    "interpolation_nodes":list(range(21)),"D_degree_bound":20,
                    "D_degree_actual":len(D)-1,"z_root_order_at_least":8}
    # Row-addition contrast in natural coordinates only.
    Y = [row[:] for row in X]
    Y[0] = [a+b for a,b in zip(Y[0],Y[1])]
    row_control = {"det_before":integer(det(X)),"det_after":integer(det(Y)),
                   "per_before":C,"per_after":jets(sum(Y,[]),perm_mons(3))[0]}
    assert row_control["det_before"] == row_control["det_after"]
    assert row_control["per_before"] != row_control["per_after"]
    after = hashes()
    assert before == after
    output = {"status":"PASS_EXACT_TINY_CONTROLS","claim_scope":"Natural-coordinate examples and one exact polynomial line; no multiplicity count or new separation theorem.",
              "source_control":source_control,"essential_variable_rank":essential,
              "det4_Hessian_rank_at_diag_0111":rank(DH),
              "row_addition_control":row_control,"line_control":line_control,
              "input_hashes_unchanged_during_run":True,"inputs":before}
    path = HERE/'tiny_evidence.json'
    if path.exists():
        assert json.loads(path.read_text()) == output
        print("PASS: exact same-implementation replay")
    else:
        path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ("status","source_control","row_addition_control")},indent=2))

if __name__ == '__main__': main()
