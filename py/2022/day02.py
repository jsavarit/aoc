def p1(f):
    score = 0
    for x in f.read().split("\n"):
        data = x.split(" ")
        openent = ord(data[0]) - ord('A') + 1
        me = ord(data[1]) - ord('X') + 1
        score += me
        if openent == me:
            score += 3
        elif (me - openent) == 1 or (me - openent) == -2:
            score += 6
    return score

def p2(f):
    score = 0
    for x in f.read().split("\n"):
        data = x.split(" ")
        openent = ord(data[0]) - ord('A') + 1
        outcome = ord(data[1]) - ord('X') + 1
        lose = 1
        draw = 2
        win = 3

        if outcome == draw:
            score += 3
        elif outcome == win:
            score += 6

        me = 0

        if outcome == lose:
            me = openent - 1
            if me == 0:
                me = 3
        elif outcome == win:
            me = openent + 1
            if me == 4:
                me = 1
        elif outcome == draw:
            me = openent

        score += me

    return score
