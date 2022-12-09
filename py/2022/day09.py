def moovDatSnaik(f,snaikkSz):
    tailMoves = set()
    x, y = [0] * snaikkSz, [0] * snaikkSz
    for line in f:
        hdg, dist = line.split()
        for _ in range(int(dist)):
            if hdg == 'R': x[0] += 1
            elif hdg == 'L': x[0] -= 1
            elif hdg == 'D': y[0] -= 1
            elif hdg == 'U': y[0] += 1
            for i in range(snaikkSz-1):
                xD = x[i] - x[i+1]
                yD = y[i] - y[i+1]
                if(abs(xD) == 2 and abs(yD) == 1): y[i+1] = y[i]
                if(abs(yD) == 2 and abs(xD) == 1): x[i+1] = x[i]
                x[i+1] += int(xD/2)
                y[i+1] += int(yD/2)
            tailMoves.add((x[-1], y[-1]))
    return len(tailMoves)

def p1(f):
    return moovDatSnaik(f, 2)

def p2(f):
    return moovDatSnaik(f, 10)