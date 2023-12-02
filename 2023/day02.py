f = open("input/day02.txt").readlines()

RMAX, GMAX, BMAX = 12, 13, 14
p1 = set()
p2 = 0

for i, line in enumerate(f, 1):
    p1.add(i)
    reveals = line.strip().split(": ")[1].split("; ")
    red, green, blue = [], [], []
    for reveal in reveals:
        for color in reveal.split(", "):
            match color.split():
                case [n, "red"]:
                    red.append(int(n))
                    if red[-1] > RMAX: p1.discard(i)
                case [n, "green"]:
                    green.append(int(n))
                    if green[-1] > GMAX: p1.discard(i)
                case [n, "blue"]:
                    blue.append(int(n))
                    if blue[-1] > BMAX: p1.discard(i)
    p2 += max(red) * max(green) * max(blue)

print(sum(p1))
print(p2)