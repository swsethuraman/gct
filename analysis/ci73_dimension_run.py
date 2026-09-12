import gzip,json,sys,time
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73_dimension as v

def main():
    start=time.monotonic();v.selfcheck_rim()
    root=Path('results/ci73/inputs')
    cert=json.loads((root/'dimension73.json').read_text())
    power=json.loads(gzip.decompress((root/'dimension73_power.json.gz').read_bytes()))
    cubic=v.cubic_exact(13)[13]
    mods={p:v.modular_newton(13,p,True)[13] for p in v.PRIMES}
    h=v.check_hpad(13,cubic,mods,cert,power)
    print('target',h,'seconds',time.monotonic()-start,flush=True)
    a,F=v.ambient13()
    print('ambient',a,'power classes',len(F),'seconds',time.monotonic()-start,flush=True)
    result={'method':'exact Newton power expansion and outer-rim MN','n':4,'degree':13,
            'lambda':[21,17]+[2]*7,'dimension':a,
            'values_are':'exact power-sum coefficients of h_13[h_4]',
            'rows':[[list(rho),c.numerator,c.denominator] for rho,c in sorted(F.items())]}
    Path('results/ci73/ambient13_power.json.gz').write_bytes(gzip.compress(json.dumps(result,separators=(',',':')).encode(),mtime=0))
    Path('results/ci73/dimension_replay.json').write_text(json.dumps({'status':'PASS','target':h,'source':a,'channels':cert['rows'],
            'cubic_classes':len(cubic),'quartic_classes':len(F),'seconds':time.monotonic()-start},indent=2)+'\n')

if __name__=='__main__':main()
