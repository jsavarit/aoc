def preproc(f, param):
    stream = f.read()
    for x in range(len(stream)-param):
        if len(set(stream[x:x+param])) == param:
            return x+param

def p1(f):
    return preproc(f,4)
 
def p2(f):
    return preproc(f,14)