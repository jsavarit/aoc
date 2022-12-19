DIRECTIONS = ([-1,0,0],[1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1])

def p1(f):
    result = 0
    lava = set()
    for line in f: lava.add(tuple(map(int,line.strip().split(','))))
    for e in lava:
        for dx,dy,dz in DIRECTIONS:
            if (e[0]+dx,e[1]+dy,e[2]+dz) not in lava: result+=1
    return result

def p2(f):
    result = 0
    lava = set()
    for line in f: lava.add(tuple(map(int,line.strip().split(','))))
    xMin = min(e[0] for e in lava)
    
    def countNeighbours(xyz):
        count = 0
        for dx,dy,dz in DIRECTIONS:
            if (xyz[0]+dx,xyz[1]+dy,xyz[2]+dz) in lava: count += 1
        return count
    
    for e in lava:
        if e[0] == xMin: start = (e[0]-1,e[1],e[2])

    seen, toVisit = {start}, [start]
    while toVisit:
        e = toVisit.pop(0)
        result+=countNeighbours(e)
        for dx,dy,dz in DIRECTIONS:
            d = (e[0]+dx,e[1]+dy,e[2]+dz)
            if d not in lava and d not in seen:
                if countNeighbours(d)>0 or any(countNeighbours((d[0]+dx,d[1]+dy,d[2]+dz))>0 for dx,dy,dz in DIRECTIONS):
                    toVisit.append(d)
                    seen.add(d)
    return result
