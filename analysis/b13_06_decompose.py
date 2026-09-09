"""Exact stable LMR product support: Pieri/JT versus independent LR tableaux."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement
import json
from math import comb, prod
from pathlib import Path
import time

LAM = (65, 17) + (2,) * 7
OUT = Path('results/b13_06')


@lru_cache(None)
def horizontal(mu, n):
    """nu/mu horizontal n-strip, by nu_i >= mu_i >= nu_(i+1)."""
    base = mu + (0,)
    answer = []
    def rec(i, left, row):
        if i == len(base):
            if left == 0: answer.append(tuple(x for x in row if x))
            return
        hi = left if i == 0 else min(left, mu[i - 1] - base[i])
        for inc in range(hi + 1):
            rec(i + 1, left - inc, row + [base[i] + inc])
    rec(0, n, [])
    return tuple(answer)


def two_row_product(mu, a, b):
    """s_(a,b)=h_a h_b-h_(a+1) h_(b-1), with b=0 handled directly."""
    ans = Counter()
    for mid in horizontal(mu, a): ans.update(horizontal(mid, b))
    if b:
        for mid in horizontal(mu, a + 1): ans.subtract(horizontal(mid, b - 1))
    assert all(v >= 0 for v in ans.values())
    return ans


def all_skew(mu, n):
    """All outer partitions with n added boxes, by the Young lattice."""
    seen = {mu}
    for _ in range(n):
        after = set()
        for p in seen:
            for i in range(len(p) + 1):
                if i and i < len(p) and p[i] == p[i - 1]: continue
                q = list(p)
                if i == len(p): q.append(1)
                else: q[i] += 1
                after.add(tuple(q))
        seen = after
    return sorted(seen, reverse=True)


def lr_count(mu, content, nu):
    """Semistandard lattice-word LR tableaux, independently of Pieri/JT."""
    if len(nu) < len(mu) or any(nu[i] < x for i, x in enumerate(mu)):
        return 0
    boxes = [(r, c) for r, end in enumerate(nu)
             for c in range(end, (mu[r] if r < len(mu) else 0), -1)]
    if len(boxes) != sum(content): return 0
    fill = {}; used = [0] * len(content)
    def rec(k):
        if k == len(boxes): return 1
        r, c = boxes[k]; result = 0
        for idx, bound in enumerate(content):
            val = idx + 1
            if used[idx] == bound: continue
            if (r, c+1) in fill and val > fill[r, c+1]: continue
            if (r-1, c) in fill and val <= fill[r-1, c]: continue
            used[idx] += 1
            if all(used[j] >= used[j+1] for j in range(len(used)-1)):
                fill[r, c] = val
                result += rec(k+1)
                del fill[r, c]
            used[idx] -= 1
        return result
    return rec(0)


def schur_dim(lam, r):
    if len(lam) > r: return 0
    lam = lam + (0,) * (r - len(lam))
    d = Fraction(1)
    for i in range(r):
        for j in range(i+1, r):
            d *= Fraction(lam[i] - lam[j] + j - i, j - i)
    assert d.denominator == 1
    return d.numerator


def exps(n, r):
    if r == 1: return [(n,)]
    return [(a,) + b for a in range(n+1) for b in exps(n-a, r-1)]


def schur_character(shape, r):
    """Independent SSYT weight character (only eight-box controls)."""
    boxes = [(i,j) for i,v in enumerate(shape) for j in range(v)]
    char = Counter(); filled={}; weight=[0]*r
    def rec(k):
        if k == len(boxes):
            char[tuple(weight)] += 1; return
        i,j=boxes[k]
        low=max(filled.get((i,j-1),0), filled.get((i-1,j),-1)+1)
        for val in range(low,r):
            filled[i,j]=val; weight[val]+=1
            rec(k+1)
            weight[val]-=1; del filled[i,j]
    rec(0)
    return char


def symmetric_square_controls():
    tests=[]
    for r in (2,3,4):
        letters=exps(4,r)
        char=Counter(tuple(x+y for x,y in zip(a,b))
                     for a,b in combinations_with_replacement(letters,2))
        rhs=Counter()
        for sh in ((8,),(6,2),(4,4)): rhs.update(schur_character(sh,r))
        assert char == rhs
        tests.append(dict(r=r, monomials=sum(char.values()), weights=len(char),
                          equality=True))
    return tests


def cell_record(nu, k, channels):
    content=[(4,)] if k == 1 else [(8,),(6,2),(4,4)]
    cartan = []
    for sh in content:
        expected = tuple(LAM[i]+(sh[i] if i < len(sh) else 0) for i in range(len(LAM)))
        if nu == expected: cartan.append(list(sh))
    t=sum(channels.values()); r=len(nu)
    # This is a conservative exact storage price for a naive tail DP, not its run time.
    tail_entries=(25+k)*prod(x+1 for x in nu[1:])
    return dict(partition=list(nu), degree=24+k, length=r,
                tensor_multiplicity=t, channels=channels,
                product_image_rank_lower_bound=int(bool(cartan)),
                product_image_rank_upper_bound=t, cartan_factors=cartan,
                ambient_multiplicity='[s_nu] h_%d[h_4]'%(24+k),
                image_matrix_shape=['a_nu',t],
                intrinsic_rank_question='j_nu = rank_Q(B_nu); 0 <= j_nu <= tensor_multiplicity',
                sufficient_gap_question='certify rank(T_pad,nu) >= a_nu-j_nu+1',
                necessary_reducible_gate='i_det,nu > i_red,nu; j_nu > i_red,nu suffices for this gate only',
                gap_deciding_question='D_nu = rank(T_pad,nu)-rank(T_det,nu); establish both ranks or separated bounds',
                specialization='vanishes for r=9' if r>9 else 'present for r>=9',
                padded_length_exclusion=(r>10),
                cartan_u_ladder=(nu == (65+4*k,17)+(2,)*7),
                naive_tail_dp_entries=tail_entries,
                one_uint64_tail_dp_bytes=tail_entries*8,
                schur_dimensions={str(d):schur_dim(nu,d) for d in (9,10,11,16)})


def main():
    start=time.monotonic(); OUT.mkdir(parents=True,exist_ok=True)
    control=symmetric_square_controls()
    all_rows=[]; audit=[]; dimensions=[]
    for k, shapes in ((1,((4,0),)),(2,((8,0),(6,2),(4,4)))):
        channels={str((a,b)):two_row_product(LAM,a,b) for a,b in shapes}
        candidates=all_skew(LAM,4*k)
        for nu in candidates:
            coeff={}
            for a,b in shapes:
                sh=(a,b) if b else (a,)
                jt=channels[str((a,b))][nu]
                lr=lr_count(LAM,sh,nu)
                assert jt==lr,(k,nu,sh,jt,lr)
                coeff[str(sh)]=jt
                audit.append(dict(degree=24+k,partition=list(nu),factor=list(sh),
                                  jt=jt,lr=lr))
            if sum(coeff.values()): all_rows.append(cell_record(nu,k,coeff))
        rows=[x for x in all_rows if x['degree']==24+k]
        for r in (9,10,11,16):
            lhs=schur_dim(LAM,r)*comb(comb(r+3,4)+k-1,k)
            rhs=sum(x['tensor_multiplicity']*x['schur_dimensions'][str(r)] for x in rows)
            assert lhs==rhs,(k,r,lhs,rhs)
            dimensions.append(dict(degree=24+k,r=r,domain_dimension=str(lhs),
                                   decomposed_dimension=str(rhs),equal=True))
    summary={}
    for d in (25,26):
        rows=[x for x in all_rows if x['degree']==d]
        summary[str(d)]=dict(components=len(rows),tensor_multiplicity_sum=sum(x['tensor_multiplicity'] for x in rows),
                            lengths=dict(Counter(x['length'] for x in rows)),
                            max_tensor_multiplicity=max(x['tensor_multiplicity'] for x in rows),
                            cartan_components=sum(bool(x['cartan_factors']) for x in rows))
    output=dict(board_numbering='batch13',session_id='B13-06',source_weight=list(LAM),
                source_degree=24,meaning='Tensor-domain decomposition, NOT the multiplication image.',
                coefficient_convention='c_alpha(F)=[s^alpha]F; E_ij c_alpha=(alpha_i+1)c_(alpha+e_i-e_j)',
                summary=summary,dimension_checks=dimensions,symmetric_square_controls=control,
                rows=all_rows,wall_seconds=time.monotonic()-start)
    (OUT/'components.json').write_text(json.dumps(output,indent=2)+'\n')
    (OUT/'lr_audit.json').write_text(json.dumps(dict(board_numbering='batch13',session_id='B13-06',
                                      checked=len(audit),rows=audit),indent=2)+'\n')
    lines=['# Complete LMR product-domain census','',
           'Tensor multiplicities are upper bounds on product-image multiplicities. All rows are exact.', '',
           '| Degree | Partition | Length | S4 | S8 | S62 | S44 | Total | Proved image floor | Status |',
           '|---|---|---:|---:|---:|---:|---:|---:|---:|---|']
    for row in all_rows:
        c=row['channels']; status=('D<=0: length>10' if row['padded_length_exclusion'] else
                                  'same D as degree 24' if row['cartan_u_ladder'] else
                                  'image/comparison ranks unresolved')
        lines.append('| %d | %s | %d | %d | %d | %d | %d | %d | %d | %s |'%(
            row['degree'],tuple(row['partition']),row['length'],c.get('(4,)',0),c.get('(8,)',0),
            c.get('(6, 2)',0),c.get('(4, 4)',0),row['tensor_multiplicity'],
            row['product_image_rank_lower_bound'],status))
    (OUT/'components.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(dict(summary=summary,lr_checks=len(audit),dimension_checks=len(dimensions),
                         symmetric_square_controls=control,seconds=time.monotonic()-start)),flush=True)


if __name__=='__main__': main()
