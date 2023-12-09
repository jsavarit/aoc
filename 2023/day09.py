f = open("input/day09.txt").read().splitlines()

p1, p2 = 0, 0
for line in f:
    D, tmp = [[int(x) for x in line.split()]], 0
    while set(D[-1]) != {0}:
        D.append([(y-x) for x,y in zip(D[-1][:-1], D[-1][1:])])
    p1 += sum([x[-1] for x in D])
    for i in range(len(D)-1): tmp = D[-i-2][0] - tmp
    p2 += tmp
print(p1, p2)