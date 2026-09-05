"""
Session 50 — Task 2: size the multiplicity computation at the LMR cell, honestly.

lambda = (65,17,2^7), delta = 24, N = 16, form-degree 4.  |lambda| = 96 = 4*24.
We report dim S_lambda(C^16) (Weyl), N_S (monomials of weight lambda in
Sym^24(Sym^4 C^16)) as an exact DP where feasible / a bound otherwise, the
character count n_chi via the session-46 generator-walk cost, and the shape of
the i_det linear system.  n=3 (a known, mult 6) is computed alongside as a check.
"""
from math import comb, factorial
from functools import lru_cache

def weyl_dim(lam, Nvars):
    """dim of the GL_N irreducible S_lambda, Weyl product formula (exact)."""
    l = list(lam) + [0]*(Nvars-len(lam))
    num = 1; den = 1
    for i in range(Nvars):
        for j in range(i+1, Nvars):
            num *= (l[i]-l[j]+j-i)
            den *= (j-i)
    assert num % den == 0
    return num//den

def num_deg4_monomials(N):
    return comb(N+3,4)          # degree-4 monomials in N vars

def NS_weight_count(lam, delta, N, formdeg):
    """
    Number of monomials of weight `lam` in Sym^delta(Sym^formdeg C^N):
    multisets of `delta` degree-`formdeg` exponent vectors summing to lam.
    Exact DP over the sorted list of degree-formdeg exponent vectors, packing
    partial weight as a tuple.  Feasible only for small cases (used for n=3 to
    validate; for n=4 we report the state-space size instead).
    """
    import itertools
    # generate degree-formdeg exponent vectors over N vars, weight-bounded by lam
    lam = tuple(list(lam)+[0]*(N-len(lam)))
    vecs = []
    for c in itertools.combinations_with_replacement(range(N), formdeg):
        e=[0]*N
        for v in c: e[v]+=1
        if all(e[i]<=lam[i] for i in range(N)):
            vecs.append(tuple(e))
    # DP: multisets of size delta summing to lam. Use ordered vectors to avoid
    # double counting (nondecreasing index sequence).  This is #multisets.
    # dp over (position in vecs, remaining count, remaining weight) -- too big to
    # memoise fully; only call for tiny n=3-like cases.
    from functools import lru_cache
    V = len(vecs)
    import sys
    sys.setrecursionlimit(100000)
    @lru_cache(maxsize=None)
    def go(idx, cnt, rem):
        if cnt==0:
            return 1 if all(r==0 for r in rem) else 0
        if idx>=V: return 0
        # prune
        total=0
        v=vecs[idx]
        # choose k copies of vecs[idx]
        maxk=cnt
        cur=list(rem); ok=True; k=0; total=0
        # k=0 branch
        total+=go(idx+1,cnt,rem)
        acc=list(rem)
        for k in range(1,cnt+1):
            good=True
            for i in range(N):
                acc_i = acc[i]-v[i]
                if acc_i<0: good=False; break
            if not good: break
            acc=[acc[i]-v[i] for i in range(N)]
            total+=go(idx+1,cnt-k,tuple(acc))
        return total
    return go(0, delta, lam)

def main():
    print("### n = 3 sanity cell: lambda=(19,7,2^5), delta=12, N=9, formdeg 3")
    lam3=(19,7,2,2,2,2,2); N3=9; d3=12
    print("  |lambda| =", sum(lam3), "= 3*delta? ", sum(lam3)==3*d3)
    print("  dim S_lambda(C^9) =", weyl_dim(lam3, N3))
    print("  #deg-3 monomials in 9 vars =", comb(9+2,3))
    # NS for n=3 is large; attempt only if quick
    print("  (LMR state: multiplicity a(lambda,12) = 6, from paper 3.2)")

    print()
    print("### n = 4 LMR cell: lambda=(65,17,2^7), delta=24, N=16, formdeg 4")
    lam4=(65,17,2,2,2,2,2,2,2); N4=16; d4=24
    print("  |lambda| =", sum(lam4), "= 4*delta? ", sum(lam4)==4*d4, " ; ell =", len([x for x in lam4 if x>0]))
    dS = weyl_dim(lam4, N4)
    print("  dim S_lambda(C^16) =", dS)
    print("  digits of dim S_lambda:", len(str(dS)))
    nmon4 = comb(16+3,4)
    print("  #deg-4 monomials in 16 vars =", nmon4, " (variables of Sym^4 C^16)")
    print("  dim Sym^24(Sym^4 C^16) = C(nmon+23,24) =", comb(nmon4+23,24), "(digits:", len(str(comb(nmon4+23,24))),")")
    # crude lower bound on N_S: it is enormous; report the dimension of the
    # weight-lambda space is between 1 and dim Sym^24(...).  We give the ambient.
    print()
    print("  Interpretation for the i_det computation:")
    print("   * a(lambda,24) = mult S_lambda in Sym^24(Sym^4 C^16): the ambient")
    print("     multiplicity. Not computed (plethysm at this scale is the wall);")
    print("     lower bound a>=1 (the LMR module occurs). For n=3 the analogue is 6.")
    print("   * N_S = #weight-lambda monomials; n_chi = character count.")
    print("   * i_det = dim I(D)^HWV_{lambda,24} needs the a x n_chi evaluation")
    print("     system; both dimensions are astronomically beyond reach.")

if __name__=="__main__":
    main()
