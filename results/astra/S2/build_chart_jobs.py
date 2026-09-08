"""Generate the two exhaustive projective graph jobs. Does not run a CAS."""
from pathlib import Path
from itertools import permutations, product
import json, random, math
from verify_s2 import exps,numeric_det,P1,P2
OUT=Path(__file__).resolve().parent
E=exps(4,5);anchor=E.index((0,0,0,0,4));assert anchor==0
terms=[{} for _ in E];idx={e:i for i,e in enumerate(E)}
for pi in permutations(range(4)):
    sg=(-1)**sum(pi[i]>pi[j] for i in range(4) for j in range(i+1,4))
    for ks in product(range(5),repeat=4):
        alpha=tuple(ks.count(k) for k in range(5));mon=tuple(sorted(16*ks[r]+4*r+pi[r] for r in range(4)))
        q=terms[idx[alpha]];q[mon]=q.get(mon,0)+sg
assert sum(len(q) for q in terms)==15000
def expression(q,pivot):
    out=[]
    for mon,c in sorted(q.items()):
        factors=[f'x{j}' for j in mon if j!=pivot];m='*'.join(factors) or '1'
        out.append(('+' if c>0 else '-')+(str(abs(c))+'*' if abs(c)!=1 else '')+m)
    return ''.join(out).lstrip('+') or '0'

good=[i for i,e in enumerate(E) if e[4]>0 and i!=anchor]
bad=[i for i,e in enumerate(E) if e[4]==0]
assert len(good)==34 and len(bad)==35
target_names=[f'y{i}' for i in good]
jobs=OUT/'cas';jobs.mkdir(exist_ok=True)
for pivot in (0,64):
    xs=[f'x{i}' for i in range(80) if i!=pivot];ys=[f'y{i}' for i in range(70) if i!=anchor]
    lines=[f'// S2 source chart x{pivot}=1; target y0=1 (coefficient s5^4).',
       '// Field Q. Lex order u > x in numerical order > y in numerical order.',
       '// SATURATE THE FULL GRAPH FIRST, THEN impose y_bad=0.',
       '// Generated recipe, NOT a completed elimination certificate.',
       'ring r=0,('+','.join(['u']+xs+ys)+'),lp;', 'option(redSB);']
    lines += [f'poly f{i}={expression(q,pivot)};' for i,q in enumerate(terms)]
    lines += ['ideal raw=1-u*f0,'+','.join(f'f{i}-y{i}*f0' for i in range(1,70))+';',
       'ideal G=std(raw);','ideal H=eliminate(G,u);',
       f'write("chart_{pivot}_graph.txt",H);',
       'ideal W='+','.join(f'y{i}' for i in bad)+';',
       'ideal KW=std(H+W);',
       # u is already absent; x variables are eliminated in the second step.
       'ideal imageFull=eliminate(KW,'+'*'.join(xs)+');',
       f'write("chart_{pivot}_image_full.txt",imageFull);',
       'ring target=0,('+','.join(target_names)+'),lp;',
       'map shrink=r,'+','.join(['0']*(1+79)+[f'y{i}' if i in good else '0' for i in range(1,70)])+';',
       'ideal Image=shrink(imageFull);','ideal GB=std(Image);',
       f'write("chart_{pivot}_image_Q.txt",GB);',
       'print("IMAGE DIMENSION (target has 34 variables):");','print(dim(GB));',
       'print("Need a NONZERO image ideal for the noncontainment fallback.");',
       '// Export lift/standard-basis transformation certificates before mathematical promotion.',
       'quit;']
    (jobs/f'chart_{pivot}_Q.sing').write_text('\n'.join(lines)+'\n',encoding='utf-8')

manifest=dict(field='Q',source_projective_dimension=79,target_W_projective_dimension=34,
 coefficient_normalization='ordinary monomial coefficients; no factorials',
 source_order=[dict(index=16*k+4*r+c,k=k,r=r,c=c) for k in range(5) for r in range(4) for c in range(4)],
 quartic_exponents=E,anchor_index=0,W_good_nonanchor_indices=good,W_bad_indices=bad,
 raw_determinant_terms=15000,chart_pivots=[0,64],ring_variables_per_job=149,
 status='Generated and coefficient-verified; Singular not installed, no elimination run.',
 jobs=[f'cas/chart_{p}_Q.sing' for p in (0,64)],
 order='lex(u, x0..x79 excluding pivot, y1..y69); second target lex(y_good)',
 criterion='Each Image ideal nonzero (unit ideal also acceptable for an empty chart).')
(OUT/'chart_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
# Independently verify generated determinant coefficients against direct numeric determinants.
rng=random.Random(2077002);checks=[]
for pivot in (0,64):
    for case in range(6):
        x=[rng.randint(-3,3) for _ in range(80)];x[pivot]=1
        s=[rng.randint(-3,3) for _ in range(5)]
        co=[sum(c*math.prod(x[j] for j in mon) for mon,c in q.items()) for q in terms]
        val=sum(c*math.prod(a**b for a,b in zip(s,e)) for c,e in zip(co,E))
        mat=[[sum(s[k]*x[16*k+4*r+c] for k in range(5)) for c in range(4)] for r in range(4)]
        expected=numeric_det(mat);assert val==expected
        assert all(val%p==expected%p for p in (P1,P2))
        # anchor and W are independently checked as det A5 and restriction s5=0.
        assert co[0]==numeric_det([[x[64+4*r+c] for c in range(4)] for r in range(4)])
        checks.append(dict(pivot=pivot,source=x,variables=s,determinant=expected))
(OUT/'chart_coefficient_checks.json').write_text(json.dumps(dict(seed=2077002,checks=checks),indent=2),encoding='utf-8')
print(json.dumps({k:manifest[k] for k in ['raw_determinant_terms','chart_pivots','ring_variables_per_job','status']},indent=2))
