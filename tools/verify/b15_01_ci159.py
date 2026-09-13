"""Fresh finite N14 rank-floor verification with the accepted CI73 backend.

This entrypoint imports no producer. Complete interpolation is claimed only
when dimension159, a full separating minor, fresh exact source identities,
and a fresh generic source minor all pass. Otherwise it certifies a partial
target rank floor, not global vanishing of the sampled relations.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results/b15_01"
sys.path.insert(0, str(ROOT / "tools/verify"))
import ci73_eval as ev
import ci73_dimension as dim
import ci73_linear as la
from flint import fmpz_mat, nmod_mat

ev.CACHE = OUT / "verification_cache"
P = 2147483647
Q = 2147483629
CALLS = 0
STATS = Counter()
START = time.monotonic()
CERT_DATA = None
PROFILE = "quartic_lmr_degree14_ci159"
PARTIAL_PROFILE = "quartic_lmr_degree14_ci158"
DEPENDENCIES = {
    "members": "results/b15_01/pilot.json",
    "points": "results/b14_prep/points/P14.json",
    "source": "results/s74/source.json",
    "source_values": "results/b14_07/A14_exact.json.gz",
    "kernel": "results/b14_07/K14.json",
    "degree13": "results/ci73/certificate.json",
    "dimension": "results/b14_04/hpad14.json",
    "power": "results/b14_04/hpad14_power.json.gz",
    "generic": "results/s74/columns_gen_2147483647.json.gz",
}
CONVENTIONS = {"coefficient":"ordinary c_alpha; symbol alpha! c_alpha",
               "bracket":"initial-column Leibniz sum; no orbit averaging",
               "orientation":"source rows; point columns; A^T K=0",
               "transport":"u=24*c_(4,0^8); native to degree14"}
ORIGINAL_PLAN=ev.plan


@lru_cache(maxsize=256)
def source_plan(serialized):
    """Full subset contraction-order optimization for fourteen quartic letters.

    Ordering changes cost only. The backend still performs its independently
    signed Leibniz contraction; there is no source-value cache.
    """
    f=json.loads(serialized)
    if len(f["val"])!=14 or f["val"]!=[4]*14:
        return ORIGINAL_PLAN(serialized)
    d=14;h=f["h"];edges=f["two"];full=(1<<d)-1
    a=sum(1<<v for v in f["C1"]);b=sum(1<<v for v in f["C2"])
    neighbors=[[other if v==i else i for i,other in edges if v in (i,other)] for v in range(d)]
    @lru_cache(None)
    def info(mask):
        na=(mask&a).bit_count();nb=(mask&b).bit_count()
        width=sum(bool(mask&(1<<i))!=bool(mask&(1<<j)) for i,j in edges)
        return na,nb,width,math.comb(h,na)*math.comb(h,nb)*(1<<width)
    costs=[None]*(1<<d);costs[0]=(0,())
    for mask in range(1<<d):
        cost,order=costs[mask]
        na,nb,width,states=info(mask)
        for letter in range(d):
            if mask&(1<<letter):
                continue
            opens=sum(not(mask&(1<<q)) for q in neighbors[letter])
            transitions=states*(h-na if a&(1<<letter) else 1)*(h-nb if b&(1<<letter) else 1)*(1<<opens)
            nxt=mask|(1<<letter);candidate=(cost+transitions,order+(letter,))
            if costs[nxt] is None or candidate<costs[nxt]:
                costs[nxt]=candidate
    cost,order=costs[full];mask=0;previous=1;peak=0;width=0
    for letter in order:
        mask|=1<<letter;na,nb,w,states=info(mask)
        peak=max(peak,states+previous);previous=states;width=max(width,w)
    return dict(order=order,transitions=cost,peak_states_pair=peak,frontier=width)


ev.plan=source_plan


def need(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    if CERT_DATA is not None:
        return CERT_DATA[path]
    raw = (ROOT/path).read_bytes()
    return json.loads(gzip.decompress(raw) if path.endswith(".gz") else raw)


def save(name, value):
    path = OUT/name
    raw = (json.dumps(value,separators=(",",":"),sort_keys=True)+"\n").encode()
    if name.endswith(".gz"):
        raw = gzip.compress(raw,mtime=0)
    tmp = path.with_suffix(path.suffix+".tmp")
    tmp.write_bytes(raw)
    tmp.replace(path)


def log(value):
    print(f"[{time.monotonic()-START:.2f}s] {value}",flush=True)


def row(f,symbols,p,label):
    global CALLS
    f = ev.filling(f)
    plan = ev.plan(json.dumps(f,sort_keys=True))
    unit = plan["peak_states_pair"]*(8 if p else 32)
    need(unit <= 380_000_000,"single-point array bound")
    batch = min(48,max(1,380_000_000//max(1,unit)))
    values = []
    for offset in range(0,len(symbols),batch):
        CALLS += 1
        v,r = ev.evaluate(f,symbols[offset:offset+batch],p,
                          name=f"b15_01_verify_{os.getpid()}_{label}_{CALLS}",seconds=100)
        values.extend(v)
        STATS["backend_wall_seconds"] += r["wall_seconds"]
        STATS["entries"] += len(v)
        STATS["max_array_bytes"] = max(STATS["max_array_bytes"],r["peak_array_bytes"])
    return values


def source_row(entry,symbols,p,label):
    degree=entry["rung"]
    values=row(ev.native_source(entry,degree),symbols,p,label)
    expo=14-degree
    result=[v*s[4][(4,)+(0,)*8]**expo for v,s in zip(values,symbols)]
    return [v%p for v in result] if p else result


def generic_symbols():
    """Validate all generic input data before starting costly evaluation."""
    generic=read("results/s74/columns_gen_2147483647.json.gz")
    gpoints=generic["points"][:93]
    need(len(gpoints)==93,"generic point count")
    symbols=[]
    for point in gpoints:
        need(point["type"]=="form","generic point kind")
        need(len(point["coefficients"])==495 and all(type(v) is int and len(alpha)==9 and
             all(type(x) is int and x>=0 for x in alpha) and sum(alpha)==4 for alpha,v in point["coefficients"]),"generic integral coefficient data")
        coeff={tuple(alpha):v for alpha,v in point["coefficients"]}
        need(set(coeff)==set(ev.exps(4,9)),"generic coefficient completeness")
        symbols.append({4:{a:v*math.prod(math.factorial(x) for x in a) for a,v in coeff.items()}})
    return gpoints,symbols


def main(skip_generic=False):
    progress = dict(status="RUNNING", model="gpt-6-astra", profile="b15_01_partial_N14")
    save("verification.json",progress)
    pilot = read("results/b15_01/pilot.json")
    members = pilot["members"]
    r = len(members)
    need(88 <= r <= 159 and pilot["rank_mod_p"] == r,"rank label")
    need(pilot["prime"] == P,"pilot modulus")
    cols = pilot["pivot_columns"]
    need(len(cols)==r and len(set(cols))==r and all(0<=j<192 for j in cols),"minor columns")
    pts = read("results/b14_prep/points/P14.json")
    source = read("results/s74/source.json")["entries"][:93]
    old = read("results/b14_07/A14_exact.json.gz")
    need(len(source)==93,"source count")
    for i,e in enumerate(source):
        need(e["index"] == i and e["native"]["delta"] == e["rung"],"source indices/degrees")
        need(e["key"] == old["rows"][i]["key"],"original source keys")
        need(e["key"] == [e["native"][k] for k in ("C1","C2","two","one")],"native source differs from its key")
        f=ev.native_source(e,14)
        need(f["h"]==9 and len(f["two"])==15 and len(f["one"])==8,"source highest weight")
        literal=e["literal"]
        need(literal["n"]==4 and literal["delta"]==24 and e["exponent"]==24-e["rung"],"degree24 literal metadata")
        lifted=ev.filling(dict(h=literal["h"],val=[4]*24,**{k:literal[k] for k in ("C1","C2","two","one")}))
        need(ev.native_source(e,24)==lifted,"literal degree24 transport")
    kj = read("results/b14_07/K14.json")
    ci = read("results/ci73/certificate.json")
    ratios = [3,-2,6]
    for j,scale in enumerate(ratios):
        need(all(Fraction(ci["kernel"]["entries"][i][j])*Fraction(ci["source_rows"][i]["scale"])
                 == scale*kj["kernel_columns"][j][i] for i in range(39)),"exact degree13 normalization comparison")
        need(not any(kj["kernel_columns"][j][39:]),"degree13 trailing coordinates")
    save("kernel_comparison.json",dict(status="EXACT",
         convention="effective CI73 column j = scale[j] times K14 column j on first39 coordinates",
         scale=ratios,degree14_transport="multiply the degree13 polynomials by u",
         remaining_independent_columns_zero_based=[3,4],remaining_last_nonzero_indices=[91,92]))
    all_primes=[2147483647,2147483629,2147483587,2147483579,2147483563,2147483549,2147483543]
    need(all(all(p%d for d in range(2,math.isqrt(p)+1)) for p in all_primes),"prime validation")
    H=math.factorial(9)**2*2**15*1176**14
    need(math.prod(all_primes)>2*H,"CRT signed margin")
    stored=fmpz_mat([[int(v) for v in row] for row in old["matrix"]])
    kernel=fmpz_mat([[v[i] for v in kj["kernel_columns"]] for i in range(93)])
    need(stored.nrows()==93 and stored.ncols()==212 and kernel.rank()==5,"stored source/kernel sizes")
    need((stored.transpose()*kernel).is_zero(),"stored exact source kernel identities")
    for m in members:
        if m["kind"]=="source_pullback":
            need(type(m["source_index"]) is int and 0<=m["source_index"]<93 and m["degree"]==14,"source member definition")
        else:
            need(m["kind"] in ("mixed_bracket","hybrid_bracket"),"unknown member kind")
            f=ev.filling(m["filling"])
            counts=Counter(f["val"])
            need(f["h"]==9 and len(f["two"])==15 and len(f["one"])==8 and counts[4]+counts[1]==14 and counts[4]+counts[3]==14,"mixed/hybrid membership preflight")
            need(m["kind"]=="hybrid_bracket" or counts[4]==0,"mixed type mismatch")
    ce = pts["cubic_exponents"]
    need(len(ce)==165 and all(len(a)==9 and all(type(x) is int and x>=0 for x in a) and sum(a)==3 for a in ce)
         and len(set(map(tuple,ce)))==165 and set(map(tuple,ce))==set(ev.exps(3,9)),"complete integral cubic exponent ordering")
    selected = [pts["points"][j] for j in cols]
    for pt in selected:
        need(len(pt["linear"])==9 and len(pt["cubic_coefficients"])==165,"point dimensions")
        need(all(type(x) is int and abs(x)<=7 for x in pt["linear"]+pt["cubic_coefficients"]),"point integral coefficient bound")
    need(all(pilot["point_ids"][j] == pts["points"][j]["id"] for j in range(192)),"point identity")
    mixed = [ev.mixed_symbols(pt,ce) for pt in selected]
    quartic = [{4:ev.quartic_symbols(pt,ce)} for pt in selected]
    for pt,s in zip(selected,quartic):
        need(s[4][(4,)+(0,)*8]==pt["u_symbol"],"point u normalization")
        need(max(abs(v) for v in s[4].values())==pt["max_abs_quartic_symbol"],"point maximum symbol normalization")
    hybrid=[dict(m,**{}) for m in mixed]
    for m,q in zip(hybrid,quartic):
        m[4]=q[4]
    if not skip_generic:
        gpoints,gsymbols=generic_symbols()
    fresh = []
    for i,m in enumerate(members):
        if m["kind"] == "source_pullback":
            k = m["source_index"]
            need(type(k) is int and 0<=k<93 and m["degree"]==14,"source reference")
            values = source_row(source[k],quartic,P,"source")
        else:
            need(m["kind"] in ("mixed_bracket","hybrid_bracket"),"unrecognized member")
            f = ev.filling(m["filling"])
            need(f["h"]==9 and len(f["two"])==15 and len(f["one"])==8,"mixed shape")
            counts=Counter(f["val"])
            need(counts[4]+counts[1]==14 and counts[4]+counts[3]==14,"mixed/hybrid bidegree")
            # Evaluate the full expanded degree14 definition, independently of
            # the producer's degree13-factor shortcut and construction metadata.
            values = row(f,hybrid if m["kind"]=="hybrid_bracket" else mixed,P,"mixed")
        need(values == [pilot["rows_mod_p"][i][j] for j in cols],"fresh member mismatch")
        fresh.append(values)
        if i % 10 == 0 or i+1==r:
            log(f"fresh member rows {i+1}/{r}")
    determinant = int(nmod_mat(fresh,P).det())
    need(determinant != 0,"fresh full partial minor singular")
    save("fresh_target_minor.json",dict(status="REPLAYED_RANK_FLOOR",rank_lb=r,
         prime=P,determinant=determinant,member_indices=list(range(r)),point_indices=cols,
         point_ids=[pt["id"] for pt in selected],rows_mod_p=fresh,
         membership="validated integral degree14 source pullbacks or initial-column mixed brackets",
         source="pilot.json definitions, independently evaluated from full degree14 fillings"))
    log(f"fresh {r}-minor determinant {determinant} modulo {P}")
    progress.update(target_rank_lb=r,target_dimension_ub=159,target_minor=determinant,
                    source_basis="NOT_REPLAYED",complete_interpolation=False)
    save("verification.json",progress)
    # Exact independent dimension calculations, not stored labels.
    dim.selfcheck_rim()
    ep = dim.cubic_exact(14)[14]
    mp = {p:dim.modular_newton(14,p,cubic_outer=True)[14] for p in (P,Q)}
    h = dim.check_hpad(14,ep,mp,read("results/b14_04/hpad14.json"),read("results/b14_04/hpad14_power.json.gz"))
    ap = dim.power_plethysm(4,14)
    a = sum(v*dim.character((25,17)+(2,)*7,k) for k,v in ap.items())
    need(a==93 and h==159,"independent dimension disagreement")
    dim.character.cache_clear()
    progress.update(ambient_dimension=93,target_dimension=159,literal_u10_transport_checked=True,
                    degree24_coordinate_extension_zero_rows=181)
    log("fresh source and target dimensions93/159 PASS")
    if not skip_generic:
        rows = []
        for i,e in enumerate(source):
            rows.append(source_row(e,gsymbols,P,"generic"))
            if i % 15 == 0:
                log(f"fresh generic source rows {i+1}/93")
        gd = int(nmod_mat(rows,P).det())
        need(gd!=0,"generic source completeness minor")
        save("generic_source_minor.json.gz",dict(status="REPLAYED_RANK_FLOOR",rank_lb=93,
             prime=P,determinant=gd,points=gpoints,source_indices=list(range(93)),
             values=rows,degree=14,convention="literal native*u^(14-rung), ordinary generic coefficients"))
        progress.update(source_basis="fresh rank93 plus independently recomputed ambient93",
                        generic_determinant=gd)
        save("verification.json",progress)
        log(f"fresh source completeness determinant {gd}")
    if r>=158 and not skip_generic:
        # A global kernel statement additionally needs exact identities of the
        # actual polynomials at the separating points, not residue zeros.
        H = math.factorial(9)**2*2**15*1176**14
        need(2**256>2*H,"signed integer reconstruction bound")
        need(all(abs(v)<=1176 for s in quartic for v in s[4].values()),"point symbol bound")
        exact = []
        for i,e in enumerate(source):
            vals = source_row(e,quartic,0,"integer")
            need(vals == [int(old["matrix"][i][j]) for j in cols],"fresh integer source mismatch")
            need(all(abs(v)<=H for v in vals),"integer value bound")
            exact.append(vals)
            if i % 15 == 0:
                log(f"fresh exact source rows {i+1}/93")
        kj = read("results/b14_07/K14.json")
        K = fmpz_mat([[v[i] for v in kj["kernel_columns"]] for i in range(93)])
        A = fmpz_mat(exact)
        need(K.rank()==5 and (A.transpose()*K).is_zero(),"fresh rational source identities")
        need(A.rank()==88,"exact source matrix rank")
        save("fresh_source_values.json.gz",dict(status="EXACT",source_indices=list(range(93)),
             point_indices=cols,values=[[str(x) for x in row] for row in exact],
             kernel_columns=kj["kernel_columns"],kernel_rank=5,source_rank=88,
             integer_modulus=str(2**256),integer_bound=str(H),signed_margin=str(2**256-2*H)))
        progress.update(fresh_exact_source_entries=93*r,global_kernel_lb=5-(159-r),
                        complete_interpolation=(r==159))
    else:
        progress.update(global_kernel_lb=3,global_kernel_evidence="inherited accepted CI73; no improvement from this partial minor")
    hashes = {n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in
              ["results/b15_01/pilot.json","results/s74/source.json","results/b14_prep/points/P14.json",
               "results/s74/columns_gen_2147483647.json.gz","analysis/b15_01_verify.py",
               "tools/verify/ci73_eval.py","tools/verify/ci73_backend.cs","tools/verify/ci73_dimension.py"]}
    progress.update(status="EXACT" if progress.get("global_kernel_lb",0)>=4 else "REPLAYED_RANK_FLOOR",
                    stats=STATS,wall_seconds=time.monotonic()-START,input_hashes=hashes)
    save("verification.json",progress)
    log(json.dumps(progress))
    return progress


def schema(c):
    need(type(c) is dict and set(c)==set("format kind profile title produced_by field cell conventions dependencies claim".split()),"CI159 certificate keys")
    need(c["format"]=="gct-cert/1" and ((c["kind"]=="complete_interpolation" and c["profile"]==PROFILE)
         or (c["kind"]=="partial_interpolation" and c["profile"]==PARTIAL_PROFILE)),"CI14 profile/kind")
    need(c["field"]=="Q" and c["cell"]==dict(n=4,r=9,delta=14,**{"lambda":[25,17]+[2]*7}),"CI159 field/cell")
    need(c["conventions"]==CONVENTIONS,"CI159 conventions")
    need(all(type(c[k]) is str and bool(c[k].strip()) for k in ("title","produced_by")),"CI159 attribution")
    need(type(c["dependencies"]) is dict and set(c["dependencies"])==set(DEPENDENCIES),"CI159 dependency keys")
    expected=(dict(source_dimension=93,target_dimension=159,source_rank_Q=88,i_red14=5) if c["profile"]==PROFILE else
              dict(source_dimension=93,target_dimension=159,target_rank_lb=158,sampled_source_rank_Q=88,i_red14_lb=4,i_red14_ub=5))
    need(c["claim"]==expected,"CI14 claim")
    for ref in c["dependencies"].values():
        need(type(ref) is dict and set(ref)=={"path","canonical_sha256"},"CI159 reference")


def verify(c,root):
    """Shared-verifier entry: snapshots are hashed, then values are regenerated."""
    global CERT_DATA, START
    import ci73_io as io
    checks=[]
    try:
        schema(c)
        CERT_DATA={DEPENDENCIES[k]:io.read_reference(ref,root) for k,ref in c["dependencies"].items()}
        pilot=CERT_DATA[DEPENDENCIES["members"]]
        full=c["profile"]==PROFILE
        expected_rank=159 if full else 158
        need(len(pilot["members"])==expected_rank and pilot["rank_mod_p"]==expected_rank,"target rank required by interpolation profile")
        checks.append(dict(check="CI159 schema and canonical input identities",ok=True))
        START=time.monotonic()
        STATS.clear()
        result=main(False)
        need(result["complete_interpolation"]==full and result["global_kernel_lb"]==expected_rank-154,"interpolation gates")
        checks += [dict(check="fresh integral target minor",ok=True,detail=dict(rank=expected_rank,prime=P,determinant=result["target_minor"])),
                   dict(check="independent complete dimensions",ok=True,detail=dict(source=93,target=159)),
                   dict(check="fresh generic source completeness",ok=True,detail=dict(rank=93,prime=P,determinant=result["generic_determinant"])),
                   dict(check="fresh exact source identities and rational kernel",ok=True,detail=dict(entries=result["fresh_exact_source_entries"],rank_Q=88,kernel_rank=5)),
                   dict(check="global reducible ideal multiplicity bound",ok=True,detail=dict(i_red14_lb=expected_rank-154,i_red14_ub=5,field="Q"))]
        return dict(status="PASS",checks=checks,claim=c["claim"])
    except Exception as exc:
        return dict(status="FAIL",checks=checks,code="CI159 verification",detail=str(exc))
    finally:
        CERT_DATA=None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-generic",action="store_true")
    args=parser.parse_args()
    main(args.skip_generic)
