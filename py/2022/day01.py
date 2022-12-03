def preproc(f):
    return [sum(map(int, x.split())) for x in f.read().split("\n\n")]

def p1(f):
    return max(preproc(f))

def p2(f):
    return sum(sorted(preproc(f))[-3:])
