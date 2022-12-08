def readForrest(f):
    forrest = []
    for line in f:
        forrestLine = []
        for x in range(len(line)-1):
            forrestLine.append(int(line[x]))
        forrest.append(forrestLine)
    return forrest

def p1(f):
    forrest = readForrest(f)
    forrestDepth = len(forrest)
    forrestWidth = len(forrest[0])
    result = forrestDepth * 2 + (forrestWidth - 2) * 2 #all edges are visible
    for i in range(1, forrestDepth-1):
        for j in range(1, forrestWidth-1):
            isVisible = False
            if forrest[i][j] > max(forrest[i][0:j]): isVisible |= True
            if forrest[i][j] > max(forrest[i][j+1:forrestWidth]): isVisible |= True
            maxFromTop = 0
            for x in range(0,i):
                maxFromTop = max(maxFromTop, forrest[x][j])
            if forrest[i][j] > maxFromTop: isVisible |= True
            maxFromBottom = 0
            for x in range(i+1,forrestDepth):
                maxFromBottom = max(maxFromBottom, forrest[x][j])
            if forrest[i][j] > maxFromBottom: isVisible |= True
            
            if isVisible: result += 1
    return result

def p2(f):
    forrest = readForrest(f)
    result = 0
    forrestDepth = len(forrest)
    forrestWidth = len(forrest[0])
    for i in range(1, forrestDepth-1):
        for j in range(1, forrestWidth-1):
            for x in range(j+1, forrestWidth):
                rightScore = abs(x-j)
                if forrest[i][x] >= forrest[i][j]: break
            for x in range(j-1, -1, -1):
                leftScore = abs(x-j)
                if forrest[i][x] >= forrest[i][j]: break
            for x in range(i-1, -1, -1):
                bottomScore = abs(x-i)
                if forrest[x][j] >= forrest[i][j]: break
            for x in range(i+1, forrestDepth):
                topScore = abs(x-i)
                if forrest[x][j] >= forrest[i][j]: break
            result = max(result, leftScore * rightScore * topScore * bottomScore)
    return result
