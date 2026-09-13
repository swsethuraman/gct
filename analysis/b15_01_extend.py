"""B15-01 optional measured extension: move both added letters explicitly.

The pilot's cubic-only exchanges leave the new linear letter as a singleton.
This bounded family removes that restriction. It makes no spanning assertion.
"""
import argparse
import copy
import hashlib
import json
import time
from pathlib import Path

import b15_01_members as core


def exchanges(f,new,old_val=3):
    for kind,number,col in [("C1",-1,f["C1"]),("C2",-1,f["C2"])]+[("two",j,c) for j,c in enumerate(f["two"])]:
        for pos,old in enumerate(col):
            if f["val"][old]!=old_val or new in col:
                continue
            g=copy.deepcopy(f)
            (g[kind] if number==-1 else g[kind][number])[pos]=new
            g["one"][g["one"].index(new)]=old
            core.verify_member(g)
            # Two identical linear forms in an alternating column give zero
            # identically. This is a structural identity, not sampled pruning.
            if any(sum(g["val"][x]==1 for x in c)>1 for c in [g["C1"],g["C2"]]+g["two"]):
                continue
            yield dict(kind=kind,column=number,position=pos,old=old,new=new),g


def main(seconds):
    original=core.read("results/b15_01/pilot.json")
    core.save("pilot_initial.json",original)
    pts=core.read("results/b14_prep/points/P14.json")
    symbols=[core.ev.mixed_symbols(pt,pts["cubic_exponents"]) for pt in pts["points"][:192]]
    c13=[m["filling"] for m in core.read("results/ci73/certificate.json")["target_members"] if m["kind"]=="mixed_bracket"]
    parents=[core.lift13(f) for f in c13]
    basis=core.Basis()
    rows=original["rows_mod_p"][:]
    members=original["members"][:]
    for row in rows:
        core.need(basis.add(row),"initial independent basis")
    # A different label prevents backend files from overwriting pilot receipts.
    core.CALLS=100000
    candidates=[]
    per_parent=[]
    for parent,f in enumerate(parents):
        linear=list(exchanges(f,26))
        cubic=list(exchanges(f,27))
        local=[]
        # Rotate parent-dependent positions, while keeping the sequence explicit.
        for k in range(max(len(linear),len(cubic))):
            if k<len(linear):
                desc,g=linear[k]
                local.append((dict(phase="linear_exchange",degree13_member=parent,moves=[desc]),g))
                second=list(exchanges(g,27))
                if second:
                    desc2,h=second[(parent+k)%len(second)]
                    local.append((dict(phase="double_exchange",degree13_member=parent,moves=[desc,desc2]),h))
            if k<len(cubic):
                desc,g=cubic[k]
                local.append((dict(phase="cubic_exchange_reordered",degree13_member=parent,moves=[desc]),g))
        per_parent.append(local)
    for k in range(max(map(len,per_parent))):
        for local in per_parent:
            if k<len(local):
                candidates.append(local[k])
    # Avoid already accepted polynomial definitions. Exact column order remains
    # in the key; this is not a claim to recognize every polynomial equality.
    seen={json.dumps(m["filling"],sort_keys=True) for m in members if m["kind"]=="mixed_bracket"}
    seen.update(json.dumps(f,sort_keys=True) for f in parents)
    for test in original["tested"]:
        desc=test["definition"]
        if desc["phase"]=="exchange":
            f=copy.deepcopy(parents[desc["degree13_member"]])
            change=desc["move"]
            col=f[change["kind"]] if change["column"]==-1 else f[change["kind"]][change["column"]]
            col[change["position"]]=change["new"]
            f["one"][f["one"].index(change["new"])]=change["old"]
            seen.add(json.dumps(f,sort_keys=True))
    tested=[]
    begun=time.monotonic()
    next_index=0
    def checkpoint(reason):
        rec=copy.deepcopy(original)
        rec.update(members=members,rows_mod_p=rows,rank_mod_p=len(rows),pivot_columns=basis.pivots,
                   reason=reason,extension=dict(candidate_count=len(candidates),next_candidate_index=next_index,
                   tested=tested,stats=core.STATS,wall_seconds=time.monotonic()-begun,
                   construction="linear, cubic and double occurrence exchanges; structural repeated-linear-column zero test",
                   program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
        core.save("pilot.json",rec)
    core.log(f"measured extension from rank{len(rows)}, finite candidate count{len(candidates)}")
    checkpoint("EXTENSION_RUNNING")
    last_gain=time.monotonic()
    for idx,(desc,f) in enumerate(candidates):
        if time.monotonic()-begun>seconds-25:
            break
        key=json.dumps(f,sort_keys=True)
        next_index=idx+1
        if key in seen:
            continue
        seen.add(key)
        t=time.monotonic()
        values=core.evaluate(f,symbols,core.P,"extension")
        gain=basis.add(values)
        tested.append(dict(index=idx,definition=desc,seconds=time.monotonic()-t,nonzero=any(values),added=gain,rank=len(basis.rows)))
        if gain:
            rows.append(values)
            members.append(dict(kind="mixed_bracket",filling=f,construction=desc))
            last_gain=time.monotonic()
            core.log(f"rank {len(rows)}/159: candidate {idx}, {desc['phase']}")
        elif len(tested)%8==0:
            core.log(f"candidate {idx}, rank {len(rows)}")
        checkpoint("EXTENSION_RUNNING")
        if len(rows)==159:
            break
        core.need(len(rows)<159,"rank exceeds dimension")
        if len(tested)>=50 and time.monotonic()-last_gain>300:
            core.log("measured 300-second plateau after at least50 members")
            break
    checkpoint("FULL_RANK" if len(rows)==159 else "BOUNDED_EXTENSION_STOP")
    core.log(f"extension ended at rank {len(rows)}/159 after {len(tested)} evaluated members")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds",type=int,default=1700)
    main(parser.parse_args().seconds)
