import math
from itertools import chain

def p1(f):
    exLine10 = set()
    exBeacon10 = set()
    exLine2M = set()
    exBeacon2M = set()
    for line in f:
        line = line.strip().replace("x=",",").replace("y=",",").replace(":",",").split(",")
        xS, yS, xB, yB = int(line[1]), int(line[3]), int(line[5]), int(line[-1])
        dist = abs(yS-yB)+abs(xS-xB)
        dY10 = dist - abs(yS-10)
        if dY10>=0:
            for x in range(xS-dY10, xS+dY10+1): exLine10.add(x)
        if yB == 10: exBeacon10.add(xB)
        dY2M = dist - abs(yS-2000000)
        if dY2M>=0:
            for x in range(xS-dY2M, xS+dY2M+1): exLine2M.add(x)
        if yB == 2000000: exBeacon2M.add(xB)
    return len(exLine10-exBeacon10), len(exLine2M-exBeacon2M)

def p2(f):
    xS, yS, xB, yB, dist = [], [], [], [], []
    xyMax = 4000000
    for line in f:
        line = line.strip().replace("x=",",").replace("y=",",").replace(":",",").split(",")
        xS.append(int(line[1]))
        yS.append(int(line[3]))
        xB.append(int(line[5]))
        yB.append(int(line[-1]))
        dist.append(abs(yS[-1]-yB[-1])+abs(xS[-1]-xB[-1]))
    for i in range(len(dist)):
        rPlusOne = dist[i] + 1
        xMin, xMax, yMin, yMax = xS[i] - rPlusOne, xS[i] + rPlusOne, yS[i] - rPlusOne, yS[i] + rPlusOne
        for x, y in zip(chain(range(xMin,xMax),range(xMax,xMin,-1)), chain(range(yS[i],yMax),range(yMax,yMin,-1),range(-yMin,yS[i]))):
            isSolution = True
            if not(0<=x<xyMax and 0<=y<xyMax): continue
            for i2 in range(len(dist)):
                if i2 == i: continue
                if (abs(y-yS[i2])+abs(x-xS[i2]))<=dist[i2]:
                    isSolution = False
                    break
            if isSolution: 
                return x*4000000+y
    return 0
