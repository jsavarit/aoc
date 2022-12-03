def dance(f, steps=10):
    grid = f.read().splitlines()
    elves = set()
    moves = [[(0,1),(-1,1),(1,1)], [(0,-1),(-1,-1),(1,-1)], [(-1,0),(-1,-1),(-1,1)], [(1,0),(1,-1),(1,1)]]
    DIR = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
    for y, line in enumerate(grid[::-1]):
        for x in range(len(line)):
            if line[x] == "#": elves.add((x,y))

    step = 0
    while step!=steps:
        moving, walks, duplicates = False, {}, set()
        for elf in elves:
            if not any([(elf[0]+d[0],elf[1]+d[1]) in elves for d in DIR]): continue
            moving = True
            for i in range(len(moves)):
                hdg = moves[(step+i)%len(moves)]
                if not any([(elf[0]+move[0],elf[1]+move[1]) in elves for move in hdg]):
                    goto = (elf[0]+hdg[0][0],elf[1]+hdg[0][1])
                    if goto not in duplicates:
                        if goto not in walks.keys():
                            walks[goto] = elf
                        else:
                            del walks[goto]
                            duplicates.add(goto)
                    break
        if not moving: return step+1
        for goto, origin in walks.items():
            elves.remove(origin)
            elves.add(goto)
        step+=1
    xE, yE = [e[0] for e in elves], [e[1] for e in elves]
    return (max(xE) + 1 - min(xE))*(max(yE) + 1 - min(yE)) - len(elves)

def p1(f):
    return dance(f)

def p2(f):
    return dance(f, -1)