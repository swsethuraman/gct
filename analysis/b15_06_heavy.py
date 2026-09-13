"""One preselected pilot and replay, only after an integrator lease."""
import argparse
import json
import time
from pathlib import Path
from b15_06_geometry import ROOT, OUT, pilot, save
from b15_06_verify import geometry

LEASE=Path('C:/Users/swami/Projects/gct-gpt/Batch15_Launch/native_20260913/LEASES.json')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--rank',type=int,required=True,choices=(1,2,3))
    args=parser.parse_args()
    lease=json.loads(LEASE.read_text(encoding='utf-8'))
    holders=lease.get('holders',[])
    assert '06' in holders, 'B15-06 has no heavy numerical lease'
    selection=json.loads((OUT/'selection.json').read_text())
    cell=next(c for c in selection['selected'] if c['rank']==args.rank)
    r,t=cell['r'],cell['t']
    save(f'lease_used_r{r}_t{t}.json',{'status':'RECORDED','lease_record':lease,
                          'read_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                          'selection_rank':args.rank,'r':r,'t':t})
    pilot(r,t,cell['points'],['GEN','DET','PAD'])
    geometry(r,t)
    save(f'heavy_completion_r{r}_t{t}.json',{'status':'RECORDED','complete':True,
                                 'ended_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})


if __name__=='__main__':main()
