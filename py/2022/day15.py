import math

def p1(f):
    exLine10 = set()
    exBeacon10 = set()
    exLine2M = set()
    exBeacon2M = set()
    for line in f:
        match line.strip().replace("x=",",").replace("y=",",").replace(":",",").split(","):
            case ['Sensor at ', xS, ' ', yS, ' closest beacon is at ', xB, ' ', yB]:
                xS, yS, xB, yB = int(xS), int(yS), int(xB), int(yB)
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
    return 0
