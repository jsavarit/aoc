from itertools import product
from collections import defaultdict

f = open("input/day03.txt").read().splitlines()

p1, p2 = 0, 0
X, Y = len(f[0]), len(f)
gears = defaultdict(list)

for y in range(Y):
    number, isValid, star = "", False, (0,0)
    for x in range(X):
        c = f[y][x]
        if c.isnumeric():
            number += f[y][x]
            for dx, dy in product([-1, 0 , 1], [-1, 0, 1]):
                if 0<=x+dx<X and 0<=y+dy<Y:
                    if not f[y+dy][x+dx].isnumeric() and f[y+dy][x+dx]!=".":
                        isValid = True
                        if f[y+dy][x+dx] == "*": star = (x+dx, y+dy)
        if not c.isnumeric() or x == X-1:
            if isValid and len(number)>0:
                p1 += int(number)
                if star != (0,0): gears[star].append(int(number))
            number, isValid, star = "", False, (0,0)

for r in gears:
    if len(gears[r])==2: p2 += gears[r][0] * gears[r][1]

print(p1)
print(p2)