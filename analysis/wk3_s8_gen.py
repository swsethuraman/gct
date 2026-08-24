"""Generate HWV scheme files for weight (8,8,8,6^6) = six eps_9 + two eps_3 columns.
Copies: 20 distinct triples over symbols {0..5}=eps9, {6,7}=eps3(top-3 vars);
cover: 9 per eps9, 3 per eps3. Copy order: early eps-completion passes."""
import itertools, os
os.makedirs('evalin', exist_ok=True)

DET = [(1,(0,4,8)), (-1,(0,5,7)), (-1,(1,3,8)), (1,(1,5,6)), (1,(2,3,7)), (-1,(2,4,6))]
ALL20 = [t for t in itertools.combinations(range(6), 3)]

def check_and_order(shorts, removed, name):
    pure = [t for t in ALL20 if t not in removed]
    assert len(pure) == 14, (name, len(pure))
    # cover checks
    for s in range(6):
        c = sum(1 for t in pure if s in t) + sum(1 for t in shorts if s in t)
        assert c == 9, (name, s, c)
    for e in (6, 7):
        assert sum(1 for t in shorts if e in t) == 3
    tris = shorts + pure
    assert len(set(tris)) == 20
    # order: passes by lowest new symbol; shorts first within a pass
    ordered, used = [], set()
    for sym in range(8):
        batch = [t for t in tris if t not in used and sym in t]
        batch.sort(key=lambda t: (0 if (6 in t or 7 in t) else 1, t))
        for t in batch:
            ordered.append(t); used.add(t)
    assert len(ordered) == 20
    with open(f'evalin/{name}', 'w') as f:
        f.write("9 8 20 3\n")
        f.write("9 9 9 9 9 9 3 3\n")
        for t in ordered: f.write(" ".join(map(str, t)) + "\n")
        f.write(f"{len(DET)}\n")
        for c, vs in DET:
            f.write(f"{c} " + " ".join(map(str, vs)) + "\n")
        f.write("-1 1\n")
    print(name, "ok; order:", ordered[:6], "...")

check_and_order(
    [(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)],
    {(0,1,2),(3,4,5),(0,1,3),(2,4,5),(0,2,4),(1,3,5)},
    'hwv1.txt')
check_and_order(
    [(0,3,6),(1,4,6),(2,5,6),(0,4,7),(1,5,7),(2,3,7)],
    {(0,1,2),(3,4,5),(0,1,4),(2,3,5),(0,2,5),(1,3,4)},
    'hwv2.txt')
check_and_order(
    [(0,1,6),(2,3,6),(4,5,6),(0,2,7),(1,4,7),(3,5,7)],
    {(0,1,3),(2,4,5),(0,1,4),(2,3,5),(0,1,5),(2,3,4)},
    'hwv3.txt')
