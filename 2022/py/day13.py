import json

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a<b: return True
        if b<a: return False
    if isinstance(a, list) and isinstance(b, int): return compare(a, [b])
    if isinstance(a, int) and isinstance(b, list): return compare([a], b)
    if isinstance(a, list) and isinstance(b, list): 
        if len(a) > 0 and len(b) == 0: return False
        if len(a) == 0 and len(b) > 0: return True
        for i in range(min(len(a), len(b))):
            if (compare(a[i],b[i]) == True or compare(a[i],b[i]) == False): return compare(a[i],b[i])
            if i == min(len(a), len(b)) - 1:
                if len(a) > len(b): return False
                if len(a) < len(b): return True

def p1(f):
    result = 0
    input = list(filter(None, f.read().splitlines()))
    for i in range(1, len(input)//2 + 1):
        lhs = json.loads(input[2*i - 2])
        rhs = json.loads(input[2*i - 1])
        if compare(lhs, rhs): result += i
    return result

def p2(f):
    input = list(filter(None, f.read().splitlines()))
    for i in range(len(input)): input[i] = json.loads(input[i])
    input = input + [[[2]], [[6]]]
    for i in range(len(input)):
        sorted = True
        for j in range(len(input)-i-1):
            if not (compare(input[j],input[j+1]) == True):
                input[j], input[j+1] = input[j+1], input[j]
                sorted = False
        if sorted: break
    for i in range(len(input) -1 ):
        if input[i] == [[2]]: div1 = i + 1
        if input[i] == [[6]]: div2 = i + 1
    return div1 * div2
