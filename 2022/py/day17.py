def rockNroll(f, N):
    jet = f.read()
    shapes = [[[0,1,2,3], [0,0,0,0]], [[1,0,1,2,1], [0,1,1,1,2]],
              [[0,1,2,2,2], [0,0,0,1,2]], [[0,0,0,0], [0,1,2,3]], [[0,1,0,1], [0,0,1,1]]]
    width, height, step, dH, rocks = 7, 0, 0, [], set()
    for rock in range(N):
        sx, sy = shapes[rock%len(shapes)]
        x, y = 2, height+3
        while True:
            j = 1 if jet[step%len(jet)] == ">" else -1
            if j==1 and x+max(sx)<(width-1) or j==-1 and x>0:
                if all((x+dx+j,y+dy) not in rocks for dx,dy in zip(sx,sy)): x += j
            step += 1
            if y>0 and all((x+dx,y+dy-1) not in rocks for dx,dy in zip(sx,sy)): y -=1
            else:
                for dx, dy in zip(sx, sy): rocks.add((x+dx,y+dy))
                dH.append(max(height,y+max(sy)+1)-height)
                height = max(height,y+max(sy)+1)
                break
        if (rock+1)%3 == 0:
            i = (rock+1)//3
            if i>5 and dH[i:2*i] == dH[2*i:3*i]: return sum(dH[:i])+(N-i)//i*sum(dH[i:2*i])+sum(dH[i:(N%i+i)])
    return height

def p1(f):
    return rockNroll(f,2022)

def p2(f):
    return rockNroll(f,1000000000000)