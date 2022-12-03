def decrypt(f,cypher=1,repeat=1):
    dF = list(map(lambda x:cypher*int(x),f.read().splitlines()))
    size = len(dF)
    dF = [dF,list(range(size))]
    for _ in range(repeat):
        for i in range(size):
            x = dF[1].index(i)
            e = dF[0].pop(x)
            dF[1].pop(x)
            dF[0].insert((x+e)%(size-1),e)
            dF[1].insert((x+e)%(size-1),i)
    return sum([dF[0][(dF[0].index(0)+d)%size] for d in [1000,2000,3000]])

def p1(f):
    return decrypt(f)

def p2(f):
    return decrypt(f,811589153,10)
