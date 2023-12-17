f = open("input/day15.txt").read().split(',')

def findHash(block):
  x = 0
  for c in block:
    x+=ord(c)
    x*=17
    x%=256
  return x

p1 = 0
for block in f:
  p1 += findHash(block)
print(p1)

boxes = [[] for x in range(256)]
values = {}
p2 = 0
for b in f:
  if b[-1].isnumeric():
    label = b[0:-2]
    box = findHash(label)
    if not label in boxes[box]: boxes[box].append(label)
    values[label] = int(b[-1])
  else:
    label = b[0:-1]
    box = findHash(label)
    if (label in boxes[box]): boxes[box].pop(boxes[box].index(label))

for b, box in enumerate(boxes,1):
  for i, label in enumerate(box, 1):
    p2 +=b * i * values[label]
print(p2)