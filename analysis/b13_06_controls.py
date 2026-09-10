"""Exact product controls and s74 native-value arithmetic (no new rank claim)."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
import hashlib
import json
from math import gcd, lcm, prod
from pathlib import Path
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results/b13_06'
PRIMES=(2147483647,2147483629)


def read(path): return json.loads((ROOT/path).read_text())
def digest(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def determinant(M):
    """Exact Leibniz sum by subsets: O(n 2^n), only n<=10 controls."""
    n=len(M); dp={0:1}
    for row in M:
        after={}
        for mask,v in dp.items():
            for j,x in enumerate(row):
                if mask>>j&1: continue
                sign=-1 if (mask>>(j+1)).bit_count()%2 else 1
                q=mask|(1<<j)
                after[q]=after.get(q,0)+sign*v*x
        dp=after
    return dp[(1<<n)-1]


def permanent(M):
    return sum(prod(M[i][p[i]] for i in range(len(M))) for p in permutations(range(len(M))))


def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def binary_det(pencil):
    out=[0]*5
    for p in permutations(range(4)):
        sign=(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        q=[1]
        for i in range(4):q=multiply(q,[pencil[0][i][p[i]],pencil[1][i][p[i]]])
        out=[a+sign*b for a,b in zip(out,q)]
    return out


def binary_pad(forms):
    out=[0]*4
    for p in permutations(range(3)):
        q=[1]
        for i in range(3):q=multiply(q,forms[1+3*i+p[i]][:2])
        out=[a+b for a,b in zip(out,q)]
    return multiply(forms[0][:2],out)


def binary_red(q):
    c=[0]*4
    for e,v in q['cubic']:
        if all(x==0 for x in e[2:]):c[e[1]]+=v
    return multiply(q['l'][:2],c)


def u(fam,q):
    if fam=='det':return 24*determinant(q['pencil'][0])
    if fam=='pad':
        lf=q['linear_forms']
        return 24*lf[0][0]*permanent([[lf[1+3*i+j][0] for j in range(3)] for i in range(3)])
    if fam=='red':
        v=next(v for e,v in q['cubic'] if tuple(e)==(3,)+(0,)*8)
        return 24*q['l'][0]*v
    raise ValueError(fam)


def quadratic_hwvs():
    """c_j denotes [s1^(4-j)s2^j]F, E c_j=(5-j)c_(j-1)."""
    q={'8':{(0,0):1},'62':{(0,2):8,(1,1):-3},
       '44':{(0,4):12,(1,3):-3,(2,2):1}}
    out=[]
    for name,terms in q.items():
        deriv=Counter()
        for mon,v in terms.items():
            for i,j in enumerate(mon):
                if j:
                    changed=list(mon); changed[i]=j-1
                    deriv[tuple(sorted(changed))]+=v*(5-j)
        assert not any(deriv.values()),(name,deriv)
        out.append(dict(name=name,terms=[dict(indices=list(mon),coefficient=v) for mon,v in terms.items()],
                        raising_derivative_zero_over_Z=True))
    return q,out


def multiplication_control():
    rows=[]
    for j in range(5):
        t=[Fraction(1)]
        for a in range(j): t.append(-t[-1]*Fraction(5-j+a,4-a))
        scale=lcm(*(x.denominator for x in t)); coeff=[int(x*scale) for x in t]
        div=gcd(*coeff); coeff=[x//div for x in coeff]
        raising=Counter(); product=Counter()
        for a,c in enumerate(coeff):
            b=j-a
            if a:raising[a-1,b]+=c*(5-a)
            if b:raising[a,b-1]+=c*(5-b)
            product[tuple(sorted((a,b)))]+=c
        assert not any(raising.values())
        product={mon:c for mon,c in product.items() if c}
        assert bool(product)==(j%2==0)
        rows.append(dict(partition=[8-j,j] if j else [8],
                    tensor_terms=[dict(indices=[a,j-a],coefficient=c) for a,c in enumerate(coeff)],
                    product_terms=[dict(indices=list(mon),coefficient=c) for mon,c in product.items()],
                    exact_product_image_multiplicity=int(bool(product))))
    assert sum((9-2*j)*rows[j]['exact_product_image_multiplicity'] for j in range(5))==15
    return dict(family='Sym^4(C^2) tensor Sym^4(C^2) -> Sym^2(Sym^4(C^2))',
                domain_dimension=25,image_dimension=15,kernel_dimension=10,rows=rows,
                method='explicit highest-weight tensors, exact multiplication and raising; no sampled rank')


def full10_control(qs):
    det=read('results/s74/columns_det_2147483647.json')['points'][0]
    red=read('results/s74/columns_red_2147483647.json')['points'][0]
    pad=read('results/s74/columns_pad_2147483647.json')['points'][0]
    forms=pad['linear_forms']; completion=None
    for j in range(10):
        matrix=[row+[int(i==j)] for i,row in enumerate(forms)]
        det10=determinant(matrix)
        if det10:
            completion=dict(linear_forms=matrix,completion_column=j,determinant_over_Z=det10,
                            meaning='invertible substitution of full ten-variable l*per3; no loss of essential variables')
            break
    assert completion is not None
    coeffs={'det4_pencil':binary_det(det['pencil']),
            'generic_reducible_control':binary_red(red),
            'full10_padded_permanent':binary_pad(completion['linear_forms'])}
    answers={}
    for fam,c in coeffs.items():
        vals={name:sum(v*prod(c[i] for i in mon) for mon,v in terms.items()) for name,terms in qs.items()}
        assert all(vals.values()),(fam,vals)
        answers[fam]=dict(binary_coefficients=c,quadratic_values=vals,
                         values_are='exact integer values in ordinary coefficient normalization; no transport')
    return dict(det_point=det,reducible_point=red,padded_point=completion,evaluations=answers,
                scope='nonvanishing of coefficient factors only; does not establish a positive multiplicity gap')


def stored_arithmetic():
    source=read('results/s74/source.json'); ent=source['entries']
    assert source['complete'] and len(ent)==274 and [e['index'] for e in ent]==list(range(274))
    for e in ent:
        for key in ('native','literal'):
            f=e[key]; counts=Counter(f['C1']+f['C2']+f['one'])
            counts.update(x for pair in f['two'] for x in pair)
            assert len(counts)==f['delta'] and set(counts.values())=={4}
            assert len(set(f['C1']))==len(f['C1'])==9
            assert len(set(f['C2']))==len(f['C2'])==9
            assert all(a!=b for a,b in f['two'])
        assert e['exponent']==24-e['rung'] and e['factorial_scalar']==24**e['exponent']
    cert=read('results/s74/certified.json'); outputs=[]
    for p in PRIMES:
        c=cert['primes'][str(p)]; y=c['lmr_line']['kernel_mod_p']
        assert len(y)==274 and any(v%p for v in y)
        for fam in ('det','pad','red'):
            path=f'results/s74/columns_{fam}_{p}.json'; col=read(path)
            uu=[u(fam,q) for q in col['points']]
            assert len(uu)==col['K']
            assert all(a%b for a in uu for b in PRIMES)
            assert all(a%p==b%p for a,b in zip(uu,col['u_symbol']))
            residues=[]
            for j in range(col['K']):
                v=sum(y[i]*col['rows_native'][str(e['key'])][j]*pow(uu[j],24-e['rung'],p)
                      for i,e in enumerate(ent))%p
                residues.append(v)
            if fam=='det':assert not any(residues)
            else:
                assert all(residues)
                claimed=c['lmr_line']['residues_at_padded_points' if fam=='pad' else 'residues_at_red_points']
                # A banked line may be normalized on a different pivot.
                factor=residues[0]*pow(claimed[0],-1,p)%p
                assert all(a==factor*b%p for a,b in zip(residues,claimed))
            rec=dict(prime=p,family=fam,input_file=path,input_sha256=digest(path),
                     source_sha256=digest('results/s74/source.json'),
                     source_rank_status='ADOPTED from s74/integrator; not reranked in B13-06',
                     coefficient_vector=y,coefficient_vector_values_are='modular coordinates of stored LMR kernel candidate, NOT rational reconstruction',
                     points=[dict(integer_point=q,u_integer=v,residue=z,
                              values_are='u=24*c_(4,0,...,0); residue=sum_i y_i*native_i*u^(24-rung_i) mod p')
                             for q,v,z in zip(col['points'],uu,residues)],
                     checked_columns=col['K'],nonzero_LMR_residues=sum(bool(v) for v in residues))
            (OUT/f'input_arithmetic_{fam}_{p}.json').write_text(json.dumps(rec,separators=(',',':'))+'\n')
            outputs.append({k:v for k,v in rec.items() if k not in ('points','coefficient_vector')})
    ladder=read('results/s63_aladder.json')
    assert ladder['a_24']==ladder['a_inf_31']==274 and ladder['ladder'][-1]==274
    return dict(source_fillings_validated=274,rows=outputs,
                adopted_saturation=dict(a24=274,a25=274,a31=274,
                source='results/s63_aladder.json',sha256=digest('results/s63_aladder.json')),
                rank_replay_status='not performed: required python-flint import missing; installation socket denied')


def main():
    start=time.monotonic(); OUT.mkdir(parents=True,exist_ok=True)
    qs,hw=quadratic_hwvs()
    result=dict(board_numbering='batch13',session_id='B13-06',quadratic_HWVs=hw,
                multiplication_control=multiplication_control(),three_family_control=full10_control(qs),
                stored_input_arithmetic=stored_arithmetic())
    result['wall_seconds']=time.monotonic()-start
    (OUT/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(exact_HWVs=3,multiplication_control='image 15, kernel 10',
                         point_factors=result['three_family_control']['evaluations'],
                         stored_columns=result['stored_input_arithmetic']['rows'],
                         seconds=result['wall_seconds'])),flush=True)


if __name__=='__main__':main()
