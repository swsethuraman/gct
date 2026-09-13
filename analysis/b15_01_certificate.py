"""Export self-contained canonical CI159 input snapshots, then replay controls."""
import argparse
import copy
import gzip
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/b15_01"
sys.path.insert(0,str(ROOT/"tools/verify"))
import ci73_io as io
import b15_01_ci159 as ci


def build():
    data={k:ci.read(path) for k,path in ci.DEPENDENCIES.items()}
    rank=data["members"]["rank_mod_p"]
    need=rank in (158,159)
    if not need:
        raise ValueError("No interpolation bound certificate before rank158")
    # Retain every definition/point/value the independent verifier consumes;
    # omit large unrelated source rungs and unused generic bank fields.
    data["source"]={"entries":data["source"]["entries"][:93]}
    data["generic"]={"points":data["generic"]["points"][:93]}
    # S74 serializes nonzero ordinary coefficients only. Expand this sparse
    # polynomial representation; omitted monomials have coefficient zero.
    exponents=ci.ev.exps(4,9)
    for point in data["generic"]["points"]:
        pairs=point["coefficients"]
        coeff={tuple(a):v for a,v in pairs}
        if len(coeff)!=len(pairs) or not set(coeff)<=set(exponents) or not all(type(v) is int for v in coeff.values()):
            raise ValueError("invalid sparse S74 generic point")
        point["coefficients"]=[[list(a),coeff.get(a,0)] for a in exponents]
    keep=("members","rank_mod_p","prime","pivot_columns","point_ids","rows_mod_p")
    data["members"]={k:data["members"][k] for k in keep}
    folder=OUT/"ci159_inputs"
    folder.mkdir(exist_ok=True)
    deps={}
    for k,value in data.items():
        path=folder/(k+".json.gz")
        raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()
        path.write_bytes(gzip.compress(raw,mtime=0))
        deps[k]=io.reference(path,OUT)
    full=rank==159
    cert=dict(format="gct-cert/1",kind="complete_interpolation" if full else "partial_interpolation",profile=ci.PROFILE if full else ci.PARTIAL_PROFILE,
              title="Degree14 complete interpolation" if full else "Degree14 partial interpolation proves a fourth reducible equation",
              produced_by="B15-01, gpt-6-astra; S74/B14-07 inputs retain original attribution",
              field="Q",cell=dict(n=4,r=9,delta=14,**{"lambda":[25,17]+[2]*7}),
              conventions=ci.CONVENTIONS,dependencies=deps,
              claim=(dict(source_dimension=93,target_dimension=159,source_rank_Q=88,i_red14=5) if full else
                     dict(source_dimension=93,target_dimension=159,target_rank_lb=158,sampled_source_rank_Q=88,i_red14_lb=4,i_red14_ub=5)))
    ci.schema(cert)
    (OUT/"certificate.json").write_text(json.dumps(cert,indent=2)+"\n",encoding="utf-8")
    print("Interpolation certificate exported, rank"+str(rank),flush=True)


def controls():
    cert=io.load(OUT/"certificate.json")
    import verify as shared
    legacy=io.load(ROOT/"results/ci73/certificate.json")
    if shared.validate(legacy)!="complete_interpolation" or shared.validate(cert)!=cert["kind"]:
        raise ValueError("shared schema dispatch regression")
    (OUT/"shared_schema_regression.json").write_text(json.dumps(dict(status="EXACT",
        legacy_profile=legacy["profile"],legacy_schema_accepted=True,
        new_profile=cert["profile"],new_schema_accepted=True),indent=2)+"\n",encoding="utf-8")
    records=[]
    for label,edit in [
        ("wrong claim",lambda c:c["claim"].update(i_red14=4)),
        ("wrong degree",lambda c:c["cell"].update(delta=13)),
        ("wrong normalization",lambda c:c["conventions"].update(coefficient="ordinary only")),
        ("unknown field",lambda c:c.update(unregistered=True)),
        ("changed input digest",lambda c:c["dependencies"]["members"].update(canonical_sha256="0"*64)),
        ("escaping reference",lambda c:c["dependencies"]["members"].update(path="../pilot.json")),
    ]:
        c=copy.deepcopy(cert)
        edit(c)
        result=ci.verify(c,OUT)
        if result["status"]=="PASS":
            raise ValueError("altered certificate accepted: "+label)
        records.append(dict(control=label,status=result["status"],reason=result["detail"]))
    if cert["profile"]==ci.PARTIAL_PROFILE:
        c=copy.deepcopy(cert)
        c["kind"]="complete_interpolation";c["profile"]=ci.PROFILE
        c["claim"]=dict(source_dimension=93,target_dimension=159,source_rank_Q=88,i_red14=5)
        result=ci.verify(c,OUT)
        if result["status"]=="PASS":
            raise ValueError("rank158 accepted as complete159")
        records.append(dict(control="rank158 cannot certify all five equations",status=result["status"],reason=result["detail"]))
        c=copy.deepcopy(cert)
        m=io.read_reference(c["dependencies"]["members"],OUT)
        m["members"]=m["members"][:-1];m["rows_mod_p"]=m["rows_mod_p"][:-1]
        m["pivot_columns"]=m["pivot_columns"][:-1];m["rank_mod_p"]=157
        path=OUT/"ci159_inputs/b15_01_altered_rank_control.json.gz"
        path.write_bytes(gzip.compress(json.dumps(m,separators=(",",":"),sort_keys=True).encode(),mtime=0))
        c["dependencies"]["members"]=io.reference(path,OUT)
        result=ci.verify(c,OUT)
        if result["status"]=="PASS":
            raise ValueError("rank157 accepted as a fourth equation bound")
        records.append(dict(control="rank157 cannot certify four equations",status=result["status"],reason=result["detail"]))
    # Saved values never constitute a fresh evaluation. Mutate the first source
    # value and recompute the canonical reference digest. The data-level error
    # must be caught by an actual new polynomial evaluation of that row.
    c=copy.deepcopy(cert)
    m=io.read_reference(c["dependencies"]["members"],OUT)
    m["rows_mod_p"][0][m["pivot_columns"][0]]=(m["rows_mod_p"][0][m["pivot_columns"][0]]+1)%ci.P
    path=OUT/"ci159_inputs/b15_01_altered_member_control.json.gz"
    path.write_bytes(gzip.compress(json.dumps(m,separators=(",",":"),sort_keys=True).encode(),mtime=0))
    c["dependencies"]["members"]=io.reference(path,OUT)
    # The authentic receipt is preserved because the adversarial run starts its
    # own RUNNING record; restore it after retaining that control's outcome.
    authentic=(OUT/"verification.json").read_bytes()
    result=ci.verify(c,OUT)
    (OUT/"verification.json").write_bytes(authentic)
    if result["status"]=="PASS" or "fresh member mismatch" not in result.get("detail",""):
        raise ValueError("altered value did not fail in fresh evaluation: "+str(result))
    records.append(dict(control="altered value with recomputed digest",status=result["status"],reason=result["detail"]))
    (OUT/"shared_verifier_controls.json").write_text(json.dumps(dict(status="EXACT",controls=records),indent=2)+"\n",encoding="utf-8")
    print(str(len(records))+" interpolation altered-input controls rejected",flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("mode",choices=["build","controls"])
    args=parser.parse_args()
    build() if args.mode=="build" else controls()
