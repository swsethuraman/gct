#!/usr/bin/env python3
"""
Session 72 -- Residue 1, the reproducible top-component measurement for P cap c21.

Self-contained: builds the reduced Q_2^pi, writes a 25-random-hyperplane slice,
runs msolve to get the Groebner parametrisation of the (dim-26) top component as
a curve in one free variable, constructs generic points of the top component from
it, verifies each lies on V(Q_2^pi), and measures the order-2 fixed-factor image
by s59's identity.  Prints 19 at every generic top-component point.

Needs msolve on PATH.  Run:  python3 analysis/wk11_s72_pc21_top.py
"""
import sys, os, subprocess, random, re, json, argparse
sys.path.insert(0, 'analysis')
from flint import nmod_mat
from wk11_s72_pc21 import build_reduced, split_ab, order2_image_at

def slice_and_measure(p, seed=1, ncut=25, npts=4, verbose=True):
    S = build_reduced('P_c21', seed, p); red = S['red']; nW = S['nW']; inv2 = pow(2, p-2, p)
    a_idx, b_idx, bad = split_ab(red, nW, p)
    rng = random.Random(1000 + p % 97)
    polys = []
    for Sm in red:
        terms = []
        for i in range(nW):
            for j in range(i, nW):
                c = (Sm[i][i]*inv2) % p if i == j else Sm[i][j] % p
                if not c: continue
                terms.append(f"{c}*w{i+1}^2" if i == j else f"{c}*w{i+1}*w{j+1}")
        polys.append(" + ".join(terms) if terms else "0")
    vs = ",".join(f"w{i+1}" for i in range(nW))
    lins = [" + ".join(f"{rng.randint(1,p-1)}*w{i+1}" for i in range(nW)) + f" + {rng.randint(1,p-1)}"
            for _ in range(ncut)]
    ms = f"analysis/s72_pc21_top_p{p}.ms"; out = f"results/s72_pc21_top_p{p}.out"
    open(ms, 'w').write(vs + "\n" + str(p) + "\n" + ",\n".join(polys + lins) + "\n")
    subprocess.run(['msolve', '-f', ms, '-g', '2', '-o', out], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    txt = open(out).read(); body = txt[txt.rfind('['):]
    gb = [s.strip() for s in body.strip('[]:\n').split(',') if s.strip()]
    sol = {}
    for poly in gb:
        terms = re.findall(r'(\d+)\*w(\d+)\^1', poly)
        d = {int(idx): int(coef) % p for coef, idx in terms}
        ones = [idx for idx, co in d.items() if co == 1]
        if not ones: continue
        lv = min(ones); m = re.search(r'([+-]?\d+)\s*$', poly.strip()); c = int(m.group(1)) % p if m else 0
        sol[lv] = ({idx: co for idx, co in d.items() if idx != lv}, c)
    # dimension: number of free variables left (leading vars = keys of sol)
    free = [i+1 for i in range(nW) if (i+1) not in sol]
    dimV = ncut + len(free)   # dim of slice + free = codim of the cut inside V + ...
    def qeval(w):
        out = []
        for Sm in red:
            s = 0
            for i in range(nW):
                if not w[i]: continue
                for j in range(i, nW):
                    c = (Sm[i][i]*inv2) % p if i == j else Sm[i][j] % p
                    if c: s = (s + c*w[i]*w[j]) % p
            out.append(s % p)
        return out
    imgs = []
    for _ in range(npts):
        vals = {f: rng.randint(1, p-1) for f in free}
        for _ in range(4):
            for lv, (dep, c) in sol.items():
                s = c
                for idx, co in dep.items(): s = (s + co*vals.get(idx, 0)) % p
                vals[lv] = (-s) % p
        w = [vals.get(i+1, 0) for i in range(nW)]
        onV = not any(qeval(w))
        img = order2_image_at(S, w)
        imgs.append((onV, img.get('order2_image')))
    return dict(p=p, a_linear_nonzero=bad, free_vars_after_25cut=len(free),
                dim_V_reduced=25 + len(free), points=imgs)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--primes', default='32003,1000003,2147483647')
    a = ap.parse_args(); res = []
    for p in [int(x) for x in a.primes.split(',')]:
        r = slice_and_measure(p); res.append(r)
        print(f"p={p}: a-linear nonzero={r['a_linear_nonzero']} (0=proved a-linear); "
              f"free vars after 25-cut={r['free_vars_after_25cut']} => dim V(Q2pi) reduced={r['dim_V_reduced']}; "
              f"top-component images={[img for _,img in r['points']]} (onV={[ov for ov,_ in r['points']]})", flush=True)
    json.dump(res, open('results/s72_pc21_top.json', 'w'), indent=1)
    allimgs = [img for r in res for _, img in r['points']]
    print(f"\nP cap c21 top-component order-2 image = {sorted(set(allimgs))} across primes "
          f"{[r['p'] for r in res]} -> {'19 confirmed' if set(allimgs)=={19} else 'CHECK'}")
    print("wrote results/s72_pc21_top.json")
