#list_perms.py
import itertools,math,copy
import tsp_functions as tsp

def combinePermutations(perms):
    a = min(min(p) for p in perms)
    b = max(max(p) for p in perms)
    d = {i:i for i in range(a,b+1)}
    for p in perms:
        pairs = zip(sorted(p),p)
        for i,j in pairs:
            d[i] = j
    return tuple(d[i] for i in range(a,b+1))

def permute(cell):
    return [p for p in itertools.permutations(cell)]

def getAllPerms(cells):
    return itertools.product(*(permute(cell) for cell in cells))

def listGoodPerms(cells):
    products = getAllPerms(cells)
    return [perms for perms in products]

def distance(p1,p2):
    try:
        return math.sqrt(((p1[0]-p2[1])**2) + ((p1[1]-p2[1])**2))
    except Exception as e:
        print((p1,p2))
        raise e

def find_shortest(perms):
    t = []
    for path in perms:
        t.append([tsp.path_distance(path),path])
    t.sort(key=lambda x:x[0])
    return t[0][1]
coords = tsp.generate_points(15,50)

perms = listGoodPerms(coords)

print(tsp.path_distance(find_shortest(perms)))
