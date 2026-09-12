"""Full fresh CI73 verifier run with a machine-readable result."""
import json,sys
from pathlib import Path
sys.path.insert(0,str(Path('tools/verify').resolve()))
import ci73,ci73_io

def main():
    path=Path('results/ci73/certificate.json')
    result=ci73.verify(ci73_io.load(path),path.parent)
    Path('results/ci73/verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}),flush=True)
    raise SystemExit(0 if result['status']=='PASS' else 1)

if __name__=='__main__':main()
