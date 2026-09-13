"""Three sequential preselected pilots, only after an integrator lease."""
import json
import time
from pathlib import Path
from b15_06_geometry import ROOT, OUT, pilot, save
from b15_06_verify import geometry

LEASE=Path('C:/Users/swami/Projects/gct-gpt/Batch15_Launch/native_20260913/LEASES.json')


def main():
    lease=json.loads(LEASE.read_text(encoding='utf-8'))
    holders=lease.get('holders',[])
    assert '06' in holders, 'B15-06 has no heavy numerical lease'
    save('lease_used.json',{'status':'RECORDED','lease_record':lease,
                          'read_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
    selection=json.loads((OUT/'selection.json').read_text())
    for cell in selection['selected']:
        r,t=cell['r'],cell['t']
        pilot(r,t,cell['points'],['GEN','DET','PAD'])
        geometry(r,t)
    save('heavy_completion.json',{'status':'RECORDED','complete':True,
                                 'ended_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})


if __name__=='__main__':main()
