f = open("input/day14.txt").read().splitlines()

X, Y = len(f[0]), len(f)
for y in range(Y): f[y] = [f[y][x] for x in range(X)]

def tilt():
  for x in range(X):
    i=0
    for y in range(Y):
      if f[y][x] == 'O': f[y][x], f[i][x], i = '.', 'O', i+1
      if f[y][x] == '#': i=y+1

def score(f):
  return sum(["".join(f[y]).count('O')*(Y-y) for y in range(Y)])

def asString(f):
  return "".join(["".join(line) for line in f])

history, scores, p1 = [], [], True
for cycle in range(int(1e9)):
  for _ in range(4):
    tilt()
    if p1: print(score(f)); p1=False
    f=[[f[y][x] for y in range(Y)[::-1]] for x in range(X)];
  if asString(f) in history:
    start = history.index(asString(f))
    print(scores[start+(int(1e9)-start)%(cycle-start)-1])
    break
  history.append(asString(f))
  scores.append(score(f))
