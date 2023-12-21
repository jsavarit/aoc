import bisect

f = open("input/day17.txt").read().splitlines()
X, Y = len(f[0]), len(f)
D = {'u':(0,-1),'r':(1,0),'d':(0,1),'l':(-1,0)}
L, R = dict(zip('urdl','lurd')), dict(zip('urdl','rdlu'))

def minimize(sMin, sMax):
  frontier, visited = sorted([(int(f[0][1]),1,0,'r',1),(int(f[1][0]),0,1,'d',1)]), set()
  while frontier:
    cost, x, y, d, s = frontier.pop(0) # d: last direction, s: steps in that direction
    if s>=sMin and x==X-1 and y==Y-1: return cost
    if (x, y, d, s) in visited: continue
    visited.add((x, y, d, s))
    for d2, s2 in [(L[d],0), (R[d],0), (d, s)]:
      x2, y2, valid = x+D[d2][0], y+D[d2][1], (s2 and s<sMax or not s2 and s>=sMin)
      if 0<=x2<X and 0<=y2<Y and valid and not (x2, y2, d2, s2+1) in visited:
        bisect.insort(frontier,(cost+int(f[y2][x2]), x2, y2, d2, s2+1))

print(minimize(1,3)) # part 1
print(minimize(4,10)) # part 2