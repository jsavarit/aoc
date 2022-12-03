def splitLhsRhs(pairs):
    return list(map(int,pairs[0].split('-'))), list(map(int,pairs[1].split('-')))

def p1(f):
    result = 0
    for line in f:
        lhs, rhs = splitLhsRhs(line.strip().split(','))
        if (lhs[0] <= rhs[1] and lhs[1] >= rhs[1]) or (rhs[0] <= lhs[0] and rhs[1] >= lhs[1]):
            result += 1
    return result

def p2(f):
    result = 0
    for line in f:
        lhs, rhs = splitLhsRhs(line.strip().split(','))
        if not((lhs[1] < rhs[0] or lhs[0] > rhs[1]) and (rhs[0] < lhs[0] or rhs[1] > lhs[1])):
            result += 1
    return result
