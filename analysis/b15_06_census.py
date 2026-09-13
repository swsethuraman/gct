"""Exact stable counts; reuses attributed B14-04 power-sum/MN methods."""
from pathlib import Path
import sys
import json
import gzip
import time
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial, comb

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / 'analysis'), str(ROOT)]
from b14_04 import recount as R
from b14_06_bracket import enumerate_brackets
from tools.integrate.exclusion_predicates import conclusions_for

OUT = ROOT / 'results/b15_06'


def save(name, value):
    OUT.mkdir(exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(',', ':')) + '\n').encode()
    if name.endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    (OUT / name).write_bytes(raw)


def exact_series(nmax, degrees):
    """Newton exponential recurrence in Q[p_1,...], with checkpoint per weight."""
    L = R.logs(nmax, degrees)
    F = [{(): Q(1)}]
    for n in range(1, nmax + 1):
        row = defaultdict(Q)
        for m in range(1, n + 1):
            for x, a in L[m].items():
                for y, b in F[n-m].items():
                    row[tuple(sorted(x+y, reverse=True))] += a*b
        F.append({x: v/n for x, v in row.items() if v})
        save('count_progress.json', {'status': 'RECORDED', 'generator_degrees': degrees,
                                    'completed_weight': n, 'terms': len(F[-1])})
    return F


def controls():
    # Direct products vs the logarithmic recurrence, independent expressions.
    F = exact_series(9, (2, 3, 4))
    for n in range(10):
        direct = defaultdict(Q)
        for a in range(n//2+1):
            for b in range(n//3+1):
                rest = n-2*a-3*b
                if rest < 0 or rest % 4:
                    continue
                for rho, v in R.mul(R.mul(R.pleth_p(a,2), R.pleth_p(b,3)),
                                    R.pleth_p(rest//4,4)).items():
                    direct[rho] += v
        assert dict(direct) == F[n]
    for n in range(1, 7):
        for lam in R.parts(n):
            assert R.chi(lam, (1,)*n) == R.hooks(lam)
            for mu in R.parts(n):
                assert sum(Q(R.chi(lam,rho)*R.chi(mu,rho), R.zr(rho))
                           for rho in R.parts(n)) == int(lam==mu)
    altered = dict(F[2]); altered[(2,)] += 1
    assert altered != R.pleth_p(1,2)
    save('count_controls.json', {'status':'EXACT', 'direct_product_weights':list(range(10)),
         'orthogonality_through':6, 'altered_normalization_rejected':True})


def count(F, tail):
    n = sum(tail)
    total = Q(0)
    terms = []
    for rho, coefficient in sorted(F[n].items(), reverse=True):
        char = R.chi(tail, rho)
        total += coefficient * char
        terms.append([rho, coefficient.numerator, coefficient.denominator, char])
        if R.chi.cache_info().currsize > 180000:
            R.chi.cache_clear()
    assert total.denominator == 1 and total >= 0
    return int(total), terms


def main():
    start = time.perf_counter()
    controls()
    # This allocation is a symmetric-function expansion, not a weight carrier.
    census = [(r,t,(t,)+(2,)*(r-2)) for r in range(7,11) for t in range(3,22,2)]
    sizing = [{'r':r, 't':t, 'W':sum(tail),
               'brackets':len(enumerate_brackets(sum(tail),r-1)),
               'power_sum_partition_upper_bound':len(R.parts(sum(tail))),
               'evaluation_entries_at_600_points':600*len(enumerate_brackets(sum(tail),r-1))}
              for r,t,tail in census]
    save('sizing.json', {'status':'EXACT', 'rows':sizing,
         'method':'exact bracket enumeration and integer partition count',
         'weight_carrier_allocated':False})
    F = exact_series(37, (2,3,4))
    index = json.loads((ROOT/'results/integrate/inherited_exclusions.json').read_text())
    overlay = json.loads((ROOT/'results/b15_prep/transport_overlay.json').read_text())
    history = [json.loads(line) for line in (ROOT/'results/s57_cells/stable_a.jsonl').read_text().splitlines()]
    components = json.loads((ROOT/'results/b13_06/components.json').read_text())['rows']
    rows = []
    for r,t,tail in census:
        value, terms = count(F,tail)
        n=sum(tail)
        cert=f'count_r{r}_t{t}.json.gz'
        save(cert, {'status':'EXACT', 'tail':tail, 'generator_degrees':[2,3,4],
                    'a_inf':value, 'rows_rho_numerator_denominator_character':terms})
        old=[h['a_inf'] for h in history if tuple(h['tail'])==tail]
        assert all(v==value for v in old), (tail,value,old)
        ext=[v for v in overlay['family_extensions'] if tuple(v['tail'])==tail]
        lam=[3*n]+list(tail)
        rules=conclusions_for(index,dict(n=4,ell=r,delta=n,**{'lambda':lam}), 'quartic_padded_gap')
        L=3 if r==9 and t>=17 else 0
        row={'r':r,'t':t,'tail':tail,'n':4,'comparison_variables':16,
             'stable_degree':n,'stable_partition':lam,'a_inf':value,
             'h_pad_ub':None,'i_pad_lb':L,'m_pad_ub':value-L,
             'padded_floor_basis':'degree13 three-equation source and q62/q44 products' if L else 'trivial bound only',
             'padded_floor_from_degree':(13 if t==17 else 15) if L else None,
             'overlay_exclusions':ext,'ledger_conclusions':rules,
             'prior_stable_counts':old,'count_certificate':cert,
             'reserved':r==9 and t==21,'status':'EXACT',
             'components':[{'degree':c['degree'],'partition':c['partition'],
                            'tensor_multiplicity':c['tensor_multiplicity'],
                            'image_rank_lb':c['product_image_rank_lower_bound']}
                           for c in components if tuple(c['partition'][1:])==tail],
             **next(s for s in sizing if s['r']==r and s['t']==t)}
        rows.append(row)
        print('COUNT',r,t,value,'brackets',row['brackets'],flush=True)
        save('census.json',{'status':'RECORDED','complete':False,'rows':rows})
        R.chi.cache_clear()
    assert next(x['a_inf'] for x in rows if (x['r'],x['t'])==(9,17))==274
    assert next(x['a_inf'] for x in rows if (x['r'],x['t'])==(9,19))==392
    # Stable reducible normalization bound: on the monic depressed chart write
    # F=(s0+l)(s0^3-l*s0^2+q*s0+c). Parameters l,q,c have degrees 1,2,3.
    del F
    H = exact_series(37,(1,2,3))
    for row in rows:
        h,terms=count(H,tuple(row['tail']))
        row['h_pad_ub']=h
        row['m_pad_ub']=min(row['a_inf'],h,row['a_inf']-row['i_pad_lb'])
        row['i_pad_lb']=max(row['i_pad_lb'],row['a_inf']-h)
        save(f"hbound_r{row['r']}_t{row['t']}.json.gz",{
            'status':'EXACT','tail':row['tail'],'generator_degrees':[1,2,3],
            'h_normalization':h,'rows_rho_numerator_denominator_character':terms})
        R.chi.cache_clear()
    save('census.json',{'status':'EXACT','complete':True,'rows':rows,
                       'seconds':time.perf_counter()-start})
    print('CENSUS COMPLETE',time.perf_counter()-start,flush=True)


if __name__=='__main__':
    main()
