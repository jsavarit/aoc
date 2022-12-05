def preproc(f, param):
    input = f.read().split("\n\n")
    header = input[0].splitlines()
    instructionList = input[1].splitlines()
    numStacks = int(header[-1][-2])
    crates = [[] for x in range(numStacks)]
    for line in range(len(header)-1):
        for stack in range(numStacks):
            crate = header[line][1+4*stack]
            if (crate != ' '): crates[stack].append(crate)
    for instruction in instructionList:
        instruction = instruction.split(' from ')
        instruction[0] = instruction[0].replace('move ', '')
        numEl = int(instruction[0])
        fromStack = int(instruction[1][0]) - 1
        toStack = int(instruction[1][-1]) - 1
        for x in range(numEl):
            buffer = crates[fromStack][0]
            crates[fromStack].pop(0)
            crates[toStack].insert(x*param, buffer)
    return ''.join([crates[stack][0] for stack in range(len(crates))])
 
def p1(f):
    return preproc(f, 0)
 
def p2(f):
    return preproc(f, 1)