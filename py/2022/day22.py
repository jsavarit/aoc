def p1(f):
    board, moves = f.read().split("\n\n")
    board = board.split("\n")
    moves = moves.strip().replace("R",",R,").replace("L",",L,").split(",")
    DIR = ["Right","Down","Left","Up"]
    xMin = []
    xMax = [len(board[y])-1 for y in range(len(board))]
    for y in range(len(board)):
        for x in range(xMax[y]):
            if board[y][x] == '.' or board[y][x] == '#':
                xMin.append(x)
                break
    yMin, yMax = [], []
    for x in range(max(xMax)):
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
                if DIR[d] == "Right": x2,y2 = x+1 if x<xMax[y] else xMin[y], y
                elif DIR[d] == "Left": x2, y2 = x-1 if x>xMin[y] else xMax[y], y
                elif DIR[d] == "Down": x2, y2 = x,y+1 if y<yMax[x] else yMin[x]
                elif DIR[d] == "Up": x2, y2 = x,y-1 if y>yMin[x] else yMax[x]
                if board[y2][x2] == ".": x, y = x2, y2
                else: break
    return 1000*(y+1)+4*(x+1)+d