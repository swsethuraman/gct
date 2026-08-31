"""Session 22, main test: chi vs det(G)^-2 vs the Psi ratio, on both cosets."""
import sympy as sp, random
from wk4_s22_dict import (mat_from_transvections, uN, net_rows, graph_normalise,
                          h_elt, chi, Psi, transport, BANK, rand_sl3, rand_pencil,
                          det3_form)

def report(A, B, a, b, transpose, tag, verbose=True):
    t = h_elt(a, b, transpose)
    Ap, Bp, G, q = transport(A, B, t)
    if Ap is None:
        return ('degenerate', None)
    assert all(q[i,j] == 0 for i in range(3) for j in range(3,9)), "q leaves Q!"
    dG = sp.nsimplify(G.det())
    ch = sp.nsimplify(chi(q))
    pred = sp.nsimplify(dG**-2)
    p0, p1 = Psi(A,B), Psi(Ap,Bp)
    ok_chi = sp.simplify(ch - pred) == 0
    ok_psi = sp.simplify(p1 - pred*p0) == 0
    ok_dq  = sp.simplify(sp.nsimplify(q[0:3,0:3].det()) - dG**-1) == 0
    if verbose:
        print(f"  {tag:26s} det(t)={int(t.det()):>3}  detG={dG}  chi={ch}  det(q|V/W)={sp.nsimplify(q[0:3,0:3].det())}"
              f"  Psi {p0} -> {p1}   [chi=detG^-2: {ok_chi}] [Psi law: {ok_psi}] [det(q|V/W)=detG^-1: {ok_dq}]")
    return ('ok', (ok_chi, ok_psi, ok_dq))

if __name__ == '__main__':
    rng = random.Random(220222)
    print("=== 2. SLOT DICTIONARY on H^0 (X -> aXb, det a det b = 1) ===")
    stats = {'chi':[], 'psi':[], 'dq':[]}
    for n in range(8):
        A, B = rand_pencil(rng)
        a, b = rand_sl3(rng), rand_sl3(rng)
        st, r = report(A, B, a, b, False, f"random pencil #{n}")
        if r: [stats[k].append(v) for k, v in zip(('chi','psi','dq'), r)]
    print()
    print("=== 3. TRANSPOSE COSET (X -> a X^T b) — the dangerous check ===")
    for n in range(8):
        A, B = rand_pencil(rng)
        a, b = rand_sl3(rng), rand_sl3(rng)
        st, r = report(A, B, a, b, True, f"transpose #{n}")
        if r: [stats[k].append(v) for k, v in zip(('chi','psi','dq'), r)]
    print()
    print("=== 4. bare transpose tau on the banked points ===")
    for k, tv in BANK.items():
        A, B = mat_from_transvections(tv)
        st, r = report(A, B, sp.eye(3), sp.eye(3), True, f"tau at {k}")
        if r: [stats[kk].append(v) for kk, v in zip(('chi','psi','dq'), r)]
    print()
    print("=== 5. non-unimodular H-elements (det a det b = m != 1): does anything break? ===")
    for m in (2, -1, -4):
        A, B = rand_pencil(rng)
        a = rand_sl3(rng)*sp.diag(m,1,1); b = rand_sl3(rng)
        t = h_elt(a, b)
        fixes = sp.expand(det3_form(t) - det3_form()) == 0
        Ap, Bp, G, q = transport(A, B, t)
        print(f"  det(a)det(b) = {a.det()*b.det()}: t fixes det_3? {fixes};  "
              f"chi={sp.nsimplify(chi(q))}, detG^-2={sp.nsimplify(G.det()**-2)}, "
              f"Psi ratio={sp.nsimplify(Psi(Ap,Bp)/Psi(A,B)) if Psi(A,B)!=0 else 'n/a'}")
    print()
    print(f"SUMMARY: chi=detG^-2 {sum(stats['chi'])}/{len(stats['chi'])};  "
          f"Psi law {sum(stats['psi'])}/{len(stats['psi'])};  "
          f"det(q|V/W)=detG^-1 {sum(stats['dq'])}/{len(stats['dq'])}")
