"""Level DP probe: state = (vmask[0..5]) packed; weight = signed sum of paths.
Future parities depend only on masks (depositor term is 0 in static copy order),
so subtree values are path-independent => forward DP is exact.
Copy 0 fixed to diagonal root (x36 at the end). Prints state counts per level."""
import sys, time

DM = [(0,4,8),(0,5,7),(1,3,8),(1,5,6),(2,3,7),(2,4,6)]
DS = [1,-1,-1,1,1,-1]
P6 = [(0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)]

raw = []
for a in range(6):
    for b in range(a+1,6):
        for c in range(b+1,6):
            if (a,b,c) in ((0,1,2),(3,4,5)): continue
            raw.append((a,b,c))
TRI = []
for cls in range(3):
    for t in raw:
        k = 0 if 0 in t else (1 if 1 in t else 2)
        if k == cls: TRI.append(t)
assert len(TRI) == 18 and TRI[0] == (0,1,3)

# options per copy: list of (legs, sign), legs = ((e,v),(e,v),(e,v))
OPT = []
for i in range(18):
    tri = TRI[i]
    opts = []
    for m in range(6):
        for p in P6:
            legs = tuple((tri[k], DM[m][p[k]]) for k in range(3))
            opts.append((legs, DS[m]))
    OPT.append(opts)

LEVEL_CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 18
STATE_CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 3_000_000

def pack(masks): return masks[0] | masks[1]<<9 | masks[2]<<18 | masks[3]<<27 | masks[4]<<36 | masks[5]<<45

# root: copy 0 diagonal option
masks0 = [0]*6
masks0[0] = 1<<0; masks0[1] = 1<<4; masks0[3] = 1<<8
cur = {pack(masks0): 1}
t0 = time.time()
print(f"level 1: states 1  (after fixed root)")

for depth in range(1, LEVEL_CAP):
    nxt = {}
    opts = OPT[depth]
    for key, w in cur.items():
        m = [(key >> (9*e)) & 511 for e in range(6)]
        for legs, sg in opts:
            ok = True
            for e, v in legs:
                if m[e] >> v & 1: ok = False; break
            if not ok: continue
            s = sg
            nk = key
            for e, v in legs:
                me = (nk >> (9*e)) & 511
                if bin(me >> (v+1)).count('1') & 1: s = -s
                nk |= 1 << (9*e + v)
            nw = nxt.get(nk)
            if nw is None: nxt[nk] = w*s
            else:
                nw += w*s
                if nw: nxt[nk] = nw
                else: del nxt[nk]
    cur = nxt
    el = time.time() - t0
    print(f"level {depth+1}: states {len(cur)}  ({el:.0f}s)")
    sys.stdout.flush()
    if len(cur) > STATE_CAP:
        print("STATE CAP EXCEEDED — needs C implementation"); break
    if not cur:
        print("empty layer — VALUE = 0"); break

if len(cur) <= 2 and LEVEL_CAP == 18 and cur:
    (k, w), = cur.items()
    print(f"final weight {w}; VALUE = 36 x {w} = {36*w}")
    print("BIT =", 1 if w != 0 else 0)
