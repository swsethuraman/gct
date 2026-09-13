"""Check sparse zero completion and enlarged bounded evaluation batches."""
import gzip
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/b15_01"
sys.path.insert(0,str(ROOT/"tools/verify"))
import b15_01_ci159 as ci
import ci73_io as io


def main():
    cert=io.load(OUT/"certificate.json")
    ci.CERT_DATA={ci.DEPENDENCIES[k]:io.read_reference(ref,OUT) for k,ref in cert["dependencies"].items()}
    original=io.load(ROOT/"results/s74/columns_gen_2147483647.json.gz")["points"][:93]
    completed,symbols=ci.generic_symbols()
    omitted=0
    for a,b in zip(original,completed):
        ca={tuple(k):v for k,v in a["coefficients"]}
        cb={tuple(k):v for k,v in b["coefficients"]}
        if {k:v for k,v in ca.items() if v}!={k:v for k,v in cb.items() if v}:
            raise ValueError("zero completion changed the polynomial")
        omitted+=495-len(ca)
    pts=ci.read("results/b14_prep/points/P14.json")
    syms=[{4:ci.ev.quartic_symbols(p,pts["cubic_exponents"])} for p in pts["points"][:48]]
    source=ci.read("results/s74/source.json")["entries"]
    old=ci.read("results/b14_07/A14_exact.json.gz")
    checks=[]
    for index in (0,39):
        for p in (0,ci.P):
            values=ci.source_row(source[index],syms,p,"batch_control")
            expected=[int(v) for v in old["matrix"][index][:48]]
            if p:
                expected=[v%p for v in expected]
            if values!=expected:
                raise ValueError("enlarged batch changes a native source value")
            checks.append(dict(source_index=index,prime=p,entries=48))
    ci.CERT_DATA=None
    result=dict(status="EXACT",generic_points=93,explicit_zero_coefficients_added=omitted,
                generic_symbols_complete=True,ordinary_polynomials_unchanged=True,
                batch_checks=checks,entries=192,stats=ci.STATS,
                array_budget_bytes=380_000_000,maximum_batch=48)
    (OUT/"export_and_batch_controls.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result),flush=True)


if __name__=="__main__":
    main()
