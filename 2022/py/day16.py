from collections import defaultdict
from itertools import combinations

def solve(f, alone=True):
    p = defaultdict(lambda: 1e6)
    vR, vP = {}, set()
    for line in f:
        match line.strip().replace(" ", ";").replace("=", ";").replace(",", "").split(";") :
            case [_, v, _, _, _, rate, _, _, _, _, _, *toValves]:
                if rate != "0": vP.add(v)
                vR[v] = int(rate)
                for toV in toValves: p[v, toV] = 1

    for k in vR:
        for i in vR:
            for j in vR:
                p[i,j] = min(p[i,j], p[i,k] + p[k,j])

    def findBestScore(fromV, leftV, mnLeft):
        bestScore = 0
        for toV in leftV:
            mnLeftV = mnLeft - p[fromV,toV] - 1
            if mnLeftV >= 0:
                bestScore = max(bestScore, vR[toV] * mnLeftV + findBestScore(toV, leftV-{toV}, mnLeftV))
        return bestScore

    if alone: return findBestScore("AA", vP, 30)
    else:
        result = 0
        for N in range(len(vP)//2-1,len(vP)//2+1):
            for vMe in set(combinations(vP, N)):
                result = max(result, findBestScore("AA", set(vMe), 26) + findBestScore("AA", vP-set(vMe), 26))
        return result

def p1(f):
    return solve(f)

def p2(f):
    return solve(f, False)