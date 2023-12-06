f = open("input/day06.txt").read().splitlines()

time = [int(x) for x in f[0].split(":")[1].split()]
dist = [int(x) for x in f[1].split(":")[1].split()]
p1 = 1

for i in range(len(time)):
    n = 0
    for t in range(time[i]):
        if (t*(time[i]-t)) > dist[i]: n+=1
    p1 *= n

print(p1)

time = int("".join([str(x) for x in time]))
dist = int("".join([str(x) for x in dist]))
p2=0
for t in range(time):
    if (t*(time-t)) > dist: p2+=1
print(p2)