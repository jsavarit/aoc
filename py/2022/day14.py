def cave(f, bottom = False):
    cave = [['.' for _ in range(1000)] for _ in range(1000)]
    path = []
    yMax = 0
    for line in f:
        p = line.strip().split(" -> ")
        path.append([list(map(int, e.split(","))) for e in p])
    for a in path:
        for i in range(len(a) - 1):
            x1, x2, y1, y2 = a[i][0], a[i+1][0], a[i][1], a[i+1][1]
            yMax = max(yMax, y1, y2)
            if (x1 == x2):
                for y in range(min(y1, y2), max(y1, y2)+1): cave[y][x1] = '#'
            else:
                for x in range(min(x1, x2), max(x1, x2)+1): cave[y1][x] = '#'
    iter = 0
    if bottom:
        for x in range(len(cave[0])): cave[yMax+2][x] = "#"
    while True:
        iter += 1
        x, y = 500, 0
        while True:
            if y > yMax+1:
                break
            for x2, y2 in ((x, y+1), (x-1, y+1), (x+1, y+1)):
                if cave[y2][x2] == ".":
                    x, y = x2, y2
                    break
            else:
                cave[y][x] = "o"
                break
        if (x == 500 and y == 0) or (y > yMax + 1): break
    return iter

def p1(f):
    return cave(f)-1

def p2(f):
    return cave(f, True)
