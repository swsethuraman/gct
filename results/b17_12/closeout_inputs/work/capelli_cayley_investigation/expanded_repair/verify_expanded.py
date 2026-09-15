"""Exact expanded repair construction/verification; Python standard library only.

Run only through the inspected B15-01 b15_bound.py wrapper, with -B,
--seconds 60 --memory-mb 512. Pass --produce for the single initial pilot;
omit it to verify retained artifacts in an independently authorized replay.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
from itertools import permutations
import json
from math import factorial, gcd
import os
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent
ROOT = SOURCE.parent.parent
ZERO = (0,) * 9
START = time.perf_counter()
METRICS = {"max_polynomial_terms": 0, "max_echelon_integer_bits": 0}


def checkpoint(label):
    deadline = float(os.environ.get("CI73_DEADLINE", "0"))
    if not deadline:
        raise RuntimeError("Run through the required bounded wrapper")
    if time.monotonic() + 1 >= deadline:
        raise RuntimeError("Bounded pilot deadline reserve reached")
    print(json.dumps({"stage": label, "elapsed_seconds": time.perf_counter()-START}), flush=True)


def clean(p):
    p = {e: c for e, c in p.items() if c}
    METRICS["max_polynomial_terms"] = max(METRICS["max_polynomial_terms"], len(p))
    assert len(p) <= 30000, "Polynomial support cap"
    return p


def mul(p, q):
    out = defaultdict(int)
    for a, c in p.items():
        for b, d in q.items():
            out[tuple(x+y for x, y in zip(a,b))] += c*d
    return clean(out)


def diff(p, alpha):
    out = {}
    positions = [(i,a) for i,a in enumerate(alpha) if a]
    for e, c in p.items():
        v = c
        for i,a in positions:
            for k in range(a):
                v *= e[i]-k
        if v:
            out[tuple(x-y for x,y in zip(e,alpha))] = v
    return clean(out)


def addto(out, p, factor=1):
    for e,c in p.items():
        out[e] += factor*c


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in compositions(n-i,k-1):
                yield (i,)+tail


def weight(a):
    return tuple(sum(a[3*i:3*i+3]) for i in range(3)) + tuple(sum(a[j::3]) for j in range(3))


def matching_terms(n):
    out=[]
    for p in permutations(range(n)):
        e=[0]*(n*n)
        for i,j in enumerate(p):
            e[n*i+j]=1
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        out.append((tuple(e),sign))
    return out


MATCH = [e for e,_ in matching_terms(3)]
G = dict.fromkeys(MATCH,1)


def powers(p, last):
    result=[{(0,)*len(next(iter(p))):1}]
    for _ in range(last):
        result.append(mul(result[-1],p))
    return result


def construct():
    monos=list(compositions(3,9))
    groups=defaultdict(list)
    for a in monos:
        groups[weight(a)].append(a)
    pairs=[(a,b) for w in sorted(groups) for a in groups[w] for b in groups[w]]
    assert len(monos)==165 and len(groups)==100 and len(pairs)==339
    assert Counter(map(len,groups.values()))=={1:51,2:36,3:12,6:1}
    gp=powers(G,4)
    assert list(map(len,gp))==[1,6,21,55,120]
    columns=[{"kind":"A","alpha":list(a)} for a in MATCH]
    columns += [{"kind":"T","alpha":list(a),"beta":list(b),"weight":list(weight(a))} for a,b in pairs]
    rows=[]
    labels=[]
    for s in range(1,5):
        polys=[diff(gp[s],a) for a in MATCH]
        polys += [diff(mul({b:1},gp[s-1]),a) for a,b in pairs]
        support=set(gp[s-1])
        for p in polys:
            support.update(p)
        assert support==set(gp[s-1])
        for e in sorted(support,key=lambda e:tuple(reversed(e))):
            assert weight(e)==(s-1,)*6
            labels.append({"s":s,"exponents":list(e)})
            rows.append([p.get(e,0) for p in polys]+[(s+1)*(s+2)*(s+3)*gp[s-1].get(e,0)])
    assert len(rows)==83 and all(len(r)==346 for r in rows)
    return {"row_count":83,"variable_count":345,"rows":labels,"columns":columns,"augmented_matrix":rows,
            "cubic_monomials":[list(a) for a in monos],
            "weight_blocks":[{"weight":list(w),"monomials":[list(a) for a in groups[w]]} for w in sorted(groups)]},gp


def verify_by_coefficient_formula(data,gp):
    # Independent extraction: [y^e] partial^alpha f = (e+alpha)!/e! [y^(e+alpha)]f.
    for label,row in zip(data["rows"],data["augmented_matrix"]):
        s=label["s"]
        e=tuple(label["exponents"])
        for j,column in enumerate(data["columns"]):
            a=column["alpha"]
            raised=tuple(e[i]+a[i] for i in range(9))
            factor=1
            for x,y in zip(e,raised):
                factor *= factorial(y)//factorial(x)
            if column["kind"]=="A":
                value=factor*gp[s].get(raised,0)
            else:
                source=tuple(raised[i]-column["beta"][i] for i in range(9))
                value=factor*gp[s-1].get(source,0)
            assert value==row[j], (s,e,j,"independent coefficient mismatch")
        assert row[-1]==(s+1)*(s+2)*(s+3)*gp[s-1][e]


def echelon(matrix):
    # Integral row operations preserve rational row space. Primitive row
    # normalization avoids introducing Fraction objects in elimination.
    rows=[r[:] for r in matrix]
    pivots=[]
    for c in range(len(rows[0])):
        r=len(pivots)
        candidates=[i for i in range(r,len(rows)) if rows[i][c]]
        if not candidates:
            continue
        j=min(candidates,key=lambda i:abs(rows[i][c]))
        rows[r],rows[j]=rows[j],rows[r]
        pivot=rows[r]
        for i in range(r+1,len(rows)):
            value=rows[i][c]
            if not value:
                continue
            d=gcd(pivot[c],value)
            a=pivot[c]//d
            b=value//d
            tail=[a*x-b*y for x,y in zip(rows[i][c+1:],pivot[c+1:])]
            bits=max((abs(x).bit_length() for x in tail),default=0)
            METRICS["max_echelon_integer_bits"]=max(METRICS["max_echelon_integer_bits"],bits)
            assert bits<=4096, "Integer intermediate cap"
            divisor=gcd(*tail)
            if divisor>1:
                tail=[x//divisor for x in tail]
            rows[i][c:]=[0]+tail
        pivots.append(c)
        if len(pivots)==len(rows):
            break
    return {"pivots":pivots,"rank":len(pivots),"echelon_nonzero_rows":rows[:len(pivots)]}


def balanced_control(data):
    saved=json.loads((SOURCE/"normal_relaxation_certificate.json").read_text())
    lookup={(tuple(c["alpha"]),tuple(c.get("beta",[]))):j for j,c in enumerate(data["columns"])}
    indices=list(range(6))+[lookup[a,b] for a in MATCH for b in MATCH]
    reduced=[[r[j] for j in indices]+[r[-1]] for r in data["augmented_matrix"]]
    assert data["rows"]==saved["labels"]
    assert reduced==[[int(x) for x in r] for r in saved["matrix"]]
    w=[Fraction(int(n),int(d)) for n,d in saved["left_certificate"]]
    products=[sum(w[i]*reduced[i][j] for i in range(83)) for j in range(43)]
    assert products==[0]*42+[1]
    result=echelon(reduced)
    assert result["rank"]==37 and result["pivots"][-1]==42
    assert sum(c<42 for c in result["pivots"])==36
    return {"coefficient_rank":36,"augmented_rank":37,"matrix_matches_saved":True,
            "left_certificate_verified":True,"left_certificate_nonzeros":sum(bool(x) for x in w),
            "selected_expanded_columns":indices,"pivots":result["pivots"]}


def analytic_solution(data):
    t=defaultdict(Fraction)
    for a in compositions(2,3):
        coefficient=Fraction(3,2)*factorial(2)
        for x in a:
            coefficient/=factorial(x)
        for j in range(3):
            e=a+tuple(int(i==j) for i in range(3))+(0,0,0)
            t[e]+=coefficient
    for a in compositions(3,3):
        coefficient=-Fraction(1,2)*factorial(3)
        for x in a:
            coefficient/=factorial(x)
        t[a+(0,)*6]+=coefficient
    solution=[]
    for c in data["columns"]:
        solution.append(t.get(tuple(c["alpha"]),Fraction(0)) if c["kind"]=="T" and c["alpha"]==c["beta"] else Fraction(0))
    for row in data["augmented_matrix"]:
        assert sum(c*v for c,v in zip(row[:-1],solution))==row[-1]
    assert sum(bool(x) for x in solution)==28
    return solution


def tensor_rank(data,solution):
    lookup={(tuple(c["alpha"]),tuple(c["beta"])):solution[j] for j,c in enumerate(data["columns"]) if c["kind"]=="T"}
    ranks=[]
    for block in data["weight_blocks"]:
        monos=list(map(tuple,block["monomials"]))
        m=[[lookup[a,b] for b in monos] for a in monos]
        denominator=1
        for r in m:
            for x in r:
                denominator=denominator*x.denominator//gcd(denominator,x.denominator)
        rank=echelon([[int(x*denominator) for x in r] for r in m])["rank"]
        ranks.append({"weight":block["weight"],"dimension":len(monos),"rank":rank})
    assert sum(b["rank"] for b in ranks)==28
    return ranks


def direct_normal_controls(gp):
    # Full polynomials use Y[0..8],z,w,t. No truncated series or reduced
    # coefficient formula is used to compute the left side.
    cases=[
        ({MATCH[0]:2,MATCH[3]:-3},{MATCH[2]:3,MATCH[5]:-1},{MATCH[1]:-2,MATCH[4]:5}),
        ({MATCH[1]:-2,MATCH[5]:4},{(3,0,0,0,0,0,0,0,0):2,(1,1,0,1,0,0,0,0,0):-1},
         {(3,0,0,0,0,0,0,0,0):-3,(0,0,0,0,2,0,0,0,1):2}),
        ({a:i-2 for i,a in enumerate(MATCH) if i!=2},
         {(0,0,0,0,0,0,1,2,0):3,(0,0,0,0,0,0,0,0,3):-2,MATCH[0]:1},
         {(0,0,0,0,0,0,1,2,0):-2,(0,2,1,0,0,0,0,0,0):1,MATCH[5]:3})]
    output=[]
    for index,(A,H,k) in enumerate(cases):
        f={e+(1,0,0):c for e,c in G.items()}
        f.update({e+(0,1,1):c for e,c in k.items()})
        fp=powers(f,4)
        checks=[]
        for s in range(1,5):
            full=defaultdict(int)
            for a,c in A.items():
                addto(full,diff(fp[s],a+(1,0,0)),c)
            for a,c in H.items():
                for e,v in diff(fp[s],a+(0,1,0)).items():
                    full[e[:-1]+(e[-1]-1,)]+=c*v
            direct=clean({e:c for e,c in full.items() if e[-1]==0 and e[-2]==0})
            reduced=defaultdict(int)
            for a,c in A.items():
                addto(reduced,diff(gp[s],a),c)
            kg=mul(k,gp[s-1])
            for a,c in H.items():
                addto(reduced,diff(kg,a),c)
            expected={e+(s-1,0,0):s*c for e,c in clean(reduced).items()}
            assert direct==expected, ("direct t0 extraction",index,s)
            checks.append({"s":s,"input_power_terms":len(fp[s]),"extracted_terms":len(direct),"verified":True})
        output.append({"case":index,"A":[[list(e),c] for e,c in A.items()],"H":[[list(e),c] for e,c in H.items()],
                       "k":[[list(e),c] for e,c in k.items()],"checks":checks})
    return output


def determinant_permanent_controls():
    output=[]
    for n in (2,3):
        for kind in ("det","per"):
            f={e:sign if kind=="det" else 1 for e,sign in matching_terms(n)}
            fp=powers(f,4)
            for s in range(1,5):
                residual=defaultdict(int)
                for a,c in f.items():
                    addto(residual,diff(fp[s],a),c)
                b=factorial(s+n-1)//factorial(s-1)
                addto(residual,fp[s-1],-b)
                residual=clean(residual)
                if kind=="det" or s<=2 or n==2:
                    assert not residual
                else:
                    assert residual
                if n==3 and kind=="per" and s==3:
                    assert len(residual)==6 and set(residual.values())=={12}
                    assert all(set(e)<={0,1} and weight(e)==(2,)*6 for e in residual)
                output.append({"n":n,"kind":kind,"s":s,"residual_terms":len(residual),"verified":True})
    return output


def block_determinant_control():
    # F_t=det([[Y,t*u],[t*v^T,z]]). Its dual operator has t^{-2}
    # two-normal terms, separately from the single-normal repair ansatz.
    terms=matching_terms(4)
    f={e+(sum(e[4*i+j] for i in range(4) for j in range(4) if (i==3)!=(j==3)),):c for e,c in terms}
    fp=powers(f,4)
    checks=[]
    for s in range(1,5):
        lhs=defaultdict(int)
        for a,c in f.items():
            derivative=diff(fp[s],a[:-1]+(0,))
            for e,v in derivative.items():
                lhs[e[:-1]+(e[-1]-a[-1],)]+=c*v
        lhs=clean(lhs)
        b=s*(s+1)*(s+2)*(s+3)
        assert lhs=={e:b*c for e,c in fp[s-1].items()}
        assert all(e[-1]>=0 for e in lhs)
        checks.append({"s":s,"input_power_terms":len(fp[s]),"output_terms":len(lhs),"all_t_coefficients_verified":True})
    return {"input_terms":len(f),"t_degree_counts":{str(k):v for k,v in Counter(e[-1] for e in f).items()},"checks":checks}


def hashes():
    paths=[SOURCE/name for name in ("next_experiment.md","normal_relaxation_certificate.json","verify_normal_relaxation.js","exact_checks.js","check_claude_depth2.js")]
    paths += [ROOT/"work/batch15_workers/B15-01/analysis/b15_bound.py",Path(sys.executable),Path(__file__),HERE/"preflight.md"]
    out=[]
    for path in paths:
        raw=path.read_bytes()
        out.append({"path":str(path),"bytes":len(raw),"sha256_bytes":hashlib.sha256(raw).hexdigest(),
                    "sha256_crlf_to_lf":hashlib.sha256(raw.replace(b"\r\n",b"\n")).hexdigest() if path.suffix not in (".exe",".dll") else None})
    return out


def write_json(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+"\n",encoding="utf-8")


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--produce",action="store_true")
    args=parser.parse_args()
    checkpoint("start")
    data,gp=construct()
    verify_by_coefficient_formula(data,gp)
    checkpoint("constructed and independently checked all coefficients")
    solution=analytic_solution(data)
    expanded=echelon(data["augmented_matrix"])
    assert all(c<345 for c in expanded["pivots"])
    balanced=balanced_control(data)
    blocks=tensor_rank(data,solution)
    checkpoint("rational solution, expanded exact rank, and balanced contradiction verified")
    normal=direct_normal_controls(gp)
    basic=determinant_permanent_controls()
    checkpoint("direct Laurent extraction and determinant/permanent controls verified")
    block=block_determinant_control()
    checkpoint("full block determinant Laurent Cayley control verified")
    certificate={"status":"consistent","coefficient_rank":expanded["rank"],"augmented_rank":expanded["rank"],
                 "affine_solution_dimension":345-expanded["rank"],"pivots":expanded["pivots"],
                 "solution":[[str(x.numerator),str(x.denominator)] for x in solution],
                 "solution_nonzero_entries":[{"column":j,"value":[str(x.numerator),str(x.denominator)]} for j,x in enumerate(solution) if x],
                 "A_zero":True,"T_rank":28,"T_block_ranks":blocks,"rank_at_most_six_status":"unresolved; no low-rank search performed",
                 "verified_equations":83,"powers_checked":[1,2,3,4],
                 "formula":"T = (3/2) R(1,2) R(2,1) - (1/2) R(1,3); A=0, in normal ordering partial^alpha y^alpha",
                 "proof_scope":"Necessary restricted boundary identities only; no full arc, global separator, saturation membership, or multiplicity gap."}
    controls={"balanced_only":balanced,"direct_coefficient_extraction":normal,"determinant_permanent":basic,
              "full_block_determinant":block,"all_passed":True}
    if args.produce:
        for name in ("matrix.json","certificate.json","controls.json","input_hashes.json","verification.json"):
            assert not (HERE/name).exists(), "Refuse to overwrite an existing pilot artifact"
        write_json("matrix.json",data)
        write_json("certificate.json",certificate)
        write_json("controls.json",controls)
        write_json("input_hashes.json",hashes())
    else:
        assert json.loads((HERE/"matrix.json").read_text())==data
        assert json.loads((HERE/"certificate.json").read_text())==certificate
        assert json.loads((HERE/"controls.json").read_text())==controls
        assert json.loads((HERE/"input_hashes.json").read_text())==hashes()
    # Read back the complete retained matrix and check every rational equation.
    retained=json.loads((HERE/"matrix.json").read_text())
    cert=json.loads((HERE/"certificate.json").read_text())
    vals=[Fraction(int(n),int(d)) for n,d in cert["solution"]]
    assert retained==data
    for row in retained["augmented_matrix"]:
        assert sum(v*c for v,c in zip(vals,row[:-1]))==row[-1]
    verification={"all_passed":True,"exact_arithmetic":"unbounded Python integers and fractions.Fraction; no floating point or modular rank inference",
                  "independent_matrix_entry_checks":83*346,"expanded_coefficient_rank":expanded["rank"],
                  "expanded_augmented_rank":expanded["rank"],"solution_rank_T":28,"balanced_control_ranks":[36,37],
                  "direct_laurent_cases":3,"direct_laurent_identities":12,"full_block_determinant_powers":4,
                  "metrics":METRICS,"elapsed_seconds":time.perf_counter()-START,
                  "python_version":sys.version,"scientific_processes":1,"configured_blas_threads":1,
                  "thread_settings":{k:os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS","VECLIB_MAXIMUM_THREADS")}}
    if args.produce:
        write_json("verification.json",verification)
    print(json.dumps(verification),flush=True)


if __name__=="__main__":
    main()
