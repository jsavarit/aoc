f = open("input/day16.txt").read().splitlines()

X, Y = len(f[0]), len(f)

D = {'u':(0,-1),'d':(0,1),'l':(-1,0),'r':(1,0)}
R = {'/':{'r':'u','l':'d','u':'r','d':'l'},
     '\\':{'r':'d','l':'u','u':'l','d':'r'}}

starts_p1 = [(-1,0,'r')]
starts_p2 = []
starts_p2.extend([(-1,y,'r') for y in range(Y)])
starts_p2.extend([(X,y,'l') for y in range(Y)])
starts_p2.extend([(x,-1,'d') for x in range(X)])
starts_p2.extend([(x,Y,'u') for x in range(X)])
result = 0
for starts in [starts_p1, starts_p2]:
  for start in starts:
    rays, visited, rayhistory = [start], set(), set()
    while(rays):
      r = rays.pop(0)
      d = r[2]
      x, y = r[0]+D[d][0], r[1]+D[d][1]
      if 0<=x<X and 0<=y<Y and not (x,y,d) in rayhistory:
        visited.add((x,y))
        rayhistory.add((x,y,d))
        c = f[y][x]
        if c == '.': rays.append((x,y,r[2]))
        elif c in ['/', '\\']:
          d = R[c][r[2]]
          rays.append((x, y, d))
        elif c=='-' and d in ['l','r'] or c=='|' and d in ['u','d']:
          rays.append((x, y, d))
        elif c=='-':
          rays.extend([(x,y,'l'),(x,y,'r')])
        elif c=='|':
          rays.extend([(x,y,'u'),(x,y,'d')])
      result = max(result,len(visited))
  print(result)