from copy import deepcopy
import math

f = open("input/day19.txt").read().split("\n\n")

workflows = dict([[line.split('{')[0], [rule for rule in line.split('{')[1][:-1].split(',')]] for line in f[0].splitlines()])
parts = [dict([[value[0], int(value[2:])] for value in line[1:-1].split(',')]) for line in f[1].splitlines()]

def process(part, key='in'):
  while True:
    if key == 'A': return sum(part.values())
    elif key == 'R': return 0
    rules = workflows[key]
    for rule in rules:
      if not ':' in rule: key=rule; break
      elif eval(str(part[rule[0]])+rule.split(':')[0][1:]): key=rule.split(':')[1]; break

print(sum([process(part) for part in parts])) # part 1

def applyRule(rule, rng, isTrue=True):
  c, op, val = rule[0], rule[1], rule[2:]
  if op == '>' and isTrue or op == '<' and not isTrue: rng[c][0] = max(rng[c][0], int(val)+isTrue)
  else: rng[c][1] = min(rng[c][1], int(val)-isTrue)
  return rng

keys, valid = [('in', dict([[c,[1,4000]] for c in 'xmas']))], []
while keys:
  key, ranges = keys.pop(0)
  if key == 'A': valid.append(ranges); continue
  elif key == 'R': continue
  rules = workflows[key]
  for rule in rules:
    if not ':' in rule: keys.append((rule, ranges)); break
    keys.append((rule.split(':')[1], applyRule(rule.split(':')[0], deepcopy(ranges)))) # assume true
    applyRule(rule.split(':')[0], ranges, False) # assume false

print(sum([math.prod([r[1]-r[0]+1 for r in ranges.values()]) for ranges in valid])) # part 2