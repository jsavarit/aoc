def solve(f,reverse=False):
    data, toCompute, isIn, cp = {}, set(), {}, {"+":"-", "-":"+", "*":"/", "/":"*"}
    for line in f:
        line = line.strip().split(": ")
        if line[1].isdigit(): data[line[0]] = int(line[1])
        else:
            data[line[0]] = [line[1][0:4],line[1][5:6],line[1][7:]]
            isIn[data[line[0]][0]], isIn[data[line[0]][-1]] = [line[0], 0], [line[0], 1]
            if not reverse or line[0] != "root": toCompute.add(line[0])

    if reverse:
        n = "humn"
        while True:
            if isIn[n][0] == "root":
                data[n] = [data["root"][-1+isIn[n][1]], "+", "zero"]
                break
            if isIn[n][1] == 0: data[n]=[isIn[n][0],cp[data[isIn[n][0]][1]],data[isIn[n][0]][2]]
            elif data[isIn[n][0]][1] in ["*","+"]: data[n]=[isIn[n][0],cp[data[isIn[n][0]][1]],data[isIn[n][0]][0]]
            else: data[n]=[data[isIn[n][0]][0],data[isIn[n][0]][1],isIn[n][0]]
            n = isIn[n][0]

        data["zero"]=0
        del data["root"]
        toCompute.add("humn")

    search = True
    while search:
        for e in toCompute.copy():
            if isinstance(data[data[e][0]],int) and isinstance(data[data[e][-1]],int):
                data[e] = int(eval(str(data[data[e][0]])+data[e][1]+str(data[data[e][-1]])))
                toCompute.remove(e)
        if not reverse and len(toCompute)==0 or reverse and "humn" not in toCompute: search = False       

    return data["humn"] if reverse else data["root"]

def p1(f):
    return solve(f)

def p2(f):
    return solve(f,True)