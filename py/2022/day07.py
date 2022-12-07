from collections import defaultdict

def getSizeDict(f):
    currentDir = []
    sizeDico = defaultdict(int)
    for line in f:
        if line[0:4] == "$ cd":
            dir = line.strip().split(' ')[-1]
            if dir == "..": currentDir.pop()
            elif dir == "/" or currentDir == ["/"]: currentDir.append(dir)
            else: currentDir.append('/'+dir)
        else:
            size = line.strip().split(' ')[0]
            if (size.isnumeric()):
                for x in range(len(currentDir)):
                    sizeDico["".join(currentDir[0:x+1])] += int(size)
    return sizeDico

def p1(f):
    return sum(size for size in getSizeDict(f).values() if size <= 100000)

def p2(f):
    sizesDict = getSizeDict(f)
    diskSize = 70e6
    usedSpace = sizesDict["/"]
    freeSpace = diskSize - usedSpace
    neededSpace = 30e6
    minDeleteSize = neededSpace - freeSpace
    return min(size for size in sizesDict.values() if size >= minDeleteSize)
