f = open("input/day01.txt").readlines()
p1 = 0
for line in f:
    for char in line:
        if char.isdigit(): 
            p1 += 10*int(char);
            break
    for char in line[::-1]:
        if char.isdigit():
            p1 += int(char);
            break
        
print(p1)

DIGITS = "one 1 two 2 three 3 four 4 five 5 six 6 seven 7 eight 8 nine 9".split()
INF = 1e9

p2 = 0
for line in f:
    lpos, rpos, lval, rval = INF, -INF, 0, 0
    for i, digit in enumerate(DIGITS, 1):
        i = (i+1) // 2
        l, r = line.find(digit), line.rfind(digit)
        if (l >= 0 and l < lpos): lpos, lval = l, i
        if (r > rpos): rpos, rval = r, i

    p2 += 10*lval + rval

print(p2)