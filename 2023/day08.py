from math import lcm

f = open("input/day08.txt").read().split("\n\n")

moves, direction, graph = f[0], {'L':0, 'R':1}, {}

for line in f[1].splitlines(): graph[line[0:3]] = (line[7:10], line[12:15])

def findGoal(node, goal):
    i = 0
    while(not node.endswith(goal)):
        node = graph[node][direction[moves[i%len(moves)]]]
        i += 1
    return i

print(findGoal("AAA", "ZZZ")) # part 1

start = [node for node in graph.keys() if node.endswith('A')]
print(lcm(*[findGoal(node, "Z") for node in start])) # part 2