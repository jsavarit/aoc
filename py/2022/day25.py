def convert(snafu):
    digits = {'=':-2, '-':-1, '0':0, '1':1, '2':2}
    result, n = 0, 1
    for x in snafu[::-1]:
        result += n*digits[x]
        n*=5
    return result

def encrypt(number):
    digits = {-2:'=', -1:'-', 0:'0', 1:'1', 2:'2'}
    snafu = ""
    while number > 0:
        rest = (number+2)%5-2
        snafu = digits[rest] + snafu
        number = (number-rest)//5
    return snafu

def p1(f):
    result = 0
    for line in f:
        result += convert(line.strip())
    return encrypt(result)