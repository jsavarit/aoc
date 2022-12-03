def getCharValue(common):
    value = 0
    if (ord(common) > ord('Z')):
        value += ord(common) - ord('a') + 1
    else:
        value += ord(common) - ord('A') + 27
    return value

def p1(f):
    prio_sum = 0
    for line in f:
        lhs, rhs = line[:len(line)//2], line[len(line)//2:]
        common = ''.join(set(lhs).intersection(rhs))
        prio_sum += getCharValue(common)
    return prio_sum

def p2(f):
    result = 0
    index = 0
    linegroup = set()
    for line in f:
        linegroup.add(line.strip())
        if (index % 3) == 2:
            common = set.intersection(*map(set,linegroup))
            common = str(next(iter(common)))
            result += getCharValue(common)
            linegroup.clear()
        index += 1
    return result
