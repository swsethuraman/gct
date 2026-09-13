"""A bounded deeper-occurrence fallback, prioritized by fewer linear singletons.

One linear exchange and two cubic exchanges are genuine degree14 members.
This removes the one-nonsingleton-occurrence restriction on the added cubic.
"""
import argparse
import copy
import json
import time

import b15_01_members as core
from b15_01_extend import exchanges


def replay_move(f,move):
    col=f[move["kind"]] if move["column"]==-1 else f[move["kind"]][move["column"]]
    col[move["position"]]=move["new"]
    f["one"][f["one"].index(move["new"])]=move["old"]


def main(seconds):
    before=core.read("results/b15_01/pilot.json")
    core.save("pilot_after_extension.json",before)
    c13=[m["filling"] for m in core.read("results/ci73/certificate.json")["target_members"] if m["kind"]=="mixed_bracket"]
    parents=[core.lift13(f) for f in c13]
    order=sorted(range(len(parents)),key=lambda j:(sum(c13[j]["val"][x]==1 for x in c13[j]["one"]),j))
    basis=core.Basis()
    rows=before["rows_mod_p"][:]
    members=before["members"][:]
    for row in rows:
        core.need(basis.add(row),"starting basis")
    seen={json.dumps(m["filling"],sort_keys=True) for m in members if m["kind"]=="mixed_bracket"}
    for oldtest in before.get("extension",{}).get("tested",[]):
        desc=oldtest["definition"]
        f=copy.deepcopy(parents[desc["degree13_member"]])
        for move in desc["moves"]:
            replay_move(f,move)
        seen.add(json.dumps(f,sort_keys=True))
    candidates=[]
    grouped=[]
    for parent in order:
        # The first linear placement is a fixed construction choice, not a
        # data-derived vanishing filter. Every successful row is exported.
        linear=list(exchanges(parents[parent],26))
        if not linear:
            continue
        move_l,g=linear[0]
        cubic=list(exchanges(g,27))
        blocks=[]
        for k,(move_c,h) in enumerate(cubic[:8]):
            # Include previously untested double exchanges before deeper moves.
            block=[(dict(phase="focused_double",degree13_member=parent,moves=[move_l,move_c]),h)]
            deeper=list(exchanges(h,27))
            for j,(move_cc,ff) in enumerate(deeper[:8]):
                block.append((dict(phase="two_cubic_occurrences",degree13_member=parent,
                                   moves=[move_l,move_c,move_cc]),ff))
            blocks.append(block)
        grouped.append(blocks)
    for k in range(8):
        for blocks in grouped:
            if k<len(blocks):
                candidates.extend(blocks[k])
    points=core.read("results/b14_prep/points/P14.json")
    symbols=[core.ev.mixed_symbols(pt,points["cubic_exponents"]) for pt in points["points"][:192]]
    core.CALLS=200000
    tested=[]
    started=time.monotonic()
    def checkpoint(reason):
        result=copy.deepcopy(before)
        result.update(members=members,rows_mod_p=rows,rank_mod_p=len(rows),pivot_columns=basis.pivots,reason=reason,
                      focus=dict(tested=tested,candidate_count=len(candidates),parent_order=order,
                                 stats=core.STATS,wall_seconds=time.monotonic()-started,
                                 construction="one linear and up to two added-cubic occurrence exchanges; bounded first8 choices"))
        core.save("pilot.json",result)
    core.log(f"deeper occurrence family {len(candidates)} definitions; initial rank{len(rows)}")
    checkpoint("FOCUS_RUNNING")
    for idx,(desc,f) in enumerate(candidates):
        if time.monotonic()-started>seconds-40:
            break
        key=json.dumps(f,sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        t=time.monotonic()
        vals=core.evaluate(f,symbols,core.P,"focus")
        gain=basis.add(vals)
        tested.append(dict(index=idx,definition=desc,seconds=time.monotonic()-t,nonzero=any(vals),added=gain,rank=len(basis.rows)))
        if gain:
            members.append(dict(kind="mixed_bracket",filling=f,construction=desc))
            rows.append(vals)
            core.log(f"rank {len(rows)}/159, candidate{idx}, parent{desc['degree13_member']}, {desc['phase']}")
        elif len(tested)%8==0:
            core.log(f"tested{len(tested)}, rank{len(rows)}")
        checkpoint("FOCUS_RUNNING")
        if len(rows)==159:
            break
        core.need(len(rows)<159,"rank exceeds dimension")
    checkpoint("FULL_RANK" if len(rows)==159 else "BOUNDED_FOCUS_STOP")
    core.log(f"focus ended at rank{len(rows)} after{len(tested)} evaluated members")


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds",type=int,default=850)
    main(parser.parse_args().seconds)
