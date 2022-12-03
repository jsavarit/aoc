def solve(f, flat=True):
    board, moves = f.read().split("\n\n")
    board = board.split("\n")
    moves = moves.strip().replace("R",",R,").replace("L",",L,").split(",")
    DIR = ["Right", "Down", "Left", "Up"]
    xMin, xMax = [], [len(board[y])-1 for y in range(len(board))]
    for y in range(len(board)):
        for x in range(xMax[y]):
            if board[y][x] == '.' or board[y][x] == '#':
                xMin.append(x)
                break
    yMin, yMax = [], []
    for x in range(max(xMax)+1):
        for y in range(len(board)):
            if xMin[y]<=x<=xMax[y]:
                yMin.append(y)
                break
        for y in range(len(board)-1,-1,-1):
            if xMin[y]<=x<=xMax[y]:
                yMax.append(y)
                break
    x, y, d = xMin[0], 0, 0
    for m in moves:
        if m=="L": d = (d-1)%4
        elif m=="R": d = (d+1)%4
        else:
            for _ in range(int(m)):
                d2 = d
                if DIR[d] == "Right":
                    if x<xMax[y]: x2,y2 = x+1, y
                    elif flat: x2,y2 = xMin[y], y
                    elif y<50: x2, y2, d2 = 99, 149-y, 2
                    elif y<100: x2, y2, d2 = y+50, 49, 3
                    elif y<150: x2, y2, d2 = 149, 149-y, 2
                    else: x2, y2, d2 = y-100, 149, 3
                elif DIR[d] == "Down":
                    if y<yMax[x]: x2,y2 = x, y+1
                    elif flat: x2, y2 = x, yMin[x]
                    elif x<50: x2, y2 = x+100, 0
                    elif x<100: x2, y2, d2 = 49, x+100, 2
                    else: x2, y2, d2 = 99, x-50, 2
                elif DIR[d] == "Left":
                    if x>xMin[y]: x2,y2 = x-1, y
                    elif flat: x2,y2 = xMax[y], y
                    elif y<50: x2, y2, d2 = 0, 149-y, 0
                    elif y<100: x2, y2, d2 = y-50, 100, 1
                    elif y<150: x2, y2, d2 = 50, 149-y, 0
                    else: x2, y2, d2 = y-100, 0, 1
                elif DIR[d] == "Up":
                    if y>yMin[x]: x2,y2 = x, y-1
                    elif flat: x2,y2 = x, yMax[x]
                    elif x<50: x2, y2, d2 = 50, x+50, 0
                    elif x<100: x2, y2, d2 = 0, x+100, 0
                    else: x2, y2 = x-100, 199
                if board[y2][x2] == ".": x, y, d = x2, y2, d2
                else: break
    return 1000*(y+1)+4*(x+1)+d

def p1(f):
    return solve(f)

def p2(f):
    return solve(f, False)