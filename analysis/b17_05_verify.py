"""One bounded B17-05 pilot: five finite flag multiplication channels.

Run only through the existing b15_bound.py, -B, 60 s / 512 MiB.
All arithmetic is exact in F_2147483647. Nonzero minors imply Q lower bounds;
the separately proved LR ceiling, never a sampled nullspace, supplies uppers.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
from math import comb, factorial
import sys
import time
from fractions import Fraction
from flint import nmod_mat

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[2]
OUT = ROOT / 'results/b17_05'
P = 2147483647
ORDER = 4


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fq(x):
    x = Fraction(x)
    return x.numerator * pow(x.denominator, -1, P) % P


def plus(x, y):
    if isinstance(x, int) and x == 0:
        return y
    if isinstance(y, int) and y == 0:
        return x
    z = x + y
    return z % P if isinstance(z, int) else z


def times(x, y):
    if (isinstance(x, int) and x == 0) or (isinstance(y, int) and y == 0):
        return 0
    z = x * y
    return z % P if isinstance(z, int) else z


class Jet:
    def __init__(self, c):
        self.c = list(c[:ORDER + 1]) + [0] * max(0, ORDER + 1 - len(c))

    def __add__(self, other):
        if not isinstance(other, Jet):
            other = Jet([other])
        return Jet([plus(x, y) for x, y in zip(self.c, other.c)])

    __radd__ = __add__

    def __neg__(self):
        return self * (P - 1)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Jet) else -other % P)

    def __mul__(self, other):
        if not isinstance(other, Jet):
            other = Jet([other])
        out = [0] * (ORDER + 1)
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c[:ORDER + 1 - i]):
                out[i + j] = plus(out[i + j], times(x, y))
        return Jet(out)

    def __rmul__(self, other):
        return Jet([other]) * self

    def __pow__(self, n):
        out = Jet([1])
        for _ in range(n):
            out = out * self
        return out

    def diff(self):
        return Jet([times(i + 1, self.c[i + 1]) for i in range(ORDER)])

    def transpose(self):
        return Jet([x if isinstance(x, int) else x.transpose() for x in self.c])

    def scalar(self):
        return Jet([x if isinstance(x, int) else int(x[0, 0]) for x in self.c])

    def trace(self):
        return Jet([x if isinstance(x, int) else sum(int(x[i, i]) for i in range(x.nrows())) % P for x in self.c])


def sym(x, y):
    return (x * y.transpose() + y * x.transpose()) * pow(2, -1, P)


def mm(x):
    return nmod_mat([[fq(v) for v in row] for row in x], P)


def trprod(x, y):
    if isinstance(x, int) or isinstance(y, int):
        assert x == 0 or y == 0
        return 0
    return sum(int(x[i, j]) * int(y[j, i]) for i in range(10) for j in range(10)) % P


def contract(E, M, r=0, h=0):
    """Highest projection sum a_i <C^i E,C^(r-i) M>, h_E=48."""
    coefficient = 1
    out = 0
    for i in range(r + 1):
        out += coefficient * factorial(i) * factorial(r - i) * 2 * trprod(E.c[i], M.c[r - i])
        if i < r:
            coefficient = -coefficient * (r - i) * (h - r + i + 1) * pow((i + 1) * (48 - i), -1, P) % P
    return out % P


def reciprocal(base, length):
    out = [1]
    for k in range(1, length):
        out.append(-sum(base[j] * out[k - j] for j in range(1, min(k, len(base) - 1) + 1)) % P)
    return out


def point(N, vandermonde_inverse, inherited):
    s2, s3, s4 = [M[0][0] for M in N]
    H2 = mm([[12] + [0]*9] + [[0] + [2*x for x in row] for row in N[0]])
    H1 = mm([[0] + [4*N[0][i][0] for i in range(9)]] +
            [[4*N[0][i][0]] + [6*x for x in N[1][i]] for i in range(9)])
    H0 = mm([[2*s2] + [3*N[1][i][0] for i in range(9)]] +
            [[3*N[1][i][0]] + [12*x for x in N[2][i]] for i in range(9)])
    node_rows = []
    for t in range(21):
        H = H2*(t*t) + H1*t + H0
        determinant = int(H.det())
        assert determinant, 'Predeclared interpolation node is singular; pilot stops.'
        adj = H.inv()*determinant
        node_rows.append([int(adj[i, j]) for i in range(10) for j in range(10)] + [determinant])
    coefficients = vandermonde_inverse * nmod_mat(node_rows, P)
    assert all(int(coefficients[k, j]) == 0 for k in (19, 20) for j in range(100))
    invp = reciprocal([1, 0, s2, s3, s4], 22)
    invp2 = [sum(invp[i]*invp[k-i] for i in range(k+1)) % P for k in range(22)]

    def residue(j, squared, column):
        shift, inv, degree = (7, invp2, 20) if squared else (3, invp, 18)
        return sum(int(coefficients[k, column]) * inv[k+j-shift]
                   for k in range(degree+1) if k+j >= shift) % P

    L = [nmod_mat([[residue(j, False, 10*i+k) for k in range(10)] for i in range(10)], P) for j in range(5)]
    K = [residue(j, True, 100) for j in range(7)]
    L0 = Jet([L[k]*comb(15+k, k) for k in range(5)])
    Kj = [Jet([K[j+k]*comb(13+j+k, k) % P for k in range(5)]) for j in range(3)]
    a0 = mm([[int(i == 0)] for i in range(10)])
    b0 = mm([[int(i == 1)] for i in range(10)])
    a, b = Jet([a0, b0]), Jet([b0])
    Ha, Hb = Jet([H2, H1, H0]), Jet([H0])
    g = (Ha*a)*pow(3, -1, P)
    c = (a.transpose()*g).scalar()*pow(4, -1, P)
    assert c.c == [1, 0, s2 % P, s3 % P, s4 % P]
    c1 = (b.transpose()*g).scalar()
    c2 = (b.transpose()*Ha*b).scalar()*pow(2, -1, P)
    X = (L0*g)*(32*c**15) - (a*Kj[2] + b*Kj[1])*(fq('2/3')*c**16)
    Y = (a*Kj[1] + b*Kj[0])*(-fq('2/3')*c**16)
    W = -fq('44/3')*c**16*Kj[0]
    V = -fq('2/3')*c**15*(86*c*Kj[1] + 16*c1*Kj[0])
    U = 480*c**14*(g.transpose()*L0*g).scalar() + 32*c**15*(L0*Ha).trace() - 100*c**16*Kj[2] - fq('64/3')*c**15*c1*Kj[1]
    E = c**16*L0 - sym(b, Y)*fq('1/24') + sym(a, Y.diff())*fq('1/1752') - sym(a, X)*fq('1/73')
    E += sym(b, b)*W*fq('1/1104') - sym(a, b)*W.diff()*fq('1/40296') + sym(a, b)*V*fq('1/1752')
    E += sym(a, a)*W.diff().diff()*fq('1/5802624') - sym(a, a)*V.diff()*fq('1/126144') + sym(a, a)*U*fq('1/10512')

    Hab = Ha*b
    Hba = Hb*a
    M8 = 2*c*Ha + 2*sym(g, g)
    M60 = 8*c*Ha - 6*sym(g, g)
    Mab = 2*sym(g, Hab) + 8*c*Ha.diff() - 6*c1*Ha
    Maa = 8*c2*Ha + 16*sym(g, Hba) + 8*c*Hb - 6*sym(Hab, Hab) - 6*c1*Ha.diff()
    M51 = Mab + M60.diff()*fq('1/6')
    M42 = Maa + Mab.diff()*fq('1/2') + M60.diff().diff()*fq('1/20')
    M44 = 12*c*Hb - 6*sym(g, Hba) - 3*c1*Jet([H1, H0*2]) + 2*sym(Hab, Hab) + 2*c2*Ha
    products = [contract(E, M8, 2, 6), contract(E, M60, 2, 6), contract(E, M51, 1, 4), contract(E, M42), contract(E, M44)]
    row, polys, rs, S = inherited.candidates(N)
    row = [x % P for x in row]
    expected44 = (144*row[13] + 8*row[4] + 4*row[11] + fq('48/23')*row[8] + fq('4/23')*row[9]) % P
    assert products[4] == 2*expected44 % P, 'Inherited S44 multiplication control failed.'
    low = [fq(rs[0][3]), fq(inherited.rem(polys[5], [s4,s3,s2,0,1])[3]), fq(S[5]), fq(s2*S[7])]
    expected25 = sum(fq(v)*x for v,x in zip(('2/73','227/657','2/5037','191/45333'),low)) % P
    assert contract(E, Ha*fq('1/12')) == expected25, 'Inherited degree25 control failed.'
    expected62 = (16*low[1] + fq('16/69')*low[3]) % P
    assert contract(E, M60) == 2*expected62 % P, 'Inherited S62 multiplication control failed.'
    return products, row


def independent_rows(rows, width):
    selected = []
    previous = 0
    for i, row in enumerate(rows):
        rank = nmod_mat([rows[j][:width] for j in selected] + [row[:width]], P).rank()
        if rank > previous:
            selected.append(i)
            previous = rank
    return selected


def main():
    started = time.perf_counter()
    pins = json.loads((OUT/'input_hashes.json').read_text())
    for record in pins['inputs']:
        assert hashlib.sha256(Path(record['path']).read_bytes()).hexdigest() == record['sha256'], record['path']
    H = load_module('b17_05_inherited_hessian', PROJECT/'Batch15_Launch/native_20260913/reviews_filesystem/Hessian11_1631/verify_small.py')
    LR = load_module('b17_05_inherited_lr', ROOT.parent/'B15-06/analysis/b13_06_decompose.py')
    lam = (65,17)+(2,)*7
    target = (69,19)+(2,)*8
    channels = [LR.lr_count(lam, factor, target) for factor in ((8,), (6,2), (4,4))]
    assert channels == [1,3,1]
    Vinv = nmod_mat([[pow(t,k,P) for k in range(21)] for t in range(21)],P).inv()
    products, basis_rows, points = [], [], []
    for seed in range(917050,917064):
        N = H.generic(seed)
        product, basis = point(N,Vinv,H)
        products.append(product)
        basis_rows.append([basis[i] for i in (0,1,2,3,4,5,6,7,8,10,11)])
        points.append({'seed':seed,'N':N})
        print(json.dumps({'point':len(points),'elapsed':time.perf_counter()-started}),flush=True)
    selected = independent_rows(products,5)
    image_floor = len(selected)
    certificate = {'field_prime':P,'degree':26,'weight':target,'source_degree':24,
        'source_weight':lam,'channels':channels,'image_lower':image_floor,'image_upper':5,
        'image_exact':image_floor==5,'source_circuits':['S8_r2','S62_60_r2','S62_51_r1','S62_42_r0','S44_42_r0'],
        'points':points,'product_rows':products,'basis_rows':basis_rows,
        'selected_rows':selected,'controls':'P25, P26_62 and P26_44 agree at all 14 points',
        'runtime_seconds':time.perf_counter()-started}
    if image_floor == 5:
        certificate['minor5'] = int(nmod_mat([products[i] for i in selected],P).det())
        assert certificate['minor5']
    # The full finite ideal basis is inherited, not estimated from these samples.
    pole = json.loads((ROOT.parent/'B15-04/results/b16_04/universal_pole_certificate.json').read_text())
    family = pole['families']['19']
    degree_table = next(v for v in family.values() if isinstance(v, dict) and '26' in v)
    finite_basis = degree_table['26']['kernel']
    assert len(finite_basis) == 10 and degree_table['26']['all_kernel_vectors_universally_polynomial']
    certificate['finite_ideal_dimension_inherited'] = 10
    certificate['per_channel_rank_floors'] = [
        nmod_mat([[row[j] for j in indices] for row in products], P).rank()
        for indices in ((0,), (1,2,3), (4,))]
    if image_floor == 5:
        augmented = [row[:] for row in products]
        representatives = []
        for index, vector in enumerate(finite_basis):
            values = [sum(fq(v)*x for v,x in zip(vector,row)) % P for row in basis_rows]
            candidate = [row+[x] for row,x in zip(augmented,values)]
            if nmod_mat(candidate,P).rank() > len(augmented[0]):
                augmented = candidate
                representatives.append({'finite_basis_index':index,'rational_E_coordinates':vector})
        assert len(representatives) == 5
        rows10 = independent_rows(augmented,10)
        square10 = [augmented[i] for i in rows10]
        minor10 = int(nmod_mat(square10,P).det())
        assert minor10 and len(rows10) == 10
        mutated = [row[:] for row in square10]
        mutated[1] = mutated[0][:]
        assert nmod_mat(mutated,P).det() == 0
        certificate.update(quotient_dimension=5,quotient_representatives=representatives,
            quotient_rows=rows10,quotient_matrix=square10,quotient_minor10=minor10,
            duplicate_row_mutation_rejected=True)
    (OUT/'image_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps({k:certificate[k] for k in ('image_lower','image_upper','image_exact','runtime_seconds')}),flush=True)


if __name__ == '__main__':
    main()
