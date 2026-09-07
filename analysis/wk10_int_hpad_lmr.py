import sys, time
sys.path.insert(0,'analysis'); sys.path.insert(0,'/root/work')
from wk9_s42_hpad import pieri_strips
from ple2 import mult
LAM=(65,17,2,2,2,2,2,2,2); D=24
st=pieri_strips(LAM,D)
st=[tuple(x for x in m if x) for m in st]
print("Pieri shapes:", len(st), " lengths:", sorted(set(len(m) for m in st)), flush=True)
tot=0
for i,mu in enumerate(st):
    t=time.time(); v=mult(mu, D, 9, 3); tot+=v
    print("%2d/%d  mu=%-34s a_3=%d   (%.1fs)  running h_pad=%d"%(i+1,len(st),str(mu),v,time.time()-t,tot), flush=True)
print()
print("h_pad(LMR) =", tot)
