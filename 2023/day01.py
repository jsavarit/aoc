f = open("input/day01.txt").readlines()
p1 = 0
for line in f:
    for char in line.strip():
        if char.isdigit(): 
            p1 += 10*int(char);
            break
    for char in line[::-1]:
        if char.isdigit():
            p1 += int(char);
            break
        
print(p1)

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

p2 = 0
for line in f:
    lpos, rpos, lval, rval = 1e9, 0, 0, 0
    for i, digit in enumerate(DIGITS, 1):
        l = line.find(digit)
        r = line.rfind(digit)
        if (l >= 0 and l < lpos): lpos, lval = l, i
        if (r > rpos): rpos, rval = r, i

    for i, char in enumerate(line):
        if char.isdigit() and i<lpos:
            lval = int(char)
            break
    for i, char in reversed(list(enumerate(line))):
        if char.isdigit() and i>=rpos:
            rval = int(char)
            break
    
    p2 += 10*lval + rval

print(p2)