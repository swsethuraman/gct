"""Four-point timing controls; no research rank conclusion."""
import json
import time
from b15_06_geometry import (OUT,PRIMES,Evaluator,generate,enumerate_brackets,
                             minor_certificate,save)


def main():
    rows=[]
    selection=json.loads((OUT/'selection.json').read_text())
    # Known rank2 rectangular matrix validates the explicit-minor extraction.
    for p in PRIMES:
        minor=minor_certificate([[1,2,3,4],[0,1,1,1],[1,3,4,5]],p)
        assert minor['rank_lb']==2 and minor['determinant_mod_p']
        assert minor_certificate([[0,0],[0,0]],p)['rank_lb']==0
    for cell in selection['selected']:
        r,t=cell['r'],cell['t'];W=t+2*(r-2);p=PRIMES[0]
        stamp=time.perf_counter()
        bs=enumerate_brackets(W,r-1);ev=Evaluator(bs,r-1,p)
        construction=time.perf_counter()-stamp
        for family in ('GEN','DET','PAD'):
            stamp=time.perf_counter();reds,native=generate(family,r,p,4,151500+r)
            point_seconds=time.perf_counter()-stamp
            stamp=time.perf_counter();values=[ev.values(red) for red in reds]
            evaluation_seconds=time.perf_counter()-stamp
            # Exact JSON round-trip for source indices, used by geometric replay.
            ev2=Evaluator(json.loads(json.dumps(bs)),r-1,p)
            assert ev2.values(reds[0])==values[0]
            rows.append({'r':r,'t':t,'family':family,'points':4,'brackets':len(bs),
                'construction_seconds':construction,'point_seconds':point_seconds,
                'evaluation_seconds':evaluation_seconds,
                'two_prime_full_evaluation_seconds_estimate':2*cell['points']*(point_seconds+evaluation_seconds)/4,
                'estimate_method':'linear scaling of four-point wall time; excludes reduction and replay',
                'rank_not_computed':True})
    save('timing_controls.json',{'status':'RECORDED','rows':rows,
         'known_minor_rank2_and_rank0_controls':True,'source_JSON_roundtrip':True})
    print(json.dumps(rows),flush=True)


if __name__=='__main__':main()
