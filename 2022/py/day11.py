def processMonkeyness(f, rounds, panic = False):
    mItems, operator, opNum, divTest, mTrue, mFalse, prod = [], [], [], [], [], [], 1
    for line in f:
        match line.strip().replace(' ', ':').replace(',', '').split(':'):
            case ['Starting', 'items', '', *items]:
                mItems.append(list(map(int,items)))
            case ['Operation', '', 'new', '=', 'old', plusOrTimes, number]:
                operator.append(plusOrTimes)
                opNum.append(number)
            case ['Test', '', 'divisible', 'by', num]:
                divTest.append(int(num))
            case ['If', 'true', '', 'throw', 'to', 'monkey', monkey]:
                mTrue.append(int(monkey))
            case ['If', 'false', '', 'throw', 'to', 'monkey', monkey]:
                mFalse.append(int(monkey))
    inspectCnt = [0] * len(mItems)
    for x in divTest: prod *= x
    for round in range(rounds):
        for m in range(len(mItems)):
            for item in mItems[m]:
                inspectCnt[m] += 1
                if opNum[m] == "old":
                    item = item * item % prod
                elif operator[m] == '+':
                    item += int(opNum[m])
                elif operator[m] == '*':
                    item *= int(opNum[m])
                if not panic: item = item//3
                if (item%divTest[m] == 0): 
                    mItems[mTrue[m]].append(item)
                else:
                    mItems[mFalse[m]].append(item)
                mItems[m] = []
    inspectCnt.sort()
    return inspectCnt[-1] * inspectCnt[-2]

def p1(f):
    return processMonkeyness(f, 20)

def p2(f):
    return processMonkeyness(f, 10000, True)