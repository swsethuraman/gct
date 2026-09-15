"""B16-06 bounded exact image receiver. No dense carrier or geometry production."""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import sys
from flint import fmpq_mat
from b16_06_projector import solve,small_polynomial_control
from b13_06_decompose import lr_count,horizontal,schur_dim

ROOT=Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-06')
PROJECT=ROOT.parents[2]
OUT=Path('C:/Users/swami/Projects/gct-gpt/work/batch15_workers/B15-12/results/b16_12/replay/06_verify/results/b16_06')
INHERITED=PROJECT/'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py'
spec=importlib.util.spec_from_file_location('hessian11',INHERITED)
H=importlib.util.module_from_spec(spec);spec.loader.exec_module(H)

def rank(rows):return len(H.pivot_columns(rows))
def combine(cols,co):
    z=defaultdict(Q)
    for i,c in co.items():
        for k,v in cols[i].items():z[k]+=c*v
    return H.clean(z)
def source_rank(vs):
    keys=sorted(set().union(*(set(v) for v in vs)))
    return rank([[v.get(k,0) for v in vs] for k in keys])

def main():
    OUT.mkdir(exist_ok=True)
    projector=solve();small=small_polynomial_control()
    # Rational Pieri removes two boxes, including the negative last row.
    mixed=[(63,15)+(0,)*7+(-2,), (62,15)+(0,)*7+(-1,),
           (63,14)+(0,)*7+(-1,), (61,15)+(0,)*8,
           (62,14)+(0,)*8, (63,13)+(0,)*8]
    cas=lambda w:sum(x*(x+11-2*(i+1)) for i,x in enumerate(w))
    cv=cas((63,15)); cn=22
    kvals=[(cv+cn-cas(w))//2 for w in mixed]
    assert kvals==[0,73,24,144,96,46]
    dims=[schur_dim(tuple(x+2 for x in w),10) for w in mixed]
    assert sum(dims)==schur_dim((63,15),10)*55
    p25=list(map(Q,projector['contraction_image']))
    assert p25==[Q(2,73),Q(227,657),Q(2,5037),Q(191,45333)]
    pc={tuple(k):Q(c) for k,c in zip(projector['basis'],projector['coefficients'])}
    # Both quadratic multiplier tensors annihilate a, so every u term drops.
    cq=pc[(0,1,0,0,1)]*Q(-32,3)+pc[(0,2,0,0,2)]*Q(-704,3)
    c44a=pc[(0,1,0,0,1)]*(-96)+pc[(0,2,0,0,2)]*(-2112)
    c44b=pc[(0,1,0,0,1)]*(-8)+pc[(0,2,0,0,2)]*(-176)
    assert (cq,c44a,c44b)==(Q(16,69),Q(48,23),Q(4,23))
    # v25 is multiplied by s2 only to embed its tail17 source into tail19.
    # This is injective in the ambient polynomial domain.
    maps={
      's2_P25':dict(zip((1,11,6,9),p25)),
      's2_P26_62':{11:Q(16),9:cq},
      'P26_44':{13:Q(144),4:Q(8),11:Q(4),8:c44a,9:c44b}}
    lam=(65,17)+(2,)*7
    tensor={}
    for d,t in ((25,17),(26,17),(26,19)):
        nu=(4*d-t-16,t)+(2,)*8
        factors=((4,),) if d==25 else ((8,),(6,2),(4,4))
        cc={str(f):lr_count(lam,f,nu) for f in factors}
        if d==25:assert (nu in horizontal(lam,4)) and sum(cc.values())==1
        else:assert sum(cc.values())==(2 if t==17 else 5)
        tensor[f'{d},{t}']=cc
    raw,reduced,summary=H.symbolic()
    vectors=[combine(reduced,co) for co in maps.values()]
    sq=[reduced[i] for i in (5,6,7,8,9)]
    square17=[reduced[i] for i in (6,9)]
    rows=[];lower=[];points=[]
    for seed in range(916060,916074):
        N=H.generic(seed);v,polys,rs,S=H.candidates(N)
        s2=N[0][0][0];p=[N[2][0][0],N[1][0][0],s2,0,1]
        tt=H.rem(polys[5],p)[3]
        lo=[rs[0][3],tt,S[5],s2*S[7]]
        assert all(x.denominator==1 for x in lo)
        lower.append(list(map(int,lo)));rows.append(v);points.append(N)
    assert rank(lower)==4 and rank(rows)==11
    products=[[sum(co.get(i,0)*v[i] for i in range(14)) for co in maps.values()] for v in rows]
    checks={}
    for name,indices,Scols in [('tail17_degree25',[0],square17),('tail17_degree26',[0,1],square17),('tail19_degree26_selected',[2],sq),('tail19_degree27_selected',[0,2],sq)]:
        vv=[vectors[i] for i in indices]
        ir=source_rank(vv);sr=source_rank(Scols);ur=source_rank(vv+Scols)
        # Exact evaluation lower bounds match formal-source upper bounds.
        extra=[6,9] if 'tail17' in name else [5,6,7,8,9]
        ev=[[products[k][i] for i in indices]+[Q(rows[k][j]) for j in extra] for k in range(len(rows))]
        assert rank(ev)==ur
        cols=H.pivot_columns(ev);rids=H.pivot_columns([[r[j] for r in ev] for j in cols])
        minor=[[ev[i][j] for j in cols] for i in rids]
        det=str(fmpq_mat([[str(x) for x in r] for r in minor]).det())
        assert Q(det)!=0
        checks[name]=dict(selected_image_rank=ir,comparison_square_rank=sr,union_rank=ur,
            intersection_dimension=ir+sr-ur,square_quotient_dimension=ur-ir,
            exact_minor_rows=rids,exact_minor_columns=cols,
            exact_minor=[[str(x) for x in r] for r in minor],exact_minor_determinant=det)
    control=H.direct_source_check(points[0],raw,rows[0])
    result=dict(status='EXACT_SELECTED_POLYNOMIAL_IMAGES_WITH_GLOBAL_PROOF',
        source='One degree24 LMR FLAG module E24=S_(65,17,2^7).',
        map_coefficients_in_inherited_14={k:{str(i):str(c) for i,c in v.items()} for k,v in maps.items()},
        formal_source_summary=summary,projector=projector,small_control=small,
        mixed_tensor_decomposition=dict(weights=[list(w) for w in mixed],
            K_eigenvalues=kvals,dimensions=list(map(str,dims)),
            full_dimension=str(sum(dims)),dimension_sum_checked=True),
        fresh_tensor_upper_checks=tensor,
        reduced_product_source_vectors=[H.encode_vector(v) for v in vectors],
        source_expansion_control=control,generic_seeds=list(range(916060,916074)),
        generic_points=points,generic_values=rows,lower17_values=lower,
        product_values=[[str(x) for x in r] for r in products],comparisons=checks,
        fresh_claims=['E24*A1 at (25,(67,17,2^8)) has image multiplicity1.',
          'E24*A2 at (26,(71,17,2^8)) has image multiplicity2.',
          'Selected E24*S44 product at (26,(69,19,2^8)) has image multiplicity1.',
          'At (27,(73,19,2^8)), selected transported products have image multiplicity2.'],
        inherited_premises=['LMR flag source is nonzero and globally determinantal.',
          'Inherited 14 Hessian expressions and Euler source conventions.',
          'Pieri/LR upper multiplicities1 and2 in the two tail17 cells.',
          'S57 chart injection and ambient extension in characteristic zero.',
          'Squared space has polynomial lifts23/25/27; no full finite filtration inherited.'],
        limits=['No full J24 image or all-LMR/saturation computation.',
          'Tail19 selected image is not the full E24*A2 or E24*A3 image.',
          'Quotients are by specified image, not the full ideal.',
          'No padding rank computation or positive multiplicity gap.'])
    target=OUT/'image_certificate.json'
    if '--verify' in sys.argv:assert result==json.loads(target.read_text())
    else:target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',small_control=small,comparisons={k:{a:v[a] for a in ('selected_image_rank','comparison_square_rank','union_rank','intersection_dimension')} for k,v in checks.items()})))

if __name__=='__main__':main()
