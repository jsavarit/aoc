def compute(f, qLvl=True):
    OREore, CLAYore, OBSore, OBSclay, GEOore, GEOobs = [], [], [], [], [], []
    for line in f:
        line = line.split(' ')
        OREore.append(int(line[6]))
        CLAYore.append(int(line[12]))
        OBSore.append(int(line[18]))
        OBSclay.append(int(line[21]))
        GEOore.append(int(line[27]))
        GEOobs.append(int(line[30]))
    (N, result, T) = (len(OREore), 0, 24) if qLvl else (3, 1, 32)
    for i in range(N):
        if N>len(OREore): return
        t, state = 0, {(1, 0, 0, 0, 0, 0, 0, 0)}
        hist = set()
        while t<T:
            hist.update(state)
            t, new = t+1, set()
            for x in state:
                (Rore, Rclay, Robs, Rgeo, ore, clay, obs, geo) = x
                if GEOore[i] <= ore and GEOobs[i] <= obs:
                    s = (Rore, Rclay, Robs, Rgeo+1, ore+Rore-GEOore[i], clay+Rclay, obs+Robs-GEOobs[i], geo+Rgeo)
                    new.add(s)
                    continue
                if OBSore[i] <= ore and OBSclay[i] <= clay:
                    if Robs<GEOobs[i]:
                        s = (Rore, Rclay, Robs+1, Rgeo, ore+Rore-OBSore[i], clay+Rclay-OBSclay[i], obs+Robs, geo+Rgeo)
                        if s not in hist: new.add(s)
                        continue
                if CLAYore[i] <= ore:
                    if Rclay<OBSclay[i]:
                        s = (Rore, Rclay+1, Robs, Rgeo, ore+Rore-CLAYore[i], clay+Rclay, obs+Robs, geo+Rgeo)
                        if s not in hist: new.add(s)
                if OREore[i] <= ore:
                    if Rore<max(OREore[i], CLAYore[i], OBSore[i], GEOore[i]):
                        s = (Rore+1, Rclay, Robs, Rgeo, ore+Rore-OREore[i], clay+Rclay, obs+Robs, geo+Rgeo)
                        if s not in hist: new.add(s)
                s = (Rore, Rclay, Robs, Rgeo, ore+Rore, clay+Rclay, obs+Robs, geo+Rgeo)
                if s not in hist: new.add(s)
            state=new
        if qLvl: result += (i+1)*max([x[-1] for x in state])
        else: result *= max([x[-1] for x in state])
    return result

def p1(f):
    return compute(f)

def p2(f):
    return compute(f, False)