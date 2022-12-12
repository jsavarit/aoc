import collections

def p1(f):
    hMap = []
    xS = yS = xE = yE =  0
    for line in f:
        hMap.append(line.strip())
        if 'S' in line: xS, yS = line.find('S'), len(hMap)-1
        if 'E' in line: xE, yE = line.find('E'), len(hMap)-1
    width = len(hMap[0])
    height = len(hMap)
    hMap[yS] = hMap[yS].replace('S', 'a')


    queue = collections.deque([[(xS, yS)]])
    seen = set([(xS, yS)])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if hMap[y][x] == 'E':
            return(len(path)+1)
            break
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                if ord(hMap[y2][x2]) - ord(hMap[y][x]) <= 1:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
    return 0

def p2(f):
    hMap, aCoordMap = [], []
    xS = yS = xE = yE =  0
    for line in f:
        hMap.append(line.strip())
        if 'S' in line: xS, yS = line.find('S'), len(hMap)-1
        if 'E' in line: xE, yE = line.find('E'), len(hMap)-1
    width = len(hMap[0])
    height = len(hMap)
    hMap[yS] = hMap[yS].replace('S', 'a')

    for y in range(len(hMap)):
        for x in range(len(hMap[0])):
            if hMap[y][x] == 'a': aCoordMap.append([x, y])

    pathLength = []
    for aPos in aCoordMap:
        queue = collections.deque([[(aPos[0], aPos[1])]])
        seen = set([(aPos[0], aPos[1])])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if hMap[y][x] == 'E':
                pathLength.append(len(path)+1)
                break
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                    if ord(hMap[y2][x2]) - ord(hMap[y][x]) <= 1:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))


    return min(pathLength)