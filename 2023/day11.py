f = open("input/day11.txt").read().splitlines()

X, Y, g = len(f[0]), len(f), []

for y in range(Y):
  for x in range(X):
    if f[y][x] == '#': g.append((x,y))

Xempty, Yempty = set(range(X))-set([x[0] for x in g]), set(range(Y))-set([x[1] for x in g])

def measure(expansion):
  l = 0
  for i in range(len(g)):
    for j in range(i, len(g)):
      xi, xj, yi, yj = g[i][0], g[j][0], g[i][1], g[j][1]
      l += abs(xi-xj)+abs(yi-yj)
      l += (expansion-1)*len(set.intersection(Xempty, set(range(min(xi, xj), max(xi, xj)))))
      l += (expansion-1)*len(set.intersection(Yempty, set(range(min(yi, yj), max(yi, yj)))))
  return l

print(measure(2)) # part 1
print(measure(int(1e6))) # part 2