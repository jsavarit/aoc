def cycleUp(cycle, reg, result, picture):
    if (cycle%40 in [reg-1,reg,reg+1]): picture += '\u2588'
    else: picture += " "
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]: result += cycle * reg
    return cycle, picture, result

def process(f, draw = False):
    cycle = result = 0
    reg = 1
    picture = ""
    for line in f:
        match line.split():
            case['noop']:
                cycle, picture, result = cycleUp(cycle, reg, result, picture)
            case['addx', value]:
                cycle, picture, result = cycleUp(cycle, reg, result, picture)
                cycle, picture, result = cycleUp(cycle, reg, result, picture)
                reg += int(value)
    if draw:
        print()
        for x in range(len(picture)//40):
            print(picture[40*x:40*(x+1)])
    return result

def p1(f):
    return process(f)

def p2(f):
    process(f, True)