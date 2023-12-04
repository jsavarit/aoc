from collections import defaultdict

f = open("input/day04.txt").read().splitlines()

p1, won = 0, defaultdict(int)

for card, line in enumerate(f, 1):
    lr = line.split(": ")[1].split("| ")
    l, r = set(lr[0].split()), set(lr[1].split())
    score = len(l.intersection(r))
    p1 += int(2 ** (score-1))
    won[card] += 1
    for i in range(card, card+score): won[i+1] += won[card]

print(p1)
print(sum(won.values()))