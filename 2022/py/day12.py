import collections

def letsHike(f, fromAnyLowest = False):
    hMap, startMap = [], []
    xS = yS = xE = yE =  0
    for line in f:
        hMap.append(line.strip())
        if 'S' in line: xS, yS = line.find('S'), len(hMap)-1
        if 'E' in line: xE, yE = line.find('E'), len(hMap)-1
    height = len(hMap)
    width = len(hMap[0])
    hMap[yS] = hMap[yS].replace('S', 'a')
    hMap[yE] = hMap[yE].replace('E', '{')

    if fromAnyLowest:
        for y in range(len(hMap)):
            for x in range(len(hMap[0])):
                if hMap[y][x] == 'a': startMap.append([x, y])
    else:
        startMap.append([xS, yS])

    pathLength = []
    for start in startMap:
        queue = collections.deque([[(start[0], start[1])]])
        seen = set([(start[0], start[1])])
        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if hMap[y][x] == '{':
                pathLength.append(len(path)-1)
                break
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < width and 0 <= y2 < height and (x2, y2) not in seen:
                    if ord(hMap[y2][x2]) - ord(hMap[y][x]) <= 1:
                        queue.append(path + [(x2, y2)])
                        seen.add((x2, y2))
    return min(pathLength)

def p1(f):
    return letsHike(f)

def p2(f):
    return letsHike(f, True)
