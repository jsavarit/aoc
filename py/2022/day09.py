def moovDatSnaik(f,snaikkSz):
    tailMap = [[0, 0]]
    x = [0] * snaikkSz
    y = [0] * snaikkSz
    for line in f:
        move = line.split()
        hdg = move[0]
        dist = int(move[1])
        for a in range(dist):
            if hdg == 'R': x[0] += 1
            elif hdg == 'L': x[0] -= 1
            elif hdg == 'D': y[0] -= 1
            elif hdg == 'U': y[0] += 1
            for i in range(snaikkSz-1):
                xD = x[i] - x[i+1]
                yD = y[i] - y[i+1]
                if(abs(xD) == 2 and abs(yD) == 1): y[i+1] = y[i]
                if(abs(yD) == 2 and abs(xD) == 1): x[i+1] = x[i]
                if(abs(xD) == 2): x[i+1] += xD//2
                if(abs(yD) == 2): y[i+1] += yD//2
            tailMap.append([x[-1], y[-1]])
    uniqueMap = []
    for x in tailMap:
        if x not in uniqueMap: uniqueMap.append(x)
    return len(uniqueMap)

def p1(f):
    return moovDatSnaik(f, 2)

def p2(f):
    return moovDatSnaik(f, 10)
