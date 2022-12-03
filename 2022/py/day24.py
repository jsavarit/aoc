def mistyValley(f, sillyElf=False):
    valley=f.read().splitlines()
    blz, hdg, DIR = [], [], {'v':(0,-1), '<':(-1,0), '^':(0,1), '>':(1,0)}
    H, W = len(valley)-2, len(valley[0])-2
    for y, line in enumerate(valley[::-1][1:-1]):
        for x, e in enumerate(line[1:-1]):
            if e!='.':
                blz.append((x,y))
                hdg.append(DIR[e])
    pos, time, trip, START, END = {(0,H)}, 0, 0, (0,H), (W-1,-1)
    while True:
        for e, d in enumerate(hdg):
            blz[e] = ((blz[e][0]+d[0])%W,(blz[e][1]+d[1])%H)
        blzMap, new, old = set(blz), set(), trip
        time+=1
        for (px,py) in pos.copy():
            for (dx,dy) in [(0,0)]+list(DIR.values()):
                x, y = px+dx, py+dy
                if old==trip:
                    if (x,y) == END:
                        if not sillyElf or trip == 2: return time
                        if trip == 0: trip=1
                    if (x,y) == START and trip == 1: trip=2
                if 0<=x<W and 0<=y<H:
                    if (x,y) not in blzMap: new.add((x,y))
            if (px,py) not in blzMap: new.add((px,py))
        if old!=trip: pos = {END} if trip==1 else {START}
        else: pos = new

def p1(f):
    return mistyValley(f)

def p2(f):
    return mistyValley(f, True)