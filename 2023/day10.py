from collections import defaultdict

f = open("input/day10.txt").read().splitlines()

X, Y, graph, start = len(f[0]), len(f), defaultdict(list), (0,0)

C = {'|':['N','S'], '-':['W','E'], 'L':['N','E'],
     'J':['N','W'], '7':['W','S'], 'F':['S','E'],
     '.':[], 'S':['N','S','W','E'] }
D = {'N':(0,-1,'S'),'S':(0,1,'N'),'W':(-1,0,'E'),'E':(1,0,'W')}

for y in range(Y):
  for x in range(X):
    if f[y][x] == 'S': start = (x, y)
    for d in C[f[y][x]]:
      x2, y2 = x+D[d][0], y+D[d][1]
      if 0<=x2<X and 0<=y2<Y:
        if D[d][2] in C[f[y2][x2]]: graph[(x,y)].append((x2,y2))

frontier, distance = [start], {start:0}
while(frontier):
  node = frontier.pop(0)
  for neighbor in graph[node]:
    if neighbor not in distance.keys():
      distance[neighbor] = distance[node] + 1
      frontier.append(neighbor)

print(max(distance.values())) # part 1

for p in C.keys():
  if sorted([D[d][0:2] for d in C[p]]) == sorted([(x-start[0],y-start[1]) for x,y in graph[start]]):
    f[start[1]] = f[start[1]].replace('S', p)

p2 = 0
for y in range(Y):
  tmp = 0
  for x in range(X):
    if (x,y) in distance.keys():
      if 'N' in C[f[y][x]]: tmp+=1
    elif tmp%2==1: p2+=1
print(p2)