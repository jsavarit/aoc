from collections import defaultdict

def p1(f):
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

    return findBestScore("AA", vP, 30)