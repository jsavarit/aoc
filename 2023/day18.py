f = open("input/day18.txt").read().splitlines()

D = {'U':(0,1),'D':(0,-1),'L':(-1,0),'R':(1,0)}

for p2 in [False, True]:
    x, y, l, e, area = 0, 0, 0, [(0,0)], 0

    for line in f:
        d, s, color = line.split(' ')
        s = int(color[2:-2], 16) if p2 else int(s)
        if p2: d="RDLU"[int(color[-2])]
        x, y, l = x+s*D[d][0], y+s*D[d][1], l+s
        e.append((x,y))

    for i in range(len(e)-1): area += e[i+1][0]*e[i][1] - e[i][0]*e[i+1][1]

    print((area+l)//2+1)
