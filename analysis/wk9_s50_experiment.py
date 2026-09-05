"""
Session 50 — the n=4 four-control remainder experiment.

Ambient C^16.  k = 2n-2 = 6, F = k+3 = 9, d = 4, edeg = (k+3)(d-2) = 18.
For each control P: test  P | det_9( B^T H_P(By) B )  (a degree-18 form in 9 y's).

Controls:
  1  det_4                       expect DIVIDES     (calibration; LMR theorem)
  2  generic quartic (10 vars)   expect NOT_DIVIDES (expression not identically 0)
  3  l * c, c generic cubic      expect NOT_DIVIDES (transfer control)
  4  x_0 * per_3 (full 10 vars)  the sharp test
Plus P5: generic rank of H_{padded} and rank on {P=0} (Katz).
"""
import random, json, sys, time
import wk9_s50_lmr as L

P1 = 2147483647
P2 = 2147483629
N = 16; F = 9; D = 4

def det4_idx():  return [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
def per3_idx():  return [[1,2,3],[4,5,6],[7,8,9]]   # x_1..x_9 ; x_0 pads

def build_det4():
    return L.normalise(L.det_form(det4_idx()), N)

def build_padded_per3():
    per = L.per_form(per3_idx())            # dict form, vars 1..9
    padded = L.scale_var_product(per, 0)    # * x_0
    return L.normalise(padded, N)

def build_generic_quartic(active, nmon, seed):
    import itertools
    rng = random.Random(seed)
    from collections import defaultdict
    acc = defaultdict(int)
    combos = list(itertools.combinations_with_replacement(active, 4))
    rng.shuffle(combos)
    for c in combos[:nmon]:
        e=[0]*N
        for v in c: e[v]+=1
        acc[tuple(e)] += rng.randrange(1,50)
    return [(cc,ee) for ee,cc in acc.items()]

def build_lc(active, seed):
    """l (linear) * c (generic cubic), both in `active` variables."""
    import itertools
    rng = random.Random(seed)
    lin = [(rng.randrange(1,50), tuple(1 if k==v else 0 for k in range(N))) for v in active]
    cub = []
    from collections import defaultdict
    accc = defaultdict(int)
    for c in itertools.combinations_with_replacement(active,3):
        e=[0]*N
        for v in c: e[v]+=1
        accc[tuple(e)] += rng.randrange(1,50)
    cub = [(cc,ee) for ee,cc in accc.items()]
    # product
    from collections import defaultdict as dd
    acc = dd(int)
    for cl, el in lin:
        for cc, ec in cub:
            e = tuple(el[i]+ec[i] for i in range(N))
            acc[e] += cl*cc
    return [(v,k) for k,v in acc.items() if v!=0]

def per3_zero_point(rng, p):
    """A point with x_0 != 0 and per_3(x_1..x_9)=0 (interesting dual component)."""
    idx = per3_idx()
    for _ in range(500):
        x=[0]*N
        x[0]=rng.randrange(1,p)
        for v in range(1,10): x[v]=rng.randrange(0,p)
        # solve per_3 = 0 in x[1] along the line
        per = L.normalise(L.per_form(idx), N)
        nodes=list(range(4)); vals=[]
        for t in nodes:
            xx=list(x); xx[1]=t
            vals.append(L.eval_form(per, xx, p))
        poly=L.lagrange(nodes,vals,p); rts=poly.roots()
        if rts:
            x[1]=int(rts[0][0])
            padded = build_padded_per3()
            if L.eval_form(padded, x, p)==0 and x[0]!=0:
                return x
    return None

def run_control(name, terms, B, primes, nsamples, seed, expect):
    out = dict(name=name, expect=expect, monomials=len(terms), by_prime={})
    for p in primes:
        r = L.test_divisibility(terms, N, B, F=F, dform=D, p=p, nsamples=nsamples, seed=seed)
        # independent cross-check of each sample via gcd route
        gcd_ok = True
        for res in r['results']:
            gcd_ok = gcd_ok and (res['r_is_zero'] == _gcd_divides(terms, B, res['a'], p))
        out['by_prime'][p] = dict(verdict=r['verdict'], any_nonzero_r=r['any_nonzero_r'],
                                  all_g_zero=r['all_g_zero'],
                                  gdegs=sorted({d['gdeg'] for d in r['results']}),
                                  sample_r=[d['r_coeffs'] for d in r['results']][:3],
                                  gcd_crosscheck=gcd_ok)
    return out

def _gcd_divides(terms, B, a, p):
    """Independent route: p_a | g_a  <=>  gcd(p_a,g_a) has degree = deg(p_a)."""
    from flint import nmod_poly
    H = L.hessian_monlists(terms, N)
    r, pdeg, gdeg = L.remainder_one(terms, H, B, a, p, N, F, D)
    if r is None: return True
    # rebuild p_a and g_a to gcd
    M0,M1,M2 = L.matpoly_from_H(H,B,a,p,N,F,D)
    edeg=F*(D-2); gnodes=list(range(edeg+1))
    gvals=[L.det_at_t(M0,M1,M2,t,p,F) for t in gnodes]
    g=L.lagrange(gnodes,gvals,p)
    def xnum(t):
        col=[t]+list(a); return [sum(B[rr][c]*col[c] for c in range(F))%p for rr in range(N)]
    pnodes=list(range(D+1)); pvals=[L.eval_form(terms,xnum(t),p) for t in pnodes]
    pa=L.lagrange(pnodes,pvals,p)
    if pa.degree()<1: return True
    gg=g.gcd(pa)
    return gg.degree()==pa.degree()

def main():
    t0=time.time()
    random.seed(0)
    B  = [[random.randrange(1,40) for _ in range(F)] for _ in range(N)]   # the 9-plane, recorded
    Bseed = "python random.seed(0); 16x9 in [1,40)"
    det4 = build_det4()
    padded = build_padded_per3()
    gq   = build_generic_quartic(active=list(range(10)), nmon=200, seed=71)
    lc   = build_lc(active=list(range(10)), seed=73)

    print(f"B[0]={B[0]}  ({Bseed})")
    results = []
    results.append(run_control("1_det4",        det4,   B, [P1,P2], 6, 11, "DIVIDES"))
    results.append(run_control("2_generic",     gq,     B, [P1],    3, 12, "NOT_DIVIDES"))
    results.append(run_control("3_lc",          lc,     B, [P1],    3, 13, "NOT_DIVIDES"))
    results.append(run_control("4_padded_per3", padded, B, [P1,P2], 6, 14, "SHARP"))

    # P5: Hessian rank of padded permanent
    rng=random.Random(9)
    gr, _ = L.rank_H_generic(padded, N, P1, seed=9)
    zp = per3_zero_point(rng, P1)
    rz = L.rank_H_at_point(padded, N, P1, zp) if zp else None
    # also rank on {x_0=0} component
    x0zero=[0]+[random.randrange(1,P1) for _ in range(9)]+[0]*6
    rz0 = L.rank_H_at_point(padded, N, P1, x0zero)
    p5 = dict(generic_rank=gr, rank_on_per3_zero=rz, rank_on_x0_zero=rz0)

    for r in results:
        print(f"\n[{r['name']}] expect={r['expect']} monomials={r['monomials']}")
        for p,v in r['by_prime'].items():
            print(f"   p={p}: {v['verdict']:12s} g_zero={v['all_g_zero']} gdegs={v['gdegs']} gcd_xcheck={v['gcd_crosscheck']}")
            if v['sample_r'] and not all(len(s)==0 for s in v['sample_r']):
                print(f"          sample remainder coeffs (first): {v['sample_r'][0]}")
    print(f"\n[P5] padded-permanent Hessian ranks: generic={p5['generic_rank']} "
          f"on(per3=0,x0!=0)={p5['rank_on_per3_zero']} on(x0=0)={p5['rank_on_x0_zero']}")
    print(f"\nelapsed {time.time()-t0:.1f}s")

    json.dump(dict(B=B, Bseed=Bseed, results=results, p5=p5,
                   params=dict(N=N,F=F,d=D,k=6,edeg=F*(D-2),delta=24,
                               weight="(65,17,2^7)")),
              open("../results/s50_controls.json","w"), indent=1)

if __name__=="__main__":
    main()
