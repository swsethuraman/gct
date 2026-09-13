"""Explicit mixed diagrams with quartic letters evaluated on ell*c.

This includes source15, the member completing the accepted degree13 target.
Equivariant substitution gives genuine N14 members without expanding each
quartic letter into four linear/cubic placements. No polynomial values are
borrowed from a sampled matrix.
"""
import argparse
import copy
import json
import time
from collections import Counter
import random

import b15_01_members as core


def membership(f):
    f=core.ev.filling(f)
    counts=Counter(f["val"])
    core.need(counts[4]+counts[1]==14 and counts[4]+counts[3]==14,"hybrid bidegree")
    core.need(f["h"]==9 and len(f["two"])==15 and len(f["one"])==8,"hybrid weight")
    return f


def move(f,new,slot):
    kind,colnum,pos=slot
    g=copy.deepcopy(f)
    col=g[kind] if colnum==-1 else g[kind][colnum]
    if new in col or g["val"][col[pos]]!=4 or new not in g["one"]:
        return None
    old=col[pos]
    col[pos]=new
    g["one"][g["one"].index(new)]=old
    return membership(g)


def split_letter(f,letter):
    """Polar identity: sum of these four diagrams replaces m4(ell*c).

    Each summand separately has the same bidegree and highest weight, since
    all column shapes are unchanged and substitution is equivariant.
    """
    places=[]
    for kind,colnum,col in [("C1",-1,f["C1"]),("C2",-1,f["C2"]),("one",-1,f["one"])]+[("two",j,c) for j,c in enumerate(f["two"])]:
        places += [(kind,colnum,k) for k,x in enumerate(col) if x==letter]
    core.need(len(places)==4 and f["val"][letter]==4,"quartic split valence")
    result=[]
    for place in places:
        g=copy.deepcopy(f)
        new=len(g["val"])
        g["val"][letter]=3
        g["val"].append(1)
        kind,j,k=place
        (g[kind] if j==-1 else g[kind][j])[k]=new
        result.append((dict(letter=letter,linear_occurrence=place),membership(g)))
    return result


def main(seconds):
    rng=random.Random(150115)
    ce=core.ev.exps(3,2)
    controls=[]
    for trial in range(4):
        pt=dict(linear=[rng.randint(-4,4) for _ in range(2)],cubic_coefficients=[rng.randint(-4,4) for _ in ce])
        s=core.ev.mixed_symbols(pt,ce)
        s[4]=core.ev.quartic_symbols(pt,ce)
        f=dict(h=2,val=[4,1,3],C1=[0,1],C2=[0,2],two=[[0,2]],one=[0,2])
        want=core.ev.literal(f,s)
        for p in [0,core.P,2147483629]:
            got=core.evaluate(f,[s],p,"hybrid_control")
            core.need(got==[want%p if p else want],"literal hybrid control")
        controls.append(dict(point=pt,exact_value=want))
    core.need(any(c["exact_value"] for c in controls),"hybrid source liveness")
    core.save("hybrid_controls.json",dict(status="EXACT",filling=f,cubic_exponents=ce,controls=controls,comparisons=12))
    before=core.read("results/b15_01/pilot.json")
    core.save("pilot_before_hybrid.json",before)
    basis=core.Basis()
    members=before["members"][:]
    rows=before["rows_mod_p"][:]
    for row in rows:
        core.need(basis.add(row),"starting hybrid basis")
    source=core.read("results/s74/source.json")["entries"][:39]
    parents=[]
    for e in source:
        f=core.ev.native_source(e,13)
        f["val"] += [1,3]
        f["one"] += [13,14,14,14]
        parents.append(membership(f))
    slots=[("C1",-1,j) for j in range(9)]+[("C2",-1,j) for j in range(9)]+[("two",j,k) for j in range(15) for k in range(2)]
    # Include every source parent and individually polarized pieces of the
    # accepted completing source15. Interleave these sources deterministically.
    variants=[(dict(source13_index=15),parents[15])]
    for j in range(39):
        if j<13:
            for split,g in split_letter(parents[15],j):
                variants.append((dict(source13_index=15,quartic_split=split),g))
        if j!=15:
            variants.append((dict(source13_index=j),parents[j]))
    candidates=[]
    for k,slot in enumerate(slots):
        for origin,f in variants:
            configurations=[[(14,slot)],[(13,slot)],
                            [(13,slot),(14,slots[(k+9)%48])],
                            [(13,slot),(14,slots[(k+9)%48]),(14,slots[(k+18)%48])]]
            for swaps in configurations:
                g=f
                for new,location in swaps:
                    g=move(g,new,location)
                    if g is None:
                        break
                if g is not None:
                    candidates.append((dict(origin,swaps=swaps),g))
    pts=core.read("results/b14_prep/points/P14.json")
    symbols=[]
    for pt in pts["points"][:192]:
        s=core.ev.mixed_symbols(pt,pts["cubic_exponents"])
        s[4]=core.ev.quartic_symbols(pt,pts["cubic_exponents"])
        symbols.append(s)
    base=core.evaluate(parents[15],symbols[:3],0,"hybrid_polar_base")
    pieces=split_letter(parents[15],0)
    polar=[core.evaluate(g,symbols[:3],0,"hybrid_polar_piece") for desc,g in pieces]
    core.need([sum(row[j] for row in polar) for j in range(3)]==base,"exact polarized quartic substitution identity")
    old=core.read("results/b14_07/A14_exact.json.gz")["matrix"][15]
    core.need([4*v for v in base]==[int(x) for x in old[:3]],"hybrid u/4 source normalization")
    core.save("hybrid_polar_control.json",dict(status="EXACT",source13_index=15,quartic_letter=0,
              point_indices=[0,1,2],base_filling=parents[15],base_values=[str(x) for x in base],
              pieces=[dict(split=desc,filling=g,values=[str(x) for x in vals]) for (desc,g),vals in zip(pieces,polar)],
              identity="sum of four polarized diagrams = unsplit quartic-on-ell*c diagram = degree14 source15/4"))
    tested=[]
    seen=set()
    started=time.monotonic()
    core.CALLS=300000
    def checkpoint(reason):
        rec=copy.deepcopy(before)
        rec.update(members=members,rows_mod_p=rows,rank_mod_p=len(rows),pivot_columns=basis.pivots,reason=reason,
                   hybrid=dict(tested=tested,candidate_count=len(candidates),stats=core.STATS,wall_seconds=time.monotonic()-started,
                               definition="val4 on ell*c, val1 on ell, val3 on c; integral initial-column Leibniz sum"))
        core.save("pilot.json",rec)
    core.log(f"hybrid rank{len(rows)}; {len(candidates)} explicit definitions; 15 or16 letters per diagram")
    checkpoint("HYBRID_RUNNING")
    for idx,(desc,f) in enumerate(candidates):
        if time.monotonic()-started>seconds-40:
            break
        key=json.dumps(f,sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        t=time.monotonic()
        vals=core.evaluate(f,symbols,core.P,"hybrid")
        gain=basis.add(vals)
        tested.append(dict(index=idx,definition=desc,seconds=time.monotonic()-t,added=gain,nonzero=any(vals),rank=len(basis.rows)))
        if gain:
            members.append(dict(kind="hybrid_bracket",filling=f,construction=desc))
            rows.append(vals)
            core.log(f"rank {len(rows)}/159, hybrid candidate{idx}, source13 index{desc['source13_index']}")
        elif len(tested)%8==0:
            core.log(f"hybrid tested{len(tested)}, rank{len(rows)}")
        checkpoint("HYBRID_RUNNING")
        if len(rows)==159:
            break
        core.need(len(rows)<159,"rank exceeds proved dimension")
    checkpoint("FULL_RANK" if len(rows)==159 else "BOUNDED_HYBRID_STOP")
    core.log(f"hybrid ended at rank{len(rows)} after{len(tested)} evaluated members")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds",type=int,default=550)
    main(parser.parse_args().seconds)
