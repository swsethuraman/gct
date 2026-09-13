"""Focused replay for native transport and the full14-subset planner."""
import json
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools/verify"))
import b15_01_ci159 as ci


def main():
    points=ci.read("results/b14_prep/points/P14.json")
    src=ci.read("results/s74/source.json")["entries"]
    old=ci.read("results/b14_07/A14_exact.json.gz")["matrix"]
    symbols=[{4:ci.ev.quartic_symbols(pt,points["cubic_exponents"])} for pt in points["points"][:8]]
    records=[]
    for i in [0,15,39,92]:
        for p in [0,ci.P]:
            t=time.monotonic()
            values=ci.source_row(src[i],symbols,p,"native_control")
            expected=[int(v)%p if p else int(v) for v in old[i][:8]]
            ci.need(values==expected,"native transport fresh values")
            records.append(dict(source_index=i,prime=p,entries=8,seconds=time.monotonic()-t,
                                values=[str(v) for v in values],plan=ci.source_plan(json.dumps(ci.ev.native_source(src[i],src[i]["rung"]),sort_keys=True))))
    # The exact14 planner and the inherited order agree on actual geometry.
    f=ci.ev.native_source(src[39],14)
    before=ci.ev.plan
    ci.ev.plan=ci.ORIGINAL_PLAN
    direct=ci.row(f,symbols[:2],ci.P,"original_order_control")
    ci.ev.plan=before
    optimized=ci.row(f,symbols[:2],ci.P,"exact_order_control")
    ci.need(direct==optimized,"order invariance")
    ci.save("native_transport_controls.json",dict(status="EXACT",records=records,
            order_invariance_checked=True,entries=68,stats=ci.STATS))
    print(json.dumps(dict(status="EXACT",entries=68,stats=ci.STATS)),flush=True)


if __name__=="__main__":
    main()
